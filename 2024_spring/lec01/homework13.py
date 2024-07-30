import bs4
from gtts import gTTS

def extract_stories_from_NPR_text(text):

    soup = bs4.BeautifulSoup(text, 'html.parser')
    stories = []
    
    for item in soup.find_all('article'):
        title = item.find('h2').get_text(strip=True) if item.find('h2') else ''
        teaser = item.find('p').get_text(strip=True) if item.find('p') else ''
        stories.append((title, teaser))
    
    return stories

def read_nth_story(stories, n, filename):

    if n < 0 or n >= len(stories):
        raise IndexError("Story index out of range")
    
    story = stories[n]
    text = f"Title: {story[0]}\nTeaser: {story[1]}"
    
    tts = gTTS(text=text, lang='en')
    tts.save(filename)


import requests


response = requests.get('https://www.npr.org/')
webpage_text = response.text


stories = extract_stories_from_NPR_text(webpage_text)

read_nth_story(stories, 0, 'story.mp3')
