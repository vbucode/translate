from search import Search
from words import Words

inp = input("translate: ")
if inp == "exit":
    exit()
w = Words(inp)
wl = w.load()
s = Search(wl)
sl = s.load()
vs = " ".join(sl)
print("translated text: ", vs)
