using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ShowPicture8
{
    public partial class Form1 : Form
    {
        G2D_ImageFadeinFadeout2 imageObject; // 淡入淡出物件
        Bitmap[] bitmap = new Bitmap[4]; // 我有四張圖
        int D = 0; // 第 D 張
        Point pos; // 圖的中心位置

        string filename0 = @"C:\______test_files\__pic\_scenery\Blue hills.jpg";
        string filename1 = @"C:\______test_files\__pic\_scenery\Sunset.jpg";
        string filename2 = @"C:\______test_files\__pic\_scenery\Water lilies.jpg";
        string filename3 = @"C:\______test_files\__pic\_scenery\Winter.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.pictureBox_FadeInFadeOut.Size = 

            bitmap[0] = new Bitmap(filename0);
            bitmap[1] = new Bitmap(filename1);
            bitmap[2] = new Bitmap(filename2);
            bitmap[3] = new Bitmap(filename3);

            this.pictureBox_FadeInFadeOut.Size = new Size(bitmap[0].Width, bitmap[0].Height); // 調整pictureBox的大小

            imageObject = new G2D_ImageFadeinFadeout2(bitmap[D], bitmap[D + 1]);  // 產生淡入淡出物件
            pos = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2); // 產生淡入淡出物件
            imageObject.Init(pos, 10000);  // 10 秒
        }

        private void timer_FadeInFadeOut_Tick(object sender, EventArgs e)
        {
            this.pictureBox_FadeInFadeOut.Invalidate(); // 要求重畫
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

        private void pictureBox_FadeInFadeOut_Paint(object sender, PaintEventArgs e)
        {
            imageObject.Draw(e.Graphics); // 繪出
        }
    }
}
