from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

N = 11
start_time = 50
end_time = 61
ffmpeg_extract_subclip("BBB.mp4", start_time, end_time, targetname="BBB_11.mp4")


# I made an alternative solution using subprocess to call ffmpeg
'''import subprocess

input_video = 'BBB.mp4'
output_video = 'BBB_11.mp4'
subprocess.run('ffmpeg -ss 00:00:50 -to 00:01:01 -i '+input_video+' -c copy '+output_video+'', shell=True)
'''