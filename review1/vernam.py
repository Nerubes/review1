import alphabet


def correct(string, seed):
    arg1 = True
    arg2 = True
    for i, j in zip(string, seed):
        arg1 = i in alphabet.rus and arg1 and j in alphabet.rus
        arg2 = i in alphabet.eng and arg2 and j in alphabet.eng
    return arg1 or arg2


def encrypt(string, seed):
    """
    Шифрует/Расшифровывает строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованный/расшифрованный текст
    (шифрование и дешифровка являются одним и тем же действием)
    """
    string = string.lower()
    seed = seed.lower()
    res = ''
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    else:
        using_alphabet = alphabet.rus
    for i in range(len(string)):
        res += using_alphabet[(using_alphabet.find(string[i])) ^ (using_alphabet.find(seed[i]))]
    return res
