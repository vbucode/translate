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
        searchlist2 = []

        for k in self.text:
            for i, x in enumerate(self.instb):
                if x == k:
                    searchlist.append((k, self.text.index(k), i))
        if len(searchlist) != 0:
            for i in range(len(self.dlist)):
                countw = 0
                for k in searchlist:
                    try:
                        if self.vect[i][k[2]] == 1:
                            triallist = [k[2]]
                            countw += 1
                            if countw == len(self.dlist[i]) and triallist[-2] == k[2] - 1:
                                searchlist2.append((self.rlist2[i], k[1]))
                                del self.text[triallist]
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

        for i in self.text:
            binaryr = binarysearch(self.llist, i)
            if binaryr != False:
                tlist.insert(self.text.index(i), self.rlist[binaryr])
        for i in searchlist2:
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
