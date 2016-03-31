l=[1,2,3]

for i in range(1,-1,-1):
    if i == 0:
        print(l)
    else:
        print(l[:-(i)])