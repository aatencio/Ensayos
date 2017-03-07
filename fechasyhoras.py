# MANUAL DE LA LIBRERIA DATETIME
from datetime import datetime as date
from datetime import timedelta as delta
from datetime import time

# Formatos de tiempo
formatoFecha = "%d-%m-%Y"
formatoHora = "%H:%M:%S"
miFormato = "%d-%m-%Y %H:%M:%S"

# variables de tiempo
periodoDias = delta(days = 2)
periodoMinutos = delta(minutes = 7)



# ---------------------------------------------------------
def captura_horario():
    ahora = date.now()
    return(ahora)
# ---------------------------------------------------------
fechaActual = captura_horario()
print("Inicio del sistema " + fechaActual.strftime("%b %d %Y %H:%M:%S %p"))

fechaInicial = date.strptime("01-03-2017", formatoFecha)
fechaFinal = date.strptime("06-03-2017", formatoFecha)

TIME_ON = date.strptime("03-03-2017 21:45:00", miFormato)
print(TIME_ON)

#TIME_OFF = date.strptime("06-03-2017 21:45:00", miFormato)

TIME_OFF = TIME_ON + periodoMinutos
print(TIME_OFF)


if TIME_ON < fechaActual:
    print("La fecha de encendido es menor")






#NOTA: queda pendiente el error de manejo de horas
# el manejo de fechas quedo OK
