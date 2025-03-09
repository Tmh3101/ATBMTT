# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
import base64

def Char2Num(c):
	return ord(c) - 65

def Num2Char(n):
	return chr(n + 65)

def encryptAF(txt, a, b, m):
    r = ""
    for c in txt:
        if c != " ":
            kt = 97 <= ord(c) <= 122
            if kt:
                c = chr(ord(c) - 32)
            e = (a * Char2Num(c) + b) % m
            r = r + (Num2Char(e) if not kt else chr(ord(Num2Char(e)) + 32))
        else:
            r = r + "0"
    return r

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m!=0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp + x0
    return x0

def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        if c != "0":
            kt = 97 <= ord(c) <= 122
            if kt:
                c = chr(ord(c) - 32)
            e = (a1 * (Char2Num(c) - b)) % m
            r = r + (Num2Char(e) if not kt else chr(ord(Num2Char(e)) + 32))
        else:
            r = r + " "
    return r

class MAHOA_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa Affine")
        self.geometry('800x600')

        self.lbl = Label(
            self,
            text="CHƯƠNG TRÌNH DEMO",
            font=("Arial Bold", 20)
        )
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(
            self,
            text="MẬT MÃ ĐỐI XỨNG AFFINE",
            font=("Arial Bold", 15)
        )
        self.lb2.grid(column=1, row=2)

        self.plainlb3 = Label(
            self,
            text="Văn bản gốc",
            font=("Arial", 14)
        )
        self.plainlb3.grid(column=0, row=4)
        self.plaintxt = Entry(self, width=40)
        self.plaintxt.grid(column=1, row=4)

        self.KEYlb4 = Label(self, text="KEY PAIR",font=("Arial", 14))
        self.KEYlb4.grid(column=2, row=4)
        self.KEYA1 = Entry(self,width=3)
        self.KEYA1.grid(column=3, row=4)
        self.KEYB1 = Entry(self,width=5)
        self.KEYB1.grid(column=4, row=4)

        self.lb5 = Label(
            self,
            text="Văn bản được mã hóa",
            font=("Arial", 14)
        )
        self.lb5.grid(column=0, row=6)
        self.ciphertxt = Entry(self,width=40)
        self.ciphertxt.grid(column=1, row=6)

        self.lb6 = Label(
            self,
            text="Văn bản được giải mã",
            font=("Arial", 14)
        )
        self.lb6.grid(column=0, row=7)
        self.denctxt = Entry(self,width=40)
        self.denctxt.grid(column=1, row=7)

        self.btn_enc = Button(
            self,
            text="Mã Hóa",
            command=self.mahoa
        )
        self.btn_enc.grid(column=1, row=8)

        self.btn_dec = Button(
            self,
            text="Giải Mã ",
            command=self.giaima
        )
        self.btn_dec.grid(column=1, row=9)
        
        self.thoat = Button(
            self,
            text="Quay về màn hình chính",
            command=self.destroy
        )
        self.thoat.grid(column=1, row=10)
        
    def mahoa(self):
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        entxt = encryptAF(self.plaintxt.get(),a,b,m)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)

    def giaima(self):
        ci_txt = str(self.ciphertxt.get())
        a = int(self.KEYA1.get())
        b = int(self.KEYB1.get())
        m = 26
        de_txt = decryptAF(ci_txt, a, b, m)
        self.denctxt.insert(INSERT, de_txt)