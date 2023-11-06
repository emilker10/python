c = []          #инициализируем матрицу
#Заполняем матрицу, пока не введем "end"
while True:
    a = [i for i in input().split()]
    if a == ['end']:
        break
    c.append(a)
#Вычисляем длину каждой из сторон    
n, m = len(c), len(c[0])
#Считаем каждой элемент в матрице и выводим на печать
for i in range(n):
    for j in range(m):
        x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
        print(x, end=' ')
    print()