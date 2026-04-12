matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapares=0
scol=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}][{c+1}]: '))
        if matriz[l][c] % 2==0:
            somapares=somapares+matriz[l][c]
for l in range(0,3):
    scol+=matriz[l][2]
for c in range(0,3):
    if c==0:
        mai=matriz[1][c]
    elif matriz[1][c]> mai:
        mai=matriz[1][c]
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^4}]", end='')
    print()
print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {scol}')
print(f'A maior valor da segunda linha é {mai}')

