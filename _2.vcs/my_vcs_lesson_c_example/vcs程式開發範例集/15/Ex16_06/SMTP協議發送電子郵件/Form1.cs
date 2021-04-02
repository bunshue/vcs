using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net.Mail;
//using System.IO;
//using System.Net;


namespace SMTP協議發送電子郵件
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
        MailMessage Mail;
        SmtpClient Client;
        public  void CreateTimeoutTestMessage(string server)
        {
            try
            {
                //實例MailMessage類
                Mail = new MailMessage(this.txtFrom.Text, this.txtGet.Text);
                Mail.Subject =this.txtSubject.Text.Trim().ToString();
                Mail.Body = this.richTextBox1.Text.Trim().ToString();
                Client = new SmtpClient(server, 25);//實例一個SmtpClient類
                Client.Send(Mail);
                MessageBox.Show("郵件發送成功！！！");
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (this.richTextBox1.Text.Trim().ToString() != "")
            {
                CreateTimeoutTestMessage("hywork");//參數傳的是POP３服務器的名稱
            }
            else
            {
                MessageBox.Show("請認真填寫郵件！");
                return;
            }
        }
    }
}