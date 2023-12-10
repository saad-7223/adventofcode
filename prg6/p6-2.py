import re

def possible_outcome(tr , dr):
    l = []
    for k in range(0,tr):
        if (k*(tr-k)) > dr:
            l.append(k*(tr-k))
    print(len(l))
    
sm = 1
df = ['53     83     72     88',
    '333   1635   1289   1532']
# df = ['7  15   30','9  40  200']
t = int(df[0].replace(' ',''))
d = int(df[1].replace(' ',''))
possible_outcome(t,d)
