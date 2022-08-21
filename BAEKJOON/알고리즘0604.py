import sys
T = int(sys.stdin.readline())
print("T",T)
for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print("N",N, "M",M)
    c = 0
    for i in range(N,M+1):
        c += str(i).count('0')
    print(c)
