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
        Image image;
        int W = 0;
        int H = 0;

        string filename = @"C:\______test_files\picture1.jpg";
        bool flag_mouse_down = false;

        int x_st = 0;
        int y_st = 0;
        int x_sp = 0;
        int y_sp = 0;

        int w = 0;
        int h = 0;
        Rectangle cropRectangle = new Rectangle(new Point(0, 0), new Size(0, 0));

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

            //試著在啟動時就把預設截取位置畫出來
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = true;
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
            if (flag_mouse_down == true)
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
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = false;

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

            cropRectangle = new Rectangle(x_st2, y_st2, w, h);
        }

        private void pictureBox2_MouseDown(object sender, MouseEventArgs e)
        {
            try
            {
                Graphics g2 = this.pictureBox2.CreateGraphics();
                Bitmap bitmap = new Bitmap(pictureBox1.Image);
                Bitmap cloneBitmap = bitmap.Clone(cropRectangle, PixelFormat.DontCare);
                g2.DrawImage(cloneBitmap, e.X, e.Y);
                /* 原本圖要不要塗白  像是剪下
                Graphics g1 = pictureBox1.CreateGraphics();
                SolidBrush myBrush = new SolidBrush(Color.White);
                g1.FillRectangle(myBrush, cropRectangle);
                */
            }
            catch
            { }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            Bitmap bitmap = new Bitmap(pictureBox1.Image);
            Bitmap cloneBitmap = bitmap.Clone(cropRectangle, PixelFormat.DontCare);
            cloneBitmap.Save(filename, ImageFormat.Bmp);
            richTextBox1.Text += "存截圖，存檔檔名：" + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            Bitmap bitmap = new Bitmap(pictureBox1.Image);
            cropRectangle = new Rectangle(x_st, y_st, 200, 200);
            richTextBox1.Text += cropRectangle.ToString() + "\n";
            Bitmap cloneBitmap = bitmap.Clone(cropRectangle, PixelFormat.DontCare);
            cloneBitmap.Save(filename, ImageFormat.Bmp);
            richTextBox1.Text += "存截圖，存檔檔名：" + filename + "\n";
        }
    }
}
