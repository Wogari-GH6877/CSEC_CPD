num=int(input())
colors=input()
count=0
for i in range(1,num):
    if colors[i]==colors[i-1]:
        count+=1
print(count)
