using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Xml;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

using System.Security.Cryptography; //for MD5CryptoServiceProvider
using Microsoft.Win32;  //for RegistryKey

using System.Drawing.Imaging;

namespace test6
{
    public partial class Form1 : Form
    {
        //實現控件中捕獲按鍵 只要補上這個函數就好
        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            const int WM_KEYDOWN = 0x100;
            const int WM_SYSKEYDOWN = 0x104;
            if ((msg.Msg == WM_KEYDOWN) || (msg.Msg == WM_SYSKEYDOWN))
            {
                switch (keyData)
                {
                    case Keys.Down:
                        this.Text = "向下鍵已經被捕捉";
                        break;
                    case Keys.Up:
                        this.Text = "向上鍵已經被捕捉";
                        break;
                    case Keys.Left:
                        this.Text = "向左鍵已經被捕捉";
                        break;
                    case Keys.Right:
                        this.Text = "向右鍵已經被捕捉";
                        break;
                    case Keys.Home:
                        this.Text = "Home 鍵已經被捕捉";
                        break;
                    case Keys.End:
                        this.Text = "End 鍵已經被捕捉";
                        break;
                }
            }
            return base.ProcessCmdKey(ref msg, keyData);
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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //模擬MSN窗體抖動1

            int rand = 50;
            int recordx = this.Left;　//保存原來窗體的左上角的x坐標
            int recordy = this.Top;　//保存原來窗體的左上角的y坐標

            Random random = new Random();

            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }

                this.Left = recordx;　//還原原始窗體的左上角的x坐標
                this.Top = recordy;　//還原原始窗體的左上角的y坐標
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //模擬MSN窗體抖動2

            int rand = 10;
            int recordx = this.Left;
            int recordy = this.Top;
            Random random = new Random();
            for (int i = 0; i < 50; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }
                System.Threading.Thread.Sleep(1);
            }
            this.Left = recordx;
            this.Top = recordy;
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //字串編碼處理
            /*
            GB2312是簡體中文系統的標准編碼 用“區” 跟“位”的概念表示 稱之為區位碼
            區指代大的范圍 位相當於偏移量。
            每個漢字占兩個字節
            高位字節”的范圍是0xB0-0xF7，“低位字節”的范圍是0xA1-0xFE。
            它的規律好像是按拼音a到z的順序排列的
            “啊”字是GB2312之中的第一個漢字，它的區位碼就是1601
            為此我們現在用代碼的方式輸出一個漢字

            c#下是little字節序 b0跑後面去了。
            */

            ushort u = 0xa1b0;

            int i;
            for (i = 0; i < 30; i++)
            {
                byte[] chs = BitConverter.GetBytes(u + i);
                Console.Write(Encoding.GetEncoding("GB2312").GetString(chs));
                richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(chs);
            }
            richTextBox1.Text += "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //輸出所有的漢字
            /*
            GB2312是簡體中文系統的標准編碼 用“區” 跟“位”的概念表示 稱之為區位碼
            區指代大的范圍 位相當於偏移量。
            每個漢字占兩個字節
            高位字節”的范圍是0xB0-0xF7，“低位字節”的范圍是0xA1-0xFE。
            它的規律好像是按拼音a到z的順序排列的
            “啊”字是GB2312之中的第一個漢字，它的區位碼就是1601
            為此我們現在用代碼的方式輸出一個漢字

            c#下是little字節序 b0跑後面去了。
            */

            richTextBox1.Text += "輸出所有的漢字\n";
            //gb2312
            //B0-F7，低字節從A1-FE
            //byte hi = 0xB0;
            //byte lo = 0xA1;
            for (byte i = 0xB0; i <= 0xF7; i++)
            {
                for (byte j = 0xA1; j <= 0xFE; j++)
                {
                    //byte t = (byte)(j | (byte)0x01);
                    Console.Write(Encoding.GetEncoding("GB2312").GetString(new byte[] { i, j }));
                    richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(new byte[] { i, j });
                }
            }
            richTextBox1.Text += "\n\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            /**
            實際上，全角字符的第一個字節總是被置為163，
            而第二個字節則是相同半角字符碼加上128（不包括空格）。
            如半角A為65，則全角A則是163（第一個字節）、193（第二個字節，128+65）。
            */

            richTextBox1.Text += "全形ASCII\n";
            for (byte k = 0x00; k < 0x7f; k++)
            {
                byte[] ch = new byte[2];
                ch[0] = 163;
                ch[1] = (byte)(128 + k);
                Console.Write(Encoding.GetEncoding("GB2312").GetString(ch));
                richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(ch);
            }
            richTextBox1.Text += "\n";
        }


        //C#切換鼠標左右鍵習慣無需控制面板中修改

        [DllImport("user32.dll")]
        private extern static bool SwapMouseButton(bool fSwap);

        [DllImport("user32.dll")]
        private extern static int GetSystemMetrics(int index);

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 切換鼠標左右鍵\n";

            int flag = GetSystemMetrics(23);//獲取當前鼠標設置狀態
            if (flag == 0)//右手習慣
            {
                SwapMouseButton(true);//設置成左手
                richTextBox1.Text += "換成左手\n";
            }
            else//左手習慣
            {
                SwapMouseButton(false);//設置成右手
                richTextBox1.Text += "換成右手\n";
            }
        }


        /*
        理解多態。
        首先，我們先來看下怎樣用虛方法實現多態

        我們都知道，喜鵲（Magpie）、老鷹（Eagle）、企鵝（Penguin）都是屬於鳥類，我們可以根據這三者的共有特性提取出鳥類（Bird）做為父類，喜鵲喜歡吃蟲子，老鷹喜歡吃肉，企鵝喜歡吃魚。
        */

        //創建基類Bird如下，添加一個虛方法Eat():


        /*
        /// <summary>
        /// 鳥類：父類
        /// </summary>
        public class Bird
        {
            /// <summary>
            /// 吃：虛方法
            /// </summary>
            public virtual void Eat()
            {
                Console.WriteLine("我是一只小小鳥，我喜歡吃蟲子~");
            }
        }
        */

        /// <summary>
        /// 鳥類：基類
        /// </summary>
        public abstract class Bird
        {
            /// <summary>
            /// 吃：抽象方法
            /// </summary>
            public abstract void Eat(); //抽象類Bird內添加一個Eat()抽象方法，沒有方法體。也不能實例化。
        }

        //創建子類Magpie如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 飛 接口
        /// </summary>
        public interface IFlyable
        {
            void Fly();
        }

        /*
        /// <summary>
        /// 喜鵲：子類
        /// </summary>
        public class Magpie : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
            }
        }

        //創建一個子類Eagle如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 老鷹：子類
        /// </summary>
        public class Eagle : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
            }
        }
        */

        //喜鵲Magpie實現IFlyable接口，代碼如下：

        /// <summary>
        /// 喜鵲：子類，實現IFlyable接口
        /// </summary>
        public class Magpie : Bird, IFlyable
        {
            /// <summary>
            /// 重寫父類Bird中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只喜鵲，我喜歡吃蟲子~");
            }
            /// <summary>
            /// 實現 IFlyable接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一只喜鵲，我可以飛哦~~");
            }
        }

        //老鷹Eagle實現IFlyable接口，代碼如下：

        /// <summary>
        /// 老鷹：子類實現飛接口
        /// </summary>
        public class Eagle : Bird, IFlyable
        {
            /// <summary>
            /// 重寫父類Bird中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只老鷹，我喜歡吃肉~");
            }

            /// <summary>
            /// 實現 IFlyable接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一只老鷹，我可以飛哦~~");
            }
        }


        //創建一個子類Penguin如下，繼承父類Bird，重寫父類Bird中的虛方法Eat()：

        /// <summary>
        /// 企鵝：子類
        /// </summary>
        public class Penguin : Bird
        {
            /// <summary>
            /// 重寫父類中Eat方法
            /// </summary>
            public override void Eat()
            {
                Console.WriteLine("我是一只小企鵝，我喜歡吃魚~");
            }
        }

        /// <summary>
        /// 飛機類，實現IFlyable接口
        /// </summary>
        public class Plane : IFlyable
        {
            /// <summary>
            /// 實現接口方法
            /// </summary>
            public void Fly()
            {
                Console.WriteLine("我是一架飛機，我也能飛~~");
            }
        }


        private void button9_Click(object sender, EventArgs e)
        {
            //Class測試
            //創建一個Bird基類數組，添加基類Bird對象，Magpie對象，Eagle對象，Penguin對象
            Bird[] birds = { 
                       //new Bird(),    用Abstract, Bird就不能創建對象了
                       new Magpie(),
                       new Eagle(),
                       new Penguin()
            };
            //遍歷一下birds數組
            foreach (Bird bird in birds)
            {
                bird.Eat();
            }

            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象
            IFlyable[] flys = { 
                       new Magpie(),
                       new Eagle()
        };
            //遍歷一下flys數組
            foreach (IFlyable fly in flys)
            {
                fly.Fly();
            }


            //創建一個IFlyable接口數組，添加 Magpie對象，Eagle對象，Plane對象
            IFlyable[] flys2 = { 
                           new Magpie(),
                           new Eagle(),
                           new Plane()
            };
            //遍歷一下flys數組
            foreach (IFlyable fly in flys2)
            {
                fly.Fly();
            }

        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\elephant.jpg";
            Image sample = new Bitmap(filename);
            MemoryStream buf = new MemoryStream();
            sample.Save(buf, ImageFormat.Bmp);
            byte[] currentImage = buf.GetBuffer();

            int[] stats = new int[3];
            for (int i = 0; i < currentImage.Length; )
            {
                for (int j = 0; j < 3; j++)
                {
                    stats[j] += currentImage[i];
                    ++i;
                }
            }
            richTextBox1.Text += "Blue: " + stats[0] + "\n";
            richTextBox1.Text += "Green: " + stats[1] + "\n";
            richTextBox1.Text += "Red: " + stats[2] + "\n";
            if ((stats[0] > stats[1]) && (stats[0] > stats[2]))
            {
                richTextBox1.Text += "This is a cold picture." + "\n";
            }
            if ((stats[1] > stats[0]) && (stats[1] > stats[2]))
            {
                richTextBox1.Text += "This is a summer picture." + "\n";
            }
            if ((stats[2] > stats[0]) && (stats[2] > stats[1]))
            {
                richTextBox1.Text += "This is a fiery picture." + "\n";
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //建立亂七八糟陣列
            byte[] dataArray = new byte[100];//字節

            new Random().NextBytes(dataArray);//創建隨機字節

            for (int i = 0; i < dataArray.Length; i++)
            {

                //sf.WriteByte(dataArray[i]);//將字節寫入文件理.
                richTextBox1.Text += dataArray[i].ToString() + " ";

            }

        }

        //設置系統日期和時間 ST
        public class SetSystemDateTime
        {

            [DllImportAttribute("Kernel32.dll")]

            public static extern void GetLocalTime(SystemTime st);

            [DllImportAttribute("Kernel32.dll")]

            public static extern void SetLocalTime(SystemTime st);

        }

        [StructLayoutAttribute(LayoutKind.Sequential)]
        public class SystemTime
        {

            public ushort vYear;

            public ushort vMonth;

            public ushort vDayOfWeek;

            public ushort vDay;

            public ushort vHour;

            public ushort vMinute;

            public ushort vSecond;

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //設置系統日期和時間
            //Romeo可用 Sugar不可用
            //DateTime Year = this.dateTimePicker1.Value;
            SystemTime MySystemTime = new SystemTime();
            SetSystemDateTime.GetLocalTime(MySystemTime);
            /*
            MySystemTime.vYear = (ushort)this.dateTimePicker1.Value.Year;
            MySystemTime.vMonth = (ushort)this.dateTimePicker1.Value.Month;
            MySystemTime.vDay = (ushort)this.dateTimePicker1.Value.Day;
            MySystemTime.vHour = (ushort)this.dateTimePicker2.Value.Hour;
            MySystemTime.vMinute = (ushort)this.dateTimePicker2.Value.Minute;
            MySystemTime.vSecond = (ushort)this.dateTimePicker2.Value.Second;
            */
            MySystemTime.vYear = 2021;
            MySystemTime.vMonth = 11;
            MySystemTime.vDay = 3;
            MySystemTime.vHour = 23;
            MySystemTime.vMinute = 37;
            MySystemTime.vSecond = 00;

            SetSystemDateTime.SetLocalTime(MySystemTime);
        }
        //設置系統日期和時間 SP

        private void button13_Click(object sender, EventArgs e)
        {
            //用C#去讀取特定位置的Refistry Key
            string result = ReadRegistryKey("Software\\AIMTest"); //直接給string的Registry路徑即可
            richTextBox1.Text += "result : \t" + result + "\n";

        }

        public string ReadRegistryKey(string RegKey)
        {
            //讀取Registry Key位置

            RegistryKey RegK = Registry.LocalMachine.OpenSubKey(RegKey);
            //讀取Registry Key String"test"裡面的值
            string RegT = (string)RegK.GetValue("test");
            //Show Registry Key值，檢查讀取的值是否正確
            MessageBox.Show(RegT);
            return RegT;

        }


        private void button14_Click(object sender, EventArgs e)
        {
            //使用Shell32讀取影音文件屬性
            /*
            由於需要用到實時讀取影音文件(mp3、wma、wmv …)播放時間長度的功能，搜索到的結果有：
            （1）硬編碼分析影音文件，需要分析各種媒體格式，代價最大；
            （2）使用WMLib SDK，需要熟悉SDK各個接口，且不同版本的WM接口有別，代價次之；
            （3）使用系統Shell32的COM接口，直接訪問媒體文體屬性，取其特定內容，代價最小。
            顯然第3種方案見效最快，立即操刀：
            ①引用Shell32底層接口c:\windows\system32\shell32.dll，VS自動轉換成Interop.Shell32.dll（注：64位系統和32位系統生成的Interop.Shell32.dll不一樣）
            ②編碼讀取播放時間長度：
            */

            //取得媒體資訊
            //string filename = @"C:\______test_files\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            string filename = @"C:\______test_files\_mp3\aaaa.mp3";
            int i;
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + GetMediaInfo(filename, i) + "\n";
            }
        }

        public string GetMediaInfo(string path, int item)
        {
            //參考/Shell32/右鍵/屬性/內嵌Interop型別改成False
            try
            {
                string result = string.Empty;
                Shell32.Shell shell = new Shell32.ShellClass();
                Shell32.Folder folder = shell.NameSpace(path.Substring(0, path.LastIndexOf("\\")));
                Shell32.FolderItem folderItem = folder.ParseName(path.Substring(path.LastIndexOf("\\") + 1));
                return folder.GetDetailsOf(folderItem, item);
            }
            catch (Exception ex)
            {
                return null;
            }
        }


        private void button15_Click(object sender, EventArgs e)
        {
            //C#讀取XML文檔的方法
            //C#讀取XML文檔的方法

            //這裡介紹一種讀取XML文檔的方法,示例中用的是 XmlTextReader 函數,每執行 Read() 一次,讀取一行.

        }


        public void ReadConfig(string XmlConfigFile)
        {
            try
            {
                // Open an XML file
                System.Xml.XmlTextReader reader;
                reader = new System.Xml.XmlTextReader(XmlConfigFile);
                while (reader.Read())
                {
                    if ((reader.NodeType == XmlNodeType.EndElement)
                    && (reader.Name == "KSBM"))
                    {
                        break;
                    }
                    if (reader.IsStartElement("ServerPath"))
                    {
                        reader.Read();
                        //_conf.ServerPath = reader.Value;
                    }
                    else if (reader.IsStartElement("SmtpServer"))
                    {
                        reader.Read();
                        //_conf.SMTPServer = reader.Value;
                    }
                    else if (reader.IsStartElement("ConnectString"))
                    {
                        reader.Read();
                        //_conf.ConnectString = reader.Value;
                    }
                }
                //return _conf;
            }
            catch
            {
                //return _conf;
            }
            finally
            {
            }
        }
    }
}
