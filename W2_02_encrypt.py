from Crypto.Cipher import AES

with open("aes_key.bin", "rb") as f:
    key = f.read()

with open("nilai_mahasiswa.txt", "rb") as f:
    plaintext = f.read()

cipher = AES.new(key, AES.MODE_GCM)

ciphertext, tag = cipher.encrypt_and_digest(plaintext)

with open("nilai_mahasiswa.enc", "wb") as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(ciphertext)

print("Encryption successful!")
print()
print("Plaintext:")
print(plaintext.decode())
print()
print("Ciphertext (hex):")
print(ciphertext.hex())
