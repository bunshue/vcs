using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace GraduallyWindows
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Opacity += 0.1; 
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //this.Opacity += 0.1;
        }
    }
}