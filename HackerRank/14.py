def count_substring(string, sub_string):
    string = str(string)
    sub_string = str(sub_string)
    count = 0
    for posi, i in enumerate(string):
        if string[posi:posi+len(sub_string)] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)