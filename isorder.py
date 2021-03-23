n = int(input())
list1 = input().split(" ")
orden = True
for x in range(n - 1):
    if int(list1[x]) <= int(list1[x + 1]):
        continue
    else:
        orden = False
if orden == True:
    print("Ordenado")
else:
    print("Desordenado")
