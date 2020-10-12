k = int(input(''))
STDIN = str(input('')).strip()
b = STDIN.split()
for x in b:
    if b.count(x) == 1:
        c = x
        break
print(c)