shift_key = int(input("Choose shift key: "))

while True:
    operation = input("Choose the operation: Encrypt (1) or Decrypt (2)")
    if operation == "1" or operation == "encrypt" or operation == "Encrypt" or operation == "2" or operation == "decrypt" or operation == "Decrypt":
        break

alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_text = ""

if operation == "encrypt" or operation == "Encrypt" or operation == "1":
    text = input("Choose text to encrypt: ")
    letters = len(text)
    while letters > 0:
        letter = alphabet.find(text[:1]) + shift_key 
        while letter > 25:
            letter = letter % 26
        encrypted_text = encrypted_text + alphabet[letter]
        text = text[1:]
        letters -= 1
else:
    text = input("Choose text to decrypt: ")
    letters = len(text)
    while letters > 0:
        letter = alphabet.find(text[:1]) - shift_key
        while letter < -26:
            letter = letter + 26
        encrypted_text = encrypted_text + alphabet[letter]
        text = text[1:]
        letters -= 1
print(encrypted_text)