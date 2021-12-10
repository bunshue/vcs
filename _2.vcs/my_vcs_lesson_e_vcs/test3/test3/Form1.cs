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
using System.Management;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

using System.IO;
using System.IO.Ports;
using System.Threading;
using System.Reflection;    //for Assembly
using System.Security;
using System.Security.Cryptography;

using Shell32;
using Microsoft.Win32;  //for Registry

namespace test3
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// 操作系統關閉時，關閉應用程序
        /// </summary>
        /// <param name="m">截獲系統消息</param>
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case 0x0011://WM_QUERYENDSESSION
                    //m.Result = (IntPtr)1;
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    break;
                default:
                    base.WndProc(ref m);
                    break;
            }
        }
        /*
        做了一個定時播放器,程序運行時最小化到任務欄托盤,可這時候關閉或重啟操作系統使如果程序沒有退出,
        則系統不能關閉.那麼如何實現關機時自動退出程序呢?其實很簡單,當windows操作系統執行關閉動作時,
        它會發送給各個正在運行的應用程序一個消息WM_QUERYENDSESSION,告訴應用程序要關機了,如果反饋回來的消息值為1,
        那麼windows操作系統就會自動關閉.因此,通過截獲WM_QUERYENDSESSION消息,就能實現自動退出程序.
        */


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

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 15);
            pictureBox1.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 0);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1);

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
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string result = appInfo();
            richTextBox1.Text += result + "\n";
        }

        public static string appInfo()
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            FileVersionInfo fvi = FileVersionInfo.GetVersionInfo(assembly.Location);
            string result = "File Version: " + fvi.FileVersion
                + Environment.NewLine + "Company Name: " + fvi.CompanyName
                + Environment.NewLine + "Comments: " + fvi.Comments
                + Environment.NewLine + "Product Name: " + fvi.ProductName
                + Environment.NewLine + "Copyright: " + fvi.LegalCopyright
                + Environment.NewLine + "File Name: " + fvi.FileName
                + Environment.NewLine + "Original File Name: " + fvi.OriginalFilename
                + Environment.NewLine + "Product Version: " + fvi.ProductVersion
                + Environment.NewLine + "Special build: " + fvi.SpecialBuild
                + Environment.NewLine + "" + fvi.CompanyName;
            return result;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //html轉txt
            //http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184774.html
        }

        /// C#過濾html標簽
        /// 用正則表達式來做html轉txt
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            return htmlStr.Trim();
        }

        // 顏色模板
        //  黑、白、紅、綠、藍、黃/ 棕 、灰
        private const int BLACK = 0;
        private const int WHITE = 1;
        private const int RED1 = 2;
        private const int RED2 = 3;
        private const int GREEN1 = 4;
        private const int GREEN2 = 5;
        private const int BLUE1 = 6;
        private const int BLUE2 = 7;
        private const int YELLOW1 = 8;
        private const int YELLOW2 = 9;
        private const int BROWN = 10;
        private const int GRAY = 11;

        private void button13_Click(object sender, EventArgs e)
        {
            //顯示顏色
            int[,] colorVelue = null;
            colorVelue = new int[,] {
            {50,50,50},    //黑
            {255,255,255},  //白
            {240,80,80}, //紅小
            {240,160,160},  //紅大
            {60,180,60}, //綠小
            {160,240,160},  //綠大
            {80,80,240}, //藍小
            {160,160,240},  //藍大
            {240,190,80}, //黃小
            {240,240,160},  //黃大
            {205,133,63},   //棕/褐
            //{162,162,162},//灰，特殊
            };

            int total_colors = colorVelue.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_colors = " + total_colors.ToString() + "\n";

            int i;
            for (i = 0; i < total_colors; i++)
            {
                switch (i)
                {
                    case -1:
                        richTextBox1.Text += "無此色\n";
                        break;
                    case 0:
                        richTextBox1.Text += "黑\n";
                        break;
                    case 1:
                        richTextBox1.Text += "白\n";
                        break;
                    case 2:
                        richTextBox1.Text += "紅\n";
                        break;
                    case 3:
                        richTextBox1.Text += "紅\n";
                        break;
                    case 4:
                        richTextBox1.Text += "綠\n";
                        break;
                    case 5:
                        richTextBox1.Text += "綠\n";
                        break;
                    case 6:
                        richTextBox1.Text += "藍\n";
                        break;
                    case 7:
                        richTextBox1.Text += "藍\n";
                        break;
                    case 8:
                        richTextBox1.Text += "黃\n";
                        break;
                    case 9:
                        richTextBox1.Text += "黃\n";
                        break;
                    case 10:
                        richTextBox1.Text += "棕\n";
                        break;
                    case 11:
                        richTextBox1.Text += "灰\n";
                        break;
                    default:
                        richTextBox1.Text += "其他\n";
                        break;
                }

                int R = colorVelue[i, 0];
                int G = colorVelue[i, 1];
                int B = colorVelue[i, 2];
                richTextBox1.Text += "show color " + i.ToString() + " " + R.ToString() + " " + G.ToString() + " " + B.ToString() + "\n";

                pictureBox1.BackColor = Color.FromArgb(R, G, B);
                Application.DoEvents();
                Thread.Sleep(1000);

            }

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

