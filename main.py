from search import Search
from words import Words

def main():
    inp = input("translate: ")
    if inp == "exit":
        exit()
    w = Words(inp)
    wl = w.load()
    s = Search(wl)
    sl = s.load()
    varstring = " ".join(sl)
    #sl.clear()
    print("translated text: ", sl)
while True:
    main()
