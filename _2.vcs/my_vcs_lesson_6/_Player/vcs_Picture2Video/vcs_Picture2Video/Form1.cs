using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for dll

using System.Threading;
using System.Diagnostics;   //for Stopwatch

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
using AForge.Video.FFMPEG;      //for VideoFileWriter

using System.IO;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;   //for PixelFormat

using AviFile;

namespace vcs_Picture2Video
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

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
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
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 5);

            pictureBox1.Size = new Size(300, 300);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(400, 560 - 300);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 300 + BORDER);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Size = new Size(800, 620);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void drawMessage(Bitmap bitmap1)
        {
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bmp = vcs_Picture2Video.Properties.Resources.logo;
            Graphics g;
            g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(new Pen(Color.Red, 10), 50, 50, W - 50 * 2, H - 50 * 2);    //draw boundary
            g.DrawString("台東之旅", new Font("標楷體", 30), new SolidBrush(Color.Navy), new PointF(W - 50 - 240, H - 50 - 50));
            g.DrawImage(bmp, W - 50 - 70, H - 50 - 50 - 30, bmp.Width / 4, bmp.Height / 4);

            //原圖貼上
            //               貼上位置x      貼上位置y      貼上大小W            貼上大小H
            //g.DrawImage(bmp, x_st + dx * 0, y_st + dy * 0, bmp.Width * 12 / 10, bmp.Height * 12 / 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "圖片轉影片\n";
            Application.DoEvents();

            //vcs最小化錄影
            string filename = "tmp_video_writer0.avi";
            int W = 1600;
            int H = 760;
            int fps = 1;

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

            //公用變數
            VideoFileWriter writer = new VideoFileWriter();

            //開啟檔案
            writer.Open(filename, W, H, fps);

            for (int i = 0; i < 10; i++)
            {
                writer.WriteVideoFrame(bitmap1);//寫入影格
                writer.WriteVideoFrame(bitmap2);//寫入影格
                writer.WriteVideoFrame(bitmap3);//寫入影格
                writer.WriteVideoFrame(bitmap4);//寫入影格
            }

            //關閉檔案
            writer.Close();

            richTextBox1.Text += "圖片轉影片 OK\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "製作繪圖影片\n";
            Application.DoEvents();

            //vcs最小化錄影
            string filename = "tmp_video_writer1.avi";
            int W = 300;
            int H = 300;
            int fps = 1;

            //公用變數
            VideoFileWriter writer = new VideoFileWriter();

            //開啟檔案
            writer.Open(filename, W, H, fps);

            //製作繪圖影片
            Bitmap bitmap1 = new Bitmap(300, 300);
            Graphics g = Graphics.FromImage(bitmap1);
            int cx = 300 / 2;
            int cy = 300 / 2;
            int R = 100;
            for (R = 0; R < 150; R++)
            {
                g.Clear(Color.White);
                g.DrawEllipse(new Pen(Color.FromArgb(255, 255, 0, 0)), cx - R, cy - R, R * 2, R * 2);

                writer.WriteVideoFrame(bitmap1);//寫入影格
            }

            //關閉檔案
            writer.Close();

            richTextBox1.Text += "製作繪圖影片 OK\n";

            pictureBox1.Image = bitmap1;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //test VideoFileWriter  0

            string filename = "test0.avi";
            int W = 640;
            int H = 480;
            int frameRate = 25;
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            VideoFileWriter writer = new VideoFileWriter();
            writer.Open(filename, W, H, frameRate, VideoCodec.MPEG4);

            Bitmap image = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(image);
            g.FillRectangle(Brushes.Black, 0, 0, W, H);
            Brush[] brushList = new Brush[] { Brushes.Green, Brushes.Red, Brushes.Yellow, Brushes.Pink, Brushes.LimeGreen };
            Random rnd = new Random();

            for (int i = 0; i < 250; i++)
            {
                int rndTmp = rnd.Next(1, 3);
                Application.DoEvents();
                g.FillRectangle(brushList[i % 5], (i % W) * 2, (i % H) * 0.5f, i % 30, i % 30);
                g.FillRectangle(brushList[i % 5], (i % W) * 2, (i % H) * 2, i % 30, i % 30);
                g.FillRectangle(brushList[i % 5], (i % W) * 0.5f, (i % H) * 2, i % 30, i % 30);
                g.Save();
                writer.WriteVideoFrame(image);
            }

            g.DrawString("(c) 2016 - Test Video", new System.Drawing.Font("Calibri", 30), Brushes.White, 80, 240);
            g.Save();
            for (int i = 0; i < 125; i++)
            {
                writer.WriteVideoFrame(image);
            }

            writer.Close();
            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //test VideoFileWriter  1
            //int frameRate = 25;
            int W = 512;
            int H = 512;
            int[] frameRates = { 60, 120, 180 };

            double preamblePostamble = 0.5;    // seconds
            double movieLength = 20.0;    // seconds

            foreach (var frameRate in frameRates)
            {
                richTextBox1.Text += "frameRate = " + frameRate.ToString() + "\n";
                Application.DoEvents();

                VideoFileWriter writer = new VideoFileWriter();
                VideoCodec codec = VideoCodec.WMV2;

                string filename = "test1." + codec.ToString() + "." + frameRate.ToString("000") + "Hz." + movieLength.ToString() + "sec." + W.ToString() + "." + H.ToString() + ".avi";
                if (File.Exists(filename) == true)
                {
                    File.Delete(filename);
                }

                writer.Open(filename, W, H, frameRate, codec);

                RectangleF rectText = new RectangleF(W / 2, 0, W / 2, H);
                RectangleF rectBlock = new RectangleF(0, 0, W / 2, H);

                Bitmap bmp = new Bitmap(W, H, PixelFormat.Format24bppRgb);
                SolidBrush brushWhite = new SolidBrush(Color.White);
                SolidBrush brushBlack = new SolidBrush(Color.Black);
                var font = new Font("Tahoma", W <= 64 ? 8 : W <= 128 ? 12 : W <= 256 ? 16 : 20);

                // Preamble
                for (int i = 0; i < (int)(frameRate * preamblePostamble); i++)
                {
                    using (Graphics g = Graphics.FromImage(bmp))
                    {
                        g.Clear(Color.Black);
                        g.Flush();
                    }
                    writer.WriteVideoFrame(bmp);
                }

                for (int i = 0; i < (int)(frameRate * movieLength); i++)
                {
                    bmp.SetPixel(i % W, i % H, Color.Blue);

                    using (Graphics g = Graphics.FromImage(bmp))
                    {
                        g.Clear(Color.Black);
                        g.SmoothingMode = SmoothingMode.AntiAlias;
                        g.InterpolationMode = InterpolationMode.HighQualityBicubic;
                        g.PixelOffsetMode = PixelOffsetMode.HighQuality;
                        g.DrawString(i.ToString(), font, Brushes.White, rectText);

                        g.FillRectangle(((i & 1) == 0) ? brushWhite : brushBlack, rectBlock);
                        g.Flush();
                    }
                    writer.WriteVideoFrame(bmp);
                }

                // Postamble
                for (int i = 0; i < (int)(frameRate * preamblePostamble); i++)
                {
                    using (Graphics g = Graphics.FromImage(bmp))
                    {
                        g.Clear(Color.Black);
                        g.Flush();
                    }
                    writer.WriteVideoFrame(bmp);
                }

                writer.Close();
                richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
            }
            richTextBox1.Text += "完成\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "桌面錄影 10秒\n";

            string filename = "test2.avi";
            int W = 800;
            int H = 600;
            int frameRate = 5;  //5 fps, 所以要錄50張
            int frameCount = frameRate * 10;
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            VideoFileWriter writer = new VideoFileWriter();

            writer.Open(filename, W, H, frameRate, VideoCodec.MPEG4);

            int i = 0;
            for (i = 0; i < frameCount; i++)
            {
                Stopwatch sw = new Stopwatch();
                sw.Start();
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

                    if (200 - t > 0)
                        Thread.Sleep((int)(200 - t));
                }
            }

            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "錄影 1000張圖, 25fps, 所以是40秒\n";

            string filename = "test3.wmv";
            int W = 800;
            int H = 600;
            int frameRate = 25;  //25 fps
            int frameCount = 1000;
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            VideoFileWriter writer = new VideoFileWriter();
            writer.Open(filename, W, H, frameRate, VideoCodec.MPEG4);

            // create a bitmap to save into the video file
            Bitmap image = new Bitmap(W, H, PixelFormat.Format24bppRgb);

            // write 1000 video frames
            for (int i = 0; i < frameCount; i++)
            {
                image.SetPixel(i % W, i % H, Color.Red);
                writer.WriteVideoFrame(image);
            }
            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = "test4.avi";
            int W = 990;
            int H = 742;
            int frameRate = 1;  //一秒一張
            int frameCount = 360;   //一秒一張  所以是6分鐘
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            VideoFileWriter writer = new VideoFileWriter();
            //writer.Open(filename, W, H, frameRate, VideoCodec.WMV1);
            writer.Open(filename, W, H, frameRate, VideoCodec.MPEG4);

            Bitmap image = new Bitmap(W, H);

            string pic_filename = @"C:\_git\vcs\_1.data\______test_files1\bear.bmp";

            image = new Bitmap(pic_filename);

            for (int i = 0; i < frameCount; i++)
            {
                writer.WriteVideoFrame(image);
            }
            image.Dispose();

            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = "test5.avi";
            int W = 0;
            int H = 0;
            int frameRate = 1;  //一秒一張  若是30，就是一秒30張
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_MU";
            var dinfo = new DirectoryInfo(foldername);
            var files = dinfo.GetFiles().OrderBy(p => p.Name).ToArray();
            string pic_filename = @"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\id_card_01.jpg";
            Bitmap image = (Bitmap)Image.FromFile(pic_filename);
            VideoFileWriter writer = new VideoFileWriter();

            W = image.Width;
            H = image.Height;
            writer.Open(filename, W, H, frameRate, VideoCodec.MPEG4);
            foreach (var file in files)
            {
                if (file.FullName.Contains("id_card") == true)
                {
                    Console.WriteLine(file.FullName);
                    image = (Bitmap)Image.FromFile(file.FullName);
                    writer.WriteVideoFrame(image);
                }
            }
            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string filename = "test7.avi";
            int W = 640;
            int H = 480;
            int frameRate = 1;  //一秒一張  若是30，就是一秒30張
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            var residualBuffer = new Bitmap(W, H, PixelFormat.Format32bppArgb);
            var residualBufferGraphics = Graphics.FromImage(residualBuffer);
            residualBufferGraphics.CompositingMode = CompositingMode.SourceOver;
            residualBufferGraphics.CompositingQuality = CompositingQuality.HighSpeed;

            //Image residualSpriteImage = null;
            Point mapOrigin = Point.Empty;
            Size mapSize = Size.Empty;
            Point dataOrigin = Point.Empty;
            Size dataSize = Size.Empty;

            var heatMapFadeMatrix = new ColorMatrix();

            heatMapFadeMatrix.Matrix33 = 0.95f;// alphaFade;

            var heatMapFadeImageAttributes = new ImageAttributes();
            heatMapFadeImageAttributes.SetColorMatrix(heatMapFadeMatrix);

            var residualFadeMatrix = new ColorMatrix();
            residualFadeMatrix.Matrix00 = 0.45f;
            residualFadeMatrix.Matrix01 = 0.45f;
            residualFadeMatrix.Matrix02 = 0.45f;
            residualFadeMatrix.Matrix10 = 0.45f;
            residualFadeMatrix.Matrix11 = 0.45f;
            residualFadeMatrix.Matrix12 = 0.45f;
            residualFadeMatrix.Matrix20 = 0.45f;
            residualFadeMatrix.Matrix21 = 0.45f;
            residualFadeMatrix.Matrix22 = 0.45f;


            var residualFadeImageAttributes = new ImageAttributes();
            residualFadeImageAttributes.SetColorMatrix(residualFadeMatrix);

            //var lastTime = 0u;
            //var endPadding = 8 * options.Duration * frameRate;
            var endPadding = 8 * 50 * frameRate;

            var font = new Font("Consolas", 10.0f);
            var pens = new[] {
                new Pen(Color.FromArgb(unchecked((int) 0x080000FF))),
                new Pen(Color.FromArgb(unchecked((int) 0x08FF0000)))
             };
            residualBufferGraphics.CompositingMode = CompositingMode.SourceOver;

        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將.avi的聲音分離出來\n";
            string audio_filename = "test9.wav";
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

        private void button10_Click(object sender, EventArgs e)
        {
            //轉錄
            string filename_read = "test5.avi";
            string filename_write = "test5b.avi";

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
            int frameRate = reader.FrameRate;

            /*
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";
            richTextBox1.Text += "frameRate = " + frameRate.ToString() + "\n";
            richTextBox1.Text += "end = " + end.ToString() + "\n";
            */

            writer.Open(filename_write, W, H, frameRate, VideoCodec.MPEG4);

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

        private void button11_Click(object sender, EventArgs e)
        {

        }
    }
}
