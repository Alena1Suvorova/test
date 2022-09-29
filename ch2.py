# 2.1

s = 0
a = 1

while a != 0:
    a = int(input())
    s += a

print(int(s))

#2.1 2
a = int(input())
b = int(input())
d = 1
while (d % a != 0) or (d % b != 0):
    d += 1

print(d)
# 2.2
i = 0
while i <= 100:
    i = int(input())
    if i < 10 or i > 100:
        continue
    print(i)
