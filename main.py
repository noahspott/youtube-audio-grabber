from pytube import YouTube

print("Hello world")

# Get youtube URL from user input
url = input("Enter the YouTube URL: ")

# create a youtube object
youtube = YouTube(url);

# get the audio stream
audio_stream = youtube.streams.filter(only_audio=True).first()

# download the audio file
audio_stream.download(output_path='/audio', filename_prefix='audio-')
print("Audio file downloaded successfully!");