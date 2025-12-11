def main():
    a = input(f"Please enter the a(num): ")
    b = input(f"Please enter the b(num): ")
    operator = input(f"Please enter the operator(+, -, *, /): ")
    if operator == "+":
        print(f"{a} + {b} = {float(a) + float(b)}")
    elif operator == "-":
        print(f"{a} - {b} = {float(a) - float(b)}")
    elif operator == "*":
        print(f"{a} * {b} = {float(a) * float(b)}")
    elif operator == "/":
        if b != 0:
            print(f"{a} / {b} = {float(a) / float(b)}")
        else:
            print("Error: Division by zero!")
    else:
        print("please input the right operator or num!")

if __name__ == "__main__":
    main()

