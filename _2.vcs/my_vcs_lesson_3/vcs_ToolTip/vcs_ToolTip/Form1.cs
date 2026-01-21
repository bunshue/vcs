using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ToolTip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            toolTip1.InitialDelay = 300;
            toolTip1.ReshowDelay = 300;
            toolTip1.ShowAlways = true;
            toolTip1.SetToolTip(this.button1, "button1 的提示");
            toolTip1.SetToolTip(this.button2, "button2 的提示");
            toolTip1.SetToolTip(this.button3, "button3 的提示");

            toolTip1.InitialDelay = 300;
            toolTip1.ReshowDelay = 300;
            toolTip1.ShowAlways = true;
            toolTip1.SetToolTip(this.richTextBox1, "richTextBox1 的提示");

            toolTip1.InitialDelay = 300;
            toolTip1.ReshowDelay = 300;
            toolTip1.ShowAlways = true;
            toolTip1.SetToolTip(this.pictureBox1, "pictureBox1 的提示");

            //6060
            toolTip2.OwnerDraw = true;
            toolTip2.SetToolTip(button4, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA");
            toolTip2.SetToolTip(button5, "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB");
            toolTip2.SetToolTip(button6, "CCCCCCCCCCCCCCCCCCCCCCCCCCCCCC");

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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 7+20);

            pictureBox1.Size = new Size(400, 400);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Size = new Size(400, 400);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1080, 620);
            this.Text = "vcs_ToolTip";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = e.Location.ToString();
            SetTooltip(e.Location);
        }

        private void SetTooltip(PointF point)
        {
            if (pictureBox1.Image == null)
            {
                //return;
            }

            string mesg = "";

            mesg = "目前座標 " + point.ToString();

            if (toolTip1.GetToolTip(pictureBox1) != mesg)
            {
                toolTip1.SetToolTip(pictureBox1, mesg);
            }
            pictureBox1.Refresh();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private const int Margin = 10;
        private void toolTip2_Draw(object sender, DrawToolTipEventArgs e)
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

        private void toolTip2_Popup(object sender, PopupEventArgs e)
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
    }
}
