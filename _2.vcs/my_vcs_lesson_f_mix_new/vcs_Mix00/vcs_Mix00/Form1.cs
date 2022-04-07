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
        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定义鼠标 
        Bitmap bitmap1;

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

            string filename = @"C:\______test_files\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;


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

            string strServiceName = string.Empty;


            string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
            //string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";


            //Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定义鼠标 

            //使用WMI取得USB資訊

            ManagementObjectSearcher search = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            ManagementObjectCollection collection = search.Get();
            var usbList = from u in collection.Cast<ManagementBaseObject>()
                          select new
                          {
                              id = u.GetPropertyValue("DeviceID"),
                              name = u.GetPropertyValue("Name"),
                              status = u.GetPropertyValue("Status"),
                              system = u.GetPropertyValue("SystemName"),
                              caption = u.GetPropertyValue("Caption"),
                              pnp = u.GetPropertyValue("PNPDeviceID"),
                              description = u.GetPropertyValue("Description")
                          };
            foreach (var u in usbList)
            {
                richTextBox1.Text += String.Format("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}{7}{7}", u.id, u.name, u.status, u.system, u.caption, u.pnp, u.description, Environment.NewLine);
            }




        }

        private Image theimage;
        private Image smallimage;

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //使用TextureBrush類繪製圖像

            string filename = @"C:\______test_files\__RW\_gif\sky.gif";

            SetStyle(ControlStyles.Opaque, true);
            Bounds = new Rectangle(0, 0, 1300, 850);
            theimage = new Bitmap(filename);
            smallimage = new Bitmap(theimage, new Size(theimage.Width, theimage.Height));

            Graphics g = pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, ClientRectangle);

            Brush brush = new TextureBrush(smallimage, new Rectangle(0, 0, smallimage.Width, smallimage.Height));
            //用圖像創建畫筆,來繪制圖像
            g.FillEllipse(brush, new Rectangle(0, 200, 200, 200));
            //用圖像創建剛筆,來繪制圖像
            Pen pen = new Pen(brush, 20);
            g.DrawRectangle(pen, new Rectangle(250, 200, 200, 200));
            //用圖像繪製文本
            Font font = new Font("Times New Roman", 40, FontStyle.Bold | FontStyle.Italic);
            g.DrawString("Hello Image !!", font, brush, new Rectangle(0, 0, 500, font.Height));

            brush.Dispose();
            font.Dispose();



        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //折線圖
            Pic();

        }

        private void Pic()
        {
            //測試數據
            DataTable table = new DataTable("Data");
            DataRow Dr;
            DataColumn Dc = new DataColumn("ID", Type.GetType("System.Int32"));
            DataColumn Dc2 = new DataColumn("Num", Type.GetType("System.Int32"));
            DataColumn Dc3 = new DataColumn("name", Type.GetType("System.String"));
            table.Columns.Add(Dc);
            table.Columns.Add(Dc2);
            table.Columns.Add(Dc3);
            Random rnd = new Random();
            for (int n = 0; n < 61; n++)
            {
                Dr = table.NewRow();
                Dr[0] = n;
                Dr[1] = rnd.Next(10, 140);
                Dr[2] = n.ToString();
                table.Rows.Add(Dr);
            }
            //畫圖參數
            int BG_Width = 450;
            int BG_Height = 180;
            int Pic_Width = 450;
            int Pic_Height = 180;
            int pic_X = 6;
            int pic_H = 1;
            int pic_tr = 5;
            int pic_td = 12;
            Rectangle rec = new Rectangle(50, 15, 360, 150);
            Pen Pic_Bolder = new Pen(Color.Black, 1);
            Pen Pic_line = new Pen(Color.Gray, 1);
            Pen Pic_Data = new Pen(Color.Red, 2);
            SolidBrush brusth = new SolidBrush(Color.Blue);
            Point[] DataPt = new Point[table.Rows.Count];
            int x;
            int y;
            for (int n = 0; n < table.Rows.Count; n++)
            {
                Dr = table.Rows[n];
                x = (int)Dr[0] * pic_X + rec.X;
                y = (int)Dr[1] * pic_H + rec.Y;
                DataPt[n] = new Point(x, y);
            }
            Bitmap Bg = new Bitmap(BG_Width, BG_Height, PixelFormat.Format24bppRgb);
            Graphics Ph = Graphics.FromImage(Bg);
            Ph.Clear(Color.White);
            Ph.DrawRectangle(Pic_Bolder, rec);
            //畫折線
            Ph.DrawCurve(Pic_Data, DataPt);
            //rec.
            Point SPoint = new Point();
            Point Epoint = new Point();
            //畫橫線
            for (int n = 1; n < pic_tr; n++)
            {
                //cell[0] = new Point(rec.X);
                SPoint.X = 0 + rec.X;
                SPoint.Y = n * 30 + rec.Y;
                Epoint.X = rec.Width + rec.X;
                Epoint.Y = n * 30 + rec.Y;
                Ph.DrawLine(Pic_line, SPoint, Epoint);
            }
            //畫豎線
            for (int n = 1; n < pic_td; n++)
            {
                SPoint.X = n * 30 + rec.X;
                SPoint.Y = rec.Y;
                Epoint.X = n * 30 + rec.X;
                Epoint.Y = rec.Height + rec.Y;
                Ph.DrawLine(Pic_line, SPoint, Epoint);
            }
            //畫標題
            string Title = "畫折線測試";
            SolidBrush brush = new SolidBrush(Color.RoyalBlue);
            Ph.DrawString(Title, new Font("Franklin Gothic Demi", 12, FontStyle.Italic), brush, new Point(200, 0));
            Ph.Save();
            //Bg.Save(Response.OutputStream, ImageFormat.Gif);
            pictureBox1.Image = Bg;
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

        //局部圖像放大
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            int r = 20;
            int ratio = 2;
            try
            {
                //局部圖像放大
                Cursor.Current = myCursor;								//定义鼠标
                Graphics graphics = pictureBox1.CreateGraphics();				//实例化pictureBox1控件的Graphics类
                //声明两个Rectangle对象，分别用来指定要放大的区域和放大后的区域
                Rectangle sourceRectangle = new Rectangle(e.X - r, e.Y - r, r * 2, r * 2);	//要放大的区域 
                Rectangle destRectangle = new Rectangle(e.X - r * ratio, e.Y - r * ratio, r * 2 * ratio, r * 2 * ratio);
                //调用DrawImage方法对选定区域进行重新绘制，以放大该部分
                graphics.DrawImage(bitmap1, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch { }

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
