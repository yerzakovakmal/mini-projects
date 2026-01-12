import random, string

def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            if length > 0:
                return length
            else:
                print("Password length must be greater than 0!")
        except ValueError:
            print("Please enter a valid number!")


def get_character_set():
    while True:
        ask = str(input("Include numbers?(y/n): "))
        if ask.lower() == "y":
            ask = str(input("Include symbols?(y/n): "))
            if ask.lower() == "y":
                chars = string.ascii_letters + string.digits + string.punctuation
                return chars
            elif ask.lower() == "n":
                chars = string.ascii_letters + string.digits
                return chars
            else:
                print("Try again!")
                continue
        elif ask.lower() == "n":
            ask = str(input("Include symbols?(y/n): "))
            if ask.lower() == "y":
                chars = string.ascii_letters + string.punctuation
                return chars
            elif ask.lower() == "n":
                chars = string.ascii_letters
                return chars
            else:
                print("Try again!")
                continue
        else:
            print("Try again!")
            continue

def generate_password(length, chars):
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def main():
    print("--> Welcome to the RANDOM PASSWORD generator! <--")
    length = get_password_length()
    chars = get_character_set()
    password = generate_password(length, chars)
    print("\n--> Your password:", password)
main()