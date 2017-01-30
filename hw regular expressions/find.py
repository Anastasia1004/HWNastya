import re
def findforms():
    find = r"\bна(ш(ёл(ся)?|е(л(ся)?|дш(е(го(ся)?|м(ся|у(ся)?)?|е(ся)?|й(ся)?|ю(ся)?)|ую(ся)?|ая(ся)?|и(й(ся)?|е(ся)?|сь|м(и(ся)?)?|х(ся)?)?))|л(а(сь)?|о(сь)?|и(сь)?))|й(ти(сь)?|д(я(сь)?|у(сь|т(ся)?)?|ё(м(ся)?|шь(ся)?|т(ся|е(сь)?)?|нн(ую|ая|ы(х|е|й|ми?)|о(й|го|о|ю|му?)))|е(шь(ся)?|т(ся|е(сь)?)?|м(ся)?|н(а|о|ы|н((ую|ая|ы(х|е|й|ми?)|о(й|го|о|ю|му?))))?)|и(сь|те(сь)?)?)))\b"
    arr = []
    with open("find.txt", "r", encoding="utf-8") as f:
        words = f.read()
        for word in words.split():
            p = re.search(find, word)
            if p != None:
                if word not in arr:
                    arr.append(word)
        for item in arr:
            print(item)
findforms()
