import sys

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

retA = list(map(int, fileIn.readline().split()))
retB = list(map(int, fileIn.readline().split()))

widthA, heightA = abs(retA[2] - retA[0]), abs(retA[3] - retA[1])
widthB, heightB = abs(retB[2] - retB[0]), abs(retB[3] - retB[1])

if ((retA[0] + widthA) > retB[0]) and (retA[0] < (retB[0] + widthB)):
    if ((retA[1] + heightA) > retB[1]) and (retA[1] < (retB[1] + heightB)):
        fileOut.write('1\n')
    else:
        fileOut.write('0\n')
else:
    fileOut.write('0\n')
    
fileIn.close()
fileOut.close()