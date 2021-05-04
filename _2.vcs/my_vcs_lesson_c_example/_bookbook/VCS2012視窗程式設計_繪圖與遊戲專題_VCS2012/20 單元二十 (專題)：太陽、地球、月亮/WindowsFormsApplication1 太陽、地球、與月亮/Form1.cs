using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        float angleEarth = 0;  // 地球的旋轉角度
        float angleMoon = 0;   // 月球的旋轉角度

        float deltaEarth = 1;  // 地球旋轉角度的遞增值
        float deltaMoon = 12;  // 月球旋轉角度的遞增值

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(500, 500); // 視窗客戶區的寬高
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            // 繪出 太陽
            e.Graphics.TranslateTransform(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            e.Graphics.FillEllipse(Brushes.Crimson, -100, -100, 200, 200);

            // 繪出 地球
            e.Graphics.RotateTransform(angleEarth);
            e.Graphics.TranslateTransform(200, 0);
            e.Graphics.FillEllipse(Brushes.Cyan, -20, -20, 40, 40);

            // 繪出 月球
            e.Graphics.RotateTransform(angleMoon);
            e.Graphics.TranslateTransform(40, 0);
            e.Graphics.FillEllipse(Brushes.PaleGreen, -5, -5, 10, 10);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            angleEarth += deltaEarth; // 地球的旋轉角度 累進
            angleEarth %= 360;

            angleMoon += deltaMoon; // 月球的旋轉角度 累進
            angleMoon %= 360;
            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Up)
            {
                deltaEarth += 1;
            }
            else if (e.KeyData == Keys.Down)
            {
                deltaEarth -= 1;
                if (deltaEarth < 1) deltaEarth = 1;
            }

            if (e.KeyData == Keys.Right)
            {
                deltaMoon += 1;
            }
            else if (e.KeyData == Keys.Left)
            {
                deltaMoon -= 1;
                if (deltaMoon < 1) deltaMoon = 1;
            }

            if (e.KeyData == Keys.Space)
            {
                deltaEarth = 1;
                deltaMoon = 12;
            }
        }
    }
}