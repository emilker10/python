def update_dictionary(d, key, value):
    if key not in d:
        if 2*key not in d:
            d[2*key] = [value]
        else:
            d[2*key].append(value)
    else:
        d[key].append(value) 

d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-1]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-1, -2]}
update_dictionary(d, 4, -2)
print(d)                            # {2: [-1, -2], 8: [-2]}
update_dictionary(d, 8, -2)
print(d)                            # {2: [-1, -2], 8: [-2, -2]}