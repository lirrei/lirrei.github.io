from gtts import gTTS

def synthesize(text, lang, filename):
    '''
    Use gtts.gTTs(text=text, lang=lang) to synthesize speech, then write it to filename.
    
    @params:
    text (str) - the text you want to synthesize
    lang (str) - the language in which you want to synthesize it
    filename (str) - the filename in which it should be saved
    '''
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

# 测试代码
import importlib
import homework12
importlib.reload(homework12)

homework12.synthesize("This is speech synthesis!","en","english.mp3")
y, sr = librosa.load("english.mp3")
IPython.display.Audio(data=y, rate=sr)
