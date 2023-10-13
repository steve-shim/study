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

# N = int(input())
# map = [list(map(int, input().strip())) for _ in range(N)]
# chk = [[False] * N for _ in range(N)]
# result = []
# each = 0

def solution(testcase):
    if testcase:
        map = testcase
        N = len(testcase)
        chk = [[False] * N for _ in range(N)]
        result = []
        #each = 0
    print(map)
    print(chk)
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    def dfs(y,x,each):
        each += 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    dfs(ny, nx, each)
                else:
                    return each


    for j in range(N):
        for i in range(N):
            if map[j][i] == 1 and chk[j][i] == False:
                # 방문체크표시
                chk[j][i] = True
                # DFS로 크기 구하기
                each = 0
                dfs(j,i,each)
                # 크기를 결과 리스트에 넣기
                result.append(each)

    result.sort()
    print(len(result))
    for i in result:
        print(i)
        
if __name__ == '__main__':
    testcase = [[0,1,1,0,1,0,0],
                [0,1,1,0,1,0,1],
                [1,1,1,0,1,0,1],
                [0,0,0,0,1,1,1],
                [0,1,0,0,0,0,0],
                [0,1,1,1,1,1,0],
                [0,1,1,1,0,0,0]]
    
    solution(testcase)