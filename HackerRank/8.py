# 
n = int(input().strip())
if n % 2 == 0:
    if 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')
else:
    print('Weird')