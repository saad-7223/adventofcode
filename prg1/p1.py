import re

ns = {
    v: str(i+1)
    for i,v in enumerate(['one','two','three','four','five','six','seven','eight','nine'])
}
print(ns)
sm = 0
with open ("input2.txt",'r') as f:
    for ln in f:
        ln = ln.strip()
        # nbs = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|\d))',ln)
        nbs = re.findall('\d',ln)  

        a = str(nbs[0])
        b = str(nbs[-1])

        sm += int(ns.get(a,a)+ns.get(b,b))
print(sm)