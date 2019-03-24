import pytest
from VigEncrypt.functions import vigenere


@pytest.mark.parametrize('key', ['1', 'a', '!'])
def test_wrong_key_value(key):
    with pytest.raises(ValueError):
        vigenere.shift_letter('a', key, False)


@pytest.mark.parametrize('key', [1, 3.4, ['a', 'b'], 'string'])
def test_wrong_key_type(key):
    with pytest.raises(TypeError):
        vigenere.shift_letter('a', key, False)


@pytest.mark.parametrize('letter', [1, 3.4, ['a', 'b'], 'string'])
def test_wrong_letter_type(letter):
    with pytest.raises(TypeError):
        vigenere.shift_letter(letter, 'A', False)


@pytest.mark.parametrize('reverse', [1, 3.4, ['a', 'b'], 'string', 'a'])
def test_wrong_reverse_type(reverse):
    with pytest.raises(TypeError):
        vigenere.shift_letter('a', 'A', reverse)


@pytest.mark.parametrize('tuple', [('R', 'V', False, 'M'),
                                   ('r', 'V', False, 'm'),
                                   ('A', 'E', False, 'E'),
                                   ('P', 'R', False, 'G'),
                                   ('p', 'R', False, 'g'),
                                   ('!', 'V', False, '!'),
                                   ('@', 'F', False, '@'),
                                   ('M', 'V', True, 'R'),
                                   ('m', 'V', True, 'r'),
                                   ('!', 'V', True, '!')])
def test_correct_shift(tuple):
    letter = tuple[0]
    key = tuple[1]
    reverse = tuple[2]
    result = tuple[3]
    assert vigenere.shift_letter(letter, key, reverse) == result
