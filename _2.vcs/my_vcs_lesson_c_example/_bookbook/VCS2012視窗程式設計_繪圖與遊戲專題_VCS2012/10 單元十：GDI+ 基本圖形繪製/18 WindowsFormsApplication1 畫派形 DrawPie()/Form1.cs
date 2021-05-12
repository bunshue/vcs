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
        int startAngle = -10; // 開始的角度
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            startAngle = startAngle + 1; // 更新開始的角度
            this.pictureBox1.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = !timer1.Enabled;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            int cx = W / 2;
            int cy = H / 2;
            int d = (int)(Math.Min(W, H) / 2) - 10; //半徑

            for (int i = 0; i < 18; i++)
            {
                if (i % 2 == 0)  // 偶數才要繪出
                {
                    e.Graphics.DrawPie(Pens.Black, cx - d, cy - d, 2 * d, 2 * d, startAngle + i * 20, 20); // 繪出派形
                }
            }

        }
    }
}