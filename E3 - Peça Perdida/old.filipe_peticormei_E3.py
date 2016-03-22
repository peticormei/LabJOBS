import sys

entrada = open(sys.argv[1], 'r')
saida = open(sys.argv[2], 'w')

caso = int(entrada.readline())
lista_str = entrada.readline().split()
elementos = list(map(int,lista_str))

if caso >= 2 and caso <= 1000:
    elementos.sort()
    for i in range(caso - 1):
        if elementos[i] != i + 1:
            saida.write(str(i + 1)+'\n')
            break

entrada.close()
saida.close()