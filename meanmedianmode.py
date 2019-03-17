def getMean(lis):
    sum = 0
    for i in lis:
        sum += i
    mean = (sum) / len(lis)
    return mean

def getMedian(lis):
    median = 0.0
    size = len(lis)
    copy = lis
    copy.sort()
    if(size % 2 == 0):
        median = (copy[size//2 - 1] + copy[size//2]) / 2
    else:
        median =(copy[(size)//2])
    return median

def getMode(lis):
    mode = 0
    size = len(lis)
    count, max = 0, 0
    copy = lis
    copy.sort()
    current = 0
    for i in copy:
        if (i == current):
            count += 1
        else:
            count = 1
            current = i
        if (count > max):
            max = count
            mode = i
    return mode

size = int(input())
a = list(map(int,input().split()))
print (getMean(a))
print (getMedian(a))
print (getMode(a))