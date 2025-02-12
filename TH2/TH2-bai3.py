import pandas as pd
from Crypto.Cipher import DES
import base64

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def giaima_DES(cipher_txt, key):
    txt = cipher_txt
    txt = base64.b64decode(txt)
    key = pad(key).encode('utf8')
    cipher = DES.new(key, DES.MODE_ECB)
    try:
        detxt = unpad(cipher.decrypt(txt)).decode('utf8')
    except UnicodeDecodeError:
        detxt = unpad(cipher.decrypt(txt)).decode('latin1')
    return detxt

def get_key(cipher_txt, key_list, plain_txt):
    for key in key_list:
        k = pad(key).encode('utf8')
        if len(k) > 8:
            continue
        if giaima_DES(cipher_txt, key) == plain_txt:
            return key

plain_txt = 'The treasure is under the coconut tree'
cipher_txt = 'lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=='

coun_list = pd.read_csv('country.csv')['value'].to_list()

key = get_key(cipher_txt, coun_list, plain_txt)
print("key =>", key)

cipher_txt_1 = 'LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=='
cipher_txt_2 = '5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9'

print(giaima_DES(cipher_txt_1, key))
print(giaima_DES(cipher_txt_2, key))