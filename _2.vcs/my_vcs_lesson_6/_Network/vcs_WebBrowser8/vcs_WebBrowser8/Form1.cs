using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser8
{
    public partial class Form1 : Form
    {
        bool flag_loading = true;
        bool flag_finished = false;

        int flag_use_method = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            flag_use_method = 1;
            for (int i = 0; i <= 25; i++)
            {
                flag_loading = true;

                //假設Google有http://www.google.com?Hello=A,http://www.google.com?Hello=B,http://www.google.com?Hello=C....等26個網頁

                //就用迴圈去跑，當網頁讀進來完成之後，便會觸發到下面的Navigated事件

                //(DocumentCompleted事件的話常常會有問題，因為如果網頁下載不完全就會當在那邊)
                webBrowser1.Navigate("http://www.google.com?Hello=" + Convert.ToChar(65 + i));
                flag_finished = false;

                //跑到這因為loading還是true的關係，會一直跑下面這個迴圈

                //而Application.DoEvents();是讓程式在跑迴圈時還能去傾聽其他的事件
                while (flag_loading == true)
                {
                    Application.DoEvents();
                }
            }
        }

        private void webBrowser1_Navigated(object sender, WebBrowserNavigatedEventArgs e)
        {
            if (flag_use_method == 1)
            {
                timer1.Start();
            }
        }

        /*
        WebBrowserReadyState的五種狀況
        Complete 	控制項已完成新文件和其所有內容的載入。 
        Interactive 	控制項已載入文件足夠多的部分，可進行有限的使用者互動，例如按一下已顯示的超連結。 
        Loaded 	控制項已載入並初始化新文件，但是尚未收到所有的文件資料。 
        Loading 	控制項正在載入新文件。 
        Uninitialized 	目前未載入任何文件。 
        */

        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            richTextBox1.Text += "webBrowser1_DocumentCompleted, state = " + webBrowser1.ReadyState.ToString() + "\n";

            //雖然webBrowser讀取完成會觸發事件DocumentCompleted, 但實際上卻不斷重複執行,
            //使用ReadyState及1個變數判斷是否已執行完成, 即可避免重複執行.
            if (webBrowser1.ReadyState < WebBrowserReadyState.Complete || flag_finished == true)
            {
                return;
            }
            flag_finished = true;

            if (webBrowser1.ReadyState == WebBrowserReadyState.Complete)
            {
                //在此範圍中寫下你要在載入完成後做的事件
            }
        }

        //這是webbrowser1的"事件"，當跳出新視窗時要做什麼
        private void webBrowser1_NewWindow(object sender, CancelEventArgs e)
        {
            //這行就是讓多跳出的新視窗跳不出來
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

                    if (doc.All[i].GetAttribute("href").Contains("abc"))
                    {                             //InnerText就是取得標籤中間的內容，<標籤>內容</標籤>
                        richTextBox1.AppendText(doc.All[i].InnerText);
                        richTextBox1.AppendText(doc.All[i].GetAttribute("href"));
                        richTextBox1.AppendText(Environment.NewLine);

                        //另外這個函式可以去更改HTML裡面屬性的內容
                        //XXX.SetAttribute("value", "Hello");
                    }
                }
            }


            //另外還有些用法

            //搜尋整個Body標籤內的內容是否有"我在這"這個文字字串
            HtmlDocument doc2 = webBrowser1.Document;

            doc2.Body.InnerHtml.Contains("我在這");



            //整個文件的Img標籤有幾個

            //doc2.Images.Count


            //先搜尋標籤名字為tbody的標籤，然後後面的[4]代表著拿整個HTML的第四個tbody

            //HtmlElement tbody = doc2.GetElementsByTagName("tbody")[4];

            //拿上面第4個tbody裡面的第6個tr標籤
            //HtmlElement tr = tbody.GetElementsByTagName("tr")[6];

            /*
            //讀Frames用法
            HtmlWindow currentWindow = webBrowser1.Document.Window;

            HtmlWindow frame = currentWindow.Frames["Frame1"];
            foreach (HtmlWindow fr in currentWindow.Frames)
            {

            }
            */

            /*
            //找到某一個按鈕的標籤，並且按下去
            HtmlElement MyButton = doc2.Forms["main_form"].GetElementsByTagName("input")[3];
            MyButton.InvokeMember("click");
            */

            flag_loading = false;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            flag_use_method = 2;
            //webBrowser1連結Google網站
            webBrowser1.Navigate("http://www.google.com");
            //等待網站下載完成
            Loading();
        }

        //判斷網頁是否下載完成
        private void Loading()
        {
            while (webBrowser1.ReadyState != WebBrowserReadyState.Complete)
            {
                Application.DoEvents();
            }
        }

    }
}






