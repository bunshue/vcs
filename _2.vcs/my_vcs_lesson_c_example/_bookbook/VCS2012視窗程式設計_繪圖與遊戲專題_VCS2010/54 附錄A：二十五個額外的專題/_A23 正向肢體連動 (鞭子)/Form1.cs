/* 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2009-09 */
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
        Point pos = new Point(300, 300); // 手把上節點的座標位置
        WhipSegments whip01;
        public Form1()
        {
            InitializeComponent();
            whip01 = new WhipSegments(15, 80, 20, Color.Red, 40, 20, Color.Blue);

            pos.X = this.ClientSize.Width / 2 - whip01.Handler.size.Height / 2;
            hScrollBar1.Value = (int)(whip01.cycle_Delta * 1000);
            hScrollBar2.Value = whip01.HandlerRange;
            hScrollBar3.Value = whip01.WhipRange;
            hScrollBar4.Value = whip01.HandlerBaseAngle;
            hScrollBar5.Value = whip01.WhipBaseAngle;
            hScrollBar6.Value = (int)(whip01.WhipDelayAngle * 100);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 反鋸齒呈現
            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;

            whip01.Draw(e.Graphics);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            whip01.Update(new PointF(pos.X, pos.Y));
            this.Invalidate();
        }

        private void hScrollBar1_ValueChanged(object sender, EventArgs e)
        {
            whip01.cycle_Delta = hScrollBar1.Value * 0.001f;
        }

        private void hScrollBar2_ValueChanged(object sender, EventArgs e)
        {
            whip01.HandlerRange = hScrollBar2.Value;
        }

        private void hScrollBar3_ValueChanged(object sender, EventArgs e)
        {
            whip01.WhipRange = hScrollBar3.Value;
        }

        private void hScrollBar4_ValueChanged(object sender, EventArgs e)
        {
            whip01.HandlerBaseAngle = hScrollBar4.Value;
        }

        private void hScrollBar5_ValueChanged(object sender, EventArgs e)
        {
            whip01.WhipBaseAngle = hScrollBar5.Value;
        }

        private void hScrollBar6_ValueChanged(object sender, EventArgs e)
        {
            whip01.WhipDelayAngle = hScrollBar6.Value * 0.01;
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            pos = new Point(this.ClientSize.Width/4, this.ClientSize.Height/2); // 大腿上節點的座標位置
            this.Invalidate();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.SelectedIndex != -1)
            {
                whip01.Handler.SetSegType(comboBox1.SelectedIndex);
                for (int i = 0; i < whip01.Whip.Length; i++)
                    whip01.Whip[i].SetSegType(comboBox1.SelectedIndex);
            }
        }
    }
}