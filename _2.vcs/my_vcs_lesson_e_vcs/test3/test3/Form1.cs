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

namespace test3
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

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 0+15);
            pictureBox1.Location = new Point(x_st + dx * 3+100, y_st + dy * 0);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            //控件位置
            bt_exit.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_exit.Size.Width, richTextBox1.Location.Y + 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲取文件的版本信息:
            string filename = @"C:\______test_files\_material\AForge.Video.dll";

            FileVersionInfo myFileVersionInfo1 = FileVersionInfo.GetVersionInfo(filename);
            richTextBox1.Text += "版本號: " + myFileVersionInfo1.FileVersion + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "今天是 : " + GetCnWeek() + "\n";
        }

        /// <summary>
        /// 獲得中文星期名稱
        /// </summary>
        /// <returns></returns>
        public static string GetCnWeek()
        {
            switch (DateTime.Now.DayOfWeek)
            {
                case DayOfWeek.Monday:
                    return "星期一";
                case DayOfWeek.Tuesday:
                    return "星期二";
                case DayOfWeek.Wednesday:
                    return "星期三";
                case DayOfWeek.Thursday:
                    return "星期四";
                case DayOfWeek.Friday:
                    return "星期五";
                case DayOfWeek.Saturday:
                    return "星期六";
                case DayOfWeek.Sunday:
                    return "星期日";
                default:
                    return "星期一";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲取百度首頁生成靜態文件
            this.DownUrltoFile("http://www.baidu.com", "baidu.htm", "GB2312");

            //DownUrltoFile("http://www.xueit.com/show.aspx?pid=1", "html/news/20091224-001.html", "GB2312");
            //其中URL：http://www.xueit.com/show.aspx?pid=1 是动态显示文章，html/news/20091224-001.html是表字段htmlFile预先保存的文件名，这样就可以生成静态文件了。

        }

        /// 獲取遠程URL並生成文件的代碼：
        /// <summary>
        /// 生成網頁文件
        /// </summary>
        /// <param name="url">遠程URL</param>
        /// <param name="filename">生成文件名路徑</param>
        /// <param name="pagecode">目標URL頁面編碼</param>
        protected void DownUrltoFile(string url, string filename, string pagecode)
        {
            try
            {
                //編碼
                Encoding encode = Encoding.GetEncoding(pagecode);
                //請求URL
                HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
                //設置超時(10秒)
                req.Timeout = 10000;
                //this.NotFolderIsCreate(filename);
                //獲取Response
                HttpWebResponse rep = (HttpWebResponse)req.GetResponse();
                //創建StreamReader與StreamWriter文件流對象
                StreamReader sr = new StreamReader(rep.GetResponseStream(),encode);
                StreamWriter sw = new StreamWriter(filename, false,encode);
                //寫入內容
                sw.Write(sr.ReadToEnd());
                //清理當前緩存區，並將緩存寫入文件
                sw.Flush();
                //釋放相關對象資源
                sw.Close();
                sw.Dispose();
                sr.Close();
                sr.Dispose();
                //Response.Write("生成文件"   filename   "成功");
            }
            catch (Exception ex)
            {
                //Response.Write("生成文件"   filename   "失敗，原因："   ex.Message);
            }
        }

        //以上代碼關鍵知識點，通過HttpWebRequest、HttpWebResponse請求獲取遠程URL數據，之後使用StreamReader、StreamWriter文件流讀寫數據寫入文件，注意還有編碼Encoding。

        /*
        /// <summary>
        /// 文件夾不存在則創建
        /// </summary>
        /// <param name="filename">文件名所在路徑</param>
        protected void NotFolderIsCreate(string filename)
        {
            string fileAtDir = Server.MapPath(Path.GetDirectoryName(filename));
            if (!Directory.Exists(fileAtDir))
                Directory.CreateDirectory(fileAtDir);
        }
        */

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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            MyTempImage myTempImage = new MyTempImage();

            //myTempImage.CreateImage();
            pictureBox1.Image = Image.FromFile(myTempImage.CreateImage());



            //string thefullname = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + ".gif"; // "nowtime.gif";
            //richTextBox1.Text += thefullname + "\n";
        }



    }

    public class MyTempImage
    {
        public string CreateImage()
        {
            string str = DateTime.Now.ToString();
            Bitmap image = new Bitmap(200, 30);
            Graphics g = Graphics.FromImage(image);
            string thefullname = DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + ".gif"; // "nowtime.gif";

            g.Clear(Color.White);
            g.DrawString(str, new Font("CourIEr New", 10), new SolidBrush(Color.Red), 20, 5);
            //Graphics 類還有很多繪圖方法可以繪制 直線、曲線、圓等等 
            image.Save(thefullname, System.Drawing.Imaging.ImageFormat.Gif);
            return thefullname;
        }
    }
}

