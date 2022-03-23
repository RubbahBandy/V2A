import os
import sys
import moviepy

file_in

try:
    file_in = sys.argv[1]
except IndexError:
    file_in = ""

while file_in == "":
    print("\nEnter an mp4 file to be converted: \n")
    file_in = input()

print("\nEnter a name for the outgoing mp3 file: \n")
file_out = input()

mp4 = VideoFileClip(file_in)
mp3 = mp4.audio
mp3.write_audiofile(file_out)
mp3.close()
mp4.close()



