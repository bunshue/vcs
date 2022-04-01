using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;
using System.Drawing.Text;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Management;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Media;     //for SoundPlayer
using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web
using System.Globalization; //for CultureInfo

using System.Collections;

using System.Xml;
using System.Xml.Linq;

using Shell32;  //需/參考/加入參考/COM/Microsoft Shell Controls And Automation 並把 Shell32屬性的內嵌Interop型別改成False

namespace vcs_Mix00
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //網頁protocol	解決  要求已經中止: 無法建立 SSL/TLS 的安全通道。
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

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

            pictureBox1.Size = new Size(640, 480);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            webBrowser1.Size = new Size(640, 240);
            webBrowser1.Location = new Point(x_st + dx * 1, y_st + dy * 6 + 70);

            richTextBox1.Location = new Point(x_st + dx * 5 - 50, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            byte[] bytSendData = new byte[5];

            //協議不支持
            bytSendData[0] = 0x12;
            bytSendData[1] = 0x34;
            bytSendData[2] = 0x56;

            UInt16 intCRC16 = GetCheckCode(bytSendData, 3);
            bytSendData[3] = (byte)(intCRC16 & 0xFF);   //CRC校驗低位
            bytSendData[4] = (byte)((intCRC16 >> 8) & 0xff);                //CRC校驗高位

            //發送數據
            //serial.Write(bytSendData, 0, 5);

        }

        //CRC16校驗
        private UInt16 GetCheckCode(byte[] buf, int nEnd)
        {
            UInt16 crc = (UInt16)0xffff;
            int i, j;
            for (i = 0; i < nEnd; i++)
            {
                crc ^= (UInt16)buf[i];
                for (j = 0; j < 8; j++)
                {
                    if ((crc & 1) != 0)
                    {
                        crc >>= 1;
                        crc ^= 0xA001;
                    }
                    else
                        crc >>= 1;
                }
            }
            return crc;
        }


        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            richTextBox1.Text += week + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //從windows剪貼板獲取內容
            IDataObject iData = Clipboard.GetDataObject();
            if (iData.GetDataPresent(DataFormats.Text))
            {
                richTextBox1.Text += "取得文字:\n";
                Console.WriteLine((String)iData.GetData(DataFormats.Text));
            }
            if (iData.GetDataPresent(DataFormats.Bitmap))
            {
                richTextBox1.Text += "取得圖片\n";
                Image img = (Bitmap)iData.GetData(DataFormats.Bitmap);
                pictureBox1.Image = img;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //計算兩個日期的時間間隔
            DateTime dt2 = new DateTime(1974, 9, 24);
            DateTime dt1 = new DateTime(1999, 3, 8);
            string diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";
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
    }

    //3Form1之外
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }
}
