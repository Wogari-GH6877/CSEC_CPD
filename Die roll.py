import math

person_1,person_2=map(int,input().split())
max_value=max(person_1,person_2)

favorable_outcome=6-max_value+1
max_out_come=6

gcd=math.gcd(favorable_outcome,max_out_come)
numerator=favorable_outcome//gcd
denominator=max_out_come//gcd

print(f"{numerator}/{denominator}")
