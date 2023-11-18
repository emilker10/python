def modify_list(l):
    new_l = []
    for i in range(len(l)):
        if l[i]%2==0:
            new_l.append(l[i]//2)
    l[:] = new_l

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]