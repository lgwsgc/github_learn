def main():
    try:
        a_str = input("Please enter a number a: ")
        b_str = input("Please enter a number b: ")
        operator = input("Please enter the operator (+, -, *, /): ")

        a = float(a_str)
        b = float(b_str)  

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result = a * b
        elif operator == "/":
            if b == 0:  # 如果使用 b!= 0,要注意input的类型
                print("Error: Division by zero!")
                return
            result = a / b
        else:
            print("Unknown operator, please use one of +, -, *, /")
            return

        print(f"{a} {operator} {b} = {result}")
    except ValueError:
        print("Invalid number, please enter valid numeric values.")

if __name__ == "__main__":
    main()