def untreated_crime(n,crimes):
    officer=0
    untreated=0

    for event in crimes:
        if event==-1:
            if officer>0:
                officer-=1
            else:
                untreated+=1
        else:
            officer+=event
    return untreated
n=int(input())
crimes=map(int,input().split())
print(untreated_crime(n,crimes))
