import cv2


def bin_str(string):
    """
    Переводит в двоичный формат посимвольно
    :param string: строка которую нужно представить в двочном коде
    :return: двоичный код который содержит коды символов изначальной строки
    """
    res = ""
    for char in string:
        res += format(ord(char), "08b")
    return res


def correct_for_img(string):
    """
    Проверяет являетсся ли строка корректной для зашифровки (принадлежит ASCII)
    :param string: строка для проверки
    :return: является ли строка корректной
    """
    for i in string:
        if ord(i) > 127:
            return False
    return True


def correct_for_img_size(img, string):
    """
    Проверяет "влезет" ли текст в картинку
    :param img: картинка
    :param string: текст
    :return: поместиться ли текст в картинку
    """
    if img.shape[0] * img.shape[1] < len(string) + 6:
        return False
    return True


def encrypt(string, image_name):
    """
    Зашифровывает текст в картинку и ссохраняет ее
    :param string: текст который надо зашифровать
    :param image_name: название картинки
    :return: ничего
    """
    img = cv2.imread(image_name)
    if correct_for_img(string) and correct_for_img_size(img, string):
        string += "endstr"
        binary = bin_str(string)
        index = 0
        for i in img:
            for j in i:
                for k in range(3):
                    if index >= len(binary):
                        break
                    j[k] = format(j[k], "08b")[:-1] + binary[index]
                    index += 1
    cv2.imwrite(image_name, img)


def decode(image_name):
    """
    Достает текст, который был записан в картинку
    :param image_name: название картинки
    :return: текст, содержащийся в картинке
    """
    image = cv2.imread(image_name)
    storage = ""
    for i in image:
        for j in i:
            for k in range(3):
                storage += format(j[k], "08b")[-1]
    index = 0
    bytes = list()
    letter = ""
    for i in storage:
        index += 1
        letter += i
        if index >= 8:
            bytes.append(letter)
            index = 0
            letter = ""
    res = ""
    for i in bytes:
        res += chr(int(i, 2))
        if res[-6:] == "endstr":
            break
    return res[:-6]
