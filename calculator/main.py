def menu():
    print("==== CALCULATOR ====")
    print("1. Add")
    print("2. Substract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Power")
    print("6. Exit")

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def div(a, b):
    if b == 0:
        print("Cannot be divided by 0")
    return a / b

def multp(a, b):
    return a * b

def power(a, b):
    return a ** b

def get_numbers(is_float=False):
    t = float if is_float else int
    a = t(input("Enter 1st number:"))
    b = t(input("Enter 2nd number:"))
    return a, b

def main():
    select = 0
    while select != 6:
        menu()

        try:
            select = int(input("Choose an option (1-6): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        match select:
            case 1:
                a, b = get_numbers()
                print("--> Result of addition is:", add(a, b))
            case 2:
                a, b = get_numbers()
                print("--> Result of substarction is:", substract(a, b))
            case 3:
                a, b = get_numbers()
                print("--> Result of division is:", div(a, b))
            case 4:
                a, b = get_numbers()
                print("--> Result of multiplication is:", multp(a, b))
            case 5:
                a, b = get_numbers()
                print("--> a^b is:", power(a, b))
            case 6:
                print("\nExiting...")
            case _:
                print("Invalid choice!")