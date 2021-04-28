import alphabet


def create_key(string, seed):
    """
    Создает ключ если оригинальный слишком короткий
    :param string: строка под которую надо подгонять длину
    :param seed: оригинальный ключ
    :return: новый ключ
    """
    return seed * (len(string) // len(seed) + 1)


def encrypt(string, seed, n):
    """
    Шифрует или дешифрует строку используя шифр Виженера
    :param string: текст для шифровки или дешифровки
    :param seed: ключ
    :param n: указывает на то, будет ли функция шифровать или дешифровать строку
    :return: зашифрованый или расшифрованный текст
    """
    seed = create_key(string, seed)
    res = ""
    letter_seed = 0
    if string[0] in alphabet.eng:
        using_alphabet = alphabet.eng
    elif string[0] in alphabet.rus:
        using_alphabet = alphabet.rus
    else:
        return "Incorrect Input. Try again."
    for letter_str in range(len(string)):
        index = using_alphabet.find(string[letter_str])
        index_seed = using_alphabet.find(seed[letter_seed])
        res += using_alphabet[(index + n * index_seed + len(using_alphabet)) % len(using_alphabet)]
    return res
