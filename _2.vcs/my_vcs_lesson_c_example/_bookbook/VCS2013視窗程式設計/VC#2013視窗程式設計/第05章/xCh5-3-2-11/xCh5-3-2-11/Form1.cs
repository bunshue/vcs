using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_3_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            hScrollBar1.Minimum = 0;
            hScrollBar1.Maximum = pictureBox1.Width;

            vScrollBar1.Minimum = 0;
            vScrollBar1.Maximum = pictureBox1.Height;

            pictureBox1.Width = 300;
            pictureBox1.Height = 225;

            hScrollBar1.Value = 300;
            vScrollBar1.Value = 225;
        }

        private void hScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            pictureBox1.Width = hScrollBar1.Value;
            label1.Text = "寛：" + hScrollBar1.Value.ToString();
        }

        private void vScrollBar1_Scroll(object sender, ScrollEventArgs e)
        {
            pictureBox1.Height = vScrollBar1.Value;
            label2.Text = "高：" + vScrollBar1.Value.ToString();
        }
    }
}
