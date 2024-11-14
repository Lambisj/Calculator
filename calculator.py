def calculator():
    while True:
        num1 = input("Give the first number: ")
        if num1 == 'OFF':
            print("ADIOS")
            break

        operator = input("Choose your fighter (+, -, *, /): ")
      
        if not (num1.isdigit() and num2.isdigit()):
            print("Please give me numbers amigo.")
            continue

        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Cant division with the 0 amigo.")
                continue
            else:
                result = num1 / num2
        else:
            print("ERROR 404!!! WRONG OPERATION!!!")
            continue

        print("THe result is:", result)

if __name__ == "__main__":
    calculator()

