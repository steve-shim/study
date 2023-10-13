# 4 5
# 00110
# 00011
# 11111
# 00000

N,M = map(int,input().split())

graph=[]
for i in range(N):
    graph.append(list(map(int,input())))

def ice_dfs(x,y):
    # 종료조건 1
    if x<0 or x>=N or y<0 or y>=M:
        return False  

    # 성공조건  
    if graph[x][y]==0:
        graph[x][y]=1
        ice_dfs(x,y+1) # 우
        ice_dfs(x+1,y) # 하
        ice_dfs(x,y-1) # 좌
        ice_dfs(x-1,y) # 상
        return True
    # 종료조건 2
    return False    
    
result=0
for i in range(N):
    for j in range(M):
        if ice_dfs(i,j):
            result+=1
print(result)