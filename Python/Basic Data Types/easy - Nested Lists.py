if __name__ == '__main__':
    lst = []
    secondmaxlst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
        secondmaxlst.append(score)
    max = lst[0][1]
                
    secondmaxlst = list(dict.fromkeys(secondmaxlst))
    secondmaxlst.sort()

    secondmax = secondmaxlst[0]
    if(len(secondmaxlst) > 1):
        secondmax = secondmaxlst[1]

    names = []
    for i in range(len(lst)):
        if(lst[i][1] == secondmax):
            names.append(lst[i][0])

    names.sort()
    print(*names, sep = "\n")
