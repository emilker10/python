# Задание с leetcode.com
## 55. Jump Game

---

You are given an integer array *nums*. You are initially positioned at the array's **first index**, and each element in the array represents your maximum jump length at that position.

Return *true if you can reach the last index, or false otherwise*.

---

***Example 1:***</br>
**Input:** nums = [2,3,1,1,4]</br>
**Output:** true</br>
**Explanation:** Jump 1 step from index 0 to 1, then 3 steps to the last index.</br>

---

***Example 2:***</br>
**Input:** nums = [3,2,1,0,4]</br>
**Output:** false</br>
**Explanation:** You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.</br>

---

***Constraints:***</br>
- 1 <= nums.length <= 10<sup>4</sup>
- 0 <= nums[i] <= 10<sup>5</sup>

---

## Перевод

---

Дан целочисленный массив *nums*. Изначально вы находитесь в **первом индексе** массива, и каждый элемент в массиве представляет вашу максимальную длину прыжка в этой позиции.

Верните *true, если вы можете достичь последнего индекса, или false в противном случае* 