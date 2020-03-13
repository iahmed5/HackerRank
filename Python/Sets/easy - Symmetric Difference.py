a = input()
an = set(input().split())
b = input()
bn = set(input().split())
sdiffernce = (an.difference(bn)).union(bn.difference(an))
sortedset = sorted(sdiffernce, key=int, reverse=False)
for num in sortedset:
    print(num)
