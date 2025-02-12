# Ho va ten sinh vien: Tran Minh Hieu
# Ma so sinh vien: B2207521
# STT: 

#  space -> số -> in hoa -> in thường
def Char2Num(c):
    if ord(c) == 32:
        return ord(c) - 32
    if 48 <= ord(c) <= 57:
        return ord(c) - 47
    if 65 <= ord(c) <= 90:
        return ord(c) - 54
    return ord(c) - 60

def Num2Char(n):
    if n == 0:
        return chr(n + 32)
    if 1 <= n <= 10:
        return chr(n + 47)
    if 11 <= n <= 36:
        return chr(n + 54)
    return chr(n + 60)

def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0: x0 = temp + x0
    return x0

def decryptAF(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        # print(f'{c} - {Char2Num(c)}')
        e = (a1 * (Char2Num(c) - b)) % m
        r = r + Num2Char(e)
    return r

def gcd(a, m):
    while m != 0:
        a, m = m, a % m
    return a


cipher_txt = "gAdX5d6IXpvBX3XawdSLHIXIAdXCTITwdXL6XIPXHwdvIdXLI"
hint = "predict"

m = 63
for a in range(1, m):
    if gcd(a, m) == 1:
        for b in range(m):
            res = decryptAF(cipher_txt, a, b, m)
            print(f'{a} - {b} => {res}')
            if hint in res:
                print(f'(a = {a}, b = {b}) => {res}')

