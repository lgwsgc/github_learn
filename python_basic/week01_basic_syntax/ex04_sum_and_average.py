def main():
    a = int(input("Please enter a positive integer: "))
    if a <= 0:
        print("a must be a positive integer.")
        return

    total = 0
    for i in range(1, a + 1):
        total += i

    print(f"sum: {total}")
    print(f"average: {total / a}")
   
if __name__ == "__main__":
    main()