from translate import Translate
from words import Words

def main():
    ip = input("translate: ")
    w = Words(ip)
    wl = w.load()
    t = Translate(wl)
    tl = t.load()
    print("translated text: {}".format(" ".join(tl)))
main()
