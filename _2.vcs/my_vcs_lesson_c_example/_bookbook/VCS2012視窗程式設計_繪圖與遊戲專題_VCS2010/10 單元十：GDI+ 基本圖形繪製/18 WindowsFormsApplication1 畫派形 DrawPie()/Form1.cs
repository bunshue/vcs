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
            int Cx = this.ClientSize.Width / 2;
            int Cy = this.ClientSize.Height / 2;
            int D = (int)(Math.Min(this.ClientSize.Width,
                         this.ClientSize.Height) / 2) - 10; //半徑

            for (int i = 0; i < 18; i++)
            {
                if (i % 2 == 0)  // 偶數才要繪出
                    e.Graphics.DrawPie(Pens.Black, Cx - D, Cy - D, 2 * D, 2 * D, startAngle + i * 20, 20); // 繪出多邊形
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            startAngle = startAngle + 1; // 更新開始的角度
            this.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = !timer1.Enabled;
        }
    }
}