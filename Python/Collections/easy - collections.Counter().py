from collections import Counter
noOfShoes = int(input())
shoes = Counter(map(int, input().split()))

income = 0;

noOfCustomers = int(input())
for index in range(noOfCustomers):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
    
print(income)
