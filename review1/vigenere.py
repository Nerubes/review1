import alphabet


def create_key(string, seed):
    """
    Создает ключ если оригинальный слишком короткий
    :param string: строка под которую надо подгонять длину
    :param seed: оригинальный ключ
    :return: новый ключ
    """
    return seed * (len(string) // len(seed) + 1)


def encrypt(string, seed):
    """
    Шифрует строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованый текст
    """
    seed = create_key(string, seed)
    res = ""
    letter_seed = 0
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    else:
        using_alphabet = alphabet.rus
    for letter_str in range(len(string)):
        index = using_alphabet.find(string[letter_str])
        index_seed = using_alphabet.find(seed[letter_seed])
        res += alphabet.eng[(index + index_seed) % len(using_alphabet)]
    return res


def decode(string, seed):
    """
    Шифрует строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованый текст
    """
    seed = create_key(string, seed)
    res = ""
    letter_seed = 0
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    else:
        using_alphabet = alphabet.rus
    for letter_str in range(len(string)):
        index = using_alphabet.find(string[letter_str])
        index_seed = using_alphabet.find(seed[letter_seed])
        res += alphabet.eng[(index - index_seed + len(using_alphabet)) % len(using_alphabet)]
    return res
