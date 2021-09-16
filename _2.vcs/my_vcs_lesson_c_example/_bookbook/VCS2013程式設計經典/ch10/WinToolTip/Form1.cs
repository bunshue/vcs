using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinToolTip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        // 表單載入時執行
        private void Form1_Load(object sender, EventArgs e)
        {
           linkLabel1.Text = "碁峰資訊";
           toolTip1.IsBalloon = true;			// 使用汽球的型式
           toolTip1.ToolTipIcon = ToolTipIcon.Info;  	// 顯示資訊圖示Icon
           toolTip1.ToolTipTitle = "碁峰給您快樂學習"; 	// 設定工具提示標題
           toolTip1.BackColor = Color.Orange;	// 設定工具提示背景色為橘色
           toolTip1.SetToolTip(linkLabel1, "碁峰提供好書"); 
           linkLabel2.Text = "請聯絡我們";
           linkLabel2.LinkArea=new LinkArea(1, 2);// 設定「聯絡」可以超連結
           toolTip2.SetToolTip(linkLabel2, "歡迎讀者來信");
        }
        // 連結到碁峰網站
        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // 連結到碁峰網站
            System.Diagnostics.Process.Start("http://www.gotop.com.tw");

        }
        // 按下 "連絡" 執行
        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
         // 開啟郵件軟體連結 wltasi@yahoo.com.tw
         System.Diagnostics.Process.Start("mailto:wltasi@yahoo.com.tw");
        }
    }
}
