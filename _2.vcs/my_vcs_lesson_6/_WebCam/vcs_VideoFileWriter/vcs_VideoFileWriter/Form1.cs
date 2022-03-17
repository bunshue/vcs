using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Threading;
using System.Diagnostics;   //for Stopwatch

using AForge.Video;
using AForge.Video.DirectShow;  // Video Recording
using AForge.Video.FFMPEG;      //for VideoFileWriter

using System.Drawing.Drawing2D;

using System.Drawing.Imaging;   //for PixelFormat

using AviFile;

namespace vcs_VideoFileWriter
{
    public partial class Form1 : Form
    {
        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;
        private bool flag_webcam_ok = false;    //判斷是否啟動webcam的旗標
        Stopwatch stopwatch;

        private const int BORDER = 10;

        private bool flag_recording = false;    //判斷是否啟動錄影的旗標, for 錄影1
        private bool flag_limit_recording_time = false;
        private string recording_filename = string.Empty;
        VideoFileWriter writer = new VideoFileWriter();
        DateTime recording_time_st = DateTime.Now;

        int webcam_w = 0;
        int webcam_h = 0;
        int webcam_fps = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象

                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.

                //以下為WebCam訊息與調整視窗大小
                //Cam.VideoResolution = Cam.VideoCapabilities[0];
                string webcam_name = string.Empty;
                int ww = Cam.VideoCapabilities[0].FrameSize.Width;
                int hh = Cam.VideoCapabilities[0].FrameSize.Height;
                //webcam_name = USBWebcams[0].Name + " " + ww.ToString() + " X " + hh.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                webcam_name = USBWebcams[0].Name + " " + ww.ToString() + " X " + hh.ToString();
                this.Text = webcam_name;

                //有抓到WebCam, 重新設定pictureBox和vsp的大小和位置
                pictureBox1.Size = new Size(ww, hh);
                //pictureBox1.Location = new Point(BORDER, BORDER);

                stopwatch = new Stopwatch();
                stopwatch.Start();
                flag_webcam_ok = true;

                webcam_w = ww;
                webcam_h = hh;
                //webcam_fps = fps;
            }
            else
            {
                this.Text = "無影像裝置";
                flag_webcam_ok = false;

            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (Cam != null)
            {
                if (Cam.IsRunning)  // When Form1 closes itself, WebCam must stop, too.
                {
                    Cam.Stop();   // WebCam stops capturing images.
                    Cam.SignalToStop();
                    Cam.WaitForStop();
                }
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public Bitmap bm = null;
        int frame_cnt = 0;          //每多少張做一個計算
        int frame_count = 0;        //計算fps用
        int frame_count_old = 0;    //計算fps用
        DateTime dt_old = DateTime.Now;

        Graphics g;
        //SolidBrush drawBrush;
        Font drawFont1;

        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            frame_count++;
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();

            g = Graphics.FromImage(bm);

            //顯示時間
            SolidBrush drawBrush;
            Font drawFont;
            string drawDate;
            int x_st = 0;
            int y_st = 0;

            drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            drawBrush = new SolidBrush(Color.Yellow);
            drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);

            //在畫面的上方顯示時間
            g.DrawString(drawDate, drawFont, drawBrush, BORDER * 3, BORDER);

            if (flag_recording == true)
            {
                if (DateTime.Now.Millisecond > 500)
                {
                    //g.DrawString("錄影中", drawFont, new SolidBrush(Color.Red), BORDER+230, BORDER);
                    g.FillEllipse(Brushes.Red, 5, BORDER, 25, 25);
                }

                try
                {
                    writer.WriteVideoFrame(bm);
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "xxx錯誤訊息e01 : " + ex.Message + "\n";
                }
            }

            //bm.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;

            GC.Collect();       //回收資源
        }

        void show_item_location()
        {
            int x_st = BORDER;
            int y_st = BORDER;
            int dx = 140 + 50;
            int dy = 50 + 15;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 670);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_fps.Text = "";
            lb_fps.Location = new Point(750, 5);
        }

        private void button0_Click(object sender, EventArgs e)
        {
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

        private void button1_Click(object sender, EventArgs e)
        {
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

        private void button2_Click(object sender, EventArgs e)
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

        private void button3_Click(object sender, EventArgs e)
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

        private void button4_Click(object sender, EventArgs e)
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

            string pic_filename = @"C:\______test_files\bear.bmp";

            image = new Bitmap(pic_filename);

            for (int i = 0; i < frameCount; i++)
            {
                writer.WriteVideoFrame(image);
            }
            image.Dispose();

            writer.Close();

            richTextBox1.Text += "製作影片完成, 檔案 : " + filename + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = "test5.avi";
            int W = 0;
            int H = 0;
            int frameRate = 1;  //一秒一張  若是30，就是一秒30張
            if (File.Exists(filename) == true)
            {
                File.Delete(filename);
            }

            string foldername = @"C:\______test_files\__pic\_MU";
            var dinfo = new DirectoryInfo(foldername);
            var files = dinfo.GetFiles().OrderBy(p => p.Name).ToArray();
            string pic_filename = @"C:\______test_files\__pic\_MU\id_card_01.jpg";
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

        private void button6_Click(object sender, EventArgs e)
        {
            string filename_read = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_WebCam\vcs_VideoFileWriter\vcs_VideoFileWriter\bin\Debug\test5.avi";
            string filename_write = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_WebCam\vcs_VideoFileWriter\vcs_VideoFileWriter\bin\Debug\test5b.avi";
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

        private void button7_Click(object sender, EventArgs e)
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

            Image residualSpriteImage = null;
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

            var lastTime = 0u;
            //var endPadding = 8 * options.Duration * frameRate;
            var endPadding = 8 * 50 * frameRate;

            var font = new Font("Consolas", 10.0f);
            var pens = new[] {
                new Pen(Color.FromArgb(unchecked((int) 0x080000FF))),
                new Pen(Color.FromArgb(unchecked((int) 0x08FF0000)))
             };
            residualBufferGraphics.CompositingMode = CompositingMode.SourceOver;




        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "將.avi的聲音分離出來\n";
            string audio_filename = "test9.wav";
            if (File.Exists(audio_filename) == true)
            {
                File.Delete(audio_filename);
            }

            string filename = @"C:\______test_files\__RW\_avi\i2c.avi";

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

        void do_record()
        {
            if (flag_webcam_ok == false)    //如果webcam沒啟動
            {
                richTextBox1.Text += "無相機\n";
                return;
            }

            if (flag_recording == false)
            {
                //開啟錄影模式
                flag_recording = true;

                recording_filename = Application.StartupPath + "\\avi_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".avi";

                richTextBox1.Text += "filename : " + recording_filename + "\n";
                richTextBox1.Text += "Width : " + webcam_w.ToString() + "\n";
                richTextBox1.Text += "Height : " + webcam_h.ToString() + "\n";

                int fps = 30;
                //writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.MPEG4);
                writer.Open(recording_filename, webcam_w, webcam_h, fps, VideoCodec.WMV2);

                richTextBox1.Text += "錄影開始\t時間 : " + DateTime.Now.ToString() + "\n";
                recording_time_st = DateTime.Now;
            }
            else
            {
                richTextBox1.Text += "已在錄影\n";
            }
        }

        //錄影 ST
        private void bt_record_start_Click(object sender, EventArgs e)
        {
            flag_limit_recording_time = false;
            do_record();
        }

        //錄影 ST, 有限時
        private void bt_record_start2_Click(object sender, EventArgs e)
        {
            flag_limit_recording_time = true;
            do_record();
        }

        //錄影 SP
        private void bt_record_stop_Click(object sender, EventArgs e)
        {
            if (flag_recording == true)
            {
                //錄影完需將影像停止不然會出錯
                flag_recording = false;

                writer.Close();

                richTextBox1.Text += "錄影結束\t時間 : " + DateTime.Now.ToString() + "\n";
                richTextBox1.Text += "錄影時間 :\t" + (DateTime.Now - recording_time_st).TotalSeconds.ToString("0.00") + " 秒\n";
                //richTextBox1.Text += "錄影時間 : " + (DateTime.Now - recording_time_st).ToString() + "\n\n";
                richTextBox1.Text += "檔案 :\t\t" + recording_filename + "\n\n";
                flag_limit_recording_time = false;
            }
            else
            {
                richTextBox1.Text += "並沒有在錄影\n";
            }
        }

        int min_old = 0;
        private void timer_fps_Tick(object sender, EventArgs e)
        {
            if (flag_webcam_ok == true)
            {
                DateTime dt = DateTime.Now;
                lb_fps.Text = (((frame_count - frame_count_old) * 1000) / ((TimeSpan)(dt - dt_old)).TotalMilliseconds).ToString("F2") + " fps";
                dt_old = dt;
                frame_count_old = frame_count;

                if (flag_recording == true)
                {
                    int min = (int)((DateTime.Now - recording_time_st).TotalMinutes);
                    if ((min > 0) && (min != min_old))
                    {
                        richTextBox1.Text += "已錄影 " + min.ToString() + " 分\n";
                        min_old = min;
                    }

                    if (flag_limit_recording_time == true)
                    {
                        if ((DateTime.Now - recording_time_st).TotalSeconds > 180)
                        {
                            flag_limit_recording_time = false;
                            bt_record_stop_Click(sender, e);
                        }
                    }
                }
            }
            else
            {
                lb_fps.Text = "";
            }
        }

    }
}

