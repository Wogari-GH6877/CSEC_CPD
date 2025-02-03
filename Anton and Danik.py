num_of_game=int(input())

winner=list(input("").upper())

if winner.count('A')>winner.count('D'):
    print("Anton")


elif winner.count('A') < winner.count('D'):
    print("Danik")
else:
    print("Friendship")

 
