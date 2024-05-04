shift_key = int(input("Choose shift key: "))
text = input("Choose text to encrypt: ")

letters = len(text)
alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_text = ""

while letters > 0:
    letter = alphabet.find(text[:1]) + shift_key 
    while letter > 25:
        letter = letter % 26
    encrypted_text = encrypted_text + alphabet[letter]
    text = text[1:]
    letters -= 1
print(encrypted_text)