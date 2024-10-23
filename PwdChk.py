import re

# Function checks password strength based on criteria and compares it to the dicitonary with common passwords.
def check_password_strength(password, dictionary_file="common_passwords.txt"):

    # Open text file for reading common passwords
    with open(dictionary_file, "r") as f:
        common_passwords = set(f.read().splitlines())

    # List of possible errors
    short_error = "Password not at least 8 characters long."
    long_error = "Password not at less than 20 characters long."
    lowercase_error = "Password does not contain at least one lowercase letter."
    uppercase_error = "Password does not contain at least one uppercase letter."
    digit_error = "Password does not contain at least one digit."
    special_char_error = "Password does not contain at least one special character."
    dictionary_error = "Password found in common password list. Please change it."
    white_space_error = "Password contains whitespace. Please enter a password without whitespace."

    # Set list for errors
    errors = []
    err_list = ""

    # Check passwords strength based on regex criteria patterns
    if len(password) < 8:
        errors.append(short_error)
    if len(password) > 20:
        errors.append(long_error)
    if not re.search(r"[a-z]", password):
        errors.append(lowercase_error)
    if not re.search(r"[A-Z]", password):
        errors.append(uppercase_error)
    if not re.search(r"\d", password):
        errors.append(digit_error)
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?~`]", password):
        errors.append(special_char_error)
    if re.search(r"\s", password):
        errors.append(white_space_error)
    if password.lower() in common_passwords:
        errors.append(dictionary_error)

    # Return the errors if any
    if errors:
        # Iterate through list of errors caught and add them to a string with new lines
        for i in errors:
            err_list += ("\n" + i)
        return err_list
    else:
        return "Strong password!"

if __name__ == "__main__":
    print("***PASSOWRD STRENGTH CHECKER***\nPassword Requirements:\n")
    print("1. Password should be at least 8 characters long.\n2. Password should be no longer than 20 characters long.\n3. Password should contain at least one lowercase letter.\n4. Password should contain at least one uppercase letter.\n5. Password should contain at least one digit.\n6. Password should contain at least one special character.\n7. Password should not be among common passwords i.e. \"12345678\" or \"password\".\n8. Password should not contain any whitespace.\n")
    password = input("Enter your password: ")
    print(check_password_strength(password))