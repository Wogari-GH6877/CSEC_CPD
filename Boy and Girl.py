#Boy and Girl
name=list(input())
name.sort()
result=[]
for names in name:
    if names not in result:
        result+=names
        total=len(result)
if total%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
