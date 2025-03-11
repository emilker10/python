def permute(nums):
    #Вспомогательная функция для рекурсивного построения перестановок
    def backtrack(start):
        if start == len(nums):                          #если достигли конца списка, добавляем текущую перестановку в результат
            result.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  #меняем местами текущий элемент с элементом на позиции i
            backtrack(start + 1)                         #рекурсивно вызываем функцию для следующего элемента.
            nums[start], nums[i] = nums[i], nums[start]  #возвращаем элементы на свои места (откат изменений).

    result = []
    backtrack(0)                                         #начинаем построение перестановок с первого элемента.
    return result

nums = [1,2,3]
print(permute(nums))