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

class Search:
    def __init__(self):
        pass 
    def load(self, text):
        self.text = text
        var = 0
        for i in self.text:
            count = 0
            while var > 0:
                var -= 1
                break
            else:
                for j in llist:
                    count += 1
                    clearlist = []
                    clearlist = re.split("[\-\s]", j)
                    if clearlist[0] == i and len(clearlist) == 1 and len(self.text) == 1:
                        tlist.append(rlist[llist.index(j)])
                        break
                    elif clearlist[0] == i and len(clearlist) == 1 and len(self.text) > 1:
                        tlist.append(rlist[llist.index(j)])
                        break
                    elif clearlist[0] == i and len(clearlist) > 1 and len(self.text) > 1:
                        try:
                            count2 = 0
                            for k in clearlist:
                                if k == self.text[self.text.index(i) + count2]:
                                    count2 += 1
                            if count2 == len(clearlist):
                                tlist.append(rlist[llist.index(j)])
                                var = len(clearlist) - 1
                            else:
                                count += 1
                                continue
                        except IndexError:
                            count += 1
                            continue
                        break
                    elif count == len(llist):
                        tlist.append("out")
        return tlist
