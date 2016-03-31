import sys

count = 0
flag = True
flag_out = False
num = [1, 2, 3, 4, 5, 6, 7, 8]

horse_pos = [4,3]
table_hole = [[1, 3], [2, 3], [2, 5], [5, 4]]
mov_horse = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

n_int_case = int(fileIn.readline())
n_str_mov = fileIn.readline().split()
n_int_mov = list(map(int, n_str_mov))

if n_int_case >= 1 and n_int_case <= 100:
    for e in n_int_mov:
        if e not in num:
            flag = False 
    if flag == True:
        if n_int_case == len(n_int_mov):
            for i in n_int_mov:
                count += 1
                mov = mov_horse[i-1]
                horse_pos[0] += mov[0]
                horse_pos[1] += mov[1]
                if horse_pos[0] > 7 or horse_pos[1] > 7 or horse_pos[0] < 0 or horse_pos[1] < 0:
                    fileOut.write('Erro: Cavalo saiu do tabuleiro\n')
                    flag_out = True
                    break
                if horse_pos in table_hole:
                    break
            if flag_out == True:
                pass
            else:
                fileOut.write(str(count))
        else:
            fileOut.write('Erro: Numero de casos diferente do numero de movimentos\n')
    else:
        fileOut.write('Erro: Algum numero de movimento nao e aceito\n')
else:
    fileOut.write('Erro: Numeros de caso nao aceito\n')

fileIn.close()
fileOut.close()