using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;
using System.Net.Mail;  //for SmtpClient
using System.Xml;
using System.Web.Mail;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.Management;
using System.Diagnostics;
using Shell32;

namespace network_test3_mail
{
    public partial class Form1 : Form
    {
        string email_addr_from = "bunshue@gmail.com";
        string email_addr_from_nicknane = "王大頭";
        string email_addr_to = "david@insighteyes.com";
        string password = "jasmine0311wang";
        string mail_subject = "測試郵件標題";
        string mail_body = "郵件內容lion-mouse";
        string smtp_server = "smtp.gmail.com";
        string attach_filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
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
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //從 gmail 寄信到 ims
            richTextBox1.Text += "透過gmail寄信 ST 0\n";
            Application.DoEvents();
            int result = SendEmail(email_addr_from, password, new string[] { email_addr_to }, mail_subject + " case 0", mail_body + DateTime.Now.ToString(), smtp_server);
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
            //發件者郵箱地址
            string fjrtxt = sendEmailAddress;
            //發件者郵箱密碼
            string mmtxt = sendEmailPwd;
            string[] fasong = fjrtxt.Split('@');
            //設置郵件協議
            SmtpClient client = new SmtpClient(host);   //System.Net.Mail.SmtpClient
            client.UseDefaultCredentials = false;
            //通過網絡發送到Smtp服務器
            client.DeliveryMethod = SmtpDeliveryMethod.Network;
            //通過用戶名和密碼 認證
            client.Credentials = new NetworkCredential(fasong[0].ToString(), password);  //這裡要填正確的帳號跟密碼
            //QQ郵箱使用ssl加密，需要設置SmtpClient.EnableSsl 屬性為True表示“指定 SmtpClient 使用安全套接字層 (SSL) 加密連接。”
            client.EnableSsl = true;

            //發件人和收件人的郵箱地址
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.From = new MailAddress(fjrtxt);
            for (int i = 0; i < msgToEmail.Length; i++)
            {
                mail.To.Add(new MailAddress(msgToEmail[i]));
            }
            //郵件主題
            mail.Subject = title;
            //主題編碼
            mail.SubjectEncoding = Encoding.UTF8;
            //郵件正文
            mail.Body = content;
            //正文編碼
            mail.BodyEncoding = Encoding.UTF8;
            //設置為HTML格式
            mail.IsBodyHtml = true;
            //優先級
            mail.Priority = System.Net.Mail.MailPriority.High;

            try
            {
                client.Send(mail);
                return 0;
            }
            catch (Exception exss)
            {
                string msg = exss.Message;
                return 1;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            要寄Gmail信首先要登入Gmail，
            然後到 https://www.google.com/settings/security/lesssecureapps
            低安全性應用程式 → 開啟較低的應用程式存取權限
            選擇開啟，否則會無法正常寄信
            */

            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.To.Add(email_addr_to);
            //mail.To.Add("b@b.com");可以發送給多人
            //mail.CC.Add("c@c.com");
            //mail.CC.Add("c@c.com");可以抄送副本給多人 
            //這裡可以隨便填，不是很重要
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, System.Text.Encoding.UTF8);
            /* 上面3個參數分別是發件人地址（可以隨便寫），發件人姓名，編碼*/
            mail.Subject = mail_subject + " case 1"; //郵件標題
            mail.SubjectEncoding = System.Text.Encoding.UTF8;//郵件標題編碼
            mail.Body = mail_body + DateTime.Now.ToString();   //郵件內容
            mail.BodyEncoding = System.Text.Encoding.UTF8;//郵件內容編碼 
            mail.Attachments.Add(new Attachment(attach_filename));  //附件
            mail.IsBodyHtml = true;//是否是HTML郵件 
            //mail.Priority = MailPriority.High;//郵件優先級 

            SmtpClient client = new SmtpClient();
            client.Credentials = new System.Net.NetworkCredential(email_addr_from, password); //這裡要填正確的帳號跟密碼
            client.Host = smtp_server;  //設定smtp Server
            client.Port = 25; //設定Port
            client.EnableSsl = true; //gmail預設開啟驗證

            richTextBox1.Text += "透過gmail寄信 ST 1\n";
            Application.DoEvents();
            try
            {
                client.Send(mail); //寄出信件
                client.Dispose();
                mail.Dispose();
                richTextBox1.Text += "透過gmail寄信 SP 1 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 1 NG\t原因: " + ex.Message.ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();  //From在前, To在後
            mail.From = email_addr_from;
            mail.To = email_addr_to;

            //別名
            //mail.To = "\"John\" <me@mycompany.com>";
            //mail.From = "\"Tony Gong\" <you@yourcompany.com>";

            //多人
            //mail.To = "me@mycompany.com;him@hiscompany.com;her@hercompany.com";

            mail.Subject = mail_subject + " case 2";
            mail.BodyFormat = MailFormat.Html;
            //mail.Body = "this is my test email body";
            mail.Body = "this is my test email body.<br><b>this part is in bold</b>";
            //發送附件
            MailAttachment attachment = new MailAttachment(attach_filename); //create the attachment
            mail.Attachments.Add(attachment); //add the attachment

            //mail.Fields.Add("////authenticate", "");    //帳號, 密碼, PORT, SSL....


            /*
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = 587;
            //smtp.UseDefaultCredentials = false;
            smtp.EnableSsl = true;
            NetworkCredential nc = new NetworkCredential(email_addr_from, password);
            smtp.Credentials = nc;

            richTextBox1.Text += "透過gmail寄信 ST 2\n";
            Application.DoEvents();
            try
            {
                smtp.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 2 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 2 NG\t原因: " + ex.ToString() + "\n";
            }
            */


            System.Web.Mail.SmtpMail.SmtpServer = smtp_server;  //your real server goes here

            richTextBox1.Text += "透過gmail寄信 ST 2 NG fail\n";
            Application.DoEvents();
            try
            {
                System.Web.Mail.SmtpMail.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 2 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 2 NG\t原因: " + ex.Message.ToString() + "\n";
            }


            /*
            修改smtp服務器的端口，以及使用SSL加密
            大部分smtp服務器的端口是25，但有些卻不是
            同時，絕大部分Smtp服務器不需要SSL登陸，有些卻需要
            比如Gmail，smtp端口是：465，同時支持SSL
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "透過gmail寄信 ST 3 NG fail\n";
            Application.DoEvents();
            sendmail_net();
        }

        //c#如何發郵件?

        private void sendmail_net()
        {//.Net smtp類進行郵件發送，支持認證，附件添加；
            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();

            mail.From = email_addr_from;
            mail.To = email_addr_to;

            //mail.Body = this.tb_mailBody.Text.Trim();
            mail.Subject = mail_subject + " case 3";
            /* 附件的粘貼, ^_^,笨了點;
            if(this.att1.Value.ToString().Trim()!=string.Empty)
             mail.Attachments.Add(new System.Web.Mail.MailAttachment(this.att1.Value.ToString().Trim()));

            if(this.att2.Value.ToString().Trim()!=string.Empty)
             mail.Attachments.Add(new System.Web.Mail.MailAttachment(this.att2.Value.ToString().Trim()));
            if(this.att3.Value.ToString().Trim()!=string.Empty)
             mail.Attachments.Add(new System.Web.Mail.MailAttachment(this.att3.Value.ToString().Trim()));
            */
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate", "1");
            //是否需要驗證，一般是要的    
            mail.Fields.Add
             ("http://schemas.microsoft.com/cdo/configuration/sendusername", "gallon_han");
            //自己郵箱的用戶名    
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendpassWord", "218500");
            //自己郵箱的密碼 
            System.Web.Mail.SmtpMail.SmtpServer = smtp_server;  //your real server goes here

            richTextBox1.Text += "透過gmail寄信 ST 3\n";
            Application.DoEvents();
            try
            {
                System.Web.Mail.SmtpMail.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 3 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 3 NG\t原因: " + ex.ToString() + "\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            System.Web.Mail.MailPriority priority = System.Web.Mail.MailPriority.Normal;

            string body = mail_body + DateTime.Now.ToString();

            //, System.Collections.ArrayList files)

            //發送附件
            System.Collections.ArrayList files = new System.Collections.ArrayList();
            files.Add(attach_filename);

            richTextBox1.Text += "透過gmail寄信 ST 4 NG\n";
            Application.DoEvents();
            sendTxtMail(email_addr_from, password, email_addr_to, mail_subject + " case 4", priority, body, smtp_server, files);
        }

        public void sendTxtMail(string from, string pass, string to, string subject, System.Web.Mail.MailPriority priority, string body, string smtpServer, System.Collections.ArrayList files)
        {
            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();
            mail.From = from;
            mail.To = to;
            mail.Subject = subject;
            mail.Priority = priority;
            mail.BodyFormat = System.Web.Mail.MailFormat.Text;
            mail.Body = body;
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate", "1"); //basic authentication
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendusername", from.Substring(0, from.IndexOf("@"))); //set your username here
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendpassword", pass); //set your passWord here
            for (int i = 0; i < files.Count; i++)
            {
                if (System.IO.File.Exists(files[i].ToString()))
                {
                    mail.Attachments.Add(new MailAttachment(files[i].ToString()));
                }
            }
            SmtpMail.SmtpServer = smtpServer;


            richTextBox1.Text += "透過gmail寄信 ST\n";
            Application.DoEvents();
            try
            {
                SmtpMail.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP NG\t原因: " + ex.ToString() + "\n";
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }

        public void sendHtmlMail(string from, string pass, string to, string subject, System.Web.Mail.MailPriority priority, string body, string smtpServer, System.Collections.ArrayList files)
        {
            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();
            mail.From = from;
            mail.To = to;
            mail.Subject = subject;
            mail.Priority = priority;
            mail.BodyFormat = System.Web.Mail.MailFormat.Html;
            mail.Body = body;
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate", "1"); //basic authentication
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendusername", from.Substring(0, from.IndexOf("@"))); //set your username here
            mail.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendpassword", pass); //set your passWord here
            for (int i = 0; i < files.Count; i++)
            {
                if (System.IO.File.Exists(files[i].ToString()))
                {
                    mail.Attachments.Add(new MailAttachment(files[i].ToString()));
                }
            }
            System.Web.Mail.SmtpMail.SmtpServer = smtpServer;

            richTextBox1.Text += "透過gmail寄信 ST\n";
            Application.DoEvents();
            try
            {
                System.Web.Mail.SmtpMail.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP NG\t原因: " + ex.ToString() + "\n";
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            System.Net.Mail.MailPriority priority = System.Net.Mail.MailPriority.Normal;

            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();  //From在前, To在後
            //System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();  //From在前, To在後

            mail.From = email_addr_from;
            mail.To = email_addr_to;

            //多個收件者
            //mail.To(email_addr_to);
            //mail.To("Secondry@gmail.com");

            mail.Subject = mail_subject + " case 5";
            mail.Body = mail_body + DateTime.Now.ToString();
            //mail..IsBodyHtml = true;
            SmtpClient smtp = new SmtpClient(smtp_server, 587);
            // smtp.Host = smtp_server; //Or Your SMTP Server Address
            smtp.EnableSsl = true;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, password);
            //smtp.Port = 587;
            //Or your Smtp Email ID and Password
            smtp.UseDefaultCredentials = false;
            // smtp.EnableSsl = true;
            //smtp.Send(mail);

            //System.Web.Mail.SmtpMail.SmtpServer = smtp_server;  //your real server goes here

            richTextBox1.Text += "透過gmail寄信 ST 5 NG fail\n";
            Application.DoEvents();
            try
            {
                System.Web.Mail.SmtpMail.Send(mail);
                //smtp.Send(System.Net.Mail mail);
                //smtp.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 5 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 5 NG\t原因: " + ex.ToString() + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            System.Net.Mail.MailPriority priority = System.Net.Mail.MailPriority.Normal;
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.Subject = mail_subject + " case 6";
            mail.From = new MailAddress(email_addr_from);
            mail.To.Add(new MailAddress(email_addr_to));
            mail.Body = mail_body + DateTime.Now.ToString();
            mail.Attachments.Add(new Attachment(attach_filename));  //附件

            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = 587;
            //smtp.UseDefaultCredentials = false;
            smtp.EnableSsl = true;
            NetworkCredential nc = new NetworkCredential(email_addr_from, password);
            smtp.Credentials = nc;

            richTextBox1.Text += "透過gmail寄信 ST 6\n";
            Application.DoEvents();
            try
            {
                smtp.Send(mail);
                richTextBox1.Text += "透過gmail寄信 SP 6 OK\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "透過gmail寄信 SP 6 NG\t原因: " + ex.ToString() + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //using System.Net.Mail;

            string mailContent = "郵件內容";

            System.Net.Mail.MailMessage msg = new System.Net.Mail.MailMessage();
            msg.To.Add("david@insighteyes.com"); //收件人

            //發件人信息
            msg.From = new MailAddress("bunshue@gmail.com", "發送人姓名", System.Text.Encoding.UTF8);
            msg.Subject = "這是測試郵件";   //郵件標題
            msg.SubjectEncoding = System.Text.Encoding.UTF8;    //標題編碼
            msg.Body = mailContent; //郵件主體
            msg.BodyEncoding = System.Text.Encoding.UTF8;
            msg.IsBodyHtml = true;  //是否HTML
            msg.Priority = System.Net.Mail.MailPriority.High;   //優先級

            SmtpClient client = new SmtpClient();
            //設置GMail郵箱和密碼 
            client.Credentials = new System.Net.NetworkCredential("bunshue@gmail.com", "pwd");
            client.Port = 587;
            client.Host = "smtp.gmail.com";
            client.EnableSsl = true;
            object userState = msg;
            try
            {
                client.Send(msg);
                MessageBox.Show("發送成功");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "發送郵件出錯");
            } 

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

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }
    }

    /*
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }
    */
}
