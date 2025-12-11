"""
用两层 for 循环：
外层控制行（从 1 到 9）
内层控制列（从 1 到 当前行数）
"""

def main():
    a = 10
    for j in range(1, a):
        for i in range(1, j+1):
            print(f" {i} * {j} = {j * i} ", end="")
        # print(f"\n")
        print()
if __name__ == "__main__":
    main()
