# 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for x in range(0,arr.count(max(arr))):
        arr.remove(max(arr))
    print(max(arr))