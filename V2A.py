import sys
import pytube.exceptions
from pytube import YouTube

#Example video: https://www.youtube.com/watch?v=9Gbzk-cA4sE

#Checks if video is valid
def try_url(url):
    try: 
        yt = YouTube(url)
        return url
    except pytube.exceptions.VideoUnavailable:
        return ""

#Check if a link has been passed as arg 1
try:
    link = sys.argv[1]
except IndexError:
    link = ""

#Want it to try once, if invalid it enters the loop
try_url(link)

#Loop until valid link is given
while link == "":
    link = input("\nPlease enter a valid YouTube link for processing: ")
    try_url(link)
    
print("\nDownloading: " + link + "\n")

my_audio = YouTube(link).streams.get_audio_only()
my_audio.download()

print("File Location: " + my_audio.download())



