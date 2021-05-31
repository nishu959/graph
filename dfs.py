def dfs(graph, Node, visited=set()):
  print(Node)
  visited.add(Node)
  for child in graph[Node]:
    if child not in visited:
      dfs(graph, child, visited)



#edges of graph
ip = [[1,2] ,[1,5] ,[2,3] ,[2,4] ,[2,5] ,[3,4] ,[4,5] ,[4,6] ,[3,6],[5,6]]
#no of nodes(0 to 5)
n=6

graph= {}
for i in range(1,n+1):
  graph[i] = []
 

for u, v in ip:
  graph[u].append(v)
  graph[v].append(u)
 
 
dfs(graph, 1)