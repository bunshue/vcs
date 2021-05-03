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
            x_st = 12;
            y_st = 12;
            dx = 185;
            dy = 55;

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

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //取得Owner與Company
            object owner_string = "", company_string = "";
            OperatingSystem os_info = System.Environment.OSVersion;
            if (os_info.Platform == PlatformID.Win32Windows)
            {
                // Windows 98?
                owner_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows\CurrentVersion\",
                    "RegisteredOwner", "Unknown");
                company_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows\CurrentVersion\",
                    "RegisteredOrganization", "Unknown");
            }
            else if (os_info.Platform == PlatformID.Win32NT)
            {
                // Windows NT.
                owner_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows NT\CurrentVersion\",
                    "RegisteredOwner", "Unknown");
                company_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows NT\CurrentVersion\",
                    "RegisteredOrganization", "Unknown");
            }

            richTextBox1.Text += "Owner :\t" + owner_string.ToString() + "\n";
            richTextBox1.Text += "Company :\t" + company_string.ToString() + "\n";




        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "進入Windows前發出警告\n";

            string title = "寫標題在此";
            string content = "寫內容在此";
            RegistryKey rkey = Registry.LocalMachine;
            RegistryKey rkeyInfo = rkey.CreateSubKey(@"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon");

            //偽執行
            rkeyInfo.SetValue("LegalNoticeCaption", title, RegistryValueKind.String);
            rkeyInfo.SetValue("LegalNoticeText", content, RegistryValueKind.String);

            MessageBox.Show("已完成設定，請重新啟動計算機！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);

            //若已存入，要用regedit到 HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows NT/CurrentVersion/Winlogon 刪除相關設定
        }

        private void button2_Click(object sender, EventArgs e)
        {

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

        private void button9_Click(object sender, EventArgs e)
        {


        }

        private void button10_Click(object sender, EventArgs e)
        {
            //取得各瀏覽器版本訊息
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey("software\\Microsoft\\Internet Explorer");
            string IEVersion = "目前IE瀏覽器的版本訊息：\t" + (String)mreg.GetValue("Version");
            mreg.Close();
            richTextBox1.Text += IEVersion + "\n";

            RegistryKey mreg2;
            mreg2 = Registry.LocalMachine;
            mreg2 = mreg2.CreateSubKey("software\\mozilla.org\\Mozilla");
            string FirefoxVersion = "目前Firefox瀏覽器的版本訊息：\t" + (String)mreg2.GetValue("CurrentVersion");
            mreg2.Close();
            richTextBox1.Text += FirefoxVersion + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //設定IE瀏覽器的預設主頁

            //1.讀取目前IE的首頁
            RegistryKey reg1 = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            object strInfo = reg1.GetValue("Start Page", "沒有值");
            //this.textBox1.Text = (string)strInfo;
            richTextBox1.Text += "IE目前的首頁:\t" + (string)strInfo + "\n";

            //2.設定IE的首頁為空白頁
            RegistryKey reg2 = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg2.SetValue("Start Page", "about:blank", RegistryValueKind.String);
            richTextBox1.Text += "IE 目前的預設頁為\t空白頁\n";

            //3.設定IE的首頁為Google首頁
            string url = @"https://www.google.com.tw/";
            RegistryKey reg3 = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg3.SetValue("Start Page", url, RegistryValueKind.String);
            richTextBox1.Text += "IE 目前的預設頁為\t" + url + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //禁止修改IE主頁設定
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Policies\Microsoft\Internet Explorer\Control Panel");
            reg.SetValue("HomePage", 1, RegistryValueKind.DWord);
            MessageBox.Show("禁止修改IE主頁設定成功");
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //啟動IE主頁設定
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Policies\Microsoft\Internet Explorer\Control Panel");
            reg.SetValue("HomePage", 0, RegistryValueKind.DWord);
            MessageBox.Show("啟動IE主頁設定成功");
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //修改IE瀏覽器標題欄內容
            string new_title = "AAAAAAA";
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg.SetValue("Window Title", new_title, RegistryValueKind.String);
            MessageBox.Show("修改成功");
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //恢復IE瀏覽器標題欄內容
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg.DeleteValue("Window Title", false);
            MessageBox.Show("恢復成功");
        }
    }
}

