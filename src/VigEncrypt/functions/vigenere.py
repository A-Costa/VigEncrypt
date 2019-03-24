def shift_letter(letter, key, reverse=False):
    if not (isinstance(key, str) and len(key) == 1):
        raise TypeError('key must be of type str and len == 1')
    if not (isinstance(letter, str) and len(letter) == 1):
        raise TypeError('letter must be of type str and len == 1')
    if not isinstance(reverse, bool):
        raise TypeError('reverse must be a boolean')
    if not (64 < ord(key) < 91):
        raise ValueError('key must be a capital letter')

    key_ordinal = ord(key) - 65

    if reverse:
        multiplire = -1
    else:
        multiplire = 1

    if 64 < ord(letter) < 91:
        return chr(((ord(letter) - 65 + (key_ordinal * multiplire)) % 26) + 65)

    elif 96 < ord(letter) < 123:
        return chr(((ord(letter) - 97 + (key_ordinal * multiplire)) % 26) + 97)

    else:
        return letter


def encrypt(plaintext, key, key_mode):
    pass


def decrypt(ciphertext, key, key_mode):
    pass
