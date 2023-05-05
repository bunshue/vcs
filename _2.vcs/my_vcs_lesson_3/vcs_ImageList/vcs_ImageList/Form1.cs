using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ImageList
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Enabled = true;
            button2.Enabled = false;
            button3.Enabled = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //initialize

            richTextBox1.Text += "cnt1 = " + imageList1.Images.Count.ToString() + "\n";
            int i;
            for (i = 1; i <= 9; i++)
            {
                imageList1.Images.Add(new Bitmap(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_0" + i.ToString() + ".jpg"));

            }

            if (imageList1.Images.Count > 0)
            {
                pictureBox1.Image = imageList1.Images[0];
                button2.Enabled = true;
                button3.Enabled = true;
            }

            richTextBox1.Text += "cnt2 = " + imageList1.Images.Count.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //previous

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //next

        }
    }
}
