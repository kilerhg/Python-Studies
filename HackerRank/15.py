'''
In the first line, print True if has any alphanumeric characters. Otherwise, print False.
In the second line, print True if has any alphabetical characters. Otherwise, print False.
In the third line, print True if has any digits. Otherwise, print False.
In the fourth line, print True if has any lowercase characters. Otherwise, print False.
In the fifth line, print True if has any uppercase characters. Otherwise, print False.
'''
if __name__ == '__main__':
    lista = [0,0,0,0,0]
    s = str(input())
    for i in s:
        if i.isalnum():
            lista[0] = 1
        if i.isalpha():
            lista[1] = 1
        if i.isdigit():
            lista[2] = 1
        if i.islower():
            lista[3] = 1
        if i.isupper():
            lista[4] = 1
    for x in lista:
        if x == 1:
            print('True')
        else:
            print('False')