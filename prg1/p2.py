p1=0
p2=0
with open("input2.txt") as f:
    for line in f:
        d1 = []
        d2 = []
        for i,c in enumerate(line):
            if c.isdigit():
                d1.append(c)
                d2.append(c)
            for d,val in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
                if line[i:].startswith(val):
                    d2.append(str(d+1))
        p1 += int(d1[0]+d1[-1])
        p2 += int(d2[0]+d2[-1]) 
    print(f"Considering only digits : {p1}")
    print(f'Considering digits as well as alphabetical numbers : {p2}')