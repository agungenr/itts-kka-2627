from Crypto.Cipher import AES

with open("aes_key.bin", "rb") as f:
    key = f.read()

with open("nilai_mahasiswa.enc", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

try:
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    # Simpan hasil dekripsi ke file baru
    with open("nilai_mahasiswa_decrypted.txt", "wb") as f:
        f.write(plaintext)

    print("Decryption successful!")
    print()
    print("Decrypted data:")
    print(plaintext.decode())
    print()
    print("File saved as: nilai_mahasiswa_decrypted.txt")

except ValueError:
    print("Decryption FAILED!")
    print("Wrong key or data has been modified.")
