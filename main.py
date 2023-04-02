import secrets
import string


def pass_gen(pass_len):

    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation

    char_set = letters + digits + special_chars

    while True:
        pwd = ""
        for i in range(pass_len):
            pwd += pwd.join(secrets.choice(char_set))

        if any(char in special_chars for char in pwd) and sum(char in char_set for char in pwd) >= 2:
            """
                checks whether at least one special chars are present and
                 also whether chars are repeated not more than 2 times
            """
            return pwd


if __name__ == "__main__":
    n = int(input("Enter password length: "))
    print("Generated password: " + pass_gen(n))
