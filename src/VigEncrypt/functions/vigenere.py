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
        multiplier = -1
    else:
        multiplier = 1

    if 64 < ord(letter) < 91:
        return chr(((ord(letter) - 65 + (key_ordinal * multiplier)) % 26) + 65)

    elif 96 < ord(letter) < 123:
        return chr(((ord(letter) - 97 + (key_ordinal * multiplier)) % 26) + 97)

    else:
        return letter


def cipher(text, key, key_mode, decrypt=False):
    if not ((key_mode == 'repeat') or (key_mode == 'autokey')):
        raise ValueError('key_mode must be \'repeat\' or \'autokey\'')

    result = []
    n = 0
    for letter in text:
        if key_mode == 'repeat':
            key_position = n % len(key)
            shifted_letter = shift_letter(letter, key[key_position], decrypt)
            if (shifted_letter != letter) or key[key_position] == 'A':
                n += 1
            result.append(shifted_letter)
        else:
            shifted_letter = shift_letter(letter, key[n], decrypt)
            if (shifted_letter != letter) or key[n] == 'A':
                n += 1
                if not decrypt:
                    key += shifted_letter.capitalize()
                else:
                    key += letter.capitalize()
            result.append(shifted_letter)

    return ''.join(result)
