import math
import re
import tkinter as tk


def arithmetic_calc(expression):
    tokens = re.findall(r'\d+\.\d+|\d+|[()+\-*/]', expression.replace(' ', ''))
    if not tokens:
        return "Invalid expression"

    values = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def apply_op():
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            values.append(left / right)

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            values.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_op()
            if operators and operators[-1] == '(':
                operators.pop()
        elif token in precedence:
            while operators and operators[-1] in precedence and precedence[operators[-1]] >= precedence[token]:
                apply_op()
            operators.append(token)

    while operators:
        apply_op()

    result = values[0]
    if result.is_integer():
        return str(int(result))
    return str(result)


def scientific_calc(choice, value):
    angle = math.radians(value)
    if choice == 'sin':
        return f"sin({value}) = {math.sin(angle):.6f}"
    if choice == 'cos':
        return f"cos({value}) = {math.cos(angle):.6f}"
    if choice == 'tan':
        return f"tan({value}) = {math.tan(angle):.6f}"
    if choice == 'cot':
        result = math.tan(angle)
        return "cot is undefined" if result == 0 else f"cot({value}) = {1 / result:.6f}"
    if choice == 'cosec':
        result = math.sin(angle)
        return "cosec is undefined" if result == 0 else f"cosec({value}) = {1 / result:.6f}"
    if choice == 'sec':
        result = math.cos(angle)
        return "sec is undefined" if result == 0 else f"sec({value}) = {1 / result:.6f}"
    if choice == 'log2':
        return "log2 is only for positive numbers" if value <= 0 else f"log2({value}) = {math.log2(value):.6f}"
    if choice == 'factorial':
        return "Factorial is only for non-negative numbers" if value < 0 else f"factorial({int(value)}) = {math.factorial(int(value))}"
    return "Invalid choice"


def age_calc(current_year, birth_year):
    return "Invalid birth year" if birth_year > current_year else f"Age = {current_year - birth_year} years"


def bmi_calc(weight, height):
    if height <= 0:
        return "Invalid height"
    bmi = weight / (height * height)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return f"BMI = {bmi:.2f}\nCategory = {category}"


def emi_calc(principal, rate, years):
    monthly_rate = rate / 1200
    months = years * 12
    if monthly_rate == 0:
        return f"Monthly EMI = {principal / months:.2f}"
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / (((1 + monthly_rate) ** months) - 1)
    return f"Monthly EMI = {emi:.2f}"


def quadratic_calc(a, b, c):
    if a == 0:
        return "Equation is linear"
    d = (b * b) - (4 * a * c)
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return f"Roots = {root1:.2f}, {root2:.2f}"
    if d == 0:
        return f"One root = {(-b) / (2 * a):.2f}"
    real_part = (-b) / (2 * a)
    imag_part = math.sqrt(abs(d)) / (2 * a)
    return f"Roots = {real_part:.2f} ± {imag_part:.2f}i"


def clear_inputs():
    for box in (entry_one, entry_two, entry_three):
        box.delete(0, tk.END)
    result_label.config(text="")


def set_mode(title, info, first, second="", third="", operation=False):
    global current_mode
    current_mode = title
    clear_inputs()
    mode_label.config(text=title)
    info_label.config(text=info)
    input_one_label.config(text=first)
    input_two_label.config(text=second)
    input_three_label.config(text=third)

    entry_two.grid_remove()
    entry_three.grid_remove()
    operation_menu.grid_remove()

    if second:
        entry_two.grid()
    if third:
        entry_three.grid()
    if operation:
        operation_menu.grid()


def calculate():
    try:
        if current_mode == "Basic Arithmetic":
            expression = entry_one.get().strip()
            if expression == "":
                result_label.config(text="Enter an expression", fg="red")
            else:
                result_label.config(text=f"Result = {arithmetic_calc(expression)}", fg="green")
        elif current_mode == "Scientific Calculator":
            value = entry_two.get().strip()
            if value == "":
                result_label.config(text="Enter a value", fg="red")
            else:
                result_label.config(text=scientific_calc(operation_var.get(), float(value)), fg="green")
        elif current_mode == "Age Calculator":
            current_year = entry_one.get().strip()
            birth_year = entry_two.get().strip()
            if current_year == "" or birth_year == "":
                result_label.config(text="Enter both years", fg="red")
            else:
                result_label.config(text=age_calc(int(current_year), int(birth_year)), fg="green")
        elif current_mode == "BMI Calculator":
            weight = entry_one.get().strip()
            height = entry_two.get().strip()
            if weight == "" or height == "":
                result_label.config(text="Enter weight and height", fg="red")
            else:
                result_label.config(text=bmi_calc(float(weight), float(height)), fg="green")
        elif current_mode == "EMI Calculator":
            principal = entry_one.get().strip()
            rate = entry_two.get().strip()
            years = entry_three.get().strip()
            if principal == "" or rate == "" or years == "":
                result_label.config(text="Enter all EMI values", fg="red")
            else:
                result_label.config(text=emi_calc(float(principal), float(rate), int(years)), fg="green")
        elif current_mode == "Quadratic Equation":
            a = entry_one.get().strip()
            b = entry_two.get().strip()
            c = entry_three.get().strip()
            if a == "" or b == "" or c == "":
                result_label.config(text="Enter a, b, and c", fg="red")
            else:
                result_label.config(text=quadratic_calc(float(a), float(b), float(c)), fg="green")
    except:
        result_label.config(text="Invalid input", fg="red")


root = tk.Tk()
root.title("Multi Calculator")
root.geometry("650x380")
root.resizable(False, False)

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=15, pady=15)

left_frame = tk.Frame(main_frame)
left_frame.pack(side="left", fill="y", padx=(0, 15))

right_frame = tk.Frame(main_frame)
right_frame.pack(side="left", fill="both", expand=True)

mode_label = tk.Label(right_frame, text="Basic Arithmetic", font=("Arial", 18, "bold"))
mode_label.pack(pady=(0, 5))

info_label = tk.Label(right_frame, text="Enter an expression like: 10+(20*3)", font=("Arial", 10))
info_label.pack(pady=(0, 15))

form_frame = tk.Frame(right_frame)
form_frame.pack(pady=5)

input_one_label = tk.Label(form_frame, text="Expression")
input_one_label.grid(row=0, column=0, sticky="w", pady=6)
entry_one = tk.Entry(form_frame, width=35)
entry_one.grid(row=0, column=1, pady=6, padx=10)

input_two_label = tk.Label(form_frame, text="")
input_two_label.grid(row=1, column=0, sticky="w", pady=6)
entry_two = tk.Entry(form_frame, width=35)
entry_two.grid(row=1, column=1, pady=6, padx=10)

input_three_label = tk.Label(form_frame, text="")
input_three_label.grid(row=2, column=0, sticky="w", pady=6)
entry_three = tk.Entry(form_frame, width=35)
entry_three.grid(row=2, column=1, pady=6, padx=10)

operation_var = tk.StringVar(value="sin")
operation_menu = tk.OptionMenu(form_frame, operation_var, "sin", "cos", "tan", "cot", "cosec", "sec", "log2", "factorial")
operation_menu.grid(row=1, column=2, padx=10)
operation_menu.grid_remove()

calculate_button = tk.Button(right_frame, text="Calculate", width=12, command=calculate)
calculate_button.pack(pady=12)

result_label = tk.Label(right_frame, text="", font=("Arial", 11), fg="blue")
result_label.pack(pady=10)

buttons = [
    ("Arithmetic", lambda: set_mode("Basic Arithmetic", "Enter an expression like: 10+(20*3)", "Expression")),
    ("Scientific", lambda: set_mode("Scientific Calculator", "Choose one operation and enter the value", "Operation", "Value", operation=True)),
    ("Age", lambda: set_mode("Age Calculator", "Enter current year and birth year", "Current Year", "Birth Year")),
    ("BMI", lambda: set_mode("BMI Calculator", "Enter weight in kg and height in meters", "Weight", "Height")),
    ("EMI", lambda: set_mode("EMI Calculator", "Enter loan amount, interest rate, and years", "Loan Amount", "Interest Rate (%)", "Years")),
    ("Quadratic", lambda: set_mode("Quadratic Equation", "Enter a, b, and c for ax² + bx + c = 0", "a", "b", "c")),
]

for text, command in buttons:
    tk.Button(left_frame, text=text, width=15, command=command).pack(pady=5)

current_mode = ""
set_mode("Basic Arithmetic", "Enter an expression like: 10+(20*3)", "Expression")
root.mainloop()
