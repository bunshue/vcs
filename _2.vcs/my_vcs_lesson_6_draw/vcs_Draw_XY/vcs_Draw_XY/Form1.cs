using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode

namespace vcs_Draw_XY
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            pictureBox1.Image = null;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            int[] data_in = new int[256];
            int[] data_out = new int[256];

            double gamma;
            gamma = 2.2;

            for (i = 0; i < 256; i++)
            {
                data_in[i] = i;
                data_out[i] = (int)(Math.Sin(i) * 100 + 100);
                //data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

            }


            plotXY(data_in, data_out);



        }

        void plotXY(int[] x, int[] y)
        {
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            richTextBox1.Text += "x_len = " + x.Length.ToString() + "\n";
            richTextBox1.Text += "y_len = " + y.Length.ToString() + "\n";

            int x_ratio = W / x.Length;
            int y_ratio = H / y.Length;

            richTextBox1.Text += "x_ratio = " + x_ratio.ToString() + "\n";
            richTextBox1.Text += "y_ratio = " + y_ratio.ToString() + "\n";

            g.Clear(Color.White);

            int i;
            //double gamma;

            //int[] data_in = new int[256];
            //int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            //gamma = 2.2;
            //畫出真正的Gamma 2.2曲線
            for (i = 0; i < 256; i++)
            {
                //data_in[i] = x[i];
                //data_out[i] = y[i];

                curvePoints[i].X = x[i] * x_ratio;
                curvePoints[i].Y = H - y[i] * y_ratio;
            }
            g.DrawLines(gammaPen, curvePoints);   //畫直線

            g.DrawRectangle(new Pen(Color.Red), new Rectangle(0, 0, W - 1, H - 1));

            pictureBox1.Image = bitmap1;


        }






    }
}
