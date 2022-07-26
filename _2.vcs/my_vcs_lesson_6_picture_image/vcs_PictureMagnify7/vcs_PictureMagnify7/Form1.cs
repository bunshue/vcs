using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureMagnify7
{
    public partial class Form1 : Form
    {
        int magnifying_type = 2;    //0: 矩形, 1: 圓形 不用塗刷, 2: 圓形 使用塗刷

        Bitmap bitmap1;         //螢幕的圖
        Bitmap bitmap2;    //放大2倍的圖
        Size ScreenSize;  // 螢幕的 寬高
        TextureBrush texBrush; // 兩倍影像的塗刷
        Point mousePos; // 滑鼠位置
        int D = 100; // 放大鏡半徑
        int magnify_ratio = 20;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //Cursor.Hide(); // 隱藏滑鼠游標
        }

        private void Form1_Activated(object sender, EventArgs e)
        {
            Initial();
        }

        void Initial()
        {
            ScreenSize = SystemInformation.PrimaryMonitorSize; // 得到 螢幕的 寬高
            bitmap1 = new Bitmap(ScreenSize.Width, ScreenSize.Height);
            Graphics g1 = Graphics.FromImage(bitmap1);
            g1.CopyFromScreen(0, 0, 0, 0, ScreenSize); // 拷貝 螢幕的圖 到 bitmap

            if (magnifying_type == 2)
            {
                bitmap2 = new Bitmap(ScreenSize.Width * 2, ScreenSize.Height * 2);
                Graphics g2 = Graphics.FromImage(bitmap2);
                Rectangle rectDest = new Rectangle(0, 0, ScreenSize.Width * 2, ScreenSize.Height * 2);
                Rectangle rectSRC = new Rectangle(0, 0, ScreenSize.Width, ScreenSize.Height);
                g2.DrawImage(bitmap1, rectDest, rectSRC, GraphicsUnit.Pixel); // 拷貝2倍螢幕的圖 到 bitmap2

                texBrush = new TextureBrush(bitmap2);  // 兩倍影像的塗刷
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Rectangle rectDest = new Rectangle(0, 0, ScreenSize.Width, ScreenSize.Height);
            Rectangle rectSRC = new Rectangle(0, 0, ScreenSize.Width, ScreenSize.Height);
            e.Graphics.DrawImage(bitmap1, rectDest, rectSRC, GraphicsUnit.Pixel);  // 繪出 螢幕的圖

            if ((magnifying_type == 0) || (magnifying_type == 1))
            {
                bitmap2 = new Bitmap(2 * D, 2 * D);
                Graphics g2 = Graphics.FromImage(bitmap2);
                rectDest = new Rectangle(0, 0, 2 * D, 2 * D);
                rectSRC = new Rectangle(mousePos.X - D / 2, mousePos.Y - D / 2, D, D);
                g2.DrawImage(bitmap1, rectDest, rectSRC, GraphicsUnit.Pixel); // 拷貝 2倍螢幕的圖 到 bitmap2
            }

            // 圓形放大鏡 要將 圓形外的像素設為 透明 => 會吃資源
            // 重設 bitmap2 的 圖素 
            if (magnifying_type == 0)
            {
                /*double dis;
                double D2 = D * D;
                for (int x = 0; x < bitmap2.Width; x++)
                {
                    for (int y = 0; y < bitmap2.Height; y++)
                    {
                        Color pixelColor = bitmap2.GetPixel(x, y); // 得到圖素
                        Color newColor = pixelColor;

                        dis = Math.Abs((x-bitmap2.Width/2) * (x-bitmap2.Width/2) +
                            (y-bitmap2.Height/2) * (y-bitmap2.Height/2));
                        if (dis >= D2)
                          newColor = Color.FromArgb(0, pixelColor.R, pixelColor.G, pixelColor.B);

                        bitmap2.SetPixel(x, y, newColor); // 設定圖素
                    }
                }*/
            }
            else if (magnifying_type == 1)
            {
                double dis;
                double D2 = D * D;
                Color pixelColor;
                Color newColor;

                for (int x = 0; x < bitmap2.Width; x++)
                {
                    for (int y = 0; y < bitmap2.Height; y++)
                    {
                        dis = ((x - bitmap2.Width / 2) * (x - bitmap2.Width / 2) + (y - bitmap2.Height / 2) * (y - bitmap2.Height / 2));

                        if (dis >= D2)
                        {
                            pixelColor = bitmap2.GetPixel(x, y); // 得到圖素
                            newColor = Color.FromArgb(0, pixelColor.R, pixelColor.G, pixelColor.B);
                            bitmap2.SetPixel(x, y, newColor); // 設定圖素
                        }
                    }
                }
            }
            else if (magnifying_type == 2)
            {


            }

            if ((magnifying_type == 0) || (magnifying_type == 1))
            {
                rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);
                rectSRC = new Rectangle(0, 0, 2 * D, 2 * D);
                e.Graphics.DrawImage(bitmap2, rectDest, rectSRC, GraphicsUnit.Pixel);  // 繪出 螢幕的圖
            }
            if (magnifying_type == 0)
            {
                e.Graphics.DrawRectangle(Pens.Black, rectDest); // 正方形 放大鏡外框
            }
            else if (magnifying_type == 1)
            {
                e.Graphics.DrawEllipse(Pens.Black, rectDest); // 圓形放大鏡外框
            }

            if (magnifying_type == 2)
            {
                //here
                //int magnify_ratio = 20;
                rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);
                texBrush.ResetTransform();  // 塗刷的轉換矩陣 = 單位矩陣
                texBrush.TranslateTransform(-mousePos.X, -mousePos.Y); // 塗刷對齊 滑鼠位置
                e.Graphics.FillEllipse(texBrush, rectDest); // 使用影像塗刷 繪出圓形
                e.Graphics.DrawEllipse(Pens.Black, rectDest); // 放大鏡外框
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄 滑鼠位置
            this.Invalidate(); // 要求更新表單
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape) // 離開
            {
                Cursor.Show();
                Application.Exit();
            }
            else if (e.KeyData == Keys.F1 || e.KeyData == Keys.Space)  // 程式最小化
            {
                this.WindowState = FormWindowState.Minimized;
            }
            else if (e.KeyData == Keys.Up)  // 放大鏡半徑 變大
            {
                D = D + 10;
                if (D > 500)
                {
                    D = 500;
                }
                this.Invalidate();
            }
            else if (e.KeyData == Keys.Down)  // 放大鏡半徑 變小
            {
                D = D - 10;
                if (D < 30)
                {
                    D = 30;
                }
                this.Invalidate();
            }
            else if (e.KeyData == Keys.Add)  // 放大鏡倍率 變大
            {
                //TBD
                D = D + 10;
                if (D > 500)
                {
                    D = 500;
                }
                this.Invalidate();
            }
            else if (e.KeyData == Keys.Subtract)  // 放大鏡倍率 變小
            {
                //TBD
                D = D - 10;
                if (D < 30)
                {
                    D = 30;
                }
                this.Invalidate();
            }
        }
    }
}
