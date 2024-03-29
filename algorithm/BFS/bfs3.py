# Mirror Exodus

'''
(1,1)에서 (N,M)에 출구가 있고,
한 칸에 한 번씩 이동이 가능. 괴물이 있는 부분은 0로 표시가 된다.
괴물이 없는 부분은 1

미로는 반드시 탈출 가능. 움직여야 하는 최소 칸의 개수는?

첫째 줄에 두 정수 주어짐 4<=N, M<=200
주어지는 수들은 공백이 없다.

이 때 최소 이동 칸의 수를 구하는데, 시작 칸과 마지막 칸을 포함한다.
'''

'''
입구
↓
101010
111111
000001
111111
111111 ←출구

리스트를 이런식으로 입력받는다고 하면, 어떻게 해야 '최단거리'로 출구에 도달 가능할까
'''

# 아이디어
'''
0을 만나면 그 방향으로는 진행을 못할거고 1을 만나면 당연히 진행하게 될 것이다. 이것은 명백하고 그렇게 진행해야만 하는데
만약에 진행할 수 있는 방향이 여러 개면 어떻게 처리해야 할까.
일단, 출구는 반드시 오른쪽 꼭지점에 위치한다는 것을 기억
될 수 있으면, 우측과 아래 방향으로 이어 나가고, 그게 안되면 왼쪽 방향이나 위쪽 방향으로 틀어야 한다.
극단적으로

입구
↓
10111
11101
00011
00010
00011←출구

이런 미로가 주어질 수도 있음. 이 미로 같은 경우에는 위로 돌아가는게 한 번 존재하고
왼쪽으로 한번 돌아가는 것도 존재한다.
'''

# 리스트 입력 받기
n,m=map(int,input().split()) # 행, 열 입력
graph=[list(map(int,input())) for _ in range(1,n+1)]
print(graph)
'''
우선 처음으로 드는 생각은 어떻게든 돌아서라도 길을 가야한다는 생각
그 다음에 한번 지난 노드는 다시 재방문 하면 안된다는 생각.
여기서 DFS나 BFS를 생각할 수 있게 된다.

솔직히 DFS도 가능할 것 같은데 BFS로 작성하면 아래와 같다.
이렇게 보는 이유는, 1칸 인접한 노드 끼리는 같은 노드일 것인데, 이 노드 들로 접근하면 된다.

'''

# 방향을 정의 해야 한다. 알고리즘 풀 때는 종종 쓰이는 방식
dx=[-1,1,0,0] # 상하 방향을 정의함
dy=[0,0,-1,1] # 좌우 방향을 정의함

# 이것들이 같은 인덱스를 하나씩 읽으면 그것이 현재 방향으로 부터 next 방향이라고 할 수 있음.

from collections import deque

def BFS(i,j):

    queue=deque() # 시작 노드 하나 input 하고 시작.
    queue.append((i,j))
    
    while queue: # 큐가 가득 차 있을 동안에 이걸 반복한다.
        print("queue",queue)
        i,j=queue.popleft()

        # 현재 위치에서 네 방향 확인이 필요
        for k in range(4): # k가 dx,dy 방향 벡터 리스트를 순회하면서 next 방향을 찾음.
            next_i=i+dx[k]
            next_j=j+dy[k] # 이렇게 for 문 돌면 상하좌우 다 살펴본다.

            # 미로 찾기 공간 벗어난 경우 무시한다.
            if next_i<0 or next_j<0 or next_i>=n or next_j>=m:
                continue # 무시하고 진행하기를 택한다. 여기 걸리면 for 문 처음으로 돌아감

            # 벽이 있다면(괴물이 있다면) 피함
            if graph[next_i][next_j]==0:
                continue # 마찬가지

            # 해당 노드를 처음 방문하는 경우에 최단 거리를 기록함
            if graph[next_i][next_j]==1:
                graph[next_i][next_j]=graph[i][j]+1 # 이 값이 점점 1에서 늘어나게 되는 것이다.
                queue.append((next_i,next_j)) # 방문한 곳은 인덱스를 기록한다.

    return graph[n-1][m-1] # 가장 오른쪽 아래의 최단 거리 반환


print(BFS(0,0))