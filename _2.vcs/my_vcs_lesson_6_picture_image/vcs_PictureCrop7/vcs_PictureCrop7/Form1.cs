using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat

namespace vcs_PictureCrop7
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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
                                                            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
                                                            this.UpdateStyles();
                                                            //以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題

                                                            bitmap1 = new Bitmap(filename);
                                                            pictureBox1.Image = bitmap1;

                                                            W = bitmap1.Width;
                                                            H = bitmap1.Height;
                                                            pictureBox1.ClientSize = new Size(W, H);
                                                            pictureBox2.ClientSize = new Size(W, H);
                                                            
            
            
            bitmap1 = new Bitmap(this.BackgroundImage);//BackgroundImage為全屏圖片，我們另用變量來保存全屏圖片
            W = this.BackgroundImage.Width;
            H = this.BackgroundImage.Height;

            /*
            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = new Bitmap(filename);
            W = bitmap1.Width;
            H = bitmap1.Height;
            pictureBox1.Image = bitmap1;
            */
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

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                if (flag_select_area == false)    //如果捕捉沒有開始
                {
                    flag_select_area = true;
                    pt_st = e.Location;    //保存鼠標按下時的坐標
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_select_area == true) //如果捕捉開始
            {
                Bitmap destBmp = (Bitmap)bitmap1.Clone();//新建一個圖片對象，並讓它與原始圖片相同
                Point newPoint = new Point(pt_st.X, pt_st.Y);//獲取鼠標的坐標
                Graphics g = Graphics.FromImage(destBmp);//在剛才新建的圖片上新建一個畫板
                Pen p = new Pen(Color.Blue, 1);
                int width = Math.Abs(e.X - pt_st.X);
                int height = Math.Abs(e.Y - pt_st.Y);   //獲取矩形的長和寬

                if (e.X < pt_st.X)
                {
                    newPoint.X = e.X;
                }
                if (e.Y < pt_st.Y)
                {
                    newPoint.Y = e.Y;
                }
                select_rectangle = new Rectangle(newPoint, new Size(width, height));//保存矩形
                g.DrawRectangle(p, select_rectangle);//將矩形畫在這個畫板上
                g.Dispose();//釋放目前的這個畫板
                p.Dispose();

                Graphics g1 = this.CreateGraphics();//重新新建一個Graphics類
                //如果之前那個畫板不釋放，而直接g=this.CreateGraphics()這樣的話無法釋放掉第一次創建的g,因為只是把地址轉到新的g了．如同string一樣
                g1 = this.CreateGraphics();//在整個全屏窗體上新建畫板
                g1.DrawImage(destBmp, new Point(0, 0));//將剛才所畫的圖片畫到這個窗體上
                //這個也可以屬於二次緩沖技術，如果直接將矩形畫在窗體上，會造成圖片抖動並且會有無數個矩形．
                g1.Dispose();
                destBmp.Dispose();//要及時釋放，不然內存將會被大量消耗
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                if (flag_select_area == true)
                {
                    pt_sp = e.Location;//保存鼠標放開時的坐標
                    flag_select_area = false;

                    int w = Math.Abs(pt_sp.X - pt_st.X) + 1;
                    int h = Math.Abs(pt_sp.Y - pt_st.Y) + 1;

                    int sx = pt_st.X;
                    int sy = pt_st.Y;
                    int sw = w;
                    int sh = h;
                    Rectangle srcRect = new Rectangle(sx, sy, sw, sh);   //擷取部分區域

                    //指定畫布大小
                    pictureBox2.Width = sw;
                    pictureBox2.Height = sh;
                    Bitmap bitmap1;

                    string filename = "C:\\______test_files\\picture1.jpg";
                    bitmap1 = new Bitmap(filename);

                    if (((sx + sw) >= W) || ((sy + sh) >= H))
                        return;

                    Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

                    //將處理之後的圖片貼出來
                    pictureBox2.Image = bitmap1.Clone(srcRect, PixelFormat.Format32bppArgb);
                    g.Dispose();
                    bitmap1.Dispose();
                }
            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

    }
}
