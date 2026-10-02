"""
Nama Program : Algoritma Vigenere Chiper
Nama         : Ibnaty Farah Rabbany
NPM          : 140810240022
Tanggal      : 15 September 2026
"""

def clean_text(text):
    return "".join(c for c in text.upper() if c.isalpha())

def letter_to_number(letter):
    return ord(letter) - ord("A")

def number_to_letter(number):
    return chr((number % 26) + ord("A"))

def extend_key(text, key):
    if not key:
        raise ValueError("Key tidak boleh kosong.")
    return "".join(key[i % len(key)] for i in range(len(text)))

def vigenere_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    key = clean_text(key)
    extended_key = extend_key(plaintext, key)
    return "".join(
        number_to_letter(letter_to_number(p) + letter_to_number(k))
        for p, k in zip(plaintext, extended_key)
    )

def vigenere_decrypt(ciphertext, key):
    ciphertext = clean_text(ciphertext)
    key = clean_text(key)
    extended_key = extend_key(ciphertext, key)
    return "".join(
        number_to_letter(letter_to_number(c) - letter_to_number(k))
        for c, k in zip(ciphertext, extended_key)
    )

def make_calculation_table(plaintext, key):
    plaintext = clean_text(plaintext)
    key = clean_text(key)
    extended_key = extend_key(plaintext, key)
    rows = []
    for i, (p, k) in enumerate(zip(plaintext, extended_key), 1):
        pn = letter_to_number(p)
        kn = letter_to_number(k)
        cn = (pn + kn) % 26
        rows.append((i, p, pn, k, kn, cn, number_to_letter(cn)))
    return rows

def print_calculation_table(rows):
    print("\nTABEL PERHITUNGAN VIGENERE")
    print("-" * 75)
    print(f"{'No':<4}{'PT':<5}{'n(PT)':<8}{'K':<5}{'n(K)':<8}{'(P+K) mod 26':<16}{'CT':<5}")
    print("-" * 75)
    for r in rows:
        print(f"{r[0]:<4}{r[1]:<5}{r[2]:<8}{r[3]:<5}{r[4]:<8}{r[5]:<16}{r[6]:<5}")
    print("-" * 75)

def main():
    print("=" * 50)
    print("             VIGENERE CIPHER")
    print("=" * 50)
    plaintext = input("Masukkan plaintext : ")
    key = input("Masukkan key       : ")

    plaintext = clean_text(plaintext)
    key = clean_text(key)
    ciphertext = vigenere_encrypt(plaintext, key)
    decrypted = vigenere_decrypt(ciphertext, key)

    print("\nHASIL")
    print("-" * 50)
    print(f"Plaintext   : {plaintext}")
    print(f"Key         : {key}")
    print(f"Key Extended: {extend_key(plaintext, key)}")
    print(f"Ciphertext  : {ciphertext}")
    print(f"Dekripsi    : {decrypted}")
    print_calculation_table(make_calculation_table(plaintext, key))

if __name__ == "__main__":
    main()
