import requests
import json

import time
def news(news_str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(news_str)
news("Welcome")
news("To listen news press 1 else 2")
i= input("Enter your choice: ")
if i=="1":
    req= requests.get("https://newsapi.org/v2/everything?q=tesla&from=2025-05-02&sortBy=publishedAt&apiKey=c13c8c59598f411fb5ebd07251fcb2a8")
    data=req.json()
    for i in data:
        if i=="articles":
            n=1
            for j in data[i]:
                news(f"News {n}: {j['title']}")
                n+=1
                time.sleep(2)