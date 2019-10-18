using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace testtest
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            int width, height;
            width = this.ClientSize.Width;
            height = this.ClientSize.Height;
            p = new Pen(Color.Blue, 5);
            e.Graphics.Clear(Color.Gray);
            e.Graphics.DrawRectangle(p, 0, 0, width - 1, height - 1);
            */
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //p = new Pen(Color.Red, 5);
            int width, height;
            width = pictureBox1.ClientSize.Width;
            height = pictureBox1.ClientSize.Height;
            g.Clear(Color.LightGreen);
            g.DrawRectangle(p, 0, 0, width - 1, height - 1);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     //default pen

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            SolidBrush sb = new SolidBrush(Color.Gold);
            p = new Pen(sb, 10);
            richTextBox1.Text += "SolidBrush\n";
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            TextureBrush tb = new TextureBrush(new Bitmap(@"C:\______test_files\bear.jpg"));
            p = new Pen(tb, 10);
            richTextBox1.Text += "TextureBrush\n";
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
            p = new Pen(hb, 10);
            richTextBox1.Text += "HatchBrush\n";
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
            LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
            p = new Pen(lgb, 10);
            richTextBox1.Text += "LinearGradientBrush\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //g.Clear(Color.LightGreen);
            p.Width = 10;
            for (int i = 0; i <= pictureBox1.Width; i = i + 36)
            {
                g.DrawLine(p, i, 0, i, pictureBox1.Height);
                p.Width += 2;
            }
        }
    }
}
