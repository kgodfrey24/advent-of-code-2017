import math

def find_middle(min, max):
    return (min + max) / 2

x = 361527

root = math.sqrt(x)

print "root of x:",root

round_root = math.ceil(root)

if round_root % 2 == 0:
    round_root = round_root + 1

print "rounded root number:",round_root

width = round_root - 1

bottom_right = round_root ** 2
bottom_left = bottom_right - width
top_left = bottom_left - width
top_right = top_left - width

print "bottom_right:",bottom_right
print "bottom_left:",bottom_left
print "top_left:",top_left
print "top_right:",top_right

if x > bottom_left:
    middle = find_middle(bottom_left, bottom_right)
elif x > top_left:
    middle = find_middle(top_left, bottom_left)
elif x > top_right:
    middle = find_middle(top_right, top_left)
else:
    middle = find_middle(top_right - width, top_right)

steps_horizontal = abs(x - middle)
steps_vertical = width / 2

print steps_horizontal + steps_vertical
