def main():
    a = int(input("Please enter the a(num): "))
    nums = 0
    for i in range (a+1):
       nums += i
    print(f"nums: {nums}")
    print(f"average : {nums / a}")
   
   
if __name__ == "__main__":
    main()