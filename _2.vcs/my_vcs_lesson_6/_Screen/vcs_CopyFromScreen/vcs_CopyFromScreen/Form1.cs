using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;       //for Process
using System.Drawing.Imaging;   //ImageFormat
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_CopyFromScreen
{
    public partial class Form1 : Form
    {
        //本程式截圖 ST
        [DllImportAttribute("gdi32.dll")]

        private static extern bool BitBlt(
        IntPtr hdcDest, //目的DC的句柄
        int nXDest, //目的圖形的左上角的x坐標
        int nYDest, //目的圖形的左上角的y坐標
        int nWidth, //目的圖形的矩形寬度
        int nHeight, //目的圖形的矩形高度
        IntPtr hdcSrc, //源DC的句柄
        int nXSrc, //源圖形的左上角的x坐標
        int nYSrc, //源圖形的左上角的x坐標
        System.Int32 dwRop //光柵操作代碼
        );
        //本程式截圖 SP


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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 120 + 10;
            dy = 50 + 10;

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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            this.Location = new Point(200, 100);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //抓屏將生成的圖片顯示在pictureBox

            Image image1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);

            Graphics g = Graphics.FromImage(image1);

            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));

            //IntPtr dc1 = g.GetHdc();      //此處這兩句多餘，具體看最後GetHdc()定義

            //g.ReleaseHdc(dc1);           

            g.Dispose();

            this.pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

            this.pictureBox1.Image = image1;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            save_fullscreen_to_local_drive();       //全螢幕截圖
        }

        void save_fullscreen_to_local_drive()
        {
            //全螢幕截圖
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            using (Bitmap bitmap1 = new Bitmap(W, H))   //建立空白畫布
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    //取得畫布的繪圖物件用以繪圖
                    g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";
                    IntPtr dc1 = g.GetHdc();
                    g.ReleaseHdc(dc1);
                }

                //存成bmp檔
                String filename = Application.StartupPath + "\\image_full_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                richTextBox1.Text += "全螢幕截圖，存檔檔名：" + filename + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            save_current_program_to_local_drive();  //本程式截圖
        }

        void save_current_program_to_local_drive()
        {
            //本程式截圖
            int W = this.Width;
            int H = this.Height;

            using (Bitmap bitmap1 = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
                    g.CopyFromScreen(this.Location, new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";
                    IntPtr dc1 = g.GetHdc();
                    g.ReleaseHdc(dc1);
                }

                //存成bmp檔
                String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }

                //存成jpg檔
                //String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                //bitmap1.Save(filename, ImageFormat.Jpeg);

                richTextBox1.Text += "本程式截圖，存檔檔名：" + filename + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //抓螢幕某區塊為檔案, 從(x_st, y_st)開始, 抓 W X H 大小的圖
            int x_st = 300;
            int y_st = 200;
            int W = 1000;
            int H = 200;

            using (Bitmap bitmap1 = new Bitmap(W, H))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    //                   擷取螢幕位置起點    自建bmp的位置起點     擷取大小
                    g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(W, H));
                    //richTextBox1.Text += "W = " + W.ToString() + "\n";
                    //richTextBox1.Text += "H = " + H.ToString() + "\n";

                    //pictureBox1.Image = image;   //若有picturebox 可以貼上
                }
                //存成bmp檔
                String filename = Application.StartupPath + "\\image_partial_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                try
                {
                    bitmap1.Save(filename, ImageFormat.Bmp);
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                richTextBox1.Text += "已部分截圖存檔完成, 檔名 : " + filename + "\n";
            }
        }

        //抓特定程式的畫面

        //範圍
        public struct Rect
        {
            public int Left;
            public int Top;
            public int Right;
            public int Bottom;
        }
        [DllImport("user32.dll")]
        //取得應用程式畫面
        public static extern Boolean GetWindowRect(IntPtr hWnd, ref Rect rect);
        [DllImport("User32.dll")]
        private static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);
        [DllImport("User32.dll")]
        //將程式置於前景
        private static extern bool SetForegroundWindow(IntPtr hWnd);
        [DllImport("user32.dll")]
        //顯示視窗
        private static extern IntPtr ShowWindow(IntPtr hWnd, int nCmdShow);

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "抓特定程式的畫面  要先打開putty\n";

            richTextBox1.Text = string.Empty;

            // 列出系統中所有的程序
            //Process[] processes = Process.GetProcesses(Environment.MachineName);   //相同
            Process[] processes = Process.GetProcesses();

            richTextBox1.Text += "系統中共有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process p in processes)
            {
                /*
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除。對其他程序取時間也會造成錯誤，故不用。
                if (!p.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    richTextBox1.Text += p.ProcessName + "\t\t" + p.StartTime.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                }
                else
                {
                    richTextBox1.Text += p.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
                }
                */

                //取得特定應用程式的資訊
                //richTextBox1.Text += p.ProcessName + "\n";
                if (p.ProcessName == "putty")
                {
                    richTextBox1.Text += p.ProcessName + "\n";
                    SetForegroundWindow(p.MainWindowHandle);
                    ShowWindow(p.MainWindowHandle, 1);
                    richTextBox1.Text += "time = " + p.StartTime.ToString() + "\n";
                    Rect rect = new Rect();
                    GetWindowRect(p.MainWindowHandle, ref rect);
                    richTextBox1.Text += "Left = " + rect.Left.ToString() + "\n";
                    richTextBox1.Text += "Right = " + rect.Right.ToString() + "\n";
                    richTextBox1.Text += "Top = " + rect.Top.ToString() + "\n";
                    richTextBox1.Text += "Bottom = " + rect.Bottom.ToString() + "\n";
                    richTextBox1.Text += "Width = " + (rect.Right - rect.Left).ToString() + "\n";
                    richTextBox1.Text += "Height = " + (rect.Bottom - rect.Top).ToString() + "\n";

                    richTextBox1.Text += "擷取此應用程式的畫面\n";

                    int width = rect.Right - rect.Left;
                    int height = rect.Bottom - rect.Top;
                    Bitmap bmp = new Bitmap(width, height, PixelFormat.Format32bppArgb);

                    Graphics.FromImage(bmp).CopyFromScreen(rect.Left,
                                                           rect.Top,
                                                           0,
                                                           0,
                                                           new Size(width, height),
                                                           CopyPixelOperation.SourceCopy);
                    string filename = Application.StartupPath + "\\capture_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                    //string path = DateTime.Now.ToString("yyyyMMdd HHmmss") + ".jpg";
                    //bmp.Save(path);
                    bmp.Save(filename, ImageFormat.Jpeg);
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            save_current_program_to_local_drive2();
        }

        void save_current_program_to_local_drive2()
        {
            //imsLink的方法
            //本程式截圖
            Bitmap bmp = new Bitmap(this.Width, this.Height);
            Graphics g = Graphics.FromImage(bmp);
            //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(this.Width, this.Height));
            //richTextBox1.Text += "W = " + this.Width.ToString() + "\n";
            //richTextBox1.Text += "H = " + this.Height.ToString() + "\n";
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);

            //存成bmp檔
            String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bmp.Save(filename, ImageFormat.Bmp);

            //存成jpg檔
            //String filename = Application.StartupPath + "\\picture\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //myImage.Save(filename, ImageFormat.Jpeg);
            richTextBox1.Text += "本程式截圖，存檔檔名：" + filename + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //全螢幕截圖1
            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap1 = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);
                    //存成bmp檔
                    String filename = Application.StartupPath + "\\image_full_screen_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    richTextBox1.Text += "全螢幕截圖，存檔檔名：" + filename + "\n";
                }
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //全螢幕截圖2
            Bitmap bitmap1;
            Graphics g;

            bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height, System.Drawing.Imaging.PixelFormat.Format32bppArgb);
            g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(Screen.PrimaryScreen.Bounds.X, Screen.PrimaryScreen.Bounds.Y, 0, 0, Screen.PrimaryScreen.Bounds.Size, CopyPixelOperation.SourceCopy);
            String filename = Application.StartupPath + "\\image_full_screen_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(filename, ImageFormat.Bmp);
            richTextBox1.Text += "全螢幕截圖，存檔檔名：" + filename + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //全螢幕截圖
            //抓取全螢幕的小程序
            Bitmap bitmap1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(0, 0, 0, 0, new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            this.pictureBox1.Image = bitmap1;

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //抓取指定螢幕的一部分存檔
            Point source_point = new Point(0, 0);
            Point destination_point = new Point(0, 0);
            Rectangle rect = new Rectangle(0, 0, 300, 300);

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            CaptureImage(source_point, destination_point, rect, filename);
        }

        public void CaptureImage(Point SourcePoint, Point DestinationPoint, Rectangle SelectionRectangle, string filename)
        {
            using (Bitmap bitmap1 = new Bitmap(SelectionRectangle.Width, SelectionRectangle.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap1))
                {
                    g.CopyFromScreen(SourcePoint, DestinationPoint, SelectionRectangle.Size);
                }

                try
                {
                    //bitmap1.Save(@file1, ImageFormat.Jpeg);
                    bitmap1.Save(filename, ImageFormat.Bmp);
                    //bitmap1.Save(@file3, ImageFormat.Png);

                    //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename + "\n";
                    //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //擷取部分圖片貼上

            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bitmap = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bitmap))
                {
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);
                }
                bitmap.Save("test.jpg", ImageFormat.Jpeg);
            }
        }

        public static void Snap(int x, int y, int width, int height)
        {
            try
            {
                //這段代碼也可以實現截圖
                //Image image = new Bitmap(width, height);
                //Graphics g = Graphics.FromImage(image);
                //g.CopyFromScreen(x, y, 0, 0, new System.Drawing.Size(width, height));
                //string hour = DateTime.Now.Minute.ToString();
                //string second = DateTime.Now.Second.ToString();
                //image.Save(ScreenshotPath + "\\" + hour + "_" + second + ".jpg");

                Bitmap image = new Bitmap(640, 480);
                using (Graphics g = Graphics.FromImage(image))
                {
                    g.CopyFromScreen(0, 0, 0, 0, image.Size);
                    g.Dispose();
                    string hour = DateTime.Now.Minute.ToString();
                    string second = DateTime.Now.Second.ToString();
                    image.Save("aaa.jpg");
                }
            }
            catch
            {
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //實現全屏截圖
            //上面的Snap
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //抓屏將生成的圖片顯示在pictureBox

            Image image1 = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            Graphics g = Graphics.FromImage(image1);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            //IntPtr dc1 = g.GetHdc();      //此處這兩句多餘，具體看最後GetHdc()定義
            //g.ReleaseHdc(dc1);           
            g.Dispose();
            this.pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
            this.pictureBox1.Image = image1;
            image1.Save("Screen.png", ImageFormat.Png);

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //全屏幕截圖 3種


            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;


            //全屏幕截圖 1

            Bitmap bitmap1 = new Bitmap(W, H); //創建一個與屏幕大小一樣的位圖

            using (Graphics g = Graphics.FromImage(bitmap1))
            {
                g.CopyFromScreen(0, 0, 0, 0, new Size(W, H));  //用Graphics.CopyFromScreen()把屏幕位圖拷貝到該位圖上
            }
            pictureBox1.Image = bitmap1;

            //存圖
            //bitmap1.Save("111.jpg");

            //bitmap1.Dispose();

            //顯示
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.Image = bitmap1;


            //全屏幕截圖 2
            //獲得當前屏幕的分辨率
            Screen scr = Screen.PrimaryScreen;
            Rectangle rc = scr.Bounds;
            int w = rc.Width;
            int h = rc.Height;
            //創建一個和屏幕一樣大的Bitmap
            Image image = new Bitmap(w, h);
            //從一個繼承自Image類的對象中創建Graphics對象
            Graphics g2 = Graphics.FromImage(image);
            //抓屏並拷貝到myimage裡
            g2.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(w, h));

            //存圖
            //image.Save("aaaaaa.jpeg");

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //本程式截圖
            Graphics g1 = this.CreateGraphics();//獲得窗體圖形對象

            Image image = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height, g1);

            Graphics g2 = Graphics.FromImage(image);//創建位圖圖形對象

            IntPtr dc1 = g1.GetHdc();//獲得窗體的上下文設備

            IntPtr dc2 = g2.GetHdc();//獲得位圖文件的上下文設備

            BitBlt(dc2, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height, dc1, 0, 0, 13369376);//寫入到位圖

            g1.ReleaseHdc(dc1);//釋放窗體的上下文設備

            g2.ReleaseHdc(dc2);//釋放位圖文件的上下文設備


            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            try
            {
                image.Save(filename, ImageFormat.Bmp);
                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}

