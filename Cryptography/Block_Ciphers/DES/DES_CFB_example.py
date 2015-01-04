#!/usr/bin/env python

__author__ = "bt3"


from Crypto.Cipher import DES
from Crypto import Random

iv = Random.get_random_bytes(8)

des1 = DES.new('01234567', DES.MODE_CFB, iv)
des2 = DES.new('01234567', DES.MODE_CFB, iv)
text = 'abcdefghijklmnop'

cipher_text = des1.encrypt(text)
print cipher_text
print des2.decrypt(cipher_text)
