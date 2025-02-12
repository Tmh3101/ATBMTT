# -*- coding: utf8 -*-
from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import DES
import base64

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcomea to Demo AT&BMTT")


# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ ĐỐI XỨNG DES",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)
plainlb = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb.grid(column=0, row=3)
plaintxt = Entry(window,width=50)
plaintxt.grid(column=1, row=3)

def upload_file():
    file_path = filedialog.askopenfilename(title='Chon file', filetypes=[('Text files', '*.txt'), ('All files', '*.*')])
    file = open(file_path, 'r')
    plaintxt.delete(0, END)
    plaintxt.insert(INSERT, file.read())

upload_file_button = Button(window, text='Upload file', command=upload_file)
upload_file_button.grid(column=2, row=3)

keylb = Label(window, text="Khóa",font=("Arial", 14))
keylb.grid(column=0, row=4)
keytxt = Entry(window,width=50)
keytxt.grid(column=1, row=4)
cipherlb = Label(window, text="Văn bản được mã hóa",font=("Arial", 14))
cipherlb.grid(column=0, row=5)
ciphertxt = Entry(window,width=50)
ciphertxt.grid(column=1, row=5)
decryplb = Label(window, text="Văn bản được giải mã",font=("Arial", 14))
decryplb.grid(column=0, row=6)
decryptxt = Entry(window,width=50)
decryptxt.grid(column=1, row=6)

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def mahoa_DES():
    txt = pad(plaintxt.get()).encode('utf8')
    key = pad(keytxt.get()).encode('utf8')
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0, END)
    ciphertxt.insert(INSERT, entxt)

# Tao nut co ten AFbtn
AFbtn = Button(window, text="Mã Hóa", command=mahoa_DES)
AFbtn.grid(column=0, row=7)

def giaima_DES():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    key = pad(keytxt.get()).encode('utf8')
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    decryptxt.delete(0, END)
    decryptxt.insert(INSERT, detxt)

deAFbtn = Button(window, text="Giai ma", command=giaima_DES)
deAFbtn.grid(column=1, row=7)

window.geometry('800x300')
window.mainloop()