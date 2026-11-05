using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for DriveInfo
using System.Diagnostics;
using System.Globalization;  // for CultureInfo
using System.Runtime.InteropServices;  // for DllImport, StructLayout
using System.Text.RegularExpressions;

/*
磁碟類型DriveType
DriveType.Removable = 2,  // 抽取式存放裝置，例如軟碟機或 USB 快閃磁碟機。
DriveType.Fixed = 3,  // 固定式磁碟。
DriveType.Network = 4,  // 網路磁碟機。
DriveType.CDRom = 5,  // 光碟機，例如 CD 或 DVD-ROM。
DriveType.Ram = 6, //  RAM 磁碟。
*/

namespace vcs_DriveInfo1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //搜尋本機磁碟
            HDD_Scan();

            //------------------------------------------------------------  # 60個

        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            comboBox_drive.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 1 - 30);
            bt_show_disk_info.Location = new Point(x_st + dx * 2 + 130, y_st + dy * 1 - 30);

            pictureBox1.Size = new Size(300, 300);
            pictureBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(550, 380);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 5 - 40);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1000, 750);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void HDD_Scan()
        {
            comboBox_drive.Items.Clear();

            //使用 DriveInfo 類別來顯示目前系統上所有磁片磁碟機的相關資訊
            DriveInfo[] drives = DriveInfo.GetDrives();  // 找磁碟分割區
            foreach (DriveInfo drive in drives)
            {
                comboBox_drive.Items.Add(drive.Name);
            }

            /*   same
            if (comboBox_drive.Items.Count > 0)
                comboBox_drive.Text = comboBox_drive.Items[0].ToString();
            */
            if (drives.Length > 0)
            {
                comboBox_drive.Text = drives[0].ToString();
            }

            //if (comboBox_drive.Items.Count > 0)
            //comboBox_drive.Text = comboBox_drive.Items[0].ToString();

            if (drives.Length > 0)
            {
                comboBox_drive.Text = drives[0].ToString();
            }

            //same
            if (comboBox_drive.Items.Count > 0)
            {
                comboBox_drive.Text = comboBox_drive.Items[0].ToString();
            }
        }

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionTBGBMBKB(Int64 size)
        {
            if (size < 0)
                return "不合法的數值";
            else if (size / TB >= 1024)//如果目前Byte的值大於等於1024TB
                return "無法表示";
            else if (size / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(size / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (size / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(size / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (size / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(size / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (size / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

        private const int WIDTH = 100;
        void drawDiskSpace(long free, long total)
        {
            removeDrawDiskSpace();

            int x_st = 430;
            int y_st = 100;

            //產出panel, 畫硬碟使用空間占比圖
            Panel pnl = new Panel();
            pnl.Left = x_st;
            pnl.Top = y_st;
            pnl.Width = WIDTH;
            pnl.Height = WIDTH;
            pnl.Tag = "show_disk_space";
            pnl.BackColor = Color.Pink;
            this.Controls.Add(pnl);

            Graphics g;
            g = pnl.CreateGraphics();

            // debug
            //Pen p = new Pen(Color.Black, 1);
            //p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            //g.DrawRectangle(p, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100);

            Brush b;
            long used = total - free;

            int used_angle = (int)(used * 360 / total);
            //richTextBox1.Text += "used_angle = " + used_angle.ToString() + "\n";

            b = new SolidBrush(Color.LightGreen);
            g.FillEllipse(b, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100);

            b = new SolidBrush(Color.Red);
            g.FillPie(b, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100, -180, used_angle);

            b = new SolidBrush(Color.White);
            g.FillEllipse(b, WIDTH / 4, WIDTH / 4, WIDTH / 2, WIDTH / 2);
        }

        //移除按鈕部分,  一趟並不會將所有panel上的button回傳, 所以加入while迴圈, 真是神奇驚訝 
        void removeDrawDiskSpace()
        {
            bool flag_do_remove = true;
            while (flag_do_remove == true)
            {
                bool flag_do_remove_this = false;
                foreach (Control con in this.Controls)
                {
                    //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString
                    if (con.Tag != null)
                    {
                        if (con.Tag.ToString() == "show_disk_space")
                        {
                            this.Controls.Remove(con);
                            flag_do_remove_this = true;
                        }
                    }
                }
                if (flag_do_remove_this == false)
                {
                    flag_do_remove = false;
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void comboBox_drive_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "選中 : " + comboBox_drive.Text + "\n";

            //DriveInfo drive = new DriveInfo(comboBox_drive.Text); //same
            DriveInfo drive = new DriveInfo(comboBox_drive.SelectedItem.ToString());
            if (drive.IsReady == true)  // 使用IsReady屬性判斷裝置是否就緒
            {
                richTextBox1.Text += "  檔案系統名稱 : " + drive.DriveFormat + "\n";
                richTextBox1.Text += "  目前可用空間量: \t{0, 15} bytes" + drive.AvailableFreeSpace + "\n";
                richTextBox1.Text += "  可用空間總量: \t{0, 15} bytes" + drive.TotalFreeSpace + "\n";
                richTextBox1.Text += "  可儲存空間總量: \t{0, 15} bytes " + drive.TotalSize + "\n";

                richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                richTextBox1.Text += "名稱 : " + drive.Name + "\n";
                richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                richTextBox1.Text += "類型 : " + drive.DriveType + "\n";
                richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionTBGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t"
                    + ByteConversionTBGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\t( "
                    + ((float)drive.AvailableFreeSpace / (float)drive.TotalSize).ToString("P", CultureInfo.InvariantCulture) + " )\n";
                richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionTBGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";
                richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";

                drawDiskSpace(drive.AvailableFreeSpace, drive.TotalSize);
            }
            else
            {
                richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒\n";
            }

            //another
            // Display information about the selected drive.
            string drive_letter = comboBox_drive.Text.Substring(0, 1);
            richTextBox1.Text += "drive_letter\t" + drive_letter + "\n";

            //DriveInfo
            drive = new DriveInfo(drive_letter);

            richTextBox1.Text += "IsReady\t" + drive.IsReady + "\n";
            richTextBox1.Text += "DriveType\t" + drive.DriveType + "\n";
            richTextBox1.Text += "Name\t" + drive.Name + "\n";
            richTextBox1.Text += "RootDirectory\t" + drive.RootDirectory.Name + "\n";

            if (drive.IsReady)
            {
                richTextBox1.Text += "DriveFormat\t" + drive.DriveFormat + "\n";
                richTextBox1.Text += "AvailableFreeSpace\t" + drive.AvailableFreeSpace.ToString() + "\n";
                richTextBox1.Text += "TotalFreeSize\t" + drive.TotalFreeSpace.ToString() + "\n";
                richTextBox1.Text += "TotalSize\t" + drive.TotalSize.ToString() + "\n";
                richTextBox1.Text += "VolumeLabel\t" + drive.VolumeLabel + "\n";
                richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                richTextBox1.Text += "名稱 : " + drive.Name + "\n";
                richTextBox1.Text += "可用空間 : " + drive.AvailableFreeSpace + "\n";
                richTextBox1.Text += "可用大小 : " + drive.TotalSize + "\n";
                richTextBox1.Text += "可用總空間 : " + drive.TotalFreeSpace + "\n";
                richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                richTextBox1.Text += "型態 : " + drive.DriveType + "\n";
                richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";
            }
            else
            {
                richTextBox1.Text += "磁碟未Ready\n";
                richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_show_disk_info_Click(object sender, EventArgs e)
        {
            draw_drive_info(comboBox_drive.Text);
        }

        void draw_drive_info(string drive_name)
        {
            richTextBox1.Text += drive_name + "\n";
            Graphics g = this.pictureBox1.CreateGraphics();  // 创建Graphics绘图对象
            g.Clear(Color.White);

            DriveInfo drive = new DriveInfo(drive_name);  // 实例化DriveInfo
            if (drive.IsReady == true)  // 使用IsReady屬性判斷裝置是否就緒
            {
                float tsize = drive.TotalSize;  // 获得磁盘的总容量
                float fsize = drive.TotalFreeSpace;  // 获取剩余容量
                Pen pen1 = new Pen(Color.Red);  // 创建画笔对象
                Brush brush1 = new SolidBrush(Color.WhiteSmoke);  // 创建笔刷
                Brush brush2 = new SolidBrush(Color.LimeGreen);  // 创建笔刷
                Brush brush3 = new SolidBrush(Color.RoyalBlue);  // 创建笔刷
                Font font1 = new Font("Courier New", 16, FontStyle.Bold);  // 设置字体
                Font font2 = new Font("標楷體", 9);  // 设置字体
                g.DrawString("磁碟容量分析", font1, brush2, new Point(60, 50));  // 绘制文本
                float angle1 = Convert.ToSingle((360 * (Convert.ToSingle(fsize / 100000000000) / Convert.ToSingle(tsize / 100000000000))));  // 计算绿色饼形图的范围
                float angle2 = Convert.ToSingle((360 * (Convert.ToSingle((tsize - fsize) / 100000000000) / Convert.ToSingle(tsize / 100000000000))));  // 计算蓝色饼形图的范围
                // 调用Graphics对象的FillPie方法绘制饼形图
                g.FillPie(brush2, 60, 80, 150, 150, 0, angle1);
                g.FillPie(brush3, 60, 80, 150, 150, angle1, angle2);
                g.DrawRectangle(pen1, 30, 235, 200, 50);
                g.FillRectangle(brush2, 35, 245, 20, 10);
                g.DrawString("磁碟剩餘容量:" + drive.TotalFreeSpace / 1000 + "KB", font2, brush2, 55, 245);
                g.FillRectangle(brush3, 35, 265, 20, 10);
                g.DrawString("磁碟已用容量:" + (drive.TotalSize - drive.TotalFreeSpace) / 1000 + "KB", font2, brush3, 55, 265);
            }
            else
            {
                richTextBox1.Text += "硬碟 : " + drive_name + " 未Ready\n";
                g.DrawString("硬碟 : " + drive_name + " 未Ready", new Font("標楷體", 24), new SolidBrush(Color.Blue), new PointF(10, 60));
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

