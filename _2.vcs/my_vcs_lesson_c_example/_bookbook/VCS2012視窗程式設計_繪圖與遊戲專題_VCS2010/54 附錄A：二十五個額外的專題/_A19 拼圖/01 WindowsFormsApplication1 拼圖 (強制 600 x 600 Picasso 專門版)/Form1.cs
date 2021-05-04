using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing.Imaging; //  for ColorMatrix, ImageAttributes

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Bitmap bitmap = Properties.Resources.Picasso_01; // 原圖 是 600 X 600
        RectangleF[,] small_rect;    // 小圖 目前在視窗的位置  (變動的)
        RectangleF[,] small_rect_0;  // 小圖框 架構 在視窗的位置 (不變的)
        RectangleF[,] small_rect_1;  // 小圖框 架構 在原圖的位置 (不變的)

        int x0 = 100;  // 全部小圖 的左上角座標定位點
        int y0 = 100;
        bool selected = false; //是否有小圖 被選到
        int selected_X, selected_Y; //是哪一張 小圖 被選到
        float Dx, Dy; // 被選到小圖 和 滑鼠座標 的偏移值
        Random rd = new Random();
        int SplitNo = 3; //  預設小圖的個數是 3 X 3 
        float D; //  小圖的 寬高

        float[][] m_cmArray = // 色彩調整矩陣 透明度 20%
               {
                  new float[] {1, 0, 0, 0,    0},
                  new float[] {0, 1, 0, 0,    0},
                  new float[] {0, 0, 1, 0,    0},
                  new float[] {0, 0, 0, 0.2f, 0},
                  new float[] {0, 0, 0, 0,    1}
               };
        bool hint = false; // 是否有提示

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(820, 800); // 視窗寬高
            Cut(); // 切成 許多小圖
        }

        // 切成 許多小圖
        void Cut()
        {
            //small = new Bitmap[SplitNo, SplitNo];
            small_rect = new RectangleF[SplitNo, SplitNo];
            small_rect_0 = new RectangleF[SplitNo, SplitNo]; // 小圖框 架構 在視窗的位置 (不變的)
            small_rect_1 = new RectangleF[SplitNo, SplitNo]; // 小圖框 架構 在原圖的位置 (不變的)

            D = 600.0f / SplitNo; //  小圖的 寬高

            RectangleF rect;
            for (int i = 0; i< SplitNo; i++)
                for (int j = 0; j < SplitNo; j++)
                {
                    rect = new RectangleF(i * D, j * D, D, D);
                    //small[i, j] = bitmap.Clone(rect, System.Drawing.Imaging.PixelFormat.DontCare);
                    small_rect[i, j] = new RectangleF(i * D + x0, j * D+y0, D, D);
                    small_rect_0[i, j] = new RectangleF(i * D + x0, j * D + y0, D, D);
                    small_rect_1[i, j] = new RectangleF(i * D , j * D , D, D);
                }

            //  打亂 小圖
            int i1, j1;
            for (int i = 0; i< SplitNo; i++)
                for (int j = 0; j < SplitNo; j++)
                {
                    i1 = rd.Next(SplitNo);
                    j1 = rd.Next(SplitNo);

                    rect = small_rect[i, j];
                    small_rect[i, j] = small_rect[i1, j1];
                    small_rect[i1, j1] = rect;
                }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 繪出 完整的圖
            RectangleF dest = new Rectangle(710,10,100,100);
            RectangleF src = new Rectangle(0,0,600,600);
            e.Graphics.DrawImage(bitmap, dest, src, GraphicsUnit.Pixel);

            // 如果有提示  就繪出 提示的圖
            if (hint)
            {
                Rectangle dest2 = new Rectangle(x0, y0, 600, 600);

                ColorMatrix cm = new ColorMatrix(m_cmArray);
                ImageAttributes ia = new ImageAttributes();
                ia.SetColorMatrix(cm,
                    ColorMatrixFlag.Default,
                    ColorAdjustType.Bitmap);

                e.Graphics.DrawImage(bitmap,
                    dest2,
                    0, 0, 600,600,
                    GraphicsUnit.Pixel, ia);
            }

            // 繪出 全部小圖
            for (int i = 0; i< SplitNo; i++)
                for (int j = 0; j < SplitNo; j++)
                {
                    e.Graphics.DrawImage(bitmap, small_rect[i, j], small_rect_1[i, j], GraphicsUnit.Pixel);
                }

            // 畫出框線
            for (int i = 0; i <= SplitNo; i++)
                e.Graphics.DrawLine(Pens.White, x0, y0+i * D, x0 + 600, y0+i*D);

            for (int i = 0; i <= SplitNo; i++)
                e.Graphics.DrawLine(Pens.White, x0 + i * D, y0, x0 + i * D, y0 + 600);
        }

        // 滑鼠被按下
        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            for (int i = SplitNo-1; i >= 0 ; i--)  // 因為有上下層 的關悉 
                for (int j = SplitNo - 1; j >= 0; j--) //後畫的在前面 會先被選到
                {
                    if (e.X >= small_rect[i, j].X && e.X < small_rect[i, j].X + D &&
                        e.Y >= small_rect[i, j].Y && e.Y < small_rect[i, j].Y + D)
                    {
                        selected = true; // 是有小圖被選到
                        selected_X = i; // 紀錄 被選到的小圖
                        selected_Y = j;
                        Dx = e.X - small_rect[i, j].X; // 紀錄 滑鼠座標 的偏移值
                        Dy = e.Y - small_rect[i, j].Y;
                        return; // 不用再找了
                    }
                }
        }

        // 滑鼠被放開 
        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            selected = false;
        }

        // 滑鼠移動
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            float dx, dy;       // 小圖 和小圖框 實際的距離差距
            float epsilon = 20; // 預設的距離差距

            if (selected) // 如果目前是有小圖被選到
            {
                small_rect[selected_X, selected_Y].X = e.X - Dx; // 更新 被選到小圖 的座標
                small_rect[selected_X, selected_Y].Y = e.Y - Dy;

                // 如果距離夠近 就將小圖擺正
                for (int i = 0; i < SplitNo; i++)
                    for (int j = 0; j < SplitNo; j++)
                    {
                        dx = small_rect[selected_X, selected_Y].X - small_rect_0[i, j].X;
                        dy = small_rect[selected_X, selected_Y].Y - small_rect_0[i, j].Y;

                        if (dx < epsilon && dx > -epsilon && dy < epsilon && dy > -epsilon)
                            small_rect[selected_X, selected_Y] = small_rect_0[i, j];
                    }

                this.Invalidate();
            }
        }

        // 更新 小圖 的切割 數目
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.D3 || e.KeyData == Keys.D4 ||
                e.KeyData == Keys.D5 || e.KeyData == Keys.D6 ||
                e.KeyData == Keys.D7 || e.KeyData == Keys.D8 ||
                e.KeyData == Keys.D9 || e.KeyData == Keys.Space)
            {
                if (e.KeyData == Keys.D3)  SplitNo = 3;
                else if (e.KeyData == Keys.D4) SplitNo = 4;
                else if (e.KeyData == Keys.D5) SplitNo = 5;
                else if (e.KeyData == Keys.D6) SplitNo = 6;
                else if (e.KeyData == Keys.D7) SplitNo = 7;
                else if (e.KeyData == Keys.D8) SplitNo = 8;
                else if (e.KeyData == Keys.D9) SplitNo = 9;

                Cut();
                this.Invalidate();
            }
            else if (e.KeyData == Keys.H)
            {
                hint = !hint;
                this.Invalidate();
            }
        }

        private void panel1_Click(object sender, EventArgs e)
        {
            Panel p = (Panel)(sender);
            if (p  == panel1) bitmap = Properties.Resources.Picasso_01; // 原圖 是 600 X 600
            else if (p == panel2) bitmap = Properties.Resources.Picasso_02;
                        
            Cut();
            this.Invalidate();
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Bitmap bitmap2 = new Bitmap(openFileDialog1.FileName); // 儲存 點陣圖物件
                bitmap = (Bitmap)bitmap2.GetThumbnailImage(600, 600, null, (IntPtr)0); // 扭曲為 600 x 600
                this.ActiveControl = null;  // 不讓 按鈕 持續取得 焦點
                Cut();
                this.Invalidate();
            }
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            // 開啟 顏色選取視窗
            if (colorDialog1.ShowDialog() == DialogResult.OK)
            {
                this.BackColor = colorDialog1.Color; //呈現選色
                this.Invalidate();
            }
        }
    }
}
