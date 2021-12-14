import time
import os
import json
import requests


key = "put your Google Youtube API here"
channel = "UCLA_DiR1FfKNvjuUpBHmylQ" # NASA channel, you can change it to what you want!

# request the html information about the live stream to test if the video is still live or not.
url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&type=video&eventType=live&key={}".format(channel,key)
r =requests.get(url)
json_info = r.text
y = json.loads(json_info)

# the url of the live stream.
url = "https://www.youtube.com/watch\?v\=21X5lGlDOfg"
i = 0

# this code will continue to run until the live stream is stopped.
while (y["items"][0]["snippet"]["liveBroadcastContent"] == "live"):
    i = i+1
    print ("vedio {}".format(i))
    # get the video using ffmpeg ss: starting second, t:stops writing the output after the duration provided
    # so because this t, The code is repeated every t time
    os.system('ffmpeg -ss 00:00:5.00 -i $(youtube-dl -f 94 -g {}) -t 00:00:30.00 -c copy video_{}.mp4'.format(url, i))
    # extract the audio feom the video
    os.system('ffmpeg -i video_{}.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 audio_output_{}.wav'.format(i, i))
    # get a screenshot in the second 30 of viedo 
    # you can edit it by changing the value of ss
    os.system('ffmpeg -i video_{}.mp4 -ss 00:00:29 -frames:v 1 img_{}.jpeg'.format(i, i))
    
    # if you want to remove the video, audio and image after using them by the other part of the code
    #os.remove('video_{}.mp4'.format(i))
    #os.remove('audio_output_{}.wav'.format(i))
    #os.remove('img_{}.jpeg'.format(i))
