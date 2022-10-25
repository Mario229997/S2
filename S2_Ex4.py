import subprocess

# Convert stereo to mono
audio_stereo = 'Audios_Ex4/horse_stereo.wav'
output_name = 'Audios_Ex4/horse_mono.wav'
subprocess.run('ffmpeg -i '+audio_stereo+' -ac 1 '+output_name+'', shell=True)

# Convert mono to stereo
audio_mono = 'Audios_Ex4/trumpet_mono.wav'
output_name = 'Audios_Ex4/trumpet_stereo.wav'
subprocess.run('ffmpeg -i '+audio_mono+' -ac 2 '+output_name+'', shell=True)
