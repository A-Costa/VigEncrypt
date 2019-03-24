import pytest
from VigEncrypt.functions import vigenere


@pytest.mark.parametrize('keymode', [1, 'test', 3.4])
def test_wrong_key_mode(keymode):
    with pytest.raises(ValueError):
        vigenere.cipher('test', 'test', keymode, True)


@pytest.mark.parametrize('tuple', [('Rapporto immediato', 'VERME', 'repeat', False, 'Megbsmxf uqhiuueos'),
                                   ('Rapporto immediato', 'VERME', 'autokey', False, 'Megbsdxu jepbxreip'),
                                   ('Megbsmxf uqhiuueos', 'VERME', 'repeat', True, 'Rapporto immediato'),
                                   ('Megbsdxu jepbxreip', 'VERME', 'autokey', True, 'Rapporto immediato')])
def test_correct_encrypt(tuple):
    text, key, key_mode, decrypt, result = tuple
    assert vigenere.cipher(text, key, key_mode, decrypt) == result
