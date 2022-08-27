secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numero=int(input('Introduce el numero aca '))
while numero!=secret_number:
    print('"¡Ja, ja! ¡Estás atrapado en mi bucle!"')
    
    numero=int(input("Introduce de nuevo el numero aca "))
print("Has salido del ciclo")
