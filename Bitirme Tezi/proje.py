from datetime import datetime
from msilib.schema import File
from turtle import goto
import requests
import speech_recognition as sr
import pyaudio
import time
from datetime import datetime
import webbrowser
from gtts import gTTS
from playsound import playsound
import random
import os
from bs4 import BeautifulSoup
from urllib import request


r = sr.Recognizer()

def record(ask = False):
    
    with sr.Microphone() as source:
        if ask:
            speak(ask)
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('anlayamadim')
            print('anlayamadim')
        except sr.RequestError:
            speak('sistem calismiyor')
            print('sistem calismiyor')
        return voice


def response(voice):
    if'nasılsın' in voice:
        speak('iyi senden')
        print('iyi senden')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
        print(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsun')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım')
        print(search + ' için bulduklarım')
    if "tamamdır" in voice:
        speak('görüşürüz')
        exit()
    if "hava nasıl" in voice:
        search = record("hangi şehir")
        url = "https://www.ntvhava.com/{}-hava-durumu".format(search)
        request=requests.get(url)
    
        html_icerigi=request.content

        soup=BeautifulSoup(html_icerigi,'html.parser')

        gunduz_sicakliklari=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-box-bottom-degree-big"})
        gece_sicakliklari=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-box-bottom-degree-small"})
        hava_durumlari=soup.find_all("div",{"class":"daily-report-tab-content-pane-item-text"})


        gunduz=[1]
        gece=[1]
        hava=[1]

        for x in gunduz_sicakliklari:
            x=x.text
            gunduz.append(x)

        for y in gece_sicakliklari:
            y=y.text
            gece.append(y)

        for z in hava_durumlari:
            z=z.text
            hava.append(z)
    
        birlestirme="{} için yarınki hava raporları şöyle {} gündüz sıcaklığı {} gece sıcaklığı {}".format(search,hava[1],gece[1],gunduz[1])
        speak(birlestirme)
    if "video aç" in voice or "müzik aç" in voice or "youtube aç" in voice:
        search = record("hangi video")
        url = "https://www.youtube.com/results?search_query={}".format(search)
        request=requests.get(url)
        tarayici=webdriver.Chrome()
        tarayici.get(url)
        buton=tarayici.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()
    if "piyasa nasıl" in voice:
        speak ("Piyasayı ekrana yansıtıyorum")
        url="https://www.sabah.com.tr/finans/doviz"

        request=requests.get(url)

        html_icerigi=request.content

        soup=BeautifulSoup(html_icerigi,'html.parser')

        dolar_guncel=soup.find_all("div",{"class":"table-wrapper"})

        for x in dolar_guncel:
            print(x.text)


        

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

print('Nasıl yardımcı olabilirim')
speak('Nasıl yardımcı olabilirim')
time.sleep(1)

while 1:
    voice = record()
    print(voice)
    response(voice)