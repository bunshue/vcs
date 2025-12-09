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

namespace vcs_ReadWrite_GIF1
{
    public partial class Form1 : Form
    {
        //檢查是否可刪除檔案:
        //string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\dog.gif";
        //string filename2 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\cat.gif";

        string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_小綠人\green_man3.gif";

        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(filename1);

            if (ImageAnimator.CanAnimate(bitmap1)) // 是否 是動畫影像
            {
                ImageAnimator.Animate(bitmap1, new EventHandler(this.OnFrameChanged1));// 播放動畫
            }
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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            bt_pause.Location = new Point(x_st + dx * 2 - 70, y_st + dy * 0);

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

            button10.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button12.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button13.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            pictureBox1.Size = new Size(320, 320);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            richTextBox1.Size = new Size(600, 640);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1260, 700);
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
            string dirname = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\png2gif";
            string filename = Application.StartupPath + "\\gif_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gif";

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

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
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
    }
}


