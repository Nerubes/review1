import alphabet


def correct(string, seed):
    """
    Проверяет на то, чтобы в тексте были только буквы одного алфавита
    :param string: строка для проверки
    :param seed: вторая строка для проверки
    :return: являются ли строки "правильными"
    """
    arg1 = True
    arg2 = True
    for i, j in zip(string, seed):
        arg1 = i in alphabet.rus and arg1 and j in alphabet.rus
        arg2 = i in alphabet.eng and arg2 and j in alphabet.eng
    return arg1 or arg2


def correction(string):
    """
    Удаляет пробелы в начале строки
    :param string: строка в которой нужно удалить пробелы
    :return: строка без пробелов
    """
    if len(string) != 0 and string[0] == " ":
        string = string[1:]
    return string
