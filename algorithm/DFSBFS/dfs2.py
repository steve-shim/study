# DFS 메서드 정의
def dfs(graph, v, visited, j):
    # 현재 노드를 방문 처리
    j += 1
    visited[v] = True
    print(f"{j%10}[**dfs {v} in**] ".rjust(j*2), end='')
    print(v, end='')
    print(" visited",visited)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        print(f"graph[v] {v} -> {graph[v]} (now {i})")
        if not visited[i]:
            # 재귀함수 호출 -> 스택에 push
            dfs(graph, i, visited, j)
            # 재귀함수 return -> 스택에서 pop
            print(f"{j%10}[**dfs {i} out**] ".rjust(j*2))

# 각 노드가 연결된 정보를 표현(2차원 리스트)
# graph = [
#          [], 
#          [2, 3, 8], # 1
#          [1, 7],    # 2
#          [1, 4, 5], # 3
#          [3, 5],    # 4
#          [3, 4],    # 5
#          [7],       # 6
#          [2, 6, 8], # 7
#          [1, 7]     # 8
#         ]    

graph = [[], [2, 3, 4], [1], [1, 5, 6], [1, 7], [3, 8], [3], [4], [5]]
# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9
# 정의된 DFS 함수 호출
dfs(graph, 1, visited, 10)
print("real dfs out")