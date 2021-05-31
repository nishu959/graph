#edges of graph
ip = [[0,4] ,[0,1] ,[1,4] ,[1,2] ,[1,3] ,[4,3] ,[4,5] ,[2,5] ,[3,5]]
#no of nodes(0 to 5)
n=6

mg = {}
for i in range(6):
  mg[i] = []
 

for u, v in ip:
  mg[u].append(v)
  mg[v].append(u)
 
 
for i in mg.items():
  print(i)