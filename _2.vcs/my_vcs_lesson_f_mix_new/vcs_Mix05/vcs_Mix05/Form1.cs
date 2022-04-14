using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;

using System.Management;
using System.Drawing.Text;  //for InstalledFontCollection
using System.Runtime.InteropServices;
using Microsoft.Win32;  //for RegistryKey


namespace vcs_Mix05
{
    public partial class Form1 : Form
    {
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
            dy = 80;

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
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);


            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string sText = this.Text;
            string sFullName = string.Format("{0} %1", Application.ExecutablePath);
            // Application.ExecutablePath 是程式執行檔的完整路徑檔案名稱
            // %1 表示傳入的檔案
            //if (this.rbFile.Checked)
            {
                // 加入檔案右鍵選單
                RegFile(sText, sFullName);
            }
            //else
            {
                // 加入目錄右鍵選單
                //RegDirectory(sText, sFullName);
            }
            MessageBox.Show("作業成功");
        }

        private void RegFile(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"*\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue(string.Empty, sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }

        private void RegDirectory(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"directory\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue("", sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }

        List<double[]> pts = new List<double[]>();    //二維List for double array
        int g = 10;

        //二維List for double
        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            double t = 0;

            for (t = 0; t <= 5.0; t += 0.1)
            {
                //richTextBox1.Text += "t = " + t.ToString() + "\n";
                pts.Add(new double[] { t, g * t * t / 2, g * t * t * t / 2, Math.Sqrt(g * t * t / 2) });
            }

            int len = pts.Count;

            richTextBox1.Text += "共有 " + len.ToString() + " 個項目, 分別是:\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += pts[i][0].ToString("n3") + "\t" + pts[i][1].ToString("n3") + "\t" + pts[i][2].ToString("n3") + "\t" + pts[i][3].ToString("n3") + "\n";
            }
        }

        //多筆資料比較
        private const int CNT = 100;
        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //int N = 10;

            pts.Clear();

            //一維陣列用法：
            double[] a = new double[CNT];
            int[] checked_array = new int[CNT]; //一維陣列用法

            int i;
            int j;

            Random r = new Random();
            for (i = 0; i < CNT; i++)
            {
                //a[i] = r.NextDouble();
                a[i] = r.Next(100, 200);
            }


            for (i = 0; i < CNT; i++)
            {
                //richTextBox1.Text += "取0.0~1.0的亂數值：" + a[i].ToString() + "\n";
                //richTextBox1.Text += "a[" + i.ToString() + "] = " + a[i].ToString() + "\n";

                //result3 += r.Next(10, 20).ToString() + " ";
            }

            Stopwatch sw = new Stopwatch();
            sw.Start();

            int equal_count = 0;

            int[] same_index = new int[10]; //一維陣列用法
            int index = 0;

            for (i = 0; i < CNT; i++)
            {
                if (checked_array[i] == 1)
                    continue;

                index = 0;
                same_index = new int[100];

                for (j = (i + 1); j < CNT; j++)
                {
                    if ((a[i] == a[j]) && (a[i] != -1))
                    {
                        equal_count++;
                        same_index[index] = j;
                        index++;
                        //richTextBox1.Text += "取得相同數字\t\ta[" + i.ToString() + "] = " + a[i].ToString() + "\t\ta[" + j.ToString() + "] = " + a[j].ToString() + "\n";
                    }
                }

                if (index > 0)
                {
                    checked_array[i] = 1;
                    richTextBox1.Text += "取得相同數字\t\ta[" + i.ToString() + "] = " + a[i].ToString();
                    int k;
                    for (k = 0; k < index; k++)
                    {
                        checked_array[same_index[k]] = 1;
                        richTextBox1.Text += "\t\ta[" + same_index[k].ToString() + "] = " + a[same_index[k]].ToString();
                    }
                    richTextBox1.Text += "\n";

                    /*
                    if (index == 1)
                    {
                        richTextBox1.Text += "a[" + same_index[0].ToString() + "] = " + a[same_index[0]].ToString() + "\n";
                    }
                    else if (index == 2)
                    {
                        richTextBox1.Text += "a[" + same_index[0].ToString() + "] = " + a[same_index[0]].ToString() + "\t\ta[" + same_index[1].ToString() + "] = " + a[same_index[1]].ToString() + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "333333333333\n";
                    }
                    //richTextBox1.Text += "index = " + index.ToString() + "\n";
                    */
                }
            }

            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";

            for (i = 0; i < CNT; i++)
            {
                //richTextBox1.Text += "取0.0~1.0的亂數值：" + a[i].ToString() + "\n";
                //richTextBox1.Text += "a[" + i.ToString() + "] = " + a[i].ToString() + "\n";

                //result3 += r.Next(10, 20).ToString() + " ";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //C#中時間相關知識點小結
            //一、月份英文簡寫

            DateTime dt = DateTime.Now;
            string MM = dt.AddMonths(-1).ToString("MMM", new System.Globalization.CultureInfo("en-us"));//月英文縮寫：Jul
            richTextBox1.Text += "月份英文簡寫\t" + MM + "\n";



            //二、當月第一天和最后一天

            DateTime ThisMonth_Frist = DateTime.Now.AddDays(1 - DateTime.Now.Day).Date;
            DateTime ThisMOnth_Last = DateTime.Now.AddDays(1 - DateTime.Now.Day).Date.AddMonths(1).AddSeconds(-1);
            richTextBox1.Text += "當月第一天\t" + ThisMonth_Frist + "\n";
            richTextBox1.Text += "當月最后一天\t" + ThisMOnth_Last + "\n";

            //三、上月第一天和最后一天

            DateTime Today = DateTime.Today;//當天時間
            DateTime ThisMonth = new DateTime(Today.Year, Today.Month, 1);//當前月第一天時間
            DateTime LastMonth_First = ThisMonth.AddMonths(-1);//上月第一天時間
            DateTime LastMonth_Last = ThisMonth.AddDays(-1);//上月最后一天時間
            richTextBox1.Text += "上月第一天\t" + LastMonth_First + "\n";
            richTextBox1.Text += "上月最后一天\t" + LastMonth_Last + "\n";

            //四、本周第幾天

            int daysInWeek1 = (int)DateTime.Now.DayOfWeek;//注意：此處周,日時回傳0，
            int daysInWeek2 = (int)DateTime.Now.DayOfWeek == 0 ? 7 : (int)DateTime.Now.DayOfWeek;//當前周第幾天,注釋:周日為0
            richTextBox1.Text += "本周第幾天\t" + daysInWeek1.ToString() + "\n";
            richTextBox1.Text += "本周第幾天\t" + daysInWeek2.ToString() + "\n";


            //五、本月第幾周

            //int a = WeekOfMonth(DateTime.Now, false);//
            //richTextBox1.Text += "本月第幾周\t" + a + "\n";
        }

        //本年第幾周
        private int WeekOfYear()
        {
            var dt = DateTime.Now;
            int firstWeekend = Convert.ToInt32(DateTime.Parse(dt.Year + "-1-1").DayOfWeek);
            int weekDay = firstWeekend == 0 ? 1 : (7 - firstWeekend + 1);
            int currentDay = dt.DayOfYear;
            int current_week = Convert.ToInt32(Math.Ceiling((currentDay - weekDay) / 7.0)) + 1;
            return current_week;
        }

        //前幾周的周一和周日
        private void FEDayInLastWeek()
        {
            int N = 3;//前幾周引數
            DateTime Today = DateTime.Now;
            int daysInWeek = (int)Today.DayOfWeek == 0 ? 7 : (int)Today.DayOfWeek;//當前周第幾天,注釋:周日為0

            for (int i = N; i > 0; i--)
            {
                //起始日期
                DateTime firstDay = Today.AddDays(1 - (7 * i + daysInWeek));
                DateTime lastDay = Today.AddDays(7 - (7 * i + daysInWeek));
            }
        }

        //本周一和當前日
        private void FristDayToNowInThisWeek()
        {
            int daysInWeek = (int)DateTime.Now.DayOfWeek == 0 ? 7 : (int)DateTime.Now.DayOfWeek;//當前周第幾天,注釋:周日為0
            //起始日期
            DateTime firstDay = DateTime.Now.AddDays(1 - daysInWeek);
            DateTime lastDay = DateTime.Now;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //class test ST
        class P
        {
            private string pname;
            public string Name
            {
                get
                {
                    return "name : " + pname;
                }
                set
                {
                    pname = value;
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            P obj = new P();
            obj.Name = "david wang";            //使用到set
            Console.WriteLine(obj.Name);        //使用到get

        }
        //class test SP

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //分出 時:分:秒 再組合
            DateTime dt = DateTime.Now;
            richTextBox1.Text += dt.Hour.ToString().PadLeft(2, '0') + ":"
                                    + dt.Minute.ToString().PadLeft(2, '0') + ":"
                                    + dt.Second.ToString().PadLeft(2, '0') + "\n";
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

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

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

        //Class測試 ST

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

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //Class測試
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
        //Class測試 SP

        //最短路徑分析 ST
        static int length = 6;
        static string[] shortedPath = new string[length];
        static int noPath = 2000;
        static int MaxSize = 1000;
        static int[,] G =
         {
             { noPath, noPath, 10, noPath, 30, 100 },
             { noPath, noPath, 5, noPath, noPath, noPath },
             { noPath, noPath, noPath, 50, noPath, noPath },
             { noPath, noPath, noPath, noPath, noPath, 10 },
             { noPath, noPath, noPath, 20, noPath, 60 },
             { noPath, noPath, noPath, noPath, noPath, noPath }
         };
        static string[] PathResult = new string[length];

        static int[] path1 = new int[length];
        static int[,] path2 = new int[length, length];
        static int[] distance2 = new int[length];

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int dist1 = getShortedPath(G, 0, 1, path1);
            richTextBox1.Text += "點0到點5路徑:" + "\n";
            for (int i = 0; i < path1.Length; i++)
            {
                Console.Write(path1[i].ToString() + " ");
            }
            richTextBox1.Text += "長度:" + dist1 + "\n";


            richTextBox1.Text += "\r\n-----------------------------------------\r\n";

            int[] pathdist = getShortedPath(G, 0, path2);
            richTextBox1.Text += "點0到任意點的路徑:" + "\n";
            for (int j = 0; j < pathdist.Length; j++)
            {
                richTextBox1.Text += "點0到" + j + "的路徑:" + "\n";
                for (int i = 0; i < length; i++)
                    richTextBox1.Text += path2[j, i].ToString() + " ";
                richTextBox1.Text += "長度:" + pathdist[j] + "\n";
            }
        }

        //從某一源點出發，找到到某一結點的最短路徑
        static int getShortedPath(int[,] G, int start, int end, int[] path)
        {
            bool[] s = new bool[length]; //表示找到起始結點與當前結點間的最短路徑
            int min;  //最小距離臨時變量
            int curNode = 0; //臨時結點，記錄當前正計算結點
            int[] dist = new int[length];
            int[] prev = new int[length];

            //初始結點信息
            for (int v = 0; v < length; v++)
            {
                s[v] = false;
                dist[v] = G[start, v];
                if (dist[v] > MaxSize)
                    prev[v] = 0;
                else
                    prev[v] = start;
            }
            path[0] = end;
            dist[start] = 0;
            s[start] = true;
            //主循環
            for (int i = 1; i < length; i++)
            {
                min = MaxSize;
                for (int w = 0; w < length; w++)
                {
                    if (!s[w] && dist[w] < min)
                    {
                        curNode = w;
                        min = dist[w];
                    }
                }

                s[curNode] = true;
                for (int j = 0; j < length; j++)
                    if (!s[j] && min + G[curNode, j] < dist[j])
                    {
                        dist[j] = min + G[curNode, j];
                        prev[j] = curNode;
                    }

            }
            //輸出路徑結點
            int e = end, step = 0;
            while (e != start)
            {
                step++;
                path[step] = prev[e];
                e = prev[e];
            }
            for (int i = step; i > step / 2; i--)
            {
                int temp = path[step - i];
                path[step - i] = path[i];
                path[i] = temp;
            }
            return dist[end];
        }

        //從某一源點出發，找到到所有結點的最短路徑
        static int[] getShortedPath(int[,] G, int start, int[,] path)
        {
            int[] PathID = new int[length];//路徑（用編號表示）
            bool[] s = new bool[length]; //表示找到起始結點與當前結點間的最短路徑
            int min;  //最小距離臨時變量
            int curNode = 0; //臨時結點，記錄當前正計算結點
            int[] dist = new int[length];
            int[] prev = new int[length];
            //初始結點信息
            for (int v = 0; v < length; v++)
            {
                s[v] = false;
                dist[v] = G[start, v];
                if (dist[v] > MaxSize)
                    prev[v] = 0;
                else
                    prev[v] = start;
                path[v, 0] = v;
            }

            dist[start] = 0;
            s[start] = true;
            //主循環
            for (int i = 1; i < length; i++)
            {
                min = MaxSize;
                for (int w = 0; w < length; w++)
                {
                    if (!s[w] && dist[w] < min)
                    {
                        curNode = w;
                        min = dist[w];
                    }
                }

                s[curNode] = true;

                for (int j = 0; j < length; j++)
                {
                    if (!s[j] && min + G[curNode, j] < dist[j])
                    {
                        dist[j] = min + G[curNode, j];
                        prev[j] = curNode;
                    }
                }
            }
            //輸出路徑結點
            for (int k = 0; k < length; k++)
            {
                int e = k, step = 0;
                while (e != start)
                {
                    step++;
                    path[k, step] = prev[e];
                    e = prev[e];
                }
                for (int i = step; i > step / 2; i--)
                {
                    int temp = path[k, step - i];
                    path[k, step - i] = path[k, i];
                    path[k, i] = temp;
                }
            }
            return dist;
        }
        //最短路徑分析 SP

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //(Console)各種數據格式的輸出

            Console.WriteLine("各種數據格式的輸出：");
            // Console.WriteLine 中各種數據格式的輸出
            Console.WriteLine("{0, 8 :C}", 2);     // $2.00
            Console.WriteLine("{0, 8 :C3}", 2);    // $2.000
            Console.WriteLine("{0 :D3}", 2);       // 002
            Console.WriteLine("{0 :E}", 2);        // 2.000000E+000
            Console.WriteLine("{0 :G}", 2);        // 2
            Console.WriteLine("{0 :N}", 2500000.00);    // 2,500,00.00
            Console.WriteLine("{0 :x4}", 12);      // 000c
            Console.WriteLine("{0, 2 :x}", 12);    //  c
            Console.WriteLine("{0 :000.000}", 12.23);   // 012.230
            Console.WriteLine("{0 :r}", 15.62);    // 15.62
            Console.WriteLine("{0 :d}", System.DateTime.Now);    // 2012-3-27
            Console.WriteLine("{0 :D}", System.DateTime.Now);    // 2012年3月27日

            Console.WriteLine("{0 :t}", System.DateTime.Now);    // 11:43
            Console.WriteLine("{0 :T}", System.DateTime.Now);    // 11:43:34

            Console.WriteLine("{0 :f}", System.DateTime.Now);    // 2012年3月27日 11:43
            Console.WriteLine("{0 :F}", System.DateTime.Now);    // 2012年3月27日 11:43:34

            Console.WriteLine("{0 :g}", System.DateTime.Now);    // 2012-3-27 11:43
            Console.WriteLine("{0 :G}", System.DateTime.Now);    // 2012-3-27 11:43:34

            Console.WriteLine("{0 :M}", System.DateTime.Now);    // 3月27日
            Console.WriteLine("{0 :r}", System.DateTime.Now);// Tue, 27 Mar 2012 11:43:34 GMT
            Console.WriteLine("{0 :s}", System.DateTime.Now);    // 2012-03-27T11:43:34
            Console.WriteLine("{0 :u}", System.DateTime.Now);    // 2012-03-27 11:43:34Z
            Console.WriteLine("{0 :U}", System.DateTime.Now);    // 2012年3月27日 3:43:34
            Console.WriteLine("{0 :Y}", System.DateTime.Now);    // 2012年3月

            Console.WriteLine("{0 :dd}", System.DateTime.Now);   // 27
            Console.WriteLine("{0 :ddd}", System.DateTime.Now);  // 二
            Console.WriteLine("{0 :dddd}", System.DateTime.Now); // 星期二

            Console.WriteLine("{0 :f}", System.DateTime.Now);    // 2012年3月27日 11:46
            Console.WriteLine("{0 :ff}", System.DateTime.Now);   // 18
            Console.WriteLine("{0 :fff}", System.DateTime.Now);  // 187
            Console.WriteLine("{0 :ffff}", System.DateTime.Now); // 1875
            Console.WriteLine("{0 :fffff}", System.DateTime.Now); // 18750

            Console.WriteLine("{0 :gg}", System.DateTime.Now);   // 公元
            Console.WriteLine("{0 :ggg}", System.DateTime.Now);  // 公元
            Console.WriteLine("{0 :gggg}", System.DateTime.Now); // 公元
            Console.WriteLine("{0 :ggggg}", System.DateTime.Now);     // 公元
            Console.WriteLine("{0 :gggggg}", System.DateTime.Now);    // 公元

            Console.WriteLine("{0 :hh}", System.DateTime.Now);   // 11
            Console.WriteLine("{0 :HH}", System.DateTime.Now);   // 11

            Console.WriteLine("{0 :mm}", System.DateTime.Now);   // 50
            Console.WriteLine("{0 :MM}", System.DateTime.Now);   // 03

            Console.WriteLine("{0 :MMM}", System.DateTime.Now);  // 三月
            Console.WriteLine("{0 :MMMM}", System.DateTime.Now); // 三月

            Console.WriteLine("{0 :ss}", System.DateTime.Now);   // 43
            Console.WriteLine("{0 :tt}", System.DateTime.Now);   // 上午

            Console.WriteLine("{0 :yy}", System.DateTime.Now);   // 12
            Console.WriteLine("{0 :yyyy}", System.DateTime.Now); // 2012
            Console.WriteLine("{0 :zz}", System.DateTime.Now);   // +08
            Console.WriteLine("{0 :zzz}", System.DateTime.Now);  // +08:00
            Console.WriteLine("{0 :hh:mm:ss}", System.DateTime.Now);  // 11：43：34
            Console.WriteLine("{0 :dd/MM/yyyy}", System.DateTime.Now); // 27-03-2012

            // TODO: Implement Functionality Here

            Console.Write("Press any key to continue . . . ");

        }

        private void button13_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取當前行號
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
            richTextBox1.Text += "當前行號 : " + GetLineNum().ToString() + "\n";
        }

        //獲取當前行號
        public static int GetLineNum()
        {
            System.Diagnostics.StackTrace st = new System.Diagnostics.StackTrace(1, true);
            return st.GetFrame(0).GetFileLineNumber();
        }


        private void button14_Click(object sender, EventArgs e)
        {
        }
        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //易經 六十四卦
            char[] word = new char[64];
            word = GetChars();
            int i;
            for (i = 0; i < 64; i++)
            {
                richTextBox1.Text += word[i].ToString() + "    ";
            }
        }

        public static char[] GetChars()
        {
            List<char> chars = new List<char>();
            for (int i = 19904; i <= 19967; i++)
            {
                chars.Add((char)i);
            }
            return chars.ToArray();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //生成隨機字符串
            string random_str = RandomStringGenerator.GetRandomString();
            richTextBox1.Text += random_str + "\n";
        }

        /// <summary> 
        /// 生成隨機字符串
        /// </summary> 
        private class RandomStringGenerator
        {
            static readonly Random r = new Random();
            const string _chars = "0123456789";
            public static string GetRandomString()
            {
                char[] buffer = new char[5];
                for (int i = 0; i < 5; i++)
                {
                    buffer[i] = _chars[r.Next(_chars.Length)];
                }
                return new string(buffer);
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            foreach (Process p in Process.GetProcesses())
            {
                //Console.Write(p.ProcessName);
                //Console.Write("----");
                //Console.WriteLine(GetProcessUserName(p.Id));

                richTextBox1.Text += p.ProcessName + "\t" + GetProcessUserName(p.Id) + "\n";
            }
        }

        private static string GetProcessUserName(int pID)
        {
            string text1 = null;
            SelectQuery query1 = new SelectQuery("Select * from Win32_Process WHERE processID=" + pID);
            ManagementObjectSearcher searcher1 = new ManagementObjectSearcher(query1);
            try
            {
                foreach (ManagementObject disk in searcher1.Get())
                {
                    ManagementBaseObject inPar = null;
                    ManagementBaseObject outPar = null;
                    inPar = disk.GetMethodParameters("GetOwner");
                    outPar = disk.InvokeMethod("GetOwner", inPar, null);
                    text1 = outPar["User"].ToString();
                    break;
                }
            }
            catch
            {
                text1 = "SYSTEM";
            }
            return text1;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //字串轉拜列
            richTextBox1.Text += "字串 轉 拜列\n";

            string str = "this is a lion-mouse.";

            richTextBox1.Text += "字串 : " + str + "\n";

            byte[] byte_array = Encoding.ASCII.GetBytes(str);

            int len = byte_array.Length;
            richTextBox1.Text += "拜列長度 : " + len.ToString() + "\n";
            richTextBox1.Text += "拜列內容 :\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (char)byte_array[i] + "\t" + byte_array[i].ToString("X2") + "\n";

            }

        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //split
            string str = "this-is-a-lion-mouse";
            string[] word = str.Split('-');
            richTextBox1.Text += "原字串: " + str + "\n";
            richTextBox1.Text += "分割後, len = " + word.Length.ToString() + ", 內容:\n";
            foreach (string s in word)
            {
                richTextBox1.Text += s + "\n";
            }

        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //連接符 與 佔位符
            string str1 = "lion";
            string str2 = "mouse";
            string m = String.Format("{0}", str1);   //字符串格式輸出
            string n = String.Format("{0}", str2);

            richTextBox1.Text += "str = " + m + "-" + n + "\n";     //用“+”連接符
        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //動態創建按鈕和事件

            int i = 0;
            for (i = 0; i < 10; i++)
            {
                Button btn = new Button();//創建一個新的按鈕
                btn.Name = "button" + i.ToString();//這是我用來區別各個按鈕的辦法
                btn.Text = "button" + i.ToString();
                btn.Size = new Size(80, 45);
                Point p = new Point(400, 13 + i * 50);//創建一個坐標,用來給新的按鈕定位
                btn.Location = p;//把按鈕的位置與剛創建的坐標綁定在一起

                this.richTextBox1.Controls.Add(btn);    //向 某控件 中添加此按鈕

                //動態添加控件的事件,語句:
                //Control.Command += new CommandEventHandler(this.EventFun);
                btn.Click += new System.EventHandler(btn_click);//將按鈕的方法綁定到按鈕的單擊事件中b.Click是按鈕的單擊事件
            }
        }

        private void btn_click(object sender, System.EventArgs e)
        {
            Button b1 = (Button)sender;//將觸發此事件的對象轉換為該Button對象

            richTextBox1.Text += "你按了 " + b1.Name + "\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取系統字體
            InstalledFontCollection fc = new InstalledFontCollection();
            foreach (FontFamily font in fc.Families)
            {
                richTextBox1.Text += "get font : " + font.Name + "\n";
            }
        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //獲取系統預定義顏色
            Array colors = System.Enum.GetValues(typeof(KnownColor));
            foreach (object colorName in colors)
            {
                richTextBox1.Text += "get color : " + colorName.ToString() + "\n";
            }
        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //2007年4月24日
            richTextBox1.Text += DateTime.Now.ToString("D") + "\n";
            //2007-4-24
            richTextBox1.Text += DateTime.Now.ToString("d") + "\n";

            //2007年4月24日 16:30:15
            richTextBox1.Text += DateTime.Now.ToString("F") + "\n";
            //2007年4月24日 16:30
            richTextBox1.Text += DateTime.Now.ToString("f") + "\n";

            //2007-4-24 16:30:15
            richTextBox1.Text += DateTime.Now.ToString("G") + "\n";
            //2007-4-24 16:30
            richTextBox1.Text += DateTime.Now.ToString("g") + "\n";

            //16:30:15
            richTextBox1.Text += DateTime.Now.ToString("T") + "\n";
            //16:30
            richTextBox1.Text += DateTime.Now.ToString("t") + "\n";

            //2007年4月24日 8:30:15
            richTextBox1.Text += DateTime.Now.ToString("U") + "\n";
            //2007-04-24 16:30:15Z
            richTextBox1.Text += DateTime.Now.ToString("u") + "\n";

            //4月24日
            richTextBox1.Text += DateTime.Now.ToString("m") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("M") + "\n";
            //Tue, 24 Apr 2007 16:30:15 GMT
            richTextBox1.Text += DateTime.Now.ToString("r") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("R") + "\n";
            //2007年4月 
            richTextBox1.Text += DateTime.Now.ToString("y") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("Y") + "\n";
            //2007-04-24T15:52:19.1562500+08:00
            richTextBox1.Text += DateTime.Now.ToString("o") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("O") + "\n";
            //2007-04-24T16:30:15
            richTextBox1.Text += DateTime.Now.ToString("s") + "\n";
            //2007-04-24 15:52:19
            richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd HH：mm：ss：ffff") + "\n";
            //2007年04月24 15時56分48秒
            richTextBox1.Text += DateTime.Now.ToString("yyyy年MM月dd HH時mm分ss秒") + "\n";

            //星期二, 四月 24 2007
            richTextBox1.Text += DateTime.Now.ToString("dddd, MMMM dd yyyy") + "\n";
            //二, 四月 24 '07
            richTextBox1.Text += DateTime.Now.ToString("ddd, MMM d \"'\"yy") + "\n";
            //星期二, 四月 24
            richTextBox1.Text += DateTime.Now.ToString("dddd, MMMM dd") + "\n";
            //4-07
            richTextBox1.Text += DateTime.Now.ToString("M/yy") + "\n";
            //24-04-07
            richTextBox1.Text += DateTime.Now.ToString("dd-MM-yy") + "\n";


        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            richTextBox1.Text += "111\t" + 12345.ToString("n") + "\n"; //生成 12,345.00
            richTextBox1.Text += "111\t" + 12345.ToString("C") + "\n"; //生成 ￥12,345.00
            richTextBox1.Text += "111\t" + 12345.ToString("e") + "\n"; //生成 1.234500e+004
            richTextBox1.Text += "111\t" + 12345.ToString("f4") + "\n"; //生成 12345.0000
            richTextBox1.Text += "111\t" + 12345.ToString("x") + "\n"; //生成 3039 (16進制)
            richTextBox1.Text += "111\t" + 12345.ToString("p") + "\n"; //生成 1,234,500
        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //陽歷轉換成陰歷的類



        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
/*            
//時間比較
use "DateTime.Compare" static method

DateTime.Compare( dt1, dt2 ) > 0 : dt1 > dt2
DateTime.Compare( dt1, dt2 ) == 0 : dt1 == dt2
DateTime.Compare( dt1, dt2 ) < 0 : dt1 < dt2
       

DateTime值類型代表了一個從公元0001年1月1日0點0分0秒到公元9999年12月31日23點59分59秒之間的具體日期時刻。
因此，你可以用DateTime值類型來描述任何在想象范圍之內的時間。
*/
            DateTime dt1 = new DateTime(2006, 3, 11, 9, 15, 20);
            DateTime dt2 = DateTime.Now;
            string diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "diff = " + diff + "\n";

            dt1 = new DateTime(1939, 9, 1);
            dt2 = new DateTime(1945, 9, 2);
            diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "diff = " + diff + "\n";
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
    }

    public class LunarDate
    {
        public const int MAX_YEAR = 2011;
        public const int MIN_YEAR = 1900;

        static readonly string[] lookupTable = new string[] 
    { 
        "0100101101101080131", "0100101011100000219", "1010010101110000208",
        "0101001001101050129", "1101001001100000216", "1101100101010000204",
        "0110101010101040125", "0101011010100000213", "1001101011010000202", 
        "0100101011101020122", "0100101011100000210", "1010010011011060130",
        "1010010011010000218", "1101001001010000206", "1101010101001050126",
        "1011010101010000214", "0101011010100000204", "1001011011010020123", 
        "1001010110110000211", "0100100110111070201", "0100100110110000220", 
        "1010010010110000208", "1011001001011050128", "0110101001010000216", 
        "0110110101000000205", "1010110110101040124", "0010101101100000213", 
        "1001010101110000202", "0100100101111020123", "0100100101110000210", 
        "0110010010110060130", "1101010010100000217", "1110101001010000206", 
        "0110110101001050126", "0101101011010000214", "0010101101100000204", 
        "1001001101110030124", "1001001011100000211", "1100100101101070131", 
        "1100100101010000219", "1101010010100000208", "1101101001010060127",
        "1011010101010000215", "0101011010100000205", "1010101011011040125", 
        "0010010111010000213", "1001001011010000202", "1100100101011020122", 
        "1010100101010000210", "1011010010101070129", "0110110010100000217", 
        "1011010101010000206", "0101010110101050127", "0100110110100000214", 
        "1010010110110000203", "0101001010111030124", "0101001010110000212", 
        "1010100101010080131", "1110100101010000218", "0110101010100000208", 
        "1010110101010060128", "1010101101010000215", "0100101101100000205",
        "1010010101110040125", "1010010101110000213", "0101001001100000202",
        "1110100100110030121", "1101100101010000209", "0101101010101070130",
        "0101011010100000217", "1001011011010000206", "0100101011101050127",
        "0100101011010000215", "1010010011010000203", "1101001001101040123",
        "1101001001010000211", "1101010100101080131", "1011010101000000218",
        "1011011010100000207", "1001011011010060128", "1001010110110000216", 
        "0100100110110000205", "1010010010111040125", "1010010010110000213", 
        "1011001001011100202", "0110101001010000220", "0110110101000000209", 
        "1010110110101060129", "1010101101100000217", "1001001101110000206",
        "0100100101111050127", "0100100101110000215", "0110010010110000204", 
        "0110101001010030123", "1110101001010000210", "0110101100101080131",
        "0101101011000000219", "1010101101100000207", "1001001101101050128", 
        "1001001011100000216", "1100100101100000205", "1101010010101040124",
        "1101010010100000212", "1101101001010000201", "0101101010101020122",
        "0101011010100000209", "1010101011011070129", "0010010111010000218",
        "1001001011010000207", "1100100101011050126", "1010100101010000214",
        "1011010010100000214" 
    };

        /**/
        /// <summary>十二生肖</summary>
        static readonly string animalsTable = "鼠牛虎兔龍蛇馬羊猴雞狗豬";
        static readonly string monthsTable = "正二三四五六七八九十寒臘";
        static readonly string daysTable = "初一初二初三初四初五初六初七初八初九初十十一十二十三十四十五十六十七十八十九二十廿一廿二廿三廿四廿五廿六廿七廿八廿九三十";

        /**/
        /// <summary>天干地支</summary>
        static readonly string[] chineseEra;
        static LunarDate()
        {
            string sky = "甲乙丙丁戊已庚辛壬癸";        //天干
            string earth = "子丑寅卯辰巳午未申酉戌亥";  //地支
            chineseEra = new string[60];
            for (int i = 0; i < 60; i++)
                chineseEra[i] = sky.Substring(i % 10, 1) + earth.Substring(i % 12, 1);
        }

        public LunarDate(int year, int month, int day)
        {
            if ((year < MIN_YEAR) || (year > MAX_YEAR))
                throw new ArgumentOutOfRangeException("year to0 large or too small");

            // 計算農歷年
            int lunarYear;
            int lunarMonth;
            int lunarDay;

            lunarYear = year;
            // 農歷新年月份
            lunarMonth = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(15, 2)));
            // 農歷新年日子
            lunarDay = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(17, 2))); ;
            if ((month < lunarMonth) || ((month == lunarMonth) && (day < lunarDay)))
            {
                lunarYear--;
                // 農歷新年月份
                lunarMonth = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(15, 2)));
                // 農歷新年日子
                lunarDay = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(17, 2))); ;
            }

            // 計算農歷月
            DateTime date = new DateTime(year, month, day);
            DateTime lunarDate = new DateTime(lunarYear, lunarMonth, lunarDay);
            TimeSpan span = date - lunarDate;
            int dayCount = span.Days;
            lunarMonth = 1;
            lunarDay = 1;
            bool leapMonth = false; //閏月
            for (int i = 0; i < dayCount; i++)
            {
                lunarDay++;
                if (lunarDay == 30 + Convert.ToInt32(lookupTable[lunarYear - MIN_YEAR].Substring(lunarMonth - 1, 1)) ||
                (leapMonth == true && (lunarDay == 30 + Convert.ToInt32(lookupTable[lunarYear - MIN_YEAR].Substring(12, 1)))))
                {
                    if (
                        (leapMonth == false) &&
                        (lunarMonth == Convert.ToInt32(lookupTable[lunarYear - MIN_YEAR].Substring(13, 2)))
                        )
                    {
                        leapMonth = true;
                    }
                    else
                    {
                        leapMonth = false;
                        lunarMonth++;
                    }
                    lunarDay = 1;
                }
                else
                {
                }
            }

            // 計算農歷日
            lunarDayText = daysTable.Substring((lunarDay - 1) * 2, 2);
            // 計算農歷月
            lunarMonthText = monthsTable.Substring(lunarMonth - 1, 1) + "月";
            if (leapMonth == true) lunarMonthText = "閏" + lunarMonthText;
            // 農歷年
            lunarYearText = Convert.ToString(lunarYear, 10) + "年";
            // 計算天干地支
            chineseEarText = chineseEra[(lunarYear - 4) % 60];
            // 計算生肖
            aminalsText = animalsTable.Substring((lunarYear - 4) % 12, 1);
        }

        //農歷日
        private string lunarDayText;
        public string LunarDay { get { return this.lunarDayText; } }

        //農歷月
        private string lunarMonthText;
        public string LunarMonth { get { return this.lunarMonthText; } }

        //農歷年
        private string lunarYearText;
        public string LunarYear { get { return this.lunarYearText; } }

        //天干地支
        private string chineseEarText;
        public string chineseEar { get { return this.chineseEarText; } }

        //生肖
        private string aminalsText;
        public string Aminals { get { return this.aminalsText; } }

        public override string ToString()
        {
            return aminalsText + "," + chineseEarText + "," + lunarYearText + lunarMonthText + lunarDayText;
        }
    }
}


