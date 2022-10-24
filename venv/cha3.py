#3 функции
# 3.1.1
def fan(x):
    s = 0
    if x <= -2:
        s = 1 - ((x+2)**2)
    elif x > -2 and x<= 2:
        s = -x/2
    elif x > 2:
        s = ((x - 2) ** 2) + 1
    return s
# 3.1.2
lst = [1, 2, 3, 4, 5, 6]

def modify_list(l):
    for j in range(len(l)-1, -1, -1):
        if l[j] % 2 != 0:
            l.pop(j)
        else:
            l[j] = l[j]//2

modify_list(lst)

# словари
x = {2: [-1]}
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif key * 2 in d:
        d[key * 2].append(value)
    else:
        d[key * 2] = [value]

update_dictionary(x, 2, 9)
update_dictionary(x, 1, 5)
update_dictionary(x, 3, -3)
print(x)
# кол-во слов в строке
a = input().lower().split()
slovar = dict()

for sl in a:
    if sl not in slovar:
        slovar[sl] = 1
    else:
        slovar[sl] += 1
for key in slovar:
    print(key, slovar[key])

# Кеш Считайте, что функция f(x) уже определена выше. Определять её отдельно не требуется.
n = int(input())
slovar = dict()
for i in range(n):
    x = int(input())
    if x in slovar:
        print(slovar[x])
    else:
        a = f(x)
        slovar[x] = a
        print(slovar[x])
# файлы
def preob_strok(sdo):
    a = sdo + ' '
    num = ''
    b = sdo[0]
    c = ''
    for i, st in enumerate(a):
        if st.isnumeric() == False:
            if num != '':
                c += (b * int(num))
                b = st
                num = ''
        if st.isnumeric() == True:
            num += st
    return c

with open('test.txt') as inf:
    s = inf.readline()
    output = preob_strok(s)
    with open('otvet.txt', 'w') as f:
        f.write(output)
