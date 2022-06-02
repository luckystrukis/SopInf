
set = {''}
set.remove('')
for i in range(3):
    ing = input()
    set.add(ing)

abc = ''
bcd = ''
cde = ''
i = 0
for elem in set:
    i = i + 1
    if elem.find('a') == 0 and i == 1:
        abc = elem

    if elem.find('a') == 0 and i == 2:
        bcd = elem

    if elem.find('a') == 0 and i == 3:
        cde = elem
set.discard(abc)
set.discard(bcd)
set.discard(cde)
print("set final: ", set)