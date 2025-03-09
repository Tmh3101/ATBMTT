# Họ và tên sinh viên: Tran Minh Hieu
# Mã số sinh viên: B2207521
# STT: 25

from math import gcd
from Crypto.Util.number import inverse

def gen_keys(p, q):
    n = p * q
    phi_euler = (p - 1) * (q - 1)
    for i in range(2, phi_euler):
        if gcd(i, phi_euler) == 1:
            e = i
            break
    d = inverse(e, phi_euler)
    pub_key = (e, n)
    pri_key = (d, n)
    return pub_key, pri_key

def encrypt(plain_txt, pub_key):
    e, n = pub_key
    cipher_txt = [pow(ord(c), e, n) for c in plain_txt]
    return cipher_txt

def decrypt(cipher_txt, pri_key):
    d, n = pri_key
    mess = ''.join([chr(pow(c, d, n)) for c in cipher_txt])
    return mess

p = 751
q = 769
pub_key, pri_key = gen_keys(p, q)

plain_txt = "SECRET"
cipher_txt = encrypt(plain_txt, pub_key)
print(cipher_txt)

entxt = decrypt(cipher_txt, pri_key)
print(entxt)
