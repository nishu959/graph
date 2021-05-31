def dfs(graph, Node, ans, d):
  for i in graph[Node]:
    if ans[i] is None:
      ans[i] =d+1
      dfs(graph,i,ans,d+1)
   
  return   
    



#edges of graph
ip= [['A','B'],['B','D'],['A','C'],['C','E'],['D','G'],['G','H'],['F','C'],['G' , 'I']]
#no of nodes(0 to 5)
#ip = [[1,2] ,[1,5] ,[2,3] ,[2,4] ,[2,5] ,[3,4] ,[4,5] ,[4,6] ,[3,6],[5,6]]
#no of nodes(0 to 5)
Nodes = ['A', 'B', 'C', 'D', 'E', 'F','G' ,'H', 'I']
n=6
ans = {}

graph= {}
for i in Nodes:
  graph[i] = []
  ans[i] = None
 
ans['A' ] =0

for u, v in ip:
  graph[u].append(v)
  graph[v].append(u)
 
 
dfs(graph, 'A' , ans, 0)
print(ans)