import re
import math

def arithmaticCalculate(number,operator):
    num_list = [int(num) for num in number]
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
            
while True:
    print("="*30)
    print("1. Arithmetic Operations")
    print("2. Quadratic Equation")
    print("="*30)
    choice = input("Enter your choice : ")

    match(choice):
        case "1":
            print("-"*30)
            print("| + | - | * | / |")
            opr = input("Enter your equation : ")
            regex = '\d+'
            operators = '[+*/-]'
            number = re.findall(regex, opr)
            symbol = re.findall(operators,opr)
            print('='*30)
            print(f"Result: {arithmaticCalculate(number,symbol)}")
            print("-"*30)
            
        case "2":
            print("-"*30)
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            c = int(input("Enter c: "))
            print(QuadraticEquation(a,b,c))
            print("-"*30)
        case _:
            print("Invalid Selection!")