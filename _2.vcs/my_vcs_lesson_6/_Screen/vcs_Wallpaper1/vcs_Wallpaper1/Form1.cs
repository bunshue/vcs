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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

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
            SetDesktopPicture(filename);
        }
    }
}
