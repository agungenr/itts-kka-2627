from Crypto.Random import get_random_bytes

key = get_random_bytes(32)   # 32 bytes = 256 bits

with open("aes_key.bin", "wb") as f:
    f.write(key)

print("AES-256 key berhasil dibuat.")
print("Key length:", len(key) * 8, "bits")
print("Key (hex):", key.hex())
