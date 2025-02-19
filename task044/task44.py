def compareVersion(version1: str, version2: str) -> int:
    i = j = 0                                       #индексы для обхода строк version1 и version2

    #Проходим по строкам, пока не достигнем конца одной из них
    while i < len(version1) or j < len(version2):
        v1 = v2 = 0                                 #переменные для хранения текущих чисел версий

        #Извлекаем число из version1 до точки
        while i < len(version1) and version1[i] != '.':
            v1 = v1 * 10 + int(version1[i])
            i += 1

        #Извлекаем число из version2 до точки
        while j < len(version2) and version2[j] != '.':
            v2 = v2 * 10 + int(version2[j])
            j += 1

        #Сравниваем текущие числа версий
        if v1 > v2:
            return 1
        elif v1 < v2:
            return -1

        #Переходим к следующему числу после точки
        i, j = i + 1, j + 1

    #Если все числа версий равны, версии равны
    return 0

version1 = "1.2"
version2 = "1.10"

print(compareVersion(version1, version2))
