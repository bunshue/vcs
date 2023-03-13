using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ToolTipTest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //ToolTip：當游標停滯在某個控制項時，就會跳出一個小視窗
            ToolTip toolTip1 = new ToolTip();
            //SetToolTip：定義控制項會跳出提示的文字
            toolTip1.SetToolTip(textBox1, "please enter number!!");

            //以下為提示視窗的設定(通常會設定的部分)
            //ToolTipIcon：設定顯示在提示視窗的圖示類型。
            toolTip1.ToolTipIcon = ToolTipIcon.Info;
            //ForeColor：顧名思義就是前景顏色，你懂的!!XD
            toolTip1.ForeColor = Color.Blue;
            //BackColor：顧名思義就是背景顏色，你也懂的!!XD
            toolTip1.BackColor = Color.Gray;
            //AutoPopDelay：當游標停滯在控制項，顯示提示視窗的時間。(以毫秒為單位)
            toolTip1.AutoPopDelay = 5000;
            //ToolTipTitle：設定提示視窗的標題。
            toolTip1.ToolTipTitle = "提示訊息";
        }
    }
}
