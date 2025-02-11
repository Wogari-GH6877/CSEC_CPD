def bird_hunting(num_wire, birds, num_shot, shots):
    for x, y in shots:
        x -= 1

        if x > 0:
            birds[x - 1] += (y - 1)

        if x < num_wire - 1:
            birds[x + 1] += (birds[x] - y)
        birds[x] = 0

    for count in birds:
        print(count)


num_wire=int(input())
birds=list(map(int,input().split()))
num_shot=int(input())
shots = []
for _ in range(num_shot):
    x, y = map(int, input().split())
    shots.append((x, y))

bird_hunting(num_wire, birds, num_shot, shots)
