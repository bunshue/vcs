using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
程式啟動後
最小化至系統列
每一秒檢查一次
10分鐘後跳到最上層顯示
人按ack後 再最小化至系統列
直到10分鐘後再跳出來
最好能做到快捷鍵
*/

namespace vcs_Clock
{
    public partial class Form1 : Form
    {
        //移動無邊框窗體 ST
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x1;
        private const int HTCAPTION = 0x2;

        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_NCHITTEST:
                    base.WndProc(ref m);
                    if ((int)m.Result == HTCLIENT)
                        m.Result = (IntPtr)HTCAPTION;
                    return;
                    break;
            }
            base.WndProc(ref m);
        }
        //移動無邊框窗體 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;//設定無邊框
            //this.WindowState = FormWindowState.Minimized;
            //this.ShowInTaskbar = false;

            int x_st = 30;
            int y_st = 30;
            int w = 100;
            int h = 100;
            int dx = 10;

            int W = x_st + w * 3 + dx * 2 + x_st;
            int H = y_st + h + y_st;

            pictureBox1.ClientSize = new Size(W, H);
            pictureBox1.Location = new Point(0, 0);
            this.ClientSize = new Size(W, H);

            int SW = Screen.PrimaryScreen.Bounds.Width;
            this.Location = new Point(SW - W, 0);
        }

        int show_seconds = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();

            show_seconds++;
            if (show_seconds > 10)
            {
                this.TopMost = false;
                this.WindowState = FormWindowState.Minimized;
                this.ShowInTaskbar = false;
            }

            DateTime dt = DateTime.Now;//現在時間

            this.Text = dt.ToLongTimeString();

            if (((dt.Minute % 30) == 0) && (dt.Second < 2))
            {
                this.WindowState = FormWindowState.Normal;
                this.ShowInTaskbar = true;
                this.TopMost = true;
                show_seconds = 0;
            }
        }

        private void pictureBox1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************
        #region 移動無邊框表單
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                isMouseDown = true;
            }
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                isMouseDown = false;
            }
        }
        #endregion

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int hh = DateTime.Now.Hour;
            int mm = DateTime.Now.Minute;
            int ss = DateTime.Now.Second;

            int x_st = 30;
            int y_st = 30;
            int w = 100;
            int h = 100;
            int dx = 10;

            e.Graphics.Clear(Color.Red);

            for (int i = 0; i < 3; i++)
            {
                e.Graphics.FillRectangle(new SolidBrush(Color.Black), x_st + (w + dx) * i, y_st, w, h);
            }

            e.Graphics.DrawLine(new Pen(Color.Red, 6), x_st, y_st + h / 2, x_st + 380, y_st + h / 2);

            int dy = 15;
            e.Graphics.DrawString(hh.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st, y_st + dy);
            e.Graphics.DrawString(mm.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st + (w + dx) * 1, y_st + dy);
            e.Graphics.DrawString(ss.ToString("D2"), new Font("標楷體", 55, FontStyle.Bold), Brushes.White, x_st + (w + dx) * 2, y_st + dy);
        }
    }
}
