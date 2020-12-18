import tkinter as tk



window = tk.Tk()
window.geometry("600x500")


leftFrame = tk.Frame(window)
leftFrame.pack(side="left",fill="both",expand=1, anchor="w")

searchArea = tk.Frame(leftFrame)
searchArea.pack(side="top",fill="x", anchor="w",padx=(5, 5))

searchLabel = tk.Label(searchArea,text="Search").pack()

searchbox = tk.Entry(searchArea)
searchbox.pack(side="left",fill="x",expand=1,padx=(5, 10))

searchButton = tk.Button(searchArea,text="search").pack(side="right")

selectedWord = tk.Listbox(leftFrame).pack(fill="both",expand=1,padx=(5, 5),pady=(5,20))




rightFrame = tk.Frame(window)
rightFrame.pack(side="right",fill="both",expand=1, anchor="w")

text2 = tk.Text(rightFrame).pack(fill="both",expand=1,padx=(15, 15),pady=(10,20))


window.mainloop()