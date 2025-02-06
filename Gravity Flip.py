#Gravity Flip
num_column=int(input())

num_boxes=list(map(int,input().split()))
num_boxes.sort()
print(*num_boxes)
