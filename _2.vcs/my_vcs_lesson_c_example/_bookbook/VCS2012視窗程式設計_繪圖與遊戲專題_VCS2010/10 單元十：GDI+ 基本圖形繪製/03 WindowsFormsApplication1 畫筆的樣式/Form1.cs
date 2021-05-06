using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Drawing2D; // for DashStyle

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
            Pen pen1 = new Pen(Color.Black, 3);  // 紅色畫筆 粗細為 1
            Pen pen2 = new Pen(Color.Red, 10); // 紅色畫筆 粗細為 10

            pen1.DashStyle = DashStyle.Dash; //虛線
            e.Graphics.DrawLine(pen1, 10, 10, 200, 10);

            pen1.DashStyle = DashStyle.DashDot; // 虛線-點線
            e.Graphics.DrawLine(pen1, 10, 40, 200, 40);

            pen1.DashStyle = DashStyle.DashDotDot; // 虛線-點-點線
            e.Graphics.DrawLine(pen1, 10, 70, 200, 70);

            pen1.DashStyle = DashStyle.Dot; //點線
            e.Graphics.DrawLine(pen1, 10, 100, 200, 100);

            pen1.DashStyle = DashStyle.Solid; //實線
            e.Graphics.DrawLine(pen1, 10, 130, 200, 130);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}