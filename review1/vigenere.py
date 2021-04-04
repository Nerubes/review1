import alphabet


def create_key(string, seed):
    """
    ССоздает ключ если оригинальный слишком короткий
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
    string = string.lower()
    seed = seed.lower()
    seed = create_key(string, seed)
    res = ''
    j = 0
    for i in range(len(string)):
        index_eng = alphabet.eng.find(string[i])
        index_rus = alphabet.rus.find(string[i])
        index_seed_eng = alphabet.eng.find(seed[j])
        index_seed_rus = alphabet.rus.find(seed[j])
        if index_eng >= 0:
            if index_seed_eng >= 0:
                res += alphabet.eng[(index_eng + index_seed_eng) % len(alphabet.eng)]
            else:
                res += alphabet.eng[(index_eng + index_seed_rus) % len(alphabet.eng)]
        elif index_rus >= 0:
            if index_seed_rus >= 0:
                res += alphabet.rus[(index_eng + index_seed_eng) % len(alphabet.rus)]
            else:
                res += alphabet.rus[(index_eng + index_seed_rus) % len(alphabet.rus)]
        else:
            res += i
            j -= 1
        j += 1
    return res


def decode(string, seed):
    """
    Шифрует строку используя шифр цезаря
    :param string: текст для шифровки
    :param seed: ключ
    :return: зашифрованый текст
    """
    string = string.lower()
    seed = seed.lower()
    seed = create_key(string, seed)
    res = ''
    j = 0
    for i in range(len(string)):
        index_eng = alphabet.eng.find(string[i])
        index_rus = alphabet.rus.find(string[i])
        index_seed_eng = alphabet.eng.find(seed[j])
        index_seed_rus = alphabet.rus.find(seed[j])
        if index_eng >= 0:
            if index_seed_eng >= 0:
                res += alphabet.eng[(index_eng - index_seed_eng + len(alphabet.eng)) % len(alphabet.eng)]
            else:
                res += alphabet.eng[(index_eng - index_seed_rus + len(alphabet.eng)) % len(alphabet.eng)]
        elif index_rus >= 0:
            if index_seed_eng >= 0:
                res += alphabet.rus[(index_eng - index_seed_eng + len(alphabet.rus)) % len(alphabet.rus)]
            else:
                res += alphabet.rus[(index_eng - index_seed_rus + len(alphabet.rus)) % len(alphabet.rus)]
        else:
            res += i
            j -= 1
        j += 1
    return res
