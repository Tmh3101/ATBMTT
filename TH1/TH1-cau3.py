# Ho va ten sinh vien: Tran Minh Hieu
# Ma so sinh vien: B2207521
# STT: 


# -*- coding: utf8 -*-
from tkinter import *

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)
lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)
lb2 = Label(window, text="MẬT MÃ AFFINE",font=("Arial Bold", 15))
lb2.grid(column=0, row=2)
plainlb3 = Label(window, text="PLAIN TEXT",font=("Arial", 14))
plainlb3.grid(column=0, row=3)
plaintxt = Entry(window,width=20)
plaintxt.grid(column=1, row=3)
KEYlb4 = Label(window, text="KEY PAIR",font=("Arial", 14))
KEYlb4.grid(column=2, row=3)
KEYA1 = Entry(window,width=3)
KEYA1.grid(column=3, row=3)
KEYB1 = Entry(window,width=5)
KEYB1.grid(column=4, row=3)

plainlb4 = Label(window, text="CIPHER TEXT",font=("Arial", 14))
plainlb4.grid(column=0, row=4)
ciphertxt3 = Entry(window,width=20)
ciphertxt3.grid(column=1, row=4)

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

def mahoa():
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    entxt = encryptAF(plaintxt.get(),a,b,m)
    ciphertxt3.delete(0,END)
    ciphertxt3.insert(INSERT,entxt)

# Tao nut co ten AFbtn
AFbtn = Button(window, text="Mã Hóa", command=mahoa)
AFbtn.grid(column=5, row=3)


res_txt = Entry(window,width=20)
res_txt.grid(column=3, row=4)

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

def giaima():
    ci_txt = str(ciphertxt3.get())
    a = int(KEYA1.get())
    b = int(KEYB1.get())
    m = 26
    de_txt = decryptAF(ci_txt, a, b, m)
    res_txt.insert(INSERT, de_txt)

deAFbtn = Button(window, text="Giai ma", command=giaima)
deAFbtn.grid(column=2, row=4)

window.geometry('800x300')
window.mainloop()