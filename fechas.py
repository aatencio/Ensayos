# MANUAL DE LA LIBRERIA DATETIME
from datetime import datetime as date
from datetime import timedelta as delta
from datetime import time


#guardar en la variable fecha y hora
fecha_actual = date.now()
print(fecha_actual)

#crear una variable con el formato de time
establecer_hora = time(21, 16, 00) #(hora, minutos, segundos)
print(establecer_hora)

# crea una variable con un tiempo
# timedelta(days=999999999, hours=23, minutes=59,
# seconds=59, microseconds=999999)
duracion = delta(weeks=0, days=0, hours=0, minutes=1, seconds=0)
nueva_fecha = fecha_actual + duracion
nuevo_dia = nueva_fecha.day
nueva_hora = nueva_fecha.hour
nuevo_minuto = nueva_fecha.minute
print(nuevo_dia, nueva_hora, nuevo_minuto)

while True:
	if fecha_actual.hour == nueva_hora and fecha_actual.day == nuevo_dia and fecha_actual.minute == nuevo_minuto:
		print("Dentro del tiempo")
		fecha_actual = fecha_actual + duracion
