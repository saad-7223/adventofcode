import re

f = open("p44data.txt",'r')
n = len(f.readlines())
d = {}
for line in f.read().splitlines():
    k = line.split(':')
    l = k[1].split('|')
    # WINNING NUMBERS
    w = re.findall("\d+",l[0].strip())
    # USER NUMBERS
    n = re.findall("\d+",l[1].strip())
    num = set(w).intersection(n)
    val = (len(num)) if len(num) >= 1 else 0
    print(val)
