import sys

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

retA = list(map(int, fileIn.readline().split()))
retB = list(map(int, fileIn.readline().split()))

widthA, heightA = abs(retA[2] - retA[0]), abs(retA[3] - retA[1])
widthB, heightB = abs(retB[2] - retB[0]), abs(retB[3] - retB[1])

if (retA[0] < 0) or (retB[0] < 0) or (retA[0] > retA[2]) or (retB[0] > retB[2]) or (retA[2] < 0) or (retB[2] < 0):
    fileOut.write('Erro: Xa ou Xb passou do limite estabelecido\n')
elif (retA[1] < 0) or (retB[1] < 0) or (retA[1] > retA[3]) or (retB[1] > retB[3]) or (retA[3] < 0) or (retB[3] < 0):
    fileOut.write('Erro: Ya ou Yb passou do limite estabelecido\n')
elif (retA[0] >= 1000000) or (retA[2] >= 1000000) or (retB[0] >= 1000000) or (retB[2] >= 1000000):
    fileOut.write('Erro: Xa ou Xb passou do limite estabelecido\n')
elif (retA[1] >= 1000000) or (retA[3] >= 1000000) or (retB[1] >= 1000000) or (retB[3] >= 1000000):
    fileOut.write('Erro: Ya ou Yb passou do limite estabelecido\n')
else:
    if ((retA[0] + widthA) > retB[0]) and (retA[0] < (retB[0] + widthB)):
        if ((retA[1] + heightA) > retB[1]) and (retA[1] < (retB[1] + heightB)):
            fileOut.write('1\n')
        else:
            fileOut.write('0\n')
    else:
        fileOut.write('0\n')
    
fileIn.close()
fileOut.close()