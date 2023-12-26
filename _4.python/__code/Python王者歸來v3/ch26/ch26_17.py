# ch26_17.py
import imapclient

imap = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imap.login('cshung1961@gmail.com', 'Your_Password')
imap.select_folder('INBOX', readonly=True)
UIDs = imap.search(['SINCE', '16-Nov-2023'])
print(UIDs)




