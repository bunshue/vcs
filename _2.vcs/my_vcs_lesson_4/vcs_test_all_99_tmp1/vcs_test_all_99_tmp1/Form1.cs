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
using System.Drawing.Imaging;   //for bmp2jpg
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

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

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
                    richTextBox1.Text += p.ProcessName + "\t\t" + p.StartTime.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
                    //listBox1.Items.Add(string.Format("{0} - {1}", p.ProcessName, p.StartTime.ToString("yyyy/MM/dd HH:mm:ss")));
                }
                else
                    richTextBox1.Text += p.ProcessName + "\t\t" + "xxxxxxxxxxxxxxxx\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
            string fileName1 = "c:\\______test_vcs\\test_ReadAllBytes.bmp";

            byte[] bmp_header = new byte[256];
            FileStream fs1 = new FileStream(fileName1, FileMode.Open);

            richTextBox1.Text += "\nlength = " + fs1.Length.ToString() + "\n";

            fs1.Read(bmp_header, 0, bmp_header.Length);

            for (int i = 0; i < bmp_header.Length; i++)
            {
                richTextBox1.Text += bmp_header[i].ToString("X2");
                if ((i % 16) == 15)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += " ";

            }


            // 關閉檔案。
            fs1.Close();

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
            //依字串長度改變控件大小
            //AutoSizeControl
            int textPadding = 10;   //表示要套用至控制項所有邊緣的填補量
            button18.Text = "012345678901234567890123456789012345";
            Graphics g = button2.CreateGraphics();      //// Create a Graphics object for the Control.
            // Get the Size needed to accommodate the formatted Text.
            Size preferredSize = g.MeasureString(button18.Text, button18.Font).ToSize();
            richTextBox1.Text += "size W = " + preferredSize.Width.ToString() + "\n";
            richTextBox1.Text += "size H = " + preferredSize.Height.ToString() + "\n";
            // Pad the text and resize the control.
            button18.ClientSize = new Size(
                preferredSize.Width + (textPadding * 2),
                preferredSize.Height + (textPadding * 2));
            g.Dispose();    // Clean up the Graphics object.

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

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

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

        private void button34_Click_1(object sender, EventArgs e)
        {


        }

        private void button35_Click_1(object sender, EventArgs e)
        {
            string fileName1 = "c:\\______test_vcs\\test_ReadAllBytes.bmp";
            string fileName2 = "c:\\______test_vcs\\test_WriteAllBytes.bmp";

            //讀取資料
            byte[] data_read = File.ReadAllBytes(fileName1);
            richTextBox1.Text += "讀取檔案" + fileName1 + "\t";
            richTextBox1.Text += "len = " + data_read.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            //修改資料
            for (int i = 54; i < data_read.Length; i++)
            {
                if (data_read[i] == 0xCC)
                    data_read[i] = 0xFF;
            }

            //寫資料
            File.WriteAllBytes(fileName2, data_read);
            richTextBox1.Text += "寫成檔案" + fileName2 + "\n";

        }

        private void button23_Click_1(object sender, EventArgs e)
        {
            int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            MessageBox.Show("螢幕解析度為 " + screenWidth.ToString() + "*" + screenHeight.ToString());

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

        private void button5_Click(object sender, EventArgs e)
        {
        }


        private void button41_Click(object sender, EventArgs e)
        {
            PictureBox pb_new = new PictureBox();
            Button bt_new = new Button();
            this.Controls.Add(pb_new);
            this.Controls.Add(bt_new);
            bt_new.Location = new Point(332, 502);
            bt_new.Size = new Size(154, 42);
            bt_new.BackColor = Color.Red;
            bt_new.Text = "新增控件";
            bt_new.Click += new EventHandler(bt_new_Click);

        }

        private void bt_new_Click(System.Object sender, System.EventArgs e)
        {
            richTextBox1.Text += "你按了這個新控件\n";
        }



    }
}
