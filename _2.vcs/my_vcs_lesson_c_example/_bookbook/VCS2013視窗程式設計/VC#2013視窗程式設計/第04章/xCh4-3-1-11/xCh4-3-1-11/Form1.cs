using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_3_1_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Image image1 = Image.FromFile("c:\\MyImages\\一頁書.jpg");
            pictureBox1.ClientSize = new Size(512, 384);
            pictureBox1.Image = image1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Image image1 = new Bitmap(@"C:\MyImages\南宮恨.jpg", true);
            pictureBox1.ClientSize = new Size(400, 267);
            pictureBox1.Image = image1;	
        }

        private void button3_Click(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(800, 512);
            pictureBox1.ImageLocation = "file:///c:/MyImages/素還真.png";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(400, 480);
            pictureBox1.Load("file:///c:/MyImages/妙築玄華.jpg");
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1.Text = "一頁書";
            button2.Text = "黑白郎君";
            button3.Text = "素還真";
            button4.Text = "妙築玄華";
            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;
        }
    }
}
