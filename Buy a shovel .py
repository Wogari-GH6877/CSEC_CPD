def sold_shovel(k,r):
    for num in range(1, 11):
        price_of_shovel = num * k
        if price_of_shovel % 10 == 0 or price_of_shovel % 10 == r:
            return num


k,r=map(int,input().split())
result=sold_shovel(k,r)
print(result)
