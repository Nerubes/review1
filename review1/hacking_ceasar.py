import collections

import alphabet


def frequency_analysis(string):
    """
    Анализирует строку на наличие в ней букв и определяет самую частую, по ней определяет ключ в коде цезаря
    :param string: строка для анализа
    :return: ключ цезаря
    """
    count = collections.Counter()
    for j in string:
        count[j] += 1
    most_common = str(count.most_common()[0])
    if alphabet.eng.find(string[0]) >= 0:
        return (len(alphabet.eng) - alphabet.eng.find(most_common) + alphabet.eng.find('e')) % len(alphabet.eng)
    else:
        return (len(alphabet.rus) - alphabet.rus.find(most_common) + alphabet.rus.find('о')) % len(alphabet.rus)
