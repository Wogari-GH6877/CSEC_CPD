color=input()
instruction=input()

current_position=1
for a in instruction:
    if current_position <len(color) and color[current_position-1]==a:
        current_position+=1
print(current_position)
