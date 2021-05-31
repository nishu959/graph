def dfs(graph, Node, visited=set()):
  p =0
  visited.add(Node)
  for child in graph[Node]:
    if child not in visited:
      p = p+dfs(graph, child, visited)

  return p+1

#edges of graph
edges= [['A','B'],['A','D'],['A','C'],['B','E'],['D','E'],['F','H'],['F','G'],['I','J']]
#no of nodes(0 to 5)
Nodes = ['A', 'B', 'C', 'D', 'E', 'F','G' ,'H', 'I', 'J', 'K']

graph = {}
for i in Nodes:
  graph[i] = []
 

for (u, v) in edges:
  graph[u].append(v)
  graph[v].append(u)
 

ans = []
visited = set()
for i in Nodes:
  if i not in visited:
    ans.append(dfs(graph, i, visited))
  

print(ans)