#Verificación de inicio de sesión
#Ingresar nombre de usuario y clave.
#Si el usuario es “admin” y la clave “1234admin”, permitir acceso.
#Si no, denegar.
usuario="admin"
clave="123admin"
usuario_ingresado=str(input("Ingrese el usuario: "))
clave_ingresada=str(input("Ingrese la clave: "))
if usuario_ingresado==usuario and clave_ingresada==clave:
    print("Acceso permitido")
else:
    print("Acceso denegado")