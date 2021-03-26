using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser4
{
    public partial class Form1 : Form
    {
        bool loading = true;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //for (int I = 0; I <= 25; I++)
            {
                //richTextBox1.Text += I.ToString() + "\n";
                loading = true;

                //假設Google有http://www.google.com?Hello=A,http://www.google.com?Hello=B,http://www.google.com?Hello=C....等26個網頁

                //就用迴圈去跑，當網頁讀進來完成之後，便會觸發到下面的Navigated事件

                //(DocumentCompleted事件的話常常會有問題，因為如果網頁下載不完全就會當在那邊)
                //webBrowser1.Navigate("http://www.google.com?Hello=" + Convert.ToChar(65 + I));

                string url = "http://antwrp.gsfc.nasa.gov/apod/";

                webBrowser1.Navigate(url);

                //跑到這因為loading還是true的關係，會一直跑下面這個迴圈

                //而Application.DoEvents();是讓程式在跑迴圈時還能去傾聽其他的事件
                while (loading)
                {
                    Application.DoEvents();
                    //richTextBox1.Text += ".";
                }

            }

        }

        private void webBrowser1_Navigated(object sender, WebBrowserNavigatedEventArgs e)
        {
            //放個計時器，等待一下網頁下載回來
            timer1.Start();
        }

        private void webBrowser1_NewWindow(object sender, CancelEventArgs e)
        {
            //這行就是讓多跳出的新視窗跳不出來 =.="

            e.Cancel = true;

        }

        //等待完後就開始擷取網頁資料
        private void timer1_Tick(object sender, EventArgs e)
        {
            timer1.Stop();

            //這邊使用的是一種叫做DOM的技術，DOM是Document Object Model          
            HtmlDocument doc = webBrowser1.Document;

            for (int i = 0; i < doc.All.Count; i++)
            {

                //去抓標籤名字有a的，像是連結<a href=xx>這種

                //奇怪的是這個方法如果要抓一些標籤都抓不到，像是<td><tr>那些=.=

                //所以那些我是用另外的方法抓的，等下會講
                if (doc.All[i].TagName.ToLower().Equals("a"))
                {

                    //GetAttribute就是去取得標籤的屬性的內容，例：

                    //<a href ="我是屬性的內容" target=_blank>，不過有些屬性取不到，像是class

                    if (doc.All[i].GetAttribute("href").Contains("imaddddge"))
                    {                             //InnerText就是取得標籤中間的內容，<標籤>內容</標籤>
                        richTextBox1.AppendText(doc.All[i].InnerText);
                        richTextBox1.AppendText(doc.All[i].GetAttribute("href"));
                        richTextBox1.AppendText(Environment.NewLine);

                        //另外這個函式可以去更改HTML裡面屬性的內容
                        //XXX.SetAttribute("value", "Hello");

                    }
                }
            }
            for (int i = 0; i < doc.All.Count; i++)
            {
                //richTextBox1.Text += doc.All[i]. + "\n";
            }
            richTextBox1.Text += "done\n";
            loading = false;

        }



    }
}
