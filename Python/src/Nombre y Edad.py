# from colorama import init, Fore
# init()
# print(Fore.BLUE + "Hola JL")

# Ingreso de nombre.
nombre = input("¿Cuál es tu nombre? ")
print("Hola " + nombre)

# Ingreso de edad
edad = int(input("¿Qué edad tienes? "))

# Evalúa mayoría de edad.
esMayorEdad = edad >= 18

if esMayorEdad:
    #    print(Fore.BLUE + "Eres Mayor de Edad.")
    # else:
    print("Eres Menor de Edad.")
