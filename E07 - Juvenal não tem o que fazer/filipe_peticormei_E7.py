import sys

counter = 0
list_counter = []

def F(n):
    global counter
    if (n == 1):
        return 1
    else:
        if (n % 2 == 0):
            counter += 1
            return F(n/2)
        else:
            counter += 1
            return F(3*n+1)

def G(n):
    F(n)
    global list_counter
    list_counter.append(counter)

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

cases = int(fileIn.readline())
if cases >= 1 and cases <= 100:
    for i in range(cases):
        line = list(map(int, fileIn.readline().split()))
        if line == []:
            fileOut.write('Caso %d: Caso nao informado\n' % (i+1))
        else:
            if line[0] >= 1 and line[1] >= line[0] and line[1] <= 10**5:
                interval = [x for x in range(line[0], line[1]+1)]
                for n in interval:
                    counter += 1
                    G(n)
                    counter = 0
                v_max = max(list_counter)
                fileOut.write('Caso %d: %d\n' % (i+1, v_max))
                list_counter = []
            else:
                fileOut.write('Caso %d: Intervalo nao respeita a restricao\n' % (i+1))
else:
    fileOut.write('Valor de T nao respeita a restricao\n')

fileIn.close()
fileOut.close()