using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_PictureFadeInFadeOut
{
    public partial class Form1 : Form
    {
        G2D_ImageFadeinFadeout2 imageObject; // 淡入淡出物件
        Bitmap[] bitmap = new Bitmap[4]; // 我有四張圖
        int D = 0; // 第 D 張
        Point pos; // 圖的中心位置

        public Form1()
        {
            InitializeComponent();
            bitmap[0] = new Bitmap(Properties.Resources.Blue_hills);
            bitmap[1] = new Bitmap(Properties.Resources.Sunset);
            bitmap[2] = new Bitmap(Properties.Resources.Water_lilies);
            bitmap[3] = new Bitmap(Properties.Resources.Winter);

            this.ClientSize = new Size(bitmap[0].Width, bitmap[0].Height); // 調整視窗客戶區的大小

            imageObject = new G2D_ImageFadeinFadeout2(bitmap[D], bitmap[D + 1]);  // 產生淡入淡出物件
            pos = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2); // 產生淡入淡出物件
            imageObject.Init(pos, 10000);  // 10 秒
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            imageObject.Draw(e.Graphics); // 繪出
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求重畫
            if (imageObject.isTimeUp())  // 如果時間到了
            {
                D = D + 1;
                if (D == bitmap.Length) D = 0; // 已經 超過最後一張

                if (D < bitmap.Length - 1)  // 第 D 張 和 第 D + 1張
                    imageObject = new G2D_ImageFadeinFadeout2(bitmap[D], bitmap[D + 1]);
                else // 最後一張 和 第一張
                {
                    imageObject = new G2D_ImageFadeinFadeout2(bitmap[bitmap.Length - 1], bitmap[0]);
                }

                imageObject.Init(pos, 10000);
            }
        }
    }
}
