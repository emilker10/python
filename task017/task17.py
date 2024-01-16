n, k = map(int, input().split())    #принимаем 2 числа через пробел
#Функция вычисления C(n, k).
def cf(n,k):
    if k>n:
        return 0
    elif k==0:
        return 1
    return cf(n-1,k)+cf(n-1,k-1)
print(cf(n,k))