n=int(input())
x=[]
y=[]
for i in range(n):
  x1=int(input())
  x.append(x1)
x.sort()
for i in range(0,n-2):
  if(x[i]==x[i+1]):
    y.append(x[i])
print(y)
      

