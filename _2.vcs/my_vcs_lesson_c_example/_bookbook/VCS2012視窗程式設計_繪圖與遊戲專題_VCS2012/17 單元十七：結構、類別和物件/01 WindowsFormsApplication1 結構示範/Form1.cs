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
        struct Ball  // 結構
        {
            public Point pt;
            public Color color;
        }

        Random rd = new Random(); // 亂數

        List<Ball> ballList = new List<Ball>(); // 動態陣列

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Ball aBall;
            aBall.pt = new Point(rd.Next(20, this.ClientSize.Width - 20), rd.Next(40, this.ClientSize.Height - 20));
            aBall.color = Color.Red;
            ballList.Add(aBall);

            this.Invalidate();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            foreach (Ball aBall in ballList)
            {
                e.Graphics.FillEllipse(new SolidBrush(aBall.color), aBall.pt.X - 10, aBall.pt.Y - 10, 20, 20);
                e.Graphics.DrawEllipse(Pens.Black, aBall.pt.X - 10, aBall.pt.Y - 10, 20, 20);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Ball aBall;
            aBall.pt = new Point(rd.Next(20, this.ClientSize.Width - 20), rd.Next(40, this.ClientSize.Height - 20));
            aBall.color = Color.Green;
            ballList.Add(aBall);

            this.Invalidate();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            ballList.Clear();
            this.Invalidate();
        }
    }
}