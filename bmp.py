import cv2

import const


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
    for char in string:
        if ord(char) > const.ASCII_LEN:
            return False
    return True


def correct_for_img_size(img, string):
    """
    Проверяет "влезет" ли текст в картинку
    :param img: картинка
    :param string: текст
    :return: поместиться ли текст в картинку
    """
    return img.shape[0] * img.shape[1] > len(string) + len(const.END)


def encrypt(string, image_name):
    """
    Зашифровывает текст в картинку и ссохраняет ее
    :param string: текст который надо зашифровать
    :param image_name: название картинки
    """
    img = cv2.imread(image_name)
    if correct_for_img(string) and correct_for_img_size(img, string):
        string += const.END
        binary = bin_str(string)
        index = 0
        for row in img:
            for pixel in row:
                for k in range(3):
                    if index >= len(binary):
                        break
                    pixel[k] = format(pixel[k], "08b")[:-1] + binary[index]
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
    for row in image:
        for pixel in row:
            for k in range(3):
                storage += format(pixel[k], "08b")[-1]
    index = 0
    bytess = list()
    letter = ""
    for bit in storage:
        index += 1
        letter += bit
        if index >= const.BYTE_SIZE:
            bytes.append(letter)
            index = 0
            letter = ""
    res = ""
    for byte in bytess:
        res += chr(int(byte, 2))
        if res[-len(const.END):] == const.END:
            break
    return res[:-len(const.END)]
