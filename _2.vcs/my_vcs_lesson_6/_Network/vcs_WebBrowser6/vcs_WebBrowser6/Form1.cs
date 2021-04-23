using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_WebBrowser6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
      
       
        private void dToolStripMenuItem_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowPageSetupDialog();
        }

        private void 打印瀏覽UToolStripMenuItem_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowPrintPreviewDialog();
        }

        private void 打印PToolStripMenuItem_Click(object sender, EventArgs e)
        {
            webBrowser1.Print();
        }

        private void 屬性NToolStripMenuItem_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowPropertiesDialog();
        }

        private void 退出IToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
        
        private void 保存DToolStripMenuItem_Click(object sender, EventArgs e)
        {
            webBrowser1.ShowSaveAsDialog();
        }
        //文件導航
        private void GoaButton_Click(object sender, EventArgs e)
        {
            Navigate(toolStripTextBox1.Text);//文件導航
        }
        //如果導航記錄可用．
        private void backButton_Click(object sender, EventArgs e)
        {
            webBrowser1.GoBack();//如果導航記錄可用．
        }
        //導向下一頁
        private void forwardButton_Click(object sender, EventArgs e)
        {

            webBrowser1.GoForward();//導向下一頁
        }
        //取消目前頁
        private void stopButton_Click(object sender, EventArgs e)
        {
            webBrowser1.Stop();//取消目前頁
        }
        //使用控制元件重新加載頁
        private void refreshButton_Click(object sender, EventArgs e)
        {
            if (!webBrowser1.Url.Equals("about:blank"))
            {
                webBrowser1.Refresh();//使用控制元件重新加載頁
            }
        }
        //傳回主頁
        private void homeButton_Click(object sender, EventArgs e)
        {
            webBrowser1.GoHome();//傳回主頁
        }
        //控制元件導航目前頁
        private void searchButton_Click(object sender, EventArgs e)
        {
            webBrowser1.GoSearch();//控制元件導航目前頁

        }
        //打印
        private void printButton_Click(object sender, EventArgs e)
        {
            webBrowser1.Print();//打印
        }
        //導航方法
        private void Navigate(String address)//方法
        {
            if (String.IsNullOrEmpty(address)) return;
            if (address.Equals("about:blank")) return;
            if (!address.StartsWith("http://")) address = "http://" + address;
            try
            {
                webBrowser1.Navigate(new Uri(address));
            }
            catch (System.UriFormatException)
            {
                return;
            }
        }
        //Web導航後發生
        private void webBrowser1_Navigated(object sender, WebBrowserNavigatedEventArgs e)
        {
            toolStripTextBox1.Text = webBrowser1.Url.ToString();
        }
       // CanGoForward 屬性值修改時發生。 
        private void webBrowser1_CanGoForwardChanged(object sender, EventArgs e)
        {
            forwardButton.Enabled = webBrowser1.CanGoForward;
        }
        //按下Enter
        private void toolStripTextBox1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                Navigate(toolStripTextBox1.Text);
            }
          
        }

        private void Form1_Load(object sender, EventArgs e)
        {
           
        }

     
    }
}