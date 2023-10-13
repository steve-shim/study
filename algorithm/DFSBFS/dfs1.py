# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 3
# 7
# 8
# 9

# -이중 for문, 값1 && 방문x => DFS
# -DFS를 통해 찾은 값을 저장 후 정렬해서 출력

import sys
input = sys.stdin.readline

map = [[0,1,1,0,1,0,0],
        [0,1,1,0,1,0,1],
        [1,1,1,0,1,0,1],
        [0,0,0,0,1,1,1],
        [0,1,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,1,1,1,0,0,0]]
N = len(map)

# N = int(input())
# map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = []
#each = 0
print(map)
print(chk)

    #우,하,좌,상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < N and 0 <= nx < N:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx) 

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문체크표시
            chk[j][i] = True
            # DFS로 크기 구하기
            each = 0
            dfs(j,i)
            # 크기를 결과 리스트에 넣기
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)


if __name__ == '__main__':
    pass