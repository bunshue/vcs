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
            MailMessage mmsg = new MailMessage();
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
            mmsg.Priority = MailPriority.High;
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

        }

        private void button3_Click(object sender, EventArgs e)
        {

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
}

