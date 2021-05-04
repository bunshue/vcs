using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Image spider;      // 圖形的影像
        float Angle = 0; 　// 擺盪的角度
        float Angle_D = 1; // 角度的遞增值

        int spider_y = 100; // 圖形的 Y 軸高度
        Pen myPen = new Pen(Color.DarkGray, 2); // 圖形的吊掛線

        public Form1()
        {
            InitializeComponent();
            this.ClientSize = new Size(800, 600); // 設定視窗客戶區的寬高
            spider = new Bitmap(Properties.Resources.Sun128);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int x = this.ClientSize.Width / 2;
            e.Graphics.TranslateTransform(x, 0); // 平移畫布的原點
            e.Graphics.RotateTransform(Angle);　// 旋轉畫布

            // 畫出圖形
            e.Graphics.DrawImage(spider, -spider.Width / 2, spider_y);
            // 畫出圖形的吊掛線
            e.Graphics.DrawLine(myPen, 0, 0, 0, spider_y + 32);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Angle = Angle + Angle_D;　// 更新擺盪的角度
            if (Angle > 60 || Angle < -60) Angle_D = -Angle_D;
            this.Invalidate(); // 重畫
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            // 更新圖形的 Y 軸高度
            if (e.KeyData == Keys.Up)
            {
                if (spider_y >= 50) spider_y--;
            }

            if (e.KeyData == Keys.Down)
            {
                if (spider_y <= 500) spider_y++;
            }
        }
    }
}