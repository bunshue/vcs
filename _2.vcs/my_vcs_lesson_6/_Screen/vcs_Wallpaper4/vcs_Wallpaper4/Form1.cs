using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using Microsoft.Win32;

namespace vcs_Wallpaper4
{
    public partial class Form1 : Form
    {
        static string imgFile = @"C:\______test_files\";
        static string imgName = "bear.bmp";

        [DllImport("User32.dll")]
        static extern IntPtr GetDC(IntPtr hwnd);

        [DllImport("User32.dll")]
        static extern void ReleaseDC(IntPtr dc);

        [DllImport("user32.dll", EntryPoint = "SystemParametersInfo")]
        static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

                /// <summary>
        /// 直接在螢幕上畫一個區域性圖片
        /// </summary>
        public static void DrawStart()
        {
            IntPtr desktop = GetDC(IntPtr.Zero);
            Font font = new Font("Arial", 24);
            using (Graphics g = Graphics.FromHdc(desktop))
            {
                g.FillRectangle(Brushes.Black, 0, 0, 430, 150);
                g.DrawString("aaaaaaa", font, Brushes.White, 5, 5);
            }
            //ReleaseDC(desktop);
        }

        static int sW = 1024, sH = 768,cW = 20,cH = 20;

        /// <summary>
        /// 畫一個圖片,返回圖片儲存的路徑
        /// </summary>
        /// <returns></returns>
        public static string GetPathDrawImage()
        {
            Bitmap image = new Bitmap(sW, sH);
            Font font = new Font("微軟雅黑", 16);
            Pen penC = new Pen(Brushes.LightYellow);

            Graphics g = null;
            try
            {
                g = Graphics.FromImage(image);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //int i = 0;
            //int num = 0;

            g.FillRectangle(Brushes.Black, 0, 0, sW, sH);
            g.DrawString("BBBBBB", font, Brushes.White, 5, 5);
            
            int wW = 200;
            int wH = 200;
            var r = new Random();
            int z = DateTime.Now.Second;
            int cs = r.Next(0, 100);
            for (int c=0; c<cs; c++)
            {
                Pen pen = null;
                switch (r.Next(0, 10))
                {
                    case 1: pen = new Pen(Brushes.Red); break;
                    case 2: pen = new Pen(Brushes.Orange); break;
                    case 3: pen = new Pen(Brushes.Yellow); break;
                    case 4: pen = new Pen(Brushes.Green); break;
                    case 5: pen = new Pen(Brushes.Peru); break;
                    case 6: pen = new Pen(Brushes.Gray); break;
                    case 7: pen = new Pen(Brushes.Blue); break;
                    case 8: pen = new Pen(Brushes.DarkBlue); break;
                    case 9: pen = new Pen(Brushes.YellowGreen); break;
                    default: pen = new Pen(Brushes.Purple); break;
                }
                if (r.Next(0, 2) == 0)
                {
                    wW -= r.Next(0, z);
                }
                else
                {
                    wW += r.Next(0, z);
                }
                if (r.Next(0, 2) == 0)
                {
                    wH -= r.Next(0, z);
                }
                else
                {
                    wH += r.Next(0, z);
                }
                g.DrawEllipse(penC, (sW - cW) / 2, (sH - cH) / 2, cW, cH);
                g.DrawEllipse(pen, (sW - wW) / 2, (sH - wH) / 2, wW, wH);
            }

            try
            {
                g.BeginContainer();

                image.Save("aaaa.jpg");
                image.Dispose();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            return imgFile + imgName;
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

        private void button1_Click(object sender, EventArgs e)
        {
            //設置桌面圖片  OK
            string filename = @"C:\______test_files\picture1.jpg";
            SetDesktopPicture(filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //DrawStart();
            GetPathDrawImage();
        }

    }
}

