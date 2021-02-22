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
        private Point DownPoint = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point UpPoint = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private bool CatchFinished = false;//用來表示是否截圖完成
        private bool CatchStart = false;//表示截圖開始
        private Bitmap originBmp;//用來保存原始圖像
        private Rectangle CatchRect;//用來保存截圖的矩形
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
            originBmp = new Bitmap(this.BackgroundImage);//BackgroundImage為全屏圖片，我們另用變量來保存全屏圖片
            W = this.BackgroundImage.Width;
            H = this.BackgroundImage.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "down point = (" + DownPoint.X.ToString() + ", " + DownPoint.Y.ToString() + ")\n";
            richTextBox1.Text += "down point = (" + UpPoint.X.ToString() + ", " + UpPoint.Y.ToString() + ")\n";
            int w = Math.Abs(UpPoint.X - DownPoint.X) + 1;
            int h = Math.Abs(UpPoint.Y - DownPoint.Y) + 1;
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                if (CatchStart == false)    //如果捕捉沒有開始
                {
                    CatchStart = true;
                    DownPoint = new Point(e.X, e.Y);    //保存鼠標按下時的坐標
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (CatchStart == true) //如果捕捉開始
            {
                Bitmap destBmp = (Bitmap)originBmp.Clone();//新建一個圖片對象，並讓它與原始圖片相同
                Point newPoint = new Point(DownPoint.X, DownPoint.Y);//獲取鼠標的坐標
                Graphics g = Graphics.FromImage(destBmp);//在剛才新建的圖片上新建一個畫板
                Pen p = new Pen(Color.Blue, 1);
                int width = Math.Abs(e.X - DownPoint.X);
                int height = Math.Abs(e.Y - DownPoint.Y);   //獲取矩形的長和寬

                if (e.X < DownPoint.X)
                {
                    newPoint.X = e.X;
                }
                if (e.Y < DownPoint.Y)
                {
                    newPoint.Y = e.Y;
                }
                CatchRect = new Rectangle(newPoint, new Size(width, height));//保存矩形
                g.DrawRectangle(p, CatchRect);//將矩形畫在這個畫板上
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
                if (CatchStart == true)
                {
                    UpPoint = new Point(e.X, e.Y);//保存鼠標放開時的坐標
                    CatchStart = false;
                    CatchFinished = true;

                    richTextBox1.Text += "down point = (" + DownPoint.X.ToString() + ", " + DownPoint.Y.ToString() + ")\n";
                    richTextBox1.Text += "down point = (" + UpPoint.X.ToString() + ", " + UpPoint.Y.ToString() + ")\n";
                    int w = Math.Abs(UpPoint.X - DownPoint.X) + 1;
                    int h = Math.Abs(UpPoint.Y - DownPoint.Y) + 1;
                    richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

                    int sx = DownPoint.X;
                    int sy = DownPoint.Y;
                    int sw = w;
                    int sh = h;
                    Rectangle srcRect = new Rectangle(sx, sy, sw, sh);   //擷取部分區域

                    //指定畫布大小
                    pictureBox1.Width = sw;
                    pictureBox1.Height = sh;
                    Bitmap bitmap1;

                    string filename = "C:\\______test_files\\picture1.jpg";
                    bitmap1 = new Bitmap(filename);

                    if (((sx + sw) >= W) || ((sy + sh) >= H))
                        return;

                    Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

                    //將處理之後的圖片貼出來
                    pictureBox1.Image = bitmap1.Clone(srcRect, PixelFormat.Format32bppArgb);
                    g.Dispose();
                    bitmap1.Dispose();
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {

        }

    }
}
