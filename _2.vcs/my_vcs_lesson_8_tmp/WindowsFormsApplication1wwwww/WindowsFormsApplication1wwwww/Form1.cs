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
                result = sr.ReadToEnd();        //一次讀完全部
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
            string tmp = reader.ReadToEnd();

            //關閉連線
            response.Close();

            //顯示回應資訊
            richTextBox1.Text += tmp + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "文天祥過零丁洋\n";
            richTextBox1.Text += "辛苦遭逢起一經\n";
            richTextBox1.Text += "干戈寥落四周星\n";
            richTextBox1.Text += "山河破碎風飄絮\n";
            richTextBox1.Text += "身世浮沉雨打萍\n";
            richTextBox1.Text += "惶恐灘頭說惶恐\n";
            richTextBox1.Text += "零丁洋裏歎零丁\n";
            richTextBox1.Text += "人生自古誰無死\n";
            richTextBox1.Text += "留取丹心照汗青";





        }

        private void button6_Click(object sender, EventArgs e)
        {
            //richTextBox2.Text += "There are " + richTextBox1.Lines.Length.ToString() + " lines in richtextBox1\n";
            //Array.Sort(richTextBox1.Lines);   //useless
            string[] temp = richTextBox1.Lines;
            Array.Sort(temp);
            richTextBox1.Lines = temp;

        }

        private void button7_Click(object sender, EventArgs e)
        {
            string[] temp = richTextBox1.Lines;
            double[] randomIndex = new double[temp.Length];
            Random r = new Random();
            for (int i = 0; i < temp.Length; i++)
            {
                randomIndex[i] = r.NextDouble();
            }
            Array.Sort(randomIndex, temp);
            richTextBox1.Lines = temp;
        }

        //C# richTextBox 按ctrl+a全選 
        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A)
                ((RichTextBox)sender).SelectAll();
        }
    }
}
