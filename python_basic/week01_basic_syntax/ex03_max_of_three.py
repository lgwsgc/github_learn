def main():
    a = input(f"Please enter the a(num): ")
    b = input(f"Please enter the b(num): ")
    c = input(f"Please enter the c(num): ")
    max = a
    if b > max:
        max = b
        if c > max:
            max = c
        elif c < max:
            max = c
    else:
        max = a 
        if max > c:
            max = max
        elif max < c:
            max = c
    print(f"The max of {a}, {b}, {c} is {max}")

def main2():
    a = input(f"Please enter the a(num): ")
    b = input(f"Please enter the b(num): ")
    c = input(f"Please enter the c(num): ")
    nums_list = [a, b, c]
    max_num = max(nums_list)
    print(f"The max of {a}, {b}, {c} is {max_num}")

def main3():
    a = input(f"Please enter the a(num): ")
    b = input(f"Please enter the b(num): ")
    c = input(f"Please enter the c(num): ")
    nums_list = [a, b, c]
    num_max = 0.0
    for i, num in enumerate(nums_list): # input() get str, so need to convert to int
        if (num_max) < int(num): 
            num_max = num
    print(f"The max of {a}, {b}, {c} is {num_max}")

if __name__ == "__main__":
    main3()