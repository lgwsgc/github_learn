r"""
ex03_max_of_three_func.py
给“三数取最大值”也写一个函数：
def max_of_three(a: float, b: float, c: float) -> float:
    ...
要求：
不调用内置 max()，自己用 if/else 或循环实现一遍；
main() 只负责读输入、调用函数、打印结果。
练习重点：
练习写“纯函数”（输入 → 输出，没有副作用）；
把一段逻辑抽象出来，方便以后复用。
"""

def max_of_three1(a: float, b: float, c: float) -> float:
    list_num = [a,b,c]
    max_num = max(list_num)
    return max_num

def max_of_three(a: float, b: float, c: float) -> float:
    list_num = [a,b,c]
    max_num = list_num[0]
    for num in list_num[1:]:
        if num > max_num:
            max_num = num
    return max_num

if __name__ == "__main__":
    a = float(input("enter a: "))
    b = float(input("enter b: "))
    c = float(input("enter c: "))
    print(max_of_three(a, b, c))