r"""
目标： 练习 list[dict] 这种结构。
要求：
定义一个「学生成绩表」，例如：
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]
写函数：
print_all(students)：打印每个学生的名字和成绩；
get_average_score(students) -> float：返回平均分；
get_top_student(students) -> dict：返回分数最高的学生 dict。
在 main() 里调用这些函数，打印：
全部学生；
平均分；
最高分学生的信息。"""



def print_all(students):
    for student in students:
        print(f"{student['name']}: {student['score']}")
def get_average_score(students) -> float:
    scores = 0
    for student in students:
        scores += int(student['score'])
    return scores / len(students)
def get_top_student(students) -> dict:
    max_score = 0
    max_name = ""
    for student in students:
        name = student['name']
        score = int(student['score'])
        if score > max_score:
            max_score = score
            max_name = name
    print(f"name: {max_name}, score: {max_score}") 
    return max_name, max_score
    

def main(students):
    print_all(students)
    print(get_average_score(students))
    print(get_top_student(students))

if __name__ == "__main__":
    students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
]
    main(students)
