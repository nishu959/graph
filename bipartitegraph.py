""""
# 2 METHODS
def dfs(graph, node,visited,color, c):
  visited.append(node)
  color[node]=c
  for child in graph[node]:
    if child not in visited:
      temp = dfs(graph, child, visited, color,c^1)
      if temp == False:
        return False
    if color[child]==color[node]:
      return False
  return True
  
ip = [[1,2],[2,5] ,[3,4], [4,5], [2,4]]
n=6

graph= {}
color = {}

for i in range(1,n):
  graph[i] = []
  color[i] = None
  
  

for u, v in ip:
  graph[u].append(v)
  graph[v].append(u)
 
print(dfs(graph, 1,[],color,0))
"""
def dfs(graph, Node,color, c):
  for child  in graph[Node]:
    if color[child] is None:
      color[child]=c^1
      dfs(graph, child,color, c^1)
   
ip = [[1,2] ,[2,3] ,[2,4] ,[4,5] ,[1,5] ,[3,5],[1,4]]
n=6

graph= {}
color = {}

for i in range(1,n+1):
  graph[i] = []
  color[i] = None
  
  
color[1] =0

for u, v in ip:
  graph[u].append(v)
  graph[v].append(u)
 
 
dfs(graph, 1,color, 0)


s = True
for u, v in ip:
  if color[u]==color[v]:
    s = False
    break
  
print(s)
   