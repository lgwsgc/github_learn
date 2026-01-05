"""
ex02_calculator_func.py
把简易计算器拆成 函数 + 主程序：
定义一个函数：
def calculate(a: float, b: float, operator: str) -> float:
    # 内部处理 + - * /，出错时可以抛出 ValueError
main() 负责：
input → 转成 float；
调 calculate；
捕获异常（比如除零 / 非法运算符），打印提示。
练习重点：
函数返回值；
try/except 配合函数使用；
把逻辑收拢到函数里，main() 更清爽。
"""

def calculate(a: float, b: float, operator: str) -> float:
    if operator == "+":
        return a+b
    elif operator == "-":
        return a-b
    elif operator == "*":
        return a*b
    elif operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a/b
    else:
        raise ValueError("Invalid operator")

if __name__ == "__main__":
    try:
        a = float(input("enter a: "))
        b = float(input("enter b: "))
        operator = input("enter operator: ")
        result = calculate(a,b,operator)
        print(result)
    except ValueError as e:
        print(e)
