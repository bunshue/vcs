using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;  // for Process
using System.Drawing.Imaging;  // ImageFormat
using System.Runtime.InteropServices;  // for DllImport

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
            System.Int32 dwRop //光柵操作代碼\
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

            pictureBox1.Size = new Size(830, 600);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(300, 600);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1610, 750);
            this.Text = "vcs_CopyFromScreen";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void save_bitmap_file(Bitmap bitmap1)
        {
            //存檔
            String filename = Application.StartupPath + "\\image_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(filename, ImageFormat.Bmp);
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //全螢幕截圖
            int W = Screen.PrimaryScreen.Bounds.Width;  // 主螢幕寬度
            int H = Screen.PrimaryScreen.Bounds.Height;  // 主螢幕高度
            Bitmap bitmap1 = new Bitmap(W, H);  // 建立空白畫布
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));
            //IntPtr dc1 = g.GetHdc();      //此處這兩句多餘，具體看最後GetHdc()定義
            //g.ReleaseHdc(dc1);
            g.Dispose();

            save_bitmap_file(bitmap1);  // 存檔
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        //6060

        private void button2_Click(object sender, EventArgs e)
        {
            save_current_program_to_local_drive();  //本程式截圖
        }

        void save_current_program_to_local_drive()
        {
            //本程式截圖
            int W = this.Width;
            int H = this.Height;
            Bitmap bitmap1 = new Bitmap(W, H);  // 建立空白畫布
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(W, H));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            save_bitmap_file(bitmap1);  // 存檔
        }

        //6060

        private void button3_Click(object sender, EventArgs e)
        {
            //抓螢幕某區塊為檔案, 從(x_st, y_st)開始, 抓 W X H 大小的圖
            int x_st = 300;
            int y_st = 200;
            int W = 1000;
            int H = 200;

            Bitmap bitmap1 = new Bitmap(W, H);  // 建立空白畫布
            Graphics g = Graphics.FromImage(bitmap1);
            //                   擷取螢幕位置起點    自建bmp的位置起點     擷取大小
            g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(W, H));
            //pictureBox1.Image = bitmap1;   //若有picturebox 可以貼上
            save_bitmap_file(bitmap1);  // 存檔
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

                    int W = rect.Right - rect.Left;
                    int H = rect.Bottom - rect.Top;
                    Bitmap bitmap1 = new Bitmap(W, H, PixelFormat.Format32bppArgb);  // 建立空白畫布

                    Graphics.FromImage(bitmap1).CopyFromScreen(rect.Left,
                                                           rect.Top,
                                                           0,
                                                           0,
                                                           new Size(W, H),
                                                           CopyPixelOperation.SourceCopy);

                    save_bitmap_file(bitmap1);  // 存檔
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        //6060

        private void button6_Click(object sender, EventArgs e)
        {
            //全螢幕截圖

            int W = this.Bounds.Width;
            int H = this.Bounds.Height;
            Bitmap bitmap1 = new Bitmap(W, H);  // 建立空白畫布
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(W, H));  //获取没有鼠标的屏幕截图
            g.Dispose();    //释放资源
        }

        //6060

        private void button7_Click(object sender, EventArgs e)
        {
            //全螢幕截圖
            int W = Screen.PrimaryScreen.Bounds.Width;  // 主螢幕寬度
            int H = Screen.PrimaryScreen.Bounds.Height;  // 主螢幕高度

            Bitmap bitmap1 = new Bitmap(W, H, PixelFormat.Format32bppArgb);  // 建立空白畫布
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(0, 0, 0, 0, Screen.PrimaryScreen.Bounds.Size, CopyPixelOperation.SourceCopy);

            save_bitmap_file(bitmap1);  // 存檔
        }

        //6060

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //6060

        private void button9_Click(object sender, EventArgs e)
        {
            //抓取指定螢幕的一部分存檔
            Rectangle rect = new Rectangle(0, 0, 300, 300);

            Bitmap bitmap1 = new Bitmap(rect.Width, rect.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), rect.Size);

            save_bitmap_file(bitmap1);  // 存檔
        }

        //6060

        private void button10_Click(object sender, EventArgs e)
        {
            //本程式截圖

            //執行螢幕截圖的操作

            Point Var_Loc = this.Location;//取得目前視窗的位置

            richTextBox1.Text += "aaaa : " + Var_Loc.ToString() + "\n";
            richTextBox1.Text += "bbbb : " + this.Location.ToString() + "\n";

            int Frm_left = -Var_Loc.X;
            int Frm_right = -Var_Loc.Y;

            Rectangle rect = new Rectangle();//實例化Rectangle類
            rect = Screen.GetWorkingArea(this);//獲得目前螢幕的大小
            Graphics g1 = this.CreateGraphics();//建立一個以目前螢幕為模板的圖片
            Bitmap bitmap1 = new Bitmap(rect.Width, rect.Height, g1);//建立以螢幕大小為標準的位圖 
            Graphics g2 = Graphics.FromImage(bitmap1);//根據圖片實例化Graphics類

            IntPtr Screen_dc = g1.GetHdc();//得到螢幕的句柄
            IntPtr Bitmap_dc = g2.GetHdc();//得到Bitmap的句柄
            BitBlt(Bitmap_dc, 0, 0, rect.Width, rect.Height, Screen_dc, Frm_left, Frm_right, 13369376);//呼叫此API函數，完成螢幕擷取

            g1.ReleaseHdc(Screen_dc);//釋放掉螢幕的句柄
            g2.ReleaseHdc(Bitmap_dc);//釋放掉Bitmap的句柄

            save_bitmap_file(bitmap1);  // 存檔
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //本程式截圖
            Graphics g1 = this.CreateGraphics();//獲得窗體圖形對象

            Bitmap bitmap1 = new Bitmap(this.ClientRectangle.Width, this.ClientRectangle.Height, g1);

            Graphics g2 = Graphics.FromImage(bitmap1);//創建位圖圖形對象

            IntPtr dc1 = g1.GetHdc();//獲得窗體的上下文設備
            IntPtr dc2 = g2.GetHdc();//獲得位圖文件的上下文設備
            BitBlt(dc2, 0, 0, this.ClientRectangle.Width, this.ClientRectangle.Height, dc1, 0, 0, 13369376);//寫入到位圖

            g1.ReleaseHdc(dc1);//釋放窗體的上下文設備
            g2.ReleaseHdc(dc2);//釋放位圖文件的上下文設備

            save_bitmap_file(bitmap1);  // 存檔
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {


        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        [DllImport("user32.dll", EntryPoint = "GetSystemMetrics")]
        private static extern int GetSystemMetrics(int mVal);

        private void button19_Click(object sender, EventArgs e)
        {
            //參數
            int W = Screen.PrimaryScreen.Bounds.Width;  // 主螢幕寬度
            int H = Screen.PrimaryScreen.Bounds.Height;  // 主螢幕高度
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            Rectangle rect = Screen.GetBounds(Point.Empty);

            richTextBox1.Text += "rect = " + rect.ToString() + "\n";
            richTextBox1.Text += "x = " + Screen.PrimaryScreen.Bounds.X.ToString() + "\n";
            richTextBox1.Text += "y = " + Screen.PrimaryScreen.Bounds.Y.ToString() + "\n";
            richTextBox1.Text += "size = " + Screen.PrimaryScreen.Bounds.Size.ToString() + "\n";

            Rectangle rect2 = new Rectangle();//實例化Rectangle類
            rect2 = Screen.GetWorkingArea(this);//獲得目前螢幕的大小
            richTextBox1.Text += "rect2 : " + rect2.ToString() + "\n";

            return;


            //取得螢幕大小

            richTextBox1.Text += "使用 Screen.PrimaryScreen.Bounds\n";
            W = Screen.PrimaryScreen.Bounds.Width;
            H = Screen.PrimaryScreen.Bounds.Height;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "使用 GetSystemMetrics\n";
            W = GetSystemMetrics(0);
            H = GetSystemMetrics(1);
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //獲取屏幕的分辨率，也就是顯示器屏幕的大小。
            W = SystemInformation.PrimaryMonitorSize.Width;
            H = SystemInformation.PrimaryMonitorSize.Height;

            richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + "\n";

            richTextBox1.Text += "取得桌面大小\n";
            richTextBox1.Text += "桌面寬度 : \t" + Screen.PrimaryScreen.WorkingArea.Width.ToString() + "\n";
            richTextBox1.Text += "桌面高度 : \t" + Screen.PrimaryScreen.WorkingArea.Height.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //取得螢幕解析度資料
            System.Windows.Forms.Screen scr = System.Windows.Forms.Screen.PrimaryScreen;//PrimaryScreen 属性：获取主显示设备
            richTextBox1.Text += "Bounds:\t\t" + scr.Bounds.ToString() + "\n"; //获取屏幕的边界。属性值是一个Rectangle结构的值
            richTextBox1.Text += "DeviceName:\t" + scr.DeviceName.ToString() + "\n"; //获取与显示关联的设备名称
            richTextBox1.Text += "Primary:\t\t" + scr.Primary.ToString() + "\n";   //该值指示某个显示是否为主设备
            richTextBox1.Text += "WorkingArea:\t" + scr.WorkingArea.ToString() + "\n";   //获取显示器的工作区, 属性值是一个Rectangle结构的值
            richTextBox1.Text += "BitsPerPixel:\t" + scr.BitsPerPixel.ToString() + "\n"; //获取与数据的一个像素相关联的内存位数

            //------------------------------------------------------------  # 60個

            //螢幕解析度 與 可工作區域
            //取得螢幕解析度
            int ScreenWidth = Screen.PrimaryScreen.Bounds.Width;
            int ScreenHeight = Screen.PrimaryScreen.Bounds.Height;

            richTextBox1.Text += "螢幕解析度 : " + ScreenWidth.ToString() + " X " + ScreenHeight.ToString() + "\n";

            //取得可工作區域大小
            int WorkingAreaWidth = Screen.PrimaryScreen.WorkingArea.Width;
            int WorkingAreaHeight = Screen.PrimaryScreen.WorkingArea.Height;

            richTextBox1.Text += "可工作區域大小 : " + WorkingAreaWidth.ToString() + " X " + WorkingAreaHeight.ToString() + "\n";

            foreach (Screen screen in System.Windows.Forms.Screen.AllScreens)
            {
                richTextBox1.Text += "Screen " + screen.DeviceName + "\n";
                richTextBox1.Text += "\tPrimary " + screen.Primary + "\n";
                richTextBox1.Text += "\tBounds: " + screen.Bounds + "\n";
                richTextBox1.Text += "\tWorking Area: " + screen.WorkingArea + "\n";
                richTextBox1.Text += "\tBitsPerPixel: " + screen.BitsPerPixel + "\n";
            }

            //------------------------------------------------------------  # 60個

            //螢幕資訊
            richTextBox1.Text += "AllScreens.Length = " + Screen.AllScreens.Length.ToString() + "\n";

            richTextBox1.Text += "W = " + Screen.AllScreens[0].Bounds.Width.ToString() + ", H = " + Screen.AllScreens[0].Bounds.Height.ToString() + "\n";
            richTextBox1.Text += "Bounds = " + Screen.AllScreens[0].Bounds.Size.ToString() + "\n";
            richTextBox1.Text += "Rank = " + Screen.AllScreens.Rank.ToString() + "\n";

            richTextBox1.Text += "DeviceName = " + Screen.PrimaryScreen.DeviceName + "\n";
            richTextBox1.Text += "BitsPerPixel = " + Screen.PrimaryScreen.BitsPerPixel.ToString() + "\n";
            richTextBox1.Text += "Bounds = " + Screen.PrimaryScreen.Bounds.ToString() + "\n";
            richTextBox1.Text += "WorkingArea = " + Screen.PrimaryScreen.WorkingArea.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            Rectangle WorkArea = Screen.GetWorkingArea(this);//屏幕顯示區域
            W = WorkArea.Width; //屏幕寬度
            H = WorkArea.Height; //屏幕高度
            richTextBox1.Text += "W = " + W.ToString() + "\n";
            richTextBox1.Text += "H = " + H.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            // 根據桌面大小調整視窗大小 
            int DeskWidth = Screen.PrimaryScreen.WorkingArea.Width; //PrimaryScreen為取得主顯示器，WorkingArea可取得顯示器的工作區(不包含工作列…等)
            int DeskHeight = Screen.PrimaryScreen.WorkingArea.Height;
            this.Width = Convert.ToInt32(DeskWidth * 0.8);
            this.Height = Convert.ToInt32(DeskHeight * 0.8);

            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.AppendText("螢幕解析度 : " + screenWidth.ToString() + "*" + screenHeight.ToString() + "\n");

            //------------------------------------------------------------  # 60個
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
//                    來源位置             目的位置      要傳輸的區域大小  判斷在像素複製作業中來源色彩如何與目的色彩結合以產生最後的色彩
//g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(w, h), CopyPixelOperation.SourceInvert);
//g.CopyFromScreen(new Point(x_st, y_st), new Point(0, 0), new Size(w, h));
g.CopyFromScreen(new Point(pt.X - w / 2, pt.Y - h / 2), new Point(0, 0), new Size(w, h));

*/

//用Graphics.CopyFromScreen()把屏幕位圖拷貝到該位圖上
//g.CopyFromScreen(0, 0, 0, 0, new Size(W, H));
//public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, Size blockRegionSize);


//參數
//Screen.AllScreens[0].Bounds.Width, Screen.AllScreens[0].Bounds.Height));

