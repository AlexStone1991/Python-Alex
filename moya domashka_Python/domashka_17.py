# В этом задании вы реализуете программу для шифрования текста с использованием шифра Цезаря, где сдвиг происходит по кодам символов. Вы научитесь работать с функциями `ord()` и `chr()` для преобразования символов в их числовые коды и обратно.

user_text = input("Введите текст для шифрования: ")
shift = int(input("Введите сдвиг(от 1 до 32): "))

encrypted_text = []
for char in user_text:
    if char.isalpha():
        if 'a' <= char <= 'z':
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'а' <= char <= 'я':
            shifted_char = chr((ord(char) - ord('а') + shift) % 33 + ord('а'))
        elif 'А' <= char <= 'Я':
            shifted_char = chr((ord(char) - ord('А') + shift) % 33 + ord('А'))
        encrypted_text.append(shifted_char)
    else:
        encrypted_text.append(char)

encrypted_text = ''.join(encrypted_text)
print("Зашифрованный текст:", encrypted_text)

encrypted_input = input("Выхотите расшифровать текст? (да/нет): ")
if encrypted_input.lower() == 'да':
    decrypted_text = []
    for char in encrypted_text:
        if char.isalpha():
            if 'a' <= char <= 'z':
                shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif 'A' <= char <= 'Z':
                shifted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif 'а' <= char <= 'я':
                shifted_char = chr((ord(char) - ord('а') - shift) % 33 + ord('а'))
            elif 'А' <= char <= 'Я':
                shifted_char = chr((ord(char) - ord('А') - shift) % 33 + ord('А'))
            decrypted_text.append(shifted_char)
        else:
            decrypted_text.append(char)
    decrypted_text = ''.join(decrypted_text)
    print("Расшифрованный текст:", decrypted_text)
else:
    encrypted_input.lower() == "нет"
    print("Инкогнито, выходим")
    