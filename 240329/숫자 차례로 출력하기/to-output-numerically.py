N = int(input())

def up(N):
    if N == 0:
        return
    
    up(N-1)
    print(N, end=" ")

up(N)
print()

def down(N):
    if N == 0:
        return
    
    print(N, end=" ")
    down(N-1)

down(N)