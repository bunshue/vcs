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
            // 標籤元件的前景顏色
            label1.ForeColor = Color.Red;
            label2.ForeColor = Color.Green;
            label3.ForeColor = Color.Blue;

            // 面板元件的背景顏色
            panel1.BackColor = Color.FromArgb(255, 0, 0);
            panel2.BackColor = Color.FromArgb(0, 255, 0);
            panel3.BackColor = Color.FromArgb(0, 0, 255);
        }
    }
}
