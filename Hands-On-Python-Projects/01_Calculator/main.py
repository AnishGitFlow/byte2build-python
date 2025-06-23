try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("What kind of operation do you want to perform:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")

    ops = input("Enter your operation: ")

    match ops:
        case "+":
            print("The result is: ", num1 + num2)
        case "-":
            print("The result is: ", num1 - num2)
        case "*":
            print("The result is: ", num1 * num2)
        case "/":
            if num2 != 0:
                print("The result is: ", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operation. Please enter +, -, *, or /.")

except ValueError:
    print("Enter a valid number.")
except Exception as e:
    print("An error occurred: ", str(e))