using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Wifgsfgsfg
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.BackColor = Color.Gray;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //pictureBox1.Size = new System.Drawing.Size(200, 100);
            pictureBox1.Size = new Size(300, 200);
        }
    }
}
