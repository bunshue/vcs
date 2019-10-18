using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_GetThumbNail
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\bear.bmp";
        public Form1()
        {
            InitializeComponent();
            Image img = Image.FromFile(filename);

            pictureBox1.Image = img;
        }

        private Bitmap GetThumbNail(string path)
        {
            //取得原圖
            Bitmap myBitmap = new Bitmap(path);

            //產生一張與imagelist大小的Bitmap
            Bitmap newBmp = new Bitmap(100, 100);

            Graphics g = Graphics.FromImage(newBmp);

            Pen p = new Pen(Color.Black);

            //設定高品質插值法  
            //g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            //g.InterpolationMode = InterpolationMode.High;

            //設定高品質,低速度呈現平滑程度  
            //g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
            //g.SmoothingMode = SmoothingMode.HighQuality;

            //縮圖的寬高
            int newWidth = 0;
            int newHeight = 0;

            //在畫布內重繪縮圖的x,y軸座標
            int startX = 0;
            int startY = 0;

            //100為imagelist大圖示的寬,高
            if (myBitmap.Width > 100 || myBitmap.Height > 100)
            {
                if (myBitmap.Width > myBitmap.Height)
                {
                    //指定寬，高按比例
                    newWidth = 100;
                    newHeight = myBitmap.Height * newWidth / myBitmap.Width;
                    startY = (100 - newHeight) / 2;
                }
                else if (myBitmap.Width < myBitmap.Height)
                {
                    //指定高，寬按比例
                    newHeight = 100;
                    newWidth = myBitmap.Width * newHeight / myBitmap.Height;
                    startX = (100 - newWidth) / 2;
                }
            }
            else
            {
                //保持原圖的大小
                newWidth = myBitmap.Width;
                newHeight = myBitmap.Height;
                startX = (100 - newWidth) / 2;
                startY = (100 - newHeight) / 2;
            }

            //在100*100的畫布中裡在繪出比例縮圖
            //怕有寬高過大的圖產生例外，故使用先縮圖一次(使用大量記憶體)
            //g.DrawImage(myBitmap.GetThumbnailImage(newWidth, newHeight, null, IntPtr.Zero), startX, startY, newWidth, newHeight);
            g.DrawImage(myBitmap, startX, startY, newWidth, newHeight);

            //畫出最外圍的方框
            g.DrawRectangle(p, 0, 0, 99, 99);

            g.Dispose();
            myBitmap.Dispose();

            return newBmp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bmp = GetThumbNail(filename);

            pictureBox2.Image = bmp;
        }


    }
}
