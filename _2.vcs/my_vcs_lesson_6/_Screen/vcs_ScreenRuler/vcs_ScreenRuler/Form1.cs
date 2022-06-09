using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ScreenRuler
{
    public partial class Form1 : Form
    {
        Graphics g;
        Bitmap bmp;

        int W = 1920;
        int H = 1080;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            W = Screen.PrimaryScreen.Bounds.Width;
            H = Screen.PrimaryScreen.Bounds.Height;
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            this.WindowState = FormWindowState.Normal;
            this.Size = new Size(W, H / 4);
            this.Location = new Point(W - 150, H - 400);
            this.BackColor = Color.White;

            bmp = new Bitmap(W, H);     //initial W, H
            g = Graphics.FromImage(bmp);

            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, W - 1, H - 1);
            g.DrawString(W.ToString() + " X " + H.ToString(), new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(W - 290, H - 60));

            int i;
            int delta;

            delta = 100;
            //畫垂直線
            for (i = 0; i < W; i += delta)
            {
                g.DrawLine(new Pen(Color.Blue, 1), i, 0, i, H); //每隔100點畫 垂直線 藍線
                g.DrawString(i.ToString(), new Font("標楷體", 12), new SolidBrush(Color.Blue), new PointF(i - 15, 30));
            }

            //畫垂直線
            //每隔50點畫 垂直線 紅線
            //每隔10點畫 垂直線 黑線
            for (i = 0; i < W; i += 10)
            {
                if ((i % 50) == 0)
                {
                    g.DrawLine(new Pen(Color.Red, 1), i, 0, i, 100);
                }
                else if ((i % 100) != 0)
                {
                    g.DrawLine(new Pen(Color.Black, 1), i, 0, i, 50);
                }
            }

            //畫螢幕中心垂直線 與 中心水平線
            g.DrawLine(new Pen(Color.Red, 5), W / 2, 0, W / 2, H);
            g.DrawLine(new Pen(Color.Red, 5), 0, H / 2, W, H / 2);

            for (i = 0; i < H; i += delta)
            {
                g.DrawLine(new Pen(Color.Blue, 1), 0, i, W, i);
                g.DrawString(i.ToString(), new Font("標楷體", 12), new SolidBrush(Color.Blue), new PointF(0, i));
            }

            for (i = 0; i <= H; i += 10)
            {
                if ((i % 50) == 0)
                {
                    g.DrawLine(new Pen(Color.Red, 1), 0, i, 100, i);
                }
                else if ((i % 100) != 0)
                {
                    g.DrawLine(new Pen(Color.Black, 1), 0, i, 50, i);
                }
            }

            /*    百分比 不好用
            delta = W * 5 / 100;
            for (i = 0; i < W; i += delta)
            {
                g.DrawLine(new Pen(Color.Red, 1), i, 0 + 100, i, H);
                g.DrawString((i * 100 / W).ToString() + " %".ToString(), new Font("標楷體", 12), new SolidBrush(Color.Red), new PointF(i - 20, 220));
            }
            */

            /*
            i = H * 10 / 100;
            g.DrawLine(new Pen(Color.Green, 1), 0, i, i + W, i);

            i = H * 90 / 100;
            g.DrawLine(new Pen(Color.Green, 1), 0, i, i + W, i);
            */

            this.BackgroundImage = bmp;
            this.Opacity = 0.5;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.X:
                case Keys.Escape:
                    Application.Exit();
                    break;
                default:
                    //MessageBox.Show("x, KeyCode: " + e.KeyCode.ToString());
                    break;
            }
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            //this.Opacity -= 0.1;
        }

        #region 移動無邊框Form
        private Point mouseOffset;//記錄滑鼠座標
        private bool flag_mouse_down = false;//是否按下滑鼠

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset = new Point(xOffset, yOffset);
                flag_mouse_down = true;
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset.X, mouseOffset.Y);
                Location = mousePos;
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_mouse_down = false;
            }
        }
        #endregion

        int flag_screen_ruler_mode = 0;
        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            flag_screen_ruler_mode++;
            if (flag_screen_ruler_mode == 1)
            {
                this.Size = new Size(W, H);
            }
            else if (flag_screen_ruler_mode == 2)
            {
                Application.Exit();
            }
            else
            {
                flag_screen_ruler_mode = 0;

            }
        }

    }
}
