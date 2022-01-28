using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1testllist
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //string filename = @"C:\______test_files\picture1.jpg";
            //pictureBox1.Image = Image.FromFile(filename);

            richTextBox1.Text += "R = " + Color.Transparent.R.ToString() + "\n";
            richTextBox1.Text += "G = " + Color.Transparent.G.ToString() + "\n";
            richTextBox1.Text += "B = " + Color.Transparent.B.ToString() + "\n";
            richTextBox1.Text += "A = " + Color.Transparent.A.ToString() + "\n";
            richTextBox1.Text += "A2 = " + Color.Red.A.ToString() + "\n";

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            //清空畫布並用透明色填充
            //e.Graphics.Clear(Color.Transparent);


            Color c1 = Color.FromArgb(255, 255, 0, 0);
            SolidBrush sb1 = new SolidBrush(c1);
            e.Graphics.FillRectangle(sb1, 50, 50, 100, 100);

            Color c2 = Color.FromArgb(255, 0, 255, 0);
            SolidBrush sb2 = new SolidBrush(c2);
            e.Graphics.FillRectangle(sb2, 100, 50, 100, 100);


            Color c3 = Color.FromArgb(255, 255, 0, 0);
            SolidBrush sb3 = new SolidBrush(c3);
            e.Graphics.FillRectangle(sb3, 50, 200, 100, 100);

            Color c4 = Color.FromArgb(128, 0, 255, 0);
            SolidBrush sb4 = new SolidBrush(c4);
            e.Graphics.FillRectangle(sb4, 100, 200, 100, 100);


            //e.Graphics.FillRectangle(Brushes.Blue, 00, 320, 600, 50);
            //e.Graphics.FillRectangle(Brushes.Blue, 00, 420, 600, 50);
            /*
            int i;
            int w = 40;
            for (i = 0; i < 13; i++)
            {
                Color c5 = Color.FromArgb(255, 20 * i, 0, 0);
                SolidBrush sb5 = new SolidBrush(c5);
                e.Graphics.FillRectangle(sb5, 50 + w * i, 300, w, 100);

            }
            for (i = 0; i < 13; i++)
            {
                Color c5 = Color.FromArgb(20 * i, 255, 0, 0);
                SolidBrush sb5 = new SolidBrush(c5);
                e.Graphics.FillRectangle(sb5, 50 + w * i, 400, w, 100);

            }
            */

            Color c6 = Color.FromArgb(0, 255, 255, 255);
            SolidBrush sb5 = new SolidBrush(c6);
            e.Graphics.FillRectangle(sb5, 300, 100, 100, 100);


            e.Graphics.DrawString("格子裏", new Font("黑體", 100), new SolidBrush(c6), 300, 100);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\elephant.jpg";
            pictureBox1.Image = Image.FromFile(filename);

        }
    }
}
