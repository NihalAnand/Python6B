if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    y= max(arr)
    while max(arr) == y:
        arr.remove(y)

    print (max(arr))