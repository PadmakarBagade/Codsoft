import random
import string

def generate_password(length, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        include_lowercase (bool): Whether to include lowercase letters.
        include_uppercase (bool): Whether to include uppercase letters.
        include_digits (bool): Whether to include digits.
        include_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password, or an error message if no character types are selected.
    """
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected for password generation. Please choose at least one."

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    """Main function to run the password generator program."""
    print("--- Password Generator ---")

    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number for the length.")

    print("\n--- Password Complexity ---")
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    print("\nGenerating password...")
    password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)

    print(f"\nGenerated Password: {password}")
    print("--------------------------")

if __name__ == "__main__":
    main()