num = int(input("Введите целое положительное число: "))
m = num % 10
x = 100
while num != (num % x):
    b = int(((round(num / x, 1)) * 10) % 10)
    if b > m:
        m = b
    x = x * 10
if m > int(((round(num / x, 1)) * 10) % 10):
    print ("Максимальная цифра в числе1: ", m)
else:
    print("Максимальная цифра в числе2: ", int((round(num / x, 1)) * 10 % 10))
