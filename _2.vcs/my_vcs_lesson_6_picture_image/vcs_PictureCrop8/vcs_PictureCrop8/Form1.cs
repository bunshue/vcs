using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureCrop8
{
    public partial class Form1 : Form
    {
        //private static ScreenBody screenBody = null;
        //private static Form2 screenBody = null;

        private bool CatchStart;//判斷滑鼠是否按下
        private bool CatchFinished;//判斷矩形是否繪製完成
        private Point DownPoint;//滑鼠按下的點
        private Image baseMap;//最基本的圖片
        private Rectangle CatchRectangle;  

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\doraemon1.jpg";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            baseMap = Image.FromFile(filename);
            this.BackgroundImage = baseMap;

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //滑鼠左鍵按下就是開始畫圖，也就是截圖
            if (e.Button == MouseButtons.Left)
            {
                if (CatchStart == false)
                {
                    CatchStart = true;
                    //儲存此時的座標
                    DownPoint = new Point(e.X, e.Y);
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            //確保截圖開始
            if (CatchStart)
            {
                //新建一個圖片，讓它與螢幕圖片相同
                Bitmap copyBmp = (Bitmap)baseMap.Clone();
                //滑鼠按下時的座標
                Point newPoint = new Point(DownPoint.X, DownPoint.Y);

                //新建畫板和畫筆
                Graphics g = Graphics.FromImage(copyBmp);
                Pen p = new Pen(Color.Azure, 1);//畫筆的顏色為azure 寬度為1

                //獲取矩形的長度 
                int width = Math.Abs(e.X - DownPoint.Y);
                int height = Math.Abs(e.Y - DownPoint.Y);

                if (e.X < DownPoint.X)
                {
                    newPoint.X = e.X;

        }
                if (e.Y < DownPoint.Y)
                {
                    newPoint.Y = e.Y;
                }

                CatchRectangle = new Rectangle(newPoint, new Size(width, height));
                g.DrawRectangle(p, CatchRectangle);

                //釋放目前的畫板
                g.Dispose();
                p.Dispose();

                //從當前窗體建立新的畫板
                Graphics g1 = this.CreateGraphics();
                //將剛剛所畫的圖片畫到截圖窗體上去
                //為什麼不直接在當前窗體畫圖呢？？？
                //如果直接解決將矩形畫在窗體上，會造成圖片抖動而且有多個矩形
                //這樣實現也屬於二次緩衝技術
                g1.DrawImage(copyBmp, new Point(0, 0));
                g1.Dispose();

                //釋放拷貝圖片 防止記憶體被大量的消耗
                copyBmp.Dispose();
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                //如果截圖已經開始，滑鼠左鍵彈起設定截圖完成
                if (CatchStart)
                {
                    CatchStart = false;
                    CatchFinished = true;
                }
            }
        }

        //雙擊截圖區域  儲存圖片到剪貼簿
        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left && CatchFinished)
            {
                //新建一個矩形大小相同的空白圖片
                Bitmap CatcheBmp = new Bitmap(CatchRectangle.Width, CatchRectangle.Height);
                Graphics g = Graphics.FromImage(CatcheBmp); ;

                //把basemap中指定的部分按照指定大小畫到空白圖片上
                //CatchRectangle指定的baseMap中指定的部分
                //第二個引數指定繪製到空白圖片的位置和大小
                //畫完後CatchedBmp不再是空白圖片，而是具有與擷取的圖片一樣的內容
                g.DrawImage(baseMap, new Rectangle(0, 0, CatchRectangle.Width, CatchRectangle.Height));

                //將圖片儲存到剪下板中
                Clipboard.SetImage(CatcheBmp);
                g.Dispose();

                CatchFinished = false;
                this.BackgroundImage = baseMap;
                CatcheBmp.Dispose();

                //this.DialogResult = DialogResult.OK;
                //this.Close();
            }


        }

        private void Form1_MouseClick(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                this.DialogResult = DialogResult.OK;
                this.Close();
            }

        }
    }
}
