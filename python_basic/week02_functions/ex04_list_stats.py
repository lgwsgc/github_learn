r"""
ex04_list_stats.py
定义一个函数，接受一个数字列表，返回统计结果：
def list_stats(numbers: list[float]) -> dict:
    返回一个字典，包含:
    - sum
    - avg
    - max
    - min
"""

def list_stats(numbers: list) -> dict:
    sum_num = 0
    for num in numbers:
        sum_num += num
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers[1:]: 
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return {"sum": sum_num, "avg": sum_num/len(numbers), "max": max_num, "min": min_num}

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(list_stats(numbers))