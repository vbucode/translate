import re
from words import Words
import corpus

class Translate:
    def __init__(self, llist, rlist):
        self.llist = llist
        self.rlist = rlist
    def load(self, text):
        self.text = text
        var = 0
        tlist = []
        for i in self.text:
            count = 0
            while var > 0:
                var -= 1
                break
            else:
                for j in self.llist:
                    count += 1
                    clearlist = []
                    clearlist = re.split("[\-\s]", j)
                    if clearlist[0] == i and len(clearlist) == 1 and len(self.text) == 1:
                        tlist.append(self.rlist[self.llist.index(j)])
                        break
                    elif clearlist[0] == i and len(clearlist) == 1 and len(self.text) > 1:
                        tlist.append(self.rlist[self.llist.index(j)])
                        break
                    elif clearlist[0] == i and len(clearlist) > 1 and len(self.text) > 1:
                        try:
                            count2 = 0
                            for k in clearlist:
                                if k == self.text[self.text.index(i) + count2]:
                                    count2 += 1
                            if count2 == len(clearlist):
                                tlist.append(self.rlist[self.llist.index(j)])
                                var = len(clearlist) - 1
                            else:
                                count += 1
                                continue
                        except IndexError:
                            count += 1
                            continue
                        break
                    elif count == len(self.llist):
                        tlist.append("out")
        return tlist
    def upload(self, text):
        self.text = text
        var = 0
        tlist = []
        for i in self.text:
            count = 0
            while var > 0:
                var -= 1
                break
            else:
                for j in self.rlist:
                    count += 1
                    clearlist = []
                    clearlist = re.split("[\-\s]", j)
                    if clearlist[0] == i and len(clearlist) == 1 and len(self.text) == 1:
                        tlist.append(self.llist[self.rlist.index(j)])
                        break
                    elif clearlist[0] == i and len(clearlist) == 1 and len(self.text) > 1:
                        tlist.append(self.llist[self.rlist.index(j)])
                        break
                    elif clearlist[0] == i and len(clearlist) > 1 and len(self.text) > 1:
                        try:
                            count2 = 0
                            for k in clearlist:
                                if k == self.text[self.text.index(i) + count2]:
                                    count2 += 1
                            if count2 == len(clearlist):
                                tlist.append(self.llist[self.rlist.index(j)])
                                var = len(clearlist) - 1
                            else:
                                count += 1
                                continue
                        except IndexError:
                            count += 1
                            continue
                        break
                    elif count == len(self.rlist):
                        tlist.append("out")
        return tlist

if __name__ == "__main__":
    diccorpus = corpus.translate()
    t = Translate(*diccorpus)
    def main():
        inp = input("translate: ")
        if inp == "exit":
            exit()
        getw(inp)

    def getw(xarg):
        global t
        w = Words(xarg)
        wl = w.load()
        sl = t.load(wl)
        varstr = " ".join(sl)
        print("translated text: ", varstr)
    while True:
        main()
