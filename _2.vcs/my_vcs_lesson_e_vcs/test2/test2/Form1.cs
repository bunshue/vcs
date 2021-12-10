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

        }

        private void button1_Click(object sender, EventArgs e)
        {

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


        private void button9_Click(object sender, EventArgs e)
        {

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
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

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

        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}

