using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;            //for DriveInfo
using System.Globalization; //for CultureInfo

namespace vcs_DriveInfo2
{
    public partial class Form1 : Form
    {
        bool flag_debug_mode = false;

        private const int THRESHOLD = 20;
        Bitmap bitmap1 = null;
        Graphics g;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.richTextBox1.Visible = false;
            this.Text = "使用 DriveInfo 類別取得磁碟資訊";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            get_disk_info();
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
                return (Math.Round(KSize / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return KSize.ToString() + " Byte";//顯示Byte值
        }

        void drawDiskSpace(int cx, int cy, int r, string name, long free, long total)
        {
            bool flag_disk_free_low = false;
            if ((free * 100 / total) < THRESHOLD)
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

            int w = 100 * total_drives + 1;
            int h = 320;
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

                    drawDiskSpace(cx, cy, r, di.Name, free, total);

                    if ((free * 100 / total) < THRESHOLD)
                    {
                        //richTextBox1.Text += "str = " + ((float)free / (float)total).ToString() + "\n";
                        warning_directory.Add(di.Name);
                    }

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
                g.DrawString("磁碟 : " + warning + " 容量不足", new Font("標楷體", 18), new SolidBrush(Color.Red), new Point(10, 195));
            }

            if (flag_debug_mode == false)
            {
                int W = Screen.PrimaryScreen.Bounds.Width;
                int H = Screen.PrimaryScreen.Bounds.Height;

                this.BackColor = Color.Pink;
                this.ClientSize = new Size(w, h - 62);
                this.Location = new Point(W - w - 9, H / 2);
            }
            else
            {
                this.BackColor = Color.Pink;
                this.ClientSize = new Size(w + 300, h - 62 + 400);
                //this.Location = new Point(1920 - w - 16, 1080 / 2);

            }


        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            if ((cnt % 3600) == 0)
            {
                get_disk_info();
            }
        }
    }
}
