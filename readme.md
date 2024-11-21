# Password Generator Program

## Overview
This program allows you to create tailored passwords or passcodes for your needs, with the option to leave a comment so you can easily remember what source the password is for. It features several functions for generating passwords, evaluating their strength, and storing them with notes for future reference.

## Features
- **Customizable Password Generation**: Choose the length and types of characters to include (letters, uppercase letters, digits, special characters).
- **Secure Methods**: Uses cryptographically secure methods to generate passwords.
- **Password Masking**: Option to mask the password when displaying it on the screen for added security.
- **Password Storage**: Save passwords along with notes to a file, helping you remember where each password is used.
- **Strength Assessment**: Assess the strength of the generated password to ensure it's robust.

## Functions Breakdown

### 1. `generate_password(length=12, use_letters=True, use_uppercase=True, use_digits=True, use_special=True)`
This function generates a random password based on the user's preferences.
- **Arguments**:
  - `length` (int): The desired length of the password (default is 12).
  - `use_letters` (bool): Whether to include lowercase letters (default is True).
  - `use_uppercase` (bool): Whether to include uppercase letters (default is True).
  - `use_digits` (bool): Whether to include digits (default is True).
  - `use_special` (bool): Whether to include special characters (default is True).
- **Returns**: A random password as a string.
- **Raises**: `ValueError` if no character types are selected.

### 2. `get_user_preferences()`
This function prompts the user for their password generation preferences.
- **Returns**: A tuple containing the length, use_letters, use_uppercase, use_digits, and use_special preferences.

### 3. `save_passwords(passwords_with_notes, filename='passwords.txt')`
This function saves a list of passwords and their corresponding notes to a file.
- **Arguments**:
  - `passwords_with_notes` (list): List of tuples containing passwords and their notes.
  - `filename` (str): The name of the file to save the passwords (default is 'passwords.txt').

### 4. `assess_password_strength(password)`
This function evaluates the strength of a given password.
- **Arguments**:
  - `password` (str): The password to assess.
- **Returns**: A strength score from 0 (very weak) to 4 (very strong).

### 5. `display_password(password, mask=False)`
This function prints the password to the console.
- **Arguments**:
  - `password` (str): The password to display.
  - `mask` (bool): Whether to mask the password with asterisks (default is False).

### 6. `get_display_preferences()`
This function prompts the user for their display preferences.
- **Returns**: A tuple containing the mask preference and a note for the password.

### 7. `main()`
This is the main function of the program. It prompts the user for their preferences, generates the password, displays it with optional masking, assesses the strength, and then saves the password and note to a file.

## Example Usage
Run the `main()` function to start the program and follow the prompts to generate and save your passwords.

```python
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
