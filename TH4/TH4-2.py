# Họ và tên sinh viên: Tran Minh Hieu
# Mã số sinh viên: B2207521
# STT: 25

from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from tkinter import *
import random
import pandas as pd

csdl = pd.read_csv('CSDL.csv')

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcomea to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="Tao tai khoan",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

tdnlb = Label(window, text="Ten dang nhap",font=("Arial", 14))
tdnlb.grid(column=0, row=2)
tdntxt = Entry(window,width=40)
tdntxt.grid(column=1, row=2)

mklb = Label(window, text="Mat khau",font=("Arial", 14))
mklb.grid(column=0, row=3)
mktxt = Entry(window,width=40)
mktxt.grid(column=1, row=3)

def hash_password(password):
    func = random.randint(0, 4)
    password = password.encode()
    res = ''
    if func == 0:
        res = MD5.new(password)
    elif func == 1:
        res = SHA1.new(password)
    elif func == 2:
        res = SHA256.new(password)
    else:
        res = SHA512.new(password)
    return res.hexdigest().upper()

def tao_tai_khoan():
    username = tdntxt.get()
    password = mktxt.get()
    if username in [username for username in csdl["username"]]:
        lbl = Label(window, text="Nguoi dung da ton tai",font=("Arial Bold", 8))
        lbl.grid(column=1, row=5)
    else:
        hash = hash_password(password)
        new_user = pd.DataFrame({'username': [username], 'password': [hash]})
        print(new_user)
        csdl.loc[len(csdl), :] = [username, hash]
        csdl.to_csv('CSDL.csv', index=False)

tmkButton = Button(window, text="Tao tai khoann", command=tao_tai_khoan)
tmkButton.grid(column=1, row=4)

window.geometry('600x400')
window.mainloop()