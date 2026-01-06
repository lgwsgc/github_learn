r""""
目标： 用 set 理解“无序、不重复”。
要求：
定义一个列表，例如：nums = [1, 2, 2, 3, 4, 4, 5]
用 set 去重，得到 unique_nums。
对比：
原列表长度
去重后长度
把 unique_nums 再变回排序后的列表（sorted()）。
顺带理解：
set 不能保证顺序；
set 很适合做“去重”和“集合运算”（交集/并集/差集）。
sorted() vs sort()
sorted() 返回一个新列表，原列表不变
sort() 是列表方法，原列表改变
sorted()：适用于任何可迭代对象（list、tuple、set、dict、字符串、生成器…）
注意：对 dict 直接 sorted(d) 默认是排序 key
.sort()：只存在于 list 方法（只能给 list 用）
3) 性能与内存
list.sort()：通常更省内存（原地排序），很多场景也更快一点
sorted()：会创建新列表，占用额外内存，但更安全（不改原数据）
4) 参数（两者基本一样）
两者都支持：
key=...：指定排序依据
reverse=True：降序
"""
if __name__ == "__main__":
    nums = [6, 1, 7, 2, 3, 4, 4, 5]
    unique_nums = set(nums)
    print(unique_nums)
    print(len(nums))
    print(len(unique_nums))
    print(sorted(unique_nums))
