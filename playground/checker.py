import random
import string

import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box

# Private-key for the system
private_system = "d9136c8ba792fef21c9ea11ec80cf3a38cc702e36948ece61c340208b0ac596a"
private_system = PrivateKey(bytes.fromhex(private_system))

# Public-key stored for doctors
doctors = {
    "doctor1" : "58791eb10d367b8ce8328a2649e87a166fdec7bcc679104ccc7b49295652eb0d",
    "doctor2" : "7417ac098e525b273f70415e5663eb8051a25035d51fb853d5755d4a74bfb800",
    "doctor3" : "9462126cb2aa6a70204439a7446ed9feac5b0c4cd5415aece163a672f6650040",
    "doctor4" : "db25731fc67f16dce39d72c5081c688990b4bf45421ed464571d58836b707b00"
}

challenge = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
doc = input("Which doctor are you trying to authenticate (doctor1, doctor2 or doctor3)? ")
message = input("Please, tell us the result for the challenge '{}': ".format(challenge))

message = bytes.fromhex(message)
public_doctor = doctors[doc]
public_doctor = PublicKey(bytes.fromhex(public_doctor))

try:
    box = Box(private_system, public_doctor)
    plaintext = box.decrypt(message)
    result = plaintext.decode('utf-8')
except:
    result = None

if (result == challenge):
    print("Authenticated!")
else:
    print("Not authenticated!")