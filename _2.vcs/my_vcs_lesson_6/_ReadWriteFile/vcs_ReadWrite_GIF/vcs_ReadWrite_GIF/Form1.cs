using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Gif;
using Gif.Components;

using System.IO;
using System.Drawing.Imaging;

namespace vcs_ReadWrite_GIF
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_gif\dog.gif";
        string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_gif\cat.gif";

        Bitmap bitmap1;
        Bitmap bitmap2;
        bool current = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(filename1);
            bitmap2 = new Bitmap(filename2);

            if (ImageAnimator.CanAnimate(bitmap1)) // 是否 是動畫影像
            {
                // 播放動畫
                ImageAnimator.Animate(bitmap1, new EventHandler(this.OnFrameChanged1));
            }
        }

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int x_st = 300;
            int y_st = 0;

            ImageAnimator.UpdateFrames(); // 推進到下一個動畫框架 Frame
            e.Graphics.DrawImage(bitmap1, x_st, y_st, bitmap1.Width, bitmap1.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀GIF 做成PNG\n";
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_gif\sky.gif";
            string dirname = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

            GifToPngs(filename, dirname);

            richTextBox1.Text += "檔案 : " + filename + "\n解開到 : " + dirname + "\n";
            richTextBox1.Text += "完成\n\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀PNG 做成GIF\n";
            string dirname = @"C:\_git\vcs\_1.data\______test_files1\__pic\_gif\png2gif";
            string filename = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gif";

            PngsToGif(dirname, filename, 500, true);

            richTextBox1.Text += "資料夾 : " + dirname + "\n製成 : " + filename + "\n";
            richTextBox1.Text += "完成\n\n";
        }

        /// <summary>
        /// 把Gif文件转成Png文件，放在directory目录下
        /// </summary>
        /// <param name="file"></param>
        /// <param name="directory"></param>
        /// <returns></returns>
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

        /// <summary>
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

        public void PlayImage()
        {
            if (!current)
            {
                ImageAnimator.Animate(bitmap2, new EventHandler(this.OnFrameChanged2));
                current = true;
            }
        }

        // 當動畫框架變更時要呼叫的方法
        private void OnFrameChanged1(object o, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        // 當動畫框架變更時要呼叫的方法
        private void OnFrameChanged2(object o, EventArgs e)
        {
            this.Invalidate(); // 要求表單重畫
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawImage(this.bitmap1, new Point(300, 30));
            ImageAnimator.UpdateFrames();

            e.Graphics.DrawImage(this.bitmap2, new Point(1, 1));
            ImageAnimator.UpdateFrames();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (button3.Text == "播放GIF檔")
            {
                PlayImage();
                ImageAnimator.Animate(bitmap2, new EventHandler(this.OnFrameChanged2));//播放

                button3.Text = "停止播放GIF檔";
            }
            else
            {
                ImageAnimator.StopAnimate(bitmap2, new EventHandler(this.OnFrameChanged2));//停止
                button3.Text = "播放GIF檔";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (button4.Text == "停止")
            {
                // 停止播放動畫
                ImageAnimator.StopAnimate(bitmap1, new EventHandler(this.OnFrameChanged1));
                button4.Text = "開始";
            }
            else
            {
                button4.Text = "停止";

                if (ImageAnimator.CanAnimate(bitmap1)) // 是否 是動畫影像
                {
                    // 播放動畫
                    ImageAnimator.Animate(bitmap1, new EventHandler(this.OnFrameChanged1));
                }
            }
        }
    }
}
