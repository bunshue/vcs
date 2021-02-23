using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

using System.IO;


namespace WindowsFormsApplication1wwwww
{
    public partial class Form1 : Form
    {
        bool finished;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            finished = false;
            webBrowser1.Navigate("https://tw.yahoo.com/");
        }

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            richTextBox1.Text += "讀取中...\n";
            if (webBrowser1.ReadyState < WebBrowserReadyState.Complete || finished == true) return;
            finished = true;
            richTextBox1.Text += "讀取完成\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string result = null;
            string Url = "http://easun.org/perl/perl-toc/ch04.html";
            HttpWebRequest request = HttpWebRequest.Create(Url) as HttpWebRequest;
            request.Method = "GET";

            using (WebResponse response = request.GetResponse())
            {
                StreamReader sr = new StreamReader(response.GetResponseStream());
                result = sr.ReadToEnd();        //讀取所有文字內容
                sr.Close();
            }
            richTextBox1.Text += result + "\n";


        }

        private void button4_Click(object sender, EventArgs e)
        {

            //要取得的網址
            Uri uri = new Uri("http://easun.org/perl/perl-toc/ch04.html");

            //建立request
            HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(uri);

            //在request Header加入認證字串
            request.Headers.Add("Authorization", "Basic " + Convert.ToBase64String(new ASCIIEncoding().GetBytes("admin:admin")));

            //實際發送請求，並取回回應資訊
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();

            //建立讀取串流
            StreamReader reader = new StreamReader(response.GetResponseStream());

            //將串流轉字串
            string tmp = reader.ReadToEnd();	//讀取所有文字內容

            //關閉連線
            response.Close();

            //顯示回應資訊
            richTextBox1.Text += tmp + "\n";

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

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();

        }


    }
}
