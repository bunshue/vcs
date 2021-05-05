using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;       //for NetworkCredential     NetworkCredential ：這個類別可用來提供密碼架構的驗證 (Authentication) 機制的認證。
using System.Net.Mail;  //for MailMessage
using System.Net.Mime;  //for MediaTypeNames

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
        public Form1()
        {
            InitializeComponent();
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
            string mail_server = "smtp.gmail.com";//POP３服務器的名稱
            string addr_from = "bunshue@gmail.com";
            string addr_to = "David@insighteyes.com";
            string subject = "主旨 : 用vcs寄信 用gmail寄信 1";
            string filename = @"C:\______test_files\picture1.jpg";
            string filename2 = @"C:\______test_files\__RW\_excel\2006年圖書銷售情況.xls";
            try
            {
                //MailMessage mail = new MailMessage(addr_from, addr_to, subject, "郵件內容(Body)");   //一次寫完
                MailMessage mail = new MailMessage();    //實例一個MailMessage類
                //mail.BodyEncoding  //郵件編碼方式
                mail.Priority = MailPriority.High;   //設定電子郵件的優先順序

                //mail.From = new MailAddress(addr_from);
                //mail.From = new MailAddress(addr_from, "寄件者的自稱"); //email, 顯示名稱
                mail.From = new MailAddress(addr_from, "寄件者的自稱", System.Text.Encoding.UTF8); //email, 顯示名稱, 編碼
                //mail.From = new MailAddress("lion.mouse.cat.dog", "寄件者的自稱"); //email, 顯示名稱    不能亂寫

                //mail.To.Add(addr_to);
                mail.To.Add(new MailAddress(addr_to, "尊敬的收件者1"));
                mail.To.Add(new MailAddress(addr_to, "尊敬的收件者2"));

                //副本、密件副本
                mail.CC.Add(new MailAddress(addr_to, "副本"));
                mail.Bcc.Add(new MailAddress(addr_to, "密件副本"));

                mail.Subject = subject; //郵件標題
                mail.SubjectEncoding = System.Text.Encoding.UTF8;//郵件標題編碼
                
                //mail.Body = ....      //郵件內容
                //mail.Body = "莫聽穿林打葉聲，何妨吟嘯且徐行。竹杖芒鞋輕勝馬，誰怕？一蓑煙雨任平生。料峭春風吹酒醒，微冷，山頭斜照卻相迎。回首向來蕭瑟處，歸去，也無風雨也無晴。";
                mail.Body = richTextBox_mail.Text;
                mail.BodyEncoding = System.Text.Encoding.UTF8;//郵件內容編碼 
                mail.IsBodyHtml = true; //是否是HTML郵件 
                mail.ReplyToList.Add(new MailAddress("David@insighteyes.com", "receiver"));

                /*
                //附加檔案 寫法 1
                Attachment attachment = new Attachment(filename);
                mail.Attachments.Add(attachment);
                */

                //附加檔案 寫法 2
                Attachment data = new Attachment(filename2, MediaTypeNames.Application.Octet);
                ContentDisposition disposition = data.ContentDisposition;
                disposition.CreationDate = System.IO.File.GetCreationTime(filename2);
                disposition.ModificationDate = System.IO.File.GetLastWriteTime(filename2);
                disposition.ReadDate = System.IO.File.GetLastAccessTime(filename2);
                mail.Attachments.Add(data);

                //附加檔案 寫法 3
                mail.Attachments.Add(new Attachment(filename));

                SmtpClient client = new SmtpClient();   //實例一個SmtpClient類

                //client.Credentials = CredentialCache.DefaultNetworkCredentials;   //不可, 需要驗證寄件者
                client.Credentials = new NetworkCredential("bunshue@gmail.com", "jasmine0311wang");   //驗證寄件者
                client.Host = mail_server;  //設定smtp Server
                client.Port = 25; //設定Port  //指定 SMTP 交易連接埠
                client.EnableSsl = true;  //是否啟用 SSL    gmail預設開啟驗證
                SendMail(client, mail); //包一層 看寄信結果
                client.Dispose();
                mail.Dispose();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "郵件寄送失敗, 原因 : " + ex.Message + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //用gmail寄信
            string mail_server = "smtp.gmail.com";//POP３服務器的名稱
            MailMessage mail;
            SmtpClient client;
            string addr_from = "bunshue@gmail.com";
            string addr_to = "David@insighteyes.com";
            string subject = "主旨 : 用vcs寄信 用gmail寄信 2";
            try
            {
                mail = new MailMessage(addr_from, addr_to);  //實例一個MailMessage類
                mail.Subject = subject;
                mail.Body = richTextBox_mail.Text;
                using (client = new SmtpClient(mail_server, 25)) //實例一個SmtpClient類
                {
                    client.Credentials = new NetworkCredential("bunshue@gmail.com", "jasmine0311wang");
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
    }
}
