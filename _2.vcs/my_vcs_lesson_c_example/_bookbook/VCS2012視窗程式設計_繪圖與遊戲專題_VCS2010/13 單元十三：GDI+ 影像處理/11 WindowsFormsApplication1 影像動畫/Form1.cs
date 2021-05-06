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
        Bitmap bitmap1; // Bitmap 影像

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = Properties.Resources.Dog; // 影像從資源載入 Gif

        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int x_st = 100;
            int y_st = 100;

            ImageAnimator.UpdateFrames(); // 推進到下一個動畫框架 Frame
            e.Graphics.DrawImage(bitmap1, x_st, y_st, bitmap1.Width, bitmap1.Height);
        }

        // 播放動畫按鈕事件
        private void button1_Click(object sender, EventArgs e)
        {
            if (ImageAnimator.CanAnimate(bitmap1)) // 是否 是動畫影像
            {
                // 播放動畫
                ImageAnimator.Animate(bitmap1, new EventHandler(this.OnFrameChanged));
            }
        }

        // 停止播放動畫按鈕事件
        private void button2_Click(object sender, EventArgs e)
        {
            // 停止播放動畫
            ImageAnimator.StopAnimate(bitmap1, new EventHandler(this.OnFrameChanged));
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


