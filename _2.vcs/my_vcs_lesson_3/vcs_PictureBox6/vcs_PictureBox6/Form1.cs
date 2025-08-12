using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_PictureBox6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_computer\burn1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
            pictureBox1.BackColor = Color.Pink;

        }

        private void Form1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Form1 ";
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pictureBox1 ";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //做一個圓形的pictureBox
            // Make a Rectangle that defines the circular area.
            Rectangle rect = new Rectangle(15, 15, 200, 200);

            // Make a GraphicsPath and add the circle.
            GraphicsPath path = new GraphicsPath();
            path.AddEllipse(rect);

            // Convert the GraphicsPath into a Region.
            Region region = new Region(path);

            // Restrict the PictureBoxes to the Region.
            pictureBox1.Region = region;

        }
    }
}
