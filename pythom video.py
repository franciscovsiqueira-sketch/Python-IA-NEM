("function pythonvideo.py")

from moviepy.editor import ColorClip, TextClip, CompositeVideoClip

video = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=3)
text = TextClip("Olá, mundo!", fontsize=70, color='white', font='DejaVu-Sans')
text = text.set_position('center').set_duration(3)

final = CompositeVideoClip([video, text])
final.write_videofile("video.mp4", fps=24)













