#edges of graph
ip = [[0,4] ,[0,1] ,[1,4] ,[1,2] ,[1,3] ,[4,3] ,[4,5] ,[2,5] ,[3,5]]
#no of nodes(0 to 5)
n=6

am = []
for i in range(n):
  temp = []
  for j in range(n):
    temp.append(0)
  am.append(temp)
  
  
for u, v in ip:
  am[u][v]=1
  am[v][u]=1
  
for i in am:
  print(i)
  
 
