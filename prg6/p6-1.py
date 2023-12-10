import re

def possible_outcome(tr , dr):
    l = []
    for k in range(0,tr+1):
        if (k*(tr-k)) > dr:
            l.append(k*(tr-k))
    return len(l)

sm = 1
df = ['53     83     72     88',
    '333   1635   1289   1532']
t = re.findall("\d+",df[0])
d = re.findall("\d+",df[1])
for i in list(zip(t,d)):
    sm *= possible_outcome(int(i[0]),int(i[1]))
print(sm)