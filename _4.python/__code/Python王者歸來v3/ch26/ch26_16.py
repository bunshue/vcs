# ch26_16.py
import imapclient
import pprint
imap = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imap.login('cshung1961@gmail.com', 'Your_Password')
pprint.pprint(imap.list_folders())


