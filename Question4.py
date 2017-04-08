#Question4-

li = [12,24,35,24,88,120,155,88,120,155]

new_list = []

for element in li:
    if element not in new_list:
        new_list.append(element)

print new_list