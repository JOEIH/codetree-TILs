N = int(input())

def st(N):
    if N == 0:
        return

    st(N - 1)
    print("HelloWorld")

st(N)