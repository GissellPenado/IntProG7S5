from datetime import datetime
fecha_ultimo_inicio=input("Ingrese la fecha de ultimo inicio (AAAA-MM-DD): ")
fecha_ultimo_inicio=datetime.strptime(fecha_ultimo_inicio, "%Y-%m-%d")
fecha_actual=datetime.now()
dias_transcurridos=(fecha_actual-fecha_ultimo_inicio).days
if dias_transcurridos>30:
    print("Cuenta inactiva")
else:
    print("Cuenta activa")