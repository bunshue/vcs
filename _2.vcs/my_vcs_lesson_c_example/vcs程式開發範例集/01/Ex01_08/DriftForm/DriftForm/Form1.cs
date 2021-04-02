using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace DriftForm
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.textBox1.Focused  == false)
            {
                this.Top = -40;
            }
        }
        
        private void label2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void panel1_MouseClick(object sender, MouseEventArgs e)
        {
            Focus();
            this.Top = 60;
           
        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            Focus();
            this.Top = 60;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
          //  this.;
        }
    }
}