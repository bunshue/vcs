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
using System.Net.Mail;  //for MailMessage
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


namespace vcs_SendMail1
{
    public partial class Form1 : Form
    {
        //共用的郵件資訊

        string mail_server = "smtp.gmail.com";  //POP３服務器的名稱
        int mail_server_port = 25;              //指定 SMTP 交易連接埠, 預設是25
        string addr_from = "bunshue@gmail.com";
        string addr_from_pw = string.Empty;
        string addr_to = "David@insighteyes.com";

        string filename1 = @"C:\______test_files\picture1.jpg";
        string filename2 = @"C:\______test_files\__RW\_excel\2019~2021新竹日出日沒時刻表.xls";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_txt\\gmail_key.txt";
            if (File.Exists(filename) == false)
            {
                MessageBox.Show("Gmail_KEY 檔案不存在, 離開", "vcs_SendMail1", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }

            //讀取檔案
            string kk = File.ReadAllText(filename, System.Text.Encoding.Default);
            //richTextBox1.Text += "檔案內容 : " + kk + "\n";
            //richTextBox1.Text += "長度：" + kk.Length.ToString() + "\n";

            if (kk.Length == 15)
            {
                addr_from_pw = kk;
            }
            else
            {
                addr_from_pw = "xxxx";

                MessageBox.Show("Gmail_KEY 錯誤, 離開", "vcs_SendMail1", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }
        }

        private void SendMail(SmtpClient client, MailMessage mail)
        {
            try
            {
                client.Send(mail);  //寄送郵件
                richTextBox1.Text += "信件已寄出, 時間 : " + DateTime.Now.ToString() + "\n";
            }
            //Handle Mail Exceptions
            catch (InvalidOperationException exInvalidOperation)            //沒有指定 SMTP Server
            {
                richTextBox1.Text += "信件寄送失敗1, 時間 : " + DateTime.Now.ToString() + "\t原因 : " + exInvalidOperation.Message.ToString() + "\n";
            }
            catch (SmtpFailedRecipientException exSmtpFailedRecipient)      //指定錯誤的收件者
            {
                richTextBox1.Text += "信件寄送失敗2, 時間 : " + DateTime.Now.ToString() + "\t原因 : " + exSmtpFailedRecipient.Message.ToString() + "\n";
            }
            catch (SmtpException exSmtp)                                    //找不到 SMTP 或 其他的例外錯誤
            {
                richTextBox1.Text += "信件寄送失敗3, 時間 : " + DateTime.Now.ToString() + "\t原因 : " + exSmtp.Message.ToString() + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "信件寄送失敗4, 時間 : " + DateTime.Now.ToString() + "\t原因 : " + ex.Message.ToString() + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 1\t" + DateTime.Now.ToString();

            /*
            //MailAddress 的用法
            MailAddress from = new MailAddress(addr_from, "寄件者顯示的名稱");
            MailAddress to = new MailAddress(addr_to, "收件者顯示的名稱");
            MailMessage message = new MailMessage(from, to);
            */

            try
            {
                //MailMessage mail = new MailMessage(addr_from, addr_to, subject, "郵件內容(Body)");   //一次寫完
                mail = new MailMessage();    //實例一個MailMessage類
                //mail.BodyEncoding  //郵件編碼方式
                mail.Priority = MailPriority.High;   //設定電子郵件的優先順序

                //mail.From = new MailAddress(addr_from);
                //mail.From = new MailAddress(addr_from, "寄件者的自稱"); //email, 顯示名稱
                mail.From = new MailAddress(addr_from, "寄件者的自稱", Encoding.UTF8); //email, 顯示名稱, 編碼
                //mail.From = new MailAddress("lion.mouse.cat.dog", "寄件者的自稱"); //email, 顯示名稱    不能亂寫

                //mail.To.Add(addr_to);
                mail.To.Add(new MailAddress(addr_to, "尊敬的收件者1"));
                mail.To.Add(new MailAddress(addr_to, "尊敬的收件者2"));

                //副本
                mail.CC.Add(new MailAddress(addr_to, "副本"));

                //密件副本
                mail.Bcc.Add(new MailAddress(addr_to, "密件副本"));


                //對方回復郵件時默認的接收地址
                mail.ReplyTo = new MailAddress(addr_from, "IMS-Sales", Encoding.GetEncoding(950));
                mail.ReplyToList.Add(new MailAddress("David@insighteyes.com", "receiver"));

                mail.Subject = subject; //郵件標題
                mail.SubjectEncoding = Encoding.UTF8;//郵件標題編碼

                //各種郵件內容的寫法
                //mail.Body = ....      //郵件內容
                //mail.Body = "莫聽穿林打葉聲，何妨吟嘯且徐行。竹杖芒鞋輕勝馬，誰怕？一蓑煙雨任平生。料峭春風吹酒醒，微冷，山頭斜照卻相迎。回首向來蕭瑟處，歸去，也無風雨也無晴。";
                //mail.Body = richTextBox_mail.Text;
                //mailBody(mail);
                //mail.Body = "<font color=\"red\">莫聽穿林打葉聲，何妨吟嘯且徐行</font>"; //郵件正文
                mail.Body = "<html><body><h1>牡丹亭</h1><br><img src=\"C:\\______test_files\\picture1.jpg\"></body></html>";
                mail.Body = "牡丹亭";

                mail.BodyEncoding = Encoding.UTF8;//郵件內容編碼 
                mail.IsBodyHtml = true; //是否是HTML郵件 

                //通知狀態 OnSuccess, OnFailure, Delay, None, Never
                mail.DeliveryNotificationOptions = DeliveryNotificationOptions.OnFailure | DeliveryNotificationOptions.OnSuccess;

                /*
                //附加檔案 寫法 1
                Attachment attachment = new Attachment(filename1);
                mail.Attachments.Add(attachment);
                */

                //附加檔案 寫法 2
                Attachment attachment = new Attachment(filename2, MediaTypeNames.Application.Octet);
                ContentDisposition disposition = attachment.ContentDisposition;
                disposition.CreationDate = File.GetCreationTime(filename2);
                disposition.ModificationDate = File.GetLastWriteTime(filename2);
                disposition.ReadDate = File.GetLastAccessTime(filename2);
                mail.Attachments.Add(attachment);

                //附加檔案 寫法 3
                mail.Attachments.Add(new Attachment(filename1));

                //附加檔案 寫法 4

                mail.Attachments.Add(new Attachment(@"C:\______test_files\__RW\_word\Step.doc", System.Net.Mime.MediaTypeNames.Application.Rtf)); //添加附件，第二個參數表示附件的文件類型，可以不用指定

                //附加檔案 寫法 5
                /*
                foreach (var attachment in sender.Attachments)
                {
                    mail.Attachments.Add(attachment);
                }
                */

                //client = new SmtpClient(mail_server, mail_server_port);   //實例一個SmtpClient類   same
                client = new SmtpClient();   //實例一個SmtpClient類

                client.UseDefaultCredentials = true;//SMTP服務器需要身份認證，目前基本沒有不需要認證的了
                //client.Credentials = CredentialCache.DefaultNetworkCredentials;   //不可, 需要驗證寄件者
                client.Credentials = new NetworkCredential(addr_from, addr_from_pw);   //驗證寄件者

                client.DeliveryMethod = SmtpDeliveryMethod.Network; //將client的出站方式設為 Network
                client.Host = mail_server;  //設定smtp Server
                client.Port = mail_server_port; //設定Port  //指定 SMTP 交易連接埠, 預設是25
                client.EnableSsl = true;  //是否啟用 SSL    gmail預設開啟驗證 smtp服務器是否啟用SSL加密
                SendMail(client, mail); //包一層 看寄信結果
                client.Dispose();
                mail.Dispose();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "郵件寄送失敗, 原因 : " + ex.Message + "\n";
            }
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

        private void button2_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 2\t" + DateTime.Now.ToString();

            try
            {
                mail = new MailMessage(addr_from, addr_to);  //實例一個MailMessage類
                mail.Subject = subject;
                mail.Body = richTextBox_mail.Text;
                using (client = new SmtpClient(mail_server, mail_server_port)) //實例一個SmtpClient類
                {
                    client.Credentials = new NetworkCredential(addr_from, addr_from_pw);   //驗證寄件者
                    client.EnableSsl = true;

                    //client.Send(mail);
                    SendMail(client, mail); //包一層 看寄信結果
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "郵件寄送失敗, 原因 : " + ex.Message + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 3\t" + DateTime.Now.ToString();

            string myMailEncoding = "utf-8";
            string myFromEmail = addr_from;
            string myFromName = "測試寄件者";
            string myToEmail = addr_to;
            string myToName = "測試收件者";

            MailAddress from = new MailAddress(myFromEmail, myFromName, Encoding.GetEncoding(myMailEncoding));
            MailAddress to = new MailAddress(myToEmail, myToName, Encoding.GetEncoding(myMailEncoding));
            mail = new MailMessage(from, to);

            mail.Subject = subject;
            mail.SubjectEncoding = Encoding.GetEncoding(myMailEncoding);

            mail.Body = "<h1>這是郵件內容</h1><hr/><img src=\"signature.png\" />";
            mail.BodyEncoding = Encoding.GetEncoding(myMailEncoding);

            mail.IsBodyHtml = true;
            mail.Priority = MailPriority.High;

            // 設定附件檔案(Attachment)
            string strFilePath = @"C:\______test_files\_material\signature.png";
            Attachment attachment = new Attachment(strFilePath);
            attachment.Name = Path.GetFileName(strFilePath);
            attachment.NameEncoding = Encoding.GetEncoding(myMailEncoding);
            attachment.TransferEncoding = TransferEncoding.Base64;
            // 設定該附件為一個內嵌附件(Inline Attachment)
            attachment.ContentDisposition.Inline = true;
            attachment.ContentDisposition.DispositionType = DispositionTypeNames.Inline;
            mail.Attachments.Add(attachment);

            client = new SmtpClient(mail_server, mail_server_port);   //實例一個SmtpClient類

            client.Credentials = new NetworkCredential(addr_from, addr_from_pw);   //驗證寄件者
            client.EnableSsl = true;

            //client.Send(mail);
            SendMail(client, mail); //包一層 看寄信結果

            client.Dispose();
            mail.Dispose();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            sendmail();
        }

        private void sendmail()
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 4\t" + DateTime.Now.ToString();

            try
            {
                //設定寄件人
                MailAddress senderAddress = new MailAddress(addr_from, "AAAAAAA");//寄件者訊息
                //設定收件人
                MailAddress receiverAddress = new MailAddress(addr_to, "BBBBBBBBB");//<-這物件只是用來設定郵件帳號而已~
                mail = new MailMessage(senderAddress, receiverAddress);//<-這物件是郵件訊息的部分~需設定寄件人跟收件人~可直接打郵件帳號也可以使用MailAddress物件~
                //mail主旨
                mail.Subject = subject;
                //內文，可以用html的寫法，</br> 換行
                mail.Body = "<a href='http://tw.yahoo.com'>yahoo</a>"; //內文
                //mail.Body = richTextBox_mail.Text;//內文
                mail.IsBodyHtml = true;//<-如果要這封郵件吃html的話~這屬性就把他設為true~~
                //加入附件
                Attachment attachment = new Attachment(filename1);//<-這是附件部分~先用附件的物件把路徑指定進去~
                mail.Attachments.Add(attachment);//<-郵件訊息中加入附件

                client = new SmtpClient(mail_server, mail_server_port);   //實例一個SmtpClient類

                client.Port = mail_server_port; //設定Port  //指定 SMTP 交易連接埠, 預設是25
                client.Credentials = new NetworkCredential(addr_from, addr_from_pw);   //驗證寄件者
                client.EnableSsl = true;

                //client.Send(mail);
                SendMail(client, mail); //包一層 看寄信結果
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }


        private void SendMailByGmail(List<string> MailList, string Subject, string Body)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 5\t" + DateTime.Now.ToString();

            mail = new MailMessage();

            //寄件者
            mail.From = new MailAddress(addr_from, "寄件者的自稱", Encoding.UTF8); //email, 顯示名稱, 編碼

            //收件者，以逗號分隔不同收件者 例如 "test1@gmail.com,test2@gmail.com"
            //mail.To.Add(string.Join(",", MailList.ToArray()));
            mail.To.Add(new MailAddress(addr_to, "尊敬的收件者1"));

            //郵件標題
            mail.Subject = Subject;

            //郵件標題編碼 
            mail.SubjectEncoding = Encoding.UTF8;

            //郵件內容
            mail.Body = Body;
            mail.IsBodyHtml = true;//支援html
            mail.BodyEncoding = Encoding.UTF8;//郵件內容編碼
            mail.Priority = MailPriority.Normal;//郵件優先級

            #region 其它 Host
            /*
            // *  outlook.com smtp.live.com port:25
            // *  yahoo smtp.mail.yahoo.com.tw port:465
            //
            */
            #endregion

            //建立 SmtpClient 物件 並設定 Gmail的smtp主機及Port
            client = new SmtpClient(mail_server, mail_server_port);   //實例一個SmtpClient類

            client.Credentials = new NetworkCredential(addr_from, addr_from_pw);   //驗證寄件者

            client.EnableSsl = true;    //Gmial 的 smtp 使用 SSL

            //client.Send(mail);
            SendMail(client, mail); //包一層 看寄信結果
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //SendMailByGmail();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "測試中... fail....\n";
            return;

            //設定smtp主機
            string smtpAddress = "smtp.mail.yahoo.com";
            //設定Port
            int portNumber = 587;
            bool enableSSL = true;
            //填入寄送方email和密碼
            string emailFrom = "bunshue@yahoo.com.tw";
            string password = "passwd";
            //收信方email
            string emailTo = "David@insighteyes.com";
            //主旨
            string subject = "Hello";
            //內容
            string body = "Hello, I'm just writing this to say Hi!";

            using (MailMessage mail = new MailMessage())
            {
                mail.From = new MailAddress(emailFrom);
                mail.To.Add(emailTo);
                mail.Subject = subject;
                mail.Body = body;
                // 若你的內容是HTML格式，則為True
                mail.IsBodyHtml = false;

                //夾帶檔案
                //mail.Attachments.Add(new Attachment("C:\\SomeFile.txt"));
                //mail.Attachments.Add(new Attachment("C:\\SomeZip.zip"));

                using (SmtpClient smtp = new SmtpClient(smtpAddress, portNumber))
                {
                    smtp.Credentials = new NetworkCredential(emailFrom, password);
                    smtp.EnableSsl = enableSSL;
                    smtp.Send(mail);
                }
            }

        }

    }
}

