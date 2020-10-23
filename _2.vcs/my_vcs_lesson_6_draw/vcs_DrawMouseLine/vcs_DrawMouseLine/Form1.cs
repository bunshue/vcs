using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawMouseLine
{
    public partial class Form1 : Form
    {
        Point[] pt = new Point[100];
        int pt_index = -1;
        Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (pt_index < pt.Length) // 如果一維陣列內的 100 個位置還沒裝滿
            {
                pt_index++;  // 一維陣列 的索引往前
                pt[pt_index] = new Point(e.X, e.Y); // 存入 滑鼠游標位置
                //this.Text = pt_index.ToString();
                this.Text = e.X.ToString() + ", " + e.Y.ToString();
                this.Invalidate(); // 要求表單重畫
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            /*
            for (int i = 0; i <= pt_index; i++)
            {
                e.Graphics.DrawImage(img,
                pt[i].X - img.Width / 2, pt[i].Y - img.Height / 2, //影像左上角在表單的位置
                img.Width, img.Height); //影像的寬高

            }
            */
            richTextBox1.Text += "index " + pt_index.ToString() + "\n";

            if (pt_index < 1)
                return;

            Point[] pt2 = new Point[pt_index + 1];
            int i;
            for (i = 0; i <= pt_index; i++)
            {
                pt2[i] = pt[i];
            }

            e.Graphics.DrawLines(new Pen(Color.Red, 2), pt2);



        }
    }
}
