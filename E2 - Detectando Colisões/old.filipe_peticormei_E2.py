import sys

entrada = open(sys.argv[1], mode = 'r')

retangulo0 = entrada.readline()
retangulo0 = retangulo0.split()
retangulo1 = entrada.readline()
retangulo1 = retangulo1.split()

entrada.close()

ax1,ay1 = float(retangulo0[0]),float(retangulo0[1])
ax2,ay2 = float(retangulo0[2]),float(retangulo0[3])

bx1,by1 = float(retangulo1[0]),float(retangulo1[1])
bx2,by2 = float(retangulo1[2]),float(retangulo1[3])

if ax1<bx1:
    if ax2>bx1:
        if ay1<by1:
            if ay2>=by1:
                colide="1"
            else:
                colide="0"
        else:
            if ay1<=by2:
                colide="1"
            else:
                colide="0"
    else:
        colide="0"
else:
    if ax1<=bx2:
        if ay1<by1:
            if ay2>=by1:
                colide="1"
            else:
                colide="0"
        else:
            if ay1<=by2:
                colide="1"
            else:
                colide="0"
    else:
        colide="0"

saida = open(sys.argv[2], mode = 'w')
saida.wirte(colide + '\n')