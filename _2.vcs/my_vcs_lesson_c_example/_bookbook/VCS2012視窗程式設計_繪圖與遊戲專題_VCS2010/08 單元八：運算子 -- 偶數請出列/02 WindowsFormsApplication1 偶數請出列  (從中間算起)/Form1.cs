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
            int Cy = this.ClientSize.Height / 2;

            for (int i = -10; i <= 10; i++)
            {
                if (i == 0)
                    e.Graphics.DrawLine(Pens.Red, Cx + i * 10, Cy - 50, Cx + i * 10, Cy + 50);
                else if (i % 2 == 0)  // 偶數
                    e.Graphics.DrawLine(Pens.Red, Cx + i * 10, Cy - 30, Cx + i * 10, Cy + 30);
                else
                    e.Graphics.DrawLine(Pens.Black, Cx + i * 10, Cy - 20, Cx + i * 10, Cy + 20);
            }
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate();
        }
    }
}