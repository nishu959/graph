def dfs(graph, Node, ans, d, par):
  ans[Node] =d
  for child in graph[Node]:
    if child != par:
      dfs(graph, child, ans, ans[Node]+1,Node)
    
  return   
    



#edges of graph
ip= [['A','B'],['D', 'J' ], ['B','D'],['A','C'],['C','E'],['D','G'],['G','H'],['F','C'],['G' , 'I']]
#no of nodes(0 to 5)
#ip = [[1,2] ,[1,5] ,[2,3] ,[2,4] ,[2,5] ,[3,4] ,[4,5] ,[4,6] ,[3,6],[5,6]]
#no of nodes(0 to 5)
Nodes = ['A', 'B', 'C', 'D', 'E', 'F','G' ,'H', 'I','J' ]

ans = {}

graph= {}
for i in Nodes:
  graph[i] = []
  ans[i] = None
 


for u, v in ip:
  graph[u].append(v)
  graph[v].append(u)
 
 
dfs(graph, 'A' , ans, 0, -1)
print(ans)


def dfs(g, Node, ans, visited):
  visited.append(Node)
  for i in g[Node]:
    if i not in visited:
      ans[i] = ans[Node]+1
      dfs(g, i,ans, visited)
  return


ip= [['A','B'],['B','D'],['A','C'],['C','E'],['D','G'],['G','H'],['F','C'],['G' , 'I'], ['D', 'J' ]]

Nodes = ['A', 'B', 'C', 'D', 'E', 'F','G' ,'H', 'I', 'J' ]

g = {}

ans = {}
for i in Nodes:
  g[i] = []
  ans[i]= None

for u, v in ip:
  g[u].append(v)
  g[v].append(u)

ans['A']=0

dfs(g, 'A', ans,[])
 

print(ans)