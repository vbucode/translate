import re
from words import Words
import corpus

class Translate:
    def __init__(self, llist, rlist, vect, dlist, instb, rlist2):
        self.llist = llist
        self.rlist = rlist
        self.vect = vect
        self.dlist = dlist
        self.rlist2 = rlist2
        self.instb = instb

    def load(self, text):
        self.text = text
        tlist = []
        searchlist = []

        for k in self.text:
            for i, x in enumerate(self.instb):
                if x == k:
                    searchlist.append((k, self.text.index(k), i))
        if len(searchlist) != 0:
            for i in range(len(self.dlist)):
                triallist = []
                countw = 0
                for k in searchlist:
                    try:
                        if self.vect[i][k[2]] == 1:
                            triallist.append(k[1])
                            countw += 1
                            if countw == len(self.dlist[i]):
                                for j in range(len(triallist)):
                                    self.text.pop(triallist[0])
                                self.text.insert(k[1], (self.rlist2[i], k[1]))
                    except ValueError:
                       pass
        def binarysearch(xlist, item):
            low:int = 0
            high:int = len(xlist)-1
            while low <= high:
                mid:int = (low + high) // 2
                if xlist[mid] == item:
                    return mid
                elif xlist[mid] < item:
                    low = mid + 1
                elif xlist[mid] > item:
                    high = mid - 1
            return False
        print(self.text)
        for i in self.text:
            if type(i) == str:
                binaryr = binarysearch(self.llist, i)
                if binaryr != False:
                    tlist.insert(self.text.index(i), self.rlist[binaryr])
            else:
                tlist.insert(i[1], i[0])
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
