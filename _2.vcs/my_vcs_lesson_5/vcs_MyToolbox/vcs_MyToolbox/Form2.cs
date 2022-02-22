using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyToolbox
{
    public partial class Form2 : Form
    {
        public Form2(string filename, int page)
        {
            InitializeComponent();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            //this.Size = new Size(1920, 1040);
            //this.StartPosition = FormStartPosition.CenterScreen; //居中顯示

            //richTextBox1.Text += "檔案 : " + filename + "\n";
            //richTextBox1.Text += "頁數 : " + page.ToString() + "\n";

            //指名頁數
            webBrowser1.Navigate(filename + "?#initZoom=fitToPage&view=fit&navpanes=0&toolbar=0&page=" + page.ToString());
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            

        }
    }
}
