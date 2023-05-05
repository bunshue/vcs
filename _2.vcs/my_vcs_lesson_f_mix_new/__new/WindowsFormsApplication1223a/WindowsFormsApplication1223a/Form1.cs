using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace WindowsFormsApplication1223a
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\airplane.bmp";

        int x_st;
        int y_st;
        int dx = 20;
        int dy = 20;
        int W;
        int H;
        int w;
        int h;
        int pic_w = 100;
        int pic_h = 100;

        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            
            Image image = Image.FromFile(filename);
            //pictureBox1.Image = image;

            w = image.Width;
            h = image.Height;

            label3.Text = w.ToString() + " X " + h.ToString();


            W = pictureBox1.Width;
            H = pictureBox1.Height;

            x_st = W / 2 - pic_w / 2;
            y_st = H;
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            label1.Text = "按動的鍵為：" + e.KeyCode.ToString() + "\n";



        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //響應鼠標的不同按鍵 
            if (e.Button == MouseButtons.Left)
            {
                label1.Text = "按動鼠標左鍵！";
            }
            if (e.Button == MouseButtons.Middle)
            {
                label1.Text = "按動鼠標中鍵！";
            }
            if (e.Button == MouseButtons.Right)
            {
                label1.Text = "按動鼠標右鍵！";
            }


        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            label2.Text = "當前鼠標的位置為：( " + e.X + " , " + e.Y + ")";

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Image image = Image.FromFile(filename);

            //richTextBox1.Text += "(" + x_st.ToString() + ", " + y_st.ToString() + ") ";
            e.Graphics.DrawImage(image, x_st, y_st, pic_w, pic_h);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //x_st += dx;
            y_st -= dy;

            if (y_st < 0)
            {
                y_st = H;
            }

            this.pictureBox1.Invalidate();

        }

    }
}
