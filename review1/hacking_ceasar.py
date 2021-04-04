import collections

import alphabet


def correct(string):
    arg1 = True
    arg2 = True
    for i in string:
        arg1 = i in alphabet.rus and arg1
        arg2 = i in alphabet.eng and arg2
    return arg1 or arg2


def frequency_analysis(string):
    mas_string = string.get().split()
    count = collections.Counter()
    for i in mas_string:
        for j in i:
            count[j] += 1
    most_common = count.pop(0)
    if alphabet.eng.find(string.get()[0]) >= 0:
        return (len(alphabet.eng) + alphabet.eng.find(most_common) - alphabet.eng.find('e')) % len(alphabet.eng)
    else:
        return (len(alphabet.rus) + alphabet.rus.find(most_common) - alphabet.rus.find('о')) % len(alphabet.rus)
