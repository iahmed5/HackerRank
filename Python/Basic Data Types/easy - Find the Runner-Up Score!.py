if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    secondList = []
    for num in arr:
        if num not in secondList:
            secondList.append(num)
    secondList.sort()
    if(len(secondList) > 1):
        print(secondList[-2])
    else:
        print(secondList[0])
