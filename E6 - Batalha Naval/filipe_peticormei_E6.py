import sys

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

tab = []
points = []
count = 0

size_tab = list(map(int, fileIn.readline().split()))
if size_tab[0] >= 1 and size_tab[0] <= 100:
    if size_tab[1] <= 100:
        for i in range(size_tab[0]):
            m = list(map(str, fileIn.readline()))
            if '\n' in m:
                m.remove('\n')
            tab.append(m)
        j = int(fileIn.readline())
        for i in range(j):
            points.append(list(map(int, fileIn.readline().split())))
        for p in points:
            if tab[p[0]-1][p[1]-1] == '#':
                tab[p[0]-1][p[1]-1] = 'X'
        for i in range(size_tab[0]):
            for j in range(size_tab[1]):
                if tab[i][j] == 'X':
                    count +=1
        fileOut.write(str(count)+'\n')
    else:
        fileOut.write('O numero de M nao respeitou a restricao')
else:
    fileOut.write('O numero de N nao respeitou a restricao')

fileIn.close()
fileOut.close()