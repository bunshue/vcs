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

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
            //陽歷轉換成陰歷的類
        }

        private void button29_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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


