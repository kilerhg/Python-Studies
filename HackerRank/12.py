def swap_case(string):
    string = str(string)
    var = ''
    for i in s:
        if i.isupper():
            var += i.lower()
        else:
            var += i.upper()
    return var


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)