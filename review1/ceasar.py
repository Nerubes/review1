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
