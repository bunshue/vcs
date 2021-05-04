using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D;  // HatchBrush

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Font myFont = new Font("標楷體", 24); // 字型
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            string text = "VC# 繪圖程式好容易！"; // 文字字串
            SizeF stringSize = e.Graphics.MeasureString(text, myFont); // 文字字串的寬高
            float X = this.ClientSize.Width / 2 - stringSize.Width / 2; // 左上角的座標
            float Y = this.ClientSize.Height / 2 - stringSize.Height / 2;
            e.Graphics.DrawString(text,  // 繪出文字字串
                myFont,
                Brushes.Red,
                X, Y);

            Point[] pt = new Point[3];
            pt[0] = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            pt[1] = new Point(this.ClientSize.Width / 2 - 50, this.ClientSize.Height - 10);
            pt[2] = new Point(this.ClientSize.Width / 2 + 50, this.ClientSize.Height - 10);
            e.Graphics.FillPolygon(Brushes.Yellow, pt);
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }


    }
}