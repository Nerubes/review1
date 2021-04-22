import alphabet


def encrypt(string, seed, n):
    """
    Шифрует или дешифрует строку используя шифр Цезаря
    :param string: текст для шифровки или дешифровки
    :param seed: ключ
    :param n: указывает на то, будет ли функция шифровать или дешифровать строку
    :return: зашифрованый или расшифрованный текст
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
            res += using_alphabet[(index + n * seed) % len(using_alphabet)]
        else:
            res += letter
    return res
