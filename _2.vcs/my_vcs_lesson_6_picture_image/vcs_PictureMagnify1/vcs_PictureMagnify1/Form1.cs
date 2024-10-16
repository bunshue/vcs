using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; // for GraphicsPath

namespace vcs_PictureMagnify1
{
    public partial class Form1 : Form
    {
        Bitmap img; // Bitmap 影像
        Point mousePos; // 滑鼠位置
        int D = 100; // 放大鏡半徑

        int magnifying_type = 0;    //0: 矩形, 1: 圓形, 2: 心形

        //圓形
        Bitmap imgDouble; // 兩倍影像的點陣圖物件

        //心形
        Bitmap buffer; // 兩倍影像的點陣圖物件

        //圓形+心形
        TextureBrush texBrush; // 兩倍影像的塗刷

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            img = new Bitmap(filename);

            this.ClientSize = new Size(img.Width, img.Height);// 調整視窗客戶區寬高

            if (magnifying_type == 1)       //圓形
            {
                imgDouble = new Bitmap(img.Width * 2, img.Height * 2);　// 新增點陣圖物件
                Graphics G = Graphics.FromImage(imgDouble); // 由點陣圖物件產生畫布
                Rectangle rectDest = new Rectangle(0, 0, imgDouble.Width, imgDouble.Height);
                Rectangle rectSrc = new Rectangle(0, 0, img.Width, img.Height);
                G.DrawImage(img, rectDest, rectSrc, GraphicsUnit.Pixel); // 放大兩倍
                texBrush = new TextureBrush(imgDouble);  // 兩倍影像的塗刷
            }
            else if (magnifying_type == 2)      //心形
            {
                buffer = new Bitmap(img.Width * 2, img.Height * 2);　// 新增點陣圖物件
                Graphics G = Graphics.FromImage(buffer); // 由點陣圖物件產生畫布
                Rectangle rectDest = new Rectangle(0, 0, buffer.Width, buffer.Height);
                Rectangle rectSrc = new Rectangle(0, 0, img.Width, img.Height);
                G.DrawImage(img, rectDest, rectSrc, GraphicsUnit.Pixel); // 放大兩倍
                texBrush = new TextureBrush(buffer);  // 兩倍影像的塗刷

                Cursor.Position = PointToScreen(new Point(img.Width / 2, img.Height / 2)); // 設定滑鼠游標位置
                Cursor.Hide();  // 隱藏滑鼠游標
            }
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            if (magnifying_type == 0)       //矩形
            {
                e.Graphics.DrawImage(img, 0, 0, img.Width, img.Height); // 呈現原圖

                Rectangle rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);
                Rectangle rectSRC = new Rectangle(mousePos.X - D / 2, mousePos.Y - D / 2, D, D);
                e.Graphics.DrawImage(img, rectDest, rectSRC, GraphicsUnit.Pixel); // 呈現原圖 放大區域

                e.Graphics.DrawRectangle(Pens.Black, rectDest); // 放大鏡外框
            }
            else if (magnifying_type == 1)       //圓形
            {
                if (img != null)
                {
                    e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                    e.Graphics.DrawImage(img, 0, 00, img.Width, img.Height); // 呈現原圖

                    Rectangle rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);

                    texBrush.ResetTransform();  // 塗刷的轉換矩陣 = 單位矩陣
                    texBrush.TranslateTransform(-mousePos.X, -mousePos.Y); // 塗刷對齊 滑鼠位置
                    e.Graphics.FillEllipse(texBrush, rectDest); // 使用影像塗刷 繪出圓形

                    e.Graphics.DrawEllipse(Pens.Black, rectDest); // 放大鏡外框
                }
            }
            else if (magnifying_type == 2)       //心形
            {
                if (img != null)
                {
                    e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
                    e.Graphics.DrawImage(img, 0, 00, img.Width, img.Height); // 呈現原圖

                    Rectangle rectDest = new Rectangle(mousePos.X - D, mousePos.Y - D, 2 * D, 2 * D);

                    texBrush.ResetTransform();  // 塗刷的轉換矩陣 = 單位矩陣
                    texBrush.TranslateTransform(-mousePos.X, -mousePos.Y); // 塗刷對齊 滑鼠位置

                    GraphicsPath gp = new GraphicsPath(); // GraphicsPath圖形軌跡物件
                    PointF[] pt1 = new PointF[5]; //心形右邊的曲線
                    PointF[] pt2 = new PointF[5]; //心形左邊的曲線
                    GetPointF(mousePos.X, mousePos.Y, 20, pt1, pt2); //計算心形左右邊的曲線
                    gp.AddCurve(pt1, 0.6f);  // 心形曲線 的外框
                    gp.AddCurve(pt2, 0.6f);
                    e.Graphics.FillPath(texBrush, gp); //填滿形狀區域 使用影像塗刷 繪出心形
                    e.Graphics.DrawPath(Pens.Black, gp); // 放大鏡外框

                    //e.Graphics.FillEllipse(texBrush, rectDest); // 使用影像塗刷 繪出圓形象
                    //e.Graphics.DrawEllipse(Pens.Black, rectDest); // 放大鏡外框
                }
            }
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            mousePos = e.Location; // 記錄 滑鼠位置
            this.Invalidate(); // 要求更新表單
        }

        // 計算心形左右邊的曲線關鍵點座標
        void GetPointF(int x, int y, int D, PointF[] pt1, PointF[] pt2)
        {
            //心形右邊的曲線 由上往下
            pt1[0] = new PointF(x, y);
            pt1[1] = new PointF(x + 3 * D, y - 1.5f * D);
            pt1[2] = new PointF(x + 5 * D, y);
            pt1[3] = new PointF(x + 4 * D, y + 3 * D);
            pt1[4] = new PointF(x, y + 7 * D);

            //心形左邊的曲線 順時間方向 由下往上 定義點的座標
            pt2[0] = new PointF(x, y + 7 * D);
            pt2[1] = new PointF(x - 4 * D, y + 3 * D);
            pt2[2] = new PointF(x - 5 * D, y);
            pt2[3] = new PointF(x - 3 * D, y - 1.5f * D);
            pt2[4] = new PointF(x, y);
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Escape)
            {
                this.Close();  // 因為 隱藏滑鼠游標 所以以Escape結束
            }
        }
    }
}
