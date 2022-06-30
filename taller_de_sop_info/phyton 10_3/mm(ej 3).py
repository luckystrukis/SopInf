from contextlib import AbstractAsyncContextManager
from platform import java_ver
from re import A


set = {'l'}
set.remove('l')
for i in range(3):
    ing = input()
    set.add(ing)

print("set final: ", set)