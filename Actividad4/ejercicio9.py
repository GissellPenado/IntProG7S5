#Encontrar el mayor de tres números
#• Ingresar el primer número
#• Ingresar el segundo número
#• Ingresar el tercer número
#• Si el primero es mayor o igual que el segundo, comparar el primero con el tercero
#• Si el primero es menor que el segundo, compara el segundo con el tercero
#• Si los tres son iguales, mostrar “Los números son iguales”
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))
if numero1==numero2==numero3:
    print("Los numeros son iguales")
elif numero1>=numero2:
    if numero1>numero3:
        print("El primer numero es el mayor")
    else:
        print("El tercer numero es el mayor")
elif numero1<=numero2:
    if numero2>numero3:
        print("El segundo numero es el mayor")
    else: 
        print("El tercer numero es el mayor")