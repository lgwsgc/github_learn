r"""
ex05_is_prime.py
定义两个函数：
def is_prime(n: int) -> bool:
    判断 n 是否为质数（大于 1 且只有 1 和自己两个因子）
    ...
def print_primes_up_to(limit: int) -> None:
    打印 2 到 limit 之间的所有质数
    ...
main() 做：
让用户输入一个整数 n:
调 print_primes_up_to(n)。
练习重点：
组合函数：一个函数内部调用另一个函数；
for 循环 + break / continue 的使用。
"""

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    upper = int(n ** 0.5) +1  # 优化
    for i in range(2, upper):
        if n % i == 0:
            return False
    return True

def print_primes_up_to(n: int) -> None:

    if n < 2:
        print("No prime numbers.")
        return
    for i in range(2, n+1):
        if not is_prime(i):
            continue
        print(f"{i} is a prime number.")
        # else:
        #     print(f"{i} is not a prime number.")
    

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print_primes_up_to(num)





 
