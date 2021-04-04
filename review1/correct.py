import alphabet


def correct(string, seed):
    """
    Проверяет строку, чтобы она была исключительно из букв причем одного алфавита
    :param string: строка для проверки
    :param seed: если !=None вторая строка для проверки
    :return: являются ли строки "правильными"
    """
    arg1 = True
    arg2 = True
    if seed != None:
        for i, j in zip(string, seed):
            arg1 = i in alphabet.rus and arg1 and j in alphabet.rus
            arg2 = i in alphabet.eng and arg2 and j in alphabet.eng
        return arg1 or arg2
    else:
        for i in string:
            arg1 = i in alphabet.rus and arg1
            arg2 = i in alphabet.eng and arg2
        return arg1 or arg2
