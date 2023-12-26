# ch26_18.py
import imapclient
import pprint
imap = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imap.login('cshung1961@gmail.com', 'Your_Password')
imap.select_folder('INBOX', readonly=True)
UIDs = imap.search(['SINCE', '16-Nov-2023'])
raw_mail = imap.fetch(UIDs, ['BODY[]'])
pprint.pprint(raw_mail)








