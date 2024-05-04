shift_key = int(input("Choose shift key: "))
text = input("Choose text to encrypt: ")

length = len(text)
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_text = ""

while length:
    found_letter = alphabet.find(text[:1])
    if found_letter + shift_key > 26:
        alphabet = alphabet + alphabet
        encrypted_text = alphabet[found_letter + shift_key]
    else:
        encrypted_text = alphabet[found_letter + shift_key]
    text = text[1:]
    encrypted_text = encrypted_text + encrypted_text
    length -= 1
print(encrypted_text)