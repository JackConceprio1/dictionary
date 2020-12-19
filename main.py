from lxml import html,etree
from lxml.etree import tostring
from itertools import chain
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
import requests,json
from bs4 import BeautifulSoup 


def getWordFromDictionary(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = str(w.get(index)).rstrip()
    print(value)
    r = requests.get(f"https://www.dictionary.com/browse/{value}?s=t")
    if r.status_code == 200:
        soup = BeautifulSoup(r.text,features="html.parser")
        if str(soup).find == ("WORDS NEARBY"):
            divs = soup.find("li",class_="one-click-content")
            for i in div:
                print(i.text())


    else:
        print("an error has happend error code" + str(r.status_code))

def searchForWord():
    listedWords.delete(0,tk.END)
    # r = requests.get(f"https://api-portal.dictionary.com/dcom/list/{searchbox.get()}?limit=100000").text

    # loadedJson = json.loads(r)
    # print(loadedJson["data"])
    # for i in loadedJson["data"]:
    #     listedWords.insert(tk.END,i["displayForm"])
    #     print(i["displayForm"])

    file = open("dictionary words.txt","r").readlines()
    for word in file:
        if word.startswith(searchbox.get().lower()):
            print(word)
            listedWords.insert(tk.END,word)
        




window = tk.Tk()
window.geometry("800x500")


leftFrame = tk.Frame(window)
leftFrame.pack(side="left",fill="both",expand=1, anchor="w")

searchArea = tk.Frame(leftFrame)
searchArea.pack(side="top",fill="x", anchor="w",padx=(5, 5))

searchLabel = tk.Label(searchArea,text="Search").pack()

searchbox = tk.Entry(searchArea)
searchbox.pack(side="left",fill="x",expand=1,padx=(5, 10))

searchButton = tk.Button(searchArea,text="search",command=searchForWord).pack(side="right")

listedWords = tk.Listbox(leftFrame)
listedWords.pack(fill="both",expand=1,padx=(5, 5),pady=(5,20))
listedWords.bind('<<ListboxSelect>>', getWordFromDictionary)
Scrollbar1 = Scrollbar(listedWords,orient="vertical")
Scrollbar1.config(command=listedWords.yview)
Scrollbar1.pack(side="right",fill="y")



rightFrame = tk.Frame(window)
rightFrame.pack(side="right",fill="both",expand=1, anchor="w")

textfild = tk.Text(rightFrame,font=("Helvetica", 16),wrap="word")
Scrollbar1 = Scrollbar(rightFrame,orient="vertical")
Scrollbar1.config(command=textfild.yview)
Scrollbar1.pack(side="right",fill="y")

textfild.pack(side="left",fill="both",expand=1,padx=(15, 15),pady=(10,20))
textfild.tag_config('titleText',font=("Helvetica", 16))
textfild.tag_config('subText',font=("Helvetica", 12))


window.mainloop()