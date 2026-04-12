listanum= []
men=0
mai=0
for n in range (0, 5):
    listanum.append(int(input(f"Digite o {n+1} numero: ")))
    if n==0:
        mai=men=listanum[n]
    else: 
        if listanum[n] > mai:
            mai= listanum[n]
        if listanum[n] < men:
            men= listanum[n]
print(f"O maior número da lista foi {mai}")
print(f"O menor numero da lista foi {men}")




