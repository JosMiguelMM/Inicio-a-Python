'''for i in range(10):
    print("El valor de i es actualmente", i)
    '''
#empieza en 2 y termina un numero antes del 8
'''for i in range(2, 8):
    print("El valor de i es actualmente", i)
'''

#el tercer numero funciona como un incrementador, de cuanto avanza i por cada paso
'''for i in range(2, 8, 3):
    print("El valor de i es actualmente", i)
'''

#se importa libreria
'''import time

for i in range(1, 6):
    print(i, " Missisipi")
    time.sleep (5)
print("¡Listos o no, ahí voy!")
# Escribe una función de impresión con el mensaje final.
'''

# break-termina el ciclo y pasa a la siguiente liena  - ejemplo
#continue-pasa al siguiente paso del ciclo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
