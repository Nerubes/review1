from functools import partial
import tkinter
import tkinter.ttk

import ceasar
import hacking_ceasar
import vernam
import vigenere


def encrypting(string, seed, where_to_put_answer, what_cipher):
    """
    Зашифровывает строку string используя ключ seed, ответ помещает в where_to_put_answer
    :param string: текст для шиврования
    :param seed: ключ
    :param where_to_put_answer: поле, куда помещается ответ
    :param what_cipher: название шифра
    :return: ничего
    """
    where_to_put_answer.delete(1.0, tkinter.END)
    if what_cipher.get() == "Ceasar":
        if not seed.get().isdigit() and not ceasar.correct(string):
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, ceasar.encrypt(string.get(), int(seed.get())))
    elif what_cipher.get() == "Vernam":
        if not vernam.correct(string.get(), seed.get()) or len(seed.get()) < len(string.get()) or len(
                string.get()) == 0:
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vernam.encrypt(string.get(), seed.get()))
    else:
        if not seed.get().isalpha():
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vigenere.encrypt(string.get(), seed.get()))


def decoding(string, seed, where_to_put_answer, what_cipher):
    """
    Расшифровывает строку string используя ключ seed, ответ помещает в where_to_put_answer
    :param string: текст для расшифровки
    :param seed: ключ
    :param where_to_put_answer: поле, куда помещается ответ
    :param what_cipher: название шифра
    :return: ничего
    """
    where_to_put_answer.delete(1.0, tkinter.END)
    if what_cipher.get() == "Ceasar":
        if not seed.get().isdigit() and not ceasar.correct(string):
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, ceasar.decode(string.get(), int(seed.get())))
    elif what_cipher.get() == "Vernam":
        if not vernam.correct(string.get(), seed.get()) or len(seed.get()) != len(string.get()) or len(string.get()) == 0:
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vernam.encrypt(string.get(), seed.get()))
    else:
        if not seed.get().isalpha():
            where_to_put_answer.insert(tkinter.END, "Incorrect Input. Try again")
        else:
            where_to_put_answer.insert(tkinter.END, vigenere.decode(string.get(), seed.get()))


def hacking(string, where_to_put_answer):
    where_to_put_answer.delete(1.0, tkinter.END)
    if len(string.get()) != 0 and hacking_ceasar.correct(string.get()):
        seed = hacking_ceasar.frequency_analysis(string)
        where_to_put_answer.insert(tkinter.END, "key for Ceasar ")
        where_to_put_answer.insert(tkinter.END, seed)
        where_to_put_answer.insert(tkinter.END, "\nOriginal string")
        where_to_put_answer.insert(tkinter.END, ceasar.decode(string, seed))


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("cryptography")
    window.geometry("1100x600")
    label_chose = tkinter.Label(window, text="Chose your code ->")
    label_chose.grid(column=0, row=0)
    label_hack = tkinter.Label(window, text="Here to type text for hacking ->")
    label_hack.grid(column=3, row=0)
    str_for_encrypting = tkinter.Entry(window, width=30)
    str_for_encrypting.grid(column=0, row=2, padx=5, pady=10)
    str_for_hacking = tkinter.Entry(window, width=40)
    str_for_hacking.grid(column=4, row=0, padx=5, pady=10)
    column_for_seed = tkinter.Entry(window, width=30)
    column_for_seed.grid(column=0, row=3, padx=5, pady=10)
    output = tkinter.Text(window, width=40, height=15)
    output.grid(column=0, row=4, padx=5, pady=10)
    output_hack = tkinter.Text(window, width=40, height=5)
    output_hack.grid(column=4, row=3, padx=5, pady=10)
    cipher = tkinter.ttk.Combobox(window, state="readonly")
    cipher.grid(column=1, row=0)
    cipher['values'] = ("Ceasar", "Vernam", "Vigenere")
    cipher.current(0)
    encrypt = partial(encrypting, str_for_encrypting, column_for_seed, output, cipher)
    decode = partial(decoding, str_for_encrypting, column_for_seed, output, cipher)
    hack = partial(hacking, str_for_hacking, output_hack)
    btn_for_encrypting = tkinter.Button(window, text="Encrypt", command=encrypt)
    btn_for_decoding = tkinter.Button(window, text="Decode", command=decode)
    btn_for_hack = tkinter.Button(window, text="Hack", command=hack)
    btn_for_encrypting.grid(column=0, row=5, padx=5, pady=10)
    btn_for_decoding.grid(column=0, row=6, padx=5, pady=10)
    btn_for_hack.grid(column=4, row=1, padx=5, pady=10)

    window.mainloop()
