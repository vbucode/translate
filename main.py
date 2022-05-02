from search import Search
from words import Words

def main():
    inp = input("translate: ")
    if inp == "exit":
        exit()
    getw(inp)

def getw(xarg):
    w = Words(xarg)
    wl = w.load()
    s = Search(wl)
    sl = s.load()
    varstr = " ".join(sl)
    print("translated text: ", varstr)
    sl.clear()

while True:
    main()
