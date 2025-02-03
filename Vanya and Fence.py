def width(n,h):
    lists= list(map(int, input().split()))
    w=0

    for c in lists:
        if c>h:
           w+=2
        else:
            w+=1
    return w



n, h = map(int, input().split())
num=width(n,h)
print(num)
