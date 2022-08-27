#CONCATENACIONES
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + fnam + " " + lnam + ".")


print()
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print()
leg_a = float(input("Inserta la longitud del primer cateto: "))
leg_b = float(input("Inserta la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))


print()
valor1=float(input("Digita el valor 1: "))
valor2=float(input("Digita el valor 2: "))

print("El resultado de la suma es: ", valor1+valor2) 
print("El resultado de la resta es: ", valor1-valor2) 
print("El resultado de la multiplicacion es: ", valor1*valor2) 
print("El resultado de la division es: ", valor1/valor2) 

print("\n¡Eso es todo, amigos!")
