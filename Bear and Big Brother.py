weight_limak,weight_bob=map(int,input().split())
year=0

while(True):
    if weight_bob >= weight_limak :
        weight_limak=weight_limak*3
        weight_bob=weight_bob*2
        year+=1
    elif weight_bob<=weight_limak:
        #year+=1
        print(year)
        break



 
