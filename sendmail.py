import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("armory.home@gmail.com", "caracas2009")

msg = "ALERTA DE MOVIMIENTO"
server.sendmail("armory.home@gmail.com", "arnaldo.atencio@gmail.com", msg)
server.quit()
