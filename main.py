# Считываем строку и делим её на три части по пробелам  
vhod = input().split()  
  
# Берем каждый элемент по его индексу (номеру)  
a = int(vhod[0])  
znak = vhod[1]  
b = int(vhod[2])  
  
# Проверяем знак операции и выводим результат  
if znak == '+':  
    print(a + b)  
elif znak == '-':  
    print(a - b)  
elif znak == '*':  
    print(a * b)  
elif znak == '/':  
    if b != 0:  
        print(a / b)  
    else:  
        print("Деление на ноль!")

```
10:54
# Считываем размеры шоколадки и количество долек  
n = int(input("Введите n: "))  
m = int(input("Введите m: "))  
k = int(input("Введите k: "))  
  
# Проверяем условия  
if k < n * m and (k % n == 0 or k % m == 0):  
    print("YES")  
else:  
    print("NO")
10:54
x = int(input("Введите число X: "))  
  
# Список пар (числовое значение : римское обозначение)  
roman_rules = [  
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),  
    (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),  
    (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')  
]  
  
result = ""  
  
# Проходим по правилам и "собираем" римское число  
for value, letter in roman_rules:  
    while x >= value:  
        result += letter  
        x -= value  
  