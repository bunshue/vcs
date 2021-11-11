using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net.Mail;


namespace WindowsFormsApplication1ccccc
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string random_str = RandomStringGenerator.GetRandomString();
            richTextBox1.Text += random_str + "\n";

        }

        /// <summary> 
        /// 生成隨機字符串
        /// </summary> 
        private class RandomStringGenerator
        {
            static readonly Random r = new Random();
            const string _chars = "0123456789";
            public static string GetRandomString()
            {
                char[] buffer = new char[5];
                for (int i = 0; i < 5; i++)
                {
                    buffer[i] = _chars[r.Next(_chars.Length)];
                }
                return new string(buffer);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string mailContent = "郵件內容";

            MailMessage msg = new System.Net.Mail.MailMessage();
            msg.To.Add("david@insighteyes.com"); //收件人

            //發件人信息
            msg.From = new MailAddress("bunshue@gmail.com", "發送人姓名", System.Text.Encoding.UTF8);
            msg.Subject = "這是測試郵件";   //郵件標題
            msg.SubjectEncoding = System.Text.Encoding.UTF8;    //標題編碼
            msg.Body = mailContent; //郵件主體
            msg.BodyEncoding = System.Text.Encoding.UTF8;
            msg.IsBodyHtml = true;  //是否HTML
            msg.Priority = MailPriority.High;   //優先級

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
    }
}

