import os
import timeit
f = open("test.txt", "w")
while (os.path.getsize('test.txt')/(1024*1024)) < 50:
    f.write('12345678901234567890')
k = """
s = 0
with open('test.txt', "r") as file:
    for i in file.readlines:
        if i.strip().isdigit()
            s+= int(i)
"""
print(timeit.timeit(s, number = 1))
k = """
s = 0
with open('test.txt', "r") as file:
    for line in file:
        if line.strip()is.digit():
            s+= int(line.rstrip())
"""
print(timeit.timeit(s, number = 1))
