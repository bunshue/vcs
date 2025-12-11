using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考/加入參考/dll/Gif.Components.dll

using Gif;
using Gif.Components;

using System.IO;
using System.Drawing.Imaging;

/*
播放gif
最近在做一個圖片查看器，由於使用一般的PctureBox，在性能和縮放控制上都無法滿足預期的要求，因此所有組件的呈現均是通過重寫控件的OnPaint事件來繪制。在查看gif圖片時發現Graphics.DrawImage只呈現第一幀，無法滿足預期要求，因此經過摸索尋找到了解決自繪gif的較好辦法。
這裡介紹一個.net自身攜帶的類ImageAnimator，這個類類似於控制動畫的時間軸，使用ImageAnimator.CanAnimate可以判斷一個圖片是否為動畫，調用ImageAnimator.Animate可以開始播放動畫，即每經過一幀的時間觸發一次OnFrameChanged委托，我們只要在該委托中將Image的活動幀選至下一幀再迫使界面重繪就可以實現動畫效果了。
為了方便以後的使用，我將這些代碼整合到了一起，形成一個AnimateImage類，該類提供了CanAnimate、FrameCount、CurrentFrame等屬性，以及Play()、Stop()、Reset()等動畫常用的方法，
*/

//用ImageAnimator播放gif檔

namespace vcs_ReadWrite_GIF1
{
    public partial class Form1 : Form
    {
        string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\小綠人\green_man3.gif";

        AnimateImage image2;
        Bitmap bitmap1;
        Bitmap bitmap3;
        bool current3 = false;

        public void AnimateImage3()
        {
            if (current3 == false)
            {
                ImageAnimator.Animate(bitmap3, new EventHandler(this.OnFrameChanged3));
                current3 = true;
            }
        }

        private void OnFrameChanged3(object o, EventArgs e)
        {
            //this.Invalidate();
            this.pictureBox3.Invalidate();
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(filename1);
            bitmap3 = new Bitmap(filename1);

            if (ImageAnimator.CanAnimate(bitmap1)) // 是否 是動畫影像
            {
                ImageAnimator.Animate(bitmap1, new EventHandler(this.OnFrameChanged1));// 播放動畫
            }

            //------------------------------------------------------------  # 60個

            image2 = new AnimateImage(Image.FromFile(filename1));
            image2.OnFrameChanged += new EventHandler<EventArgs>(image_OnFrameChanged2);
            SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            image2.Play();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        void image_OnFrameChanged2(object sender, EventArgs e)
        {
            this.pictureBox2.Invalidate();//要求pictureBox2重畫
        }

        // 當動畫框架變更時要呼叫的方法
        private void OnFrameChanged1(object o, EventArgs e)
        {
            this.pictureBox1.Invalidate();//要求pictureBox1重畫
        }

        // 重畫事件
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int x_st = 0;
            int y_st = 0;
            e.Graphics.DrawImage(bitmap1, x_st, y_st, bitmap1.Width, bitmap1.Height);
            //e.Graphics.DrawImage(this.bitmap1, new Point(0, 0));//same
            ImageAnimator.UpdateFrames(); // 推進到下一個動畫框架 Frame

            //bt_pause_Click(sender, e);
        }

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            lock (image2.Image)
            {
                e.Graphics.DrawImage(image2.Image, new Point(0, 0));
            }
        }

        void show_item_location()
        {
            int pbx_w = 320;
            int pbx_h = 320;
            int x_st;
            int y_st;
            int dx;
            int dy;
            int dx_pbx = pbx_w + 10;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button5.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(pbx_w, pbx_h);
            pictureBox1.Location = new Point(x_st + dx_pbx * 0, y_st + dy * 0);
            bt_pause.Location = new Point(x_st + dx_pbx * 0 + pbx_w - 80, y_st + dy * 0);

            pictureBox2.Size = new Size(pbx_w, pbx_h);
            pictureBox2.Location = new Point(x_st + dx_pbx * 1, y_st + dy * 0);
            bt_stop.Location = new Point(x_st + dx_pbx * 1 + pbx_w - 80, y_st + dy * 0);
            bt_reset.Location = new Point(x_st + dx_pbx * 1 + pbx_w - 80, y_st + dy * 0 + 50);

            pictureBox3.Size = new Size(pbx_w, pbx_h);
            pictureBox3.Location = new Point(x_st + dx_pbx * 2, y_st + dy * 0);
            bt_stop3.Location = new Point(x_st + dx_pbx * 2 + pbx_w - 80, y_st + dy * 0);
            bt_start3.Location = new Point(x_st + dx_pbx * 2 + pbx_w - 80, y_st + dy * 0 + 50);

            richTextBox1.Size = new Size(570, 320);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.BackColor = Color.LightPink;
            pictureBox2.BackColor = Color.LightGreen;
            pictureBox3.BackColor = Color.LightBlue;

            this.Size = new Size(1020, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //讀GIF 做成PNG
            richTextBox1.Text += "讀GIF 做成PNG\n";
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\sky.gif";
            string dirname = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

            GifToPngs(filename, dirname);

            richTextBox1.Text += "檔案 : " + filename + "\n解開到 : " + dirname + "\n";
            richTextBox1.Text += "完成\n\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀PNG 做成GIF
            richTextBox1.Text += "讀PNG 做成GIF\n";
            string dirname = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\png2gif";
            string filename = "tmp_gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gif";

            PngsToGif(dirname, filename, 500, true);

            richTextBox1.Text += "資料夾 : " + dirname + "\n製成 : " + filename + "\n";
            richTextBox1.Text += "完成\n\n";
        }

        // 把Gif文件转成Png文件，放在directory目录下
        public static void GifToPngs(string giffile, string directory)
        {
            //把Gif文件转成Png文件

            GifDecoder gifDecoder = new GifDecoder();
            directory += "\\";
            if (!Directory.Exists(directory))
            {
                Directory.CreateDirectory(directory);
            }
            //读取
            gifDecoder.Read(giffile);
            for (int i = 0, count = gifDecoder.GetFrameCount(); i < count; i++)
            {
                Image frame = gifDecoder.GetFrame(i);  // frame i
                frame.Save(directory + "\\" + i.ToString("d2") + ".png", ImageFormat.Png);
                //转成jpg
                //frame.Save(directory + "\\" + i.ToString("d2") + ".jpg", ImageFormat.Jpeg);
            }
        }

        /// 把directory文件夹里的png文件生成为gif文件，放在giffile
        /// </summary>
        /// <param name="directory">png文件夹</param>
        /// <param name="giffile">gif保存路径</param>
        /// <param name="time">每帧的时间/ms</param>
        /// <param name="repeat">是否重复</param>
        public static void PngsToGif(string directory, string giffile, int time, bool repeat)
        {
            //把多张Png文件转成Gif文件

            //一般文件名按顺序排
            string[] pngfiles = Directory.GetFileSystemEntries(directory, "*.png");

            AnimatedGifEncoder e = new AnimatedGifEncoder();
            e.Start(giffile);

            //每帧播放时间
            e.SetDelay(time);

            //-1：不重复，0：重复
            e.SetRepeat(repeat ? 0 : -1);
            for (int i = 0, count = pngfiles.Length; i < count; i++)
            {
                e.AddFrame(Image.FromFile(pngfiles[i]));
            }
            e.Finish();
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void bt_pause_Click(object sender, EventArgs e)
        {
            //停止
            if (bt_pause.Text == "停止")
            {
                // 停止播放動畫
                ImageAnimator.StopAnimate(bitmap1, new EventHandler(this.OnFrameChanged1));//停止
                bt_pause.Text = "繼續";
            }
            else
            {
                bt_pause.Text = "停止";

                if (ImageAnimator.CanAnimate(bitmap1)) // 是否 是動畫影像
                {
                    ImageAnimator.Animate(bitmap1, new EventHandler(this.OnFrameChanged1));//繼續
                }
            }
        }

        private void bt_stop_Click(object sender, EventArgs e)
        {
            if (bt_stop.Text.Equals("Stop"))
            {
                image2.Stop();
                bt_stop.Text = "Play";
            }
            else
            {
                image2.Play();
                bt_stop.Text = "Stop";
            }
            this.pictureBox1.Invalidate();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            image2.Reset();
            bt_stop.Text = "Play";
            this.pictureBox1.Invalidate();
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
            AnimateImage3();
            ImageAnimator.UpdateFrames();

            e.Graphics.DrawImage(this.bitmap3, new Point(0, 0));
        }

        private void bt_stop3_Click(object sender, EventArgs e)
        {
            ImageAnimator.StopAnimate(bitmap3, new EventHandler(this.OnFrameChanged3));//停止
        }

        private void bt_start3_Click(object sender, EventArgs e)
        {
            ImageAnimator.Animate(bitmap3, new EventHandler(this.OnFrameChanged3));//播放
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

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/

