using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh5_3_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            trackBar1.Minimum = 0;
            trackBar1.Maximum = 255;
            trackBar1.TickFrequency = 30;
            trackBar1.LargeChange = 30;
            trackBar1.SmallChange = 10;

            trackBar2.Minimum = 0;
            trackBar2.Maximum = 255;
            trackBar2.TickFrequency = 30;
            trackBar2.LargeChange = 30;
            trackBar2.SmallChange = 10;

            trackBar3.Minimum = 0;
            trackBar3.Maximum = 255;
            trackBar3.TickFrequency = 30;
            trackBar3.LargeChange = 30;
            trackBar3.SmallChange = 10;

            label1.Text = "R";
            label2.Text = "G";
            label3.Text = "B";
            label7.Text = "示範：";
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            label4.Text = trackBar1.Value.ToString();
            textBox1.BackColor = Color.FromArgb(
                trackBar1.Value, 
                trackBar2.Value, 
                trackBar3.Value);
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            label5.Text = trackBar2.Value.ToString();
            textBox1.BackColor = Color.FromArgb(trackBar1.Value, trackBar2.Value, trackBar3.Value);
        }

        private void trackBar3_Scroll(object sender, EventArgs e)
        {
            label6.Text = trackBar3.Value.ToString();
            textBox1.BackColor = Color.FromArgb(trackBar1.Value, trackBar2.Value, trackBar3.Value);
        } 
    }
}
