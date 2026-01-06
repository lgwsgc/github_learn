r""""
要求：
定义一个列表，例如：nums = [5, 2, 9, 1, 5, 6]
完成并打印：
列表长度
列表中第一个和最后一个元素
按升序排序后的新列表（原列表保持不变）
去掉第一个和最后一个元素后的子列表（用切片）
把列表中所有元素 +1，形成一个新的列表（可以用 for 循环，也可以练习列表推导式）
"""

if __name__ =="__main__":
    nums = [5, 2, 9, 1, 5, 6]
    i = 0
    for num in nums:
        i += 1
    print(f"列表长度: {len(nums)} or {i}")
    print(f"列表中第一个和最后一个元素: {nums[0]} and {nums[-1]}")
    num2 = nums.copy()
    num2.sort()
    print(f"按升序排序后的新列表: {num2}")
    print(f"去掉第一个和最后一个元素后的子列表: {nums[1:-1]}")
    num3 = [num+1 for num in nums]
    print(f"num3: {num3}")
