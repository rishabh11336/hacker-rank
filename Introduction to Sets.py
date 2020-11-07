def average(array):
    # your code goes here
    uniqe = set(array)
    return sum(uniqe)/len(uniqe)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)