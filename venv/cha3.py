# 3.1
def fan(x):
    s = 0
    if x <= -2:
        s = 1 - ((x+2)**2)
    elif x > -2 and x<= 2:
        s =-x/2
    elif x > 2:
        s = ((x - 2) ** 2) + 1
    return s