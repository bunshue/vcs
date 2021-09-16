using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_3_1_21
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(400, 430);
            pictureBox1.ImageLocation = 
                "http://www.cwb.gov.tw/V7/observe/satellite/Data/s3p/s3p-2013-01-20-01-00.jpg";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;

            button1.Text = "衛星雲圖";
        }
    }
}
