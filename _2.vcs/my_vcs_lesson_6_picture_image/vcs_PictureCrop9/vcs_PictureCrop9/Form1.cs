using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_PictureCrop9
{
    public partial class Form1 : Form
    {
        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 
        Graphics g;

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        int x_st = -1;
        int y_st = -1;
        int x_sp = 0;
        int y_sp = 0;

        Image image;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            g = this.pictureBox1.CreateGraphics();

            int W = pictureBox1.Image.Width;
            int H = pictureBox1.Image.Height;

            nud_x_st.Maximum = W;
            nud_y_st.Maximum = H;
            nud_w.Maximum = W;
            nud_h.Maximum = H;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "選取")
            {
                button1.Text = "選取中";
                pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            }
            else
            {
                button1.Text = "選取";

            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            begin = true;
            firstPoint = new Point(e.X, e.Y);

            pictureBox1.MouseDown -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);

            nud_x_st.Value = e.X;
            nud_y_st.Value = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (begin == true)
            {
                //重新在pictureBox1上面繪圖
                this.Refresh();
                //獲取新的右下角坐標 
                secondPoint = new Point(e.X, e.Y);
                int minX = Math.Min(firstPoint.X, secondPoint.X);
                int minY = Math.Min(firstPoint.Y, secondPoint.Y);
                int maxX = Math.Max(firstPoint.X, secondPoint.X);
                int maxY = Math.Max(firstPoint.Y, secondPoint.Y);

                x_st = minX;
                y_st = minY;
                w = maxX - minX;
                h = maxY - minY;

                //畫矩形
                g.DrawRectangle(new Pen(Color.Red), x_st, y_st, w, h);
                nud_x_st.Value = x_st;
                nud_y_st.Value = y_st;
                nud_w.Value = w;
                nud_h.Value = h;

            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            begin = false;

            pictureBox1.MouseMove -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);
            button1.Text = "選取";

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
            pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);
        }

        private void nud_x_st_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();
        }

        private void nud_y_st_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();
        }

        private void nud_w_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();
        }

        private void nud_h_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();

        }

        void update_crop_picture()
        {
            if ((nud_x_st.Value < 0) || (nud_y_st.Value < 0) || (nud_w.Value <= 0) || (nud_h.Value <= 0))
            {
                //richTextBox1.Text += "選取位置錯誤\n";
                return;
            }

            //重新在pictureBox1上面繪圖
            this.Refresh();
            //獲取新的右下角坐標 

            x_st = (int)nud_x_st.Value;
            y_st = (int)nud_y_st.Value;
            w = (int)nud_w.Value;
            h = (int)nud_h.Value;

            //畫矩形
            g.DrawRectangle(new Pen(Color.Red), x_st, y_st, w, h);


            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
            pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);


        }
    }
}

