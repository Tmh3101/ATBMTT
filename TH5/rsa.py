# -*- coding: utf8 -*-
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
import tkinter as tk
from tkinter import filedialog

def read_file():
    filename = filedialog.askopenfilename(
        initialdir = "D://ATBMTT//TH5//",
        title = "Open File",
        filetypes = (("Text files", "*.txt"),("All files", "*.*"))
    )
    if filename is None: return
    file = open(filename,"rb")
    plaintxt = file.read()
    file.close()
    return plaintxt

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(
        mode = _mode,
        initialdir = "D://ATBMTT//TH5//",
        title = _title,
        filetypes = _filetypes,
        defaultextension = _defaultextension
    )
    if f is None: return
    f.write(content)
    f.close()

def get_key(key_style):
    filename = filedialog.askopenfilename(
        initialdir = "D://ATBMTT//TH5//",
        title = "Open " + key_style,
        filetypes = (("PEM files", "*.pem"),("All files", "*.*"))
    )
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

class MAHOA_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa RSA")
        self.geometry('800x600')

        self.lbl = Label(
            self,
            text="CHƯƠNG TRÌNH DEMO",
            font=("Arial Bold", 20)
        )
        self.lbl.grid(column=1, row=1)

        self.lb2 = Label(
            self,
            text="MẬT MÃ BAT ĐỐI XỨNG RSA",
            font=("Arial Bold", 15)
        )
        self.lb2.grid(column=1, row=2)

        self.plainlb = Label(self, text="Văn bản gốc",font=("Arial", 14))
        self.plainlb.grid(column=0, row=3)
        self.plaintxt = Entry(self,width=50)
        self.plaintxt.grid(column=1, row=3)

        self.cipherlb = Label(self, text="Văn bản được mã hóa",font=("Arial", 14))
        self.cipherlb.grid(column=0, row=4)
        self.ciphertxt = Entry(self,width=50)
        self.ciphertxt.grid(column=1, row=4)

        self.encodelb = Label(self, text="Văn bản được giải mã",font=("Arial", 14))
        self.encodelb.grid(column=0, row=5)
        self.encodetxt = Entry(self,width=50)
        self.encodetxt.grid(column=1, row=5)

        self.prikeylb = Label(self, text="Khoa ca nhan",font=("Arial", 14))
        self.prikeylb.grid(column=0, row=6)
        self.prikeytxt = Text(self, width=50, height=8)
        self.prikeytxt.grid(column=1, row=6)

        self.pubkeylb = Label(self, text="Khoa cong khai",font=("Arial", 14))
        self.pubkeylb.grid(column=0, row=7)
        self.pubkeytxt = Text(self, width=50, height=8)
        self.pubkeytxt.grid(column=1, row=7)

        self.genkeybtn = Button(
            self,
            text="Tao khoa", 
            command=self.generate_key
        )
        self.genkeybtn.grid(column=1, row=8)

        self.encryptbtn = Button(
            self,
            text="Ma hoa",
            command=self.mahoa_rsa
        )
        self.encryptbtn.grid(column=1, row=9)

        self.decryptbtn = Button(
            self,
            text="Giai ma",
            command=self.giaima_rsa
        )
        self.decryptbtn.grid(column=1, row=10)

        self.openfilebtn = Button(
            self,
            text="Mo file plaintxt",
            command=self.open_plaintxt_file
        )
        self.openfilebtn.grid(column=1, row=11)

        self.thoat = Button(
            self,
            text="Quay về màn hình chính",
            command=self.destroy
        )
        self.thoat.grid(column=1, row=12)

    def open_plaintxt_file(self):
        self.plaintxt.delete(0, END)
        self.plaintxt.insert(INSERT, read_file())

    def generate_key(self):
        key = RSA.generate(1024)
        save_file(
            key.exportKey('PEM'),
            'wb',
            'Lưu khóa cá nhân',
            (("All files", "*.*"), ("PEM files", "*.pem")),
            ".pem"
        )
        save_file(
            key.publickey().exportKey('PEM'),
            'wb',
            'Lưu khóa công khai',
            (("All files", "*.*"),("PEM files", "*.pem")),
            ".pem"
        )
        self.prikeytxt.delete('1.0',END)
        self.prikeytxt.insert(END,key.exportKey('PEM'))
        self.pubkeytxt.delete('1.0',END)
        self.pubkeytxt.insert(END,key.publickey().exportKey('PEM'))

    def mahoa_rsa(self):
        txt = self.plaintxt.get().encode()
        pub_key = get_key("Public Key")
        cipher = PKCS1_v1_5.new(pub_key)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        self.ciphertxt.delete(0,END)
        self.ciphertxt.insert(INSERT,entxt)

    def giaima_rsa(self):
        txt = self.ciphertxt.get()
        txt = base64.b64decode(txt)
        pri_key = get_key("Private Key")
        cipher = PKCS1_v1_5.new(pri_key)
        detxt = cipher.decrypt(txt, "Error")
        self.encodetxt.delete(0,END)
        self.encodetxt.insert(INSERT, detxt)
