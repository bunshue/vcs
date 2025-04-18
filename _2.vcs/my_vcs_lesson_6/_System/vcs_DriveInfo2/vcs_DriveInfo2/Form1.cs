﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;            //for DriveInfo
using System.Globalization; //for CultureInfo
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_DriveInfo2
{
    public partial class Form1 : Form
    {
        bool flag_debug_mode = false;
        bool flag_warning = false;

        private const int THRESHOLD1 = 20;  //預設 一級警戒, 警告
        private const int THRESHOLD2 = 10;  //預設 二級警戒, 嚴重警告
        Bitmap bitmap1 = null;
        Graphics g;

        [DllImportAttribute("user32.dll")]
        private extern static bool ReleaseCapture();
        [DllImportAttribute("user32.dll")]
        private extern static int SendMessage(IntPtr handle, int m, int p, int h);

        int hdd_space_threshold1 = THRESHOLD1; //一級警戒 低於20%
        int hdd_space_threshold2 = THRESHOLD2; //二級警戒 低於10%, 二級較嚴重
        string upload_source_directory = string.Empty;
        string upload_destination_directory = string.Empty;
        int upload_interval = 10;
        bool flag_upload_enabled = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            update_default_setting();

            this.FormBorderStyle = FormBorderStyle.None;
            //this.richTextBox1.Visible = false;
            this.Text = "使用 DriveInfo 類別取得磁碟資訊";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            get_disk_info();
        }

        void update_default_setting()
        {
            int threshold1 = Properties.Settings.Default.hdd_space_threshold1;
            int threshold2 = Properties.Settings.Default.hdd_space_threshold2;
            string source_directory = Properties.Settings.Default.upload_source_directory;
            string destination_directory = Properties.Settings.Default.upload_destination_directory;
            int interval = Properties.Settings.Default.upload_interval;
            bool flag_enabled = Properties.Settings.Default.upload_enabled;

            //檢查這些數字是否合法

            string mesg = threshold1.ToString() + " " + threshold2.ToString() + " " +
                source_directory + " " + destination_directory + " " + interval.ToString() + " " + flag_enabled.ToString();

            richTextBox1.Text += mesg + "\n";

            bool flag_parameter_reasonable = true;
            if ((threshold1 < 0) || (threshold1 > 100))
            {
                mesg = "一級警戒 範圍應為 0 ~ 100";
                richTextBox1.Text += mesg + "\n";
                flag_parameter_reasonable = false;
            }

            if ((threshold2 < 0) || (threshold2 > 100))
            {
                mesg = "二級警戒 範圍應為 0 ~ 100";
                richTextBox1.Text += mesg + "\n";
                flag_parameter_reasonable = false;
            }

            if (threshold1 >= threshold2)
            {
                mesg = "二級警戒 應該比較嚴重, 二級警戒 要大於 一級警戒";
                richTextBox1.Text += mesg + "\n";
                flag_parameter_reasonable = false;
            }

            if (interval < 0)
            {
                mesg = "上傳間隔時間應大於0分鐘";
                richTextBox1.Text += mesg + "\n";
                flag_parameter_reasonable = false;
            }

            if (source_directory != "")
            {
                if (Directory.Exists(source_directory) == false)
                {
                    mesg = "上拋來源資料夾 設定錯誤";
                    richTextBox1.Text += mesg + "\n";
                    flag_parameter_reasonable = false;
                }
            }

            if (destination_directory != "")
            {
                if (Directory.Exists(destination_directory) == false)
                {
                    mesg = "上拋目的資料夾 設定錯誤";
                    richTextBox1.Text += mesg + "\n";
                    flag_parameter_reasonable = false;
                }
            }

            if (flag_enabled == true)    //若有開啟上拋功能, 要多考慮 上拋來源/目的資料夾
            {
                if (source_directory == "")
                {
                    mesg = "未設定上拋來源資料夾";
                    richTextBox1.Text += mesg + "\n";
                    flag_parameter_reasonable = false;
                }
                else
                {
                    if (Directory.Exists(source_directory) == false)
                    {
                        mesg = "上拋來源資料夾 設定錯誤";
                        richTextBox1.Text += mesg + "\n";
                        flag_parameter_reasonable = false;
                    }
                }

                if (destination_directory == "")
                {
                    mesg = "未設定上拋目的資料夾";
                    richTextBox1.Text += mesg + "\n";
                    flag_parameter_reasonable = false;
                }
                else
                {
                    if (Directory.Exists(destination_directory) == false)
                    {
                        mesg = "上拋來源資料夾 設定錯誤";
                        richTextBox1.Text += mesg + "\n";
                        flag_parameter_reasonable = false;
                    }
                }
            }

            if (flag_parameter_reasonable == false)
            {
                richTextBox1.Text += "參數錯誤, 全不套用\n";
                //return;
            }
            else
            {
                richTextBox1.Text += "取得 一級警戒 : " + threshold1.ToString() + "\n";
                richTextBox1.Text += "取得 二級警戒 : " + threshold2.ToString() + "\n";
                richTextBox1.Text += "取得 上拋起始資料夾 : " + source_directory + "\n";
                richTextBox1.Text += "取得 上拋目的資料夾 : " + destination_directory + "\n";
                richTextBox1.Text += "取得 上拋間隔 : " + interval.ToString() + "\n";
                richTextBox1.Text += "取得 上拋功能 : " + flag_enabled.ToString() + "\n";
                richTextBox1.Text += "參數正確, 套用參數\n";

                hdd_space_threshold1 = 100 - threshold1; //一級警戒
                hdd_space_threshold2 = 100 - threshold2; //二級警戒, 二級較嚴重
                upload_source_directory = source_directory;
                upload_destination_directory = destination_directory;
                upload_interval = interval;
                flag_upload_enabled = flag_enabled;
            }
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(KSize / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (KSize / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(KSize / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (KSize / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(KSize / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (KSize / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(KSize / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return KSize.ToString() + " Byte";//顯示Byte值
        }

        void drawDiskSpace(int cx, int cy, int r, string name, long free, long total)
        {
            bool flag_disk_free_low = false;
            if ((free * 100 / total) < hdd_space_threshold2)
            {
                flag_disk_free_low = true;
                //g.FillRectangle(Brushes.Pink,
                g.FillRectangle(Brushes.Red, cx, cy, r, r);
            }
            else if ((free * 100 / total) < hdd_space_threshold1)
            {
                flag_disk_free_low = true;
                //g.FillRectangle(Brushes.Pink,
                g.FillRectangle(Brushes.Pink, cx, cy, r, r);
            }
            else
            {
                flag_disk_free_low = false;
            }

            richTextBox1.Text += "drawDiskSpace\n";
            richTextBox1.Text += "cx = " + cx.ToString() + "\tcy = " + cy.ToString() + "\tr = " + r.ToString() + "\n";
            richTextBox1.Text += "free = " + free.ToString() + "\n";
            richTextBox1.Text += "total = " + total.ToString() + "\n";

            Brush b;
            long used = total - free;

            int used_angle = (int)(used * 360 / total);
            //richTextBox1.Text += "used_angle = " + used_angle.ToString() + "\n";

            b = new SolidBrush(Color.GreenYellow);
            g.FillEllipse(b, cx + r / 10, cy + r / 10, r * 80 / 100, r * 80 / 100);

            b = new SolidBrush(Color.DeepSkyBlue);
            g.FillPie(b, cx + r / 10, cy + r / 10, r * 80 / 100, r * 80 / 100, -180, used_angle);

            b = new SolidBrush(Color.LightGray);
            g.FillEllipse(b, cx + r * 3 / 10, cy + r * 3 / 10, r * 4 / 10, r * 4 / 10);

            int x_st = 0;
            int y_st = 5;
            int dy = 20;
            //g.DrawString(name, new Font("標楷體", 14), new SolidBrush(Color.Green), new Point(x_st + cx, y_st + cy + r + dy * 0));
            //g.DrawString(name[0].ToString(), new Font("標楷體", 14), new SolidBrush(Color.Green), new Point(x_st + cx, y_st + cy + r + dy * 0));
            g.DrawString(name[0].ToString(), new Font("標楷體", 18), new SolidBrush(Color.Blue), new Point(cx + r / 2 - 10, cy + r / 2 - 10));

            string str1 = ByteConversionGBMBKB(Convert.ToInt64(total));
            string str2 = ByteConversionGBMBKB(Convert.ToInt64(total - free));
            string str3 = ByteConversionGBMBKB(Convert.ToInt64(free));
            string str4 = ((float)free / (float)total).ToString("P", CultureInfo.InvariantCulture);

            Font f = new Font("Times New Roman", 14);

            g.DrawString(str1, f, new SolidBrush(Color.Gray), new Point(x_st + cx, y_st + cy + r + dy * 0));
            g.DrawString(str2, f, new SolidBrush(Color.DeepSkyBlue), new Point(x_st + cx, y_st + cy + r + dy * 1));
            g.DrawString(str3, f, new SolidBrush(Color.LimeGreen), new Point(x_st + cx, y_st + cy + r + dy * 2));

            if (flag_disk_free_low == true)
            {
                g.DrawString(str4, f, Brushes.Red, new Point(x_st + cx, y_st + cy + r + dy * 3));
                g.DrawRectangle(new Pen(Color.Red, 7), cx, cy, r, r);
            }
            else
            {
                g.DrawString(str4, f, Brushes.Green, new Point(x_st + cx, y_st + cy + r + dy * 3));
                g.DrawRectangle(Pens.Green, cx, cy, r, r);
            }
            pictureBox1.Image = bitmap1;
        }

        void get_disk_info()
        {
            flag_warning = false;

            //使用System.IO.DriveInfo來遍歷磁片及其分區資訊
            //引用System.IO後即可調用DriveInfo類來對磁碟空間資訊進行遍歷了，此外DriveInfo只有在普通WINFORM中可以調用，WINCE專案中未封裝此類。
            //獲取磁片設備
            DriveInfo[] allDrives = DriveInfo.GetDrives();
            richTextBox1.Text += "系統共有 " + allDrives.Length.ToString() + " 部磁碟機" + "\n";
            //遍歷磁片
            foreach (DriveInfo drive in allDrives)
            {
                richTextBox1.Text += drive.Name + "        ";
            }

            richTextBox1.Text += "\n";

            int total_drives = 0;

            //取得所有磁碟資訊：
            foreach (DriveInfo drive in allDrives)
            {
                richTextBox1.Text += "磁碟分割號:  " + drive.Name + " 槽\n";
                richTextBox1.Text += "RootDirectory:  " + drive.RootDirectory + "\n";
                richTextBox1.Text += "DriveType:  " + drive.DriveType;
                if (drive.IsReady == true)  //使用IsReady屬性判斷裝置是否就緒
                {
                    total_drives++;
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "磁碟標籤:  " + drive.VolumeLabel + "\n";
                    richTextBox1.Text += "磁碟類型:  " + drive.DriveType.ToString() + "\n";
                    richTextBox1.Text += "磁碟格式:  " + drive.DriveFormat + "\n";
                    richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                    richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t"
                        + ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\t( "
                        + ((float)drive.AvailableFreeSpace / (float)drive.TotalSize).ToString("P", CultureInfo.InvariantCulture) + " )\n";
                    richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";
                }
                else
                {
                    richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
                }
                richTextBox1.Text += "\n";
            }

            richTextBox1.Text += "共有 : " + total_drives.ToString() + " 台固定式磁碟機\n";

            //total_drives = 1; debug

            int screen_width = 0;
            if (total_drives <= 2)
                screen_width = 2;
            else
                screen_width = total_drives;

            int w = 100 * screen_width + 1;
            int h = 245;
            if (total_drives <= 2)
                h = 245;
            else
                h = 220;
            bitmap1 = new Bitmap(w, h);
            g = Graphics.FromImage(bitmap1);
            g.Clear(SystemColors.ControlLight);
            pictureBox1.Size = new Size(w, h);
            pictureBox1.Location = new Point(0, 0);

            int cnt = 0;
            long total = 233905053696;
            long free = 24903962624;

            int cx = 0;
            int cy = 0;
            int r = 100;

            List<String> warning_directory = new List<String>();
            String result = "";
            foreach (DriveInfo di in DriveInfo.GetDrives())
            {
                //取得磁碟的資訊，並逐一列出
                if (di.IsReady)
                {
                    //表示有東西，若不是可能是光碟、軟碟機
                    result += String.Format("{0}\t{1}\t{2}\t{3}\r\n", di.Name, di.DriveType, di.TotalSize, di.TotalFreeSpace);
                    //印出資訊

                    total = di.TotalSize;
                    free = di.TotalFreeSpace;

                    cx = r * cnt;
                    cy = 0;

                    cnt++;

                    if (total_drives == 1)
                        drawDiskSpace(cx + r / 2, cy, r, di.Name, free, total);
                    else
                        drawDiskSpace(cx, cy, r, di.Name, free, total);

                    if ((free * 100 / total) < hdd_space_threshold1)
                    {
                        //richTextBox1.Text += "str = " + ((float)free / (float)total).ToString() + "\n";
                        warning_directory.Add(di.Name);
                    }

                    /*  debug
                    if (cnt == 1)
                        break;
                    */
                }
                else
                {
                    result += String.Format("{0}\t{1}\r\n", di.Name, di.DriveType);
                }
            }
            richTextBox1.Text += result + "\n";


            string warning = "";
            foreach (string s in warning_directory)
            {
                warning += s + " ";
            }

            if (warning.Length > 0)
            {
                flag_warning = true;
                if (total_drives < 2)
                {
                    g.DrawString("磁碟 : " + warning, new Font("標楷體", 18), new SolidBrush(Color.Red), new Point(40, 190));
                    g.DrawString("容量不足", new Font("標楷體", 18), new SolidBrush(Color.Red), new Point(40, 190 + 25));
                }
                else if (total_drives == 2)
                {
                    g.DrawString("磁碟 : " + warning, new Font("標楷體", 18), new SolidBrush(Color.Red), new Point(10, 190));
                    g.DrawString("容量不足", new Font("標楷體", 18), new SolidBrush(Color.Red), new Point(10, 190 + 25));
                }
                else
                {
                    g.DrawString("磁碟 : " + warning + " 容量不足", new Font("標楷體", 18), new SolidBrush(Color.Red), new Point(10, 190));
                }
            }

            if (flag_debug_mode == false)
            {
                int W = Screen.PrimaryScreen.Bounds.Width;
                int H = Screen.PrimaryScreen.Bounds.Height;

                this.BackColor = Color.Pink;
                this.ClientSize = new Size(w, h);
                this.Location = new Point(W - w - 6, H - h - 40);
            }
            else
            {
                this.BackColor = Color.Pink;
                this.ClientSize = new Size(w + 300, h - 62 + 400);
                //this.Location = new Point(1920 - w - 16, 1080 / 2);
            }
            int ww = 30;
            int hh = 30;
            int x_st = w - ww - 2 - 1;
            int y_st = h - hh - 2 - 1;
            g.DrawRectangle(new Pen(Color.Red, 4), x_st, y_st, ww, hh);
            g.DrawLine(new Pen(Color.Red, 4), x_st, y_st, x_st + ww, y_st + hh);
            g.DrawLine(new Pen(Color.Red, 4), x_st, y_st + hh, x_st + ww, y_st);


            Bitmap bmp = new Bitmap(Properties.Resources.setup);
            x_st = x_st - ww;
            Rectangle destRect1 = new Rectangle(x_st + 1, y_st + 1, ww - 2, hh - 2);
            float x = 0;
            float y = 0;
            float width = bmp.Width;
            float height = bmp.Height;
            GraphicsUnit units = GraphicsUnit.Pixel;
            g.DrawImage(bmp, destRect1, x, y, width, height, units);
            g.DrawRectangle(new Pen(Color.Red, 4), x_st, y_st, ww, hh);


            g.DrawRectangle(Pens.Green, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            if ((cnt % 3600) == 0)
            {
                get_disk_info();
            }
            if (flag_upload_enabled == true)
            {
                if ((cnt % (upload_interval * 60)) == 0)
                {
                    do_upload_work();
                }
            }
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Left)
            {
                this.Cursor = Cursors.SizeAll;
                ReleaseCapture();
                try
                {
                    SendMessage(this.Handle, 0xA1, 0x2, 0);
                }
                catch (Exception ex)
                {
                    //richTextBox1.Text += "xxx錯誤訊息e39 : " + ex.Message + "\n";
                }

                this.Cursor = Cursors.Default;
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "(" + e.X.ToString() + ", " + e.Y.ToString() + ") ";

            int w = pictureBox1.Size.Width;
            int h = pictureBox1.Size.Height;
            int ww = 30;
            int hh = 30;
            int x_st = w - ww - 2;
            int y_st = h - 62 - 2 - hh;
            //g.DrawRectangle(new Pen(Color.Red, 4), x_st, y_st, ww, hh);
            //g.DrawLine(new Pen(Color.Red, 4), x_st, y_st, x_st + ww, y_st + hh);
            //g.DrawLine(new Pen(Color.Red, 4), x_st, y_st + hh, x_st + ww, y_st);
            if ((e.X > (w - ww)) && (e.X < w) && (e.Y > (h - hh)) && (e.Y < h))
                Application.Exit();
            else if ((e.X > (w - ww * 2)) && (e.X < (w - ww)) && (e.Y > (h - hh)) && (e.Y < h))
            {
                richTextBox1.Text += "SETUP ";
                Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
                frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
                frm.ShowDialog();   //顯示 frm 視窗

                //update_default_setting();
            }

            Form1_MouseDown(sender, e);
        }

        void do_upload_work()
        {
            if (flag_upload_enabled == false)
                return;

            richTextBox1.Text += "做上拋工作, 時間 : " + DateTime.Now.ToString() + "\n";

            if (Directory.Exists(upload_source_directory) == false)
            {
                richTextBox1.Text += "上拋來源資料夾 : " + upload_source_directory + ", 不存在, 離開\n";
            }
            if (Directory.Exists(upload_destination_directory) == false)
            {
                richTextBox1.Text += "上拋目的資料夾 : " + upload_destination_directory + ", 不存在, 離開\n";
            }
            string backup_source_directory = upload_source_directory + "_backup";

            //建立備份資料夾
            if (Directory.Exists(backup_source_directory) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(backup_source_directory);
                richTextBox1.Text += "已建立一個新資料夾: " + backup_source_directory + "\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + backup_source_directory + " 已存在，不用再建立\n";
            }

            //開始上拋檔案/資料夾

            //只撈一層的所有檔案
            foreach (string fname in System.IO.Directory.GetFileSystemEntries(upload_source_directory))
            {
                richTextBox1.Text += fname + "\n";
                if (File.Exists(fname))
                {
                    //richTextBox1.Text += "檔案\n";
                    FileInfo fi = new FileInfo(fname);
                    if (fi.Exists == true)      //確認檔案是否存在
                    {
                        //richTextBox1.Text += "檔名：" + fi.Name + "\n";

                        string filename_backup = Path.Combine(backup_source_directory, fi.Name);
                        //richTextBox1.Text += "備份檔名：" + filename_backup + "\n";
                        if (File.Exists(filename_backup) == false)    //確認目標檔案是否存在
                        {
                            File.Copy(fname, filename_backup);
                        }
                        else
                        {
                            richTextBox1.Text += "檔案: " + filename_backup + " 已存在, 無法再拷貝\n";
                        }

                        string filename_upload = Path.Combine(upload_destination_directory, fi.Name);
                        //richTextBox1.Text += "上拋檔名：" + filename_upload + "\n";
                        if (File.Exists(filename_upload) == false)    //確認目標檔案是否存在
                        {
                            File.Move(fname, filename_upload);
                        }
                        else
                        {
                            richTextBox1.Text += "檔案: " + filename_upload + " 已存在, 無法移動\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "檔案: " + fname + " 不存在\n";
                    }
                }
                else if (Directory.Exists(fname))
                {
                    //richTextBox1.Text += "資料夾\n";
                    DirectoryInfo di = new DirectoryInfo(fname);
                    if (di.Exists == true)        //確認資料夾是否存在
                    {
                        //richTextBox1.Text += "資料夾：" + di.Name + "\n";

                        string foldername_backup = Path.Combine(backup_source_directory, di.Name);
                        //richTextBox1.Text += "備份資料夾名：" + foldername_backup + "\n";
                        //Directory..Copy(fname, foldername_backup);  目前無法備份

                        string foldername_upload = Path.Combine(upload_destination_directory, di.Name);
                        //richTextBox1.Text += "上拋資料夾名：" + foldername_upload + "\n";
                        if (Directory.Exists(foldername_upload) == false)    //確認目標資料夾是否存在
                        {
                            Directory.Move(fname, foldername_upload);
                        }
                        else
                        {
                            richTextBox1.Text += "資料夾: " + foldername_upload + " 已存在, 無法移動\n";
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "資料夾: " + fname + " 不存在\n";
                    }
                }
                else
                {
                    richTextBox1.Text += "非合法路徑或檔案\n";
                }
            }
        }
    }
}
