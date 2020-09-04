import email
from imaplib import IMAP4_SSL
from pprint import pprint

USER = 'naitvenefy@gmail.com'
PASSWORD = 'mpaa koap bxsw thlr'

server = IMAP4_SSL('imap.gmail.com')
server.login(USER, PASSWORD)

rv, output = server.select('INBOX')
rv, output = server.search(None, 'UNSEEN')
id_list = output[0].split()

email_data = []
for e_id in id_list[::-1][:10]:
    rv, output = server.fetch(e_id, '(BODY.PEEK[HEADER])')
    msg = email.message_from_bytes(output[0][1])
    hdr = {}
    hdr['to'] = email.header.decode_header(msg['to'])[0][0]
    hdr['from'] = email.header.decode_header(msg['from'])[0][0]
    hdr['date'] = email.header.decode_header(msg['date'])[0][0]
    hdr['subject'] = email.header.decode_header(msg['subject'])[0][0]
    email_data.append(hdr)
    pprint(hdr)

server.close()
server.logout()

