# -*- coding: utf8 -*-
from tkinter import *
import tkinter as tk
from Crypto.Cipher import DES
import base64

def pad(s):
    #Them vao cuoi so con thieu cho du boi cua 8
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

class MAHOA_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry('800x600')

        self.lbl = Label(
            self,
            text="CHƯƠNG TRÌNH DEMO",
            font=("Arial Bold", 20)
        )
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(
            self,
            text="MẬT MÃ ĐỐI XỨNG DES",
            font=("Arial Bold", 15)
        )
        self.lb2.grid(column=1, row=2)

        self.plainlb3 = Label(
            self,
            text="Văn bản gốc",
            font=("Arial", 14)
        )
        self.plainlb3.grid(column=0, row=4)

        self.plaintxt = Entry(self, width=100)
        self.plaintxt.grid(column=1, row=4)

        self.lb4 = Label(
            self,
            text="Khóa",
            font=("Arial", 14)
        )
        self.lb4.grid(column=0, row=5)

        self.keytxt = Entry(self, width=100)
        self.keytxt.grid(column=1, row=5)

        self.lb5 = Label(
            self,
            text="Văn bản được mã hóa",
            font=("Arial", 14)
        )
        self.lb5.grid(column=0, row=6)

        self.ciphertxt = Entry(self,width=100)
        self.ciphertxt.grid(column=1, row=6)

        self.lb6 = Label(
            self,
            text="Văn bản được giải mã",
            font=("Arial", 14)
        )
        self.lb6.grid(column=0, row=7)

        self.denctxt = Entry(self,width=100)
        self.denctxt.grid(column=1, row=7)

        self.btn_enc = Button(
            self,
            text="Mã Hóa",
            command=self.mahoa_DES
        )
        self.btn_enc.grid(column=1, row=9)

        self.btn_dec = Button(
            self,
            text="Giải Mã ",
            command=self.giaima_DES
        )
        self.btn_dec.grid(column=1, row=10)
        
        self.thoat = Button(
            self,
            text="Quay về màn hình chính",
            command=self.destroy
        )
        self.thoat.grid(column=1, row=11)

    def mahoa_DES(self):
        txt = pad(self.plaintxt.get()).encode()
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)
        
    def giaima_DES(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        key = pad(self.keytxt.get()).encode()
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))
        self.denctxt.delete(0,END)
        self.denctxt.insert(INSERT,detxt)