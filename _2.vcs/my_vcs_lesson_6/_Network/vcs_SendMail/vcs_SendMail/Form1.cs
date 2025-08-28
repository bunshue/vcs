using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;       //for NetworkCredential     NetworkCredential ：這個類別可用來提供密碼架構的驗證 (Authentication) 機制的認證。 建立認證帳號需要用到
using System.Net.Mail;  //for MailMessage, SmtpClient 新建郵件、發送郵件需要用到

//using System.Web.Mail;  //早期的.NET版本, 不推薦使用了
using System.Net.Mime;  //for MediaTypeNames

/*
郵箱必須開啟POP3/SMTP服務才可以
 
要寄Gmail信首先要登入Gmail，
然後到 https://www.google.com/settings/security/lesssecureapps
低安全性應用程式 → 開啟較低的應用程式存取權限
選擇開啟，否則會無法正常寄信

01.前置動作:(把Gmail的安全性調低，否則會發生 5.5.1 Authentication Required. 的錯誤!)
修改網址 https://www.google.com/settings/security/lesssecureapps
進入頁面之後選擇 安全性較低的應用程式存取權限 [啟用] 

*/

/*
常見的電子郵件協議有SMTP(簡單郵件傳輸協議)、POP3(郵局協議)、IMAP(Internet郵件訪問協議)
*/


//自 2022 年 5 月 30 日起，​​如果第三方應用程式或裝置只要求您以使用者名稱和密碼登入 Google 帳戶，Google 將不再支援這些應用程式或裝置。

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

        string attach_filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string attach_filename2 = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\2019~2021新竹日出日沒時刻表.xls";
        string attach_filename3 = @"D:\_git\vcs\_1.data\______test_files1\__RW\_word\Step.doc";   //RTF檔案

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            mail_body = richTextBox_mail.Text;
            show_item_location();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_key\gmail_key.txt";
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

            tb_email_addr_from.Text = email_addr_from;
            tb_email_addr_from_password.Text = email_addr_from_password;
            tb_email_addr_from_password.PasswordChar = '*';
            tb_email_addr_from_nicknane.Text = email_addr_from_nicknane;

            tb_email_addr_to.Text = email_addr_to;
            tb_email_addr_to_nicknane.Text = email_addr_to_nicknane;

            tb_email_addr_cc.Text = email_addr_cc;



            tb_smtp_server.Text = smtp_server;
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
            dx = 165;
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

            button14.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button15.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button16.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox_mail.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 7);
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

                richTextBox1.Text += "BBBBBBBBB\n";

                /*
                object userState = mail;
                smtp.SendAsync(mail, userState);   //寄送郵件
                */
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
                richTextBox1.Text += "原因: " + ex.StackTrace.ToString() + "\n";
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

            mail.Priority = priority;       //郵件優先級

            mail.Subject = mail_subject;    //郵件標題
            mail.SubjectEncoding = Encoding.UTF8;//郵件標題編碼

            //各種郵件內容的寫法
            //mail.Body = "莫聽穿林打葉聲，何妨吟嘯且徐行。竹杖芒鞋輕勝馬，誰怕？一蓑煙雨任平生。料峭春風吹酒醒，微冷，山頭斜照卻相迎。回首向來蕭瑟處，歸去，也無風雨也無晴。";
            //mail.Body = mail_body;  //郵件內容
            //mailBody(mail);
            //mail.Body = "<font color=\"red\">莫聽穿林打葉聲，何妨吟嘯且徐行</font>"; //郵件內容
            mail.Body = "<html><body><h1>牡丹亭</h1><br><img src=\"D:\\_git\\vcs\\_1.data\\______test_files1\\picture1.jpg\"></body></html>";
            mail.Body = "牡丹亭";

            mail.BodyEncoding = Encoding.UTF8;  //郵件內容編碼方式
            //                  Encoding.GetEncoding("GB2312");
            //                  Encoding.Default;

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
            htmlBody += "<img src=\"D:\\_git\\vcs\\_1.data\\______test_files1\\picture1.jpg\" width=\"305\" height=\"400\" align=\"center\" border=30 bgcolor=\"#00FF00\">";

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
            string strFilePath = @"D:\_git\vcs\_1.data\______test_files1\_material\signature.png";
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
            var from = new MailAddress("bunshue@gmail.com", "bunshue");
            var to = new MailAddress("David@insighteyes.com", "david");
            var message = new MailMessage(from, to);
            message.Subject = "The subject 2";
            message.Body = "The message body";
            message.IsBodyHtml = true;
            var host = "smtp.gmail.com";
            var client = new SmtpClient(host, 587);
            client.EnableSsl = true;
            client.Credentials = new NetworkCredential("bunshue", email_addr_from_password);
            client.Send(message);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //TBD
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //使用Email類別寄信1
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "使用Email類別寄信1 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            /*
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

            string attach_filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string attach_filename2 = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel\2019~2021新竹日出日沒時刻表.xls";
            string attach_filename3 = @"D:\_git\vcs\_1.data\______test_files1\__RW\_word\Step.doc";   //RTF檔案
            */

            /*
            public static bool SendEmail(string from, string[] to, string[] cc, string[] bcc, string subject, string body,
            bool isBodyHtml, string[] attachments, string host, string password)
            */

            string[] to = new string[] { email_addr_to };
            string[] cc = new string[] { email_addr_cc };
            string[] bcc = new string[] { email_addr_cc };

            string[] attachments = new string[] { attach_filename1, attach_filename2, attach_filename3 };

            Console.WriteLine("subject = " + mail_subject);
            EmailInfo.SendEmail(email_addr_from, to, cc, bcc, mail_subject, mail_body, true, attachments, smtp_server, email_addr_from_password);
            this.Cursor = Cursors.Default;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "使用Email類別寄信2 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            SmtpMail send_mail = new SmtpMail(email_addr_to, email_addr_to_nicknane, mail_subject, email_addr_from, email_addr_from_password, smtp_server, smtp_server_port);
            send_mail.SendMail(mail_body);
            this.Cursor = Cursors.Default;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            mail_subject = ((Button)sender).Text + "\t" + DateTime.Now.ToString();
            richTextBox1.Text += "使用Email類別寄信3 ST\t" + mail_subject + "\n";
            Application.DoEvents();

            string[] to = new string[] { email_addr_to };

            EmailHelper.SendMail(mail_subject, mail_body, attach_filename1, email_addr_from, email_addr_from_password, to);

            this.Cursor = Cursors.Default;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //使用 EmailClass




            //使用EmailHelper2


            //獲得各種參數，不需要的用空字符串

            string smtpServer = "smtp.gmail.com";//163郵箱的smtp服務器 
            int port = 25;//端口
            string mailFrom = "bunshue@gmail.com";//發件人郵箱 
            string pwd = email_addr_from_password;//密碼
            string mailTo = "David@insighteyes.com";//收件人郵箱,多個用戶用逗號隔開
            string mailCC = "";//抄送人,多個用戶用逗號隔開
            string mailBcc = "";//密送
            string mailSubject = "測試郵件";//主題
            string mailContent = "HI,這是我發給你的一個測試郵件";//內容
            string ah = attach_filename1 + "," + attach_filename2; //附件-文件路徑
            if (EmailHelper2.SendEmail(smtpServer, port, mailFrom, pwd, mailTo, mailCC, mailBcc, mailSubject, mailContent, ah) == true)
            {
                richTextBox1.Text += "發送成功!\n";
            }
            else
            {
                richTextBox1.Text += "發送失敗\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //使用 SendMail Class
            try
            {
                SendMail mail = new SendMail();
                mail.Host = smtp_server;//服務器smtp地址 
                mail.SmtpUsername = email_addr_from;//登陸用戶名 
                mail.SmtpPassWord = email_addr_from_password;//登錄密碼 
                mail.Send(email_addr_from, email_addr_to, mail_subject, mail_body, null, null);//發件人地址,收件人地址,標題,內容,其他,其他 
            }
            catch (Exception ex)
            {
                //可以捕獲異常 
            }
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

        private void bt_send_Click(object sender, EventArgs e)
        {

        }

        private Attachment att;       //用於構造郵件附件屬性和方法

        private void bt_browse_attachments_Click(object sender, EventArgs e)
        {
            openFileDialog1.CheckFileExists = true;  //不存在文件名稱顯示警告
            openFileDialog1.ValidateNames = true;    //值接受Win32文件
            openFileDialog1.Multiselect = false;     //不同意多選文件
            openFileDialog1.Filter = "全部文件(*.*)|*.*";

            //加入附件 現僅支持加入一個附件
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text = openFileDialog1.FileName;
                att = new Attachment(openFileDialog1.FileName);
                //msg.Attachments.Add(att);
            }
        }

        private void bt_clear_attachments_Click(object sender, EventArgs e)
        {
            //msg.Attachments.Clear();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //異步發送郵件

            //創建MailMessage對象
            MailAddress from = new MailAddress(email_addr_from);
            MailAddress to = new MailAddress(email_addr_to);
            MailMessage mailMessage = new MailMessage(from, to);
            mailMessage.Subject = "主題";
            mailMessage.Body = "這是一封來自遠方的郵件.";

            //附件
            Attachment attachment01 = new Attachment(attach_filename1);
            Attachment attachment02 = new Attachment(attach_filename1);
            mailMessage.Attachments.Add(attachment01);
            mailMessage.Attachments.Add(attachment02);

            SmtpClient smtp = new SmtpClient(smtp_server, smtp_server_port);   //實例一個SmtpClient類
            smtp.UseDefaultCredentials = true;
            smtp.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password); //這裡要填正確的帳號跟密碼, 驗證寄件者
            //smtp.Timeout = 5000;
            try
            {
                //使用異步發送,不會阻塞該線程
                smtp.SendCompleted += new //完成發送調用回調函數
                SendCompletedEventHandler(SendCompletedCallback);
                smtp.SendAsync(mailMessage, mailMessage);
            }
            catch (Exception ex)
            {
                mailMessage.Dispose();    //主動釋放資源
                smtp.Dispose();
                MessageBox.Show("發送失敗!  " + System.Environment.NewLine + "錯誤信息:" + ex.Message);
            }
            return;
        }

        //異步發送完成的回調函數:
        public static void SendCompletedCallback(object sender, AsyncCompletedEventArgs e)
        {
            SmtpClient smtp = (SmtpClient)sender;
            //MailMessage mailMessage = (MailMessage)e.UserState;
            if (e.Cancelled)
            {
                MessageBox.Show("Send canceled.");
            }
            if (e.Error != null)
            {
                MessageBox.Show("錯誤信息: " + e.Error.ToString());
            }
            else
            {
                MessageBox.Show("Message Sent.");
                smtp.Dispose();
                //mailMessage.Dispose();
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }
    }

    public class SmtpMail
    {
        private string toAddress = "";
        private string mailUser = "";
        private string userPassword = "";
        private string displayName = "";
        private string mailSubject = "";
        private string sendMessage = "";
        private int mailPort = 0;
        private string mailHost = "";

        public string Message
        {
            get
            {
                return sendMessage;
            }
        }

        public SmtpMail(string to_address, string display_name, string mail_subject, string mail_user, string user_password, string mail_host, int mail_port)
        {
            toAddress = to_address;
            displayName = display_name;
            mailSubject = mail_subject;
            mailUser = mail_user;
            userPassword = user_password;
            mailHost = mail_host;
            mailPort = mail_port;
        }

        public void SendMail(string strBody)
        {
            //MailMessage mail = new MailMessage(from, to);
            MailMessage mail = new MailMessage();
            mail.To.Add(toAddress);
            mail.From = new MailAddress(mailUser, displayName, System.Text.Encoding.UTF8);
            mail.Subject = mailSubject;
            mail.SubjectEncoding = System.Text.Encoding.UTF8;
            mail.Body = strBody;
            mail.BodyEncoding = System.Text.Encoding.UTF8;
            mail.IsBodyHtml = false;
            mail.Priority = MailPriority.Normal;

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient(mailHost, mailPort);   //實例一個SmtpClient類
            //smtp.Host = smtp_server;
            //smtp.Port = smtp_server_port;
            smtp.Timeout = 9999;
            smtp.EnableSsl = true; //gmail預設開啟驗證, 指定 SmtpClient 使用安全套接字層 (SSL) 加密連接
            smtp.UseDefaultCredentials = false; //不使用默認憑證，注意此句必須放在smtp.Credentials() 的上面
            //smtp.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password); //這裡要填正確的帳號跟密碼, 驗證寄件者
            smtp.Credentials = new NetworkCredential(mailUser, userPassword);
            //smtp.Credentials = CredentialCache.DefaultNetworkCredentials;   //不可, 需要驗證寄件者
            smtp.DeliveryMethod = SmtpDeliveryMethod.Network;   //通過網絡發送到SMTP服務器
            smtp.SendCompleted += new SendCompletedEventHandler(smtp_SendCompleted);


            Console.WriteLine("");
            Console.WriteLine("mailHost = " + mailHost);
            Console.WriteLine("mailPort = " + mailPort);
            Console.WriteLine("mailUser = " + mailUser);
            Console.WriteLine("userPassword = " + userPassword);


            Console.WriteLine("");

            try
            {
                smtp.Send(mail);
            }
            catch (Exception ex)
            {
                sendMessage = ex.ToString();
                throw new Exception(ex.Message);

            }
            /*
            catch (SmtpException ex)
            {
                sendMessage = ex.ToString();
            }
            */
            smtp.Dispose();
        }

        void smtp_SendCompleted(object sender, AsyncCompletedEventArgs e)
        {
            MailMessage mail = (MailMessage)e.UserState;
            string subject = mail.Subject;

            if (e.Cancelled)
            {
                string cancelled = string.Format("[{0}] Send canceled.", subject);
                sendMessage = cancelled;
            }
            if (e.Error != null)
            {
                string error = String.Format("[{0}] {1}", subject, e.Error.ToString());
                sendMessage = error;
            }
            else
            {
                sendMessage = "Message has been sent successfully!";
            }
        }
    }

    public static class EmailHelper
    {
        /// <summary>
        /// 發送郵件
        /// </summary>
        /// <param name="subject">郵件主題</param>
        /// <param name="msg">郵件內容</param>
        /// <param name="filePath">附件地址，如果不添加附件傳null或""</param>
        /// <param name="senderEmail">發送人郵箱地址</param>
        /// <param name="senderPwd">發送人郵箱密碼</param>
        /// <param name="recipientEmail">接收人郵箱</param>
        public static void SendMail(string subject, string msg, string filePath, string senderEmail, string senderPwd, params string[] recipientEmail)
        {
            if (!CheckIsNotEmptyOrNull(subject, msg, senderEmail, senderPwd) || recipientEmail == null || recipientEmail.Length == 0)
            {
                throw new Exception("輸入信息無效");
            }
            try
            {
                string[] sendFromUser = senderEmail.Split('@');

                //構造一個Email的Message對象
                MailMessage message = new MailMessage();

                //確定smtp服務器地址。實例化一個Smtp客戶端
                System.Net.Mail.SmtpClient client = new System.Net.Mail.SmtpClient("smtp." + sendFromUser[1]);

                //構造發件人地址對象
                message.From = new MailAddress(senderEmail, sendFromUser[0], Encoding.UTF8);

                //構造收件人地址對象
                foreach (string userName in recipientEmail)
                {
                    message.To.Add(new MailAddress(userName, userName.Split('@')[0], Encoding.UTF8));
                }

                if (!string.IsNullOrEmpty(filePath))
                {
                    Attachment attach = new Attachment(filePath);
                    //得到文件的信息
                    ContentDisposition disposition = attach.ContentDisposition;
                    disposition.CreationDate = System.IO.File.GetCreationTime(filePath);
                    disposition.ModificationDate = System.IO.File.GetLastWriteTime(filePath);
                    disposition.ReadDate = System.IO.File.GetLastAccessTime(filePath);
                    //向郵件添加附件
                    message.Attachments.Add(attach);
                }

                //添加郵件主題和內容
                message.Subject = subject;
                message.SubjectEncoding = Encoding.UTF8;
                message.Body = msg;
                message.BodyEncoding = Encoding.UTF8;

                //設置郵件的信息
                client.DeliveryMethod = SmtpDeliveryMethod.Network;
                message.BodyEncoding = System.Text.Encoding.UTF8;
                message.IsBodyHtml = false;

                //如果服務器支持安全連接，則將安全連接設為true。
                //gmail,qq支持，163不支持
                switch (sendFromUser[1])
                {
                    case "gmail.com":
                    case "qq.com":
                        client.EnableSsl = true;
                        break;
                    default:
                        client.EnableSsl = false;
                        break;
                }

                //設置用戶名和密碼。
                client.UseDefaultCredentials = false;
                //用戶登陸信息
                NetworkCredential myCredentials = new NetworkCredential(senderEmail, senderPwd);
                client.Credentials = myCredentials;
                //發送郵件
                client.Send(message);
            }
            catch (Exception ex)
            {
                throw (ex);
            }
        }

        /// <summary>
        /// 驗證所有傳入字符串不能為空或null
        /// </summary>
        /// <param name="ps">參數列表</param>
        /// <returns>都不為空或null返回true，否則返回false</returns>
        public static bool CheckIsNotEmptyOrNull(params string[] ps)
        {
            if (ps != null)
            {
                foreach (string item in ps)
                {
                    if (string.IsNullOrEmpty(item)) return false;
                }
                return true;
            }
            return false;
        }
    }



    public class EmailHelper2
    {
        /// <summary>
        /// 發送郵件
        /// </summary>
        /// <param name="smtpServer">smtp服務器</param>
        /// <param name="port">端口</param>
        /// <param name="mailFrom">發件人郵箱</param>
        /// <param name="userPassword">密碼</param>
        /// <param name="mailTo">收件人</param>
        /// <param name="strcc">抄送人</param>
        /// <param name="strBcc">密送</param>
        /// <param name="mailSubject">郵件主題</param>
        /// <param name="mailContent">內容</param>
        /// <param name="strs">附件</param>
        /// <returns>發送成功返回true否則false</returns>
        public static bool SendEmail(string smtpServer, int port, string mailFrom, string userPassword, string mailTo, string strcc, string strBcc, string mailSubject, string mailContent, string strs)
        {
            try
            {
                // 設置發送方的郵件信息
                // 郵件服務設置
                SmtpClient smtpClient = new SmtpClient();
                smtpClient.DeliveryMethod = SmtpDeliveryMethod.Network;//指定電子郵件發送方式
                smtpClient.Host = smtpServer; //指定SMTP服務器
                smtpClient.Port = port;//端口
                smtpClient.Credentials = new System.Net.NetworkCredential(mailFrom, userPassword);//驗證用戶名和密碼
                smtpClient.EnableSsl = true; //使用SSL
                // 發送郵件設置        
                MailMessage mailMessage = new MailMessage(mailFrom, mailTo); // 發送人和收件人

                mailMessage.Subject = mailSubject;//主題
                mailMessage.Body = mailContent;//內容
                mailMessage.BodyEncoding = Encoding.UTF8;//正文編碼
                mailMessage.IsBodyHtml = true;//設置為HTML格式
                mailMessage.Priority = MailPriority.Normal;//優先級
                //抄送人
                if (!string.IsNullOrEmpty(strcc))
                    mailMessage.CC.Add(strcc);
                //密送
                if (!string.IsNullOrEmpty(strBcc))
                    mailMessage.Bcc.Add(strBcc);
                //附件
                if (!string.IsNullOrEmpty(strs))
                {
                    List<string> paths = new List<string>();
                    if (strs.Contains(","))
                    {
                        paths = strs.Split(',').ToList();
                    }
                    else
                    {
                        paths.Add(strs);
                    }
                    foreach (var path in paths)
                    {
                        mailMessage.Attachments.Add(new Attachment(strs));
                    }
                }
                smtpClient.Send(mailMessage); // 發送郵件
                return true;
            }
            catch (Exception ex)
            {

                //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
                return false;
            }
        }
    }
    
    public static class EmailClass
    {
        /// <summary>
        /// 發件人
        /// </summary>
        public static string mailFrom { get; set; }

        /// <summary>
        /// 收件人
        /// </summary>
        public static string[] mailToArray { get; set; }

        /// <summary>
        /// 抄送
        /// </summary>
        public static string[] mailCcArray { get; set; }

        /// <summary>
        /// 標題
        /// </summary>
        public static string mailSubject { get; set; }

        /// <summary>
        /// 正文
        /// </summary>
        public static string mailBody { get; set; }

        /// <summary>
        /// 發件人密碼
        /// </summary>
        public static string mailPwd { get; set; }

        /// <summary>
        /// SMTP郵件服務器
        /// </summary>
        public static string host { get; set; }

        /// <summary>
        /// 郵件服務器端口
        /// </summary>
        public static int port { get; set; }

        /// <summary>
        /// 正文是否是html格式
        /// </summary>
        public static bool isbodyHtml { get; set; }

        /// <summary>
        /// 附件
        /// </summary>
        public static string[] attachmentsPath { get; set; }

        public static bool Send()
        {
            //使用指定的郵件地址初始化MailAddress實例
            MailAddress maddr = new MailAddress(mailFrom);

            //初始化MailMessage實例
            MailMessage myMail = new MailMessage();

            //向收件人地址集合添加郵件地址
            if (mailToArray != null)
            {
                for (int i = 0; i < mailToArray.Length; i++)
                {
                    myMail.To.Add(mailToArray[i].ToString());
                }
            }

            //向抄送收件人地址集合添加郵件地址
            if (mailCcArray != null)
            {
                for (int i = 0; i < mailCcArray.Length; i++)
                {
                    myMail.CC.Add(mailCcArray[i].ToString());
                }
            }
            //發件人地址
            myMail.From = maddr;

            //電子郵件的標題
            myMail.Subject = mailSubject;

            //電子郵件的主題內容使用的編碼
            myMail.SubjectEncoding = Encoding.UTF8;

            //電子郵件正文
            myMail.Body = mailBody;

            //電子郵件正文的編碼
            myMail.BodyEncoding = Encoding.Default;

            //電子郵件優先級
            myMail.Priority = MailPriority.High;

            //電子郵件不是html格式
            myMail.IsBodyHtml = isbodyHtml;

            //在有附件的情況下添加附件
            try
            {
                if (attachmentsPath != null && attachmentsPath.Length > 0)
                {
                    Attachment attachFile = null;
                    foreach (string path in attachmentsPath)
                    {
                        attachFile = new Attachment(path);
                        myMail.Attachments.Add(attachFile);
                    }
                }
            }
            catch (Exception err)
            {
                throw new Exception("在添加附件時有錯誤:" + err.Message);
            }

            SmtpClient client = new SmtpClient();

            //指定發件人的郵件地址和密碼以驗證發件人身份
            client.Credentials = new NetworkCredential(mailFrom, mailPwd);

            //設置SMTP郵件服務器
            //client.Host = "smtp." + myMail.From.Host;
            client.Host = host;

            //SMTP郵件服務器端口
            client.Port = port;

            //是否使用安全連接
            //client.EnableSsl = true;

            try
            {
                //將郵件發送到SMTP郵件服務器
                client.Send(myMail);
                return true;
            }
            catch (SmtpException ex)
            {
                string msg = ex.Message;
                return false;
            }
        }
    }


    public class SendMail
    {
        private string _host;
        public string Host
        {
            get { return _host; }
            set { _host = value; }
        }
        private int _port;
        public int Port
        {
            get { return _port; }
            set { _port = value; }
        }
        private string _smtpUsername;
        public string SmtpUsername
        {
            get { return _smtpUsername; }
            set { _smtpUsername = value; }
        }
        private string _smtpPassWord;
        public string SmtpPassWord
        {
            get { return _smtpPassWord; }
            set { _smtpPassWord = value; }
        }
        public void Send(string from, string to, string subject, string body, string[] cc, string[] bcc)
        {
            // Create mail message 
            MailMessage message = new MailMessage(from, to, subject, body);
            message.BodyEncoding = Encoding.GetEncoding(936);
            if (cc != null && cc.Length > 0)
            {
                foreach (string ccAddress in cc)
                    message.CC.Add(new MailAddress(ccAddress));
            }
            if (bcc != null && bcc.Length > 0)
            {
                foreach (string bccAddress in bcc)
                {
                    message.Bcc.Add(new MailAddress(bccAddress));
                }
            }
            // Send email 
            SmtpClient client = new SmtpClient(this._host, 25);
            if (!String.IsNullOrEmpty(this._smtpUsername) && !String.IsNullOrEmpty(this._smtpPassWord))

                client.Credentials = new NetworkCredential(this._smtpUsername, this._smtpPassWord);
            client.EnableSsl = false;
            client.Send(message);
        }
    }

    public class SmtpMail2
    {
        private string toAddress = "";
        private string mailUser = "";
        private string userPassword = "";
        private string displayName = "";
        private string mailSubject = "";
        private string sendMessage = "";
        private int mailPort = 0;
        private string mailHost = "";

        public string Message
        {
            get
            {
                return sendMessage;
            }
        }

        public SmtpMail2(string to_address, string display_name, string mail_subject, string mail_user, string user_password, int mail_port, string mail_host)
        {
            toAddress = to_address;
            displayName = display_name;
            mailSubject = mail_subject;
            mailUser = mail_user;
            userPassword = user_password;
            mailPort = mail_port;
            mailHost = mail_host;
        }

        public void SendMail(string strBody)
        {
            System.Net.Mail.MailMessage msg = new System.Net.Mail.MailMessage();
            msg.To.Add(toAddress);
            msg.From = new MailAddress(mailUser, displayName, System.Text.Encoding.UTF8);
            msg.Subject = mailSubject;
            msg.SubjectEncoding = System.Text.Encoding.UTF8;
            msg.Body = strBody;
            msg.BodyEncoding = System.Text.Encoding.UTF8;
            msg.IsBodyHtml = false;
            msg.Priority = MailPriority.Normal;

            SmtpClient client = new SmtpClient();
            client.Credentials = new System.Net.NetworkCredential
                (mailUser, userPassword);
            client.Port = mailPort;
            client.Host = mailHost;
            client.EnableSsl = false;
            client.SendCompleted += new SendCompletedEventHandler(client_SendCompleted);
            object userState = msg;
            try
            {
                client.SendAsync(msg, userState);
            }
            catch (System.Net.Mail.SmtpException ex)
            {
                sendMessage = ex.ToString();
            }
        }

        void client_SendCompleted(object sender, AsyncCompletedEventArgs e)
        {
            MailMessage mail = (MailMessage)e.UserState;
            string subject = mail.Subject;

            if (e.Cancelled)
            {
                string cancelled = string.Format("[{0}] Send canceled.", subject);
                sendMessage = cancelled;
            }
            if (e.Error != null)
            {
                string error = String.Format("[{0}] {1}", subject, e.Error.ToString());
                sendMessage = error;
            }
            else
            {
                sendMessage = "Message has been sent successfully!";
            }
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
