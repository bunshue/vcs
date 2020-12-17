using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;  //for Registry

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_Registry2
{
    public partial class Form1 : Form
    {
        string old_wallpaper_path = String.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey("software\\Microsoft\\Internet Explorer");
            string IEVersion = "目前IE瀏覽器的版本訊息：" + (String)mreg.GetValue("Version");
            mreg.Close();
            richTextBox1.Text += IEVersion + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            mreg = Registry.CurrentUser;
            mreg = mreg.CreateSubKey("Control Panel\\Desktop");
            old_wallpaper_path = (String)mreg.GetValue("Wallpaper");
            mreg.Close();
            richTextBox1.Text += "紀錄目前桌布路徑：" + old_wallpaper_path + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            mreg = Registry.CurrentUser;
            mreg = mreg.CreateSubKey("Control Panel\\Desktop");
            string wallpaper_path = (String)mreg.GetValue("Wallpaper");
            mreg.Close();
            richTextBox1.Text += "目前桌布路徑：" + wallpaper_path + "\n";

        }

        [DllImport("user32.dll", CharSet = CharSet.Auto)]

        private static extern Int32 SystemParametersInfo(UInt32 uiAction, UInt32 uiParam, String pvParam, UInt32 fWinIni);
        private static UInt32 SPI_SETDESKWALLPAPER = 20;
        private static UInt32 SPIF_UPDATEINIFILE = 0x1;

        public void SetImage(string filename)
        {
            SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, filename, SPIF_UPDATEINIFILE);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string new_wallpaper_path = @"C:\Windows\Web\Wallpaper\Theme1\img1.jpg";
            SetImage(new_wallpaper_path);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string new_wallpaper_path = @"C:\Windows\Web\Wallpaper\Theme1\img2.jpg";
            SetImage(new_wallpaper_path);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            string new_wallpaper_path = @"C:\Windows\Web\Wallpaper\Theme1\img3.jpg";
            SetImage(new_wallpaper_path);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (old_wallpaper_path != string.Empty)
            {
                richTextBox1.Text += "舊的桌面路徑：" + old_wallpaper_path + ", 恢復\n";
                SetImage(old_wallpaper_path);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
