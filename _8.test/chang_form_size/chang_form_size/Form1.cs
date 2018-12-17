using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace chang_form_size
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = Image.FromFile(@"D:\bear.jpg");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Size = new Size(300, 300);
            button7.Size = new Size(130, 30);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Size = new Size(600, 600);
            button7.Size = new Size(260, 60);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(150, 150);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(350, 350);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Size = new Size(DefaultSize.Width, DefaultSize.Height);
            richTextBox1.Text += "w = " + DefaultSize.Width.ToString() + " h = " + DefaultSize.Height.ToString();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "w = " + DefaultSize.Width.ToString() + " h = " + DefaultSize.Height.ToString() + "\n";
            richTextBox1.Text += "w = " + this.Width.ToString() + " h = " + this.Height.ToString() + "\n";
            richTextBox1.Text += "w = " + this.ClientSize.Width.ToString() + " h = " + this.ClientSize.Height.ToString() + "\n";
        }

        private void richTextBox1_Enter(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();


        }
    }
}
