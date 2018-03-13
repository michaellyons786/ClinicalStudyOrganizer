import hashlib

class Study():
    def __init__(self):
        pass

def hash_id(identifier):

    return hashlib.md5(identifier.encode())


def to_decimal(hex_string):
    return int(hex_string, 16)




a = hash_id('nerd')
a = a.hexdigest()
print('Hex', a)
b = int(a, 16)
print('Dec', b)
print(type(hex(b)))