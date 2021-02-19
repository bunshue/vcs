using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat

namespace vcs_DrawImage4
{
    public partial class Form1 : Form
    {
        int W;
        int H;

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
            /*
            Graphics g = this.CreateGraphics();
            Image img = Image.FromFile("c:\\______test_files\\picture1.jpg"); //載入圖檔，由檔案
            //Bitmap bmp = Bitmap.FromFile("c:\\______test_files\\picture1.jpg"); //載入圖檔，由檔案
            Pen p = new Pen(Color.Red, 3);
            //g.DrawImage(img, 100, 100);
            g.DrawImage(img, 450, 450);

            richTextBox1.Text += "轉變坐標軸角度\n";

            for (int i = 0; i <= 20; i += 3)
            {
                g.RotateTransform(i);//旋轉指定的角度
                g.TranslateTransform(500, 500);
                //g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
                g.DrawImage(img, 0, 0);
                g.ResetTransform();//恢復坐標軸坐標 回 0 度
            }
            */

            string filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bitmap1 = new Bitmap(this.Width, this.Height);

            int W = bitmap1.Width;
            int H = bitmap1.Height;

            Graphics g = this.CreateGraphics();
            Rectangle srcRect = new Rectangle(0, 0, W, H);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;

            Point ulCorner = new Point(0, 0);
            Point urCorner = new Point(0 + W, 0);
            Point llCorner = new Point(0, 0 + H);
            Point[] destRect1 = { ulCorner, urCorner, llCorner };

            g.DrawRectangle(new Pen(Color.Red, 30), 0, 0, W, H);

            Image img = Image.FromFile("c:\\______test_files\\picture1.jpg");

            g.DrawImage(img, destRect1, srcRect, units);


            richTextBox1.Text += "轉變坐標軸角度\n";

            int x_st = 0;
            int y_st = 0;

            ulCorner = new Point(x_st + 0, y_st + 0);
            urCorner = new Point(x_st + 0 + W, y_st + 0);
            llCorner = new Point(x_st + 0, y_st + 0 + H);
            Point[] destRect2 = { ulCorner, urCorner, llCorner };
            
            for (int i = 0; i <= 20; i += 3)
            {
                g.DrawRectangle(new Pen(Color.Red, 5), 0, 0, 200, 200);
                g.RotateTransform(i);//旋轉指定的角度
                g.TranslateTransform(600, 0);
                //g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
                g.DrawImage(img, destRect2, srcRect, units);
                g.ResetTransform();//恢復坐標軸坐標 回 0 度
            }






        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bitmap1 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            //pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            this.BackgroundImage = bitmap1;

        }

    }
}
