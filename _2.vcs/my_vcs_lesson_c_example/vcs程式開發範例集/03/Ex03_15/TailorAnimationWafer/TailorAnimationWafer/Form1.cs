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

        public int intImage =0;//控件圖片索引
        private void timer1_Tick(object sender, EventArgs e)
        {
            if (intImage != 11)
            {
                
                pictureBox1.Image = imageList1.Images[intImage];
                intImage++;
                
            }
            if (intImage == 11)
            {
                intImage = 0;
            }
            //
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }
    }
}