import alphabet


def correct(string):
    arg1 = True
    arg2 = True
    for i in string:
        arg1 = i in alphabet.rus and arg1
        arg2 = i in alphabet.eng and arg2
    return arg1 or arg2


def encrypt(string, seed):
    """
    Шифрует строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованный текст
    """
    string = string.lower()
    res = ''
    if alphabet.eng.find(string.split()[0][0]) >= 0:
        alpha = alphabet.eng
    else:
        alpha = alphabet.rus
    for i in string:
        index = alpha.find(i)
        res += alpha[(index + seed) % len(alpha)]
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
    if alphabet.eng.find(string.split()[0][0]) >= 0:
        alpha = alphabet.eng
    else:
        alpha = alphabet.rus
    for i in string:
        index = alpha.find(i)
        res += alpha[(index - seed) % len(alpha)]
    return res
