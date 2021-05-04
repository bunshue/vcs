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
        int X, Y;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            label1.Text = Convert.ToString(X); // 將整數轉為 字串
            label2.Text = Convert.ToString(Y);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            X = e.Location.X; //  直接使用 e.X 也可以
            Y = e.Location.Y; //  直接使用 e.Y 也可以
            this.Invalidate();
        }
    }
}