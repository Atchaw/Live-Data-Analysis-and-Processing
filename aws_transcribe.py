# AWS
import boto3
import time
import urllib
import json 


#  AWS TRNSCRIPE SPEECH TO TEXT

def transcribe_file(job_name, file_uri, transcribe_client):
    """[summary]

    Args:
        job_name ([string]): [the aws job]
        file_uri ([string]): [file URI defined (audio file)]
        transcribe_client ([type]): [client transcription]

    Returns:
        [strings]: [text transcription obatin from audio files]
    """
    transcribe_client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        LanguageCode='en-US'
    )

    max_tries = 60
    while max_tries > 0:
        max_tries -= 1
        job = transcribe_client.get_transcription_job(TranscriptionJobName=job_name)
        job_status = job['TranscriptionJob']['TranscriptionJobStatus']
        if job_status in ['COMPLETED', 'FAILED']:
            print(f"Job {job_name} is {job_status}.")
            if job_status == 'COMPLETED':
                response = urllib.request.urlopen(job['TranscriptionJob']['Transcript']['TranscriptFileUri'])
                data = json.loads(response.read())
                text = data['results']['transcripts'][0]['transcript']                
            break
        else:
            print(f"Waiting for {job_name}. Current status is {job_status}.")
        time.sleep(10)
        
    return text
        
        
