import alphabet


def encrypt(string, seed):
    """
    Шифрует строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованный текст
    """
    res = ""
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    elif string[0] in alphabet.rus:
        using_alphabet = alphabet.rus
    else:
        return "Incorrect Input. Try again."
    for letter in string:
        index = using_alphabet.find(letter)
        if index >= 0:
            res += using_alphabet[(index + seed) % len(using_alphabet)]
        else:
            res += letter
    return res


def decode(string, seed):
    """
    Расшифровывает строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: расшифрованный текст
    """
    res = ""
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    elif string[0] in alphabet.rus:
        using_alphabet = alphabet.rus
    else:
        return "Incorrect Input. Try again."
    for letter in string:
        index = using_alphabet.find(letter)
        if index >= 0:
            res += using_alphabet[(len(using_alphabet) + index - seed) % len(using_alphabet)]
        else:
            res += letter
    return res
