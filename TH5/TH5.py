# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
import base64
from des import MAHOA_DES
from affine import MAHOA_AFFINE
from rsa import MAHOA_RSA


class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)

        self.mahoa_Affine = Button(
            text="Mã hóa Affine",
            font=("Times New Roman", 11),
            command=self.affine
        )

        self.mahoa_DES = Button(
            text="Mã hóa DES",
            font=("Times New Roman", 11),
            command=self.des
        )

        self.mahoa_RSA = Button(
            text="Mã hóa RSA",
            font=("Times New Roman", 11),
            command=self.rsa
        )

        self.mahoa_Affine.pack()
        self.mahoa_DES.pack()
        self.mahoa_RSA.pack()

        self.thoat = Button(
            text="Kết Thúc",
            font=("Times New Roman", 11),
            command=quit
        )
        self.thoat.pack()

    def des(self):
        MAHOA_DES(self)

    def affine(self):
        MAHOA_AFFINE(self)

    def rsa(self):
        MAHOA_RSA(self)

def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry('300x200')
    MainWindow(window)
    window.mainloop()

main()