from translate import Translate
from words import Words

def main():
    ip = input("translate: ")
    w = Words(ip)
    wl = w.load()
    t = Translate(wl)
    tl = t.load()
    for i in tl:
        print(i)
while True:
    main()
