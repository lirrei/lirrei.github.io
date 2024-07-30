import datetime
from gtts import gTTS
import random
import speech_recognition as sr

def what_time_is_it(lang, filename):
    '''
    Tell me what time it is.
    
    Parameters:
    lang (str) - language in which to speak
    filename (str) - the filename into which the audio should be recorded
    '''
    now = datetime.datetime.now()
    time_str = now.strftime("%H:%M")
    tts = gTTS(text=f"The current time is {time_str}", lang=lang)
    tts.save(filename)

def tell_me_a_joke(lang, audiofile):
    '''
    Tell me a joke.
    
    @params:
    filename (str) - filename containing the database of jokes
    lang (str) - language
    audiofile (str) - audiofile in which to record the joke
    '''
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't some couples go to the gym? Because some relationships don't work out!"
    ]
    joke = random.choice(jokes)
    tts = gTTS(text=joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    '''
    Tell me what day it is.

    @params:
    lang (str) - language in which to record the date
    audiofile (str) - filename in which to read the date
    
    @returns:
    url (str) - URL that you can look up in order to see the calendar for this month and year
    '''
    today = datetime.datetime.now()
    date_str = today.strftime("%A, %B %d, %Y")
    tts = gTTS(text=f"Today is {date_str}", lang=lang)
    tts.save(audiofile)
    
    url = f"https://www.timeanddate.com/calendar/?year={today.year}&month={today.month}"
    return url

def personal_assistant(lang, filename):
    '''
    Listen to the user, and respond to one of three types of requests:
    What time is it?
    What day is it?
    Tell me a joke!
    
    @params:
    lang (str) - language
    filename (str) - filename in which to store the result
    '''
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your request...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        
        if "time" in query.lower():
            what_time_is_it(lang, filename)
        elif "day" in query.lower():
            what_day_is_it(lang, filename)
        elif "joke" in query.lower():
            tell_me_a_joke(lang, filename)
        else:
            tts = gTTS(text="Sorry, I didn't understand that.", lang=lang)
            tts.save(filename)
    except sr.UnknownValueError:
        tts = gTTS(text="Sorry, I could not understand the audio.", lang=lang)
        tts.save(filename)
    except sr.RequestError as e:
        tts = gTTS(text=f"Could not request results from the speech recognition service; {e}", lang=lang)
        tts.save(filename)

# 测试代码
import importlib
import homework14
importlib.reload(homework14)

homework14.personal_assistant('en', 'test.mp3')
y, sr = librosa.load("test.mp3")
IPython.display.Audio(data=y, rate=sr)

