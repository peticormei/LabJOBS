import sys

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def same_elem(n, l):
    flag = False
    for i in n:
        if i in l:
            flag = True
    return flag

fileIn = open(sys.argv[1], mode = 'r')
fileOut = open(sys.argv[2], mode = 'w')

cases = int(fileIn.readline())

if cases >= 1 and cases <= 1000:
    for i in range(cases):
        n_str = fileIn.readline().split()
        n_int = list(map(int, n_str))
        if n_int[0] >= 1 and n_int[0] <= 10000 or n_int[1] >= 1 and n_int[1] <= 1000:
            n1_factors = prime_factors(n_int[0])
            n2_factors = prime_factors(n_int[1])
            if same_elem(n1_factors, n2_factors) == True:
                fileOut.write('Caso %d: muito dificil\n' % (i + 1))
            else:
                for t in range(n_int[1]):
                    if (n_int[0] * t) % n_int[1] == 1:
                        fileOut.write('Caso ' + str(i + 1) + ': ' + str(t) + '\n')
                        break
        else:
            fileOut.write('Erro: Numeros passaram do limite')
else:
    fileOut.write('Erro: Numero de casos passou do limite')

fileIn.close()
fileOut.close()