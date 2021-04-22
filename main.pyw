from functools import partial
import cv2
import tkinter
import tkinter.ttk

import bmp
import ceasar
import correct
import const
import hacking_ceasar
import vernam
import vigenere


def encrypting(string_get, seed_get, where_to_put_answer, what_cipher):
    """
    Зашифровывает строку string используя ключ seed, ответ помещает в where_to_put_answer
    :param string_get : текст для шиврования
    :param seed_get: ключ
    :param where_to_put_answer: поле, куда помещается ответ
    :param what_cipher: название шифра
    """
    string = string_get.get().lower()
    string = correct.correction(string)
    seed = seed_get.get()
    where_to_put_answer.delete(1.0, tkinter.END)
    if what_cipher.get() == "Ceasar":
        if not seed.isdigit():
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, ceasar.encrypt(string, int(seed), const.ENCRYPT))
    elif what_cipher.get() == "Vernam":
        if not correct.correct(string, seed.lower()) or len(seed) < len(string) or len(
                string) == 0:
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vernam.encrypt(string, seed.lower()))
    else:
        if not seed.isalpha() or not correct.correct(string, seed.lower()):
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vigenere.encrypt(string, seed.lower(), const.ENCRYPT))


def decoding(string_get, seed_get, where_to_put_answer, what_cipher):
    """
    Расшифровывает строку string используя ключ seed, ответ помещает в where_to_put_answer
    :param string_get: текст для расшифровки
    :param seed_get: ключ
    :param where_to_put_answer: поле, куда помещается ответ
    :param what_cipher: название шифра
    """
    string = string_get.get().lower()
    string = correct.correction(string)
    seed = seed_get.get()
    where_to_put_answer.delete(1.0, tkinter.END)
    if what_cipher.get() == "Ceasar":
        if not seed.isdigit():
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, ceasar.encrypt(string, int(seed), const.DECODE))
    elif what_cipher.get() == "Vernam":
        if not correct.correct(string, seed.lower()) or len(seed) != len(string) or len(string) == 0:
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vernam.encrypt(string, seed))
    else:
        if not seed.isalpha() or not correct.correct(string, seed.lower()):
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vigenere.encrypt(string, seed.lower(), const.DECODE))


def hacking(string_get, where_to_put_answer):
    """
    Расшифровывает строку зашифрованную шифром цезаря с неизвестным ключем
    :param string_get: строка которую нужно расшифровать
    :param where_to_put_answer: поле куда помещать ответ
    """
    string = string_get.get()
    where_to_put_answer.delete(1.0, tkinter.END)
    if len(string) != 0:
        seed = hacking_ceasar.frequency_analysis(string)
        where_to_put_answer.insert(tkinter.END, "key for Ceasar ")
        where_to_put_answer.insert(tkinter.END, seed)
        where_to_put_answer.insert(tkinter.END, "\nOriginal string: ")
        where_to_put_answer.insert(tkinter.END, ceasar.encrypt(string, seed), const.DECODE)
    else:
        where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")


def encrypting_img(name_get, string_get):
    """
    Зашифровывает текст в картинку в формате bmp или png
    :param name_get: название картинки в которую надо зашифровать текст
    :param string_get: текст, который надо зашифровать
    """
    bmp.encrypt(string_get.get(), name_get.get())


def decoding_img(name_get, where_to_put_answer):
    """
    Расшифровывает текст из картинки в формате bmp или png
    :param name_get: название картинки из которой надо извелчь текст
    :param where_to_put_answer: поле куда поместить ответ
    """
    where_to_put_answer.delete(1.0, tkinter.END)
    where_to_put_answer.insert(tkinter.END, bmp.decode(name_get.get()))


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("cryptography")
    window.geometry("1150x700")
    label_chose = tkinter.Label(window, text="Chose your code ->")
    label_chose.grid(column=0, row=0)
    label_hack = tkinter.Label(window, text="Here to type text for hacking ->")
    label_hack.grid(column=3, row=0)
    label_img = tkinter.Label(window, text="Type here text to write in image->")
    label_img.grid(column=3, row=5)
    label_img = tkinter.Label(window, text="Type here name of the image ->")
    label_img.grid(column=3, row=4)
    str_for_encrypting = tkinter.Entry(window, width=30)
    str_for_encrypting.grid(column=0, row=2, padx=5, pady=10)
    str_for_hacking = tkinter.Entry(window, width=40)
    str_for_hacking.grid(column=4, row=0, padx=5, pady=10)
    str_for_img = tkinter.Entry(window, width=30)
    str_for_img.grid(column=4, row=4, padx=5, pady=10)
    str_for_img_encrypt = tkinter.Entry(window, width=30)
    str_for_img_encrypt.grid(column=4, row=5, padx=5, pady=10)
    column_for_seed = tkinter.Entry(window, width=30)
    column_for_seed.grid(column=0, row=3, padx=5, pady=10)
    output = tkinter.Text(window, width=40, height=15)
    output.grid(column=0, row=4, padx=5, pady=10)
    str_for_img_output = tkinter.Text(window, width=40, height=5)
    str_for_img_output.grid(column=3, row=7, padx=5, pady=10)
    output_hack = tkinter.Text(window, width=40, height=5)
    output_hack.grid(column=4, row=3, padx=5, pady=10)
    cipher = tkinter.ttk.Combobox(window, state="readonly")
    cipher.grid(column=1, row=0)
    cipher["values"] = ("Ceasar", "Vernam", "Vigenere")
    cipher.current(0)
    encrypt = partial(encrypting, str_for_encrypting, column_for_seed, output, cipher)
    decode = partial(decoding, str_for_encrypting, column_for_seed, output, cipher)
    hack = partial(hacking, str_for_hacking, output_hack)
    encrypt_img = partial(encrypting_img, str_for_img, str_for_img_encrypt)
    decode_img = partial(decoding_img, str_for_img, str_for_img_output)
    btn_for_encrypting = tkinter.Button(window, text="Encrypt", command=encrypt)
    btn_for_decoding = tkinter.Button(window, text="Decode", command=decode)
    btn_for_hack = tkinter.Button(window, text="Hack", command=hack)
    btn_for_encrypting_img = tkinter.Button(window, text="Encrypt", command=encrypt_img)
    btn_for_decoding_img = tkinter.Button(window, text="Decode", command=decode_img)
    btn_for_encrypting.grid(column=0, row=5, padx=5, pady=10)
    btn_for_decoding.grid(column=0, row=6, padx=5, pady=10)
    btn_for_hack.grid(column=4, row=1, padx=5, pady=10)
    btn_for_encrypting_img.grid(column=3, row=6)
    btn_for_decoding_img.grid(column=4, row=6)
    window.mainloop()
