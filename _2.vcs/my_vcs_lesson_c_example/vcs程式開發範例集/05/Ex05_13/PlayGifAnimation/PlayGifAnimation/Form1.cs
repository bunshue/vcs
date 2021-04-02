using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace PlayGifAnimation
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
       
        Bitmap bitmap = new Bitmap(Application.StartupPath+"\\1.gif");
        bool current = false;

        public void PlayImage()
        {
            if (!current)
            {
                ImageAnimator.Animate(bitmap, new EventHandler(this.OnFrameChanged));
                current = true;
            }
        }

        private void OnFrameChanged(object o, EventArgs e)
        {
            this.Invalidate();
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            
            e.Graphics.DrawImage(this.bitmap, new Point(1, 1));
            ImageAnimator.UpdateFrames();
        }
     
        private void button1_Click(object sender, EventArgs e)
        {
            PlayImage();
            ImageAnimator.Animate(bitmap, new EventHandler(this.OnFrameChanged));//播放
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ImageAnimator.StopAnimate(bitmap, new EventHandler(this.OnFrameChanged));//停止
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}