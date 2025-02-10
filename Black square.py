calories=list(map(int,input().split()))
second_input=input()
total_calories=0
for a in second_input:
    total_calories+=calories[int(a)-1]

print(total_calories)
