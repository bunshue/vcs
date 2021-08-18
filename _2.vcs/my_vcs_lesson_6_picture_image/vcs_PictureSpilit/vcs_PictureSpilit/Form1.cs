using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_PictureSpilit
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        PictureBox[,] pbox = new PictureBox[3, 3];

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            //pictureBox1.Image = Image.FromFile(filename);

            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int C = 4;
            int R = 3;
            int x_st = 100;
            int y_st = 100;
            int w = W / C;
            int h = H / R;
            int dx = w * 12 / 10;
            int dy = h * 12 / 10;

            Bitmap bitmap2 = new Bitmap(w, h);
            RectangleF rect;
            pbox = new PictureBox[C, R];

            Random r = new Random();

            for (int x = 0; x < pbox.GetLength(0); x++)
            {
                for (int y = 0; y < pbox.GetLength(1); y++)
                {
                    rect = new RectangleF(x * w, y * h, w, h);
                    bitmap2 = bitmap1.Clone(rect, PixelFormat.Format32bppArgb);

                    pbox[x, y] = new PictureBox();
                    pbox[x, y].Size = new Size(w, h);
                    pbox[x, y].Text = "";
                    pbox[x, y].Location = new Point(x_st + x * dx, y_st + y * dy);
                    //pbox[x, y].Location = new Point(x_st + r.Next(400), y_st + r.Next(400));
                    pbox[x, y].Name = "( " + x.ToString() + ", " + y.ToString() + ")";
                    pbox[x, y].BackColor = Color.Pink;
                    pbox[x, y].BorderStyle = BorderStyle.None;
                    pbox[x, y].SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
                    pbox[x, y].Image = bitmap2;
                    pbox[x, y].MouseDown += PictureBox_MouseDown;
                    pbox[x, y].MouseMove += PictureBox_MouseMove;
                    pbox[x, y].MouseUp += PictureBox_MouseUp;
                    //panel.Controls.Add(pbox[x, y]);
                    this.Controls.Add(pbox[x, y]);
                }
            }
        }

        bool flag_pictureBox_mouse_down = false;
        int pictureBox_position_x_old = 0;
        int pictureBox_position_y_old = 0;
        private void PictureBox_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pictureBox_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pictureBox_position_x_old = e.X;
            pictureBox_position_y_old = e.Y;
            ((PictureBox)sender).BringToFront();    //選中的那一片拉到最上層顯示
        }

        private void PictureBox_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pictureBox_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pictureBox_position_x_old;
                int dy = e.Y - pictureBox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
            }
        }

        private void PictureBox_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pictureBox_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pictureBox_position_x_old;
            int dy = e.Y - pictureBox_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            ((PictureBox)sender).Location = new Point(((PictureBox)sender).Location.X + dx, ((PictureBox)sender).Location.Y + dy);
        }






    }
}
