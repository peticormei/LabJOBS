import sys

def bubble_sort_mod(alist):
    for num in range(len(alist)-1, 0, -1):
        for i in range(num):
            if alist[i][1] < alist[i+1][1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist
    
def bubble_sort(alist):
    for num in range(len(alist)-1, 0, -1):
        for i in range(num):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

info = list(map(int, fileIn.readline().split()))
list_students = []
times = []
cont = 0

if info[1] <= info[0]:
    if info[0] >= 2 and info[0] <= 10000:
        if info[1] >= 2 and info[1] <= 1000:
            for line in fileIn:
                line = line.split()
                line[1] = int(line[1])
                list_students.append(line)
            list_students = bubble_sort_mod(list_students)
            for i in range(info[1]):
                times.append([])
            for s in list_students:
                if cont == len(times):
                    cont = 0
                times[cont].append(s[0])
                cont += 1
            for t in range(len(times)):
                fileOut.write('Time %s\n' % (t + 1))
                times[t] = bubble_sort(times[t])
                for s in times[t]:
                    fileOut.write(s + '\n')
                fileOut.write('\n')

fileIn.close()
fileOut.close()