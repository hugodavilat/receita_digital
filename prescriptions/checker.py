import random
import string

import nacl.utils
from nacl.public import PrivateKey, PublicKey, Box

def check_key(public_doctor, challenge, challenge_answer):
    # Private-key for the system
    private_system = "d9136c8ba792fef21c9ea11ec80cf3a38cc702e36948ece61c340208b0ac596a"
    private_system = PrivateKey(bytes.fromhex(private_system))

    try:
        box = Box(private_system, public_doctor)
        plaintext = box.decrypt(challenge_answer)
        result = plaintext.decode('utf-8')
    except:
        result = None

    return (result == challenge)