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

namespace vcs_SendMail
{
    public partial class Form1 : Form
    {
        //共用的郵件資訊
        string email_addr_from = "bunshue@gmail.com";
        string email_addr_from_password = string.Empty;
        string email_addr_from_nicknane = "王大頭";
        string email_addr_to = "david@insighteyes.com";
        string email_addr_cc = "bunshue@gmail.com";
        System.Net.Mail.MailPriority priority = System.Net.Mail.MailPriority.Normal;

        string mail_subject = "測試郵件標題";
        string mail_body = "郵件內容lion-mouse";
        string smtp_server = "smtp.gmail.com";  //POP3服務器的名稱
        int smtp_server_port = 25;              //指定 SMTP 交易連接埠, 預設是25

        string attach_filename1 = @"C:\______test_files\picture1.jpg";
        string attach_filename2 = @"C:\______test_files\__RW\_excel\2019~2021新竹日出日沒時刻表.xls";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string filename = "C:\\______test_files\\__RW\\_txt\\gmail_key.txt";
            if (File.Exists(filename) == false)
            {
                MessageBox.Show("Gmail_KEY 檔案不存在, 離開", "vcs_SendMail", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Application.Exit();
                return;
            }

            //讀取檔案
            string kk = File.ReadAllText(filename, System.Text.Encoding.Default);
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

        private void button0_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 1\t" + DateTime.Now.ToString();

            /*
            //MailAddress 的用法
            MailAddress from = new MailAddress(email_addr_from, "寄件者顯示的名稱");
            MailAddress to = new MailAddress(email_addr_to, "收件者顯示的名稱");
            MailMessage message = new MailMessage(from, to);
            */

            try
            {
                //MailMessage mail = new MailMessage(email_addr_from, email_addr_to, subject, "郵件內容(Body)");   //一次寫完
                mail = new MailMessage();    //實例一個MailMessage類
                //mail.BodyEncoding  //郵件編碼方式
                mail.Priority = MailPriority.High;   //設定電子郵件的優先順序

                //mail.From = new MailAddress(email_addr_from);
                //mail.From = new MailAddress(email_addr_from, "寄件者的自稱"); //email, 顯示名稱
                mail.From = new MailAddress(email_addr_from, "寄件者的自稱", Encoding.UTF8); //email, 顯示名稱, 編碼
                //mail.From = new MailAddress("lion.mouse.cat.dog", "寄件者的自稱"); //email, 顯示名稱    不能亂寫

                //mail.To.Add(email_addr_to);
                mail.To.Add(new MailAddress(email_addr_to, "尊敬的收件者1"));
                mail.To.Add(new MailAddress(email_addr_to, "尊敬的收件者2"));

                //副本
                mail.CC.Add(new MailAddress(email_addr_to, "副本"));

                //密件副本
                mail.Bcc.Add(new MailAddress(email_addr_to, "密件副本"));


                //對方回復郵件時默認的接收地址
                mail.ReplyTo = new MailAddress(email_addr_from, "IMS-Sales", Encoding.GetEncoding(950));
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

                mail.Attachments.Add(new Attachment(@"C:\______test_files\__RW\_word\Step.doc", System.Net.Mime.MediaTypeNames.Application.Rtf)); //添加附件，第二個參數表示附件的文件類型，可以不用指定

                //附加檔案 寫法 5
                /*
                foreach (var attachment in sender.Attachments)
                {
                    mail.Attachments.Add(attachment);
                }
                */

                //client = new SmtpClient(smtp_server, smtp_server_port);   //實例一個SmtpClient類   same
                client = new SmtpClient();   //實例一個SmtpClient類

                client.UseDefaultCredentials = true;//SMTP服務器需要身份認證，目前基本沒有不需要認證的了
                //client.Credentials = CredentialCache.DefaultNetworkCredentials;   //不可, 需要驗證寄件者
                client.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password);   //驗證寄件者

                client.DeliveryMethod = SmtpDeliveryMethod.Network; //將client的出站方式設為 Network
                client.Host = smtp_server;  //設定smtp Server
                client.Port = smtp_server_port; //設定Port  //指定 SMTP 交易連接埠, 預設是25
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

        private void button1_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 2\t" + DateTime.Now.ToString();

            try
            {
                mail = new MailMessage(email_addr_from, email_addr_to);  //實例一個MailMessage類
                mail.Subject = subject;
                mail.Body = richTextBox_mail.Text;
                using (client = new SmtpClient(smtp_server, smtp_server_port)) //實例一個SmtpClient類
                {
                    client.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password);   //驗證寄件者
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

        private void button2_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            MailMessage mail;
            SmtpClient client;
            string subject = "主旨 : 用vcs寄信 用gmail寄信 3\t" + DateTime.Now.ToString();

            string myMailEncoding = "utf-8";
            string myFromEmail = email_addr_from;
            string myFromName = "測試寄件者";
            string myToEmail = email_addr_to;
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

            client = new SmtpClient(smtp_server, smtp_server_port);   //實例一個SmtpClient類

            client.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password);   //驗證寄件者
            client.EnableSsl = true;

            //client.Send(mail);
            SendMail(client, mail); //包一層 看寄信結果

            client.Dispose();
            mail.Dispose();
        }

        private void button3_Click(object sender, EventArgs e)
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
                MailAddress senderAddress = new MailAddress(email_addr_from, "AAAAAAA");//寄件者訊息
                //設定收件人
                MailAddress receiverAddress = new MailAddress(email_addr_to, "BBBBBBBBB");//<-這物件只是用來設定郵件帳號而已~
                mail = new MailMessage(senderAddress, receiverAddress);//<-這物件是郵件訊息的部分~需設定寄件人跟收件人~可直接打郵件帳號也可以使用MailAddress物件~
                //mail主旨
                mail.Subject = subject;
                //內文，可以用html的寫法，</br> 換行
                mail.Body = "<a href='http://tw.yahoo.com'>yahoo</a>"; //內文
                //mail.Body = richTextBox_mail.Text;//內文
                mail.IsBodyHtml = true;//<-如果要這封郵件吃html的話~這屬性就把他設為true~~
                //加入附件
                Attachment attachment = new Attachment(attach_filename1);//<-這是附件部分~先用附件的物件把路徑指定進去~
                mail.Attachments.Add(attachment);//<-郵件訊息中加入附件

                client = new SmtpClient(smtp_server, smtp_server_port);   //實例一個SmtpClient類

                client.Port = smtp_server_port; //設定Port  //指定 SMTP 交易連接埠, 預設是25
                client.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password);   //驗證寄件者
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
            mail.From = new MailAddress(email_addr_from, "寄件者的自稱", Encoding.UTF8); //email, 顯示名稱, 編碼

            //收件者，以逗號分隔不同收件者 例如 "test1@gmail.com,test2@gmail.com"
            //mail.To.Add(string.Join(",", MailList.ToArray()));
            mail.To.Add(new MailAddress(email_addr_to, "尊敬的收件者1"));

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
            client = new SmtpClient(smtp_server, smtp_server_port);   //實例一個SmtpClient類

            client.Credentials = new NetworkCredential(email_addr_from, email_addr_from_password);   //驗證寄件者

            client.EnableSsl = true;    //Gmial 的 smtp 使用 SSL

            //client.Send(mail);
            SendMail(client, mail); //包一層 看寄信結果
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //SendMailByGmail();
        }

        private void button5_Click(object sender, EventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //從 gmail 寄信到 ims
            richTextBox1.Text += "透過gmail寄信 ST 0\n";
            Application.DoEvents();
            int result = SendEmail(email_addr_from, email_addr_from_password, new string[] { email_addr_to }, mail_subject + " case 0", mail_body + DateTime.Now.ToString(), smtp_server);
            if (result == 0)
            {
                richTextBox1.Text += "透過gmail寄信 ST 0 OK\n";
            }
            else
            {
                richTextBox1.Text += "透過gmail寄信 SP 0 NG\n";
            }
        }

        ///<summary>
        /// 發送郵件
        ///</summary>
        ///<param name="sendEmailAddress">發件人郵箱</param>
        ///<param name="sendEmailPwd">發件人密碼</param>
        ///<param name="msgToEmail">收件人郵箱地址</param>
        ///<param name="title">郵件標題</param>
        ///<param name="content">郵件內容</param>
        ///<param name="host">郵件SMTP服務器</param>
        ///<returns>0：失敗。1：成功！</returns>

        public int SendEmail(string sendEmailAddress, string sendEmailPwd, string[] msgToEmail, string title, string content, string host)
        {
            //OK
            //發件者郵箱地址
            string fjrtxt = sendEmailAddress;
            //發件者郵箱密碼
            string mmtxt = sendEmailPwd;
            string[] fasong = fjrtxt.Split('@');

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = smtp_server_port;
            //QQ郵箱使用ssl加密，需要設置SmtpClient.EnableSsl 屬性為True表示“指定 SmtpClient 使用安全套接字層 (SSL) 加密連接。”
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            //通過網絡發送到Smtp服務器
            smtp.DeliveryMethod = SmtpDeliveryMethod.Network;
            //通過用戶名和密碼 認證
            smtp.Credentials = new NetworkCredential(fasong[0].ToString(), email_addr_from_password);  //這裡要填正確的帳號跟密碼

            //發件人和收件人的郵箱地址
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.From = new MailAddress(fjrtxt);
            for (int i = 0; i < msgToEmail.Length; i++)
            {
                mail.To.Add(new MailAddress(msgToEmail[i]));
            }

            mail.Priority = System.Net.Mail.MailPriority.Normal;
            mail.Subject = title;   //郵件主題
            mail.SubjectEncoding = Encoding.UTF8;   //主題編碼
            mail.Body = content;    //郵件正文
            mail.BodyEncoding = Encoding.UTF8;  //正文編碼
            mail.IsBodyHtml = true; //設置為HTML格式
            mail.Priority = System.Net.Mail.MailPriority.High;  //優先級

            try
            {
                smtp.Send(mail);
                return 0;
            }
            catch (Exception ex)
            {
                string msg = ex.Message;
                return 1;
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //OK
            /*
            要寄Gmail信首先要登入Gmail，
            然後到 https://www.google.com/settings/security/lesssecureapps
            低安全性應用程式 → 開啟較低的應用程式存取權限
            選擇開啟，否則會無法正常寄信
            */

            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            //寄件者
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, System.Text.Encoding.UTF8);  //包含暱稱 與編碼
            //mail.From = new MailAddress(email_addr_from); //不包含暱稱

            /* 上面3個參數分別是發件人地址（可以隨便寫），發件人姓名，編碼*/
            //收件者
            mail.To.Add(email_addr_to);
            //mail.To.Add("....");  //可以發送給多人
            //副本
            mail.CC.Add(email_addr_cc);   //可以抄送副本給多人

            //高重要性
            mail.Priority = System.Net.Mail.MailPriority.Normal;

            //主旨
            mail.Subject = mail_subject + " case 1"; //郵件標題
            mail.SubjectEncoding = System.Text.Encoding.UTF8;//郵件標題編碼
            mail.Body = mail_body + DateTime.Now.ToString();   //郵件內容
            mail.BodyEncoding = System.Text.Encoding.UTF8;//郵件內容編碼 
            //附加檔案
            mail.Attachments.Add(new Attachment(attach_filename1));  //附件
            mail.IsBodyHtml = true;//是否是HTML郵件 
            //mail.Priority = MailPriority.High;//郵件優先級 

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = smtp_server_port;
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, email_addr_from_password); //這裡要填正確的帳號跟密碼

            richTextBox1.Text += "透過gmail寄信 ST 1\n";
            Application.DoEvents();
            try
            {
                smtp.Send(mail); //寄出信件
                smtp.Dispose();
                mail.Dispose();
                richTextBox1.Text += "透過gmail寄信 SP 1 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 1 NG\t訊息: " + ex.Message + "\n";
                richTextBox1.Text += "透過gmail寄信 SP 1 NG\t原因: " + ex.ToString() + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //OK
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, System.Text.Encoding.UTF8);  //包含暱稱 與編碼
            //mail.From = new MailAddress(email_addr_from); //不包含暱稱
            mail.To.Add(new MailAddress(email_addr_to));
            mail.Priority = System.Net.Mail.MailPriority.Normal;
            mail.Subject = mail_subject + " case 2";
            mail.Body = mail_body + DateTime.Now.ToString();
            mail.Attachments.Add(new Attachment(attach_filename1));  //附件

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = smtp_server_port;
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, email_addr_from_password); //這裡要填正確的帳號跟密碼

            richTextBox1.Text += "透過gmail寄信 ST 2\n";
            Application.DoEvents();
            try
            {
                smtp.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 2 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 2 NG\t訊息: " + ex.Message + "\n";
                richTextBox1.Text += "透過gmail寄信 SP 2 NG\t原因: " + ex.ToString() + "\n";
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //OK
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, System.Text.Encoding.UTF8);  //包含暱稱 與編碼
            //mail.From = new MailAddress(email_addr_from); //不包含暱稱
            mail.To.Add(email_addr_to);
            mail.Priority = System.Net.Mail.MailPriority.Normal;
            mail.Subject = mail_subject + " case 3";
            mail.SubjectEncoding = System.Text.Encoding.UTF8;
            mail.Body = mail_body + DateTime.Now.ToString();
            mail.BodyEncoding = System.Text.Encoding.UTF8;
            mail.IsBodyHtml = true;  //是否HTML

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = smtp_server_port;
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, email_addr_from_password); //這裡要填正確的帳號跟密碼

            richTextBox1.Text += "透過gmail寄信 ST 3\n";
            Application.DoEvents();
            try
            {
                smtp.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 3 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 3 NG\t訊息: " + ex.Message + "\n";
                richTextBox1.Text += "透過gmail寄信 SP 3 NG\t原因: " + ex.ToString() + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }
    }
}

