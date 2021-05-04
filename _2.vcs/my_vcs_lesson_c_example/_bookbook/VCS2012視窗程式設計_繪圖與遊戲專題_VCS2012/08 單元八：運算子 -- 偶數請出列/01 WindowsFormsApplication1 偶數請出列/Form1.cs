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
            for (int i = 1; i <= 20; i++)
            {
                if (i % 2 == 0)  // 偶數
                    e.Graphics.DrawLine(Pens.Red, i * 20, 30, i * 20, 100);
                else
                    e.Graphics.DrawLine(Pens.Black, i * 20, 50, i * 20, 100);
            }
        }
    }
}