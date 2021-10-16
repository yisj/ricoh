from moviepy.editor import *
clip = VideoFileClip("R0010228.MP4")
c = clip.subclip(120, clip.duration)
c.write_videofile("YOUTUBE-R0010228.MP4")