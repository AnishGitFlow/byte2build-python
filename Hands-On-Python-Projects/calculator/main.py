try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform:")
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press / for division")
    print("Press * for multiplication")

    o = input("Enter Operation: ")

    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            if b != 0:
                print(f"The result is: {a / b}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please try again.")
except ValueError:
    print("Enter a valid value for a and b.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")