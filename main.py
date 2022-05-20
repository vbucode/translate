import tkinter
from tkinter import scrolledtext
from translate import Translate
from words import Words

root = tkinter.Tk()
root.title("translate")
root.geometry("605x230")
root.configure(bg = "black")

t = Translate()

def translatef():
    global t
    inp = txt.get(1.0, tkinter.END)
    w = Words(inp)
    wl = w.load()
    sl = t.load(wl)
    varstr = " ".join(sl)
    txt2.insert(1.0, varstr)

def deletef():
    txt.delete(1.0, tkinter.END)
    txt2.delete(1.0, tkinter.END)

btn1 = tkinter.Button(root, text = "translate", bg = "gray", command = translatef)
btn2 = tkinter.Button(root, text = "delete", bg = "gray", command = deletef)
txt = scrolledtext.ScrolledText(root, width = 35, height = 10)
txt2 = scrolledtext.ScrolledText(root, width = 35, height = 10)
txt.place(x = 0, y = 0)
txt2.place(x = 300, y = 0)
btn1.place(x = 5, y = 185)
btn2.place(x = 160, y = 185)

if __name__ == "__main__":
    root.mainloop()
