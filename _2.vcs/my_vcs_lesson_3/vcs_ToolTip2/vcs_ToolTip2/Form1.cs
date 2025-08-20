using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ToolTip2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            toolTip1.OwnerDraw = true;
            toolTip1.SetToolTip(button1, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            toolTip1.SetToolTip(button2, "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB");
            toolTip1.SetToolTip(button3, "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCC");

            //ToolTip：當游標停滯在某個控制項時，就會跳出一個小視窗
            ToolTip toolTip_tb = new ToolTip();
            //SetToolTip：定義控制項會跳出提示的文字
            toolTip_tb.SetToolTip(textBox1, "please enter number!!");

            //以下為提示視窗的設定(通常會設定的部分)
            //ToolTipIcon：設定顯示在提示視窗的圖示類型。
            toolTip_tb.ToolTipIcon = ToolTipIcon.Info;
            //ForeColor：顧名思義就是前景顏色，你懂的!!XD
            toolTip_tb.ForeColor = Color.Blue;
            //BackColor：顧名思義就是背景顏色，你也懂的!!XD
            toolTip_tb.BackColor = Color.Gray;
            //AutoPopDelay：當游標停滯在控制項，顯示提示視窗的時間。(以毫秒為單位)
            toolTip_tb.AutoPopDelay = 5000;
            //ToolTipTitle：設定提示視窗的標題。
            toolTip_tb.ToolTipTitle = "提示訊息";
        }

        private const int Margin = 10;

        private void toolTip1_Popup(object sender, PopupEventArgs e)
        {
            int image_wid = 2 * Margin + Properties.Resources.burn.Width;
            int image_hgt = 2 * Margin +
                Properties.Resources.burn.Height;

            int wid = e.ToolTipSize.Width + 2 * Margin + image_wid;
            int hgt = e.ToolTipSize.Height;
            if (hgt < image_hgt)
                hgt = image_hgt;

            e.ToolTipSize = new Size(wid, hgt);
        }

        private void toolTip1_Draw(object sender, DrawToolTipEventArgs e)
        {
            // Draw the background and border.
            e.DrawBackground();
            e.DrawBorder();

            // Draw the image.
            e.Graphics.DrawImage(Properties.Resources.burn, Margin, Margin);

            // Draw the text.
            using (StringFormat sf = new StringFormat())
            {
                sf.Alignment = StringAlignment.Near;
                sf.LineAlignment = StringAlignment.Center;

                int image_wid = 2 * Margin +
                    Properties.Resources.burn.Width;

                Rectangle rect = new Rectangle(
                    image_wid, 0,
                    e.Bounds.Width - image_wid, e.Bounds.Height);
                e.Graphics.DrawString(e.ToolTipText, e.Font, Brushes.Green, rect, sf);
            }
        }
    }
}
