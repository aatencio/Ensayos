# Import smtplib for the actual sending function
import smtplib



# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of'
msg['From'] = "armory.home@gmail.com"
msg['To'] = "arnaldo.atencio@gmail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com',587)
s.send_message(msg)
s.quit()
