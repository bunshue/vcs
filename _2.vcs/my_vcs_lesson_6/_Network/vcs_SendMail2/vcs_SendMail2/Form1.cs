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
using System.Xml;
using System.Net.Mail;  //for SmtpClient
//using System.Web.Mail;  //據說不推薦使用了
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.Management;
using System.Diagnostics;

using Shell32;

namespace vcs_SendMail2
{
    public partial class Form1 : Form
    {
        string email_addr_from = "bunshue@gmail.com";
        string password = "";
        string email_addr_from_nicknane = "王大頭";
        string email_addr_to = "david@insighteyes.com";
        string email_addr_cc = "bunshue@gmail.com";
        System.Net.Mail.MailPriority priority = System.Net.Mail.MailPriority.Normal;

        string mail_subject = "測試郵件標題";
        string mail_body = "郵件內容lion-mouse";
        string smtp_server = "smtp.gmail.com";
        string attach_filename = @"C:\______test_files\picture1.jpg";

        string addr_from_pw = string.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;

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
                addr_from_pw = kk;
                password = addr_from_pw;
            }
            else
            {
                addr_from_pw = "xxxx";

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
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
            //OK
            //發件者郵箱地址
            string fjrtxt = sendEmailAddress;
            //發件者郵箱密碼
            string mmtxt = sendEmailPwd;
            string[] fasong = fjrtxt.Split('@');

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = 25;
            //QQ郵箱使用ssl加密，需要設置SmtpClient.EnableSsl 屬性為True表示“指定 SmtpClient 使用安全套接字層 (SSL) 加密連接。”
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            //通過網絡發送到Smtp服務器
            smtp.DeliveryMethod = SmtpDeliveryMethod.Network;
            //通過用戶名和密碼 認證
            smtp.Credentials = new NetworkCredential(fasong[0].ToString(), password);  //這裡要填正確的帳號跟密碼

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

        private void button1_Click(object sender, EventArgs e)
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
            mail.Attachments.Add(new Attachment(attach_filename));  //附件
            mail.IsBodyHtml = true;//是否是HTML郵件 
            //mail.Priority = MailPriority.High;//郵件優先級 

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = 25;
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, password); //這裡要填正確的帳號跟密碼

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

        private void button2_Click(object sender, EventArgs e)
        {
            //OK
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, System.Text.Encoding.UTF8);  //包含暱稱 與編碼
            //mail.From = new MailAddress(email_addr_from); //不包含暱稱
            mail.To.Add(new MailAddress(email_addr_to));
            mail.Priority = System.Net.Mail.MailPriority.Normal;
            mail.Subject = mail_subject + " case 2";
            mail.Body = mail_body + DateTime.Now.ToString();
            mail.Attachments.Add(new Attachment(attach_filename));  //附件

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = 25;
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, password); //這裡要填正確的帳號跟密碼

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

        private void button3_Click(object sender, EventArgs e)
        {
            //OK
            System.Net.Mail.MailMessage mail = new System.Net.Mail.MailMessage();
            mail.From = new MailAddress(email_addr_from, email_addr_from_nicknane, System.Text.Encoding.UTF8);  //包含暱稱 與編碼
            //mail.From = new MailAddress(email_addr_from); //不包含暱稱
            mail.To.Add(email_addr_to);
            mail.Priority = System.Net.Mail.MailPriority.Normal;
            mail.Subject = mail_subject + " case 7";
            mail.SubjectEncoding = System.Text.Encoding.UTF8;
            mail.Body = mail_body + DateTime.Now.ToString();
            mail.BodyEncoding = System.Text.Encoding.UTF8;
            mail.IsBodyHtml = true;  //是否HTML

            //SMTP 外寄郵件伺服器設定
            SmtpClient smtp = new SmtpClient();
            smtp.Host = smtp_server;
            smtp.Port = 25;
            smtp.EnableSsl = true; //gmail預設開啟驗證
            smtp.UseDefaultCredentials = false;
            smtp.Credentials = new System.Net.NetworkCredential(email_addr_from, password); //這裡要填正確的帳號跟密碼

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

        private void button4_Click(object sender, EventArgs e)
        {
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
