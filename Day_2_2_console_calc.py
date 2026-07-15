import math

while True:

    print("\n" + "*" * 45)
    print("        PYTHON MENU DRIVEN CALCULATOR")
    print("*" * 45)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponent")
    print("7. Factorial")
    print("8. Straight Line Equation (y = mx + c)")
    print("9. Pythagoras Theorem")
    print("10. Exit")

    choice = input("\nEnter your choice (1-10): ")

    if choice == "10":
        print("Thank you for using the calculator.")
        break

    elif choice == "1":
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        print("Result =", a + b)

    elif choice == "2":
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        print("Result =", a - b)

    elif choice == "3":
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))
        print("Result =", a * b)

    elif choice == "4":
        a = float(input("Enter first number : "))
        b = float(input("Enter second number : "))

        if b == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result =", round(a / b, 2))

    elif choice == "5":
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        if b == 0:
            print("Modulus by zero is not allowed.")
        else:
            print("Result =", a % b)

    elif choice == "6":
        base = float(input("Enter base : "))
        power = float(input("Enter exponent : "))
        print("Result =", math.pow(base, power))

    elif choice == "7":
        number = int(input("Enter a positive integer: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print("Factorial =", math.factorial(number))

    elif choice == "8":
        m = float(input("Enter slope (m): "))
        c = float(input("Enter intercept (c): "))
        x = float(input("Enter value of x: "))

        y = m * x + c

        print(f"Equation : y = ({m})x + ({c})")
        print("Value of y =", y)

    elif choice == "9":
        a = float(input("Enter first perpendicular side : "))
        b = float(input("Enter second perpendicular side : "))

        hypo = math.sqrt(a**2 + b**2)

        print("Hypotenuse =", round(hypo, 2))

    else:
        print("Invalid choice. Please try again.")