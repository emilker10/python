# Задание с leetcode.com
## 198. House Robber

---

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array *nums* representing the amount of money of each house, return *the maximum amount of money you can rob tonight ***without alerting the police***.

---

***Example 1:***</br>
**Input:** nums = [1,2,3,1]</br>
**Output:** 4</br>
**Explanation:** ob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.</br>

---

***Example 2:***</br>
**Input:** nums = [2,7,9,3,1]</br>
**Output:** 12</br>
**Explanation:** Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.</br>

---

***Constraints:***</br>
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

---

## Перевод

---

Вы профессиональный грабитель, планирующий ограбить дома на улице. В каждом доме спрятана определенная сумма денег, единственным ограничением, которое останавливает вас от ограбления каждого из них, является то, что в соседних домах подключены системы безопасности, и **они автоматически свяжутся с полицией, если в одну и ту же ночь будут взломаны два соседних дома** .

Дан целочисленный массив *nums*, представляющий сумму денег в каждом доме, *верните максимальную сумму денег, которую вы можете ограбить сегодня вечером, **не привлекая внимания полиции***.