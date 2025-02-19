# Задание с leetcode.com
## 165. Compare Version Numbers

---

Given two **version strings**, *version1* and *version2*, compare them. A version string consists of **revisions** separated by dots *'.'*. The **value of the revision** is its **integer conversion** ignoring leading zeros.

To compare version strings, compare their revision values in **left-to-right order**. If one of the version strings has fewer revisions, treat the missing revision values as *0*.

Return the following:
- If *version1 < version2*, return -1.
- If *version1 > version2*, return 1.
- Otherwise, return 0

---

***Example 1:***</br>
**Input:** version1 = "1.2", version2 = "1.10"</br>
**Output:** -1</br>
**Explanation:** version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.</br>

---

***Example 2:***</br>
**Input:** version1 = "1.01", version2 = "1.001"</br>
**Output:** 0</br>
**Explanation:** Ignoring leading zeroes, both "01" and "001" represent the same integer "1".</br>

---

***Example 3:***</br>
**Input:** version1 = "1.0", version2 = "1.0.0.0"</br>
**Output:** 0</br>
**Explanation:** version1 has less revisions, which means every missing revision are treated as "0".</br>

---

***Constraints:***</br>
- *1 <= version1.length, version2.length <= 500*
- *version1* and *version2* only contain digits and *'.'* .
- *version1* and *version2* **are valid version numbers**.
- All the given revisions in *version1* and *version2* can be stored in a **32-bit integer**.

---

## Перевод

---

Даны две **строки с версиями** *version1* и *version2*, сравните их. Строка версий состоит из **ревизий**, разделенных точками *'.'*. **Значение ревизии** — это ее **целочисленное преобразование** без учета начальных нулей.

Чтобы сравнить строки версий, сравните их значения ревизий в порядке **слева направо**. Если одна из строк версий имеет меньше ревизий, обработайте отсутствующие значения ревизий как *0*.

Верните следующее:
- Если version1 < version2, вернуть -1.
- Если version1 > version2, вернуть 1.
- В противном случае верните 0.