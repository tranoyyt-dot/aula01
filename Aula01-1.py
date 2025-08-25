n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
r = [n1 + n2, n1 - n2, n1 * n2, n1 / n2]
nr = ['Soma','Diferença','Produto','Quociente']
for c in range (0,4):
    print('\n',r[c],'=', nr[c])