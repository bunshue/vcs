using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;       //for NetworkCredential     NetworkCredential ：這個類別可用來提供密碼架構的驗證 (Authentication) 機制的認證。
using System.Net.Mail;  //for MailMessage, SmtpClient
//using System.Web.Mail;  //據說不推薦使用了
using System.Net.Mime;  //for MediaTypeNames

/*

要寄Gmail信首先要登入Gmail，
然後到 https://www.google.com/settings/security/lesssecureapps
低安全性應用程式 → 開啟較低的應用程式存取權限
選擇開啟，否則會無法正常寄信

01.前置動作:(把Gmail的安全性調低，否則會發生 5.5.1 Authentication Required. 的錯誤!)
修改網址 https://www.google.com/settings/security/lesssecureapps
進入頁面之後選擇 安全性較低的應用程式存取權限 [啟用] 

*/

/*
要寄Gmail信首先要登入Gmail，
然後到 https://www.google.com/settings/security/lesssecureapps
低安全性應用程式 → 開啟較低的應用程式存取權限
選擇開啟，否則會無法正常寄信
*/

namespace vcs_SendMail
{
    public partial class Form1 : Form
    {
        //共用的郵件資訊
        string email_encoding = "utf-8";
        string email_addr_from = "bunshue@gmail.com";
        string email_addr_from_password = string.Empty;
        string email_addr_from_nicknane = "王大頭";    //寄件者顯示的名稱
        string email_addr_to = "david@insighteyes.com";
        string email_addr_to_nicknane = "尊敬的收件者";    //收件者顯示的名稱
        string email_addr_cc = "bunshue@gmail.com";
        MailPriority priority = MailPriority.Normal;        //設定電子郵件的優先順序

        string mail_subject = string.Empty; //郵件標題
        string mail_body = string.Empty;    //郵件內容
        string smtp_server = "smtp.gmail.com";  //POP3服務器的名稱
        int smtp_server_port = 25;              //指定 SMTP 交易連接埠, 預設是25

        string attach_filename1 = @"C:\______test_files\picture1.jpg";
        string attach_filename2 = @"C:\______test_files\__RW\_excel\2019~2021新竹日出日沒時刻表.xls";
        string attach_filename3 = @"C:\______test_files\__RW\_word\Step.doc";   //RTF檔案

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mail_body = richTextBox_mail.Text;
            show_item_location();

            string filename = "C:\\______test_files\\__RW\\_txt\\gmail_key.txt";
            if (File.Exists(filename) == false)
            {
                MessageBox.Show("Gmail_KEY 檔案不存在, 離開", "vcs_SendMail", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }

            //讀取檔案
            string kk = File.ReadAllText(filename, Encoding.Default);
            //richTextBox1.Text += "檔案內容 : " + kk + "\n";
            //richTextBox1.Text += "長度：" + kk.Length.ToString() + "\n";

            if (kk.Length == 15)
            {
                email_addr_from_password = kk;
            }
            else
            {
                email_addr_from_password = "xxxx";

                MessageBox.Show("Gmail_KEY 錯誤, 離開", "vcs_SendMail", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 55;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            button7.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 6);

            richTextBox1.Location = new Point(x_st + dx * 2 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void SendGmail(MailMessage mail)
        {
            //通知狀態 OnSuccess, OnFailure, Delay, None, Never
            mail.DeliveryNotificationOptions = DeliveryNotificationOptions.OnFailure | DeliveryNotificationOptions.OnSuccess;

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient(smtp_server, smtp_server_port);   //實例一個SmtpClient類
            //smtp.Host = smtp_server;
            //smtp.Port = smtp_server_port;
            smtp.Timeout = 9999;
            smtp.EnableSsl = true; //gmail預設開啟驗證, 指定 SmtpClient 使用安全套接字層 (SSL) 加密連接
            smtp.UseDefaultCredentials = false; //不使用默認憑證，注意此句必須放在smtp.Credentials() 的上面
            smtp.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password); //這裡要填正確的帳號跟密碼, 驗證寄件者
            //smtp.Credentials = CredentialCache.DefaultNetworkCredentials;   //不可, 需要驗證寄件者
            smtp.DeliveryMethod = SmtpDeliveryMethod.Network;   //通過網絡發送到SMTP服務器
            SendMail(smtp, mail);
            smtp.Dispose();
        }

        private void SendMail(SmtpClient smtp, MailMessage mail)
        {
            richTextBox1.Text += "透過gmail寄信 ST, 時間 : " + DateTime.Now.ToString() + "\n";
            Application.DoEvents();
            try
            {
                smtp.Send(mail);  //寄送郵件
                richTextBox1.Text += "信件已寄出, 時間 : " + DateTime.Now.ToString() + "\n";
            }
            //Handle Mail Exceptions
            catch (InvalidOperationException exInvalidOperation)            //沒有指定 SMTP Server
            {
                richTextBox1.Text += "信件寄送失敗1, 時間 : " + DateTime.Now.ToString() + "\t訊息 : " + exInvalidOperation.Message.ToString() + "\n";
                richTextBox1.Text += "原因: " + exInvalidOperation.ToString() + "\n";
            }
            catch (SmtpFailedRecipientException exSmtpFailedRecipient)      //指定錯誤的收件者
            {
                richTextBox1.Text += "信件寄送失敗2, 時間 : " + DateTime.Now.ToString() + "\t訊息 : " + exSmtpFailedRecipient.Message.ToString() + "\n";
                richTextBox1.Text += "原因: " + exSmtpFailedRecipient.ToString() + "\n";
            }
            catch (SmtpException exSmtp)                                    //找不到 SMTP 或 其他的例外錯誤
            {
                richTextBox1.Text += "信件寄送失敗3, 時間 : " + DateTime.Now.ToString() + "\t訊息 : " + exSmtp.Message.ToString() + "\n";
                richTextBox1.Text += "原因: " + exSmtp.ToString() + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "信件寄送失敗4, 時間 : " + DateTime.Now.ToString() + "\t訊息 : " + ex.Message.ToString() + "\n";
                richTextBox1.Text += "原因: " + ex.ToString() + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "透過gmail寄信 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            /*
            //MailAddress 的用法
            MailAddress from = new MailAddress(email_addr_from, email_addr_from_nicknane);
            MailAddress to = new MailAddress(email_addr_to, email_addr_to_nicknane);
            MailMessage mail = new MailMessage(from, to);
            */

            //MailMessage mail = new MailMessage(email_addr_from, email_addr_to, subject, "郵件內容(Body)");   //一次寫完
            MailMessage mail = new MailMessage();

            //mail.From = new MailAddress(email_addr_from); //寄件者, 不包含顯示名稱
            //mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane); //寄件者, 顯示名稱
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, Encoding.UTF8); //寄件者, 顯示名稱, 編碼

            //mail.To.Add(email_addr_to);   //收件者, 不包含顯示名稱
            mail.To.Add(new MailAddress(email_addr_to, email_addr_to_nicknane + "1"));  //收件者, 顯示名稱
            mail.To.Add(new MailAddress(email_addr_to, email_addr_to_nicknane + "2"));  //收件者, 顯示名稱
            mail.CC.Add(new MailAddress(email_addr_to, email_addr_to_nicknane + "副本")); //副本, 顯示名稱
            mail.Bcc.Add(new MailAddress(email_addr_to, email_addr_to_nicknane + "密件副本"));  //密件副本, 顯示名稱

            //對方回復郵件時默認的接收地址
            //mail.ReplyTo = new MailAddress(email_addr_from, "IMS-Sales", Encoding.GetEncoding(950));  ReplyTo已過時, 改用ReplyToList
            mail.ReplyToList.Add(new MailAddress("David@insighteyes.com", "receiver"));

            mail.Priority = priority;

            mail.Subject = mail_subject;    //郵件標題
            mail.SubjectEncoding = Encoding.UTF8;//郵件標題編碼

            //各種郵件內容的寫法
            //mail.Body = "莫聽穿林打葉聲，何妨吟嘯且徐行。竹杖芒鞋輕勝馬，誰怕？一蓑煙雨任平生。料峭春風吹酒醒，微冷，山頭斜照卻相迎。回首向來蕭瑟處，歸去，也無風雨也無晴。";
            //mail.Body = mail_body;  //郵件內容
            //mailBody(mail);
            //mail.Body = "<font color=\"red\">莫聽穿林打葉聲，何妨吟嘯且徐行</font>"; //郵件內容
            mail.Body = "<html><body><h1>牡丹亭</h1><br><img src=\"C:\\______test_files\\picture1.jpg\"></body></html>";
            mail.Body = "牡丹亭";

            mail.BodyEncoding = Encoding.UTF8;  //郵件內容編碼方式
            mail.IsBodyHtml = true; //是否是HTML郵件

            /*
            //附加檔案 寫法 1
            Attachment attachment = new Attachment(attach_filename1);
            mail.Attachments.Add(attachment);
            */

            //附加檔案 寫法 2
            Attachment attachment = new Attachment(attach_filename2, MediaTypeNames.Application.Octet);
            ContentDisposition disposition = attachment.ContentDisposition;
            disposition.CreationDate = File.GetCreationTime(attach_filename2);
            disposition.ModificationDate = File.GetLastWriteTime(attach_filename2);
            disposition.ReadDate = File.GetLastAccessTime(attach_filename2);
            mail.Attachments.Add(attachment);

            //附加檔案 寫法 3
            mail.Attachments.Add(new Attachment(attach_filename1));

            //附加檔案 寫法 4
            //附加一個RTF檔案
            mail.Attachments.Add(new Attachment(attach_filename3, System.Net.Mime.MediaTypeNames.Application.Rtf)); //添加附件，第二個參數表示附件的文件類型，可以不用指定

            //附加檔案 寫法 5
            /*
            foreach (var attachment in sender.Attachments)
            {
                mail.Attachments.Add(attachment);
            }
            */

            mail.Attachments.Add(new Attachment(attach_filename1));  //附件

            SendGmail(mail);

            mail.Dispose();
            this.Cursor = Cursors.Default;
        }

        public void mailBody(MailMessage mail)
        {
            string palinBody = "【XXXX】";
            AlternateView plainView = AlternateView.CreateAlternateViewFromString(palinBody, null, "text/plain");

            string htmlBody = "<p> 此為系統主動發送信函，請勿直接回覆此封信件。</p> ";
            htmlBody += "<p> <a id=happyyblog target=\"_blank\" href=\"https://www.insighteyes.com\" title=\"連線到群曜醫電\">連線到群曜醫電</a></p>";
            //htmlBody += "<img alt=\"\" hspace=0 src=\"cid:logo\" align=baseline border=0 >";
            htmlBody += "<img src=\"C:\\______test_files\\picture1.jpg\" width=\"305\" height=\"400\" align=\"center\" border=30 bgcolor=\"#00FF00\">";

            AlternateView htmlView = AlternateView.CreateAlternateViewFromString(htmlBody, null, "text/html");

            // add the views
            mail.AlternateViews.Add(plainView);
            mail.AlternateViews.Add(htmlView);      //needed
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "透過gmail寄信 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            //設定寄件者
            MailAddress from = new MailAddress(email_addr_from, email_addr_from_nicknane, Encoding.GetEncoding(email_encoding));
            //設定收件者
            MailAddress to = new MailAddress(email_addr_to, email_addr_to_nicknane, Encoding.GetEncoding(email_encoding));
            MailMessage mail = new MailMessage(from, to);

            mail.Priority = priority;

            mail.Subject = mail_subject;    //郵件標題
            mail.SubjectEncoding = Encoding.GetEncoding(email_encoding);    //郵件標題編碼

            mail.Body = "<h1>這是郵件內容</h1><hr/><img src=\"signature.png\" />";
            mail.BodyEncoding = Encoding.GetEncoding(email_encoding);   //郵件內容編碼方式

            mail.IsBodyHtml = true; //是否是HTML郵件

            // 設定附件檔案(Attachment)
            string strFilePath = @"C:\______test_files\_material\signature.png";
            Attachment attachment = new Attachment(strFilePath);
            attachment.Name = Path.GetFileName(strFilePath);
            attachment.NameEncoding = Encoding.GetEncoding(email_encoding);
            attachment.TransferEncoding = TransferEncoding.Base64;
            // 設定該附件為一個內嵌附件(Inline Attachment)
            attachment.ContentDisposition.Inline = true;
            attachment.ContentDisposition.DispositionType = DispositionTypeNames.Inline;
            mail.Attachments.Add(attachment);   //附件

            SendGmail(mail);

            mail.Dispose();
            this.Cursor = Cursors.Default;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "透過gmail寄信 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            MailAddress from = new MailAddress(email_addr_from, email_addr_from_nicknane);
            MailAddress to = new MailAddress(email_addr_to, email_addr_to_nicknane);
            MailMessage mail = new MailMessage(from, to);

            mail.Subject = mail_subject;    //郵件標題
            //內容，可以用html的寫法，</br> 換行
            mail.Body = "<a href='http://tw.yahoo.com'>yahoo</a>"; //內容
            //mail.Body = mail_body;  //郵件內容
            mail.IsBodyHtml = true; //是否是HTML郵件
            Attachment attachment = new Attachment(attach_filename1);   //附件
            mail.Attachments.Add(attachment);   //附件

            SendGmail(mail);

            mail.Dispose();
            this.Cursor = Cursors.Default;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "透過gmail寄信 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            MailMessage mail = new MailMessage();
            //mail.From = new MailAddress(email_addr_from); //寄件者, 不包含顯示名稱
            //mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane); //寄件者, 顯示名稱
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, Encoding.UTF8); //寄件者, 顯示名稱, 編碼

            //mail.To.Add(new MailAddress(email_addr_to));    //收件者, 不包含顯示名稱
            mail.To.Add(new MailAddress(email_addr_to, email_addr_to_nicknane));    //收件者, 顯示名稱

            mail.Priority = priority;

            mail.Subject = mail_subject;    //郵件標題
            mail.SubjectEncoding = Encoding.UTF8;//郵件標題編碼

            mail.Body = mail_body;  //郵件內容
            mail.BodyEncoding = Encoding.UTF8;  //郵件內容編碼方式
            mail.IsBodyHtml = true; //是否是HTML郵件

            //寄送附件方法一
            mail.Attachments.Add(new Attachment(attach_filename1));  //附件

            /*
            //寄送附件方法二, 直接將string類型結果保存為附件, 不好用
            byte[] bytes = System.Text.Encoding.Default.GetBytes
                (@"<table><tr><td width=150>1234567891234567
        </td><td width=80>12345678</td></tr></table>");
            MemoryStream ms = new MemoryStream(bytes);
            ContentType ct = new ContentType();
            //附件文件類型
            ct.MediaType = MediaTypeNames.Text.Html;
            //附件名稱，可以是其它後綴名
            ct.Name = "附件名稱" + DateTime.Now.ToString() + ".html";

            mail.Attachments.Add(new Attachment(ms, ct));
            */

            SendGmail(mail);

            mail.Dispose();

            /*
            //寄送附件方法二
            ms.Close();
            ms.Dispose();
            */
            this.Cursor = Cursors.Default;
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void SendMailByGmail(List<string> MailList, string Subject, string Body)
        {
            mail_subject = "SendMailByGmail " + DateTime.Now.ToString(); //郵件標題
            richTextBox1.Text += "透過gmail寄信 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            MailMessage mail = new MailMessage();
            //mail.From = new MailAddress(email_addr_from); //寄件者, 不包含顯示名稱
            //mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane); //寄件者, 顯示名稱
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, Encoding.UTF8); //寄件者, 顯示名稱, 編碼

            //收件者，以逗號分隔不同收件者 例如 "test1@gmail.com,test2@gmail.com"
            //mail.To.Add(string.Join(",", MailList.ToArray()));
            //mail.To.Add(new MailAddress(email_addr_to));    //收件者, 不包含顯示名稱
            mail.To.Add(new MailAddress(email_addr_to, email_addr_to_nicknane));    //收件者, 顯示名稱

            mail.Priority = priority;

            mail.Subject = mail_subject;    //郵件標題
            mail.SubjectEncoding = Encoding.UTF8;//郵件標題編碼

            //郵件內容
            mail.Body = Body;
            mail.IsBodyHtml = true; //是否是HTML郵件
            mail.BodyEncoding = Encoding.UTF8;  //郵件內容編碼方式

            /*
            // *  outlook.com smtp.live.com port:25
            // *  yahoo smtp.mail.yahoo.com.tw port:465
            //
            */
            mail.Attachments.Add(new Attachment(attach_filename1));  //附件

            SendGmail(mail);

            mail.Dispose();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //SendMailByGmail();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試中... fail....\n";
            return;

            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "透過gmail寄信 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            //設定smtp主機
            string smtp_server_y = "smtp.mail.yahoo.com";
            //設定Port
            int smtp_server_port_y = 587;              //指定 SMTP 交易連接埠, 預設是25
            //填入寄送方email和密碼
            string email_addr_from_y = "bunshue@yahoo.com.tw";
            string email_addr_from_password_y = "passwd";
            //收信方email
            string emailTo = "David@insighteyes.com";

            MailMessage mail = new MailMessage();
            mail.From = new MailAddress(email_addr_from_y);
            mail.To.Add(emailTo);
            mail.Subject = mail_subject;    //郵件標題
            mail.Body = mail_body;  //郵件內容
            mail.IsBodyHtml = false; //是否是HTML郵件

            //夾帶檔案
            //mail.Attachments.Add(new Attachment("C:\\SomeFile.txt"));
            //mail.Attachments.Add(new Attachment("C:\\SomeZip.zip"));

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient(smtp_server_y, smtp_server_port_y);   //實例一個SmtpClient類
            //smtp.Host = smtp_server_y;
            //smtp.Port = smtp_server_port_y;
            smtp.EnableSsl = true; //gmail預設開啟驗證, 指定 SmtpClient 使用安全套接字層 (SSL) 加密連接
            smtp.UseDefaultCredentials = false; //不使用默認憑證，注意此句必須放在smtp.Credentials() 的上面
            smtp.Credentials = new NetworkCredential(email_addr_from_y, email_addr_from_password_y);    //這裡要填正確的帳號跟密碼, 驗證寄件者

            SendMail(smtp, mail);

            smtp.Dispose();
            mail.Dispose();
        }
    }
}


/*
//當郵件發送失敗，發送異常時 使用備用方法調用備用郵箱發送

 try
 {

 }
 catch (Exception)
 {
 //當郵件發送失敗，發送異常時 使用備用方法調用備用郵箱發送
 SendBackUp(sender);
 }

*/