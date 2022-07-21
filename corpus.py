import json

def translate():
    llist = []
    rlist = []
    instb = []
    with open("few.json", "r") as file2:
        data = json.load(file2)
    for i in data["sentok"]:
        for j in i:
            instb.append(j)

    with open("one.txt", "r") as file:
        for line in file:
            if not line:
                continue
            else:
                left, right, *res = line.split(":")
                llist.append(left)
                rlist.append(right.replace("\n", ""))
    return llist, rlist, data["vector"], data["sentok"], instb, data["tr"]
