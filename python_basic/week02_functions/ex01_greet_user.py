"""
把第一周的“问名字 + 年龄”改成用函数写：
定义一个函数：
def greet(name: str, age: int) -> None:
    ...
main() 里只负责：
读输入；
转成合适类型；
调 greet(name, age)。
练习重点：
函数定义；
参数传递；
不返回值时默认 None。
"""

def  greet(name: str, age: int) -> None:
    print(f"Hello, {name} ! You are {age} years old.") 
    age = int(age)
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
     

if __name__ == "__main__":
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    greet(name, age)