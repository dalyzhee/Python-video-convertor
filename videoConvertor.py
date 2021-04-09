import moviepy.editor as mp
video_name = input("Enter video name plus video format(mp4): ")
audio_name = input("Enter audio name plus format(mp3): ")
clip = mp.VideoFileClip(video_name)
clip.audio.write_audiofile(audio_name)
