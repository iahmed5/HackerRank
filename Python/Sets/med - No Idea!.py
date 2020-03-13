check = input().split()
arr = input().split()
a = set(input().split())
b = set(input().split())
happiness = 0
for item in arr:
    if item in a:
        happiness += 1
    elif item in b:
        happiness -= 1

print(happiness)
