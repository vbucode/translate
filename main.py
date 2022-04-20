from translate import Translate
from words import Words

def main():
    ip = input("translate: ")
    if ip == "exit":
        exit()
    it = translater(ip)
    print("translated text: ", it)
def translater(text):
    w = Words(text)
    wl = w.load()
    t = Translate(wl)
    tl = t.load()
    varstring = " ".join(tl)
    tl.clear()
    return varstring
while True:
    main()
