import string
import secrets


def generate_password(length=12, use_letters=True, use_uppercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_letters:
        characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("Вы должны выбрать хотя бы один тип символов для генерации пароля.")

    password = ''.join(secrets.choice(characters) for i in range(length))
    return password


def get_user_preferences():
    length = int(input("Введите длину пароля: "))
    use_letters = input("Использовать буквы? (y/n): ").lower() == 'y'
    use_uppercase = use_letters and input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_special = input("Использовать специальные символы? (y/n): ").lower() == 'y'
    return length, use_letters, use_uppercase, use_digits, use_special


def save_passwords(passwords_with_notes, filename='passwords.txt'):
    with open(filename, 'a') as file:
        for password, note in passwords_with_notes:
            file.write(f"{note} - {password}\n")


def assess_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1
    return strength


def display_password(password, mask=False):
    if mask:
        print("Ваш пароль: " + '*' * len(password))
    else:
        print("Ваш пароль: " + password)


def get_display_preferences():
    mask = input("Вы хотите замаскировать пароль при выводе? (y/n): ").lower() == 'y'
    note = input("Введите заметку для пароля (например, для чего он нужен): ")
    return mask, note


def main():
    passwords_with_notes = []
    length, use_letters, use_uppercase, use_digits, use_special = get_user_preferences()
    mask, note = get_display_preferences()
    password = generate_password(length, use_letters, use_uppercase, use_digits, use_special)
    display_password(password, mask=mask)
    print(f"Сложность пароля: {assess_password_strength(password)}")
    passwords_with_notes.append((password, note))
    save_passwords(passwords_with_notes)


if __name__ == "__main__":
    main()
