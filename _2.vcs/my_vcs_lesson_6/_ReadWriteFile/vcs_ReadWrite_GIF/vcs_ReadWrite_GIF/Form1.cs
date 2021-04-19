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
        Bitmap bitmap = new Bitmap(@"C:\______test_files\__RW\_gif\cat.gif");
        bool current = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__RW\_gif\sky.gif";
            string dirname = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

            GifToPngs(filename, dirname);

            richTextBox1.Text += "檔案 : " + filename + "\n解開到 : " + dirname + "\n";
            richTextBox1.Text += "完成\n\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string dirname = @"C:\______test_files\__RW\_gif\png2gif";
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

        private void button3_Click(object sender, EventArgs e)
        {
            if (button3.Text == "播放GIF檔")
            {
                PlayImage();
                ImageAnimator.Animate(bitmap, new EventHandler(this.OnFrameChanged));//播放

                button3.Text = "停止播放GIF檔";
            }
            else
            {
                ImageAnimator.StopAnimate(bitmap, new EventHandler(this.OnFrameChanged));//停止
                button3.Text = "播放GIF檔";
            }
        }
    }
}
