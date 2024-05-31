#TASK 2
#SIMPLE CALCULATOR

def add(a,b):
    return a + b

def sub (a,b):
    return a - b

def multiply (a,b):
    return a * b

def divide (a,b):
    if b==0:
        return "Error!"
        return "Division by zero."
    return a / b

def calculator ():
    print("Select an operation to be performed:")
    print ("1. Addtion")
    print ("2.Subtraction")
    print ("3. Multiplication")
    print ("4. Division")

    while True:
        choice = input ("Enter your choice: ")
        if  choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number:"))
                num2 = float(input("Enter second number:"))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"The result of {num1}+{num2} is {add(num1,num2)}")

            elif choice == '2':
                print(f"The result of {num1}-{num2} is {sub(num1,num2)}")

            elif choice == '3':
                print(f"The result of {num1}+{num2} is {add(num1,num2)}")

            elif choice == '4':
                result = divide(num1,num2)
                print(f"The result of {num1}+{num2} is {add(num1,num2)}")
            break   

        else:
            print ("Invalild choice. Please enter a valid option.")

if __name__ == "__main__":
    calculator()         
