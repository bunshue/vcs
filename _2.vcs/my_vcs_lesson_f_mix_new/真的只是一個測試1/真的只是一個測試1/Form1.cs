using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;  //for RegistryKey

using System.IO;    //for StreamReader

using System.Net;   //for HttpWebRequest HttpWebResponse

using System.Collections;   //for DictionaryEntry
using System.Drawing.Imaging;   //for ImageFormat

using System.Text.RegularExpressions;

using System.Diagnostics;	//for Stopwatch

using System.Runtime.InteropServices;

namespace 真的只是一個測試1
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
            dx = 165;
            dy = 65;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
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

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            //分出 時:分:秒 再組合

            DateTime dt = DateTime.Now;

            richTextBox1.Text += dt.Hour.ToString().PadLeft(2, '0') + ":"
                                    + dt.Minute.ToString().PadLeft(2, '0') + ":"
                                    + dt.Second.ToString().PadLeft(2, '0') + "\n";
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

        List<double[]> pts = new List<double[]>();    //二維List for double array
        int g = 10;


        //二維List for double
        private void button20_Click(object sender, EventArgs e)
        {
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
        private void button21_Click(object sender, EventArgs e)
        {
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

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
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

        //ENUM測試 ST

        //默認從0開始：分別為0，1，2，3
        enum Level1
        {
            Employee,
            Manager,
            Boss,
            BigBoss,
        }

        //未指定的列舉名的值將依著最后一個指定值向后依次遞增（注意是最后一個指定值）
        //列舉中定義的可以自定義整數值
        enum Level2
        {
            Employee = 100,
            Manager,
            Boss,
            BigBoss,
        }
        //結果為100，101，102，103

        //列舉中定義的整數值可以部分預設
        enum Level3
        {
            Employee = 100,
            Manager,
            Boss = 102,
            BigBoss,
        }
        //Manager自動為101，BigBoss自動為103

        enum Level4
        {
            Employee = 100,
            Manager,
            Boss = 101,
            BigBoss,
        }
        //結果為100，101，101，102，有兩個101也是合法的
        //但不能有兩個Manager，即enum中的名稱不能重復，

        //位元位式用法

        enum Skill
        {
            Drive = 1,  //二進制  0001
            Cook = 2,  //二進制  0010
            Program = 4, //二進制  0100
            Teach = 8, //二進制  1000
        }

        class Person
        {
            public int ID { get; set; }
            public string Name { get; set; }
            public Level1 Level { get; set; }
            public Skill Skill { get; set; }
        }

        private void button27_Click(object sender, EventArgs e)
        {
            Person person1 = new Person();
            person1.Level = Level1.Employee;

            richTextBox1.Text += "result : " + ((int)Level1.Boss).ToString() + "\n";
            //結果為2

            Person person2 = new Person();
            person2.Skill = Skill.Drive | Skill.Cook | Skill.Program | Skill.Teach; //二進制  1111，十進制的15 //結果為15

            richTextBox1.Text += "Skill : " + ((int)person2.Skill).ToString() + "\n";
            richTextBox1.Text += "Skill a : " + ((person2.Skill & Skill.Cook) > 0).ToString() + "\n";
            richTextBox1.Text += "Skill b : " + ((person2.Skill & Skill.Cook) == Skill.Cook).ToString() + "\n";

            Console.WriteLine(person2.Skill);
            Console.WriteLine((person2.Skill & Skill.Cook) > 0); //結果為True，（1111 & 0010 = 0010）
            Console.WriteLine((person2.Skill & Skill.Cook) == Skill.Cook); //結果為True



        }

        //ENUM測試 SP


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

        private void button28_Click(object sender, EventArgs e)
        {
            P obj = new P();
            obj.Name = "david wang";            //使用到set
            Console.WriteLine(obj.Name);        //使用到get

        }


        //class test SP
    }
}

