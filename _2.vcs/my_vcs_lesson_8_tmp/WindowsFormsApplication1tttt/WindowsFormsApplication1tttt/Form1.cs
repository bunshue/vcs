using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1tttt
{
    public partial class Form1 : Form
    {
        Graphics g;

        public Form1()
        {
            InitializeComponent();
            richTextBox1.Text += "aaaaa\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            g.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));


        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "bbbbbb\n";
            draw_something();

        }

        void draw_something()
        {
            richTextBox1.Text += "draw_something ST\n";
            g = this.CreateGraphics();
            g.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));
            richTextBox1.Text += "draw_something SP\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Refresh();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            richTextBox1.Text += "paint ST\n";
            g = this.CreateGraphics();
            g.DrawString("驗證完成", new Font("標楷體", 60), new SolidBrush(Color.Blue), new PointF(20, 20));

        }
    }
}
