import spell
chars = str()

def narrow(char):
    if char in spell.vowels:
        if char in spell.thinvowels:
            if char in spell.plainvowels:
                return "i"
            else:
                return "ü"
        else:
            if char in spell.plainvowels:
                return "ı"
            else:
                return "u"
    else:
        return None
    
def affinity(char1, char2):
    if char1 in spell.hardchars:
        for c in spell.softchars:
            if c == char2:
                if c == "c":
                    return "ç"
                elif c == "d":
                    return "t"
                elif c == "g":
                    return "t"
                elif c == "b":
                    return "p"
    return char2

def expansion(char):
    if char in spell.vowels:
        if char in spell.thinvowels:
            return "e"
        else:
            return "a"
    return None