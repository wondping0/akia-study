from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_aes_ecb(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_aes_ecb(ciphertext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

def main():
    key = b'Sixteen byte key'
    plaintext = b'Hello, world! This is a test message.'
    ciphertext = encrypt_aes_ecb(plaintext, key)
    decrypted = decrypt_aes_ecb(ciphertext, key)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    return ciphertext

if __name__ == "__main__":
    main()
