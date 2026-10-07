from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

wrong_key = get_random_bytes(32)

with open("nilai_mahasiswa.enc", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher = AES.new(wrong_key, AES.MODE_GCM, nonce=nonce)

try:
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    print("Decryption successful!")
    print(plaintext.decode())

except ValueError:
    print("DECRYPTION FAILED!")
    print("Wrong encryption key.")
    print("Ciphertext cannot be recovered without the correct key.")
