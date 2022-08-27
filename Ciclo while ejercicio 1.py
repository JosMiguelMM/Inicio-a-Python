blocks = int(input("Ingresa el número de bloques: "))
height=0
base=0
usados=0
while blocks!=0 :
    usados+=base
    if (usados>blocks):
        break
    
    base+=1
    blocks-usados
    height+=1
    
print("La altura de la pirámide:", height)
