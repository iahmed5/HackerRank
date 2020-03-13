def count_substring(string, sub_string):
    occurences = 0
    for index in range(0, len(string)):
        if((index) + len(sub_string) - 1) <= len(string):
            substring = string[index: index + len(sub_string)]
            if(substring == sub_string):
                occurences += 1

    return occurences


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
