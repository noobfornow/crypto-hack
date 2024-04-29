from pwn import xor

msg = "label"
num = 13

print(xor(msg, num).decode())
