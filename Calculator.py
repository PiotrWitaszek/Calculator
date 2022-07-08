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
    while True:
        choice = input("Enter choice(1/2/3/4): ")
 
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
 # Jak wprowadzam wartość nieliczbową to pojawia się na przykład ValueError: could not convert string to float: 'x' i zamyka program,
 #  ale gdy wybieram działanie i wpisuję x to nie ma tego problemu
        if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
 
        elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))
 
        elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))
 
        elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))
    else:
        exit(1)

# O takie coś chodziło?

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
    pass
