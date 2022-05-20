using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat

namespace vcs_PictureCrop8
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.bmp";

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        int x_st = 0;
        int y_st = 0;
        int x_sp = 0;
        int y_sp = 0;

        Image image;

        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            image = System.Drawing.Image.FromFile(filename);
            W = image.Width;
            H = image.Height;
            pictureBox1.Image = image;
            pictureBox1.Width = W;
            pictureBox1.Height = H;
            int w = 100;
            int h = 100;
            tb_w.Text = w.ToString();
            tb_h.Text = h.ToString();
            x_st = (W - w) / 2;
            y_st = (H - h) / 2;

            tb_x_st.Text = x_st.ToString();
            tb_y_st.Text = y_st.ToString();

            select_rectangle = MakeRectangle(x_st, y_st, x_st + w, y_st + h);


            //試著在啟動時就把預設截取位置畫出來
        }

        // Return a Rectangle with these points as corners.
        private Rectangle MakeRectangle(int x0, int y0, int x1, int y1)
        {
            return new Rectangle(Math.Min(x0, x1), Math.Min(y0, y1), Math.Abs(x0 - x1), Math.Abs(y0 - y1));
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_select_area = true;
            x_st = e.X;
            y_st = e.Y;

            Graphics g = pictureBox1.CreateGraphics();
            g.DrawLine(new Pen(Color.Black, 1), new Point(e.X, 0), new Point(e.X, H));
            g.DrawLine(new Pen(Color.Black, 1), new Point(0, e.Y), new Point(W, e.Y));
            //g.DrawLine(new Pen(Color.Black, 1), new Point(0, e.Y), new Point(e.X, e.Y));
            //g.DrawLine(new Pen(Color.Black, 1), new Point(e.X, e.Y), new Point(W - e.X, e.Y));
            //Application.DoEvents();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            /*
            //恢復原狀
            pictureBox1.Image = image;
            */
            if (flag_select_area == true)
            {
                int x_st2 = x_st;
                int y_st2 = y_st;

                x_sp = e.X;
                y_sp = e.Y;

                if (x_sp > x_st)
                    w = x_sp - x_st;
                else
                {
                    w = x_st - x_sp;
                    x_st2 = x_sp;
                }

                if (y_sp > y_st)
                    h = y_sp - y_st;
                else
                {
                    h = y_st - y_sp;
                    y_st2 = y_sp;
                }

                //恢復原狀
                pictureBox1.Image = image;

                Application.DoEvents();

                Graphics g = pictureBox1.CreateGraphics();
                g.DrawRectangle(new Pen(Color.Red, 1), x_st2, y_st2, w, h);


                nud_x_st.Value = (decimal)x_st2;
                nud_y_st.Value = (decimal)y_st2;
                nud_w.Value = (decimal)w;
                nud_h.Value = (decimal)h;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_select_area = false;

            int x_st2 = x_st;
            int y_st2 = y_st;

            x_sp = e.X;
            y_sp = e.Y;

            if (x_sp > x_st)
                w = x_sp - x_st;
            else
            {
                w = x_st - x_sp;
                x_st2 = x_sp;
                x_st = x_sp;
            }

            if (y_sp > y_st)
                h = y_sp - y_st;
            else
            {
                h = y_st - y_sp;
                y_st2 = y_sp;
                y_st = y_sp;
            }

            //恢復原狀
            pictureBox1.Image = image;
            Application.DoEvents();

            Graphics g = pictureBox1.CreateGraphics();
            g.DrawRectangle(new Pen(Color.Red, 1), x_st2, y_st2, w, h);

            select_rectangle = new Rectangle(x_st2, y_st2, w, h);
                                                                            tb_x_st.Text = x_st2.ToString();
                                                                            tb_y_st.Text = y_st2.ToString();
                                                                            tb_w.Text = w.ToString();
                                                                            tb_h.Text = h.ToString();
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            try
            {
                Graphics g2 = this.pictureBox2.CreateGraphics();
                Bitmap bitmap = new Bitmap(pictureBox1.Image);
                Bitmap cloneBitmap = bitmap.Clone(select_rectangle, PixelFormat.DontCare);
                g2.DrawImage(cloneBitmap, e.X, e.Y);
                /* 原本圖要不要塗白  像是剪下
                Graphics g1 = pictureBox1.CreateGraphics();
                SolidBrush myBrush = new SolidBrush(Color.White);
                g1.FillRectangle(myBrush, select_rectangle);
                */
            }
            catch
            { }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            Bitmap bitmap = new Bitmap(pictureBox1.Image);
            Bitmap cloneBitmap = bitmap.Clone(select_rectangle, PixelFormat.DontCare);
            cloneBitmap.Save(filename, ImageFormat.Bmp);
            richTextBox1.Text += "存截圖，存檔檔名：" + filename + "\n";
        }


    }
}
