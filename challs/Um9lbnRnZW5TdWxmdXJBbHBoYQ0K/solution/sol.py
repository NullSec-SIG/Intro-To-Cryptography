a = int(input("Enter a: "))
b = int(input("Enter b: "))
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
ct = int(input("Enter ciphertext: "))

M = (a * b) - 1
e = (a1 * M) + a
d = (b1 * M) + b
n = ((e * d) - 1) // M

def decrypt(ciphertext, d, n):
    decrypted_text = (ciphertext * d) % n
    return decrypted_text

print(f"Decrypted text: {decrypt(ct, d, n)}")