import os

file = open('1.txt', 'r')
i = 1
for line in file:
    if "TTL" in line:
        list=line.split(' ', 3)
        print(list[1])
file.close()
