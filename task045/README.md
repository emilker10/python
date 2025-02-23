# Задание с leetcode.com
## 167. Two Sum II - Input Array Is Sorted

---

Given a **1-indexed** array of integers *numbers* that is already ***sorted in non-decreasing order***, find two numbers such that they add up to a specific *target* number. Let these two numbers be *numbers[index<sub>1</sub>]* and *numbers[index<sub>2</sub>]* where *1 <= index<sub>1</sub> < index<sub>2</sub> <= numbers.length*.

Return *the indices of the two numbers, index<sub>1</sub> and index<sub>2</sub>, **added by one** as an integer array [index<sub>1</sub>, index<sub>2</sub>] of length 2.*

The tests are generated such that there is **exactly one solution**. You **may not **use the same element twice.

Your solution must use only constant extra space.

---

***Example 1:***</br>
**Input:** numbers = [2,7,11,15], target = 9</br>
**Output:** [1,2]</br>
**Explanation:** The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].</br>

---

***Example 2:***</br>
**Input:** numbers = [2,3,4], target = 6</br>
**Output:** [1,3]</br>
**Explanation:** The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].</br>

---

***Example 3:***</br>
**Input:** numbers = [-1,0], target = -1</br>
**Output:** [1,2]</br>
**Explanation:** The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].</br>

---

***Constraints:***</br>
- 2 <= numbers.length <= 3 * 10<sup>4</sup>
- -1000 <= numbers[i] <= 1000
- *numbers* is sorted in **non-decreasing order**
- -1000 <= target <= 1000
- The tests are generated such that there is **exactly one solution**.

---

## Перевод

---

Дан линейный массив целых чисел *numbers*, который уже ***отсортирован в неубывающем порядке***, найдите два числа, которые в сумме дают определенное число *target*. Пусть эти два числа будут *numbers[index<sub>1</sub>]* и *numbers[index<sub>2</sub>]*, где *1 <= index<sub>1</sub> < index<sub>2</sub> <= numbers.length*.

Верните *индексы двух чисел и  ***добавленные к единице***, в виде целочисленного массива [index<sub>1</sub>, index<sub>2</sub>] длины 2*.

Тесты генерируются таким образом, что существует **только одно решение**. **Не используйте** один и тот же элемент дважды.

Ваше решение должно использовать только постоянное дополнительное пространство.