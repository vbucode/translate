import tkinter
from tkinter import messagebox
from tkinter import scrolledtext
from translate import Translate
from words import Words
import corpus

root = tkinter.Tk()
root.title("translate")
root.geometry("650x250")
root.configure(bg = "black")

flag = 0

dcorpus = corpus.translate()

t = Translate(*dcorpus)

def translatef():
    txt2.configure(state = "normal")
    txt2.delete(1.0, tkinter.END) 
    inp = txt.get(1.0, tkinter.END)
    w = Words(inp)
    wl = w.load()
    sl = gettr(wl)
    varstr = " ".join(sl)
    txt2.insert(1.0, varstr)
    txt2.configure(state = "disable")

def deletef():
    txt2.configure(state = "normal")
    txt.delete(1.0, tkinter.END)
    txt2.delete(1.0, tkinter.END)
    txt2.configure(state = "disable")

def changelang():
    global flag
    if flag == 0:
        lbl["text"] = "Russian"
        lbl2["text"] = "English"
        flag = 1
    else:
        lbl["text"] = "English"
        lbl2["text"] = "Russian"
        flag = 0

def gettr(xarg):
    global t
    global flag
    if flag == 0:
        r = t.load(xarg)
    else:
        r = t.upload(xarg)
    return r

def infof():
    msg = messagebox.showinfo( "Translate", "by vbucode")

btn1 = tkinter.Button(root, text = "translate", bg = "gray", command = translatef)
btn2 = tkinter.Button(root, text = "delete", bg = "gray", command = deletef)
btn3 = tkinter.Button(root, text = "info", bg = "gray", command = infof)
btn4 = tkinter.Button(root, text = "<>", bg = "gray", command = changelang)
lbl = tkinter.Label(root, text = "English", fg = "white", bg = "black")
lbl2 = tkinter.Label(root, text = "Russian",  fg = "white", bg = "black")
txt = scrolledtext.ScrolledText(root, width = 35, height = 10)
txt2 = scrolledtext.ScrolledText(root, width = 35, height = 10)
lbl.place(x = 5, y = 4)
txt.place(x = 0, y = 20)
lbl2.place(x = 355, y = 4)
txt2.place(x = 350, y = 20)
btn4.place(x = 300, y = 20)
btn1.place(x = 5, y = 205)
btn2.place(x = 96, y = 205)
btn3.place(x = 170, y = 205)

if __name__ == "__main__":
    txt2.insert(1.0, "Translation")
    txt2.configure(state = "disable")
    root.mainloop()
