import alphabet


def encrypt(string, seed):
    """
    Шифрует/Расшифровывает строку используя шифр Вернама
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованный/расшифрованный текст
    (шифрование и дешифровка являются одним и тем же действием)
    """
    res = ""
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    elif string[0] in alphabet.rus:
        using_alphabet = alphabet.rus
    else:
        return "Incorrect Input. Try again."
    for i in range(len(string)):
        print(using_alphabet, (using_alphabet.find(string[i])) ^ (using_alphabet.find(seed[i])))
        res += using_alphabet[(using_alphabet.find(string[i])) ^ (using_alphabet.find(seed[i]))]
    return res
