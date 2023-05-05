using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat

namespace vcs_Draw5_Image3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            this.UpdateStyles();
            //以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題，關於這個大家可以自己去搜索下

            //this.FormBorderStyle = FormBorderStyle.None;
            //this.WindowState = FormWindowState.Maximized;
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;

            Bitmap bitmap1 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap1);

            Pen p = new Pen(Color.Gray, 1);

            int i;
            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(p, i, 0, i, H);
            }
            for (i = 0; i <= H; i += 100)
            {
                g.DrawLine(p, 0, i, W, i);
            }


            Rectangle srcRect = new Rectangle(0, 0, W, H);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;
            Image img = Image.FromFile(filename);


            int x_st = 0;
            int y_st = 0;
            int angle = 0;

            Point ulCorner = new Point(0, 0);
            Point urCorner = new Point(W, 0);
            Point llCorner = new Point(0, H);
            Point[] destRect = { ulCorner, urCorner, llCorner };

            x_st = 350 * 0;
            y_st = 200;
            angle = -10;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, srcRect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度


            x_st = 350 * 1;
            y_st = 200;
            angle = 0;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, srcRect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度


            x_st = 350 * 2;
            y_st = 200;
            angle = 10;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, srcRect, units);
                g.ResetTransform();//恢復坐標軸坐標 回 0 度





            pictureBox1.Image = bitmap1;
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bitmap1 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            this.BackgroundImage = bitmap1;

        }

    }
}
