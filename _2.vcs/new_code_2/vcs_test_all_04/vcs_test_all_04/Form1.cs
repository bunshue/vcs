using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

using System.Management;    //for ManagementObjectSearcher

using System.Diagnostics;
using System.IO;

using System.Runtime.InteropServices;   //for DllImport

using System.Text.RegularExpressions;   //for Regex

using Microsoft.VisualBasic.Devices;

using System.Collections;       //for DictionaryEntry
using System.Drawing.Imaging;   //for ImageFormat

using System.Drawing.Text;      //for InstalledFontCollection

using System.Media;     //for SoundPlayer

using Microsoft.VisualBasic;

namespace vcs_test_all_04
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            Image image = Image.FromFile(filename);
            pictureBox1.Image = image;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 140;
            dy = 60;

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

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //表單背景漸層色 只要補這一段就好
        protected override void OnPaintBackground(PaintEventArgs e)
        {
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值
            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();//定义一个Color类型的实例color
                //为实例color赋值
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);//实例化一个单色画笔类对象SBrush
                Pen pen = new Pen(SBrush, 1);//实例化一个用于绘制直线和曲线的对象pen
                e.Graphics.DrawRectangle(pen, this.ClientRectangle.X, intLocation, this.Width, intLocation + intHeight);//绘制图形
                intLocation = intLocation + intHeight;//重新为变量intLocation赋值
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string filename1 = @"C:\______test_files\bear.bmp";
            bitmap = new Bitmap(filename1);
            pictureBox1.Image = bitmap;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            FileInfo f1 = new FileInfo(filename1);

            string filename2 = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //string fileName = saveFileDialog.FileName;
            bitmap.Save(filename2, ImageFormat.Jpeg);
            FileInfo f2 = new FileInfo(filename2);

            richTextBox1.Text += "圖像轉換 : " + f1.Name + " 轉換成 " + f2.Name + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string filename1 = @"C:\______test_files\picture1.jpg";
            bitmap = new Bitmap(filename1);
            pictureBox1.Image = bitmap;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            FileInfo f1 = new FileInfo(filename1);

            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            //string fileName = saveFileDialog.FileName;
            bitmap.Save(filename2, ImageFormat.Bmp);
            FileInfo f2 = new FileInfo(filename2);

            richTextBox1.Text += "圖像轉換 : " + f1.Name + " 轉換成 " + f2.Name + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap;
            string filename1 = @"C:\______test_files\_icon\唐.ico";
            bitmap = new Bitmap(filename1);
            pictureBox1.Image = bitmap;
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            FileInfo f1 = new FileInfo(filename1);

            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            //string fileName = saveFileDialog.FileName;
            bitmap.Save(filename2, ImageFormat.Bmp);
            FileInfo f2 = new FileInfo(filename2);

            richTextBox1.Text += "圖像轉換 : " + f1.Name + " 轉換成 " + f2.Name + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //檢視圖片的像素
            string filename1 = @"C:\______test_files\picture1.jpg";

            Image image = Image.FromFile(filename1);
            richTextBox1.Text += "檔案 : " + filename + ",\t" + "圖片像素：[" + image.Width + "*" + image.Height + "]" + "\n";
        }

        #region  获取文件的播放时间，并在列表中进行显示
        /// <summary>
        /// 获取文件的播放时间，并在列表中进行显示
        /// </summary>
        /// <param Millisecond="int">毫秒数</param>
        //添加using System.Runtime.InteropServices;API函数的命名空间
        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern int GetShortPathName(string lpszLongPath, string shortFile, int cchBuffer);//获取指定文件的短路径名

        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);//播放多媒体文件

        public int LongTime(string Spath)
        {
            richTextBox1.Text += "Spath = " + Spath + "\n";
            string Pname = "";//用来保存多媒体文件的命令       
            string TemStr = "";//用来保存处理后的字符串
            int ilong = 0;//用来保存短路径文件名
            string tem_str = "";//用来保存最终的文件名
            int t = 0;//声明一个用来保存时间的变量
            TemStr = TemStr.PadLeft(128, Convert.ToChar(" "));//右对齐此实例中的字符，在左边用空格或指定的 Unicode 字符填充以达到指定的总长度
            ilong = GetShortPathName(Spath, TemStr, TemStr.Length);//获取指定路径下的短路径文件名
            Pname = "open " + Convert.ToChar(34) + Spath + Convert.ToChar(34) + " alias media";//为变量Pname赋值
            t = mciSendString(Pname, TemStr, TemStr.Length, 0);//打开指定的多媒体文件
            t = mciSendString("status " + Spath + " length", TemStr, 128, 0);//获取当前多媒体文件的状态
            tem_str = TemStr.Substring(0, TemStr.IndexOf("\0"));//为变量tem_str赋值
            if (tem_str.Trim() == "")//当变量tem_str的值为空时
                t = 0;//设定变量t的值为0
            else//当变量tem_str的值为非空时
                t = Convert.ToInt32(tem_str);//重新设定变量t的值
            return t;//返回变量t的值
        }
        #endregion

        #region  获取文件的播放时间，并按指定格式进行显示
        /// <summary>
        /// 获取文件的播放时间，并按指定格式进行显示
        /// </summary>
        /// <param Millisecond="int">毫秒数</param>
        public string GetFileTime(int Millisecond)
        {
            string Tem_Time = ""; //用来保存歌曲的播放时间
            double Tem_min = 0;  //用来保存歌曲播放的分钟部分
            double Tem_sec = 0;  //用来保存歌曲播放时间的秒
            double Tem_millisec = 0; //用来保存歌曲播放时间的毫秒

            Tem_min = Millisecond / 1000;//将当前时间转化为以秒为单位的数据类型
            Tem_min = Tem_min / 60.0; //将当前时间转化为以分为单位的数据类型

            Tem_sec = Tem_min - (int)Tem_min; //保存歌曲播放时间的小数部分（当以分为单位时）
            Tem_min = (int)Tem_min; //将double型变量Tem_min转化为int型变量
            Tem_sec = (60 * Tem_sec) / 100.0; //将获得的小数转化为以秒为单位的数据
            Tem_sec = (int)(Tem_sec * 100);//将数据类型转化为int型
            Tem_millisec = (int)((Millisecond - Tem_min * 60 * 1000 - Tem_sec * 1000) / 1000 * 100);//将歌曲播放的时间转换为以秒为单位存储
            if (Tem_min >= 100)//当Tem_min的值大于等于100时
            {
                Tem_Time = Tem_min.ToString("000") + ":" + Tem_sec.ToString("00");//设置时间的显示格式
            }
            else//当Tem_min的值小于100时
                Tem_Time = Tem_min.ToString("00") + ":" + Tem_sec.ToString("00"); //设置事件的显示格式
            return Tem_Time;//返回变量Tem_Time
        }
        #endregion

        private void button4_Click(object sender, EventArgs e)
        {
            //取得mp3播放長度
            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            richTextBox1.Text += "filename = " + filename + "\n";
            richTextBox1.Text += "播放時間 : " + GetFileTime(LongTime(filename)) + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //播放wav檔
            string filename = @"C:\______test_files\_wav\start.wav";
            SoundPlayer player = new SoundPlayer(); //声明一个控制WAV文件的声音播放文件对象
            player.SoundLocation = filename; //指定声音文件的路径
            player.LoadAsync();  //设置播放的方法
            player.Play(); //播放声音文件
        }


        [DllImport("winmm.dll", EntryPoint = "waveOutGetNumDevs")]
        public static extern int waveOutGetNumDevs();
        private void button6_Click(object sender, EventArgs e)
        {
            //是否安裝音效卡
            if (waveOutGetNumDevs() != 0)
            {
                richTextBox1.Text += "已安裝音效卡\n";
            }
            else
            {
                richTextBox1.Text += "未安裝音效卡\n";
            }

        }

        [System.Runtime.InteropServices.DllImport("user32.dll", EntryPoint = "SwapMouseButton")]
        public extern static int SwapMouseButton(int bSwap);
        [System.Runtime.InteropServices.DllImport("user32.dll")]
        public extern static int GetSystemMetrics(int nIndes);
        private void button7_Click(object sender, EventArgs e)
        {
            if (button7.Text == "切換滑鼠左右鍵")
            {
                SwapMouseButton(1);//切換滑鼠游標左右鍵


                button7.Text = "恢復滑鼠左右鍵";
            }
            else
            {
                SwapMouseButton(0);//恢復，設定左鍵為主鍵

                button7.Text = "切換滑鼠左右鍵";
            }
        }

        [DllImport("winmm.dll", EntryPoint = "mciSendString")]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, System.UInt16 uReturnLength, System.IntPtr HwndCallback);

        private void button8_Click(object sender, EventArgs e)
        {
            //光碟機打開
            int i = mciSendString("Set cdaudio door open wait", "", 0, this.Handle);
            if (i == 0)
            {
                MessageBox.Show("CD_ROM打開");
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //光碟機關閉
            int i = mciSendString("Set cdaudio door Closed wait", "", 0, this.Handle);
            if (i == 0)
            {
                MessageBox.Show("CD_ROM關閉");
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //圖片轉向
            string filename = @"C:\______test_files\picture1.jpg";
            //pictureBox1.Image = Image.FromFile(filename);


            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);
            pictureBox1.Image = bitmap1;


            Bitmap bitmap2 = (Bitmap)Bitmap.FromFile(filename);
            bitmap2.RotateFlip(RotateFlipType.Rotate90FlipX);
            pictureBox2.Image = bitmap2;


        }

        private void button11_Click(object sender, EventArgs e)
        {
            Image image = pictureBox1.Image;
            image.RotateFlip(RotateFlipType.Rotate90FlipXY);
            pictureBox1.Image = image;
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

        private void button12_Click(object sender, EventArgs e)
        {
            Int64 a = 123456;
            richTextBox1.Text += "原拜數 : \t" + a.ToString() + "\t";
            richTextBox1.Text += "轉換後 : \t" + ByteConversionGBMBKB(a).ToString() + "\n";
            a = 123456789;
            richTextBox1.Text += "原拜數 : \t" + a.ToString() + "\t";
            richTextBox1.Text += "轉換後 : \t" + ByteConversionGBMBKB(a).ToString() + "\n";
            a = 123456789123;
            richTextBox1.Text += "原拜數 : \t" + a.ToString() + "\t";
            richTextBox1.Text += "轉換後 : \t" + ByteConversionGBMBKB(a).ToString() + "\n";

        }

        private void button13_Click(object sender, EventArgs e)
        {
            DateTime dt1 = new DateTime(2006, 3, 11, 9, 15, 30);
            //DateTime dt1 = new DateTime(2021, 5, 21, 9, 15, 30);
            DateTime dt2 = DateTime.Now;
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Year, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 年\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Month, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 月\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Day, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 天\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //创建日历对象
            System.Globalization.ChineseLunisolarCalendar chinseCaleander = new System.Globalization.ChineseLunisolarCalendar();
            string TreeYear = "鼠牛虎兔龍蛇馬羊猴雞狗豬";//创建字符串对象
            int intYear = chinseCaleander.GetSexagenaryYear(DateTime.Now);//计算年信息
            //得到生肖信息
            string Tree = TreeYear.Substring(chinseCaleander.GetTerrestrialBranch(intYear) - 1, 1);

            richTextBox1.Text += "今年是十二生肖 " + Tree + " 年\n";

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

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        //繪製驗證碼 ST
        private void button24_Click(object sender, EventArgs e)
        {
            //繪製驗證碼
            CodeImage(CheckCode(), pictureBox3);
        }

        private string CheckCode()
        {
            int number;
            char code;
            string checkCode = String.Empty;

            Random random = new Random();

            for (int i = 0; i < 4; i++)
            {
                number = random.Next();

                if (number % 2 == 0)
                    code = (char)('0' + (char)(number % 10));
                else
                    code = (char)('A' + (char)(number % 26));

                checkCode += " " + code.ToString();
            }
            return checkCode;
        }

        private void CodeImage(string checkCode, PictureBox pbx)
        {
            if (checkCode == null || checkCode.Trim() == String.Empty)
                return;

            Bitmap image = new Bitmap((int)Math.Ceiling((checkCode.Length * 20.0)), 50);
            Graphics g = Graphics.FromImage(image);

            try
            {
                //產生隨機產生器
                Random random = new Random();
                //清空圖片背景色
                g.Clear(Color.White);
                //畫圖片的背景噪音線
                for (int i = 0; i < 3; i++)
                {
                    int x1 = random.Next(image.Width);
                    int x2 = random.Next(image.Width);
                    int y1 = random.Next(image.Height);
                    int y2 = random.Next(image.Height);
                    g.DrawLine(new Pen(Color.Black), x1, y1, x2, y2);
                }
                Font font = new Font("Arial", 24, (FontStyle.Bold));
                g.DrawString(checkCode, font, new SolidBrush(Color.Red), 2, 2);

                //畫圖片的前景噪音點
                for (int i = 0; i < 150; i++)
                {
                    int x = random.Next(image.Width);
                    int y = random.Next(image.Height);

                    image.SetPixel(x, y, Color.FromArgb(random.Next()));
                }
                //畫圖片的邊框線
                g.DrawRectangle(new Pen(Color.Silver), 0, 0, image.Width - 1, image.Height - 1);
                pbx.Width = image.Width;
                pbx.Height = image.Height;
                pbx.BackgroundImage = image;
            }
            catch
            { }
        }
        //繪製驗證碼 SP





    }
}

