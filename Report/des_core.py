"""
zfill(n) - Tự động thêm số 0 vào bên trái để đảm bảo output luôn có n bit.
[2:] - Loại bỏ tiền tố (2 ký tự đầu tiên). Tiền tố: nhị phân - 0b, thập lục phân - 0x.
"""

def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(64)

def bin_to_hex(binary):
    return hex(int(binary, 2))[2:].zfill(16)

def dec_to_bin(decimal):
    return bin(decimal)[2:].zfill(4)

"""
permute: hàm hoán vị các vị trí trong block theo từng giá trị trong table.
ví dụ: permute("1100", [2, 1, 4, 3], 4) -> "1010"
"""
def permute(block, table, n):
    return "".join(block[i - 1] for i in table)[:n]

""""
left_shift: hàm dịch trái key đi shifts bit theo vòng.
Hiểu một cách đơn giản thì nó sẽ chia key thành 2 phần tại vị trí shifts, sau đó đổi thứ tự 2 phần.
ví dụ: left_shift("11001100", 2) -> "00110011"
"""
def left_shift(key, shifts):
    return key[shifts:] + key[:shifts]


def generate_round_keys(key):
    key = hex_to_bin(key)

    """3
    pc1:
        Gồm 56 chữ số: Số nhỏ nhất là 1 và lớn nhất là 64, không liên tục.
        Các số còn thiếu là 8, 16, 24, 32, 40, 48, 56, 64 (các bit chẵn - parity bits)
        --> Các bit còn thiếu dùng để kiểm tra chắn lẻ (lỗi truyền thông tin dữ liệu).
        VD: Bit đầu tiên của kết quả (vị trí 1) được lấy từ bit 57 của plaintext
    """
    pc1 = [
        57, 49, 41, 33, 25, 17, 9,  1,  58, 50, 42, 34, 26, 18,
        10, 2,  59, 51, 43, 35, 27, 19, 11, 3,  60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15, 7,  62, 54, 46, 38, 30, 22,
        14, 6,  61, 53, 45, 37, 29, 21, 13, 5,  28, 20, 12, 4
    ]

    """
    pc2:
        Gồm 48 chữ số: Số nhỏ nhất là 1 và lớn nhất là 56, không liên tục.
        Các số còn thiếu là 8, 16, 24, 32, 40, 48 (các bit chẵn - parity bits)
        --> Các bit còn thiếu dùng để kiểm tra chắn lẻ (lỗi truyền thông tin dữ liệu).
    """
    pc2 = [14, 17, 11, 24, 1,  5,  3,  28, 15, 6,  21, 10, 23, 19,
           12, 4,  26, 8,  16, 7,  27, 20, 13, 2,  41, 52, 31, 37,
           47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53,
           46, 42, 50, 36, 29, 32]
    
    """
    shift_table: số lượng bit cần dịch trái ở mỗi vòng lặp. 16 vòng lặp nên có 16 giá trị.
    Giá trị của shift_table được theo chuẩn của thuật toán DES. Tránh được việc lặp lại các khóa con.
    """
    shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    
    key = permute(key, pc1, 56)
    c, d = key[:28], key[28:]
    round_keys = []
    
    for shift in shift_table:
        c = left_shift(c, shift)
        d = left_shift(d, shift)
        round_keys.append(permute(c + d, pc2, 48))
    
    return round_keys
                                                                            

""""
ip: bảng hoán vị IP ban đầu (initial permutation).
ip_inv: bảng hoán vị IP ngược (final permutation hay inverse permutation).
Số lượng phần tử đều là 64.
"""
ip = [ 
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]                                                                                     

ip_inv = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9,  49, 17, 57, 25
]                                                                           

""""
Cách trả S-box để thay thế 6 bit đầu vào thành 4 bit đầu ra.

Chia 48-bit input thành 8 phần 6-bit.
Mỗi phần 6-bit sẽ được truyền vào 1 S-box tương ứng.
VD: Phần đầu tiên:
 011000 → S-Box 1:
    Hàng: bit 1 và 6 (00) → 0
    Cột: bit 2-5 (1100) → 12
    S-Box 1[0][12] = 5 → 0101
    --> Chuyển từ 011000 thành 0101
"""
sbox = [
    # S-Box 1
    [
        [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
        [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
        [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
        [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
    ],
    # S-Box 2
    [
        [15,  1,  8, 14,  6, 11,  3,  4,  9,  7,  2, 13, 12,  0,  5, 10],
        [ 3, 13,  4,  7, 15,  2,  8, 14, 12,  0,  1, 10,  6,  9, 11,  5],
        [ 0, 14,  7, 11, 10,  4, 13,  1,  5,  8, 12,  6,  9,  3,  2, 15],
        [13,  8, 10,  1,  3, 15,  4,  2, 11,  6,  7, 12,  0,  5, 14,  9]
    ],
    # S-Box 3
    [
        [10,  0,  9, 14,  6,  3, 15,  5,  1, 13, 12,  7, 11,  4,  2,  8],
        [13,  7,  0,  9,  3,  4,  6, 10,  2,  8,  5, 14, 12, 11, 15,  1],
        [13,  6,  4,  9,  8, 15,  3,  0, 11,  1,  2, 12,  5, 10, 14,  7],
        [ 1, 10, 13,  0,  6,  9,  8,  7,  4, 15, 14,  3, 11,  5,  2, 12]
    ],
    # S-Box 4
    [
        [ 7, 13, 14,  3,  0,  6,  9, 10,  1,  2,  8,  5, 11, 12,  4, 15],
        [13,  8, 11,  5,  6, 15,  0,  3,  4,  7,  2, 12,  1, 10, 14,  9],
        [10,  6,  9,  0, 12, 11,  7, 13, 15,  1,  3, 14,  5,  2,  8,  4],
        [ 3, 15,  0,  6, 10,  1, 13,  8,  9,  4,  5, 11, 12,  7,  2, 14]
    ],
    # S-Box 5
    [
        [ 2, 12,  4,  1,  7, 10, 11,  6,  8,  5,  3, 15, 13,  0, 14,  9],
        [14, 11,  2, 12,  4,  7, 13,  1,  5,  0, 15, 10,  3,  9,  8,  6],
        [ 4,  2,  1, 11, 10, 13,  7,  8, 15,  9, 12,  5,  6,  3,  0, 14],
        [11,  8, 12,  7,  1, 14,  2, 13,  6, 15,  0,  9, 10,  4,  5,  3]
    ],
    # S-Box 6
    [
        [12,  1, 10, 15,  9,  2,  6,  8,  0, 13,  3,  4, 14,  7,  5, 11],
        [10, 15,  4,  2,  7, 12,  9,  5,  6,  1, 13, 14,  0, 11,  3,  8],
        [ 9, 14, 15,  5,  2,  8, 12,  3,  7,  0,  4, 10,  1, 13, 11,  6],
        [ 4,  3,  2, 12,  9,  5, 15, 10, 11, 14,  1,  7,  6,  0,  8, 13]
    ],
    # S-Box 7
    [
        [ 4, 11,  2, 14, 15,  0,  8, 13,  3, 12,  9,  7,  5, 10,  6,  1],
        [13,  0, 11,  7,  4,  9,  1, 10, 14,  3,  5, 12,  2, 15,  8,  6],
        [ 1,  4, 11, 13, 12,  3,  7, 14, 10, 15,  6,  8,  0,  5,  9,  2],
        [ 6, 11, 13,  8,  1,  4, 10,  7,  9,  5,  0, 15, 14,  2,  3, 12]
    ],
    # S-Box 8
    [
        [13,  2,  8,  4,  6, 15, 11,  1, 10,  9,  3, 14,  5,  0, 12,  7],
        [ 1, 15, 13,  8, 10,  3,  7,  4, 12,  5,  6, 11,  0, 14,  9,  2],
        [ 7, 11,  4,  1,  9, 12, 14,  2,  0,  6, 10, 13, 15,  3,  5,  8],
        [ 2,  1, 14,  7,  4, 10,  8, 13, 15, 12,  9,  0,  3,  5,  6, 11]
    ]
]

def get_sbox_str(xored):
    sbox_str = ""
    for j in range(8):
        row = int(xored[j * 6] + xored[j * 6 + 5], 2)  # Chọn bit đầu và cuối làm hàng
        col = int(xored[j * 6 + 1:j * 6 + 5], 2)  # 4 bit giữa làm cột
        sbox_val = sbox[j][row][col]  # Tra S-box
        sbox_str += dec_to_bin(sbox_val)
    return sbox_str


# Bảng mở rộng nửa bên phải từ 32 -> 48 bit
expansion_table = [
    32,  1,  2,  3,  4,  5,  4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32,  1
]

# Điền bảng hoán vị P (32 bit) -> tăng tính hỗn loạn, ngẫu nhiên của dữ liệu
p_table = [
    16, 7,  20, 21, 29, 12, 28, 17,
    1,  15, 23, 26,  5, 18, 31, 10,
    2,  8,  24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25
]

def f_function(right, round_key):
    # 1. Mở rộng từ 32-bit lên 48-bit
    right_exp = permute(right, expansion_table, 48)
    
    # 2. XOR với khóa con
    xored = bin(int(right_exp, 2) ^ int(round_key, 2))[2:].zfill(48)
    
    # 3. Áp dụng S-Box
    sbox_str = get_sbox_str(xored)
    
    # 4. Áp dụng hoán vị P
    result = permute(sbox_str, p_table, 32)
    
    return result


def des_encrypt(plain_text, key):    
    # Tạo round keys từ key và hoán vị plain_text theo bảng IP
    round_keys = generate_round_keys(key)
    plain_text = hex_to_bin(plain_text)
    plain_text = permute(plain_text, ip, 64)
    
    # Chia plain_text thành 2 phần: left và right
    left, right = plain_text[:32], plain_text[32:]

    # 16 vòng lặp mã hóa
    for i in range(16):
        right_new = f_function(right, round_keys[i])
        right_new = bin(int(left, 2) ^ int(right_new, 2))[2:].zfill(32)
        left = right
        right = right_new

    # right + left
    cipher_text = permute(right + left, ip_inv, 64)
    return bin_to_hex(cipher_text).upper()


def des_decrypt(cipher_text, key):
    # Tạo round keys nhưng sử dụng theo thứ tự đảo ngược
    round_keys = generate_round_keys(key)[::-1]

    cipher_text = hex_to_bin(cipher_text)
    cipher_text = permute(cipher_text, ip, 64)
    left, right = cipher_text[:32], cipher_text[32:]
    for i in range(16):
        right_new = f_function(right, round_keys[i])
        right_new = bin(int(left, 2) ^ int(right_new, 2))[2:].zfill(32)
        left = right
        right = right_new

    decrypted_text = permute(right + left, ip_inv, 64)
    return bin_to_hex(decrypted_text).upper()


# plain_text = "0123456789ABCDEF"
# key = "133457799BBCDFF1"

# print(f"Plaintext: {plain_text}")
# print(f"Key: {key}")

# # Mã hóa
# cipher_text = des_encrypt(plain_text, key)
# print(f"Cipher Text: {cipher_text}")

# # Giải mã
# decrypted_text = des_decrypt(cipher_text, key)
# print(f"Decrypted Text: {decrypted_text}")

