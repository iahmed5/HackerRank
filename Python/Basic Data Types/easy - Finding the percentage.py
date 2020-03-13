if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marksTotal = 0
    marks = student_marks.get(query_name)
    for mark in marks:
        marksTotal += float(mark)
    
    print(format(marksTotal/3, '.2f'))
