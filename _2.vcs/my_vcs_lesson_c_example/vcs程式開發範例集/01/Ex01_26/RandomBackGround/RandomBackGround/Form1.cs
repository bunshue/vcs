using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace RandomBackGround
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Random rdn = new Random();
            int i = rdn.Next(imageList1.Images.Count);
            this.BackgroundImage = imageList1.Images[i];
        }
    }
}