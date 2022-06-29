using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ScreenCapture2
{
    public partial class Form2 : Form
    {
        private Point DownPoint = Point.Empty;//記錄鼠標按下坐標，用來確定繪圖起點
        private bool CatchFinished = false;//用來表示是否截圖完成
        private bool CatchStart = false;//表示截圖開始
        private Bitmap originBmp;//用來保存原始圖像
        private Rectangle CatchRect;//用來保存截圖的矩形


        public Form2()
        {
            InitializeComponent();
        }

        private void Form2_Load(object sender, EventArgs e)
        {
            ////FormBorderStyle為None,WindowState為Maximized．

            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;


            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            this.UpdateStyles();
            //以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題，關於這個大家可以自己去搜索下
            originBmp = new Bitmap(this.BackgroundImage);//BackgroundImage為全屏圖片，我們另用變量來保存全屏圖片


            this.MouseClick += new MouseEventHandler(Form2_MouseClick);
            this.MouseDown += new MouseEventHandler(Form2_MouseDown);
            this.MouseMove += new MouseEventHandler(Form2_MouseMove);
            this.MouseUp += new MouseEventHandler(Form2_MouseUp);
            this.MouseDoubleClick += new MouseEventHandler(Form2_MouseDoubleClick);

        }

        //鼠標右鍵點擊結束截圖
        private void Form2_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                this.DialogResult = DialogResult.OK;
                this.Close();
            }
        }
        //鼠標左鍵按下時動作
        private void Form2_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                if (!CatchStart)
                {//如果捕捉沒有開始
                    CatchStart = true;
                    DownPoint = new Point(e.X, e.Y);//保存鼠標按下坐標
                }
            }
        }

        private void Form2_MouseMove(object sender, MouseEventArgs e)
        {
            if (CatchStart)
            {//如果捕捉開始
                Bitmap destBmp = (Bitmap)originBmp.Clone();//新建一個圖片對象，並讓它與原始圖片相同
                Point newPoint = new Point(DownPoint.X, DownPoint.Y);//獲取鼠標的坐標
                Graphics g = Graphics.FromImage(destBmp);//在剛才新建的圖片上新建一個畫板
                Pen p = new Pen(Color.Blue, 1);
                int width = Math.Abs(e.X - DownPoint.X), height = Math.Abs(e.Y - DownPoint.Y);//獲取矩形的長和寬
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

        private void Form2_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                if (CatchStart)
                {
                    CatchStart = false;
                    CatchFinished = true;
                }
            }
        }

        //鼠標雙擊事件，如果鼠標位於矩形內，則將矩形內的圖片保存到剪貼板中
        private void Form2_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left && CatchFinished)
            {
                if (CatchRect.Contains(new Point(e.X, e.Y)))
                {
                    Bitmap CatchedBmp = new Bitmap(CatchRect.Width, CatchRect.Height);//新建一個於矩形等大的空白圖片
                    Graphics g = Graphics.FromImage(CatchedBmp);
                    g.DrawImage(originBmp, new Rectangle(0, 0, CatchRect.Width, CatchRect.Height), CatchRect, GraphicsUnit.Pixel);
                    //把orginBmp中的指定部分按照指定大小畫在畫板上
                    Clipboard.SetImage(CatchedBmp);//將圖片保存到剪貼板
                    g.Dispose();
                    CatchFinished = false;
                    this.BackgroundImage = originBmp;
                    CatchedBmp.Dispose();
                    this.DialogResult = DialogResult.OK;
                    this.Close();
                }
            }
        }
    }
}
