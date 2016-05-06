import sys

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

n = int(fileIn.readline())
l = list(map(int, fileIn.readline().split()))
t = 0

if n >= 2 and n <= 1000:
    for i in range(1, n +1):
        t += i
    fileOut.write(str(t - sum(l)))
else:
    fileOut.write('Erro: o numero N passou do limite estabelecido')

fileIn.close()
fileOut.close()