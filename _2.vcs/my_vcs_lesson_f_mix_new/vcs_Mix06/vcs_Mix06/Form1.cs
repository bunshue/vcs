﻿using System;
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

using System.Collections;   //for Stack

namespace vcs_Mix06
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
            /*
            堆栈（Stack）代表了一个后进先出的对象集合。
            当您需要对各项进行后进先出的访问时，则使用堆栈。
            当您在列表中添加一项，称为推入元素，
            当您从列表中移除一项时，称为弹出元素。


            属性	描述
            Count	获取 Stack 中包含的元素个数。

            下表列出了 Stack 类的一些常用的 方法：
            序号	方法名 & 描述
            1	public virtual void Clear();
            从 Stack 中移除所有的元素。
            2	public virtual bool Contains( object obj );
            判断某个元素是否在 Stack 中。
            3	public virtual object Peek();
            返回在 Stack 的顶部的对象，但不移除它。
            4	public virtual object Pop();
            移除并返回在 Stack 的顶部的对象。
            5	public virtual void Push( object obj );
            向 Stack 的顶部添加一个对象。
            6	public virtual object[] ToArray();
            复制 Stack 到一个新的数组中。
            */


            Stack st = new Stack();

            st.Push('A');
            st.Push('M');
            st.Push('G');
            st.Push('W');

            Console.WriteLine("Current stack: ");
            foreach (char c in st)
            {
                Console.Write(c + " ");
            }
            Console.WriteLine();

            st.Push('V');
            st.Push('H');
            Console.WriteLine("The next poppable value in stack: {0}",
            st.Peek());
            Console.WriteLine("Current stack: ");
            foreach (char c in st)
            {
                Console.Write(c + " ");
            }
            Console.WriteLine();

            Console.WriteLine("Removing values ");
            st.Pop();
            st.Pop();
            st.Pop();

            Console.WriteLine("Current stack: ");
            foreach (char c in st)
            {
                Console.Write(c + " ");
            }
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

            DateTime _d = DateTime.Now;
            LunarDate ld = new LunarDate(_d);
            string result = "";
            result += "干支年：" + ld.LunarYear + "\n";
            result += "生肖：" + ld.Animal + "\n";
            result += "月：" + ld.LunarMonth + "\n";
            result += "日：" + ld.LunarDay + "\n";
            result += "节气：" + ld.SolarTerm + "\n";
            result += "数字农历年：" + ld.Year + "月" + ld.Month + "日" + ld.Day + "\n";

            richTextBox1.Text += result + "\n";

            //DateTime _d = DateTime.Now;
            LunarDateClass ldc = new LunarDateClass(_d);

            result = "";
            result += "干支年：" + ldc.LunarYear + "\n";
            result += "生肖：" + ldc.Animal + "\n";
            result += "月：" + ldc.LunarMonth + "\n";
            result += "日：" + ldc.LunarDay + "\n";
            result += "节气：" + ldc.SolarTerm + "\n";
            //ldc.LunarDate 返回 LunarDate对象。。
            result += "数字农历年：" + ldc.LunarDate.Year + "月" + ldc.LunarDate.Month + "日" + ldc.LunarDate.Day + "\n";

            richTextBox1.Text += result + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

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

        }

        private void button14_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button15_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button16_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button17_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button18_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button19_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button20_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button21_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button22_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button23_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button24_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button25_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button26_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button27_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button28_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

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

    }

    #region LunarDate

    public class LunarDateClass
    {
        private const ushort START_YEAR = 1901;
        private const ushort END_YEAR = 2050;
        private DateTime m_Date = DateTime.MinValue;
        private LunarDate m_LunarDate = null;
        private string m_LunarYear = "", m_LunarMonth = "", m_LunarDay = "";
        private string m_Animal = "", m_Constellation = "", m_SolarTerm = "";

        /// <summary>始化农历类。</summary>
        public LunarDateClass()
        {
            this.Date = DateTime.Today;
        }


        /// <summary>以公历日期初始化农历类。</summary>
        /// <param name="dt">初始化公历日期。要查询的日期。</param>
        public LunarDateClass(DateTime dt)
        {
            this.Date = dt.Date;
        }

        /// <summary>初始化公历日期。要查询的日期。</summary>
        public DateTime Date
        {
            get { return m_Date; }
            set
            {
                this.m_Animal = "";
                this.m_Constellation = "";
                this.m_LunarDate = null;
                this.m_LunarDay = "";
                this.m_LunarMonth = "";
                this.m_LunarYear = "";
                this.m_SolarTerm = "";
                m_Date = value;
            }
        }

        #region LunarDateClassData

        /// <summary>星座名称。</summary>
        private string[] ConstellationName =
   {
    "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
    "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座"
   };

        /// <summary>节气名称。</summary>
        private string[] LunarHolDayName =
   {
    "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
    "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑",
    "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"
   };

        /// <summary>
        /// 数组gLunarDay存入阴历1901年到2050年每年中的月天数信息，
        /// 阴历每月只能是29或30天，一年用12（或13）个二进制位表示，
        /// 对应位为1表30天，否则为29天.
        /// 测试数据只有1901.1.1 --2050.12.31
        /// </summary>
        private int[] gLunarMonthDay = {
 0x4ae0, 0xa570, 0x5268, 0xd260, 0xd950, 0x6aa8, 0x56a0, 0x9ad0, 0x4ae8, 0x4ae0, //1910
 0xa4d8, 0xa4d0, 0xd250, 0xd548, 0xb550, 0x56a0, 0x96d0, 0x95b0, 0x49b8, 0x49b0, //1920
 0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada8, 0x2b60, 0x9570, 0x4978, 0x4970, 0x64b0, //1930
 0xd4a0, 0xea50, 0x6d48, 0x5ad0, 0x2b60, 0x9370, 0x92e0, 0xc968, 0xc950, 0xd4a0, //1940
 0xda50, 0xb550, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950, 0xb4a8, 0x6ca0, //1950
 0xb550, 0x55a8, 0x4da0, 0xa5b0, 0x52b8, 0x52b0, 0xa950, 0xe950, 0x6aa0, 0xad50, //1960
 0xab50, 0x4b60, 0xa570, 0xa570, 0x5260, 0xe930, 0xd950, 0x5aa8, 0x56a0, 0x96d0, //1970
 0x4ae8, 0x4ad0, 0xa4d0, 0xd268, 0xd250, 0xd528, 0xb540, 0xb6a0, 0x96d0, 0x95b0, //1980
 0x49b0, 0xa4b8, 0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada0, 0xab60, 0x9370, 0x4978, //1990
 0x4970, 0x64b0, 0x6a50, 0xea50, 0x6b28, 0x5ac0, 0xab60, 0x9368, 0x92e0, 0xc960, //2000
 0xd4a8, 0xd4a0, 0xda50, 0x5aa8, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950, //2010
 0xb4a0, 0xb550, 0xb550, 0x55a8, 0x4ba0, 0xa5b0, 0x52b8, 0x52b0, 0xa930, 0x74a8, //2020
 0x6aa0, 0xad50, 0x4da8, 0x4b60, 0x9570, 0xa4e0, 0xd260, 0xe930, 0xd530, 0x5aa0, //2030
 0x6b50, 0x96d0, 0x4ae8, 0x4ad0, 0xa4d0, 0xd258, 0xd250, 0xd520, 0xdaa0, 0xb5a0, //2040
 0x56d0, 0x4ad8, 0x49b0, 0xa4b8, 0xa4b0, 0xaa50, 0xb528, 0x6d20, 0xada0, 0x55b0 //2050
            };

        /// <summary>数组gLanarMonth存放阴历1901年到2050年闰月的月份，如没有则为0，每字节存两年</summary>
        private byte[] gLunarMonth = {
 0x00, 0x50, 0x04, 0x00, 0x20, //1910
 0x60, 0x05, 0x00, 0x20, 0x70, //1920
 0x05, 0x00, 0x40, 0x02, 0x06, //1930
 0x00, 0x50, 0x03, 0x07, 0x00, //1940
 0x60, 0x04, 0x00, 0x20, 0x70, //1950
 0x05, 0x00, 0x30, 0x80, 0x06, //1960
 0x00, 0x40, 0x03, 0x07, 0x00, //1970
 0x50, 0x04, 0x08, 0x00, 0x60, //1980
 0x04, 0x0a, 0x00, 0x60, 0x05, //1990
 0x00, 0x30, 0x80, 0x05, 0x00, //2000
 0x40, 0x02, 0x07, 0x00, 0x50, //2010
 0x04, 0x09, 0x00, 0x60, 0x04, //2020
 0x00, 0x20, 0x60, 0x05, 0x00, //2030
 0x30, 0xb0, 0x06, 0x00, 0x50, //2040
 0x02, 0x07, 0x00, 0x50, 0x03 //2050
          };


        //数组gLanarHoliDay存放每年的二十四节气对应的阳历日期

        //每年的二十四节气对应的阳历日期几乎固定，平均分布于十二个月中
        // 1月 2月 3月 4月 5月 6月
        //小寒 大寒 立春 雨水 惊蛰 春分 清明 谷雨 立夏 小满 芒种 夏至
        // 7月 8月 9月 10月 11月 12月
        //小暑 大暑 立秋 处暑 白露 秋分 寒露 霜降 立冬 小雪 大雪 冬至
        //*********************************************************************************
        // 节气无任何确定规律,所以只好存表,要节省空间,所以....
        //**********************************************************************************}
        //数据格式说明:
        //如1901年的节气为
        // 1月 2月 3月 4月 5月 6月 7月 8月 9月 10月 11月 12月
        // 6, 21, 4, 19, 6, 21, 5, 21, 6,22, 6,22, 8, 23, 8, 24, 8, 24, 8, 24, 8, 23, 8, 22
        // 9, 6, 11,4, 9, 6, 10,6, 9,7, 9,7, 7, 8, 7, 9, 7, 9, 7, 9, 7, 8, 7, 15
        //上面第一行数据为每月节气对应日期,15减去每月第一个节气,每月第二个节气减去15得第二行
        // 这样每月两个节气对应数据都小于16,每月用一个字节存放,高位存放第一个节气数据,低位存放
        //第二个节气的数据,可得下表
        private byte[] gLunarHolDay = {
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1901
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1902
  0x96, 0xA5, 0x87, 0x96, 0x87, 0x87, 0x79, 0x69, 0x69, 0x69, 0x78, 0x78, //1903
  0x86, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x78, 0x87, //1904
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1905
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1906
  0x96, 0xA5, 0x87, 0x96, 0x87, 0x87, 0x79, 0x69, 0x69, 0x69, 0x78, 0x78, //1907
  0x86, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1908
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1909
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1910
  0x96, 0xA5, 0x87, 0x96, 0x87, 0x87, 0x79, 0x69, 0x69, 0x69, 0x78, 0x78, //1911
  0x86, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1912
  0x95, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1913
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1914
  0x96, 0xA5, 0x97, 0x96, 0x97, 0x87, 0x79, 0x79, 0x69, 0x69, 0x78, 0x78, //1915
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1916
  0x95, 0xB4, 0x96, 0xA6, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x87, //1917
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x77, //1918
  0x96, 0xA5, 0x97, 0x96, 0x97, 0x87, 0x79, 0x79, 0x69, 0x69, 0x78, 0x78, //1919
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1920
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x87, //1921
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x77, //1922
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x69, 0x69, 0x78, 0x78, //1923
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1924
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x87, //1925
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1926
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1927
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1928
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1929
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1930
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1931
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1932
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1933
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1934
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1935
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1936
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1937
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1938
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1939
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1940
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1941
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1942
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1943
  0x96, 0xA5, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1944
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1945
  0x95, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1946
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1947
  0x96, 0xA5, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1948
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x79, 0x78, 0x79, 0x77, 0x87, //1949
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1950
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1951
  0x96, 0xA5, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1952
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1953
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x68, 0x78, 0x87, //1954
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1955
  0x96, 0xA5, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1956
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1957
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1958
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1959
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1960
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1961
  0x96, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1962
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1963
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1964
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1965
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1966
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1967
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1968
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1969
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1970
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1971
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1972
  0xA5, 0xB5, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1973
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1974
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1975
  0x96, 0xA4, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x89, 0x88, 0x78, 0x87, 0x87, //1976
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1977
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x78, 0x87, //1978
  0x96, 0xB4, 0x96, 0xA6, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1979
  0x96, 0xA4, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1980
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x77, 0x87, //1981
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1982
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1983
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //1984
  0xA5, 0xB4, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1985
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1986
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x79, 0x78, 0x69, 0x78, 0x87, //1987
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //1988
  0xA5, 0xB4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1989
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1990
  0x95, 0xB4, 0x96, 0xA5, 0x86, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1991
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //1992
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1993
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1994
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x76, 0x78, 0x69, 0x78, 0x87, //1995
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //1996
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1997
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1998
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1999
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2000
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2001
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //2002
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //2003
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2004
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2005
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2006
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //2007
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2008
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2009
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2010
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x78, 0x87, //2011
  0x96, 0xB4, 0xA5, 0xB5, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2012
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //2013
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2014
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //2015
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2016
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //2017
  0xA5, 0xB4, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2018
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //2019
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x86, //2020
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2021
  0xA5, 0xB4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2022
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //2023
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2024
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2025
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2026
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //2027
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2028
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2029
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2030
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //2031
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2032
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x86, //2033
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x78, 0x88, 0x78, 0x87, 0x87, //2034
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2035
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2036
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2037
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2038
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2039
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2040
  0xA5, 0xC3, 0xA5, 0xB5, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2041
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2042
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2043
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x88, 0x87, 0x96, //2044
  0xA5, 0xC3, 0xA5, 0xB4, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2045
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //2046
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2047
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA5, 0x97, 0x87, 0x87, 0x88, 0x86, 0x96, //2048
  0xA4, 0xC3, 0xA5, 0xA5, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x86, //2049
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x78, 0x78, 0x87, 0x87 //2050
           };

        #endregion

        #region Core

        /// <summary>
        /// 取得指定阴历年的阴历闰月月份。
        /// </summary>
        /// <param name="iLunarYear">年份。</param>
        /// <returns>返回指定年的闰月月份。</returns>
        private int GetLeapMonth(ushort iLunarYear)
        {
            byte Flag;
            if (iLunarYear < START_YEAR || iLunarYear > END_YEAR)
            {
                return 0;
            }

            Flag = gLunarMonth[(iLunarYear - START_YEAR) / 2];
            if ((iLunarYear - START_YEAR) % 2 == 0)
            {
                return Flag >> 4;
            }
            else
            {
                return Flag & 0x0F;
            }
        }


        /// <summary>
        /// 计算指定阴历年月的总天数。
        /// </summary>
        /// <param name="iLunarYear">年份。</param>
        /// <param name="iLunarMonth">月份。</param>
        /// <returns>
        /// 返回阴历阴历年月的天数，如果该月为闰月，高字为第二个该月的天数，否则高字为0。
        /// </returns>
        /// <remarks>
        /// 指定年月范围在1901年1月---2050年12月之间。
        /// </remarks>
        private uint GetLunarMonthDays(ushort iLunarYear, ushort iLunarMonth)
        {
            int Height, Low;
            int iBit;
            if (iLunarYear < START_YEAR || iLunarYear > END_YEAR)
            {
                return 30;
            }
            Height = 0;
            Low = 29;
            iBit = 16 - iLunarMonth;
            if (iLunarMonth > GetLeapMonth(iLunarYear) && GetLeapMonth(iLunarYear) > 0)
            {
                iBit--;
            }

            if ((gLunarMonthDay[iLunarYear - START_YEAR] & (1 << iBit)) > 0)
            {
                Low++;
            }

            if (iLunarMonth == GetLeapMonth(iLunarYear))
            {
                if ((gLunarMonthDay[iLunarYear - START_YEAR] & (1 << (iBit - 1))) > 0)
                {
                    Height = 30;
                }
                else
                {
                    Height = 29;
                }
            }
            return (uint)(Low) | (uint)(Height) << 16; //合成为uint
        }


        /// <summary>
        /// 计算指定阴历年总天数。
        /// </summary>
        /// <param name="iLunarYear">指定阴历年，范围1901-2050。</param>
        /// <returns>返指定阴历年的总天数。</returns>
        private int GetLunarYearDays(ushort iLunarYear)
        {
            int Days;
            uint tmp;
            if (iLunarYear < START_YEAR || iLunarYear > END_YEAR)
            {
                return 0;
            }

            Days = 0;
            for (ushort i = 1; i <= 12; i++)
            {
                tmp = GetLunarMonthDays(iLunarYear, i);
                Days = Days + ((ushort)(tmp >> 16) & 0xFFFF); //取高位
                Days = Days + (ushort)(tmp); //取低位
            }
            return Days;
        }


        /// <summary>
        /// 计算从1901年1月1日过iSpanDays天后的阴历日期
        /// </summary>
        /// <param name="iYear">返回的年份。</param>
        /// <param name="iMonth">返回的月份。</param>
        /// <param name="iDay">返回的日子。</param>
        /// <param name="iSpanDays">天数。</param>
        private void CalcLunarDate(out ushort iYear, out ushort iMonth, out ushort iDay, uint iSpanDays)
        {
            uint tmp;
            //阳历1901年2月19日为阴历1901年正月初一
            //阳历1901年1月1日到2月19日共有49天
            if (iSpanDays < 49)
            {
                iYear = START_YEAR - 1;
                if (iSpanDays < 19)
                {
                    iMonth = 11;
                    iDay = (ushort)(11 + iSpanDays);
                }
                else
                {
                    iMonth = 12;
                    iDay = (ushort)(iSpanDays - 18);
                }
                return;
            }

            //下面从阴历1901年正月初一算起
            iSpanDays = iSpanDays - 49;
            iYear = START_YEAR;
            iMonth = 1;
            iDay = 1;
            //计算年
            tmp = (uint)GetLunarYearDays(iYear);
            while (iSpanDays >= tmp)
            {
                iSpanDays = iSpanDays - tmp;
                iYear++;
                tmp = (uint)GetLunarYearDays(iYear);
            }
            //计算月
            tmp = GetLunarMonthDays(iYear, iMonth); //取低位
            while (iSpanDays >= tmp)
            {
                iSpanDays = iSpanDays - tmp;
                if (iMonth == GetLeapMonth(iYear))
                {
                    tmp = (GetLunarMonthDays(iYear, iMonth) >> 16) & 0xFFFF; //取高位
                    if (iSpanDays < tmp)
                    {
                        break;
                    }
                    iSpanDays = iSpanDays - tmp;
                }
                iMonth++;
                tmp = GetLunarMonthDays(iYear, iMonth); //取低位
            }
            //计算日
            iDay = (ushort)(iDay + iSpanDays);
        }

        #endregion

        #region 星座

        /// <summary>
        /// 计算指定当前日期的星座序号。
        /// </summary>
        /// <returns>星座序号。</returns>
        private int GetConstellationIndex()
        {
            int Y, M, D;
            Y = m_Date.Year;
            M = m_Date.Month;
            D = m_Date.Day;
            Y = M * 100 + D;
            if (Y >= 321 && Y <= 419)
            {
                return 0;
            }
            else if (Y >= 420 && Y <= 520)
            {
                return 1;
            }
            else if (Y >= 521 && Y <= 620)
            {
                return 2;
            }
            else if (Y >= 621 && Y <= 722)
            {
                return 3;
            }
            else if (Y >= 723 && Y <= 822)
            {
                return 4;
            }
            else if (Y >= 823 && Y <= 922)
            {
                return 5;
            }
            else if (Y >= 923 && Y <= 1022)
            {
                return 6;
            }
            else if (Y >= 1023 && Y <= 1121)
            {
                return 7;
            }
            else if (Y >= 1122 && Y <= 1221)
            {
                return 8;
            }
            else if (Y >= 1222 || Y <= 119)
            {
                return 9;
            }
            else if (Y >= 120 && Y <= 218)
            {
                return 10;
            }
            else if (Y >= 219 && Y <= 320)
            {
                return 11;
            }
            else
            {
                return -1;
            }
        }


        /// <summary>
        /// 格式化星座序号为星座名称。
        /// </summary>
        /// <param name="ConstellationIndex">星座序号。</param>
        /// <returns>星座名称。</returns>
        private string FormatConstellation(int ConstellationIndex)
        {
            if (ConstellationIndex >= 0 && ConstellationIndex <= 11)
            {
                return ConstellationName[ConstellationIndex];
            }
            else
            {
                return "";
            }
        }

        #endregion

        #region 节气

        /// <summary>
        /// 计算公历当天对应的节气序号。
        /// </summary>
        /// <returns>返回值0-23为节气序号，-1表示不是节气。</returns>
        private int GetSolarTermIndex()
        {
            byte Flag;
            int Day, iYear, iMonth, iDay;
            iYear = m_Date.Year;
            if (iYear < START_YEAR || iYear > END_YEAR)
            {
                return -1;
            }

            iMonth = m_Date.Month;
            iDay = m_Date.Day;
            Flag = gLunarHolDay[(iYear - START_YEAR) * 12 + iMonth - 1];
            if (iDay < 15)
            {
                Day = 15 - ((Flag >> 4) & 0x0f);
            }
            else
            {
                Day = (Flag & 0x0f) + 15;
            }

            if (iDay == Day)
            {
                if (iDay > 15)
                {
                    return (iMonth - 1) * 2 + 1;
                }
                else
                {
                    return (iMonth - 1) * 2;
                }
            }
            else
            {
                return -1;
            }
        }


        /// <summary>
        /// 格式化节气序号为节气名称。
        /// </summary>
        /// <param name="SolarTermIndex">节气序号。</param>
        /// <returns>节气名称。</returns>
        private string FormatSolarTerm(int SolarTermIndex)
        {
            //string[] stroe = {"小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"};
            if (SolarTermIndex <= this.LunarHolDayName.Length && SolarTermIndex >= 0)
                return this.LunarHolDayName[SolarTermIndex];
            return "";
        }

        #endregion

        #region 年月日

        /// <summary>
        /// 格式化阴历月份。
        /// </summary>
        /// <param name="iYear">年份。</param>
        /// <returns>干支记年。</returns>
        private string FormatLunarYear(int iYear)
        {
            string strG = "甲乙丙丁戊己庚辛壬癸";
            string strZ = "子丑寅卯辰巳午未申酉戌亥";
            return strG.Substring((iYear - 4) % 10, 1) + strZ.Substring((iYear - 4) % 12, 1);
        }


        /// <summary>
        /// 格式化阴历年份。
        /// </summary>
        /// <param name="iYear">年份。</param>
        /// <returns>生肖。</returns>
        private string FormatAnimalYear(int iYear)
        {
            string strSX = "鼠牛虎免龙蛇马羊猴鸡狗猪";
            return strSX.Substring((iYear - 4) % 12, 1);
        }


        /// <summary>
        /// 格式化阴历月份。
        /// </summary>
        /// <param name="iMonth">月份。</param>
        /// <returns>中文月份。</returns>
        private string FormatLunarMonth(int iMonth)
        {
            string szText = "正二三四五六七八九十";
            if (iMonth <= 10) return szText.Substring(iMonth - 1, 1) + "月";
            if (iMonth == 11) return "十一月";
            if (iMonth == 12) return "十二月";
            return "";
        }


        /// <summary>
        /// 格式化阴历日子。
        /// </summary>
        /// <param name="iDay">日子。</param>
        /// <returns>中文日子。</returns>
        private string FormatLunarDay(int iDay)
        {
            string szText1 = "初十廿三";
            string szText2 = "一二三四五六七八九十";
            string strDay = "";
            if (iDay != 20 && iDay != 30)
            {
                try
                {
                    strDay = szText1.Substring((iDay - 1) / 10, 1);
                    strDay = strDay + szText2.Substring((iDay - 1) % 10, 1);
                }
                catch (Exception)
                {

                }
            }
            else
            {
                strDay = szText1.Substring((iDay / 10), 1);
                strDay = strDay + "十";
            }
            return strDay;
        }

        #endregion

        #region OutPut

        /// <summary>阴历日期,以LunarDate(年日月)形式表示。</summary>
        public LunarDate LunarDate
        {
            get
            {
                if (this.m_LunarDate == null)
                {
                    ushort iYear, iMonth, iDay;
                    TimeSpan ts = m_Date - (new DateTime(START_YEAR, 1, 1));
                    this.CalcLunarDate(out iYear, out iMonth, out iDay, (uint)(ts.Days));
                    this.m_LunarDate = new LunarDate(iYear, iMonth, iDay);
                }
                return this.m_LunarDate;
            }
        }


        /// <summary>阴历干支记年。</summary>
        public string LunarYear
        {
            get
            {
                if (m_LunarYear == "")
                    this.m_LunarYear = this.FormatLunarYear(this.LunarDate.Year);
                return this.m_LunarYear;
            }
        }


        /// <summary>阴历生肖。</summary>
        public string Animal
        {
            get
            {
                if (m_Animal == "")
                    this.m_Animal = this.FormatAnimalYear(this.LunarDate.Year);
                return this.m_Animal;
            }
        }


        /// <summary>格式化后的阴历月份。</summary>
        public string LunarMonth
        {
            get
            {
                if (this.m_LunarMonth == "")
                    this.m_LunarMonth = this.FormatLunarMonth(ushort.Parse(this.LunarDate.Month.ToString()));
                return this.m_LunarMonth;
            }
        }

        /// <summary>格式化后的阴历日子。</summary>
        public string LunarDay
        {
            get
            {
                if (this.m_LunarDay == "")
                    this.m_LunarDay = this.FormatLunarDay(ushort.Parse(this.LunarDate.Day.ToString()));
                if (this.m_LunarDay == "初一")
                {
                    this.m_LunarDay = this.LunarMonth;
                }
                return this.m_LunarDay;
            }
        }


        /// <summary>格式化后的阴历节气。</summary>
        public string SolarTerm
        {
            get
            {
                if (this.m_SolarTerm == "")
                    this.m_SolarTerm = this.FormatSolarTerm(this.GetSolarTermIndex());
                return this.m_SolarTerm;
            }
        }


        /// <summary>格式化后的星座。</summary>
        public string Constellation
        {
            get
            {
                if (this.m_Constellation == "")
                    this.m_Constellation = this.FormatConstellation(this.GetConstellationIndex());
                return this.m_Constellation;
            }
        }

        #endregion
    }



    public class LunarDate
    {
        private int _y, _m, _d;
        private string lunardate = "";
        private string lunarmonth = "", lunarday = "", lunaryear = "";
        private string solarterm = "", animal = "";


        public LunarDate(DateTime dt)
        {
            LunarDateClass ldc = new LunarDateClass(dt);
            this.lunarday = ldc.LunarDay;
            this.lunarmonth = ldc.LunarMonth;
            this.lunaryear = ldc.LunarYear;
            this.solarterm = ldc.SolarTerm;
            this.animal = ldc.Animal;
            this.lunardate = this.lunaryear + "(" + this.animal + ")年" + this.lunarmonth + this.lunarday + (this.solarterm == "" ? "" : " " + this.solarterm);
            this._y = ldc.LunarDate.Year;
            this._m = ldc.LunarDate.Month;
            this._d = ldc.LunarDate.Day;
        }
        public LunarDate(int y, int m, int d)
        {
            this._y = y;
            this._m = m;
            this._d = d;
        }

        public int Year
        {
            get { return this._y; }
        }


        public int Month
        {
            get { return this._m; }
        }


        public int Day
        {
            get { return this._d; }
        }


        public string LunarDay
        {
            get
            {
                return this.lunarday;
            }
        }


        public string LunarMonth
        {
            get
            {
                return this.lunarmonth;
            }
        }


        public string LunarYear
        {
            get
            {
                return this.lunaryear;
            }
        }


        public string SolarTerm
        {
            get
            {
                return this.solarterm;
            }
        }


        public string Animal
        {
            get
            {
                return this.animal;
            }
        }


        public new string ToString()
        {
            return this.lunardate;
        }

    }


    #endregion




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

}
