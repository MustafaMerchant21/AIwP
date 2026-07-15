import re
import math

# ---------------- Arithmetic Calculator ---------------- #
def arithmaticCalculate(number, operator):
    num_list = [int(num) for num in number]

    if operator[0] == '+':
        result = num_list[0] + num_list[1]
    elif operator[0] == '-':
        result = num_list[0] - num_list[1]
    elif operator[0] == '*':
        result = num_list[0] * num_list[1]
    elif operator[0] == '/':
        result = num_list[0] / num_list[1]

    for indx in range(1, len(operator)):
        if operator[indx] == '+':
            result += num_list[indx + 1]
        elif operator[indx] == '-':
            result -= num_list[indx + 1]
        elif operator[indx] == '*':
            result *= num_list[indx + 1]
        elif operator[indx] == '/':
            result /= num_list[indx + 1]

    return result


# ---------------- Quadratic Equation ---------------- #
def QuadraticEquation(a, b, c):
    if a == 0:
        return "Equation is linear."

    D = (b ** 2) - (4 * a * c)

    if D == 0:
        root = -b / (2 * a)
        return f"The equation has one repeated root: {root}"

    elif D > 0:
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D)) / (2 * a)
        return f"First Root = {root1}\nSecond Root = {root2}"

    else:
        real = -b / (2 * a)
        imag = math.sqrt(-D) / (2 * a)
        return f"Root1 = {real} + {imag}i\nRoot2 = {real} - {imag}i"


# ---------------- Age Calculator ---------------- #
def AgeCalculator(current_year, birth_year):
    if birth_year > current_year:
        return "Invalid Birth Year!"
    else:
        age = current_year - birth_year
        return f"Your Age is {age} years."


# ---------------- BMI Calculator ---------------- #
def BMICalculator(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 25:
        status = "Normal Weight"
    elif bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    return f"BMI = {round(bmi,2)}\nCategory = {status}"


# ---------------- EMI Calculator ---------------- #
def EMICalculator(principal, rate, years):
    monthly_rate = rate / (12 * 100)
    months = years * 12

    emi = (principal * monthly_rate * ((1 + monthly_rate) ** months)) / \
          (((1 + monthly_rate) ** months) - 1)

    return f"Monthly EMI = {round(emi,2)}"


# ---------------- Main Program ---------------- #
while True:

    print("=" * 40)
    print("        MULTI UTILITY CALCULATOR")
    print("=" * 40)
    print("1. Arithmetic Operations")
    print("2. Quadratic Equation")
    print("3. Age Calculator")
    print("4. BMI Calculator")
    print("5. EMI Calculator")
    print("6. Exit")
    print("=" * 40)

    choice = input("Enter your choice: ")

    match choice:

        # Arithmetic Calculator
        case "1":
            print("-" * 40)
            print("Operators Available: +  -  *  /")
            equation = input("Enter your equation: ")

            numbers = re.findall(r'\d+', equation)
            operators = re.findall(r'[+\-*/]', equation)

            if len(numbers) < 2:
                print("Invalid Expression!")
            else:
                print("=" * 40)
                print("Result =", arithmaticCalculate(numbers, operators))

            print("-" * 40)

        # Quadratic Equation
        case "2":
            print("-" * 40)
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))

            print(QuadraticEquation(a, b, c))
            print("-" * 40)

        # Age Calculator
        case "3":
            print("-" * 40)
            current_year = int(input("Enter Current Year: "))
            birth_year = int(input("Enter Birth Year: "))

            print(AgeCalculator(current_year, birth_year))
            print("-" * 40)

        # BMI Calculator
        case "4":
            print("-" * 40)
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))

            print(BMICalculator(weight, height))
            print("-" * 40)

        # EMI Calculator
        case "5":
            print("-" * 40)
            principal = float(input("Enter Loan Amount: "))
            rate = float(input("Enter Annual Interest Rate (%): "))
            years = int(input("Enter Loan Duration (Years): "))

            print(EMICalculator(principal, rate, years))
            print("-" * 40)

        # Exit
        case "6":
            print("\nThank You for Using the Calculator!")
            break

        # Invalid Choice
        case _:
            print("Invalid Selection! Please Try Again.")