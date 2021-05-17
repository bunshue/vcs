using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_LinkLabel
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            linkLabel1.Text = "群曜醫電";
            toolTip1.IsBalloon = true;			  // 使用汽球的形式
            toolTip1.ToolTipIcon = ToolTipIcon.Info;  // 顯示資訊圖示Icon
            toolTip1.ToolTipTitle = "InsightEyes"; // 設定工具提示標題
            toolTip1.SetToolTip(linkLabel1, "群曜醫電股份有限公司");   // 設定linkLabel1顯示工具提示
            linkLabel2.Text = "請聯絡我們";
            linkLabel2.LinkArea = new LinkArea(1, 2); // 設定「聯絡」可以超連結
            toolTip2.SetToolTip(linkLabel2, "歡迎來信");   // 設定linkLabel2顯示工具提示
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // 連結到群曜醫電網站
            System.Diagnostics.Process.Start("https://www.insighteyes.com/");
        }

        private void linkLabel2_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            // 開啟郵件軟體連結 david@insighteyes.com
            System.Diagnostics.Process.Start("mailto:david@insighteyes.com");
        }
    }
}
