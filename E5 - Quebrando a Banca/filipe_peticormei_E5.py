import sys

def num_max(l):
    num = l[0]
    index = 0
    for i in range(len(l)):
        if l[i] > num:
            num = l[i]
            index = i
    return [num, index + 1]

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

while True:
    n_str_case = fileIn.readline().split()
    n_str_num = fileIn.readline()
    if n_str_case == [] or n_str_num == '':
        break
    n_int_case = list(map(int, n_str_case))
    if 1 <= n_int_case[1] and n_int_case[1] < n_int_case[0] and n_int_case[0] <= 10**5:
        n_int_num, list_num = int(n_str_num), []
        for i in range(n_int_case[0]):
            division = 10 ** ((n_int_case[0] - 1) - i)
            list_num.append(n_int_num // division)
            n_int_num %= division
        start = 0
        for z in range(((n_int_case[0] - n_int_case[1]) - 1), -1, -1):
            if z == 0:
                num_info = num_max(list_num[start:])
            else:
                num_info = num_max(list_num[start: -z])
            fileOut.write(str(num_info[0]))
            start = num_info[1]
        # list_balance = list_num
        # for i in range(n_int_case[1]):
        #     list_balance.remove(min(list_num))
        # for elem in list_balance:
        #     fileOut.write(str(elem))
        fileOut.write('\n')
    else:
        fileOut.write('Erro: Numeros passaram do limite\n')

fileIn.close()
fileOut.close()