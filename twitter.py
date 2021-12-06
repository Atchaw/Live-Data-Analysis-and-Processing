import random
import tweepy


#  CLIENT ID PARAM
#-----------
bt = "AAAAAAAAAAAAAAAAAAAAAJ%2BgWQEAAAAA6LcxQVA0wH6Htv0G9fl50q5hfDg%3D2cctcoY64qso8UlIvdEtOXl19l9CEjkSqQjyBpiMjaIB9C22he"
access_key = "1466077331362131971-9dT5cdSldBzmJx6VCNDd9D25rzvwM8"
access_secret = "zzvijKvzbbxJYdLXbaXWtaP0rnJ1dCBD7hvPO9PgjevyU"
consumer_key_ = "ouBVubYV0ilrv12YKMdKjtKZ0"
consumer_secret_ = "jmGEI1C0Bmx8B759znKr8syh64buuqMHaac7nqoj71aDHkvOCa"
#-----------

client = tweepy.Client(bearer_token=bt, access_token = access_key, access_token_secret=access_secret,consumer_key=consumer_key_, consumer_secret=consumer_secret_)

def virgules(txt):
    """[summary]

    Args:
        txt ([string]): [words chain preceded by hashtag]

    Returns:
        [strings]: [strings consisting of words separeted by comma and last word by 'and']
    """
    data = txt.split("#")
    while data[0]=="" and len(data)>1 :
        data = data[1:]
    while data[-1]=="" and len(data)>1:
        data = data[:-1]
    res = data[0]
    if len(data)==1 and data[0]=="":
        res="IoT"
    if len(data)>1:
        for i in data[1:-1] :
            if i!="":
                res =  res+", "+i
        res = res +" and "+data[-1]
    return res

def tweet(trigger,url,hashtag=None):
    """[summary]

    Args:
        trigger ([string]): [Our keyword obtain from audio to speech]
        url ([string]): [Link of the live video]
        hashtag ([string], optional): [our hashtag to publish on twitter]. Defaults to None.
    """
    kw=virgules(trigger)
    
    accroches=[
        "Do you like "+kw+" ? Then join us at "+url,
        "Want to learn more about "+kw+ " ? Join us now at "+url,
        "Join for free a keynote about "+kw+" at "+url,
        kw+" is the main topic now, at "+url+" Joins now !  ",
        "A great opportunity to learn about "+kw+" now at "+url,
        "Interested in "+kw+" ? Join a free keynote on it at "+url,
        "Learn more on "+kw+" right now at "+url+" for free  ",
        "Ask your questions about "+kw+" to an expert, right now at "+url,
        "If you want to know more about "+kw+" join us at "+url,
        "We are hosting a presentation on "+kw+" right now at "+url,
        "A free talk on "+kw+ " is live at "+url,
        "Discover new use of "+kw+ " at our online event at "+url,
        "Be our guest and learn about "+kw+ " at this online event at "+url,
        kw+ " is an interesting topic to you ? Learn more about it at "+url,
        "Interact with an expert on "+kw+ " right now at "+url,
        "We will answer your question about "+kw+ " right now at "+url,
        "We are talking about "+kw+ " right now at "+url,
        "What is "+kw+ " ? Come learn about it right now at "+url,
    ]    

    message = random.choice(accroches)
    if hashtag != None :
        message=message+" "+hashtag
    
    try:  
        client.create_tweet(text=message)
        print("DONE | Tweet : \""+message+"\"")
    except:
        print("To soon, try a little later !")
   
   
   
   
""" 
tweet("Politics","https://youtu.be/T-wSaai8JcA","#FIOT #IOT #FIOT2021 !")
"""