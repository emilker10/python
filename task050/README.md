# Задание с leetcode.com
## 6. Zigzag Conversion

---

The string *"PAYPALISHIRING"* is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P&emsp;&emsp;&emsp;A&emsp;&emsp;&emsp;&emsp;H&emsp;&emsp;&emsp;&emsp;N</br>
A&emsp;P&emsp;&ensp;L&emsp;&emsp;S&emsp;&emsp;I&emsp;&emsp;I&emsp;&emsp;G</br>
Y&emsp;&emsp;&emsp;I&emsp;&emsp;&emsp;&emsp;&emsp;R</br>

And then read line by line: *"PAHNAPLSIIGYIR"*

Write the code that will take a string and make this conversion given a number of rows:

>string convert(string s, int numRows);

---

***Example 1:***</br>
**Input:** s = "PAYPALISHIRING", numRows = 3</br>
**Output:** "PAHNAPLSIIGYIR"</br>

---

***Example 2:***</br>
**Input:** s = "PAYPALISHIRING", numRows = 4</br>
**Output:** "PINALSIGYAHRPI"</br>
**Explanation:** </br>
P&emsp;&emsp;&emsp;&emsp;I&emsp;&emsp;&emsp;&emsp;N</br>
A&emsp;&emsp;L&emsp;S&emsp;&emsp;&emsp;I&emsp;G</br>
Y&emsp;A&emsp;&emsp;H&emsp;R</br>
P&emsp;&emsp;&emsp;&emsp;I</br>

---

***Example 3:***</br>
**Input:** s = "A", numRows = 1</br>
**Output:** "A"</br>

---

***Constraints:***</br>
- 1 <= s.length <= 1000
- *s* consists of English letters (lower-case and upper-case), ',' and '.'
- 1 <= numRows <= 1000

---

## Перевод

---

Строка *"PAYPALISHIRING"*записывается зигзагом в заданном количестве строк, как показано ниже: (возможно, вы захотите отобразить этот узор фиксированным шрифтом для лучшей читаемости)

P&emsp;&emsp;&emsp;A&emsp;&emsp;&emsp;&emsp;H&emsp;&emsp;&emsp;&emsp;N</br>
A&emsp;P&emsp;&ensp;L&emsp;&emsp;S&emsp;&emsp;I&emsp;&emsp;I&emsp;&emsp;G</br>
Y&emsp;&emsp;&emsp;I&emsp;&emsp;&emsp;&emsp;&emsp;R</br>

А затем прочитайте строку за строкой:*"PAHNAPLSIIGYIR"*

Напишите код, который будет принимать строку и выполнять это преобразование с учетом количества строк:

>string convert(string s, int numRows);