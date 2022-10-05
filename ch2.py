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

#2.3
a = int(input())
b = int(input())

s = 0
m = 0
for i in range(a, b+1):
    if i % 3 == 0:
        s += i
        m += 1
print(s/m)
2.4
s = input().upper()
G = (s.count('G') + s.count('C')) / len(s)
print(G * 100)

2.5
a = input()+' '
i = 0
s = 0

for i in range(len(a)-1):
    if a[i] == a[i+1]:
        i += 1
        s += 1
    else:
        a[i] != a[i+1]
        k = str(s+1)
        print(a[i]+k, end="")
        s = 0
# 2.5 списки
a = [int(i) for i in input().split()]
print(sum(a))

# 2.5.2
a = [(int(i)) for i in input().split()]
if len(a)-1 == 0:
    print(a[0])
else:
    for i in range(len(a)-1):
        s = a[i-1]+a[i+1]
        i += 1
        print(s, '', end='')
    print(a[0]+a[i-1])
# 2.5.3 убрать повторы из списка
a, j = [(int(i)) for i in input().split()], []
b = a.sort()
c = ''
for i in range(len(a)):
    if c != a[i]:
        c = a[i]
        i += 1
    elif a[i] not in j:
        j.append(a[i])
        print(a[i], '', end='')