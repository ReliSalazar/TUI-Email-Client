import smtplib
import imghdr
from email.message import EmailMessage
from email.headerregistry import Address

MY_ADDRESS = 'naitvenefy@gmail.com'
PASSWORD = 'mpaa koap bxsw thlr'

to_addr = Address(
    display_name='Reli Salazar',
    username='naitvenefy',
    domain='gmail.com')

msg = EmailMessage()
msg['Subject'] = 'Testing Testing 1.2.3'
msg['From'] = 'Reli'
msg['To'] = to_addr
msg.set_content("""Hola yo

Esto es un test para enviar correos utilizando SMTP.

Con mucho odio
Yo""")

with open('img_test.jpeg', 'rb') as fp:
    img_data = fp.read()

msg.add_attachment(img_data, maintype='image',
                    subtype=imghdr.what(None, img_data),
                    filename='img_test.jpeg')

with smtplib.SMTP('smtp.gmail.com', port=587) as s:
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    s.send_message(msg)

print('Message Sent Successfully!')

