edad=int(input("Ingrese su edad: "))
if edad>0:
    if edad<10:
        print("Usted es un niño")
    elif edad>=10 and edad<18:
        print("Usted es un adolescente")
    elif edad>=18 and edad<60:
        print("Usted es un adulto")
    else:
        print("Usted es un adulto mayor")
else: 
    print("Edad no válida")