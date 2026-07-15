import re
import math
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt, IntPrompt

console = Console()

def arithmaticCalculate(number,operator):
    num_list = [float(num) for num in number]
    if(operator[0] == '+'):
        result = num_list[0] + num_list[1]
    elif(operator[0] == '-'):
        result = num_list[0] - num_list[1]
    elif(operator[0] == '*'):
        result = num_list[0] * num_list[1]
    elif(operator[0] == '/'):
        result = num_list[0] / num_list[1]
    else:
        pass
    
    for indx in range(1,len(operator)):
        if(operator[indx] == '+'):
            result = result + num_list[indx+1]
        elif(operator[indx] == '-'):
            result = result - num_list[indx+1]
        elif(operator[indx] == '*'):
            result = result * num_list[indx+1]
        elif(operator[indx] == '/'):
            result = result / num_list[indx+1]
        else:
            pass
    return result

def QuadraticEquation(a,b,c):
    if a == 0:
        return "Equation is linear."
    else:
        D = (math.pow(b,2)) - 4*(a*c)
        if D == 0:
            single_root = (-b) / (2*a) # \(-b / (2a)\).
            return f"The equation has exactly one real repeated root: {single_root}"
        elif D > 0:
            first_root = (-b + math.sqrt(D)) / (2*a)
            second_root = (-b - math.sqrt(D)) / (2*a)
            return f"First root: {first_root}, Second root: {second_root}"
        elif D < 0:
            real_part = (-b) / (2*a)
            imgr_part = math.sqrt(abs(D)) / (2*a)
            return f"Real part: {real_part}, Imaginary Part: {imgr_part}"

def AgeCalculator(cur,birth):
    return "Invalid Birth Year!" if birth>cur else f"Your Age is {cur-birth} years."

def BMICalculator(weight,height):
    bmi=weight/(height**2)
    if bmi<18.5: cat="Underweight"
    elif bmi<25: cat="Normal"
    elif bmi<30: cat="Overweight"
    else: cat="Obese"
    return f"BMI = {bmi:.2f}\nCategory = {cat}"

def EMICalculator(p,r,y):
    m=r/(12*100); n=y*12
    emi=(p*m*(1+m)**n)/(((1+m)**n)-1)
    return f"Monthly EMI = ₹{emi:.2f}"

def ScientificCalculator(op,value):
    op = op.lower().strip()
    if op in ["sin", "cos", "con", "tan", "cot", "cosec", "sec"]:
        rad = math.radians(value)
        if op == "sin":
            return f"sin({value}) = {math.sin(rad):.6f}"
        elif op in ["cos", "con"]:
            return f"cos({value}) = {math.cos(rad):.6f}"
        elif op == "tan":
            return f"tan({value}) = {math.tan(rad):.6f}"
        elif op == "cot":
            tan_val = math.tan(rad)
            if abs(tan_val) < 1e-12:
                return "cot is undefined for this angle."
            return f"cot({value}) = {1/tan_val:.6f}"
        elif op == "cosec":
            sin_val = math.sin(rad)
            if abs(sin_val) < 1e-12:
                return "cosec is undefined for this angle."
            return f"cosec({value}) = {1/sin_val:.6f}"
        elif op == "sec":
            cos_val = math.cos(rad)
            if abs(cos_val) < 1e-12:
                return "sec is undefined for this angle."
            return f"sec({value}) = {1/cos_val:.6f}"
    elif op == "log2":
        if value <= 0:
            return "log base 2 is defined only for positive numbers."
        return f"log2({value}) = {math.log2(value):.6f}"
    return "Invalid scientific operation."

while True:
    console.clear()
    t=Table(title="🧮 Multi Utility Calculator",header_style="bold cyan")
    t.add_column("Option",justify="center")
    t.add_column("Operation")
    for a,b in [("1","Arithmetic"),("2","Scientific Calculator"),("3","Quadratic Equation"),("4","Age Calculator"),("5","BMI Calculator"),("6","EMI Calculator"),("7","Exit")]:
        t.add_row(a,b)
    console.print(t)
    ch=Prompt.ask("Enter your choice")
    if ch=="1":
        eq=Prompt.ask("Enter expression (e.g. 10+20*3)")
        nums=re.findall(r'\d+\.?\d*',eq)
        ops=re.findall(r'[+\-*/]',eq)
        console.print(Panel(str(arithmaticCalculate(nums,ops)),title="Result",border_style="green"))
    elif ch=="2":
        sci_table = Table(title="Scientific Calculator",header_style="bold green")
        sci_table.add_column("Key",justify="center")
        sci_table.add_column("Operation")
        for k,v in [("1","sin"),("2","cos(con)"),("3","tan"),("4","cot"),("5","cosec"),("6","sec"),("7","log base 2"),("8","factorial")]:
            sci_table.add_row(k,v)
        console.print(sci_table)

        sci_choice = Prompt.ask("Choose operation", choices=["1","2","3","4","5","6","7","8"])
        if sci_choice == "1":
            angle = FloatPrompt.ask("Enter angle in degrees")
            result = ScientificCalculator("sin", angle)
        elif sci_choice == "2":
            angle = FloatPrompt.ask("Enter angle in degrees")
            result = ScientificCalculator("cos", angle)
        elif sci_choice == "3":
            angle = FloatPrompt.ask("Enter angle in degrees")
            result = ScientificCalculator("tan", angle)
        elif sci_choice == "4":
            angle = FloatPrompt.ask("Enter angle in degrees")
            result = ScientificCalculator("cot", angle)
        elif sci_choice == "5":
            angle = FloatPrompt.ask("Enter angle in degrees")
            result = ScientificCalculator("cosec", angle)
        elif sci_choice == "6":
            angle = FloatPrompt.ask("Enter angle in degrees")
            result = ScientificCalculator("sec", angle)
        elif sci_choice == "7":
            val = FloatPrompt.ask("Enter a positive number")
            result = ScientificCalculator("log2", val)
        elif sci_choice == "8":
            n = IntPrompt.ask("Enter a non-negative integer")
            if n < 0:
                result = "Factorial is only defined for non-negative integers."
            else:
                result = f"{n}! = {math.factorial(n)}"

        console.print(Panel(result,title="Scientific Calculator",border_style="white"))
    elif ch=="3":
        a=FloatPrompt.ask("Enter a"); b=FloatPrompt.ask("Enter b"); c=FloatPrompt.ask("Enter c")
        console.print(Panel(QuadraticEquation(a,b,c),title="Quadratic Equation",border_style="blue"))
    elif ch=="4":
        cy=IntPrompt.ask("Current Year"); by=IntPrompt.ask("Birth Year")
        console.print(Panel(AgeCalculator(cy,by),title="Age Calculator",border_style="cyan"))
    elif ch=="5":
        w=FloatPrompt.ask("Weight (kg)"); h=FloatPrompt.ask("Height (m)")
        console.print(Panel(BMICalculator(w,h),title="BMI Calculator",border_style="magenta"))
    elif ch=="6":
        p=FloatPrompt.ask("Loan Amount"); r=FloatPrompt.ask("Interest Rate (%)"); y=IntPrompt.ask("Years")
        console.print(Panel(EMICalculator(p,r,y),title="EMI Calculator",border_style="yellow"))
    elif ch=="7":
        console.print(Panel("Thank you for using the calculator!",border_style="green"))
        break
    else:
        console.print("[red]Invalid choice[/red]")
    input("Press Enter to continue...")