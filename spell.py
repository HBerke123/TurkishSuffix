vowels = "aeıioöuü"
thinvowels = "eiöü"
lowvowels = "aıou"
plainvowels = "aeıi"
roundedvowels = "oöuü"
widevovels = "aeoö"
hardchars = "fstkçşhp"
softchars = "bcdgğjlmnrvyz"
spells = list()
vowelnums = list()
chars = list()
lastword = str()

def rchar(word, index):
    lastword = str()
    chars.clear()
    for c in word:
        chars.append(c)
    chars.pop(index)
    for c in chars:
        lastword = lastword + c 
    return lastword

def sword(word):
    global spells
    lastword = word
    spells.clear()  

    while len(lastword) > 0:
        vowelnums.clear()
        for c in range(len(lastword)):
            if (lastword[c] in vowels):
                vowelnums.append(c)

        if (len(vowelnums) == 1):
            spells.append(lastword)
            lastword = str()
        else:
            if (vowelnums[-1] - vowelnums[-2] == 1):
                if (lastword[-1] in vowels):
                    spells.append(lastword[-1])
                    lastword = rchar(lastword, -1)
                else:
                    spells.append(str())
                    for i in range(len(lastword) - vowelnums[-1]):
                        spells[-1] += lastword[-1]
                        lastword = rchar(lastword, -1)
                    spells[-1] = spells[-1][::-1]
            else:
                if (lastword[-1] in vowels):            
                    spells.append(str())
                    for i in range(2):
                        spells[-1] += lastword[-1]
                        lastword = rchar(lastword, -1)
                    spells[-1] = spells[-1][::-1]
                else:
                    if lastword[vowelnums[-1] - 1] in vowels:
                        spells.append(str())
                        for i in range(len(lastword) - vowelnums[-1]):
                            spells[-1] += lastword[-1]
                            lastword = rchar(lastword, -1)
                        spells[-1] = spells[-1][::-1]
                    else:
                        spells.append(str())
                        for i in range(len(lastword) - vowelnums[-1] + 1):
                            spells[-1] += lastword[-1]
                            lastword = rchar(lastword, -1)
                        spells[-1] = spells[-1][::-1]
    spells.reverse()
    return spells