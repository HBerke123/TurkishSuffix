import spell
import soundevents
exceptsbase = open("exceptionals.txt", "r").read().split(" ")
excepts = list()
for i in range(len(excepts) // 4):
    for a in range(4):
        excepts.append((i - 1) * 4 + a)

def asuffix(word, selection, selection2=1, moodsuffix=-1):
    global excepts
    if selection == 1:
        for i in spell.sword(word)[-1]:
            if i in spell.vowels: 
                return word + "l" + soundevents.expansion(i) + "r"
    elif selection == 2:
        if selection2 == 1:
            if word[-1] in spell.vowels:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "y" + soundevents.narrow(i)
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i)
        elif selection2 == 2:
            if word[-1] in spell.vowels:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "y" + soundevents.expansion(i)
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.expansion(i)
        elif selection2 == 3:
            for i in spell.sword(word)[-1]:
                if i in spell.vowels: 
                    return word + "d" + soundevents.expansion(i) + "n"
        elif selection2 == 4:
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "d" + soundevents.expansion(i)
        else:
            return None
    elif selection == 3:
        if selection2 == 1:
            if word[-1] in spell.vowels:
                return word + "m"
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "m"
        elif selection2 == 2:
            if word[-1] in spell.vowels:
                return word + "n"
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "n"
        elif selection2 == 3:
            if word[-1] in spell.vowels:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "s" + soundevents.narrow(i)
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i)
        elif selection2 == 4:
            if word[-1] in spell.vowels:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "m" + soundevents.narrow(i) + "z"
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "m" + soundevents.narrow(i) + "z"
        elif selection2 == 5:
            if word[-1] in spell.vowels:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "n" + soundevents.narrow(i) + "z"
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "n" + soundevents.narrow(i) + "z"
        elif selection2 == 6:
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "l" + soundevents.expansion(i) + "r" + soundevents.narrow(soundevents.expansion(i))                   
        else:
            return None
    elif selection == 4:
        if word[-1] in spell.vowels:
            return word + "n" + soundevents.narrow(word[-1]) + "n"
        else:
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + soundevents.narrow(i) + "n"
    elif selection == 5:
        for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + soundevents.affinity(word[-1], "c") + soundevents.expansion(i)
    elif selection == 6:
        if word[-1] in spell.vowels:
            for i in spell.sword(word)[-1]:
                if i in spell.vowels: 
                    return word + "yl" + soundevents.expansion(i)
        else:
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "l" + soundevents.expansion(i)
    elif selection == 7:
        if moodsuffix == 0:
            return None
        elif selection2 == 1:
            moodsuffix = 1
            if word[-1] in spell.vowels:
                return word + "r"
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.expansion(i) + "r"
        elif selection2 == 2:
            moodsuffix = 2
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "d" + soundevents.narrow(i)
        elif selection2 == 3:
            moodsuffix = 3
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "m" + soundevents.narrow(i) + "ş" 
        elif selection2 == 4:
            moodsuffix = 4
            if word[-1] in spell.vowels:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return spell.rchar(word, -1) + soundevents.narrow(i) + "yor"
            else:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "yor"
        elif selection2 == 5:
            moodsuffix = 5
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "m" + soundevents.expansion(i) + "kt" + soundevents.expansion(i)
        elif selection2 == 6:
            moodsuffix = 6
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    if word[-1] in spell.vowels:
                        return word + "y" + soundevents.expansion(i) + "c" + soundevents.expansion(i) + "k"
                    else:
                        return word + soundevents.expansion(i) + "c" + soundevents.expansion(i) + "k"
        else:
            return None
    elif selection == 8:
        if selection2 == 1:
            moodsuffix = 7
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "m" + soundevents.expansion(i) + "l" + soundevents.narrow(soundevents.expansion(i))
        elif selection2 == 2:
            moodsuffix = 8
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    return word + "s" + soundevents.expansion(i)
        elif selection2 == 3:
            moodsuffix = 9
            for i in spell.sword(word)[-1]:
                if i in spell.vowels:
                    if word[-1] in spell.vowels:
                        return word + "y" + soundevents.expansion(i)
                    else:  
                        return word + soundevents.expansion(i)
        elif selection2 == 4:
            moodsuffix = 10
            return word
        else:
            return None
    elif selection == 9:
            if selection2 == 1:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        if word[-1] in spell.vowels:
                            return word + "yd" + soundevents.narrow(i)
                        else:
                            return word + soundevents.affinity(word[-1], "d") + soundevents.narrow(i)
            elif selection2 == 2:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        if word[-1] in spell.vowels:
                            return word + "ym" + soundevents.narrow(i) + "ş"
                        else:
                            if i in spell.vowels:
                                return word + "m" + soundevents.narrow(i) + "ş"
            elif selection2 == 3:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        if word[-1] in spell.vowels:
                            return word + "ys" + soundevents.expansion(i)
                        else:
                            return word + "s" + soundevents.expansion(i)
            elif selection2 == 4:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "d" + soundevents.narrow(i) + "r"
            else:
                return None
    elif selection == 10:
        if selection2 == 1:
            if moodsuffix == 1:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "m"
            elif moodsuffix == 2:
                return word + "m"
            elif moodsuffix == 3:
                return word + word[-2] + "m"
            elif moodsuffix == 4:
                return word + "um"
            elif moodsuffix == 5:
                return word + soundevents.narrow(word[-2]) + "m"
            elif moodsuffix == 6:
                if word[-2] in spell.vowels:
                    return spell.rchar(word, -1) + "ğ" + soundevents.narrow(word[-2]) + "m"
            elif moodsuffix == 7:
                if word[-2] in spell.vowels:
                    return word + "y" + soundevents.narrow(i) + "m"
            elif moodsuffix == 8:
                return word + "m"
            elif moodsuffix == 9:
                if word[-1] in spell.vowels:
                    return word + "y" + soundevents.narrow(i) + "m"
            elif moodsuffix == 10:
                return None
            else:
                return None
        elif selection2 == 2:
            if moodsuffix == 1:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "s" + soundevents.narrow(i) + "n"
            elif moodsuffix == 2:
                return word + "n"
            elif moodsuffix == 3:
                return word + "s" + word[-2] + "n"
            elif moodsuffix == 4:
                return word + "sun"
            elif moodsuffix == 5:
                return word + "s" + soundevents.narrow(word[-2]) + "n"
            elif moodsuffix == 6:
                if word[-2] in spell.vowels:
                    return word + "s" + soundevents.narrow(word[-2]) + "n"
            elif moodsuffix == 7:
                if word[-2] in spell.vowels:
                    return word + "s" + soundevents.narrow(i) + "n"
            elif moodsuffix == 8:
                return word + "n"
            elif moodsuffix == 9:
                if word[-1] in spell.vowels:
                    return word + "s" + soundevents.narrow(i) + "n"
            elif moodsuffix == 10:
                return word
            else:
                return None
        elif selection2 == 3:
            if moodsuffix == 1:
                for i in spell.sword(word)[-1]:
                    if (i in spell.vowels) & (word[-1] != "r"):
                        return word + soundevents.narrow(i) + "r"
            elif moodsuffix == 2:
                return word
            elif moodsuffix == 3:
                return word
            elif moodsuffix == 4:
                return word
            elif moodsuffix == 5:
                return word
            elif moodsuffix == 6:
                return word
            elif moodsuffix == 7:
                return word
            elif moodsuffix == 8:
                return word
            elif moodsuffix == 9:
                return word
            elif moodsuffix == 10:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        if i in spell.thinvowels:
                            return word + "s" + soundevents.narrow(i) + "n"
            else:
                return None
        elif selection2 == 4:
            if moodsuffix == 1:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "z"
            elif moodsuffix == 2:
                return word + "k"
            elif moodsuffix == 3:
                return word + word[-2] + "z"
            elif moodsuffix == 4:
                return word + "uz"
            elif moodsuffix == 5:
                return word + "y" + soundevents.narrow(word[-2]) + "z"
            elif moodsuffix == 6:
                if word[-2] in spell.vowels:
                    return spell.rchar(word, -1) + "ğ" + soundevents.narrow(word[-2]) + "z"
            elif moodsuffix == 7:
                if word[-2] in spell.vowels:
                    return word + "y" + soundevents.narrow(i) + "m"
            elif moodsuffix == 8:
                return word + "k"
            elif moodsuffix == 9:
                if word[-1] in spell.vowels:
                    return word + "y" + soundevents.narrow(i) + "z"
            elif moodsuffix == 10:
                return word
            else:
                return None
        elif selection2 == 5:
            if moodsuffix == 1:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "s" + soundevents.narrow(i) + "n" + soundevents.narrow(i) + "z"
            elif moodsuffix == 2:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "n" + soundevents.narrow(i) + "z"
            elif moodsuffix == 3:
                return word + "s" + word[-2] + "n" + word[-2] + "z"
            elif moodsuffix == 4:
                return word + "sunuz"
            elif moodsuffix == 5:
                return word + "s" + soundevents.narrow(word[-2]) + "n" + soundevents.narrow(word[-2]) + "z"
            elif moodsuffix == 6:
                if word[-2] in spell.vowels:
                    return word + "s" + soundevents.narrow(word[-2]) + "n" + soundevents.narrow(word[-2]) + "z"
            elif moodsuffix == 7:
                if word[-2] in spell.vowels:
                    return word + "s" + soundevents.narrow(i) + "n" + soundevents.narrow(i) + "z"
            elif moodsuffix == 8:
                if word[-1] in spell.vowels:
                    return word + "n" + soundevents.narrow(i) + "z"
            elif moodsuffix == 9:
                if word[-1] in spell.vowels:
                    return word + "s" + soundevents.narrow(i) + "n" + soundevents.narrow(i) + "z"
            elif moodsuffix == 10:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "n" + soundevents.narrow(i) + "z"
            else:
                return None
        elif selection2 == 6:
            if moodsuffix == 1:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + soundevents.narrow(i) + "rl" + soundevents.expansion(i) + "r"
            elif moodsuffix == 2:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 3:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 4:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 5:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 6:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 7:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 8:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 9:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "l" + soundevents.expansion(i) + "r"
            elif moodsuffix == 10:
                for i in spell.sword(word)[-1]:
                    if i in spell.vowels:
                        return word + "s" + soundevents.narrow(i) + "nl" + soundevents.expansion(i) + "r"
            else: 
                return None
        else:
            return None
    elif selection == 11:
        for i in spell.sword(word)[-1]:
            if i in spell.vowels: 
                return word + "m" + soundevents.expansion(i) + "k"
    else:
        return None