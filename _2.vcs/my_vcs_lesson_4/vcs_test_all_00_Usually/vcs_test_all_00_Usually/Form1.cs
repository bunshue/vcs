using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;   //for SecurityProtocolType
using System.Drawing.Imaging;   //for ImageFormat
using System.Runtime.InteropServices;   //for DllImport

using AForge.Video;             //需要添加這兩個.dll
using AForge.Video.DirectShow;

using AxWMPLib;
/*  sugar
使用AxWindowsMediaPlayer播放多媒體

加入工具箱

工具箱/滑鼠右鍵/選擇項目/
/COM元件 頁籤 /勾選Windows Media Player(wmp.dll)	/ 確定

會發現工具箱多了個Windows Media Player的控制項
就是 axWindowsMediaPlayer

拉一個Windows Media Player控件進表單, 參考裡面就會出現AxWMPLib和WMPLib
*/

namespace vcs_test_all_00_Usually
{
    public partial class Form1 : Form
    {
        //WebCam ST
        //參考
        //【AForge.NET】C#上使用AForge.Net擷取視訊畫面
        //https://ccw1986.blogspot.com/2013/01/ccaforgenetcapture-image.html

        //AForge下載鏈結
        //http://www.aforgenet.com/framework/downloads.html

        //參考/右鍵/加入參考/瀏覽AForge.Video.dll和AForge.Video.DirectShow.dll

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;
        //WebCam SP

        //移動無邊框窗體1 ST
        [DllImport("user32.dll")]
        public static extern bool ReleaseCapture();
        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);
        public const int WM_SYSCOMMAND = 0x0112;
        public const int SC_MOVE = 0xF010;
        public const int HTCAPTION = 0x0002;
        //移動無邊框窗體1 SP

        //移動無邊框窗體2 ST
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x1;
        //private const int HTCAPTION = 0x2;

        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_NCHITTEST:
                    base.WndProc(ref m);
                    if ((int)m.Result == HTCLIENT)
                        m.Result = (IntPtr)HTCAPTION;
                    return;
                    break;
            }
            base.WndProc(ref m);
        }
        //移動無邊框窗體2 SP


        //移動無邊框窗體3 ST
        Point mouseOffset3;  // 移動無邊框窗體用
        //移動無邊框窗體3 SP

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE

        AxWindowsMediaPlayer axWindowsMediaPlayer1;
        bool flag_repeat_mode = true;

        Graphics g;
        Pen p = new Pen(Color.Red, 3);
        SolidBrush sb = new SolidBrush(Color.Black);
        Font f = new Font("標楷體", 18);
        Bitmap bitmap1;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //網頁protocol	解決  要求已經中止: 無法建立 SSL/TLS 的安全通道。
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            show_item_location();

            /*
            //讀取圖檔
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);
            */

            p = new Pen(Color.Red, 3);

            //指定畫布大小
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;

            /*
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            pictureBox1.Image = Image.FromStream(fs);
            fs.Close();
            */

            //移動無邊框窗體4 ST
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.WinForm_MouseDown);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.WinForm_MouseUp);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.WinForm_MouseMove);
            //移動無邊框窗體4 SP
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

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
            button20.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 1 + 40);

            label1a.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            label1b.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 25);
            label1c.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 50);
            label1d.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 75);
            label1a.Text = "移動無邊框窗體1/5, 使用MouseDown";
            label1b.Text = "移動無邊框窗體2, 最簡易";
            label1c.Text = "移動無邊框窗體3, 使用MouseDown-Move-Up";
            label1d.Text = "移動無邊框窗體4, 使用MouseDown-Move-Up";

            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 110);
            label3.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 140);
            lb_main_mesg1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 170);

            pictureBox1.Size = new Size(400, 450);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1273, 750);
            this.Text = "vcs_test_all_00_Usually";

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
            //this.WindowState = FormWindowState.Maximized;

            //離開按鈕的寫法
            bt_exit_setup();

            //最小化按鈕的寫法
            bt_minimize_setup();

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            //指定畫布大小
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            pictureBox1.Image = bitmap1;
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            //移動無邊框窗體1 ST
            ReleaseCapture();
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_MOVE + HTCAPTION, 0);
            //移動無邊框窗體1 SP

            //移動無邊框窗體3 ST
            mouseOffset3 = new Point(e.X, e.Y);
            //移動無邊框窗體3 SP

            //移動無邊框窗體5 ST
            const int WM_NCLBUTTONDOWN = 0xA1;
            const int HT_CAPTION = 0x2;
            this.Capture = false;
            Message msg = Message.Create(this.Handle, WM_NCLBUTTONDOWN, (IntPtr)HT_CAPTION, IntPtr.Zero);
            WndProc(ref msg);
            //移動無邊框窗體5 SP
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            //移動無邊框窗體3 ST
            if (e.Button == MouseButtons.Left)
            {
                this.Left += e.X - mouseOffset3.X;
                this.Top += e.Y - mouseOffset3.Y;
            }
            //移動無邊框窗體3 SP

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //一些繪圖指令
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Bitmap bitmap1 = new Bitmap(640, 480);

            string filename0 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename0);	//Bitmap.FromFile出來的是Image格式
            //pictureBox1.Image = bitmap1;

            //自動檔名 與 存檔語法
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

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
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int x;
            int y;
            richTextBox1.Text += "y = sin(x)\n";
            for (x = 0; x <= 360; x += 30)
            {
                y = (int)(100 * sind(x));
                richTextBox1.Text += "x = " + x.ToString() + ", y = " + y.ToString() + "\n";
            }

            for (x = 0; x <= 360; x += 30)
            {
                richTextBox1.Text += "x = " + x.ToString() + "\t" + (rad(x) / Math.PI).ToString() + " pi rad\t" + 100 * sind(x) + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_main_message1("顯示訊息", S_OK, 10);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //使用WMP
            this.axWindowsMediaPlayer1 = new AxWindowsMediaPlayer();
            this.axWindowsMediaPlayer1.Enabled = true;
            //this.axWindowsMediaPlayer1.Location = new System.Drawing.Point(0, 400);
            //this.axWindowsMediaPlayer1.Name = "axWindowsMediaPlayer1";
            //this.axWindowsMediaPlayer1.Size = new System.Drawing.Size(800, 500);
            //this.axWindowsMediaPlayer1.TabIndex = 2;
            //this.axWindowsMediaPlayer1.Visible = false;   //fail
            this.axWindowsMediaPlayer1.StatusChange += new EventHandler(axWindowsMediaPlayer1_StatusChange);
            this.Controls.Add(this.axWindowsMediaPlayer1);
            axWindowsMediaPlayer1.Visible = false;

            string mp3_filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\16.監獄風雲.mp3";
            axWindowsMediaPlayer1.URL = mp3_filename;
        }

        protected void axWindowsMediaPlayer1_StatusChange(object sender, EventArgs e)
        {
            if (axWindowsMediaPlayer1.playState == WMPLib.WMPPlayState.wmppsStopped)
            {
                //mp3_position = 0;

                //判斷影片是否已經停止播放
                if (flag_repeat_mode == true)
                {
                    //停頓2秒後再重新播放
                    System.Threading.Thread.Sleep(2000);
                    //重新播放
                    axWindowsMediaPlayer1.Ctlcontrols.play();
                }
            }
        }


        //WebCam ST
        private void button5_Click(object sender, EventArgs e)
        {
            if (button5.Text == "開啟WebCam")
            {
                button5.Text = "關閉WebCam";
                start_webcam();
            }
            else
            {
                button5.Text = "開啟WebCam";
                stop_webcam();
            }
        }

        void start_webcam()
        {
            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.
                //richTextBox1.Text += "有影像裝置\n";

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;

                pictureBox1.Size = new Size(ww / 1, hh / 1);
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                //pictureBox1.Location = new Point(50, 50);
            }
            else
            {
                this.Text = "無影像裝置\n";
            }
        }

        void stop_webcam()
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

        public Bitmap bm = null;
        //自定義函數, 捕獲每一幀圖像並顯示
        void Cam_NewFrame(object sender, NewFrameEventArgs eventArgs)
        {
            try
            {
                //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
                bm = (Bitmap)eventArgs.Frame.Clone();
                //pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
            }

            Graphics g = Graphics.FromImage(bm);

            int w;
            int h;
            try
            {
                w = bm.Width;
                h = bm.Height;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
                GC.Collect();       //回收資源
                return;
            }

            //顯示時間
            string drawDate = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            SolidBrush sb = new SolidBrush(Color.Yellow);
            Font f = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
            int x_st = 10;
            int y_st = 10;
            g.DrawString(drawDate, f, sb, x_st, y_st);

            try
            {
                pictureBox1.Image = bm;
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息a : " + ex.Message + "\n";
            }
            GC.Collect();       //回收資源
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            stop_webcam();
        }
        //WebCam SP

        //顯示訊息 ST
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
            }
        }

        //顯示訊息 SP

        private void button6_Click(object sender, EventArgs e)
        {
            int i;
            Int64 total_size = 0;

            total_size = 123;
            for (i = 1; i < 20; i++)
            {
                total_size *= i;
                richTextBox1.Text += "total_size = " + total_size.ToString() + "\t檔案大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
        }

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
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
            //撈出所有控件
            foreach (Control x in Controls)
            {
                //撈出所有的Button
                if (x.GetType().ToString() == "System.Windows.Forms.Button")
                {
                    System.Windows.Forms.Button myCheckbox = (System.Windows.Forms.Button)x;
                    richTextBox1.Text += "Name : " + x.Name + "\tText : " + x.Text + "\n";
                }
            }
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

        //建立無邊框移動之pictureBox ST
        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立無邊框移動之pictureBox\n";

            pbox.Width = 305;
            pbox.Height = 400;
            pbox.Location = new Point(PBOX_DEFAULT_POSITION_X, PBOX_DEFAULT_POSITION_Y);
            pbox.BackColor = Color.White;
            //pbox.SizeMode = PictureBoxSizeMode.Zoom;

            //讀取圖檔
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pbox.Image = Image.FromFile(filename);

            pbox.MouseDown += new MouseEventHandler(pbox_MouseDown);    // 加入事件
            pbox.MouseMove += new MouseEventHandler(pbox_MouseMove);    // 加入事件
            pbox.MouseUp += new MouseEventHandler(pbox_MouseUp);        // 加入事件

            this.Controls.Add(pbox);	// 將控件加入表單
            pbox.BringToFront();
            button10.Enabled = false;
        }

        //pbox initial location
        PictureBox pbox = new PictureBox();
        private const int PBOX_DEFAULT_POSITION_X = 500;
        private const int PBOX_DEFAULT_POSITION_Y = 200;
        int pbox_position_x_old = PBOX_DEFAULT_POSITION_X;
        int pbox_position_y_old = PBOX_DEFAULT_POSITION_Y;

        bool flag_pbox_mouse_down = false;
        private void pbox_MouseDown(object sender, MouseEventArgs e)
        {
            flag_pbox_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            pbox_position_x_old = e.X;
            pbox_position_y_old = e.Y;
        }

        private void pbox_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_pbox_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - pbox_position_x_old;
                int dy = e.Y - pbox_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                pbox.Location = new Point(pbox.Location.X + dx, pbox.Location.Y + dy);
            }
        }

        private void pbox_MouseUp(object sender, MouseEventArgs e)
        {
            flag_pbox_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - pbox_position_x_old;
            int dy = e.Y - pbox_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            pbox.Location = new Point(pbox.Location.X + dx, pbox.Location.Y + dy);
        }

        //建立無邊框移動之pictureBox SP

        //移動無邊框窗體4 ST
        private Point mouseOffset4; //記錄鼠標指針的坐標
        private bool flag_mouse_down = false;
        private void WinForm_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            int xOffset;
            int yOffset;
            if (e.Button == MouseButtons.Left)
            {
                xOffset = -e.X;
                yOffset = -e.Y;
                mouseOffset4 = new Point(xOffset, yOffset);
                flag_mouse_down = true;
            }
        }

        private void WinForm_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            if (flag_mouse_down == true)
            {
                Point mousePos = Control.MousePosition;
                mousePos.Offset(mouseOffset4.X, mouseOffset4.Y);
                Location = mousePos;
            }
        }

        private void WinForm_MouseUp(object sender, System.Windows.Forms.MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                flag_mouse_down = false;
            }
        }

        //移動無邊框窗體4 SP

    }

    //3Form1之外
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
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


