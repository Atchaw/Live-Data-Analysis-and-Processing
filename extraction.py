import time
import os
import json
import requests
#from pyserved.server import send_file


key = "AIzaSyBfKp8gxf20J71_5njElmtO7-PpZjVOKjM"
channel = "UCLA_DiR1FfKNvjuUpBHmylQ"

url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&type=video&eventType=live&key={}".format(channel,key)
r =requests.get(url)
json_info = r.text
y = json.loads(json_info)


#test if the vid is live
#is_live = y["items"][0]["snippet"]["liveBroadcastContent"] == "live"


starttime = time.time()

url = "https://www.youtube.com/watch\?v\=21X5lGlDOfg"
i = 0
while (y["items"][0]["snippet"]["liveBroadcastContent"] == "live"):
    i = i+1
    print ("vedio {}".format(i))
    os.system('ffmpeg -ss 00:00:5.00 -i $(youtube-dl -f 94 -g {}) -t 00:00:30.00 -c copy video_{}.mp4'.format(url, i))
    os.system('ffmpeg -i video_{}.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 audio_output_{}.wav'.format(i, i))
    os.system('ffmpeg -i video_{}.mp4 -ss 00:00:29 -frames:v 1 img_{}.jpeg'.format(i, i))
    #send_file('video_{}.mp4'.format(i), '192.168.252.11', 2021)
    #send_file('audio_output_{}.wav'.format(i), '192.168.252.11', 2021)
    #send_file('img_{}.jpeg'.format(i), '192.168.252.11', 2021)
    #time.sleep(60.0 - ((time.time() - starttime) % 60.0))
    #os.remove('video_{}.mp4'.format(i))
    #os.remove('audio_output_{}.wav'.format(i))
    #os.remove('img_{}.jpeg'.format(i))