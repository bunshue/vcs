using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh6_1_4_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Image = Image.FromFile(@"c:\Spring.jpg");

            textBox1.Text = splitContainer1.SplitterDistance.ToString();
            textBox2.Text = splitContainer1.SplitterWidth.ToString();
            textBox3.Text = splitContainer1.SplitterIncrement.ToString();
            textBox4.Text = splitContainer1.Panel1MinSize.ToString();
            textBox5.Text = splitContainer1.Panel2MinSize.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Button button = (Button)sender;

            if (splitContainer1.Orientation == Orientation.Vertical)
            {
                splitContainer1.Orientation = Orientation.Horizontal;
                button.Text = "水平(&H)";
                splitContainer1.SplitterDistance = 150;
            }
            else
            {
                splitContainer1.Orientation = Orientation.Vertical;
                button.Text = "垂直(&V)";
                splitContainer1.SplitterDistance = 232;
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            splitContainer1.Panel1Collapsed = checkBox1.Checked;
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            splitContainer1.Panel2Collapsed = checkBox2.Checked;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            splitContainer1.Panel2Collapsed = false;
            checkBox2.Checked = false;
        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {
            int width = Convert.ToInt32(textBox2.Text);
            splitContainer1.SplitterWidth = width;
        }

        private void textBox3_TextChanged(object sender, EventArgs e)
        {
            int increment = Convert.ToInt32((textBox3.Text));
            splitContainer1.SplitterIncrement = increment;
        }

        private void textBox4_TextChanged(object sender, EventArgs e)
        {
            int panel1Min = Convert.ToInt32(textBox4.Text);
            splitContainer1.Panel1MinSize = panel1Min;
        }

        private void textBox5_TextChanged(object sender, EventArgs e)
        {
            int panel2Min = Convert.ToInt32(textBox5.Text);
            splitContainer1.Panel1MinSize = panel2Min;
        }

        private void splitContainer1_SplitterMoved(object sender, SplitterEventArgs e)
        {
            textBox1.Text = splitContainer1.SplitterDistance.ToString();
        }
    }
}
