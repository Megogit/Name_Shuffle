import random
import time

print("""Lütfen isim listesini arada boşluk bırakarak giriniz.
İki isimli kişilerin isimları arasına boşluk koymayınız""")


name_list = input().split()

if len(name_list) < 2:
    print("listede en az 2 iki kişinin adı olmalıdır.")
    name_list = input().split()

while True:
    complist = []
    shuffled_list = name_list.copy()
    random.shuffle(shuffled_list)

    for x in range(0, len(name_list)):
        if name_list[x] != shuffled_list[x]:
            complist.append(shuffled_list[x])
        else:
            break

    if len(complist) == len(name_list):
        break


for x in range(0, len(name_list)):
    print(name_list[x]+"<------->" + complist[x])
