f = open("p2data.txt",'r')
# only 12 red cubes, 13 green cubes, and 14 blue cubes
sm = 0
for line in f.read().splitlines():
    rl = []
    bl = []
    gl = []
    id_,line = line.split(':')
    for event in line.split(';'):
        # print(event)
        for balls in event.split(','):
            # print(balls)
            n,col = balls.split()
            # print(f"{n}->{col}")
            if col == 'blue':
                bl.append(int(n))
            if col == 'red':
                rl.append(int(n))
            if col == 'green':
                gl.append(int(n))
    sm += max(rl)* max(gl) * max(bl)
print(sm)