def letter_rotation(names):

    current_positon="a"
    num_rotation=0
    for a in names:
        clockwise=abs(ord(a)-ord(current_positon))
        anticlokwise=26-clockwise
        num_rotation+=min(clockwise,anticlokwise)
        current_positon=a
    return num_rotation

names=input()
print(letter_rotation(names))

