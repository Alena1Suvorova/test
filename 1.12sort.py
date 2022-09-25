h=str(input())
if h=='треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    print(S)
elif h=='прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
    print(S)
elif h=='круг':
    r = float(input())
    S = 3.14*(r**2)
    print(S)
else:
    print()
#сравнение чисел
a=int(input())
b=int(input())
c=int(input())
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
elif c>a and c>b:
    print(c)
if a <= b and a <= c:
        print(a)
elif b <= a and b <= c:
        print(b)
elif c <= a and c <= b:
        print(c)
if (b>=a and b<=c) or (b>=c and b<=a):
    print(b)
elif (a<=b and a>=c) or (a<=c and a>=b):
    print(a)
elif (c>=a and c<=b) or (c>=b and c<=a):
    print(c)
    # sklonenie
    a = int(input())
    if (a == 1 or a % 10 == 1) and a % 100 != 11:
        print(a, 'программист')
    elif (a in (2, 3, 4) or a % 10 in (2, 3, 4)) and a % 100 not in (12, 13, 14):
        print(a, 'программиста')
    else:
        print(a, 'программистов')
        # счастливый билет
        a = str(input())
        b = int(a[0]) + int(a[1]) + int(a[2])
        c = int(a[3]) + int(a[4]) + int(a[5])
        if b == c:
            print('Счастливый')
        else:
            print('Обычный')



