# Задание с leetcode.com
## 45. Jump Game II

---

You are given a **0-indexed** array of integers *nums* of length *n*. You are initially positioned at *nums[0]*.

Each element *nums[i]* represents the maximum length of a forward jump from index *i*. In other words, if you are at *nums[i]*, you can jump to any *nums[i + j]* where:

- 0 <= j <= nums[i] and
- i + j < n
  
Return *the minimum number of jumps to reach nums[n - 1]*. The test cases are generated such that you can reach *nums[n - 1]*.

---

***Example 1:***</br>
**Input:** nums = [2,3,1,1,4]</br>
**Output:** 2</br>
**Explanation:** The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.</br>

---

***Example 2:***</br>
**Input:** nums = [2,3,0,1,4]</br>
**Output:** 2</br>

---

***Constraints:***</br>
- 1 <= nums.length <= 10<sup>4</sup>
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach *nums[n - 1]*

---

## Перевод

---

Вам дан **0-индексированный** массив целых чисел *nums* длины *n*. Изначально вы находитесь в позиции *nums[0]*.

Каждый элемент *nums[i]* представляет максимальную длину прыжка вперед от индекса *i*. Другими словами, если вы находитесь в *nums[i]*, вы можете перейти в любое *nums[i + j]* место, которое:

- 0 <= j <= nums[i] и
- i + j < n

Верните *минимальное количество прыжков для достижения nums[n - 1]*. Тестовые случаи генерируются таким образом, чтобы вы могли достичь *nums[n - 1]*.