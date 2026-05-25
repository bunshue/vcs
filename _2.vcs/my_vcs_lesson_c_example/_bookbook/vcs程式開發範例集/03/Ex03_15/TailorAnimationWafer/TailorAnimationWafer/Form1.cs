using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TailorAnimationWafer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        public int index = 0;//控件圖片索引
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (index != 11)
            {
                pictureBox1.Image = imageList1.Images[index];
                index++;
            }
            if (index == 11)
            {
                index = 0;
            }
        }
    }
}

