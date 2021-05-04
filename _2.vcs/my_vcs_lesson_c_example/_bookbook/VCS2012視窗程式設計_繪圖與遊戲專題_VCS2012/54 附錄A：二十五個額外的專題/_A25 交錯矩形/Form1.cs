// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace WindowsApplication1
{
    public partial class Form1 : Form
    {
        SolidBrush brush = new SolidBrush(Color.Yellow);
        Color color1 = Color.White;
        Color color2 = Color.Red;
        int D = 100;
        Random rd = new Random();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            for (int i = 0; i < this.ClientSize.Width; i = i + D)
            {
                if (i % (D * 2) == 0) brush.Color = color2;
                else brush.Color = color1;

                for (int j = 0; j < this.ClientSize.Height; j = j + D)
                {
                    if (brush.Color == color1)
                       brush.Color = color2;
                    else
                       brush.Color = color1;

                    e.Graphics.FillRectangle(brush, i, j, D, D);
                    e.Graphics.DrawRectangle(Pens.Black, i, j, D, D);
                }
            }
            
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void color1ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color1 = colorDialog1.Color;
                this.Invalidate();
            }
        }

        private void color2ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                color2 = colorDialog1.Color;
                this.Invalidate();
            }
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            D = 10;
            this.Invalidate();
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            D = 20;
            this.Invalidate();
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            D = 50;
            this.Invalidate();
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            D = 100;
            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape)
                this.Close();
            else if (e.KeyData == Keys.Space)
            {
                timer1.Enabled = false;
                timer2.Enabled = false;
            }
        }

        private void color1ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void color2ToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            timer2.Enabled = true;
        }

        private void bothToolStripMenuItem_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            timer2.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            color1 = Color.FromArgb(rd.Next(256),rd.Next(256),rd.Next(256) );
            this.Invalidate();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            color2 = Color.FromArgb(rd.Next(256), rd.Next(256), rd.Next(256));
            this.Invalidate();
        }
    }
}