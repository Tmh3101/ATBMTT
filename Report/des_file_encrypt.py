# des_file_encrypt.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from des_core import des_encrypt, des_decrypt

def pad_data(data, block_size=8):  # 8 bytes = 64 bits
    """Thêm padding vào dữ liệu để đảm bảo chia hết cho block_size."""
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unpad_data(padded_data):
    """Loại bỏ padding sau khi giải mã."""
    padding_length = padded_data[-1]
    return padded_data[:-padding_length]

def read_file_in_blocks(file_path, block_size=8):
    """Đọc file nhị phân và chia thành các khối 8 byte (64-bit)."""
    with open(file_path, 'rb') as f:
        data = f.read()
    padded_data = pad_data(data)
    blocks = [padded_data[i:i + block_size] for i in range(0, len(padded_data), block_size)]
    return blocks

def encrypt_file(input_file, output_file, key):
    """Mã hóa file nhị phân bằng DES."""
    key = key.zfill(16)  # Đảm bảo key là 16 ký tự hex
    blocks = read_file_in_blocks(input_file)
    
    encrypted_blocks = []
    for block in blocks:
        hex_block = block.hex()
        encrypted_hex = des_encrypt(hex_block, key)
        encrypted_bytes = bytes.fromhex(encrypted_hex)
        encrypted_blocks.append(encrypted_bytes)
    
    with open(output_file, 'wb') as f:
        for block in encrypted_blocks:
            f.write(block)
    return True

def decrypt_file(input_file, output_file, key):
    """Giải mã file nhị phân bằng DES."""
    key = key.zfill(16)
    blocks = read_file_in_blocks(input_file)
    
    decrypted_blocks = []
    for block in blocks:
        hex_block = block.hex()
        decrypted_hex = des_decrypt(hex_block, key)
        decrypted_bytes = bytes.fromhex(decrypted_hex)
        decrypted_blocks.append(decrypted_bytes)
    
    decrypted_data = b''.join(decrypted_blocks)
    original_data = unpad_data(decrypted_data)
    
    with open(output_file, 'wb') as f:
        f.write(original_data)
    return True

# Hàm giao diện
def select_input_file():
    """Chọn file đầu vào."""
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*"), ("Word files", "*.doc *.docx")])
    if file_path:
        input_file_var.set(file_path)

def select_output_file():
    """Chọn vị trí lưu file đầu ra."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".bin" if mode_var.get() == "encrypt" else ".docx",
        filetypes=[("All files", "*.*"), ("Binary files", "*.bin"), ("Word files", "*.docx")]
    )
    if file_path:
        output_file_var.set(file_path)

def execute_operation():
    """Thực hiện mã hóa hoặc giải mã dựa trên chế độ đã chọn."""
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    key = key_var.get()
    
    if not input_file or not output_file or not key:
        messagebox.showerror("Lỗi", "Vui lòng điền đầy đủ thông tin (file, key, vị trí lưu)!")
        return
    
    if len(key) < 16:
        messagebox.showerror("Lỗi", "Khóa phải ít nhất 16 ký tự hex (64-bit)!")
        return
    
    try:
        if mode_var.get() == "encrypt":
            success = encrypt_file(input_file, output_file, key)
            if success:
                messagebox.showinfo("Thành công", f"File đã được mã hóa thành: {output_file}")
        else:  # decrypt
            success = decrypt_file(input_file, output_file, key)
            if success:
                messagebox.showinfo("Thành công", f"File đã được giải mã thành: {output_file}")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

# Tạo giao diện
root = tk.Tk()
root.title("DES File Encryption/Decryption")

# Biến điều khiển
mode_var = tk.StringVar(value="encrypt")
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
key_var = tk.StringVar()

# Giao diện
tk.Label(root, text="Chọn chế độ:").pack(pady=5)
tk.Radiobutton(root, text="Mã hóa", variable=mode_var, value="encrypt").pack()
tk.Radiobutton(root, text="Giải mã", variable=mode_var, value="decrypt").pack()

tk.Label(root, text="Chọn file đầu vào:").pack(pady=5)
tk.Entry(root, textvariable=input_file_var, width=40).pack()
tk.Button(root, text="Chọn file", command=select_input_file).pack()

tk.Label(root, text="Nhập khóa (16 ký tự hex):").pack(pady=5)
tk.Entry(root, textvariable=key_var, width=40).pack()

tk.Label(root, text="Chọn vị trí lưu file:").pack(pady=5)
tk.Entry(root, textvariable=output_file_var, width=40).pack()
tk.Button(root, text="Chọn vị trí", command=select_output_file).pack()

tk.Button(root, text="Thực hiện", command=execute_operation, bg="green", fg="white").pack(pady=20)


root.geometry('500x400')
# Chạy giao diện
root.mainloop()