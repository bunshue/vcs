using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace draw_test
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bit = new Bitmap(100, 30);
            Graphics g = Graphics.FromImage(bit);
            SolidBrush sb = new SolidBrush(Color.Blue);
            Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
            g.FillRectangle(sb, rg);
            g.DrawString("測試測試呵呵", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
            bit.Save("d://123.bmp");//保存下來這個可以看生成的圖片 

        }

        private void button2_Click(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            //p = new Pen(Color.Red);
            p = new Pen(Color.Red, 10);
            g.DrawRectangle(p, 20,20,300,150);
            g.DrawRectangle(p, 0, 0, this.ClientSize.Width - 1,this.ClientSize.Height - 1); //  外框矩形

        }

        private void button3_Click(object sender, EventArgs e)
        {
            g = this.CreateGraphics();
            //p = new Pen(Color.Red);
            p = new Pen(Color.Red, 3);

            g.DrawRectangle(p, 20, 20, 300, 150);


        }
    }
}
