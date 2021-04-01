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
        Font font = new Font("微軟正黑體", 12);

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
                    pbox[x, y].Font = font;
                    pbox[x, y].Name = "( " + x.ToString() + ", " + y.ToString() + ")";
                    pbox[x, y].BackColor = Color.Pink;
                    pbox[x, y].BorderStyle = BorderStyle.Fixed3D;
                    pbox[x, y].SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
                    pbox[x, y].Image = bitmap2;
                    //pbox[x, y].Click += PictureBoxClick;
                    //panel.Controls.Add(pbox[x, y]);
                    this.Controls.Add(pbox[x, y]);
                }
            }
        }
    }
}
