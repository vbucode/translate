from search import Search
from words import Words

s = Search()

def main():
    inp = input("translate: ")
    if inp == "exit":
        exit()
    getw(inp)

def getw(xarg):
    global s
    w = Words(xarg)
    wl = w.load()
    sl = s.load(wl)
    varstr = " ".join(sl)
    print("translated text: ", varstr)

while True:
    main()
