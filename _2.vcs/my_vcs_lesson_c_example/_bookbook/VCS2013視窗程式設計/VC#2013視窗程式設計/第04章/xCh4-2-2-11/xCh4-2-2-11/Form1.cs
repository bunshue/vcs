using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_2_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // 「瀏覽」
        private void button1_Click(object sender, EventArgs e)
        {
            if (String.IsNullOrEmpty(textBox1.Text)) return;
            if (textBox1.Text.Equals("about:blank")) return;
            if (!textBox1.Text.StartsWith("http://") &&  !textBox1.Text.StartsWith("https://"))
            {
                textBox1.Text = "http://" + textBox1.Text;
            }
            try
            {
                webBrowser1.Navigate(new Uri(textBox1.Text));
            }
            catch (System.UriFormatException)
            {
                return;
            }
         }

        // 回首頁
        private void button2_Click(object sender, EventArgs e)
        {
            webBrowser1.GoHome();
        }

        // 下一頁
        private void button3_Click(object sender, EventArgs e)
        {
            webBrowser1.GoForward();
        }

        // 上一頁
        private void button4_Click(object sender, EventArgs e)
        {
            webBrowser1.GoBack();
        }

        // 預覽列印
        private void button5_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowPrintPreviewDialog();
        }

        // 重新載入
        private void button6_Click(object sender, EventArgs e)
        {
            webBrowser1.Refresh();
        }

        // 停止
        private void button7_Click(object sender, EventArgs e)
        {
            webBrowser1.Stop();
        }

        // 開啟 Internet Explorer [列印] 對話方塊
        private void button8_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowPrintDialog();
        }

        // 開啟 Internet Explorer [版面設定] 對話方塊
        private void button9_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowPageSetupDialog();
        }

        // 開啟 Internet Explorer [儲存網頁] 對話方塊
        private void button10_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowSaveAsDialog();
        }

        // 發生於 WebBrowser 控制項完成文件的載入時
        private void webBrowser1_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {
            this.Text = "WebBrowser控制項範例：文件名稱->" +
                webBrowser1.DocumentTitle +
                "，文件類型->" +
                webBrowser1.DocumentType;
        }

        // 程式執行後，開啟預設的網頁，本例為www.google.com.tw
        // 同時將focus移入可填寫網址的textBox1物件
        private void Form1_Load(object sender, EventArgs e)
        {
            webBrowser1.Url = new Uri("http://www.google.com.tw/");
        }
    }
}
