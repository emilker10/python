# Задание

---

Рассмотрим два HTML-документа **A** и **B**.
Из **A** можно перейти в **B** за один переход, если в **A** есть ссылка на **B**, т. е. внутри **A** есть тег **\<a href="B"\>**, возможно с дополнительными параметрами внутри тега.
Из **A** можно перейти в **B** за два перехода если существует такой документ **C**, что из **A** в C** можно перейти за один переход и из **C** в **B** можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов **A** и **B**.
Выведите **Yes**, если из **A** в **B** можно перейти за два перехода, иначе выведите **No**.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

---

**Sample Input 1:**</br>
https://stepik.org/media/attachments/lesson/24472/sample0.html</br>
https://stepik.org/media/attachments/lesson/24472/sample2.html</br>

---

**Sample Output 1:**</br>
Yes</br></br></br>

---

**Sample Input 2:**</br>
https://stepik.org/media/attachments/lesson/24472/sample0.html
</br>
https://stepik.org/media/attachments/lesson/24472/sample1.html
</br>

---

**Sample Output 2:**</br>
No</br></br></br>

---

**Sample Input 3:**</br>
https://stepik.org/media/attachments/lesson/24472/sample1.html
</br>
https://stepik.org/media/attachments/lesson/24472/sample2.html
</br>

---

**Sample Output 3:**</br>
Yes</br></br></br>
