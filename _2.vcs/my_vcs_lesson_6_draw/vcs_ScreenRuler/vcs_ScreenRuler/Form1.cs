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
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化
            this.BackColor = Color.White;

            bmp = new Bitmap(screenWidth, screenHeight);     //initial W, H
            g = Graphics.FromImage(bmp);

            g.DrawRectangle(new Pen(Color.Red, 1), 0, 0, screenWidth - 1, screenHeight - 1);

            int i;
            int delta;

            delta = 100;
            for (i = 0; i < screenWidth; i += delta)
            {
                //g.DrawLine(new Pen(Color.Green, 1), i, 0, i, screenHeight);
            }

            delta = screenWidth * 5 / 100;
            for (i = 0; i < screenWidth; i += delta)
            {
                g.DrawLine(new Pen(Color.Red, 1), i, 0, i, screenHeight);
            }

            i = screenHeight * 10 / 100;
            g.DrawLine(new Pen(Color.Green, 1), 0, i, i + screenWidth, i);

            i = screenHeight * 90 / 100;
            g.DrawLine(new Pen(Color.Green, 1), 0, i, i + screenWidth, i);

            this.BackgroundImage = bmp;
            //this.Opacity = 0.5;
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.X:
                    Application.Exit();
                    break;
                default:
                    //MessageBox.Show("x, KeyCode: " + e.KeyCode.ToString());
                    break;
            }
        }

        private void Form1_Click(object sender, EventArgs e)
        {
            this.Opacity -= 0.1;
        }
    }
}
