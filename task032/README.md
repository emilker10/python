# Задание

---

Вашей программе на вход подаются три строки **s, a, b**, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки **a** в строку **s** на строку **b**.

Например, **s = "abab", a = "ab", b = "ba"**, тогда после выполнения одной операции строка **s** перейдет в строку **"baba"**, после выполнения двух и операций – в строку **"bbaa"**, и дальнейшие операции не будут изменять строку **s**.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если операций потребуется более 1000, выведите **Impossible**.

Выведите одно число – минимальное число операций, после применения которых в строке **s** не останется вхождений строки **a**, или **Impossible**, если операций потребуется более 1000.

---

**Sample Input 1:**</br>
ababa</br>
a</br>
b</br>

---

**Sample Output 1:**</br>
1</br></br></br>

---

**Sample Input 2:**</br>
ababa</br>
b</br>
a</br>

---

**Sample Output 2:**</br>
1</br></br></br>

---

**Sample Input 3:**</br>
ababa</br>
c</br>
c</br>

---

**Sample Output 3:**</br>
0</br></br></br>

---

**Sample Input 4:**</br>
ababac</br>
c</br>
c</br>

---

**Sample Output 4:**</br>
Impossible</br>