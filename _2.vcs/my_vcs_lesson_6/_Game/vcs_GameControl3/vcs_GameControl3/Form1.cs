using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_GameControl3
{
    public partial class Form1 : Form
    {
        Image prince = new Bitmap(Properties.Resources.Prince); // 人物圖
        Rectangle[,] r = new Rectangle[4, 4]; // 人物圖的 16張小圖的矩形區域
        int dir = 2; // 人物前進方向 0 往下，1 往上，2 往右，3 往左
        int spriteStep = 0;    // 人物小圖的分解圖 0 ~ 3

        Image[] BG = new Image[3]; // 三張背景圖
        int dx = 0, dy = 0; // 背景圖的X軸、Y軸的偏移值
        int k = 0; // 背景圖索引值

        public Form1()
        {
            InitializeComponent();
            // 計算出 人物圖的 16張小圖的矩形區域
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                    r[i, j] = new Rectangle(j * 85, i * 153, 85, 153);

            // 上載三張背景圖
            BG[0] = new Bitmap(Properties.Resources.bg1);
            BG[1] = new Bitmap(Properties.Resources.bg2);
            BG[2] = new Bitmap(Properties.Resources.bg3);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            // 重複繪出背景圖
            for (int i = -1; i <= this.ClientSize.Width / BG[k].Width + 1; i++)
                for (int j = -1; j <= this.ClientSize.Height / BG[k].Height + 1; j++)
                    e.Graphics.DrawImage(BG[k], i * BG[k].Width + (dx % BG[k].Width),
                                             j * BG[k].Height + (dy % BG[k].Height));

            // 在視窗中心繪出人物小圖
            e.Graphics.DrawImage(prince, this.ClientSize.Width / 2 - 85 / 2,
                                         this.ClientSize.Height / 2 - 153 / 2,
                                         r[dir, spriteStep], GraphicsUnit.Pixel);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            spriteStep = spriteStep + 1; // 下一張人物小圖
            if (spriteStep > 3) spriteStep = 0;

            this.Invalidate();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyData == Keys.Up) // 人物往上
                dir = 1;
            else if (e.KeyData == Keys.Down)  // 人物往下 背景往上
                dir = 0;
            else if (e.KeyData == Keys.Right) // 人物往右 背景往左
                dir = 2;
            else if (e.KeyData == Keys.Left)  // 人物往左
                dir = 3;
            else if (e.KeyData == Keys.Space) // 下一張背景圖
                k = ++k % 3;
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (dir == 0) dy = dy - 5;       // 背景往上 偏移値遞減
            else if (dir == 1) dy = dy + 5;  // 背景往下 偏移値遞增
            else if (dir == 2) dx = dx - 5;  // 背景往左 偏移値遞減
            else if (dir == 3) dx = dx + 5;  // 背景往右 偏移値遞增

            this.Invalidate();
        }
    }
}