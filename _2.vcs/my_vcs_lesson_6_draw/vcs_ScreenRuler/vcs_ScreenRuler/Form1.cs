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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            this.WindowState = FormWindowState.Normal;
            this.Size = new Size(1920, 1080 / 4);
            this.Location = new Point(0, 0);
            this.BackColor = Color.White;

            bmp = new Bitmap(screenWidth, screenHeight);     //initial W, H
            g = Graphics.FromImage(bmp);

            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, screenWidth - 1, screenHeight - 1);

            int i;
            int delta;

            delta = 100;
            for (i = 0; i < screenWidth; i += delta)
            {
                g.DrawLine(new Pen(Color.Blue, 1), i, 0, i, screenHeight / 2);
                g.DrawString(i.ToString(), new Font("標楷體", 12), new SolidBrush(Color.Blue), new PointF(i - 15, 30));   //畫直線
            }

            for (i = 0; i < screenWidth; i += 10)
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

            for (i = 0; i < 350; i += delta)
            {
                g.DrawLine(new Pen(Color.Blue, 1), 0, i, screenWidth, i);
                g.DrawString(i.ToString(), new Font("標楷體", 12), new SolidBrush(Color.Blue), new PointF(0, i));
            }

            for (i = 0; i <= 350; i += 10)
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
            delta = screenWidth * 5 / 100;
            for (i = 0; i < screenWidth; i += delta)
            {
                g.DrawLine(new Pen(Color.Red, 1), i, 0 + 100, i, screenHeight);
                g.DrawString((i * 100 / screenWidth).ToString() + " %".ToString(), new Font("標楷體", 12), new SolidBrush(Color.Red), new PointF(i - 20, 220));
            }
            */

            /*
            i = screenHeight * 10 / 100;
            g.DrawLine(new Pen(Color.Green, 1), 0, i, i + screenWidth, i);

            i = screenHeight * 90 / 100;
            g.DrawLine(new Pen(Color.Green, 1), 0, i, i + screenWidth, i);
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

        //***********************
        private Point mouseOffset;//記錄滑鼠座標
        private bool isMouseDown = false;//是否按下滑鼠
        //***********************

        #region 移動無邊框Form

        private void Form1_MouseDown(object sender, MouseEventArgs e)
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

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown)
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
                isMouseDown = false;
            }
        }
        #endregion

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

    }
}
