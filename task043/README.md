# Задание с leetcode.com
## 200. Number of Islands

---

Given an *m x n* 2D binary grid *grid* which represents a map of *'1'*s (land) and *'0'*s (water), return *the number of islands*.

An **island** is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

---

***Example 1:***</br>
**Input:** grid = [</br>
  &emsp;["1","1","1","1","0"],</br>
  &emsp;["1","1","0","1","0"],</br>
  &emsp;["1","1","0","0","0"],</br>
  &emsp;["0","0","0","0","0"]</br>
]</br>
**Output:** 1</br>

---

***Example 2:***</br>
**Input:** grid = [</br>
  &emsp;["1","1","0","0","0"],</br>
  &emsp;["1","1","0","0","0"],</br>
  &emsp;["0","0","1","0","0"],</br>
  &emsp;["0","0","0","1","1"]</br>
]</br>
**Output:** 3</br>

---

***Constraints:***</br>
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'

---

## Перевод

---

Дана двумерная двоичная сетка *grid* размером *m x n*, представляющая карту *'1'* (суша) и *'0'* (вода), вернуть *количество островов*.

Остров окружен водой и образован путем соединения соседних земель по горизонтали или вертикали. Вы можете предположить, что все четыре края сетки окружены водой