using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Net.Mail;  //for SmtpClient
using System.Xml;
using System.Web.Mail;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

using System.Diagnostics;

namespace network_test3_mail
{
    public partial class Form1 : Form
    {

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
            int result = SendEmail("bunshue@gmail.com", "j0w", new string[] { "david@insighteyes.com" }, "測試標題2222", "測試內容", "smtp.gmail.com");
            if (result == 0)
            {
                richTextBox1.Text += "寄信 OK\n";
            }
            else
            {
                richTextBox1.Text += "寄信 NG\n";
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

        public static int SendEmail(string sendEmailAddress, string sendEmailPwd, string[] msgToEmail, string title, string content, string host)
        {
            //發件者郵箱地址
            string fjrtxt = sendEmailAddress;
            //發件者郵箱密碼
            string mmtxt = sendEmailPwd;
            //主題
            string zttxt = title;
            //內容
            string nrtxt = content;
            string[] fasong = fjrtxt.Split('@');
            //設置郵件協議
            SmtpClient client = new SmtpClient(host);   //System.Net.Mail.SmtpClient
            client.UseDefaultCredentials = false;
            //通過網絡發送到Smtp服務器
            client.DeliveryMethod = SmtpDeliveryMethod.Network;
            //通過用戶名和密碼 認證
            client.Credentials = new NetworkCredential(fasong[0].ToString(), mmtxt);  //System.Net.NetworkCredential
            //QQ郵箱使用ssl加密，需要設置SmtpClient.EnableSsl 屬性為True表示“指定 SmtpClient 使用安全套接字層 (SSL) 加密連接。”
            client.EnableSsl = true;

            //發件人和收件人的郵箱地址
            System.Net.Mail.MailMessage mmsg = new System.Net.Mail.MailMessage();
            mmsg.From = new MailAddress(fjrtxt);
            for (int i = 0; i < msgToEmail.Length; i++)
            {
                mmsg.To.Add(new MailAddress(msgToEmail[i]));
            }
            //郵件主題
            mmsg.Subject = zttxt;
            //主題編碼
            mmsg.SubjectEncoding = Encoding.UTF8;
            //郵件正文
            mmsg.Body = nrtxt;
            //正文編碼
            mmsg.BodyEncoding = Encoding.UTF8;
            //設置為HTML格式
            mmsg.IsBodyHtml = true;
            //優先級
            mmsg.Priority = System.Net.Mail.MailPriority.High;
            try
            {
                client.Send(mmsg);
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

            try
            {
                System.Net.Mail.MailMessage msg = new System.Net.Mail.MailMessage();
                msg.To.Add("david@insighteyes.com");
                //msg.To.Add("b@b.com");可以發送給多人
                //msg.CC.Add("c@c.com");
                //msg.CC.Add("c@c.com");可以抄送副本給多人 
                //這裡可以隨便填，不是很重要
                msg.From = new MailAddress("bunshue@gmail.com", "小魚", System.Text.Encoding.UTF8);
                /* 上面3個參數分別是發件人地址（可以隨便寫），發件人姓名，編碼*/
                msg.Subject = "測試標題333";//郵件標題
                msg.SubjectEncoding = System.Text.Encoding.UTF8;//郵件標題編碼
                msg.Body = "測試一下"; //郵件內容
                msg.BodyEncoding = System.Text.Encoding.UTF8;//郵件內容編碼 
                msg.Attachments.Add(new Attachment(@"C:\______test_files\picture1.jpg"));  //附件
                msg.IsBodyHtml = true;//是否是HTML郵件 
                //msg.Priority = MailPriority.High;//郵件優先級 

                SmtpClient client = new SmtpClient();
                client.Credentials = new System.Net.NetworkCredential("bunshue@gmail.com", "j0w"); //這裡要填正確的帳號跟密碼
                client.Host = "smtp.gmail.com"; //設定smtp Server
                client.Port = 25; //設定Port
                client.EnableSsl = true; //gmail預設開啟驗證
                client.Send(msg); //寄出信件
                client.Dispose();
                msg.Dispose();
                MessageBox.Show(this, "郵件寄送成功！");
            }
            catch (Exception ex)
            {
                MessageBox.Show(this, ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();  //From在前, To在後
            mail.From = "bunshue@gmail.com";
            mail.To = "david@insighteyes.com";

            //別名
            //mail.To = "\"John\" <me@mycompany.com>";
            //mail.From = "\"Tony Gong\" <you@yourcompany.com>";

            //多人
            //mail.To = "me@mycompany.com;him@hiscompany.com;her@hercompany.com";

            mail.Subject = "this is a test email.";
            mail.BodyFormat = MailFormat.Html;
            //mail.Body = "this is my test email body";
            mail.Body = "this is my test email body.<br><b>this part is in bold</b>";
            //發送附件
            string filename = @"C:\______test_files\picture1.jpg";
            MailAttachment attachment = new MailAttachment(filename); //create the attachment
            mail.Attachments.Add(attachment); //add the attachment

            //mail.Fields.Add("////authenticate", "");    //帳號, 密碼, PORT, SSL....


            System.Web.Mail.SmtpMail.SmtpServer = "smtp.gmail.com";  //your real server goes here
            System.Web.Mail.SmtpMail.Send(mail);


            /*
            修改smtp服務器的端口，以及使用SSL加密
            大部分smtp服務器的端口是25，但有些卻不是
            同時，絕大部分Smtp服務器不需要SSL登陸，有些卻需要
            比如Gmail，smtp端口是：465，同時支持SSL
            */
        }

        private void button3_Click(object sender, EventArgs e)
        {
            sengmill_net();

        }

        //c#如何發郵件?

        private void sengmill_net()
        {//.Net smtp類進行郵件發送，支持認證，附件添加；
            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();

            mail.From = "bunshue@gmail.com";
            mail.To = "david@insighteyes.com";

            //mail.Body = this.tb_mailBody.Text.Trim();
            mail.Subject = "test mail from hz";
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
            System.Web.Mail.SmtpMail.SmtpServer = "smtp.gmail.com";  //your real server goes here
            System.Web.Mail.SmtpMail.Send(mail);
        }


        private void button4_Click(object sender, EventArgs e)
        {
            string from = "bunshue@gmail.com";

            string pass = "pass";
            string to = "david@insighteyes.com";

            string subject = "test mail from hz";

            System.Web.Mail.MailPriority priority = System.Web.Mail.MailPriority.Normal;

            string body = "this is a lion-mouse.";

            string smtpServer = "smtp.gmail.com";


            //, System.Collections.ArrayList files)


            //發送附件
            string filename = @"C:\______test_files\picture1.jpg";

            System.Collections.ArrayList files = new System.Collections.ArrayList();
            files.Add(filename);

            sendTxtMail(from, pass, to, subject, priority, body, smtpServer, files);

        }



        public void sendTxtMail(string from, string pass, string to, string subject, System.Web.Mail.MailPriority priority, string body, string smtpServer, System.Collections.ArrayList files)
        {
            System.Web.Mail.MailMessage msg = new System.Web.Mail.MailMessage();
            msg.From = from;
            msg.To = to;
            msg.Subject = subject;
            msg.Priority = priority;
            msg.BodyFormat = System.Web.Mail.MailFormat.Text;
            msg.Body = body;
            msg.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate", "1"); //basic authentication
            msg.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendusername", from.Substring(0, from.IndexOf("@"))); //set your username here
            msg.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendpassword", pass); //set your passWord here
            for (int i = 0; i < files.Count; i++)
            {
                if (System.IO.File.Exists(files[i].ToString()))
                {
                    msg.Attachments.Add(new MailAttachment(files[i].ToString()));
                }
            }
            SmtpMail.SmtpServer = smtpServer;
           
            try
            {
                SmtpMail.Send(msg);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }

        public void sendHtmlMail(string from, string pass, string to, string subject, System.Web.Mail.MailPriority priority, string body, string smtpServer, System.Collections.ArrayList files)
        {
            System.Web.Mail.MailMessage msg = new System.Web.Mail.MailMessage();
            msg.From = from;
            msg.To = to;
            msg.Subject = subject;
            msg.Priority = priority;
            msg.BodyFormat = System.Web.Mail.MailFormat.Html;
            msg.Body = body;
            msg.Fields.Add("http://schemas.microsoft.com/cdo/configuration/smtpauthenticate", "1"); //basic authentication
            msg.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendusername", from.Substring(0, from.IndexOf("@"))); //set your username here
            msg.Fields.Add("http://schemas.microsoft.com/cdo/configuration/sendpassword", pass); //set your passWord here
            for (int i = 0; i < files.Count; i++)
            {
                if (System.IO.File.Exists(files[i].ToString()))
                {
                    msg.Attachments.Add(new MailAttachment(files[i].ToString()));
                }
            }
            System.Web.Mail.SmtpMail.SmtpServer = smtpServer;
            System.Web.Mail.SmtpMail.Send(msg);
        }



        private void button5_Click(object sender, EventArgs e)
        {

            string from = "bunshue@gmail.com";

            string pass = "pass";
            string to = "david@insighteyes.com";

            string subject = "test mail from hz";

            System.Net.Mail.MailPriority priority = System.Net.Mail.MailPriority.Normal;

            string body = "this is a lion-mouse.";

            string smtpServer = "smtp.gmail.com";

            System.Web.Mail.MailMessage mail = new System.Web.Mail.MailMessage();  //From在前, To在後
            //System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();  //From在前, To在後

            mail.From = "bunshue@gmail.com";
            mail.To = "david@insighteyes.com";

            
            //mail.To("david@insighteyes.com");
            //mail.To("Secondry@gmail.com");
            mail.From = from;
            mail.Subject = subject;
            string Body = body;
            mail.Body = Body;
            //mail..IsBodyHtml = true;
            SmtpClient smtp = new SmtpClient("smtp.gmail.com", 587);
            // smtp.Host = "smtp.gmail.com"; //Or Your SMTP Server Address
            smtp.EnableSsl = true;
            smtp.Credentials = new System.Net.NetworkCredential(from, pass);
            //smtp.Port = 587;
            //Or your Smtp Email ID and Password
            smtp.UseDefaultCredentials = false;
            // smtp.EnableSsl = true;
            //smtp.Send(mail);

            //System.Web.Mail.SmtpMail.SmtpServer = "smtp.gmail.com";  //your real server goes here
            System.Web.Mail.SmtpMail.Send(mail);

            //smtp.Send(System.Net.Mail mail);
            //smtp.Send(mail);



        }

        private void button6_Click(object sender, EventArgs e)
        {
            string from = "bunshue@gmail.com";

            string pass = "pass";
            string to = "david@insighteyes.com";

            string subject = "test mail from hz";

            System.Net.Mail.MailPriority priority = System.Net.Mail.MailPriority.Normal;

            string body = "this is a lion-mouse.";

            string smtpServer = "smtp.gmail.com";



            System.Net.Mail.MailMessage msg = new System.Net.Mail.MailMessage();
            msg.Subject = subject;
            msg.From = new MailAddress(from);
            msg.Body = "Message BODY";
            msg.To.Add(new MailAddress(to));
            SmtpClient smtp = new SmtpClient();
            smtp.Host = "smtp.gmail.com";
            smtp.Port = 587;
            //smtp.UseDefaultCredentials = false;
            smtp.EnableSsl = true;
            NetworkCredential nc = new NetworkCredential(from, pass);
            smtp.Credentials = nc;

            try
            {
                smtp.Send(msg);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Message not emailed: " + ex.ToString() + "\n";
            }



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

