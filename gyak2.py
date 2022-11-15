"""
kerd = str(input("jo nap?\n y/n"))
if kerd == "y":
    print("csak volt mert most szeppen kipakolsz")

elif kerd == "n":
    print("kys")
else:
    print("cseles cigany vagy tee")
"""
##########################################
"""
szam = int(input("szam kene "))

if szam % 2 == 0:
    print("paros a szam")

else:
    print("paratlan a szam")
"""
##########################################
"""
import random

szam = random.randrange(0, 11)
tipp = int(input("tipszmikszujje "))

if tipp == szam:
    print("baszodj meg ramona")

elif tipp > szam:
    print("uristen very big")

else:
    print("shmmmol")
"""
##########################################
"""
for x in range(0, 11):
    if x % 2 == 0:
        print(x)
"""
##########################################
"""
a = range(0, 11)
a = reversed(a)

for x in a:
    print(x)
"""
##########################################
"""
a = range(0, 11)
a = reversed(a)

for x in a:
    if x % 2 != 0:
        print(x)
"""
##########################################
"""
szov = str(input("most dumajja "))
ism = int(input("hanyszo? "))

for X in range(ism):
    print(szov)
"""
##########################################
"""
num = int(input("parsos szam "))

while num % 2 != 00:
    num = int(input("parsos szam "))

else:
    print("jon a capa")
"""
##########################################

import random

list = []

for x in range(20):
    n = random.randint(1,12)
    list.append(n)

    if n % 3 == 0:
        print(n)