import alphabet


def encrypt(string, seed):
    """
    Шифрует строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованный текст
    """
    string = string.lower()
    res = ''
    for i in string:
        index_eng = alphabet.eng.find(i)
        index_rus = alphabet.rus.find(i)
        if index_eng >= 0:
            res += alphabet.eng[(index_eng + seed) % len(alphabet.eng)]
        elif index_rus >= 0:
            res += alphabet.rus[(index_rus + seed) % len(alphabet.rus)]
        else:
            res += i
    return res

def decode(string, seed):
    """
    Расшифровывает строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: расшифрованный текст
    """
    string = string.lower()
    res = ''
    for i in string:
        index_eng = alphabet.eng.find(i)
        index_rus = alphabet.rus.find(i)
        if index_eng >= 0:
            res += alphabet.eng[(len(alphabet.eng) + index_eng - seed) % len(alphabet.eng)]
        elif index_rus >= 0:
            res += alphabet.rus[(len(alphabet.rus) + index_rus - seed) % len(alphabet.rus)]
        else:
            res += i
    return res