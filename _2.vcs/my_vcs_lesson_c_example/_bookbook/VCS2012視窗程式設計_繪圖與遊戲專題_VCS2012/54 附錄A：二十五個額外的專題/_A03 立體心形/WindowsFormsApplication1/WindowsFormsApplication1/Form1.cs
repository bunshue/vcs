// 作者：鄞永傳老師‧xnabook@yahoo.com.tw‧2012-08 
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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.ClientSize.Width / 2;
            int Cy = this.ClientSize.Height / 4;

            for (int i = 0; i <= 90; i++)
            {
                for (int j = 0; j <= 90; j++)
                {
                    double r = Math.PI / 45.0 * i * (1 - Math.Sin(Math.PI / 45 * j)) * 18;
                    double x = Cx + (r * Math.Cos(Math.PI / 45 * j) * Math.Sin(Math.PI / 45 * i));
                    double y = Cy - (r * Math.Sin(Math.PI / 45 * j));

                    e.Graphics.FillEllipse(Brushes.Black, (float)x - 1, (float)y - 1, 2, 2);
                }
            }

        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}
