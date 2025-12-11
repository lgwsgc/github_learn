"""
定义一个列表，例如：numbers = [1, 5, 8, 10, 12, 15, 18]
把列表中所有的偶数挑出来，放到一个新列表 even_numbers 里。
打印 even_numbers。
"""

def main():
    numbers = [1, 5, 8, 10, 12, 15, 18] 
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    print(f"even_numbers: {even_numbers}")

if __name__ == "__main__":
    main()