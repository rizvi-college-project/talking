from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox

from PIL import Image, ImageTk

#get_close_matches(word,possibities,n,cuttoff)
#close_match=get_close_match('appel',['app','ape','peach','puppy'])#0.0 - 1.0
#print(close_match)

#functionality part

def search():
    data=json.load(open('data.json'))
    word=enterwordEntry.get()
    word=word.lower()
    if word in data:
        meaning=data[word]
        print(meaning)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n\n')
    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno("confirm",'Did you mean '+close_match+' instead?')
        if res==True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)
            meaning=data[close_match]
            textarea.delete(1.0,END)
            for item in meaning:
                textarea.insert(END,u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error','The word doesnt exist,Please double check it.')
            enterwordEntry.delete(0,END)
            textarea.delete(1.0,END)
    else:
        messagebox.showinfo('Information', 'The word doesnt exist.')
        enterwordEntry.delete(0, END)
        textarea.delete(1.0,END)


#gui part
root = Tk()
root.geometry('1000x626+100+10')
root.title("Taking Dictionary")
#root.resizable(False, False)
# book = PhotoImage(file="library.jpeg")
book = Image.open("book.png")
photo = ImageTk.PhotoImage(book)
bookLabel = Label(root, image=photo)
bookLabel.place(x=0, y=0)
bookLabel.pack()

# text label
enterwordLabel = Label(root, text="Enter the word", font=("Algerian", 25, "bold"), fg="red", bg="lightblue")
enterwordLabel.place(x=650, y=30)

# entry fill
enterwordEntry = Entry(root, font=("Times New Roman", 24,), justify=CENTER, bd=10, relief=GROOVE)
enterwordEntry.place(x=620, y=100)

# search botton
searchBotton = Image.open("loupe.png")
readImage1 = ImageTk.PhotoImage(searchBotton)
Botton1 = Button(root, image=readImage1, bd=0, bg="red", cursor="hand2", activebackground="red", command=search)
#Botton1.size(15)
Botton1.place(x=700, y=180)

#taking vioce for word
voiceBotton = Image.open("voice.png")
readImage2 = ImageTk.PhotoImage(voiceBotton)
Botton2 = Button(root, image=readImage2, bd=0, bg="red", cursor="hand2", activebackground="red")
#Botton2.size(15)
Botton2.place(x=800, y=180)

#giving audio for word
audioBotton1 = Image.open("audio.png")
readImage6 = ImageTk.PhotoImage(audioBotton1)
Botton6 = Button(root, image=readImage6, bd=0, bg="red", cursor="hand2", activebackground="red")
#Botton2.size(15)
Botton6.place(x=900, y=180)


#meaning Label
meanwordLabel = Label(root, text="Meaning ", font=("Algerian", 25, "bold"), fg="red", bg="lightblue")
meanwordLabel.place(x=700, y=280)


#meaningbox
textarea= Text(root, width=30, height=6, font=("Times New Roman", 18), bd=10, relief=GROOVE)
textarea.place(x=600, y=330)

#audio
audioBotton = Image.open("audio.png")
readImage3 = ImageTk.PhotoImage(audioBotton)
Botton3 = Button(root, image=readImage3, bd=0, bg="red", cursor="hand2", activebackground="red")
#Botton2.size(15)
Botton3.place(x=850, y=545)

#cancel
cancelBotton = Image.open("cancel.png")
readImage4 = ImageTk.PhotoImage(cancelBotton)
Botton4 = Button(root, image=readImage4, bd=0,bg="red", cursor="hand2", activebackground="red")
#Botton2.size(15)
Botton4.place(x=750, y=545)

#exit

exitBotton = Image.open("exit.png")
readImage5 = ImageTk.PhotoImage(exitBotton)
Botton3 = Button(root, image=readImage5, bd=0, bg="red", cursor="hand2", activebackground="red")
#Botton2.size(15)
Botton3.place(x=650, y=545)


#enter button work
def enter_function(event):
    searchBotton.invoke()

root.bind('<Return>',enter_function)
root.mainloop()
