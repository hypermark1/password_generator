# Password Generator Program

## Overview

This is a password generator that allows you to create tailored passwords or passcodes for your needs, allowing you to
leave a comment so you can easily find for what source you have made it later on. It features several functions for
generating passwords, evaluating their strength, and storing them with notes for future reference.

## Functions

- `generate_password()`: Generates a random password based on user-specified criteria.
- `get_user_preferences()`: Prompts the user for their password generation preferences.
- `save_passwords()`: Saves generated passwords and notes to a file.
- `assess_password_strength()`: Evaluates the strength of a password.
- `display_password()`: Prints the password to the console, optionally masking it.
- `get_display_preferences()`: Gets user preferences for password display (masking and note).
- `main()`: The main function of the program, orchestrating the password generation and storage process.

## Note

- The code uses the `secrets` module for generating cryptographically secure random numbers.
- The `passwords.txt` file is used to store the generated passwords and notes.

## Example Usage

To use the password generator, run the `main()` function and follow the prompts to generate and save your passwords.
