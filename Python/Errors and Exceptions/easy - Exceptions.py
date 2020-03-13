lines = int(input())
for line in range(lines):
    arr = input().split()
    a = arr[0]
    b = arr[1]
    try:
        print(int(a)//int(b))
    except Exception as e:
        print("Error Code:", e)
