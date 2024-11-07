from random import randint

def generator(g, x, p):
    return pow(g, x, p)

def decrypt(cipher, key, constant=311):
    semi_plain_text = ""
    for num in cipher:
        if num == 0:
            semi_plain_text += chr(0)
        else:
            char_code = num // (key * constant)
            semi_plain_text += chr(char_code)
    return semi_plain_text

def dynamic_xor_decrypt(cipher_text, text_key):
    plain_text = ""
    key_length = len(text_key)
    for i, char in enumerate(cipher_text):
        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        plain_text += decrypted_char
    return plain_text

def decrypt_message(cipher_text, a, b, p, g, text_key):
    shared_key = generator(generator(g, b, p), a, p)
    semi_plain_text = decrypt(cipher_text, shared_key)
    original_message = dynamic_xor_decrypt(semi_plain_text, text_key)
    return original_message[::-1]

cipher_text = [746400, 686688, 2448192, 358272, 537408, 2507904, 1134528, 1701792, 268704, 2537760, 626976, 2418336, 686688, 1134528, 895680, 1253952, 1194240, 1433088, 1403232]

print(decrypt_message(cipher_text, 90, 28, 97, 31, "deadbeef"))