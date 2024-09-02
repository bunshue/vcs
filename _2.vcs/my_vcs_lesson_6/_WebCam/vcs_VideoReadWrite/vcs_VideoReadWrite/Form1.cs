using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for dll

using System.IO;
using System.Threading;
using System.Diagnostics;   //for Stopwatch
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;   //for PixelFormat

using AForge.Video.FFMPEG;      //for VideoFileWriter

using AviFile;

namespace vcs_VideoReadWrite
{
    public partial class Form1 : Form
    {
        private const int BORDER = 10;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 120 + BORDER;
            int dy = 60 + BORDER;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            pictureBox1.Size = new Size(300, 300);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 560 - 300);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 300 + BORDER);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Size = new Size(600, 620);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void drawMessage(Bitmap bitmap1)
        {
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bmp = vcs_VideoReadWrite.Properties.Resources.logo;
            Graphics g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(new Pen(Color.Red, 10), 50, 50, W - 50 * 2, H - 50 * 2);    //draw boundary
            g.DrawString("台東之旅", new Font("標楷體", 30), new SolidBrush(Color.Navy), new PointF(W - 50 - 240, H - 50 - 50));
            g.DrawImage(bmp, W - 50 - 70, H - 50 - 50 - 30, bmp.Width / 4, bmp.Height / 4);

            //原圖貼上
            //               貼上位置x      貼上位置y      貼上大小W            貼上大小H
            //g.DrawImage(bmp, x_st + dx * 0, y_st + dy * 0, bmp.Width * 12 / 10, bmp.Height * 12 / 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "製作繪圖影片 / 圖片轉影片\n";
            Application.DoEvents();

            string filename = "tmp_video_writer0.avi";
            int W = 1600;
            int H = 760;
            int fps = 1;  //一秒N張  若是30，就是一秒30張

            //公用變數
            VideoFileWriter writer = new VideoFileWriter();

            //開啟檔案
            writer.Open(filename, W, H, fps);
            //writer.Open(filename, W, H, fps, VideoCodec.MPEG4);
            //writer.Open(filename, W, H, fps, VideoCodec.WMV1);

            //VideoCodec codec = VideoCodec.WMV2;
            //writer.Open(filename, W, H, fps, codec);

            //製作繪圖影片
            //Bitmap bmp = new Bitmap(W, H, PixelFormat.Format24bppRgb);
            //Bitmap bmp = new Bitmap(W, H, PixelFormat.Format32bppArgb);
            Bitmap bmp = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bmp);
            int cx = W / 2;
            int cy = H / 2;
            int R = 100;
            int N = 5;    //共N張
            for (R = 0; R < N; R++)
            {
                //g.Clear(Color.White);
                g.Clear(Color.Black);
                g.SmoothingMode = SmoothingMode.AntiAlias;
                g.InterpolationMode = InterpolationMode.HighQualityBicubic;
                g.PixelOffsetMode = PixelOffsetMode.HighQuality;

                g.DrawEllipse(new Pen(Color.FromArgb(255, 255, 0, 0)), cx - R * 50, cy - R * 50, R * 50, R * 50);
                g.DrawString("台東之旅", new Font("標楷體", 100), new SolidBrush(Color.Navy), new PointF(cx - 100, cy));

                //g.FillRectangle(Brushes.Black, 0, 0, R * 2, R * 2);

                g.Flush();

                writer.WriteVideoFrame(bmp);//寫入影格
            }

            //製作圖片影片

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung2.jpg";
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung3.jpg";
            string filename4 = @"C:\_git\vcs\_1.data\______test_files1\__pic\_scenery/taitung4.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename2);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap3 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式
            Bitmap bitmap4 = (Bitmap)Bitmap.FromFile(filename4);	//Bitmap.FromFile出來的是Image格式

            drawMessage(bitmap1);
            drawMessage(bitmap2);
            drawMessage(bitmap3);
            drawMessage(bitmap4);

            for (int i = 0; i < 10; i++)
            {
                writer.WriteVideoFrame(bitmap1);//寫入影格
                writer.WriteVideoFrame(bitmap2);//寫入影格
                writer.WriteVideoFrame(bitmap3);//寫入影格
                writer.WriteVideoFrame(bitmap4);//寫入影格
            }

            //關閉檔案
            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "桌面錄影 10秒\n";
            Application.DoEvents();

            string filename = "tmp_video_writer4.avi";
            int W = 1920 / 2;
            int H = 1080 / 2;
            int fps = 5;  //一秒N張  若是30，就是一秒30張
            int period = 1000 / fps;//每張相隔的時間(msec)
            int sec = 10;   //10秒
            int N = fps * sec;    //共N張

            VideoFileWriter writer = new VideoFileWriter();

            writer.Open(filename, W, H, fps, VideoCodec.MPEG4);

            for (int i = 0; i < N; i++)
            {
                Stopwatch sw = new Stopwatch();
                sw.Start();
                using (Bitmap bmpScreenCapture = new Bitmap(W, H))
                {
                    using (Graphics g = Graphics.FromImage(bmpScreenCapture))
                    {
                        //                螢幕抓取位置    貼上bitmap位置   抓取與貼上大小
                        g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));

                        //錄製滑鼠游標
                        Rectangle cursorBounds = new Rectangle(new Point(Cursor.Position.X, Cursor.Position.Y), Cursors.Default.Size);
                        Cursors.Default.Draw(g, cursorBounds);
                    }
                    writer.WriteVideoFrame(bmpScreenCapture);

                    //隔一陣子再抓圖存圖, 用以達到固定fps桌面錄影功能
                    sw.Stop();
                    var t = sw.ElapsedMilliseconds;

                    if (period - t > 0)
                        Thread.Sleep((int)(period - t));
                }
            }

            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //轉錄
            string filename_read = "tmp_video_writer0.avi";
            string filename_write = "tmp_video_writer0b.avi";

            if (File.Exists(filename_read) == false)
            {
                richTextBox1.Text += "檔案 : " + filename_read + " 不存在, 離開\n";
                return;
            }

            if (File.Exists(filename_write) == true)
            {
                File.Delete(filename_write);
            }

            VideoFileReader reader = new VideoFileReader();
            VideoFileWriter writer = new VideoFileWriter();

            reader.Open(filename_read);

            richTextBox1.Text += "CodecName = " + reader.CodecName.ToString() + "\n";
            richTextBox1.Text += "Width = " + reader.Width.ToString() + "\n";
            richTextBox1.Text += "Height = " + reader.Height.ToString() + "\n";
            richTextBox1.Text += "FrameCount = " + reader.FrameCount.ToString() + "\n";
            richTextBox1.Text += "FrameRate = " + reader.FrameRate.ToString() + "\n";
            richTextBox1.Text += "CodecName = " + reader.CodecName + "\n";

            // print some of its attributes
            richTextBox1.Text += "Width: " + reader.Width + "px" + Environment.NewLine;
            richTextBox1.Text += ("Height: " + reader.Height + "px" + Environment.NewLine);
            richTextBox1.Text += ("Fps: " + reader.FrameRate + "fps" + Environment.NewLine);
            richTextBox1.Text += ("Codec: " + reader.CodecName + Environment.NewLine);
            richTextBox1.Text += ("Frames: " + reader.FrameCount + Environment.NewLine);

            richTextBox1.Text += "Duration = " + (reader.FrameCount / reader.FrameRate).ToString() + " 秒\n";

            int end = (int)reader.FrameCount;

            int W = reader.Width;
            int H = reader.Height;
            int fps = reader.FrameRate;

            /*
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";
            richTextBox1.Text += "frameRate = " + fps.ToString() + "\n";
            richTextBox1.Text += "end = " + end.ToString() + "\n";
            */

            writer.Open(filename_write, W, H, fps, VideoCodec.MPEG4);

            for (int i = 0; i < end; i++)
            {
                Bitmap videoFrame = reader.ReadVideoFrame();
                writer.WriteVideoFrame(videoFrame);
                videoFrame.Dispose();

                if (i == 5)     //切斷影片
                {
                    writer.Close();
                    break;
                }
            }
            writer.Close();
            reader.Close();

            richTextBox1.Text += "讀取檔案 : " + filename_read + "\n";
            richTextBox1.Text += "寫入檔案 : " + filename_write + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將.avi的聲音分離出來\n";
            Application.DoEvents();

            string audio_filename = "tmp_audio_only.wav";
            if (File.Exists(audio_filename) == true)
            {
                File.Delete(audio_filename);
            }

            string filename = @"C:\_git\vcs\_1.data\______test_files1\_video\i2c.avi";

            AviManager aviManager = new AviManager(filename, true);

            //try to read the stream
            try
            {
                AudioStream waveStream = aviManager.GetWaveStream();
                richTextBox1.Text += Environment.NewLine + "Audio stream found:";
                richTextBox1.Text += Environment.NewLine + "Sample Rate: " + waveStream.CountSamplesPerSecond.ToString();
                richTextBox1.Text += Environment.NewLine + "Bits:" + waveStream.CountBitsPerSample.ToString();
                richTextBox1.Text += Environment.NewLine + "Number of Channels: " + waveStream.CountChannels.ToString();

                waveStream.ExportStream(audio_filename);

                waveStream.Close();
                aviManager.Close();

                richTextBox1.Text += "聲音分離完成, 檔案 : " + audio_filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
            }
        }

        /* 引入 Win32 API 中的 User32.DLL
 * 需要加上 using System.Runtime.InteropServices;
 */
        [DllImport("user32.dll")]
        public static extern Boolean GetWindowRect(IntPtr hWnd, ref Rectangle bounds);

        private void button5_Click(object sender, EventArgs e)
        {
            //抓取指定視窗的畫面截圖
            /* 取得目標視窗的 Handle
 * 需要加上 using System.Diagnostics;
 */
            Process[] process = Process.GetProcessesByName("notepad");

            /* 取得該視窗的大小與位置 */
            Rectangle bounds = new Rectangle(100, 100, 100, 100);

            GetWindowRect(process[0].MainWindowHandle, ref bounds);

            /* 抓取截圖 */
            Bitmap screenshot = new Bitmap(bounds.Width, bounds.Height, PixelFormat.Format32bppArgb);
            Graphics gfx = Graphics.FromImage(screenshot);
            gfx.CopyFromScreen(bounds.X, bounds.Y, 0, 0, bounds.Size, CopyPixelOperation.SourceCopy);

            /* 利用 PictureBox 顯示出來 */
            pictureBox1.Image = (Image)screenshot;
            pictureBox1.Update();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //全螢幕截圖
            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);

                bitmap.Save("tmp_full_screen.jpg", ImageFormat.Jpeg);
            }

            /*
            //another

            Bitmap myImage = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            Graphics g = Graphics.FromImage(myImage);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            myImage.Save(@"c:\screen0.jpg");
            */
        }

        private void button7_Click(object sender, EventArgs e)
        {
            pictureBox1.BackColor = Color.Pink;
            int W = 250;// 1920 / 4;
            int H = 250;// 1080 / 4;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);

            //               抓取螢幕位置   貼上bitmap位置      抓取與貼上大小
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(W, H));
            //g.CopyFromScreen(this.Location, new Point(0, 0), new Size(W, H), CopyPixelOperation.MergePaint);
            //g.CopyFromScreen(this.Location, new Point(0, 0), new Size(W, H), CopyPixelOperation.SourceInvert);

            pictureBox1.Image = bitmap1;

            /*
            //桌面
            using (Bitmap bmpScreenCapture = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bmpScreenCapture))
                {
                    g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));

                    //錄製滑鼠游標
                    Rectangle cursorBounds = new Rectangle(new Point(Cursor.Position.X, Cursor.Position.Y), Cursors.Default.Size);
                    Cursors.Default.Draw(g, cursorBounds);
                }
                writer.WriteVideoFrame(bmpScreenCapture);

                //隔一陣子再抓圖存圖, 用以達到固定fps桌面錄影功能
                sw.Stop();
                var t = sw.ElapsedMilliseconds;

                if (period - t > 0)
                    Thread.Sleep((int)(period - t));
            }
            */
        }
    }
}
