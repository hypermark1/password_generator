import unittest
import string
import os
import tempfile
from main import generate_password, assess_password_strength, save_passwords, get_user_preferences, \
    get_display_preferences
from unittest.mock import patch


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_length(self):
        password = generate_password(length=10)
        self.assertEqual(len(password), 10)

    def test_generate_password_characters(self):
        password = generate_password(length=10, use_uppercase=False, use_digits=False, use_special=False)
        self.assertTrue(all(char in string.ascii_lowercase for char in password))

    def test_assess_password_strength(self):
        self.assertEqual(assess_password_strength("aA1!"), 3)  # Example of 2 password
        self.assertEqual(assess_password_strength("123"), 1)  # Example of 0 password


class TestUserPreferences(unittest.TestCase):

    @patch('builtins.input', side_effect=['12', 'y', 'y', 'y', 'y'])
    def test_get_user_preferences(self, mock_input):
        length, use_letters, use_uppercase, use_digits, use_special = get_user_preferences()
        self.assertEqual(length, 12)
        self.assertTrue(use_letters)
        self.assertTrue(use_uppercase)
        self.assertTrue(use_digits)
        self.assertTrue(use_special)

    @patch('builtins.input', side_effect=['y', 'Personal note'])
    def test_get_display_preferences(self, mock_input):
        mask, note = get_display_preferences()
        self.assertTrue(mask)
        self.assertEqual(note, 'Personal note')


class TestSavePasswords(unittest.TestCase):

    def test_save_passwords(self):
        passwords_with_notes = [("password1", "Note1"), ("password2", "Note2")]
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            filename = tmpfile.name
        save_passwords(passwords_with_notes, filename)
        with open(filename, 'r') as file:
            content = file.readlines()
        self.assertEqual(content, ["Note1 - password1\n", "Note2 - password2\n"])
        os.remove(filename)  # Clean up the test file


if __name__ == '__main__':
    unittest.main()
