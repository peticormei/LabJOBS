import sys

entrada = open(sys.argv[1], mode = 'r')

lista_str = []
lista_temp = []
lista_int = []
lista_resultados = []
caso = 0

for linha in entrada:
    lista_str.append(linha.split())
    
for sublista in lista_str:
    for numero in sublista:
        lista_temp.append(int(numero))
    lista_int.append(lista_temp)
    lista_temp = []
    
entrada.close()
    
for i in range(len(lista_int)):
    if i == 0:
        t = lista_int[i][0]
    else:
        a = lista_int[i][0]
        c = lista_int[i][1]
        if t <= 1000 and a <= 10000 and c <= 1000:
            for i in range(c):
                if (a * i) % c == 1:
                    lista_resultados.append('Caso ' + str(caso) + ': ' + str(i) + '\n')
                    break
            else:
                lista_resultados.append('Caso ' + str(caso) + ': muito dificil\n')
    caso += 1
                    
saida = open(sys.argv[2], mode = 'w')

for textos in lista_resultados:
    saida.write(textos)
    
saida.close()
