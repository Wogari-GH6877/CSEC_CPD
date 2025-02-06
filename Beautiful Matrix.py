#beautiful matrix
for a in range(5):
    row=list(map(int,input().split()))
    if 1 in row:

       x,y=a,row.index(1)
       break
position=abs(x-2) + abs(y -2)
print(position)
