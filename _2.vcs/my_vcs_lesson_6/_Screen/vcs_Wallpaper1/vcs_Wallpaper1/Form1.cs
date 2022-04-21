using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;   //for SecurityProtocolType
using System.Runtime.InteropServices;
using Microsoft.Win32;

namespace vcs_Wallpaper1
{
    public partial class Form1 : Form
    {
        #region System Innerface
        [DllImport("user32.dll", EntryPoint = "SystemParametersInfo")]
        public static extern int SystemParametersInfo(
            int uAction,
            int uParam,
            string lpvParam,
            int fuWinIni
         );
        #endregion

        public enum Style : int
        {
            Fill,
            Fit,
            Span,
            Stretch,
            Tile,
            Center
        }

        /// <summary>
        /// 設定拉伸圖片桌面桌布
        /// https://blog.csdn.net/sonyicn/article/details/746280?utm_source=blogxgwz4
        /// </summary>
        /// <param name="path"></param>
        public static void SetDesktopPicture(string path)
        {
            RegistryKey myRegKey = Registry.CurrentUser.OpenSubKey("Control Panel\\Desktop", true);
            myRegKey.SetValue("TileWallpaper", "0");
            myRegKey.SetValue("WallpagerStyle", "2");
            myRegKey.Close();

            SystemParametersInfo(20, 1, path, 1);
        }

        const int SPI_SETDESKWALLPAPER = 20;
        const int SPIF_UPDATEINIFILE = 0x01;
        const int SPIF_SENDWININICHANGE = 0x02;

        private static void SetWallPaper(string wpaper, Style style)
        {
            using (RegistryKey myRegKey = Registry.CurrentUser.OpenSubKey(@"Control Panel\Desktop", true))
            {
                if (style == Style.Fill)
                {
                    myRegKey.SetValue(@"WallpaperStyle", 10.ToString());
                    myRegKey.SetValue(@"TileWallpaper", 0.ToString());
                }
                if (style == Style.Fit)
                {
                    myRegKey.SetValue(@"WallpaperStyle", 6.ToString());
                    myRegKey.SetValue(@"TileWallpaper", 0.ToString());
                }
                if (style == Style.Span) // Windows 8 or newer only!
                {
                    myRegKey.SetValue(@"WallpaperStyle", 22.ToString());
                    myRegKey.SetValue(@"TileWallpaper", 0.ToString());
                }
                if (style == Style.Stretch)
                {
                    myRegKey.SetValue(@"WallpaperStyle", 2.ToString());
                    myRegKey.SetValue(@"TileWallpaper", 0.ToString());
                }
                if (style == Style.Tile)
                {
                    myRegKey.SetValue(@"WallpaperStyle", 0.ToString());
                    myRegKey.SetValue(@"TileWallpaper", 1.ToString());
                }
                if (style == Style.Center)
                {
                    myRegKey.SetValue(@"WallpaperStyle", 0.ToString());
                    myRegKey.SetValue(@"TileWallpaper", 0.ToString());
                }
            }

            SystemParametersInfo(SPI_SETDESKWALLPAPER,
                    0,
                    wpaper,
                    SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE);
        }

        int sel_picture = 0;
        string foldername = @"C:\______test_files\__pic\_MU\";
        int image_type = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //.Net 4.0 要強迫使用 TLS 1.2 抓資料
            ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };
            ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072;

            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.bmp";
            SetDesktopPicture(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\bear.bmp";
            SetDesktopPicture(filename);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\__pic\tiger.bmp";
            SetDesktopPicture(filename);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_material\ims1.bmp";
            //SetDesktopPicture(filename);

            //SetWallPaper(filename, Style.Center); //置中
            //SetWallPaper(filename, Style.Fill);   //填滿
            //SetWallPaper(filename, Style.Fit);  //等比例放大/縮小至螢幕最大
            //SetWallPaper(filename, Style.Span);
            //SetWallPaper(filename, Style.Stretch);
            //SetWallPaper(filename, Style.Tile);   //原圖大小 排列滿螢幕
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //下次開機後才套用
            string filename = @"C:\______test_files\picture1.bmp";

            RegistryKey myRegKey = Registry.CurrentUser.OpenSubKey("Control Panel\\Desktop", true);
            myRegKey.SetValue("TileWallpaper", "0");
            myRegKey.SetValue("WallpagerStyle", "2");
            myRegKey.SetValue("WallPaper", filename);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;



        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //任選一張圖
            DirectoryInfo DInfo = new DirectoryInfo(foldername);
            FileInfo[] FInfo = DInfo.GetFiles();
            Random rand = new Random();
            sel_picture = rand.Next(FInfo.Length);

            string filename = foldername + FInfo[sel_picture].Name;
            //richTextBox1.Text += "sel_picture = " + sel_picture.ToString() + "filename : " + filename + "\n";

            //讀取圖檔
            //pictureBox1.Image = Image.FromFile(filename);

            SetDesktopPicture(filename);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            timer_weather_Tick(sender, e);

            //定時切換 衛星雲圖
            timer_weather.Enabled = true;
        }

        int cnt = 0;
        private void timer_weather_Tick(object sender, EventArgs e)
        {
            cnt++;
            this.Text += "第 " + cnt.ToString() + " 次";

            Load_SatelliteImages();
        }

        void Load_SatelliteImages()
        {
            int i;
            string mapURL = string.Empty;
            DateTime dt = DateTime.Now;
            int Minute;
            //pictureBox1.ClientSize = new Size(1200, 1200);
            //pictureBox1.Location = new Point(0, 0);

            //加入這段語法忽略憑證
            System.Net.ServicePointManager.ServerCertificateValidationCallback = delegate { return true; };

            for (i = 0; i < 5; i++)
            {
                Minute = (dt.Minute / 10) * 10;

                switch (image_type)
                {
                    case 0:
                        //richTextBox1.Text += "000\n";
                        mapURL = string.Format("https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    case 1:
                        //richTextBox1.Text += "111\n";
                        mapURL = string.Format("https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    case 2:
                        //richTextBox1.Text += "222\n";
                        mapURL = string.Format("https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    case 3:
                        //richTextBox1.Text += "333\n";
                        mapURL = string.Format("https://www.cwb.gov.tw/Data/satellite/LCC_IR1_CR_2750/LCC_IR1_CR_2750-{0}-{1}-{2}-{3}-{4}.jpg",
                        dt.Year, dt.Month.ToString("00"), dt.Day.ToString("00"), dt.Hour.ToString("00"), Minute.ToString("00"));
                        break;
                    default:
                        //richTextBox1.Text += "xxxxx\n";
                        break;

                }

                //richTextBox1.Text += "aaaa mapURL : " + mapURL + "\n";


                //MessageBox.Show("path: " + mapURL);

                try
                {   //可能會產生錯誤的程式區段
                    pictureBox1.Load(mapURL);

                    string filename = Application.StartupPath + "\\SatelliteImage_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

                    pictureBox1.Image.Save(filename);

                    SetWallPaper(filename, Style.Fit);  //等比例放大/縮小至螢幕最大

                    /*
                    richTextBox1.Text += "URL = " + mapURL + "\n";
                    richTextBox1.Text += "W = " + pictureBox1.Image.Size.Width.ToString() + "\n";
                    richTextBox1.Text += "H = " + pictureBox1.Image.Size.Height.ToString() + "\n";
                    */
                    break;
                }
                catch (Exception ex)
                {   //定義產生錯誤時的例外處理程式碼
                    //MessageBox.Show("path: " + mapURL);
                    //MessageBox.Show(ex.Message);
                }
                finally
                {
                    //一定會被執行的程式區段
                    //MessageBox.Show("path: " + mapURL);
                }
                dt = dt.AddMinutes(-10);
            }

        }

    }

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
