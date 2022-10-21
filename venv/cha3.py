#3 функции
# 3.1.1
def fan(x):
    s = 0
    if x <= -2:
        s = 1 - ((x+2)**2)
    elif x > -2 and x<= 2:
        s =-x/2
    elif x > 2:
        s = ((x - 2) ** 2) + 1
    return s
# 3.1.2
lst = [1, 2, 3, 4, 5, 6]
def modify_list(l):
    for j in range(len(l)-1,-1,-1):
        if l[j]%2 != 0:
           l.pop(j)
        else:
            l[j]=l[j]//2
modify_list(lst)