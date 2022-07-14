# 
if __name__ == '__main__':
    n = int(input())
    var = ''
    for x in range(n-1,0,-1):
        n = f'{x}{n}'
    print(n)