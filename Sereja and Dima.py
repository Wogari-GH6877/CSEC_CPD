num=int(input())
person_1=0
person_2=0
cards=list(map(int,input().split()))
turn = True

left, right = 0, num - 1
while left <= right:
    if cards[left] > cards[right]:
        chosen_card = cards[left]
        left += 1
    else:
        chosen_card = cards[right]
        right -= 1

    if turn:
        person_1 += chosen_card
    else:
        person_2 += chosen_card

    turn = not turn

print(person_1, person_2)
