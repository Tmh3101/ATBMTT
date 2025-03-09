# Họ và tên sinh viên: Tran Minh Hieu
# Mã số sinh viên: B2207521
# STT: 25

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64
from tkinter import *
from tkinter import filedialog

# Khoi tao man hinh chinh
window = Tk()
window.title("Welcomea to Demo AT&BMTT")

# Them cac control
lb0 = Label(window, text=" ",font=("Arial Bold", 10))
lb0.grid(column=0, row=0)

lbl = Label(window, text="CHƯƠNG TRÌNH BAM",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

plainlb = Label(window, text="Văn bản",font=("Arial", 14))
plainlb.grid(column=0, row=2)
plaintxt = Entry(window,width=80)
plaintxt.grid(column=1, row=2)

def hashing():
    content = plaintxt.get().encode()
    func = hashmode.get()
    if func == 0:
        result = MD5.new(content)
    elif func == 1:
        result = SHA1.new(content)
    elif func == 2:
        result = SHA256.new(content)
    elif func == 3:
        result = SHA512.new(content)
    rs = result.hexdigest().upper()
    hashvalue.delete(0,END)
    hashvalue.insert(INSERT,rs)

radioGroup = LabelFrame(window, text = "Hàm băm")
radioGroup.grid(row=3, column=1)
hashmode = IntVar()
hashmode.set(-1)

md5_func = Radiobutton(
    radioGroup,
    text="Hash MD5",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=0,
    command=hashing
)
md5_func.grid(row=4, column=0)

sha1_func = Radiobutton(
    radioGroup,
    text="Hash SHA1",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=1,
    command=hashing
)
sha1_func.grid(row=5, column=0)

sha256_func = Radiobutton(
    radioGroup,
    text="Hash SHA256",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=2,
    command=hashing
)
sha256_func.grid(row=6, column=0)

sha512_func = Radiobutton(
    radioGroup,
    text="Hash SHA512",
    font=("Times New Roman", 11),
    variable=hashmode,
    value=3,
    command=hashing
)
sha512_func.grid(row=7, column=0)

hashlb = Label(window, text="Gia tri Bam",font=("Arial", 14))
hashlb.grid(column=0, row=4)
hashvalue = Entry(window,width=80)
hashvalue.grid(column=1, row=4)

window.geometry('600x400')
window.mainloop()