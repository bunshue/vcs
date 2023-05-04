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
using System.Drawing.Imaging;
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

        private static void SetWallPaper(string filename, Style style)
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

            SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, filename, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE);
        }

        int sel_picture = 0;
        string foldername = @"C:\______test_files1\__pic\_MU\";
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

            if (Properties.Settings.Default.foldername != null)
            {
                if (Directory.Exists(Properties.Settings.Default.foldername) == true)     //確認資料夾是否存在
                {
                    foldername = Properties.Settings.Default.foldername;
                }
            }

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
            dx = 120;
            dy = 40;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_folder.Location = new Point(x_st + dx * 1+3, y_st + dy * 6-8);
            bt_folder2.Location = new Point(x_st + dx * 1+3, y_st + dy * 7-3);

            richTextBox1.Location = new Point(x_st + dx * 1 + 55, y_st + dy * 0);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.foldername = foldername;
            Properties.Settings.Default.Save();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\picture1.bmp";
            SetDesktopPicture(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\bear.bmp";
            SetDesktopPicture(filename);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\__pic\tiger.bmp";
            SetDesktopPicture(filename);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files1\_material\ims1.bmp";
            SetDesktopPicture(filename);

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
            string filename = @"C:\______test_files1\picture1.bmp";

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
            if (Directory.Exists(foldername) == false)     //確認資料夾是否存在
            {
                richTextBox1.Text += "無圖片\n";
                return;
            }

            //任選一張圖
            DirectoryInfo DInfo = new DirectoryInfo(foldername);
            FileInfo[] FInfo = DInfo.GetFiles();
            Random rand = new Random();
            sel_picture = rand.Next(FInfo.Length);

            string filename = foldername + FInfo[sel_picture].Name;
            richTextBox1.Text += "sel_picture = " + sel_picture.ToString() + "filename : " + filename + "\n";

            //讀取圖檔
            //pictureBox1.Image = Image.FromFile(filename);

            SetDesktopPicture(filename);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            timer_weather_Tick(sender, e);

            //看起來是相隔10分鐘更新一次
            //定時切換 衛星雲圖
            int update_time = 3;
            richTextBox1.Text += "每隔 " + update_time.ToString() + " 分鐘 更新一次衛星雲圖\n";
            timer_weather.Interval = update_time * 60 * 1000;
            timer_weather.Enabled = true;
        }

        int cnt = 0;
        private void timer_weather_Tick(object sender, EventArgs e)
        {
            cnt++;
            richTextBox1.Text += "第 " + cnt.ToString() + " 次\t時間 : " + DateTime.Now.ToString() + "\t";

            Load_SatelliteImages();
        }

        string satellite_image_version = "";
        string satellite_image_version_old = "";

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

                    satellite_image_version = dt.Year + "-" + dt.Month.ToString("00") + "-" + dt.Day.ToString("00") + "-" + dt.Hour.ToString("00") + "-" + Minute.ToString("00");

                    if (satellite_image_version == satellite_image_version_old)
                    {
                        richTextBox1.Text += "取得相同資料, 忽略\n";
                    }
                    else
                    {
                        richTextBox1.Text += "取得新資料, 更新\n";

                        //string filename1 = Application.StartupPath + "\\SatelliteImage1_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
                        //string filename2 = Application.StartupPath + "\\SatelliteImage2_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

                        string filename1 = Application.StartupPath + "\\SatelliteImage1.jpg";
                        string filename2 = Application.StartupPath + "\\SatelliteImage2.bmp";

                        if (File.Exists(filename1) == true)
                        {
                            File.Delete(filename1);
                        }
                        if (File.Exists(filename2) == true)
                        {
                            File.Delete(filename2);
                        }

                        pictureBox1.Image.Save(filename1);

                        Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);
                        int W = bitmap1.Width;
                        int H = bitmap1.Height;
                        Graphics g = Graphics.FromImage(bitmap1);

                        g.DrawString(satellite_image_version, new Font("標楷體", 50), new SolidBrush(Color.Red), new PointF(W * 2 / 3 - 130, H / 4 - 50));

                        bitmap1.Save(filename2, ImageFormat.Bmp);

                        //SetWallPaper(filename, Style.Fit);  //等比例放大/縮小至螢幕最大
                        SetWallPaper(filename2, Style.Center);  //原始比例顯示正中間那一塊

                        /*
                        richTextBox1.Text += "URL = " + mapURL + "\n";
                        richTextBox1.Text += "W = " + pictureBox1.Image.Size.Width.ToString() + "\n";
                        richTextBox1.Text += "H = " + pictureBox1.Image.Size.Height.ToString() + "\n";
                        */
                        satellite_image_version_old = satellite_image_version;
                    }
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

        private void bt_folder_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "c:\\______test_files1";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                foldername = folderBrowserDialog1.SelectedPath + "\\";
                /*
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                richTextBox1.Text += "RootFolder: " + folderBrowserDialog1.RootFolder + "\n";
                richTextBox1.Text += "Container: " + folderBrowserDialog1.Container + "\n";
                richTextBox1.Text += "Description: " + folderBrowserDialog1.Description + "\n";
                richTextBox1.Text += "ShowNewFolderButton: " + folderBrowserDialog1.ShowNewFolderButton + "\n";
                richTextBox1.Text += "Site: " + folderBrowserDialog1.Site + "\n";
                richTextBox1.Text += "Tag: " + folderBrowserDialog1.Tag + "\n";
                */

            }
            else
            {
                //richTextBox1.Text = "未選取資料夾\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void bt_folder2_Click(object sender, EventArgs e)
        {

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

