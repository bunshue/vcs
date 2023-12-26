# ch26_23.py
import imapclient

imap = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imap.login('cshung1961@gmail.com', 'Your_Password')
imap.select_folder('INBOX', readonly=False)
UIDs = imap.search(['SINCE', '16-Nov-2023', 'BODY', 'Apple'])
print(f"刪除前 : {UIDs}")
imap.delete_messages(UIDs)
print(f"執行delete_messages後 : {UIDs}")










