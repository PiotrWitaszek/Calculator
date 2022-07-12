import sys
import logging
logging.basicConfig(level=logging.DEBUG)


def add(x, y):
    return x + y
 
def subtract(x, y):
    return x - y
 
def multiply(x, y):
    return x * y
 
def divide(x, y):
    return x / y

if __name__ == "__main__":
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("x.Exit programm")
    while True:
        choice = input("Enter choice(1/2/3/4/x): ")
 
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
 
        if choice == '1':
            logging.debug('Adding: {} and {}'. format(num1, num2,)) 
            print("Result is", add(num1, num2))
        elif choice == '2':
            logging.debug('Subtracting: {} and {}'. format(num1, num2,)) 
            print("Result is", subtract(num1, num2))
        elif choice == '3':
            logging.debug('Multiplying: {} and {}'. format(num1, num2,)) 
            print("Result is", multiply(num1, num2))
        elif choice == '4':
            logging.debug('Dividing: {} and {}'. format(num1, num2,)) 
            print("Result is", divide(num1, num2))
        elif choice == 'x':
            exit()
        else:
            print("Invalid input")



