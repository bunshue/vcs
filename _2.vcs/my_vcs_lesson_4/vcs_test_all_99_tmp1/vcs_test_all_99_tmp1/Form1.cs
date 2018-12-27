using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;                        //for StreamReader
using System.Diagnostics;               //for process, FileVersionInfo, Stopwatch
using System.Runtime.InteropServices;   //for DllImport
using System.Drawing.Imaging;   //for bmp2jpg ImageFormat
using System.Net;           //for WebClient

namespace vcs_test_all_99_tmp1
{
    public partial class Form1 : Form
    {
        DateTime start_time;
        public Form1()
        {
            InitializeComponent();
            start_time = DateTime.Now;
            toolTip1.SetToolTip(button26, "顯示提示訊息");
        }

        //C# 使用 Stopwatch 测量代码运行时间
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "ST\n";
            sw.Start();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            sw.Stop();
            richTextBox1.Text += "SP\n";
            richTextBox1.Text += "Elapsed milliseconds: " + sw.ElapsedMilliseconds.ToString() + "\n";
            richTextBox1.Text += "Elapsed time: " + sw.Elapsed.ToString() + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            int j = 0;
            for (int i = 0; i < 256; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t" + (char)j + "\n";

            }

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開始計時\n";
            // Create stopwatch
            Stopwatch stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            // Do something
            Application.DoEvents();         //執行某一事件，以達到延遲效果。
            for (int j = 0; j < 123; j++)
                System.Threading.Thread.Sleep(1);

            // Stop timing
            stopwatch.Stop();

            // Write result
            richTextBox1.Text += "停止計時\n";
            richTextBox1.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            // 列出系統中所有的程序
            Process[] processes = Process.GetProcesses();

            richTextBox1.Text += "系統中共有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process p in processes)
            {
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除
                if (!p.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    richTextBox1.Text += p.ProcessName + "\t\t" + p.StartTime.ToString("yyyy/MM/dd hh:mm:ss") + "\n";
                    //listBox1.Items.Add(string.Format("{0} - {1}", p.ProcessName, p.StartTime.ToString("yyyy/MM/dd hh:mm:ss")));
                }
                else
                    richTextBox1.Text += p.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Point now_p = this.Location;
            Random r = new Random();

            for (int i = 0; i < 50; i++)
            {
                Point new_p = new Point(now_p.X + r.Next(-10, 10), now_p.Y + r.Next(-10, 10)); //新的位置
                this.Location = new_p;
                System.Threading.Thread.Sleep(20);
                this.Location = now_p; //還原位置
            }
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

        private void button15_Click(object sender, EventArgs e)
        {
            //C# 產生亂數的方式(Random)
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += "number:" + Rnd.Next(10, 21).ToString() + "\n";
                //Console.WriteLine("number:" + Rnd.Next(10, 21).ToString());
            }

        }

        private void button16_Click(object sender, EventArgs e)
        {

            //只撈一層的所有檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries("c:\\______test_vcs"))
            {
                richTextBox1.Text += fname + "\n";
            }

        }

        private void button17_Click(object sender, EventArgs e)
        {
            //只撈一層的所有.txt檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries("c:\\______test_vcs", "*.txt"))
            {
                richTextBox1.Text += fname + "\n";
            }

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";//將其轉換成GB
            else if (KSize / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";//將其轉換成MB
            else if (KSize / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";//將其轉換成KGB
            else
                return KSize.ToString() + "Byte";//顯示Byte值
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "轉換格式\t將Byte轉換成GB、MB、KB\n";
            richTextBox1.Text += "原本格式： " + double.Parse(textBox1.Text) + "\n";
            richTextBox1.Text += "轉換格式： " + ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
             //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(@"C:\______test_vcs", "*.*", System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            Uri urlCheck = new Uri("http://tw.yahoo.com");
            System.Net.WebRequest request = System.Net.WebRequest.Create(urlCheck);
            System.Net.WebResponse response;
            try
            {
                response = request.GetResponse();
                //Response.Write("OK");
                richTextBox1.Text += "網頁存在\n";
            }
            catch (Exception)
            {
                //Response.Write("Error");
                richTextBox1.Text += "網頁不存在\n";
            }

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //string test_string = "ABC可否開啟檔案總管？";
            string test_string = "如果用MysonLink，就要燒錄mega上放的韌體。";
            string test_string2 = "ABCDE";
            /*
            int j = 0;
            for (int i = 0; i < 256; i++)
            {
                if ((i < 32) || (i > 126))
                    j = '-';
                else
                    j = i;
                richTextBox1.Text += i.ToString() + "\t" + (char)j + "\n";

            }
            */
            for (int i = 0; i < test_string.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + test_string[i] + "\t" + Convert.ToString(((int)test_string[i]), 16) + "\n";
            }
            for (int i = 0; i < test_string2.Length; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + test_string2[i] + "\t" + Convert.ToString(((int)test_string2[i]), 16) + "\n";
            }

        }

        public String GetWebPage(String sURL)
        {
            try
            {
                WebClient wc = new WebClient();
                wc.Headers.Add("user-agent", "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.0.3705; Combat;)");
                byte[] bd = wc.DownloadData(sURL);
                return (Encoding.Default.GetString(bd));
            }
            catch
            {
                return ("fail");
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {
            string strURL = "http://google.com.tw";
            //string strURL = "http://www.yahoo.com.tw";
            string web_data = GetWebPage(strURL);
            if (web_data == "fail")
                richTextBox1.Text += "抓取網頁失敗";
            else
                richTextBox1.Text += "抓取網頁成功";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //抓螢幕某區塊為檔案
            Image image = new Bitmap(410, 410);   //宣告Image類別
            Graphics g = Graphics.FromImage(image);
            g.CopyFromScreen(new Point(340, 255), new Point(0, 0), new Size(410, 410));
            //取得螢幕上x=340 y=255為左上角，長寬為410的區域
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //this.pictureBox1.Image = image;
            image.Save("c:\\aabbcc.jpeg");    //把圖片存起來
            richTextBox1.Text += "已截圖存檔完成\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "加入toolTip物件\n";
            richTextBox1.Text += "在Form1()的InitializeComponent()後加入訊息\n";
        }

        [DllImport("User32.dll")]
        private static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);
        [DllImport("User32.dll")]
        private static extern bool SetForegroundWindow(IntPtr hWnd);
        private const int WS_SHOWNORMAL = 1;

        private void button27_Click(object sender, EventArgs e)
        {
            //C# 指定程序還原與置於前景視窗
            // 取得目前電腦的處理序
            richTextBox1.Text += "找到 " + Process.GetProcesses().Length + " 個程序\n\n";
            foreach (Process pTarget in Process.GetProcesses())
            {
                richTextBox1.Text += pTarget.ProcessName + "\n";
                if (pTarget.ProcessName == "ACDSee32")  // 取得處理序名稱並與指定程序名稱比較
                {
                    //MessageBox.Show("你開啟了ACDSee32");
                    //richTextBox1.Text += pTarget.ProcessName + "\n";
                    HandleRunningInstance(pTarget);
                }
            }
        }
        public static void HandleRunningInstance(Process instance)
        {
            // 相同時透過ShowWindowAsync還原，以及SetForegroundWindow將程式至於前景
            ShowWindowAsync(instance.MainWindowHandle, WS_SHOWNORMAL);
            SetForegroundWindow(instance.MainWindowHandle);
            //Environment.SpecialFolder.
        }

        private void button29_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //建立空白畫布
            Bitmap bmpCanvas = new Bitmap(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);
            //取得畫布的繪圖物件用以繪圖。
            Graphics g = Graphics.FromImage(bmpCanvas);
            g.CopyFromScreen(new Point(0, 0), new Point(0, 0), new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height));
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);
            //將裁切出的矩形存成JPG圖檔。
            Image imgCanvas = (Image)bmpCanvas;
            string str = System.Windows.Forms.Application.StartupPath;
            imgCanvas.Save(str + "\\" + DateTime.Now.ToString("yyyyMMddHHmmss") + ".jpg", ImageFormat.Jpeg);

            richTextBox1.Text += "已截圖存檔完成\n";


        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string fileName1 = "c:\\______test_vcs\\bear.bmp";
            string fileName2 = "c:\\______test_vcs\\bear.bmp.jpg";
            bitmap = new Bitmap(fileName1);
            richTextBox1.Text += "width = " + bitmap.Width.ToString() + "\n";
            richTextBox1.Text += "height = " + bitmap.Height.ToString() + "\n";
            bitmap.Save(fileName2, ImageFormat.Jpeg);
            richTextBox1.Text += fileName1 + " to " +fileName2 + "轉換完成\n";
        }

        private void btn_Click(object sender, EventArgs e)
        {
            if (sender.Equals(btn1))
            {
                richTextBox1.Text += "你按了 1\n";
            }
            else if (sender.Equals(btn2))
            {
                richTextBox1.Text += "你按了 2\n";
            }
            else if (sender.Equals(btn3))
            {
                richTextBox1.Text += "你按了 3\n";
            }
            else if (sender.Equals(btn4))
            {
                richTextBox1.Text += "你按了 4\n";
            }
            else if (sender.Equals(btn5))
            {
                richTextBox1.Text += "你按了 5\n";
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void richTextBox1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = "目前滑鼠位置：" + e.X + " : " + e.Y;

        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Up：" + e.X + " : " + e.Y;

        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "Mouse Down：" + e.X + " : " + e.Y;
        }

        DateTime LoginTime;
        DateTime LogoffTime;
        TimeSpan StayTime = new TimeSpan();
        private void button10_Click_1(object sender, EventArgs e)
        {
            LoginTime = DateTime.Now; //取得目前登入的時間
            richTextBox1.Text +="登入時間： " + LoginTime + "\n";

        }

        private void button9_Click_1(object sender, EventArgs e)
        {
            LogoffTime = DateTime.Now;
            richTextBox1.Text += "登入時間： " + LogoffTime + "\n";
            StayTime = LogoffTime.Subtract(LoginTime);
            richTextBox1.Text += "您在此停留了" + StayTime.Hours + "小時" + StayTime.Minutes + "分鐘" + StayTime.Seconds + "秒\n";
        }

        private void button34_Click_1(object sender, EventArgs e)
        {


        }

        private void button35_Click_1(object sender, EventArgs e)
        {
            //[C#] 產生一組亂數
            //最後產生的finalString就是我們要的亂數,至於亂數長度,你可以調整第二行中8這個數字,如果沒改就是長度8的亂數.

            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            var stringChars = new char[8];
            var random = new Random();
            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[random.Next(chars.Length)];
            }
            var finalString = new String(stringChars);
            richTextBox1.Text += "產生8位數亂數：" + finalString + "\n";
        }

        private void button23_Click_1(object sender, EventArgs e)
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            MessageBox.Show("螢幕解析度為 " + screenWidth.ToString() + "*" + screenHeight.ToString());

        }

        private void button29_Click_1(object sender, EventArgs e)
        {
            //[c#] 取得src內的網址
            string s = "<img src=\"http://www.yahoo.com.tw/1.gif\"/>";
            System.Text.RegularExpressions.Match m = System.Text.RegularExpressions.Regex.Match(s, "\"(.*?)\"");
            string res = m.Groups[1].Value;
            richTextBox1.Text += res;

        }

        private void button32_Click_1(object sender, EventArgs e)
        {
            richTextBox1.Text += "Machine: " + Environment.MachineName + "\n";
            richTextBox1.Text += "# of processors (logical): " + Environment.ProcessorCount + "\n";
            //richTextBox1.Text += "# of processors (physical): " + CountPhysicalProcessors() + "\n";
            //richTextBox1.Text += "RAM installed:   bytes" + CountPhysicalMemory() + "\n";
            richTextBox1.Text += "Is OS 64-bit? " + Environment.Is64BitOperatingSystem + "\n";
            richTextBox1.Text += "Is process 64-bit? " + Environment.Is64BitProcess + "\n";
            richTextBox1.Text += "Little-endian: " + BitConverter.IsLittleEndian + "\n";
            foreach (Screen screen in System.Windows.Forms.Screen.AllScreens)
            {
                richTextBox1.Text += "Screen " + screen.DeviceName + "\n";
                richTextBox1.Text += "\tPrimary " + screen.Primary + "\n";
                richTextBox1.Text += "\tBounds: " + screen.Bounds + "\n";
                richTextBox1.Text += "\tWorking Area: " + screen.WorkingArea + "\n";
                richTextBox1.Text += "\tBitsPerPixel: " + screen.BitsPerPixel + "\n";
            }

        }

        private void button21_Click_1(object sender, EventArgs e)
        {
            var pathstr = "C://______test_vcs";
            if (Directory.Exists(pathstr))
            {
                //var strname=DateTime.Now.ToShortDateString().Replace("/","-")+".txt";
                var dt = DateTime.Now;
                DirectoryInfo pathinfo = new DirectoryInfo(pathstr);
                foreach (DirectoryInfo paths in pathinfo.GetDirectories())
                {
                    //File.AppendAllText("E:\\Time\\新建文檔夾 (2)"+"/"+strname,DateTime.Now+"\r\n");
                    if (paths.CreationTime < Convert.ToDateTime(dt.AddDays(-(dt.Day) + 1)))
                    {
                        //paths.Delete();
                        richTextBox1.Text += "path = " + paths + "\n";
                    }
                }
            }
            else
                richTextBox1.Text += "資料夾 " + pathstr + " 不存在\n";

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button40_Click(object sender, EventArgs e)
        {
            //Form.Controls 屬性是用來取得這張Form的控制項
            //Controls.GetType 是取得這個控制項的類別名稱

            for (int i = 0; i < this.Controls.Count; i++)
            {
                richTextBox1.Text += "Name: " + this.Controls[i].Name + "\t";
                richTextBox1.Text += "Text: " + this.Controls[i].Text + "\t";
                richTextBox1.Text += "這項是：" + this.Controls[i].GetType() + "\n";


                if (this.Controls[i] is Button)
                {
                    richTextBox1.Text += "這是Button" + "\n";
                }

            }

        }

        private void button39_Click(object sender, EventArgs e)
        {
            //列舉控制項
            int i = 1;
            foreach (Control ctrl in this.Controls)
            {
                //取出控制項的類型
                string TypeName = ctrl.GetType().Name;
                //類型若是Label
                if (TypeName == "Button")
                {
                    ctrl.Name = "test" + i.ToString();
                    richTextBox1.Text += ctrl.Name + "\n";
                    i++;
                }
            }

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo("c:\\______test_vcs");
            if (!dir.Exists)
            {
                dir = new DirectoryInfo("c:\\______test_vcs");
            }
            FileInfo[] files = dir.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in files)
            {
                richTextBox1.Text += "get file : " + file.Name + "\n";
            }

        }

        private void nudgeWindow()
        {
            // 記錄視窗舊位置
            int oldLeft = Left;
            int oldTop = Top;
            // 變動位置
            Random r = new Random();
            for (int i = 0; i <= 500; i++)
            {
                int left = r.Next(Left - 20, Left + 20);
                Left = left;
                int top = r.Next(Top - 20, Top + 20);
                Top = top;
                Left = oldLeft;
                Top = oldTop;
            }
        }

        private void button36_Click_1(object sender, EventArgs e)
        {
            nudgeWindow();
        }

        private void button11_Click_1(object sender, EventArgs e)
        {

        }

        DateTime doubleClickTimer;

        private void richTextBox1_DoubleClick(object sender, EventArgs e)
        {
            doubleClickTimer = DateTime.Now; //記下DoubleClick的時間
        }

        private void richTextBox1_Click(object sender, EventArgs e)
        {
            TimeSpan t = (TimeSpan)(DateTime.Now - doubleClickTimer); //DoubleClick後又點了一下, 計算時間差

            if (t.TotalMilliseconds <= 200) //如果小於200豪秒就全選
                richTextBox1.SelectAll();
        }

    }
}
