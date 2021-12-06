import subprocess
import boto3
import json 
import ffmpeg
from moviepy.editor import VideoFileClip, AudioClip
from pytube import YouTube
import numpy as np
import cv2
import facebook as fb
import aws_transcribe as aws
import twitter as twt

from PIL import Image, ImageFont, ImageDraw 
import requests




# link to the youtube video/streaming
url = 'https://youtu.be/MREj5r4K-ik'
subprocess.call(url, shell=True)


#get audio  from video download


com = 'ffmpeg -i Guillaume\ Neau-MREj5r4K-ik.webm -ab 160k -ar 44100 -ss 00:00:5.00 -t 00:00:12.00 -vn audio_output.wav'
subprocess.call(com, shell=True)
#subprocess.call('ffmpeg -i Guillaume\ Neau-MREj5r4K-ik.webm -f image2 -frames:v 1 -y 1 -vf fps=1/10 -strftime 1 "./images/%Y-%m-%d_%H-%M-%S.jpg"', shell=True)




#  AWS TRNSCRIPE SPEECH TO TEXT
file_uri = 's3://iotmeetcyber/audio_output.wav'
transcribe_client = boto3.client('transcribe', aws_access_key_id = 'AKIAZ7YUVFJIRC33G76V', aws_secret_access_key ='3hoFkjX7Kiw2CzmVtbq7iN6aWu48aaWIbd9v2KjP')
text = aws.transcribe_file('Example-job', file_uri, transcribe_client)

comprehend = boto3.client(service_name='comprehend')


res = json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
print('Calling DetectKeyPhrases')
print(res)
print('End of DetectKeyPhrases\n')

result = json.loads(res)

key_lst =[]
for i in result["KeyPhrases"]:
    keywords = i["Text"]
    #print(keywords)
    key_lst.append(keywords)
    print(key_lst)


#frequency distribution map each sample to the number of times that sample occurred as an outcome.
fdist_aws = FreqDist(key_lst)
#     print(fdist)
#     fdist.most_common(2)
print("you can see also the distribution and frequency of your keywords!")





#  FB NLP=> Speech to text 

comprehend = boto3.client(service_name='comprehend', region_name='region')
                
#text = "It is raining today in Seattle"

print('Calling DetectKeyPhrases')
print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
print('End of DetectKeyPhrases\n')




#######
#  SAVE AN IMAGE BEFORE INSERT THE KEYWORDS


#Add text to an image (Keyword on screenshot)
def add_text(path_image, txt): 
    """[summary]

    Args:
        path_image ([string]): [path of images and images]
        txt ([string]): [text to insert on the image]
    """
    original = Image.open(path_image)
    my_image = Image.open(path_image)
    images = []
    title_font = ImageFont.truetype('Lato-Bold.ttf', int(4000/(len(txt)+1)))
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((15,15), txt, (255, 100, 100), font=title_font)
    my_image.save("result.jpg")
    images.append(original)
    images.append(my_image)

    images[0].save('out.gif', save_all=True, append_images=[my_image,original], optimize=False, duration=500, loop=0)



add_text("a.jpg","#Blockchain technology !")









