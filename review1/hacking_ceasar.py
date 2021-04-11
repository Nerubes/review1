import collections

import alphabet


def frequency_analysis(string):
    """
    Анализирует строку на наличие в ней букв и определяет самую частую, по ней определяет ключ в коде цезаря
    :param string: строка для анализа
    :return: ключ цезаря
    """
    count = collections.Counter()
    for letter in string:
        count[letter] += 1
    most_common = str(count.most_common()[0])
    if alphabet.eng.find(string[0]) >= 0:
        return (alphabet.eng.find(most_common[2]) + alphabet.eng.find(" ")) % len(alphabet.eng)
    else:
        return (alphabet.rus.find(most_common[2]) + alphabet.rus.find(" ")) % len(alphabet.rus)
