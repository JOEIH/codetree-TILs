n = int(input())

def down_up(n):
    if n == 0:
        return

    print(n, end=' ')
    down_up(n-1)
    print(n, end=' ')

down_up(n)