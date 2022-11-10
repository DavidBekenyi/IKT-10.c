"""
list = []

szam1 = int(input("Add meg az elso szamot"))
szam2 = int(input("Add meg az masodik szamot"))
szam3 = int(input("Add meg az harmadik szamot"))

list.append(szam1)
list.append(szam2)
list.append(szam3)

def kisebb():
    print(min(list))

kisebb()
"""
##########################################
"""
list = []

szam1 = int(input("Add meg az elso szamot"))
szam2 = int(input("Add meg az masodik szamot"))
szam3 = int(input("Add meg az harmadik szamot"))

list.append(szam1)
list.append(szam2)
list.append(szam3)

def nagyobb():
    print(max(list))

nagyobb()
"""
##########################################
"""
x = int(input("Dolgozat pontszama: "))

if x < 50:
    print("elegtelen")
    
elif 50 <= x <60 :
    print("elegsegges")

elif 60 <= x <70 :
    print("kozepes")

elif 70 <= x <85 :
    print("jo")

elif x>85 :
    print("jeles")
"""
##########################################
"""
szam = int(input("szam most"))

if szam % 3 == 0:
    print("a szam oszthato 3mal")

elif szam % 5 == 0:
    print("a szam oszthato 5tel")

else:
    print("a szam paros vagy 1 et irtal kys")
"""
##########################################
"""
list = []

szam1 = int(input("szam most "))
szam2 = int(input("megin szam "))
szam3 = int(input("igen "))

list.append(szam1)
list.append(szam2)
list.append(szam3)

nagyobb = max(list)
kisebb = min(list)

if nagyobb - kisebb == szam1:
    print(szam1, "+", kisebb, "=", nagyobb )

elif nagyobb - kisebb == szam2:
    print(szam2, "+", kisebb, "=", nagyobb )

elif nagyobb - kisebb == szam3:
    print(szam3, "+", kisebb, "=", nagyobb )

else:
    print("jo gagyi vagy")
"""
##########################################
"""
szam1 = int(input("Add meg az elso szamot"))
szam2 = int(input("Add meg az masodik szamot"))
szam3 = int(input("Add meg az harmadik szamot"))

if szam1 + szam2 == szam3:
    print(szam1, "+", szam2, "=", szam3)
elif szam2 + szam3 == szam1:
    print(szam2, "+", szam3, "=", szam1)
elif szam1 + szam3 == szam2:
    print(szam1, "+", szam3, "=", szam2)
else:
    print("gagyi")
"""
##########################################
"""
import abc

list = []

szo1 = str(input("szo "))
szo2 = str(input("szo "))

list.append(szo1)
list.append(szo2)

list.sort()

print(list)
"""
##########################################
"""
szam = int(input("szamot "))
x = range(3, szam)

for szam in x:
    if szam % 3 == 0:
        print(szam)
"""
##########################################
"""
list = []
hatar1 = int(input("szamot "))
hatar2 = int(input("szamot "))
x = range(hatar1, hatar2)

list.append(hatar1)
list.append(hatar2)

szam = max(list)

for szam in x:
    if szam % 2 == 0:
        print(szam)
"""
##########################################
"""
szam = int(input("aggyal szamot. de bazzeg ha kisseb lesz mint husz kette torom a fejed "))
szam = szam - 1
ujszam = szam * " "

print(ujszam, "start")
"""
