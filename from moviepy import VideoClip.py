from moviepy import VideoClip
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
import random
import math

# =========================
# CONFIGURAÇÕES DO VÍDEO
# =========================
W, H = 720, 1280
FPS = 30
DURACAO = 8

random.seed(42)

# =========================
# CARREGA O PERSONAGEM
# =========================
personagem = Image.open("gojo.png").convert("RGBA")
personagem.thumbnail((300, 500))

# =========================
# FUNDO DA CIDADE
# =========================
def criar_fundo():
    img = Image.new("RGB", (W, H), (8, 10, 25))
    draw = ImageDraw.Draw(img)

    # Prédios
    for x in range(-20, W, 90):
        altura = random.randint(400, 850)
        largura = random.randint(60, 100)
        y = H - altura

        draw.rectangle(
            [x, y, x + largura, H],
            fill=(15, 18, 38)
        )

        # Janelas
        for wy in range(y + 30, H - 20, 45):
            for wx in range(x + 15, x + largura - 10, 30):
                if random.random() > 0.35:
                    draw.rectangle(
                        [wx, wy, wx + 8, wy + 14],
                        fill=(70, 95, 150)
                    )

    return img


FUNDO = criar_fundo()

# =========================
# PARTÍCULAS
# =========================
particulas = []

for _ in range(100):
    particulas.append({
        "x": random.randint(0, W),
        "y": random.randint(0, H),
        "vel": random.randint(8, 25),
        "tamanho": random.randint(2, 6)
    })


# =========================
# FONTE
# =========================
try:
    fonte = ImageFont.truetype("arial.ttf", 50)
except:
    fonte = ImageFont.load_default()


# =========================
# GERA CADA FRAME
# =========================
def gerar_frame(t):

    frame = FUNDO.copy().convert("RGBA")

    # Quanto mais tempo passa, maior fica a aura
    progresso = min(t / DURACAO, 1)
    aura_intensidade = progresso ** 1.5

    # =========================
    # EFEITO DE MOVIMENTO
    # =========================
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Linhas de velocidade
    for _ in range(35):
        x = random.randint(0, W)
        y = random.randint(0, H)

        comprimento = random.randint(40, 180)

        draw.line(
            [(x, y), (x, y + comprimento)],
            fill=(90, 150, 255, 100),
            width=2
        )

    frame = Image.alpha_composite(frame, overlay)

    # =========================
    # POSIÇÃO DO PERSONAGEM
    # =========================
    # Cai do topo para perto da parte inferior
    y = int(-100 + progresso * (H * 0.65))
    x = W // 2 - personagem.width // 2

    # =========================
    # AURA
    # =========================
    aura = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    aura_draw = ImageDraw.Draw(aura)

    centro_x = W // 2
    centro_y = y + personagem.height // 2

    # Pulsação da aura
    pulso = math.sin(t * 8) * 15
    raio = int(170 + aura_intensidade * 180 + pulso)

    # Vários círculos para criar brilho
    for r in range(raio, 30, -15):

        alpha = int(
            8 + 35 * aura_intensidade *
            (1 - r / max(raio, 1))
        )

        aura_draw.ellipse(
            [
                centro_x - r,
                centro_y - r,
                centro_x + r,
                centro_y + r
            ],
            outline=(80, 150, 255, alpha),
            width=10
        )

    aura = aura.filter(ImageFilter.GaussianBlur(12))
    frame = Image.alpha_composite(frame, aura)

    # =========================
    # ENERGIA AO REDOR
    # =========================
    energia = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    energia_draw = ImageDraw.Draw(energia)

    quantidade = int(20 + progresso * 80)

    for _ in range(quantidade):

        angulo = random.uniform(0, math.pi * 2)
        distancia = random.randint(70, raio)

        px = centro_x + math.cos(angulo) * distancia
        py = centro_y + math.sin(angulo) * distancia

        tamanho = random.randint(3, 10)

        energia_draw.ellipse(
            [
                px - tamanho,
                py - tamanho,
                px + tamanho,
                py + tamanho
            ],
            fill=(120, 190, 255, random.randint(80, 220))
        )

    energia = energia.filter(ImageFilter.GaussianBlur(2))
    frame = Image.alpha_composite(frame, energia)

    # =========================
    # PARTICULAS DE QUEDA
    # =========================
    part_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    part_draw = ImageDraw.Draw(part_layer)

    for p in particulas:

        py = (p["y"] + t * p["vel"] * 8) % H
        px = p["x"]

        part_draw.line(
            [(px, py), (px, py + 25)],
            fill=(170, 210, 255, 140),
            width=p["tamanho"]
        )

    frame = Image.alpha_composite(frame, part_layer)

    # =========================
    # PERSONAGEM
    # =========================
    frame.alpha_composite(personagem, (x, y))

    # =========================
    # TEXTO DE AURA
    # =========================
    texto = f"AURA +{int(progresso * 999)}"

    text_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_layer)

    bbox = text_draw.textbbox((0, 0), texto, font=fonte)
    tw = bbox[2] - bbox[0]

    text_draw.text(
        ((W - tw) / 2, 80),
        texto,
        font=fonte,
        fill=(180, 220, 255, 255),
        stroke_width=3,
        stroke_fill=(40, 70, 150, 255)
    )

    frame = Image.alpha_composite(frame, text_layer)

    # =========================
    # FLASH NO FINAL
    # =========================
    if progresso > 0.9:

        intensidade = int(
            ((progresso - 0.9) / 0.1) * 120
        )

        flash = Image.new(
            "RGBA",
            (W, H),
            (180, 220, 255, intensidade)
        )

        frame = Image.alpha_composite(frame, flash)

    return np.array(frame.convert("RGB"))


# =========================
# CRIA O VÍDEO
# =========================
video = VideoClip(
    frame_function=gerar_frame,
    duration=DURACAO
)

video.write_videofile(
    "gojo_farmando_aura.mp4",
    fps=FPS,
    codec="libx264",
    audio=False
)

print("Vídeo criado: gojo_farmando_aura.mp4")