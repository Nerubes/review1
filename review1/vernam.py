import alphabet


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
