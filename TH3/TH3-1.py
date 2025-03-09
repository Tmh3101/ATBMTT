# Họ và tên sinh viên: Tran Minh Hieu
# Mã số sinh viên: B2207521
# STT: 25

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
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

lbl = Label(window, text="CHƯƠNG TRÌNH DEMO",font=("Arial Bold", 20))
lbl.grid(column=1, row=1)

lb2 = Label(window, text="MẬT MÃ BAT ĐỐI XỨNG RSA",font=("Arial Bold", 15))
lb2.grid(column=1, row=2)

plainlb = Label(window, text="Văn bản gốc",font=("Arial", 14))
plainlb.grid(column=0, row=3)
plaintxt = Entry(window,width=50)
plaintxt.grid(column=1, row=3)

cipherlb = Label(window, text="Văn bản được mã hóa",font=("Arial", 14))
cipherlb.grid(column=0, row=4)
ciphertxt = Entry(window,width=50)
ciphertxt.grid(column=1, row=4)

encodelb = Label(window, text="Văn bản được giải mã",font=("Arial", 14))
encodelb.grid(column=0, row=5)
encodetxt = Entry(window,width=50)
encodetxt.grid(column=1, row=5)

prikeylb = Label(window, text="Khoa ca nhan",font=("Arial", 14))
prikeylb.grid(column=0, row=6)
prikeytxt = Text(window, width=50, height=8)
prikeytxt.grid(column=1, row=6)

pubkeylb = Label(window, text="Khoa cong khai",font=("Arial", 14))
pubkeylb.grid(column=0, row=7)
pubkeytxt = Text(window, width=50, height=8)
pubkeytxt.grid(column=1, row=7)

def generate_key():
    key = RSA.generate(1024)
    pri = save_file(
        key.exportKey('PEM'),
        'wb',
        'Lưu khóa cá nhân',
        (("All files", "*.*"), ("PEM files", "*.pem")),
        ".pem"
    )
    pub = save_file(
        key.publickey().exportKey('PEM'),
        'wb',
        'Lưu khóa công khai',
        (("All files", "*.*"),("PEM files", "*.pem")),
        ".pem"
    )
    prikeytxt.delete('1.0',END)
    prikeytxt.insert(END,key.exportKey('PEM'))
    pubkeytxt.delete('1.0',END)
    pubkeytxt.insert(END,key.publickey().exportKey('PEM'))

genkeybtn = Button(window, text="Tao khoa", command=generate_key)
genkeybtn.grid(column=1, row=8)

def save_file(content, _mode, _title, _filetypes, _defaultextension):
    f = filedialog.asksaveasfile(mode = _mode,
    initialdir = "D://ATBMTT//TH3//",
    title = _title,
    filetypes = _filetypes,
    defaultextension = _defaultextension)
    if f is None: return
    f.write(content)
    f.close()

def get_key(key_style):
    filename = filedialog.askopenfilename(initialdir = "D://ATBMTT//TH3//",
    title = "Open " + key_style,
    filetypes = (("PEM files", "*.pem"),("All files", "*.*")))
    if filename is None: return
    file = open(filename,"rb")
    key = file.read()
    file.close()
    return RSA.importKey(key)

def mahoa_rsa():
    txt = plaintxt.get().encode()
    pub_key = get_key("Public Key")
    cipher = PKCS1_v1_5.new(pub_key)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    ciphertxt.delete(0,END)
    ciphertxt.insert(INSERT,entxt)

encryptbtn = Button(window, text="Ma hoa", command=mahoa_rsa)
encryptbtn.grid(column=1, row=9)

def giaima_rsa():
    txt = ciphertxt.get()
    txt = base64.b64decode(txt)
    pri_key = get_key("Private Key")
    cipher = PKCS1_v1_5.new(pri_key)
    detxt = cipher.decrypt(txt, "Error")
    encodetxt.delete(0,END)
    encodetxt.insert(INSERT, detxt)

decryptbtn = Button(window, text="Giai ma", command=giaima_rsa)
decryptbtn.grid(column=1, row=10)

window.geometry('700x600')
window.mainloop()