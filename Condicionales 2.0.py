'''num1=int(input('Ingrese numero 1 '))
num2=int(input('Ingrese numero 2 '))

if(num1>num2):
    print('El numero mayor es el num1 y es ',num1)
else:
    print('El numero mayor es en num2 y es ',num2)
'''


'''num1=int(input('Ingrese numero 1 '))
num2=int(input('Ingrese numero 2 '))
num3=int(input('Ingrese numero 3 '))

if(num1>num2):
    print('El numero mayor es el num1 y es ',num1)
elif (num2>num3):
    print('El numero mayor es en num2 y es ',num2)
else:
    print('El numero mayor es el num3 y es ',num3)
'''
# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number
    
valor = max(number1, number2, number3) #o min para el numero mas pequeño

# Imprime el resultado.
print("El número más grande es:", valor)
