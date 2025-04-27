monto_total=float(input("Ingrese el monto total: "))
nivel_satisfaccion=int(input("Ingrese el nivel de satisfacción (1 para bueno, 2 para malo): "))
if nivel_satisfaccion == 1:
    propina=monto_total*0.15
    monto_pagar=monto_total+propina
    print("La propina es de $", propina, ", y el total a pagar es de: $", monto_pagar)
else:
    propina=monto_total*0.05
    monto_pagar=propina+monto_total
    print("La propina es de $", propina, ", y el total a pagar es de: $", monto_pagar)