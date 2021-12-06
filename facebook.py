import torch
import librosa
import nltk
import numpy as np
import soundfile as sf
from scipy.io import wavfile
from IPython.display import Audio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')


def Speech_to_text_Wave2vec (file_name):
    """[summary]

    Args:
        file_name ([path or audio file]): [audio file extract from video]
        
        returns :
        text ([string]) : text after processing the audio
    """
    #download the model pre-trained by facebook
    tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    #extraction of the model from the library wave2vec
    FB_model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    #Audio(file_name)
    #loading audio file and check sample rate and total time
    data = wavfile.read(file_name)
    framerate = data[0]
    sounddata = data[1]
    time = np.arange(0,len(sounddata))/framerate
    print('Sampling rate:',framerate,'Hz')
    #the librosa library loads the audio sample with a sample rate=16000 Hz as Facebook’s model accepts the sampling rate at this range
    input_audio, _ = librosa.load(file_name, sr=16000)
    input_values = tokenizer(input_audio, return_tensors="pt").input_values
    #create the inputs for the speech model
    logits = FB_model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    text = tokenizer.batch_decode(predicted_ids)[0]
    return(text)



def from_text_keywords_extraction(Text_ready_for_keywords_extraction):
    """[summary]

    Args:
        Text_ready_for_keywords_extraction ([string]): [text ready for keywords extraction]

    Returns:
        [list]: [list of keyword extracted and filted using stopwords from nltk.corpus ]
    """
    #tokenize the text into words
    tokenized_word=word_tokenize(Text_ready_for_keywords_extraction.lower())
    #print(tokenized_word)
    #filter the text from stopwords
    stop_words=set(stopwords.words("english"))
    filtered_word=[]
    for w in tokenized_word:
        if w not in stop_words:
            filtered_word.append(w)
    print("Filterd words without stopwords:",filtered_word)

    #frequency distribution map each sample to the number of times that sample occurred as an outcome.
    fdist = FreqDist(filtered_word)
    return fdist



