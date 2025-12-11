def main():
    try:
        name = input("Please enter your name: ")
        age = input("Please enter your age: ")
        
        age = int(age)
        print(f"Hello, {name} ! You are {age} years old.")
        if age >= 18:
            print("You are an adult.")
        else:
            print("You are a minor.")
    except ValueError:
        print("Invalid input. Please enter valid values.")

if __name__ == "__main__":
    main()
  