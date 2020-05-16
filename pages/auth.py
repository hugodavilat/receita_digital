from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5

# cria assinatura na receita com chave privada do medico + documento da receita
def assina(privada, receita):
    h = SHA256.new(receita)
    rsa = RSA.importKey(privada)
    signer = PKCS1_v1_5.new(rsa)
    signature = signer.sign(h)
    return signature

# verifica a assinatura com a chave publica do medico + documento da receita + assinatura da receita
def verifica(publica, receita, signature):
    h = SHA256.new(receita)
    rsa = RSA.importKey(publica)
    signer = PKCS1_v1_5.new(rsa)
    if (signer.verify(h, signature)):
        return True
    else:
        return False