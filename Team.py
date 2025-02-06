num_participant=int(input())
sure_answer=0
for a in range(num_participant):
    person_1,person_2,person_3=map(int,input().split())

    if person_1 + person_2 + person_3>= 2:
     sure_answer+=1


print(sure_answer)
