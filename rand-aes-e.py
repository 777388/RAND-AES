import sys
import random
from Crypto.Cipher import AES
print("usage python3 rand-aes-e.py noisenum filein fileout")
# define the encryption key and block size
key = b'your_key_here'
block_size = 16

# read the contents of the original file
with open(sys.argv[2], 'rb') as f:
    data = f.read()

# pad the data to a multiple of the block size
padding = block_size - len(data) % block_size
data += bytes([padding] * padding)

# create a new AES cipher object with the key and mode of operation
cipher = AES.new(key, AES.MODE_ECB)

# encrypt the data using the cipher
encrypted_data = cipher.encrypt(data)

# generate noise characters
noise_chars = ''.join(chr(random.randint(0, 255)) for i in range(int(sys.argv[1])))

# insert noise characters between each actual encrypted character
encrypted_data_with_noise = noise_chars.join([chr(b) for b in encrypted_data])

# write the encrypted data with noise characters to a new file
with open(sys.argv[3], 'w') as f:
    f.write(encrypted_data_with_noise)
