team_number=int(input())
host=[]
guest=[]
total_game=[]
b=0
guest_color=0
for a in range(team_number):

    games=list(map(int,input().split()))
    total_game+=games

for i in range(team_number):
    host.append(total_game[b])
    guest.append(total_game[b+1])
    b+=2
for team in host:
    if team in guest:
        guest_color+=guest.count(team)
print(guest_color)
