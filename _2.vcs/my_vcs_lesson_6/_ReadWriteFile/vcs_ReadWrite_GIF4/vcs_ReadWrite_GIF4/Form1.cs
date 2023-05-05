using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

/*
播放gif
最近在做一個圖片查看器，由於使用一般的PctureBox，在性能和縮放控制上都無法滿足預期的要求，因此所有組件的呈現均是通過重寫控件的OnPaint事件來繪制。在查看gif圖片時發現Graphics.DrawImage只呈現第一幀，無法滿足預期要求，因此經過摸索尋找到了解決自繪gif的較好辦法。

這裡介紹一個.net自身攜帶的類ImageAnimator，這個類類似於控制動畫的時間軸，使用ImageAnimator.CanAnimate可以判斷一個圖片是否為動畫，調用ImageAnimator.Animate可以開始播放動畫，即每經過一幀的時間觸發一次OnFrameChanged委托，我們只要在該委托中將Image的活動幀選至下一幀再迫使界面重繪就可以實現動畫效果了。

為了方便以後的使用，我將這些代碼整合到了一起，形成一個AnimateImage類，該類提供了CanAnimate、FrameCount、CurrentFrame等屬性，以及Play()、Stop()、Reset()等動畫常用的方法，代碼如下
*/

namespace vcs_ReadWrite_GIF4
{
    public partial class Form1 : Form
    {
        AnimateImage image;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_gif\cat.gif";
            image = new AnimateImage(Image.FromFile(filename));
            image.OnFrameChanged += new EventHandler<EventArgs>(image_OnFrameChanged);
            SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);

            image.Play();
        }

        void image_OnFrameChanged(object sender, EventArgs e)
        {
            this.pictureBox1.Invalidate();
            //Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            lock (image.Image)
            {
                e.Graphics.DrawImage(image.Image, new Point(0, 0));
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text.Equals("Stop"))
            {
                image.Stop();
                button1.Text = "Play";
            }
            else
            {
                image.Play();
                button1.Text = "Stop";
            }
            this.pictureBox1.Invalidate();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            image.Reset();
            button1.Text = "Play";
            this.pictureBox1.Invalidate();
        }
    }

    /// <summary>
    /// 表示一类带动画功能的图像。
    /// </summary>
    public class AnimateImage
    {
        Image image;
        FrameDimension frameDimension;
        /// <summary>
        /// 动画当前帧发生改变时触发。
        /// </summary>
        public event EventHandler<EventArgs> OnFrameChanged;

        /// <summary>
        /// 实例化一个AnimateImage。
        /// </summary>
        /// <param name="img">动画图片。</param>
        public AnimateImage(Image img)
        {
            image = img;

            lock (image)
            {
                mCanAnimate = ImageAnimator.CanAnimate(image);
                if (mCanAnimate)
                {
                    Guid[] guid = image.FrameDimensionsList;
                    frameDimension = new FrameDimension(guid[0]);
                    mFrameCount = image.GetFrameCount(frameDimension);
                }
            }
        }

        bool mCanAnimate;
        int mFrameCount = 1, mCurrentFrame = 0;

        /// <summary>
        /// 图片。
        /// </summary>
        public Image Image
        {
            get { return image; }
        }

        /// <summary>
        /// 是否动画。
        /// </summary>
        public bool CanAnimate
        {
            get { return mCanAnimate; }
        }

        /// <summary>
        /// 总帧数。
        /// </summary>
        public int FrameCount
        {
            get { return mFrameCount; }
        }

        /// <summary>
        /// 播放的当前帧。
        /// </summary>
        public int CurrentFrame
        {
            get { return mCurrentFrame; }
        }

        /// <summary>
        /// 播放这个动画。
        /// </summary>
        public void Play()
        {
            if (mCanAnimate)
            {
                lock (image)
                {
                    ImageAnimator.Animate(image, new EventHandler(FrameChanged));
                }
            }
        }

        /// <summary>
        /// 停止播放。
        /// </summary>
        public void Stop()
        {
            if (mCanAnimate)
            {
                lock (image)
                {
                    ImageAnimator.StopAnimate(image, new EventHandler(FrameChanged));
                }
            }
        }

        /// <summary>
        /// 重置动画，使之停止在第0帧位置上。
        /// </summary>
        public void Reset()
        {
            if (mCanAnimate)
            {
                ImageAnimator.StopAnimate(image, new EventHandler(FrameChanged));
                lock (image)
                {
                    image.SelectActiveFrame(frameDimension, 0);
                    mCurrentFrame = 0;
                }
            }
        }

        private void FrameChanged(object sender, EventArgs e)
        {
            mCurrentFrame = mCurrentFrame + 1 >= mFrameCount ? 0 : mCurrentFrame + 1;
            lock (image)
            {
                image.SelectActiveFrame(frameDimension, mCurrentFrame);
            }
            if (OnFrameChanged != null)
            {
                OnFrameChanged(image, e);
            }
        }
    }



}
