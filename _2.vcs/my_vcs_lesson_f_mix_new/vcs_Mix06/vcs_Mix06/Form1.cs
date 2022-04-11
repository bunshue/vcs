using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.Collections;   //for Stack

//參考/加入參考 /COM/Microsoft Shell Controls and Automation
using Shell32;  //for Shell


namespace vcs_Mix06
{
    public partial class Form1 : Form
    {
        string ffmpeg = @"C:\______test_files\_exe\ffmpeg\ffmpeg.exe";

        [DllImport("user32.dll")]
        public static extern bool GetCursorPos(out POINT lpPoint);

        [StructLayout(LayoutKind.Sequential)]
        public struct POINT
        {
            public int X;
            public int Y;
            public POINT(int x, int y)
            {
                this.X = x;
                this.Y = y;
            }
        }

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
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 185;
            dy = 85;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            button24.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 11);

            label1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 10);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            int w = 0;
            int h = 0;

            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            w = this.ClientSize.Width - richTextBox1.Location.X - 10;   //border : 10
            h = this.ClientSize.Height - richTextBox1.Location.Y - 10;   //border : 10
            richTextBox1.Size = new Size(w, h);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_exit_setup();
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            int[] rs = new int[10];
            for (int i = 0; i < 10; i++)
                rs[i] = GetRandom1();

            richTextBox1.Text += "方法一, 取得亂數 : ";
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";

            }
            richTextBox1.Text += "\t大部分都一樣\n";


            for (int i = 0; i < 10; i++)
                rs[i] = GetRandom2();

            richTextBox1.Text += "方法二, 取得亂數 : ";
            for (int i = 0; i < 10; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";

            }
            richTextBox1.Text += "\t可取得亂數\n";
        }

        private int GetRandom1()
        {
            Random r = new Random();
            return r.Next(0, 1000);
        }

        //定義一個自增的數字作為種子
        private static int _RandomSeed = (int)DateTime.Now.Ticks;
        private int GetRandom2()
        {
            if (_RandomSeed == int.MaxValue)
                _RandomSeed = 1;

            Random r = new Random(_RandomSeed++);
            return r.Next(0, 1000);
        }


        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //調用系統IPCONFIG獲取本機局域網IP以及其他相關信息

            string result = GetIPConfigReturns();
            richTextBox1.Text += "  " + result + "\n";

        }

        /// <summary> 
        /// 獲取IPCONFIG返回值 
        /// </summary> 
        /// <returns>返回 IPCONFIG輸出</returns> 
        public static string GetIPConfigReturns()
        {
            string version = Environment.OSVersion.VersionString;

            if (version.Contains("Windows"))
            {
                //調用ipconfig ,並傳入參數: /all 
                ProcessStartInfo psi = new ProcessStartInfo("ipconfig", "/all");

                psi.CreateNoWindow = true; //若為false，則會出現cmd的黑窗體 
                psi.RedirectStandardOutput = true;
                psi.UseShellExecute = false;

                Process p = Process.Start(psi);

                return p.StandardOutput.ReadToEnd();
            }

            return string.Empty;
        }


        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int len = 20;
            string random_pattern = CreateAndCheckCode(random, len);

            richTextBox1.Text += "取得random字串 : \t" + random_pattern + "\n";
        }

        Random random = new Random(~unchecked((int)DateTime.Now.Ticks));
        private string CreateAndCheckCode(Random random, int length) // code 激活碼前綴
        {
            //char[] Pattern = new char[] { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' };
            char[] Pattern = new char[] { '1', '2', '3', 'A', 'B', 'C' };
            string result = string.Empty;
            int n = Pattern.Length;
            for (int i = 0; i < length; i++)
            {
                int rnd = random.Next(0, n);
                result += Pattern[rnd];
            }
            return result;
        }

        //#制作閃動的窗體
        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            while (Visible) // 關閉窗體時，停止循環
            {
                for (int c = 0; c < 254 && Visible; c++)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c); // 此方法指定三個數字：red/green/blue.
                    Application.DoEvents(); // 此語句使操作系統能夠在程序之外執行其他操作。否則
                    // 程序將占用所有CPU周期
                    Thread.Sleep(3); // 此語句在循環中插入3毫秒的延遲。
                }
                for (int c = 254; c >= 0 && Visible; c--)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c);
                    Application.DoEvents();
                    Thread.Sleep(3);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


            string expr = "3*5*8/7";


            NEval neval = new NEval();


            double result = neval.Eval(expr);
            richTextBox1.Text += result.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //計算兩個日期的時間間隔
            //計算兩個日期的時間間隔
            DateTime dt2 = new DateTime(1974, 9, 24);
            DateTime dt1 = new DateTime(1999, 3, 8);
            string diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";
        }

        /// <summary>
        /// 計算兩個日期的時間間隔
        /// </summary>
        /// <param name="DateTime1">第一個日期和時間</param>
        /// <param name="DateTime2">第二個日期和時間</param>
        /// <returns></returns>
        private string DateDiff(DateTime DateTime1, DateTime DateTime2)
        {
            string dateDiff = null;
            TimeSpan ts1 = new TimeSpan(DateTime1.Ticks);
            TimeSpan ts2 = new TimeSpan(DateTime2.Ticks);
            TimeSpan ts = ts1.Subtract(ts2).Duration();
            dateDiff = ts.Days.ToString() + "天"
                + ts.Hours.ToString() + "小時"
                + ts.Minutes.ToString() + "分鐘"
                + ts.Seconds.ToString() + "秒";
            return dateDiff;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //字符型轉換 轉為字符串

            int value = 12345;
            richTextBox1.Text += "a\t" + value.ToString("n") + "\n"; //生成 12,345.00
            richTextBox1.Text += "b\t" + value.ToString("C") + "\n"; //生成 ￥12,345.00
            richTextBox1.Text += "c\t" + value.ToString("e") + "\n"; //生成 1.234500e+004
            richTextBox1.Text += "d\t" + value.ToString("f4") + "\n"; //生成 12345.0000
            richTextBox1.Text += "e\t" + value.ToString("x") + "\n"; //生成 3039 (16進制)
            richTextBox1.Text += "f\t" + value.ToString("p") + "\n"; //生成 1,234,500.00%
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            long seconds = DateTime.Now.Ticks / TimeSpan.TicksPerSecond;

            richTextBox1.Text += "現在時間用Ticks表示 : " + DateTime.Now.Ticks.ToString() + "\n";
            richTextBox1.Text += "每秒有幾個Ticks : " + TimeSpan.TicksPerSecond.ToString() + "\n";
            richTextBox1.Text += "現在時間用秒表示 : " + seconds.ToString() + "\n";



        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string filename = @"D:\vcs\_烏龍派出所\_烏龍派出所151~200\烏龍派出所181(日語).mp4";
            CatchImg(filename);
        }

        /// <summary>
        /// @從視頻文件截圖,生成在視頻文件所在文件夾
        /// 在Web.Config 中需要兩個前置配置項:
        /// 1.ffmpeg.exe文件的路徑
        /// <add key="ffmpeg" value="E:\ffmpeg\ffmpeg.exe" />
        /// 2.截圖的尺寸大小
        /// <add key="CatchFlvImgSize" value="240x180" />
        /// 3.視頻處理程序ffmpeg.exe
        /// </summary>
        /// <param name="vFileName">視頻文件地址,如:/Web/FlvFile/User1/00001.Flv</param>
        /// <returns>成功:返回圖片虛擬地址; 失敗:返回空字符串</returns>

        public string CatchImg(string vFileName)
        {
            if ((!File.Exists(ffmpeg)) || (!File.Exists(vFileName)))
            {
                return "";
            }

            //獲得圖片相對路徑/最後存儲到數據庫的路徑,如:/Web/FlvFile/User1/00001.jpg
            string flv_img = Path.ChangeExtension(vFileName, ".jpg");

            //圖片絕對路徑,如:D:\Video\Web\FlvFile\User1\0001.jpg
            //string flv_img_p = HttpContext.Current.Server.MapPath(flv_img);
            string flv_img_p = "aaaaaa.jpg";

            //截圖的尺寸大小,配置在Web.Config中,如:<add key="CatchFlvImgSize" value="240x180" />
            //string FlvImgSize = System.Configuration.ConfigurationSettings.APPSettings["CatchFlvImgSize"];

            ProcessStartInfo startInfo = new ProcessStartInfo(ffmpeg);
            startInfo.WindowStyle = ProcessWindowStyle.Hidden;

            //此處組合成ffmpeg.exe文件需要的參數即可,此處命令在ffmpeg 0.4.9調試通過
            //startInfo.Arguments = " -i " + vFileName + " -y -f image2 -t 0.001 -s " + FlvImgSize + " " + flv_img_p ;
            //startInfo.Arguments = " -i " + vFileName + " -y -f image2 -t 0.001 -s " + "960x540" + " " + flv_img_p;
            startInfo.Arguments = " -i " + vFileName + " -y -f image2 -t 0.001 -s " + "960x480" + " " + flv_img_p;

            try
            {
                Process.Start(startInfo);
            }
            catch
            {
                return "";
            }

            ///注意:圖片截取成功後,數據由內存緩存寫到磁盤需要時間較長,大概在3,4秒甚至更長;
            ///這兒需要延時後再檢測,我服務器延時8秒,即如果超過8秒圖片仍不存在,認為截圖失敗;
            ///此處略去延時代碼.如有那位知道如何捕捉ffmpeg.exe截圖失敗消息,請告知,先謝過!
            if (File.Exists(flv_img_p))
            {
                return flv_img;
            }

            return "";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            richTextBox1.Text += "音樂長度\n";
            string[] result = GetMP3Time(filename);
            foreach (string str in result)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";
        }


        /// <summary>  
        /// 获得音乐长度  
        /// </summary>  
        /// <param name="filePath">文件的完整路径  
        public static string[] GetMP3Time(string filePath)
        {
            string dirName = Path.GetDirectoryName(filePath);
            string SongName = Path.GetFileName(filePath);//获得歌曲名称             
            Shell sh = new Shell();
            Folder dir = sh.NameSpace(dirName);
            FolderItem item = dir.ParseName(SongName);
            string SongTime = dir.GetDetailsOf(item, 27);//27为获得歌曲持续时间 ，28为获得音乐速率，1为获得音乐文件大小      
            string[] time = Regex.Split(SongTime, ":");
            return time;
        }

        /// <summary>  
        /// 转换函数  
        /// </summary>  
        /// <param name="exe">ffmpeg程序  
        /// <param name="arg">执行参数       
        public static void ExcuteProcess(string exe, string arg)
        {
            using (var p = new Process())
            {
                p.StartInfo.FileName = exe;
                p.StartInfo.Arguments = arg;
                p.StartInfo.UseShellExecute = false;    //输出信息重定向  
                p.StartInfo.CreateNoWindow = true;
                p.StartInfo.RedirectStandardError = true;
                p.StartInfo.RedirectStandardOutput = true;
                p.Start();                    //启动线程  
                p.BeginOutputReadLine();
                p.BeginErrorReadLine();
                p.WaitForExit();//等待进程结束                                        
            }
        }



        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string fromMusic = @"C:\______test_files\_mp3\16.監獄風雲.mp3";
            string toMusic = @"C:\______test_files\_mp3\ccccc.mp3";

            int bitrate = Convert.ToInt32(10) * 1000;//恒定码率  
            int Hz = 3000;//采样频率  

            try
            {
                ExcuteProcess(ffmpeg, "-y -ab " + bitrate + " -ar " + Hz.ToString() + " -i \"" + fromMusic + "\" \"" + toMusic + "\"");

                richTextBox1.Text += "-y -ab " + bitrate + " -ar " + Hz.ToString() + " -i \"" + fromMusic + "\" \"" + toMusic + "\"";

                //转换完成  
                MessageBox.Show("转换完成");
            }
            catch (Exception ex)
            { MessageBox.Show(ex.ToString()); }

            string fromPath = fromMusic;//要切割音乐的物理路径  

            /*
            string startTime = string.Format("0:{0}:{1}", txtBeginM.Text, txtBeginS.Text).Trim();//歌曲起始时间  
            int duration = (Convert.ToInt32(this.txtEndM.Text) * 60 + Convert.ToInt32(this.txtEndS.Text)) - (Convert.ToInt32(this.txtBeginM.Text) * 60 + Convert.ToInt32(this.txtBeginS.Text));
            string endTime = string.Format("0:{0}:{1}", duration / 60, duration % 60);//endTime是持续的时间，不是歌曲结束的时间  
            */

            string startTime = "0:0:0";
            string endTime = "0:1:0";

            string savePath = toMusic;//切割后音乐保存的物理路径  
            try
            {
                ExcuteProcess(ffmpeg, "-y -i \"" + fromPath + "\" -ss " + startTime + " -t " + endTime + " -acodec copy \"" + savePath + "\"");//-acodec copy表示歌曲的码率和采样频率均与前者相同  
                MessageBox.Show("已切割完成");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.ToString());
            }


        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //顯示Loading窗體
            LoadingControl pLoading = LoadingControl.getLoading();
            pLoading.SetExecuteMethod(method);
            pLoading.ShowDialog();
        }

        private void method()
        {
            LoadingControl pLoading = LoadingControl.getLoading();
            for (int i = 0; i < 10; i++)
            {
                pLoading.SetCaptionAndDescription("", "", "執行進度" + i.ToString() + "/10");

                //XXXXXXX

                Thread.Sleep(200);
            }
            LoadingControl.getLoading().CloseLoadingForm();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取文件MD5值
            string result = string.Empty;
            string filename = @"C:\______test_files\picture1.jpg";

            result = GetMD5HashFromFile(filename);
            richTextBox1.Text += result + "\n";


        }

        /// <summary>
        /// 獲取文件MD5值
        /// </summary>
        /// <param name="fileName">文件絕對路徑</param>
        /// <returns>MD5值</returns>
        public static string GetMD5HashFromFile(string fileName)
        {
            try
            {
                FileStream file = new FileStream(fileName, FileMode.Open);
                System.Security.Cryptography.MD5 md5 = new System.Security.Cryptography.MD5CryptoServiceProvider();
                byte[] retVal = md5.ComputeHash(file);
                file.Close();

                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < retVal.Length; i++)
                {
                    sb.Append(retVal[i].ToString("x2"));
                }
                return sb.ToString();
            }
            catch (Exception ex)
            {
                throw new Exception("GetMD5HashFromFile() fail,error:" + ex.Message);
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            /// 利用C#來解讀MP3文件的TAG區信息。
            //string mp3_filename = @"C:\______test_files\_mp3\aaaa.mp3";

            // TBD

        }

        public class Classmate  //事件訂閱者
        {
            private string name;
            public Classmate(string Name)
            {
                name = Name;
            }
            public void SendResponse()  //事件處理函數，要與自定義委托類型匹配
            {
                Console.WriteLine("來自：" + this.name + "的回復: 已經收到邀請，隨時可以開始！");
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //c
            Classmate classmate1 = new Classmate("Alice");
            Classmate classmate2 = new Classmate("Banana");
            Classmate classmate3 = new Classmate("Cherry");
            Classmate classmate4 = new Classmate("Daisy");

            classmate1.SendResponse();
            classmate2.SendResponse();
            classmate3.SendResponse();
            classmate4.SendResponse();


        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取屏幕的分辨率，也就是顯示器屏幕的大小。
            int W = SystemInformation.PrimaryMonitorSize.Width;
            int H = SystemInformation.PrimaryMonitorSize.Height;

            richTextBox1.Text += "W = " + W.ToString() + " H = " + H.ToString() + "\n";

            richTextBox1.Text += "取得桌面大小\n";
            richTextBox1.Text += "桌面寬度 : \t" + Screen.PrimaryScreen.WorkingArea.Width.ToString() + "\n";
            richTextBox1.Text += "桌面高度 : \t" + Screen.PrimaryScreen.WorkingArea.Height.ToString() + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //星期幾
            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            richTextBox1.Text += week + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //從windows剪貼板獲取內容
            IDataObject iData = Clipboard.GetDataObject();
            if (iData.GetDataPresent(DataFormats.Text))
            {
                richTextBox1.Text += "取得文字:\n";
                Console.WriteLine((String)iData.GetData(DataFormats.Text));
            }
            if (iData.GetDataPresent(DataFormats.Bitmap))
            {
                richTextBox1.Text += "取得圖片\n";
                Image img = (Bitmap)iData.GetData(DataFormats.Bitmap);
                //pictureBox1.Image = img;
            }
        }

        public class Person
        {
            public string Name { get; set; }
            public int Age { get; set; }
            public int Weight { get; set; }
            public int Height { get; set; }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //class 範例 2

            Person p = new Person() { Name = "Hong", Age = 25, Weight = 65, Height = 170 };

        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取計算機磁盤空間
            //在System.IO命名空間下的DriveInfo類的GetDrives()方法可以用來獲得計算機上的所有邏輯驅動器的名稱。DriveInfo類的TotalSize屬性可義獲得磁盤的空間大小。
            System.IO.DriveInfo[] drive = System.IO.DriveInfo.GetDrives();
            for (int i = 0; i < drive.Length; i++)
            {
                richTextBox1.Text += "取得磁碟 : " + drive[i].Name;

                if (drive[i].IsReady == true)
                {
                    richTextBox1.Text += "\t空間 : " + Convert.ToString(drive[i].TotalSize / 1024 / 1024 / 1024) + "GB\n";
                }
                else
                {
                    richTextBox1.Text += "\n";
                }

            }




        }

        public class Shoe
        {
            public string Color;
        }

        public class Dude
        {
            public string Name;
            public Shoe RightShoe;
            public Shoe LeftShoe;

            public Dude CopyDude()
            {
                Dude newPerson = new Dude();
                newPerson.Name = Name;
                newPerson.LeftShoe = LeftShoe;
                newPerson.RightShoe = RightShoe;

                return newPerson;
            }

            public override string ToString()
            {
                return (Name + " : Dude!, I have a " + RightShoe.Color + " shoe on my right foot, and a " + LeftShoe.Color + " on my left foot.");
            }
        }


        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //class 範例 3

            Dude Bill = new Dude();
            Bill.Name = "Bill";
            Bill.LeftShoe = new Shoe();
            Bill.RightShoe = new Shoe();
            Bill.LeftShoe.Color = "Blue";
            Bill.RightShoe.Color = "Blue";

            Dude Ted = Bill.CopyDude();
            Ted.Name = "Ted";
            Ted.LeftShoe.Color = "Red";
            Ted.RightShoe.Color = "Red";

            richTextBox1.Text += "Bill\n" + Bill.ToString() + "\n";
            richTextBox1.Text += "Ted\n" + Ted.ToString() + "\n";


        }

        public class People
        {
            private string Id;
            private string Name;
            private string Address;
        }        

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //class 範例 4
            DataTable dt = new DataTable();
            dt.Columns.Add("Id", typeof(string));
            dt.Columns.Add("Name", typeof(string));
            dt.Columns.Add("Address", typeof(string));
            dt.PrimaryKey = new DataColumn[] { dt.Columns[0] };

            dt.Rows.Add("0001", "張三", "武漢市");
            dt.Rows.Add("0002", "李四", "北京市");
            dt.AcceptChanges();
            dt.Rows.Add("0003", "王五", "深圳市");

            //List<People> allPeople = new List<People>();
            //List<People> allPeople = new List<People>();


            /*
            List<People> allPeople = new List<People>()
            {
              new People(){ Id="0001", Name="張三", Address ="武漢市"},
              new People(){ Id="0002", Name="李四", Address ="北京市"},
              new People(){ Id="0003", Name="王五", Address ="深圳市"}
            };
            */

        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //統計英文文本中的單詞數並排序
            //統計英文文本中的單詞數並排序

            string filename = @"C:\______test_files\__RW\_txt\english_text.txt";
            StatisticsWords(filename);
        }

        public void StatisticsWords(string path)
        {
            if (!File.Exists(path))
            {
                Console.WriteLine("文件不存在！");
                return;
            }
            Hashtable ht = new Hashtable(StringComparer.OrdinalIgnoreCase);
            StreamReader sr = new StreamReader(path, System.Text.Encoding.UTF8);
            string line = sr.ReadLine();

            string[] wordArr = null;
            int num = 0;
            while (line.Length > 0)
            {
                //   MatchCollection mc =  Regex.Matches(line, @"\b[a-z]+", RegexOptions.Compiled | RegexOptions.IgnoreCase);
                //foreach (Match m in mc)
                //{
                //    if (ht.ContainsKey(m.Value))
                //    {
                //        num = Convert.ToInt32(ht[m.Value]) + 1;
                //        ht[m.Value] = num;
                //    }
                //    else
                //    {
                //        ht.Add(m.Value, 1);
                //    }
                //}
                //line = sr.ReadLine();

                wordArr = line.Split(' ');
                foreach (string s in wordArr)
                {
                    if (s.Length == 0)
                        continue;
                    //去除標點
                    line = Regex.Replace(line, @"[\p{P}*]", "", RegexOptions.Compiled);
                    //將單詞加入哈希表
                    if (ht.ContainsKey(s))
                    {
                        num = Convert.ToInt32(ht[s]) + 1;
                        ht[s] = num;
                    }
                    else
                    {
                        ht.Add(s, 1);
                    }
                }
                line = sr.ReadLine();
            }

            ArrayList keysList = new ArrayList(ht.Keys);
            //對Hashtable中的Keys按字母序排列
            keysList.Sort();
            //按次數進行插入排序【穩定排序】，所以相同次數的單詞依舊是字母序
            string tmp = String.Empty;
            int valueTmp = 0;
            for (int i = 1; i < keysList.Count; i++)
            {
                tmp = keysList[i].ToString();
                valueTmp = (int)ht[keysList[i]];//次數
                int j = i;
                while (j > 0 && valueTmp > (int)ht[keysList[j - 1]])
                {
                    keysList[j] = keysList[j - 1];
                    j--;
                }
                keysList[j] = tmp;//j=0
            }
            //打印出來
            foreach (object item in keysList)
            {
                //Console.WriteLine((string)item + ":" + (string)ht[item]);
                Console.WriteLine(item.ToString() + ":" + ht[item].ToString());
            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            DateTime dt = DateTime.Now;

            string filename = String.Format("{0}-{1}-{2}_{3}-{4}-{5}",
                                            dt.Year, dt.Month, dt.Day,
                                            dt.Hour, dt.Minute,
                                            dt.Second);

            richTextBox1.Text += filename + "\n";


            richTextBox1.Text += DateTime.Now.Ticks.ToString() + "\n";


            richTextBox1.Text += Environment.NewLine + "Conversion finished @ " + DateTime.Now.ToString();


        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //MD5驗證  32 位元

            string data = "hello world";
            string key = "123";
            string result = Md5Sum(data + key);  // 返回
            richTextBox1.Text += result + "\n";

        }


        public static string Md5Sum(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            System.Security.Cryptography.MD5 md5;
            md5 = System.Security.Cryptography.MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += System.Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //抓取網頁資料 1
            string url = @"http://140.129.118.16/~richwang/";

            string rl;
            WebRequest Request = WebRequest.Create(url.Trim());

            WebResponse Response = Request.GetResponse();

            Stream resStream = Response.GetResponseStream();

            StreamReader sr = new StreamReader(resStream, Encoding.Default);
            StringBuilder sb = new StringBuilder();
            while ((rl = sr.ReadLine()) != null)
            {
                sb.Append(rl);
            }

            richTextBox1.Text += sb + "\n";

            richTextBox1.Text += "完成\n";
        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //抓取網頁資料 2
            WebClient wc = new WebClient();
            wc.Encoding = Encoding.UTF8;
            string html = wc.DownloadString("http://www.lagou.com/");

            richTextBox1.Text += html + "\n";
        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button30_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button31_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button32_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button33_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button34_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button35_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            POINT pt = new POINT();
            GetCursorPos(out pt);
            //label1.Text = "滑鼠位置 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")";    same
            label1.Text = "滑鼠位置 : (" + string.Format("X:{0}, Y:{1}", pt.X, pt.Y) + ")";
        }
    }

    /// <summary>
    /// 表達式計算類。支持數學函數，支持函數嵌套
    /// 作者watsonyin
    /// 開發日期：2010年10月 版本1.0
    /// </summary>
    public class NEval
    {
        public NEval()
        {

        }

        public double Eval(string expr)
        {
            try
            {
                string tmpexpr = expr.ToLower().Trim().Replace(" ", string.Empty);
                return Calc_Internal(tmpexpr);
            }
            catch (ExpressionException eex)
            {
                throw eex;
            }
            catch
            {
                throw new Exception("表達式錯誤");
            }
        }

        private Random m_Random = null;
        private double Calc_Internal(string expr)
        {
            /*
             * 1.    初始化一个空堆栈 
             * 2.    从左到右读入后缀表达式 
             * 3.    如果字符是一个操作数，把它压入堆栈。 
             * 4.    如果字符是个操作符，弹出两个操作数，执行恰当操作，然后把结果压入堆栈。如果您不能够弹出两个操作数，后缀表达式的语法就不正确。 
             * 5.    到后缀表达式末尾，从堆栈中弹出结果。若后缀表达式格式正确，那么堆栈应该为空。
            */

            Stack post2 = ConvertExprBack(expr);
            Stack post = new Stack();
            while (post2.Count > 0)
                post.Push(post2.Pop());

            Stack stack = new Stack();
            while (post.Count > 0)
            {
                string tmpstr = post.Pop().ToString();
                char c = tmpstr[0];
                LetterType lt = JudgeLetterType(tmpstr);
                if (lt == LetterType.Number)
                {
                    stack.Push(tmpstr);
                }
                else if (lt == LetterType.SimpleOperator)
                {
                    double d1 = double.Parse(stack.Pop().ToString());
                    double d2 = double.Parse(stack.Pop().ToString());
                    double r = 0;
                    if (c == '+')
                        r = d2 + d1;
                    else if (c == '-')
                        r = d2 - d1;
                    else if (c == '*')
                        r = d2 * d1;
                    else if (c == '/')
                        r = d2 / d1;
                    else if (c == '^')
                        r = Math.Pow(d2, d1);
                    else
                        throw new Exception("不支持操作符:" + c.ToString());
                    stack.Push(r);
                }
                else if (lt == LetterType.Function)  //如果是函数
                {
                    string[] p;
                    double d = 0;
                    double d1 = 0;
                    double d2 = 0;
                    int tmpos = tmpstr.IndexOf('(');
                    string funcName = tmpstr.Substring(0, tmpos);
                    switch (funcName)
                    {
                        case "asin":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Asin(d).ToString());
                            break;
                        case "acos":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Acos(d).ToString());
                            break;
                        case "atan":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Atan(d).ToString());
                            break;
                        case "acot":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((1 / Math.Atan(d)).ToString());
                            break;
                        case "sin":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Sin(d).ToString());
                            break;
                        case "cos":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Cos(d).ToString());
                            break;
                        case "tan":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Tan(d).ToString());
                            break;
                        case "cot":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((1 / Math.Tan(d)).ToString());
                            break;
                        case "log":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Log(d1, d2).ToString());
                            break;
                        case "ln":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Log(d, Math.E).ToString());
                            break;
                        case "abs":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Abs(d).ToString());
                            break;
                        case "round":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Round(d1, (int)d2).ToString());
                            break;
                        case "int":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((int)d);
                            break;
                        case "trunc":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Truncate(d).ToString());
                            break;
                        case "floor":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Floor(d).ToString());
                            break;
                        case "ceil":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Ceiling(d).ToString());
                            break;
                        case "random":
                            if (m_Random == null)
                                m_Random = new Random();
                            d = m_Random.NextDouble();
                            stack.Push(d.ToString());
                            break;
                        case "exp":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Exp(d).ToString());
                            break;
                        case "pow":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Pow(d1, d2).ToString());
                            break;
                        case "sqrt":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Sqrt(d).ToString());
                            break;
                        default:
                            throw new Exception("未定义的函数：" + funcName);

                    }

                }
            }
            object obj = stack.Pop();
            return double.Parse(obj.ToString());
        }

        /// <summary>
        /// 将函数括号内的字符串进行分割，获得参数列表，如果参数是嵌套的函数，用递归法计算得到它的值
        /// </summary>
        /// <param name="funcstr"></param>
        /// <param name="paramCount"></param>
        /// <param name="parameters"></param>
        private void SplitFuncStr(string funcstr, int paramCount, out string[] parameters)
        {
            parameters = new string[paramCount];
            int tmpPos = funcstr.IndexOf('(', 0);
            string str = funcstr.Substring(tmpPos + 1, funcstr.Length - tmpPos - 2);
            if (paramCount == 1)
            {
                parameters[0] = str;
            }
            else
            {
                int cpnum = 0;
                int startPos = 0;
                int paramIndex = 0;
                for (int i = 0; i <= str.Length - 1; i++)
                {
                    if (str[i] == '(')
                        cpnum++;
                    else if (str[i] == ')')
                        cpnum--;
                    else if (str[i] == ',')
                    {
                        if (cpnum == 0)
                        {
                            string tmpstr = str.Substring(startPos, i - startPos);
                            parameters[paramIndex] = tmpstr;
                            paramIndex++;
                            startPos = i + 1;
                        }
                    }
                }
                if (startPos < str.Length)
                {
                    string tmpstr = str.Substring(startPos);
                    parameters[paramIndex] = tmpstr;
                }
            }

            //如果参数是函数， 进一步采用递归的方法生成函数值
            for (int i = 0; i <= paramCount - 1; i++)
            {
                double d;
                if (!double.TryParse(parameters[i], out d))
                {
                    NEval calc = new NEval();
                    d = calc.Eval(parameters[i]);
                    parameters[i] = d.ToString();
                }
            }
        }


        /// <summary>
        /// 将中缀表达式转为后缀表达式
        /// </summary>
        /// <param name="expr"></param>
        /// <returns></returns>
        private Stack ConvertExprBack(string expr)
        {
            /*
             * 新建一个Stack栈，用来存放运算符
             * 新建一个post栈，用来存放最后的后缀表达式
             * 从左到右扫描中缀表达式：
             * 1.若读到的是操作数，直接存入post栈，以#作为数字的结束
             * 2、若读到的是(,则直接存入stack栈
             * 3.若读到的是），则将stack栈中(前的所有运算符出栈，存入post栈
             * 4 若读到的是其它运算符，则将该运算符和stack栈顶运算符作比较：若高于或等于栈顶运算符， 则直接存入stack栈，
             * 否则将栈顶运算符（所有优先级高于读到的运算符的，不包括括号）出栈，存入post栈。最后将读到的运算符入栈
             * 当扫描完后，stack栈中还在运算符时，则将所有的运算符出栈，存入post栈
             * */


            Stack post = new Stack();
            Stack stack = new Stack();
            string tmpstr;
            int pos;
            for (int i = 0; i <= expr.Length - 1; i++)
            {
                char c = expr[i];
                LetterType lt = JudgeLetterType(c, expr, i);

                if (lt == LetterType.Number)  //操作数
                {
                    GetCompleteNumber(expr, i, out tmpstr, out pos);
                    post.Push(tmpstr);
                    i = pos;// +1;
                }
                else if (lt == LetterType.OpeningParenthesis) //左括号(
                {
                    stack.Push(c);
                }
                else if (lt == LetterType.ClosingParenthesis) //右括号)
                {
                    while (stack.Count > 0)
                    {
                        if (stack.Peek().ToString() == "(")
                        {
                            stack.Pop();
                            break;
                        }
                        else
                            post.Push(stack.Pop());
                    }
                }
                else if (lt == LetterType.SimpleOperator)  //其它运算符
                {
                    if (stack.Count == 0)
                        stack.Push(c);
                    else
                    {

                        char tmpop = (char)stack.Peek();
                        if (tmpop == '(')
                        {
                            stack.Push(c);
                        }
                        else
                        {
                            if (GetPriority(c) >= GetPriority(tmpop))
                            {
                                stack.Push(c);
                            }
                            else
                            {
                                while (stack.Count > 0)
                                {
                                    object tmpobj = stack.Peek();
                                    if (GetPriority((char)tmpobj) > GetPriority(c))
                                    {
                                        if (tmpobj.ToString() != "(")
                                            post.Push(stack.Pop());
                                        else
                                            break;
                                    }
                                    else
                                        break;
                                }
                                stack.Push(c);
                            }
                        }


                    }
                }
                else if (lt == LetterType.Function)  //如果是一个函数，则完整取取出函数，当作一个操作数处理
                {
                    GetCompleteFunction(expr, i, out tmpstr, out pos);
                    post.Push(tmpstr);
                    i = pos;// +1;
                }

            }
            while (stack.Count > 0)
            {
                post.Push(stack.Pop());
            }

            return post;
        }


        private LetterType JudgeLetterType(char c, string expr, int pos)
        {
            string op = "*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else if ((c == '-') || (c == '+'))//要判断是减号还是负数
            {
                if (pos == 0)
                    return LetterType.Number;
                else
                {
                    char tmpc = expr[pos - 1];
                    if (tmpc <= '9' && tmpc >= '0')  //如果前面一位是操作数
                        return LetterType.SimpleOperator;
                    else if (tmpc == ')')
                        return LetterType.SimpleOperator;
                    else
                        return LetterType.Number;
                }
            }
            else
                return LetterType.Function;
        }

        private LetterType JudgeLetterType(char c)
        {
            string op = "+-*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else
                return LetterType.Function;
        }

        private LetterType JudgeLetterType(string s)
        {
            char c = s[0];
            if ((c == '-') || (c == '+'))
            {
                if (s.Length > 1)
                    return LetterType.Number;
                else
                    return LetterType.SimpleOperator;
            }

            string op = "+-*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else
                return LetterType.Function;
        }

        /// <summary>
        /// 计算操作符的优先级
        /// </summary>
        /// <param name="c"></param>
        /// <returns></returns>
        private int GetPriority(char c)
        {
            if (c == '+' || c == '-')
                return 0;
            else if (c == '*')
                return 1;
            else if (c == '/')  //除号优先级要设得比乘号高，否则分母可能会被先运算掉
                return 2;
            else
                return 2;
        }

        /// <summary>
        /// 获取完整的函数表达式
        /// </summary>
        /// <param name="expr"></param>
        /// <param name="startPos"></param>
        /// <param name="funcStr"></param>
        /// <param name="endPos"></param>
        private void GetCompleteFunction(string expr, int startPos, out string funcStr, out int endPos)
        {
            int cpnum = 0;
            for (int i = startPos; i <= expr.Length - 1; i++)
            {
                char c = expr[i];
                LetterType lt = JudgeLetterType(c);
                if (lt == LetterType.OpeningParenthesis)
                    cpnum++;
                else if (lt == LetterType.ClosingParenthesis)
                {
                    cpnum--;//考虑到函数嵌套的情况，消除掉内部括号
                    if (cpnum == 0)
                    {
                        endPos = i;
                        funcStr = expr.Substring(startPos, endPos - startPos + 1);
                        return;
                    }


                }

            }
            funcStr = "";
            endPos = -1;
        }

        /// <summary>
        /// 获取到完整的数字
        /// </summary>
        /// <param name="expr"></param>
        /// <param name="startPos"></param>
        /// <param name="numberStr"></param>
        /// <param name="endPos"></param>
        private void GetCompleteNumber(string expr, int startPos, out string numberStr, out int endPos)
        {
            char c = expr[startPos];
            for (int i = startPos + 1; i <= expr.Length - 1; i++)
            {
                char tmpc = expr[i];
                if (JudgeLetterType(tmpc) != LetterType.Number)
                {
                    endPos = i - 1;
                    numberStr = expr.Substring(startPos, endPos - startPos + 1);
                    return;
                }
            }
            numberStr = expr.Substring(startPos);
            endPos = expr.Length - 1;
        }
    }


    /// <summary>
    /// 可以检测到的表达式错误的Exception
    /// </summary>
    public class ExpressionException : Exception
    {
        public override string Message
        {
            get
            {
                return base.Message;
            }
        }
    }

    /// <summary>
    /// 字符类别
    /// </summary>
    public enum LetterType
    {
        Number,
        SimpleOperator,
        Function,
        OpeningParenthesis,
        ClosingParenthesis
    }



    public class clsMP3TAG
    {
        private byte[] TAGBody = new byte[128];

        private byte[] sTag = new byte[3];
        private byte[] sTitle = new byte[30];
        private byte[] sArtist = new byte[30];
        private byte[] sAlbum = new byte[30];
        private byte[] sYear = new byte[4];
        private byte[] sComment = new byte[30];
        private byte[] sGenre = new byte[1];

        System.Exception myException;

        public clsMP3TAG(byte[] TAG)
        {
            if (TAG.Length != 128)
            {
                myException = new Exception("不是標准的 Mpeg-MP3 TAG 格式。\nTAG長度應該是 128 Byte。");
                throw (myException);
            }
            else
            {
                Array.Copy(TAG, 0, sTag, 0, 3);
                if (!Encoding.Default.GetString(sTag).Equals("TAG"))
                {
                    myException = new Exception("不是標准的 Mpeg-MP3 TAG 格式。\nTAG位校驗出錯。");
                    throw (myException);
                }

                Array.Copy(TAG, 3, sTitle, 0, 30);
                Array.Copy(TAG, 33, sArtist, 0, 30);
                Array.Copy(TAG, 63, sAlbum, 0, 30);
                Array.Copy(TAG, 93, sYear, 0, 4);
                Array.Copy(TAG, 97, sComment, 0, 30);
                Array.Copy(TAG, 127, sGenre, 0, 1);


            }
        }

        /**/
        //////////////////////////////////////////////////////
        /// 以下是屬性，只讀
        //////////////////////////////////////////////////////
        public string Title
        {
            get
            {
                return Encoding.Default.GetString(sTitle);
            }
        }

        public string Artist
        {
            get
            {
                return Encoding.Default.GetString(sArtist);
            }
        }

        public string Album
        {
            get
            {
                return Encoding.Default.GetString(sAlbum);
            }
        }

        public string Year
        {
            get
            {
                return Encoding.Default.GetString(sYear);
            }
        }

        public string Comment
        {
            get
            {
                return Encoding.Default.GetString(sComment);
            }
        }

        public string Genre
        {
            get
            {
                switch (Convert.ToInt16(sGenre[0]))
                {
                    case 0: return "Blues";
                    case 20: return "Alternative";
                    case 40: return "AlternRock";
                    case 60: return "Top 40";
                    case 1: return "Classic Rock";
                    case 21: return "Ska";
                    case 41: return "Bass";
                    case 61: return "Christian Rap";
                    case 2: return "Country";
                    case 22: return "Death Metal";
                    case 42: return "Soul";
                    case 62: return "Pop/Funk";
                    case 3: return "Dance";
                    case 23: return "Pranks";
                    case 43: return "Punk";
                    case 63: return "Jungle";
                    case 4: return "Disco";
                    case 24: return "Soundtrack";
                    case 44: return "Space";
                    case 64: return "Native American";
                    case 5: return "Funk";
                    case 25: return "Euro-Techno";
                    case 45: return "Meditative";
                    case 65: return "Cabaret";
                    case 6: return "Grunge";
                    case 26: return "AmbIEnt";
                    case 46: return "Instrumental Pop";
                    case 66: return "New Wave";
                    case 7: return "Hip-Hop";
                    case 27: return "Trip-Hop";
                    case 47: return "Instrumental Rock";
                    case 67: return "Psychadelic";
                    case 8: return "Jazz";
                    case 28: return "Vocal";
                    case 48: return "Ethnic";
                    case 68: return "Rave";
                    case 9: return "Metal";
                    case 29: return "Jazz+Funk";
                    case 49: return "Gothic";
                    case 69: return "Showtunes";
                    case 10: return "New Age";
                    case 30: return "Fusion";
                    case 50: return "Darkwave";
                    case 70: return "Trailer";
                    case 11: return "OldIEs";
                    case 31: return "Trance";
                    case 51: return "Techno-Industrial";
                    case 71: return "Lo-Fi";
                    case 12: return "Other";
                    case 32: return "Classical";
                    case 52: return "Electronic";
                    case 72: return "Tribal";
                    case 13: return "Pop";
                    case 33: return "Instrumental";
                    case 53: return "Pop-Folk";
                    case 73: return "Acid Punk";
                    case 14: return "R&B";
                    case 34: return "Acid";
                    case 54: return "Eurodance";
                    case 74: return "Acid Jazz";
                    case 15: return "Rap";
                    case 35: return "House";
                    case 55: return "Dream";
                    case 75: return "Polka";
                    case 16: return "Reggae";
                    case 36: return "Game";
                    case 56: return "Southern Rock";
                    case 76: return "Retro";
                    case 17: return "Rock";
                    case 37: return "Sound Clip";
                    case 57: return "Comedy";
                    case 77: return "Musical";
                    case 18: return "Techno";
                    case 38: return "Gospel";
                    case 58: return "Cult";
                    case 78: return "Rock & Roll";
                    case 19: return "Industrial";
                    case 39: return "Noise";
                    case 59: return "Gangsta";
                    case 79: return "Hard Rock";


                    default:
                        return "未知類型";
                }
            }
        }
    }
}


