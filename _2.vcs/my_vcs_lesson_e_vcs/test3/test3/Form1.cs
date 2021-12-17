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

using System.Drawing.Imaging;

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
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            string url = @"https://www.google.com.tw/";
            WebBrowser webBrowser1 = new WebBrowser();
            webBrowser1.ScrollBarsEnabled = false;
            webBrowser1.Size = new Size(Screen.PrimaryScreen.Bounds.Width, Screen.PrimaryScreen.Bounds.Height);

            //取得網頁資料
            webBrowser1.Navigate(url);
            while (webBrowser1.ReadyState != WebBrowserReadyState.Complete)
            {
                Application.DoEvents();
            }

            //截圖
            Bitmap bitmap1 = new Bitmap(W, H);
            Rectangle DrawRect = new Rectangle(0, 0, W, H);
            webBrowser1.DrawToBitmap(bitmap1, DrawRect);

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string senderEmail = @"david@insighteyes.com";
            string[] sendFromUser = senderEmail.Split('@');
            int len = sendFromUser.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + sendFromUser[i] + "\n";
            }



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

        private void button12_Click(object sender, EventArgs e)
        {

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
