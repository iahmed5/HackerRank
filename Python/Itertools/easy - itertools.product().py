a = input().split()
b = input().split()

lst = []
for index in a:
    for index2 in b:
        lst.append("(" + index + ", " + index2 + ")")

print(*lst, sep = " ")
