import sys
from Crypto.Cipher import AES
print("usage python3 rand-aes-d.py numused filein fileout")
# define the encryption key and block size (must match the ones used for encryption)
key = b'your_key_here'
block_size = 16

# read the contents of the encrypted file with noise characters
with open(sys.argv[2], 'r') as f:
    encrypted_data_with_noise = f.read()

# remove the noise characters to obtain the actual encrypted data
noise_chars = ''.join(chr(random.randint(0, 255)) for i in range(int(sys.argv[1])))
encrypted_data = bytes([int(b) for b in encrypted_data_with_noise.split(noise_chars)])

# create a new AES cipher object with the key and mode of operation
cipher = AES.new(key, AES.MODE_ECB)

# decrypt the data using the cipher
decrypted_data = cipher.decrypt(encrypted_data)

# remove the padding from the decrypted data
padding = decrypted_data[-1]
decrypted_data = decrypted_data[:-padding]

# write the decrypted data to a new file
with open(sys.argv[3], 'wb') as f:
    f.write(decrypted_data)
