#magnet
num_magnet=int(input())
magnets=[]
group_mangnet=1
for t in range(num_magnet):
     magnet=int(input())
     magnets.append(magnet)
for i in range(1,len(magnets)):
    if magnets[i]!=magnets[i-1]:
        group_mangnet+=1

print(group_mangnet)
