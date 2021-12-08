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
using System.Xml.Linq;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;
using System.Security.Cryptography; //for MD5

using Microsoft.Win32;

using System.Diagnostics;
using System.Threading;


namespace test2
{
    public partial class Form1 : Form
    {
        static PerformanceCounter cpu = new PerformanceCounter("Processor", "% Processor Time", "_Total");
        static PerformanceCounter memory = new PerformanceCounter("Memory", "% Committed Bytes in Use");

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
            bt_exit.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_exit.Size.Width, richTextBox1.Location.Y + 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //C#遍歷窗體控件
            string find_ctrl = "button8";
            ForeachFormControls(find_ctrl);
        }

        /// <summary>
        /// Winform C#遍历窗体控件
        /// </summary>
        /// <param name="ctrlName">控件名称</param>
        public void ForeachFormControls(string ctrlName)
        {
            foreach (Control ctrl in this.Controls)
            {
                if (ctrl is Panel)
                {
                    //相關操作代碼
                    ctrl.BackColor = Color.Aquamarine;
                }
                else if (ctrl is Button)
                {
                    ctrl.ForeColor = Color.RoyalBlue;
                }
                else if (ctrl is TextBox)
                {
                    ctrl.Text = null;
                }

                //根據控件名稱找某個控件
                if (ctrl.Name.Equals(ctrlName))
                {
                    //ctrl.Name = string.Empty;
                    ctrl.BackColor = Color.Red;
                }
            }
        }

        /* 找panel1內的控件
        /// <summary>
        /// C#遍历子控件
        /// </summary>
        /// <param name="ctrlName">控件名称</param>
        public void ForeachPanelControls(string ctrlName)
        {
            foreach (Control ctrl in panel1.Controls)
            {
                if (ctrl is Button)
                {
                    if (ctrl.Name.Equals(ctrlName))
                        ctrl.ForeColor = Color.RoyalBlue;
                    else
                        ctrl.ForeColor = Color.SkyBlue;
                }
                else if (ctrl is TextBox)
                {
                    if (ctrl.Name.Equals(ctrlName))
                        ctrl.Name = "当前值";
                    else
                        ctrl.Text = null;
                }
            }
        }
        */

        /* 找chekbox內的控件
        private void ForeachCheckBox(Control ctrls, bool currVal)
        {
            CheckBox cb;
            foreach (Control ctrl in ctrls.Controls)
            {
                if (ctrl is CheckBox)
                {
                    cb = (CheckBox)ctrl;
                    cb.Checked = currVal;
                }
            }
        }
        //same
        private void ForeachCheckBoxes(Control ctrls, bool currVal)
        {
            CheckBox cb;
            foreach (Control ctrl in ctrls.Controls.OfType<CheckBox>())
            {
                cb = (CheckBox)ctrl;
                cb.Checked = currVal;
            }
        }
        */

        private void button1_Click(object sender, EventArgs e)
        {
            //方法1    
            //例：窗体的透明度为50% 
            //this.Opacity = 0.5; 

            //方法2，我用的方法2，窗体透明控件不透明了
            // TransparencyKey只支持透明或不透明，不支持过度色，比如PNG图片中的从不透明到透明的过渡色会显示出讨厌的效果
            this.BackColor = Color.Black;
            this.TransparencyKey = Color.Black;

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

        }




        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {


        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "格式化列印\n";
            Console.WriteLine("The value 99999 in different ways:");
            Console.WriteLine("c format : {0:c}", 99999);
            Console.WriteLine("d9 format : {0:d9}", 99999);
            Console.WriteLine("f format : {0:f3}", 99999);
            Console.WriteLine("g format : {0:g}", 99999);

            Console.WriteLine("n format : {0:n}", 99999);
            Console.WriteLine("E format : {0:E}", 99999);
            Console.WriteLine("e format : {0:e}", 99999);
            Console.WriteLine("X format : {0:X}", 99999);
            Console.WriteLine("x format : {0:x}", 99999);
        }

        static bool IsWebResourceAvailable(string webResourceAddress)
        {
            try
            {
                HttpWebRequest req = (HttpWebRequest)WebRequest.CreateDefault(new Uri(webResourceAddress));
                req.Method = "HEAD";
                req.Timeout = 1000;
                HttpWebResponse res = (HttpWebResponse)req.GetResponse();
                return (res.StatusCode == HttpStatusCode.OK);
            }
            catch (WebException wex)
            {
                System.Diagnostics.Trace.Write(wex.Message); return false;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //C#使用HTTP頭檢測網絡資源是否有效
            string url = @"http://hovertree.com/themes/hvtimages/hwqlogo.png";
            bool result = IsWebResourceAvailable(url);
            richTextBox1.Text += result.ToString() + "\n";

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //C# 模擬鍵盤操作--SendKey(),SendKeys()
            //https://www.cnblogs.com/wolfocme110/p/13444309.html


            //光标移至richTextBox1
            richTextBox1.Focus();

            //模拟按下"ABCDEFG"
            SendKeys.SendWait("(ABCDEFG)");
            SendKeys.SendWait("{left 5}");
            SendKeys.SendWait("{h 10}");

            /*
            更多举例:
            SendKeys.SendWait("^C");  //Ctrl+C 组合键
            SendKeys.SendWait("+C");  //Shift+C 组合键
            SendKeys.SendWait("%C");  //Alt+C 组合键
            SendKeys.SendWait("+(AX)");  //Shift+A+X 组合键
            SendKeys.SendWait("+AX");  //Shift+A 组合键,之后按X键
            SendKeys.SendWait("{left 5}");  //按←键 5次
            SendKeys.SendWait("{h 10}");   //按h键 10次
            SendKeys.Send("汉字");  //模拟输入"汉字"2个字
            */

        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "AAAA\n";
            //獲取安裝軟件和路徑，通過注冊表得到
            using (RegistryKey key = Registry.LocalMachine.OpenSubKey(@"SoftwareMicrosoftWindowsCurrentVersionUninstall", false))
            {
                richTextBox1.Text += "BBBB\n";
                if (key != null)//判斷對象存在
                {
                    richTextBox1.Text += "CCCC\n";
                    foreach (string keyName in key.GetSubKeyNames())//遍歷子項名稱的字符串數組
                    {
                        using (RegistryKey key2 = key.OpenSubKey(keyName, false))//遍歷子項節點
                        {
                            if (key2 != null)
                            {
                                string softwareName = key2.GetValue("DisplayName", "").ToString();//獲取軟件名
                                string installLocation = key2.GetValue("InstallLocation", "").ToString();//獲取安裝路徑
                                richTextBox1.Text += "softwareName : " + softwareName + "\n";
                                richTextBox1.Text += "installLocation : " + installLocation + "\n";
                                if (!string.IsNullOrEmpty(installLocation))
                                {
                                    //將信息添加到ListView控件中
                                    ListViewItem item = new ListViewItem(softwareName);
                                    item.SubItems.Add(installLocation);
                                    //listView1.Items.Add(item);
                                    richTextBox1.Text += "get item : " + item + "\n";
                                }
                            }
                        }
                    }
                }
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
            // CPU 與記憶體使用率
            //建一個 PerformanceCounter 物件，指定分類、計數器名稱、執行個體，接著用 NextValue() 取值，輕鬆搞定。
            Console.WriteLine("CPU: {0:n1}%", cpu.NextValue());
            Console.WriteLine("Memory: {0:n0}%", memory.NextValue());

            richTextBox1.Text += "CPU: " + cpu.NextValue() + "\n";
            richTextBox1.Text += "Memory: " + memory.NextValue() + "\n";

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //LINQ to XML write
            /*
            //LINQ to XML操作Xml文檔


            //.Net中的System.Xml.Linq命名空間提供了linq to xml的支持。這個命名空間中的XDocument，XElement以及XText，XAttribute提供了讀寫xml文檔的關鍵方法。
            1. 使用linq to xml寫xml：
            使用XDocument的構造函數可以構造一個Xml文檔對象；使用XElement對象可以構造一個xml節點元素，使用XAttribute構造函數可以構造元素的屬性；使用XText構造函數可以構造節點內的文本。
            */


            var xDoc = new XDocument(new XElement("root",
                new XElement("dog",
                    new XText("dog said black is a beautify color"),
                    new XAttribute("color", "black")),
                new XElement("cat"),
                new XElement("pig", "pig is great")));

            //xDoc輸出xml的encoding是系統默認編碼，對於簡體中文操作系統是gb2312
            //默認是縮進格式化的xml，而無須格式化設置
            xDoc.Save("aaaa.xml");


            //LINQ to XML read


            var query = from item in xDoc.Element("root").Elements()
                        select new
                        {
                            TypeName = item.Name,
                            Saying = item.Value,
                            Color = item.Attribute("color") == null ? (string)null : item.Attribute("color").Value
                        };


            foreach (var item in query)
            {
                Console.WriteLine("{0} 's color is {1},{0} said {2}", item.TypeName, item.Color ?? "Unknown", item.Saying ?? "nothing");
                richTextBox1.Text += item.TypeName + "\t" + item.Color + "\n";
            }


        }

        private void button15_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\elephant.jpg";

            System.Drawing.Image.GetThumbnailImageAbort callb = null;

            try
            {
                // 保存到指定的文件夾
                Image MyImage = Image.FromFile(filename);
                // 保存大圖(原圖)
                Image NewImage = MyImage.GetThumbnailImage(800, 1000, callb, new System.IntPtr());
                NewImage.Save("big.jpg");
                // 保存中圖
                NewImage = MyImage.GetThumbnailImage(400, 500, callb, new System.IntPtr());
                NewImage.Save("middle.jpg");

                // 單款衣服的圖片大小
                NewImage = MyImage.GetThumbnailImage(255, 319, callb, new System.IntPtr());
                NewImage.Save("SingleImage.jpg");

                // 保存小圖
                NewImage = MyImage.GetThumbnailImage(115, 144, callb, new System.IntPtr());
                NewImage.Save("small.jpg");
                // 保存極小圖
                NewImage = MyImage.GetThumbnailImage(45, 56, callb, new System.IntPtr());
                NewImage.Save("dinky.jpg");

                MyImage.Dispose();
                NewImage.Dispose();
                // 一定要釋放，否則進程被占用
            }
            catch (Exception ex)
            {
                //Response.Write(ex.ToString());
            } 

        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            // CPU 與記憶體使用率
            Console.WriteLine("CPU: {0:n1}%", cpu.NextValue());
            Console.WriteLine("Memory: {0:n0}%", memory.NextValue());

            richTextBox1.Text += "CPU: " + cpu.NextValue() + " %\n";
            richTextBox1.Text += "Memory: " + memory.NextValue() + " %\n";


        }

    }
}

