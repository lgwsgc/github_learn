def main3():
    a = float(input("Please enter number a: "))
    b = float(input("Please enter number b: "))
    c = float(input("Please enter number c: "))

    nums_list = [a, b, c]
    num_max = nums_list[0]
    for num in nums_list[1:]:
        if num > num_max:
            num_max = num

    print(f"The max of {a}, {b}, {c} is {num_max}")


if __name__ == "__main__":
    main3()