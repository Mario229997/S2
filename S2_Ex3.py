import moviepy.editor as mp

# Video resized to 720p
clip = mp.VideoFileClip("BBB_11.mp4")
clip_resized = clip.resize(height=720)
clip_resized.write_videofile("Videos_Ex3/BBB_720.mp4")

# Video resized to 480p
clip = mp.VideoFileClip("BBB_11.mp4")
clip_resized = clip.resize(height=480)
clip_resized.write_videofile("Videos_Ex3/BBB_480.mp4")

# Video resized to 360x240
clip = mp.VideoFileClip("BBB_11.mp4")
clip_resized = clip.resize(newsize=(360, 240))
clip_resized.write_videofile("Videos_Ex3/BBB_360x240.mp4")

# Video resized to 160x120
clip = mp.VideoFileClip("BBB_11.mp4")
clip_resized = clip.resize(newsize=(160, 120))
clip_resized.write_videofile("Videos_Ex3/BBB_160x120.mp4")
