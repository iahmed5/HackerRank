from itertools import permutations
inputData = input().split()
permutationsSaved = []
r = len(inputData[0])
if len(inputData) > 1 and inputData[1] != None:
    r = inputData[1]
for permutation in permutations(sorted(inputData[0]), int(r)):
    permuatationString = ""
    for singlePermutation in permutation:
        permuatationString += singlePermutation
    print(permuatationString)
