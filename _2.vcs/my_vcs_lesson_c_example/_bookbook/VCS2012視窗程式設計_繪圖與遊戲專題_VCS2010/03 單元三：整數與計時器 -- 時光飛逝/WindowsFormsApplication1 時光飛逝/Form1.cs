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

        private void timer1_Tick(object sender, EventArgs e)
        {
            int i;
            i = Convert.ToInt32(label1.Text);
            i = i + 1;
            label1.Text = i.ToString();
            label1.Text = Convert.ToString(i);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            label1.Text = "0";
        }
    }
}