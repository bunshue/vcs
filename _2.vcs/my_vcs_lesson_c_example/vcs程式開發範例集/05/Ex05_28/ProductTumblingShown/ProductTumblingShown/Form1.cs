using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace ProductTumblingShown
{
    public partial class Form1 : Form
    {
        int left = 0;
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            left = 10;
            this.panel1.Left += left;
            int width=this.Width - this.panel1.Width;
            if (this.panel1.Left > width)
            {
                this.timer1.Enabled = false;
                this.timer2.Enabled = true;
                this.pictureBox1.Image = this.imageList1.Images[0];
                this.pictureBox2.Image = this.imageList2.Images[0];
                this.pictureBox3.Image = this.imageList3.Images[0];
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.Image = this.imageList1.Images[0];
            this.pictureBox2.Image = this.imageList2.Images[0];
            this.pictureBox3.Image = this.imageList3.Images[0];
            
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            left = -10;
            this.panel1.Left += left;
            if (this.panel1.Left <0)
            {
                this.timer1.Enabled = true;
                this.timer2.Enabled = false;
                this.pictureBox1.Image = this.imageList1.Images[1];
                this.pictureBox2.Image = this.imageList2.Images[1];
                this.pictureBox3.Image = this.imageList3.Images[1];
            }
        }
    }
}