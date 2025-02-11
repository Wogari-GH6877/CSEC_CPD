shoe_colors=list(map(int,input().split()))
different_color=set(shoe_colors)
num_colors_needed=4-len(different_color)
print(num_colors_needed)
