if __name__ == '__main__':
    n = int(input())
    arr = [int(item) for item in input().split()]

    arr.sort(reverse=True)
    ans = (set(arr))
    print(ans[n-1])