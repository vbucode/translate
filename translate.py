import re

tlist = []
llist = []
rlist = []

with open("words-eng-ru.txt", "r") as file:
    for line in file:
        if not line:
            continue
        else:
            left, right, *res = line.split(":")
            llist.append(left)
            rlist.append(right.replace("\n", ""))
class Translate:
    def __init__(self, text):
        self.text = text
    def load(self):
        for i in self.text:
            count = 0
            for j in llist:
                count += 1
                clearlist = []
                clearlist = re.split("[\-\s]", j)
                if clearlist[0] == i and len(clearlist) == 1:
                    tlist.append(rlist[llist.index(j)])
                    break
                elif clearlist[0] == i and len(clearlist) > 1:
                    count2 = 0
                    triallist = []
                    for k in clearlist:
                        count2 += 1
                        if k == self.text[self.text.index(i) + count2 - 1]:
                            triallist.append(rlist[llist.index(j)])
                        if len(triallist) == len(clearlist):
                            for n in triallist:
                                if triallist.index(n) == 0:
                                    tlist.append(n)
                        else:
                            tlist.append((rlist[llist.index(j)]))
                        break
                elif count == len(llist):
                        tlist.append("out")
        return tlist
