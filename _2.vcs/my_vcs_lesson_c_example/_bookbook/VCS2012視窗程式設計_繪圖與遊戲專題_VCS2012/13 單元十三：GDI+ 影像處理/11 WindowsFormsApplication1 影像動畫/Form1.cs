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
        Bitmap img; // Bitmap 影像

        public Form1()
        {
            InitializeComponent();
            img = Properties.Resources.Dog; // 影像從資源載入 Gif
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int Cx = this.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.ClientSize.Height / 2;

            ImageAnimator.UpdateFrames(); // 推進到下一個動畫框架 Frame
            e.Graphics.DrawImage(img, Cx - img.Width / 2, Cy - img.Height / 2, img.Width, img.Height);
        }

        // 播放動畫按鈕事件
        private void button1_Click(object sender, EventArgs e)
        {
            if (ImageAnimator.CanAnimate(img)) // 是否 是動畫影像
            {
                // 播放動畫
                ImageAnimator.Animate(img,
                     new EventHandler(this.OnFrameChanged));
            }
        }

        // 停止播放動畫按鈕事件
        private void button2_Click(object sender, EventArgs e)
        {
            // 停止播放動畫
            ImageAnimator.StopAnimate(img,
                   new EventHandler(this.OnFrameChanged));
        }

        // 當動畫框架變更時要呼叫的方法
        private void OnFrameChanged(object o, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }
    }
}