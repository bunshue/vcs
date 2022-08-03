using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;   //for DashStyle

//在 pictureBox 上用滑鼠畫矩形
//mode 0 : pictureBox 無圖片
//mode 1 : pictureBox 有圖片

namespace draw_rectangle
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        private bool flag_mouse_down = false;
        private int intStartX = 0;
        private int intStartY = 0;

        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));    //用來保存截圖的矩形

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        //private int w = 0;  //擷取圖的寬
        //private int h = 0;  //擷取圖的高

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int pbx_W = 900;
            int pbx_H = 600;

            x_st = 10;
            y_st = 10;
            dx = pbx_W + 10;
            dy = pbx_H + 10;

            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            //跟隨鼠標在 pictureBox 的圖片上畫矩形
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private Rectangle MakeRectangle(Point pt1, Point pt2)
        {
            return new Rectangle(Math.Min(pt1.X, pt2.X), Math.Min(pt1.Y, pt2.Y), Math.Abs(pt1.X - pt2.X), Math.Abs(pt1.Y - pt2.Y));
        }

        // Start selecting the rectangle.
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
            pt_st = e.Location; //起始點座標
            intStartX = e.X;
            intStartY = e.Y;

            nud_w.Value = 0;
            nud_h.Value = 0;
            nud_x_st.Value = 0;
            nud_y_st.Value = 0;

            //label2.Text = "";
            SelectionRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                pt_sp = e.Location; //終點座標

                SelectionRectangle = MakeRectangle(pt_st, pt_sp);

                /*
                if ((SelectionRectangle.X < 0) || (SelectionRectangle.X >= W))
                    return;
                if ((SelectionRectangle.Y < 0) || (SelectionRectangle.Y >= H))
                    return;
                if ((SelectionRectangle.Width <= 0) || (SelectionRectangle.Width > W))
                    return;
                if ((SelectionRectangle.Height <= 0) || (SelectionRectangle.Height > H))
                    return;
                if (((SelectionRectangle.X + SelectionRectangle.Width) > W) || ((SelectionRectangle.Y + SelectionRectangle.Height) > H))
                    return;
                */

                try
                {
                    //Image tmp = Image.FromFile("1.png");
                    Graphics g = this.pictureBox1.CreateGraphics();
                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox1.BackColor);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    //g.DrawEllipse(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.Dispose();
                    //this.pictureBox_Src.Image = tmp;
                }
                catch (Exception ex)
                {
                    ex.ToString();
                }

                nud_x_st.Value = SelectionRectangle.X;
                nud_y_st.Value = SelectionRectangle.Y;
                nud_w.Value = SelectionRectangle.Width;
                nud_h.Value = SelectionRectangle.Height;
                //label2.Text = "選取區域 : " + SelectionRectangle.ToString();
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (flag_mouse_down == false)
            {
                return;
            }
            flag_mouse_down = false;
            intStartX = 0;
            intStartY = 0;


            /*
            // Display the original image.
            //pictureBox1.Image = bitmap1;  //仍應保留選取區域

            int w = SelectionRectangle.Width;
            int h = SelectionRectangle.Height;

            if (w < 1)
                return;
            if (h < 1)
                return;

            bitmap2 = new Bitmap(w, h);  //擷取部分位圖Bitmap
            using (Graphics g2 = Graphics.FromImage(bitmap2))
            {
                Rectangle dest_rectangle = new Rectangle(0, 0, w, h);
                g2.DrawImage(bitmap1, dest_rectangle, SelectionRectangle, GraphicsUnit.Pixel);
            }

            //pictureBox2.Image = bitmap2;
            */

            //richTextBox1.Text += "SelectionRectangle = " + SelectionRectangle.ToString() + "\n";

            nud_x_st.Value = SelectionRectangle.X;
            nud_y_st.Value = SelectionRectangle.Y;
            nud_w.Value = SelectionRectangle.Width;
            nud_h.Value = SelectionRectangle.Height;
            //label2.Text = "選取區域 : " + SelectionRectangle.ToString();
        }
    }
}

