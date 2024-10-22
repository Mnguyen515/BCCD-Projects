import re

# Function checks password strength based on criteria and compares it to the dicitonary with common passwords.
def check_password_strength(password, dictionary_file="common_passwords.txt"):

    # Open text file for reading common passwords
    with open(dictionary_file, "r") as f:
        common_passwords = set(f.read().splitlines())

    # List of possible errors
    length_error = "Password should be at least 8 characters long."
    lowercase_error = "Password should contain at least one lowercase letter."
    uppercase_error = "Password should contain at least one uppercase letter."
    digit_error = "Password should contain at least one digit."
    special_char_error = "Password should contain at least one special character."
    dictionary_error = "Password found in common password list. Please change it."
    white_space_error = "Password should not contain any whitespace."

    # Set list for errors
    errors = []

    # Check passwords strength based on regex criteria patterns
    if len(password) < 8:
        errors.append(length_error)
    if not re.search(r"[a-z]", password):
        errors.append(lowercase_error)
    if not re.search(r"[A-Z]", password):
        errors.append(uppercase_error)
    if not re.search(r"\d", password):
        errors.append(digit_error)
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
        errors.append(special_char_error)
    if re.search(r"\s", password):
        errors.append(white_space_error)
    if password.lower() in common_passwords:
        errors.append(dictionary_error)

    # Return the errors if any
    if errors:
        return "\n".join(errors)
    else:
        return "Strong password!"

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))