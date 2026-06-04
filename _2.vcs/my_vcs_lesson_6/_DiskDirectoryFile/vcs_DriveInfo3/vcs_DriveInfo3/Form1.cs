using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for DriveInfo
using System.Globalization;  // for CultureInfo
using System.Runtime.InteropServices;  // for DllImport, StructLayout

namespace vcs_DriveInfo3
{
    public partial class Form1 : Form
    {
        [DllImport("kernel32.dll")]
        private static extern bool GetDiskFreeSpaceEx(string lpDirectoryName, out ulong lpFreeBytesAvailable, out ulong lpTotalNumberOfBytes, out ulong lpTotalNumberOfFreeBytes);

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
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            comboBox_drive.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            richTextBox1.Size = new Size(450, 690 - 140);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(900, 750);
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
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo d in drives)
            {
                comboBox_drive.Items.Add(d.Name);
            }

            /*  same
            foreach (DriveInfo d in DriveInfo.GetDrives())
            {
                comboBox_drive.Items.Add(d.Name);
            }
            */

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


        private const int WIDTH = 100;
        void drawDiskSpace(long free, long total)
        {
            removeDrawDiskSpace();

            //產出panel, 畫硬碟使用空間占比圖
            Panel pnl = new Panel();
            pnl.Left = this.ClientSize.Width - WIDTH - 10;
            pnl.Top = 10;
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

        private void button0_Click(object sender, EventArgs e)
        {
            ulong freesize;
            freesize = GetFreeSpace("C");
            richTextBox1.Text += "磁碟C剩餘空間: " + freesize.ToString() + " bytes\n";
            freesize = GetFreeSpace("D");
            richTextBox1.Text += "磁碟D剩餘空間: " + freesize.ToString() + " bytes\n";
            freesize = GetFreeSpace("G");
            richTextBox1.Text += "磁碟G剩餘空間: " + freesize.ToString() + " bytes\n";
        }

        /// <summary>
        /// 取得磁碟剩餘空間
        /// </summary>
        /// <param name="driveDirectoryName">驅動器名</param>
        /// <returns>剩餘空間</returns>
        private static ulong GetFreeSpace(string driveDirectoryName)
        {
            ulong freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;
            if (!driveDirectoryName.EndsWith(":\\"))
            {
                driveDirectoryName += ":\\";
            }
            GetDiskFreeSpaceEx(driveDirectoryName, out freeBytesAvailable, out totalNumberOfBytes, out totalNumberOfFreeBytes);
            return freeBytesAvailable;
        }

        //------------------------------------------------------------  # 60個

        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);
        private void button1_Click(object sender, EventArgs e)
        {
            //取得本機或網路磁碟機的磁碟訊息, 選擇磁碟或目錄
            FolderBrowserDialog fbd = new FolderBrowserDialog();
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                long fb, ftb, tfb;
                string str = fbd.SelectedPath;
                richTextBox1.Text += "path : " + str + "\n";
                if (GetDiskFreeSpaceEx(str, out fb, out ftb, out tfb) != 0)
                {
                    string strfb = Convert.ToString(fb / 1024 / 1024 / 1024) + " G";
                    string strftb = Convert.ToString(ftb / 1024 / 1024 / 1024) + " G";
                    string strtfb = Convert.ToString(tfb / 1024 / 1024 / 1024) + " G";
                    richTextBox1.Text += "總空間" + strfb + "\n";
                    richTextBox1.Text += "可用空間" + strftb + "\n";
                    richTextBox1.Text += "總剩餘空間" + strtfb + "\n";
                }
                else
                {
                    MessageBox.Show("NO");
                }
            }
        }

        //------------------------------------------------------------  # 60個

        //取得硬碟資訊 ST
        // TBD [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        // TBD public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);

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

        private void button2_Click(object sender, EventArgs e)
        {
            //取得硬碟資訊
            long fb, ftb, tfb;
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__RW\_excel";

            //this.textBox4.Text = foldername;
            richTextBox1.Text += "get : " + foldername + "\n";
            if (GetDiskFreeSpaceEx(foldername, out fb, out ftb, out tfb) != 0)
            {
                richTextBox1.Text += "磁碟總容量：" + ByteConversionTBGBMBKB(Convert.ToInt64(ftb)) + "\n";
                richTextBox1.Text += "可用磁碟空間：" + ByteConversionTBGBMBKB(Convert.ToInt64(fb)) + "\n";
                richTextBox1.Text += "磁碟剩餘空間：" + ByteConversionTBGBMBKB(Convert.ToInt64(tfb)) + "\n";
            }
            else
            {
                MessageBox.Show("NO");
            }
        }
        //取得硬碟資訊 SP

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
            //GetLogicalDrives 1
            // 取得目前本機所有的磁碟機, GetLogicalDrives

            richTextBox1.Text += "列出Logical Drives\n";
            foreach (string drive in Environment.GetLogicalDrives())
            {
                richTextBox1.Text += "\t" + drive + "\n";
            }

            string[] drives = Environment.GetLogicalDrives();
            richTextBox1.Text += "系統磁碟機：" + string.Join(", ", drives) + "\n";

            richTextBox1.Text += string.Format("系統磁碟機：{0}", string.Join(", ", drives)) + "\n";

            //取得所有邏輯分區
            //取得本地磁盤目錄
            richTextBox1.Text += "取得所有邏輯分區\n";
            string[] logicdrives = Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                richTextBox1.Text += "取得: " + logicdrives[i] + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            //GetLogicalDrives 2
            //顯示所有邏輯磁碟機
            GetLogicalDrives();
        }

        // Print out all logical drives on the system.
        void GetLogicalDrives()
        {
            try
            {
                string[] drives = System.IO.Directory.GetLogicalDrives();

                foreach (string str in drives)
                {
                    System.Console.WriteLine(str);
                    richTextBox1.Text += "drive : " + str + "\n";
                }
            }
            catch (System.IO.IOException)
            {
                System.Console.WriteLine("An I/O error occurs.");
            }
            catch (System.Security.SecurityException)
            {
                System.Console.WriteLine("The caller does not have the required permission.");
            }
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            //GetLogicalDrives 3
            string[] drive = Environment.GetLogicalDrives();
            for (int i = 0; i < drive.Length; i++)
            {
                richTextBox1.Text += "磁碟名稱 :" + drive[i] + "\n";
                richTextBox1.Text += "全部大小 :" + GetHardDiskTotalSize(i).ToString() + " G" + "\n";
                richTextBox1.Text += "可用大小 :" + GetHardDiskFreeSize(i).ToString() + " G" + "\n";
            }
        }

        /// <summary>
        /// 獲取磁盤總空間
        /// </summary>
        /// <param name="i">獲取磁盤需要的下標 0 c盤 1 d盤</param>
        /// <returns>磁盤總空間 long類型</returns>
        public static long GetHardDiskTotalSize(int i)
        {
            long totalSize = new long();
            System.IO.DriveInfo[] drives = System.IO.DriveInfo.GetDrives();
            if (drives[i].IsReady == true)
            {
                totalSize = drives[i].TotalSize / (1024L * 1024 * 1024);
                return totalSize;
            }
            else
                return 0;
        }

        public static long GetHardDiskFreeSize(int i)
        {
            long freeSize = new long();
            System.IO.DriveInfo[] drives = System.IO.DriveInfo.GetDrives();
            if (drives[i].IsReady == true)
            {
                freeSize = drives[i].AvailableFreeSpace / (1024 * 1024 * 1024);
                return freeSize;
            }
            else
            {
                return 0;
            }
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //取得磁碟資訊
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

            //取得單一磁碟資訊：
            //System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\");

            //取得所有磁碟資訊：
            foreach (DriveInfo drive in allDrives)
            {
                richTextBox1.Text += "磁碟分割號:  " + drive.Name + " 槽\n";
                richTextBox1.Text += "RootDirectory:  " + drive.RootDirectory + "\n";
                richTextBox1.Text += "DriveType:  " + drive.DriveType;
                if (drive.IsReady == true)  //使用IsReady屬性判斷裝置是否就緒
                {
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

            String result = "";
            foreach (DriveInfo di in DriveInfo.GetDrives())
            {
                //取得磁碟的資訊，並逐一列出
                if (di.IsReady)
                    //表示有東西，若不是可能是光碟、軟碟機
                    result += String.Format("{0}\t{1}\t{2}\t{3}\r\n", di.Name, di.DriveType, di.TotalSize, di.TotalFreeSpace);
                //印出資訊
                else
                    result += String.Format("{0}\t{1}\r\n", di.Name, di.DriveType);
            }
            richTextBox1.Text += result + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            //找資料夾所在的硬碟的標籤
            //找資料夾所在的硬碟的標籤
            string path = String.Empty;

            path = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            richTextBox1.Text += "\n資料夾路徑" + path + "\n";

            if (File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "是個檔案\n";
            }
            else if (Directory.Exists(path))
            {
                DirectoryInfo d = new DirectoryInfo(path);//輸入檔案夾
                /*
                // This path is a directory
                richTextBox1.Text += "Name : " + d.Name + "\n";
                richTextBox1.Text += "FullName : " + d.FullName + "\n";
                richTextBox1.Text += "Parent : " + d.Parent + "\n";
                richTextBox1.Text += "Root : " + d.Root + "\n";
                */

                DriveInfo drive = new DriveInfo(d.Root.ToString());

                if (drive.IsReady == true)
                {
                    richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                    richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                    //richTextBox1.Text += "名稱 : " + drive.Name + "\n";
                    richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                    richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t"
                        + ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\t( "
                        + ((float)drive.AvailableFreeSpace / (float)drive.TotalSize).ToString("P", CultureInfo.InvariantCulture) + " )\n";
                    richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";
                    /*
                    richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                    richTextBox1.Text += "型態 : " + drive.DriveType + "\n";
                    richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒\n";
                }
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void comboBox_drive_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "選中 : " + comboBox_drive.Text + "\n";
            //richTextBox1.Clear();
            //DriveInfo drive = new DriveInfo(comboBox_drive.Text); //same
            DriveInfo drive = new DriveInfo(comboBox_drive.SelectedItem.ToString());
            if (drive.IsReady == true)
            {
                richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                richTextBox1.Text += "名稱 : " + drive.Name + "\n";
                richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                richTextBox1.Text += "類型 : " + drive.DriveType + "\n";
                richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t"
                    + ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\t( "
                    + ((float)drive.AvailableFreeSpace / (float)drive.TotalSize).ToString("P", CultureInfo.InvariantCulture) + " )\n";
                richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";
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

            DriveInfo di = new DriveInfo(drive_letter);

            richTextBox1.Text += "IsReady\t" + di.IsReady + "\n";
            richTextBox1.Text += "DriveType\t" + di.DriveType + "\n";
            richTextBox1.Text += "Name\t" + di.Name + "\n";
            richTextBox1.Text += "RootDirectory\t" + di.RootDirectory.Name + "\n";

            if (di.IsReady)
            {
                richTextBox1.Text += "DriveFormat\t" + di.DriveFormat + "\n";
                richTextBox1.Text += "AvailableFreeSpace\t" + di.AvailableFreeSpace.ToString() + "\n";
                richTextBox1.Text += "TotalFreeSize\t" + di.TotalFreeSpace.ToString() + "\n";
                richTextBox1.Text += "TotalSize\t" + di.TotalSize.ToString() + "\n";
                richTextBox1.Text += "VolumeLabel\t" + di.VolumeLabel + "\n";
            }
            else
            {
                richTextBox1.Text += "磁碟未Ready\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            //僅有類別, 還不會用

            IDE ide = new IDE();
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

    }

    //讀硬盤序列號
    public class IDE
    {
        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        internal struct IDSECTOR
        {
            public ushort wGenConfig;
            public ushort wNumCyls;
            public ushort wReserved;
            public ushort wNumHeads;
            public ushort wBytesPerTrack;
            public ushort wBytesPerSector;
            public ushort wSectorsPerTrack;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
            public ushort[] wVendorUnique;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 20)]
            public string sSerialNumber;
            public ushort wBufferType;
            public ushort wBufferSize;
            public ushort wECCSize;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string sFirmwareRev;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 40)]
            public string sModelNumber;
            public ushort wMoreVendorUnique;
            public ushort wDoubleWordIO;
            public ushort wCapabilitIEs;
            public ushort wReserved1;
            public ushort wPIOTiming;
            public ushort wDMATiming;
            public ushort wBS;
            public ushort wNumCurrentCyls;
            public ushort wNumCurrentHeads;
            public ushort wNumCurrentSectorsPerTrack;
            public uint ulCurrentSectorCapacity;
            public ushort wMultSectorStuff;
            public uint ulTotalAddressableSectors;
            public ushort wSingleWordDMA;
            public ushort wMultiWordDMA;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 128)]
            public byte[] bReserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct DRIVERSTATUS
        {
            public byte bDriverError;
            public byte bIDEStatus;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
            public byte[] bReserved;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 2)]
            public uint[] dwReserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct SENDCMDOUTPARAMS
        {
            public uint cBufferSize;
            public DRIVERSTATUS DriverStatus;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 513)]
            public byte[] bBuffer;
        }

        [StructLayout(LayoutKind.Sequential, CharSet = CharSet.Ansi)]
        internal struct SRB_IO_CONTROL
        {
            public uint HeaderLength;
            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 8)]
            public string Signature;
            public uint Timeout;
            public uint ControlCode;
            public uint ReturnCode;
            public uint Length;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct IDEREGS
        {
            public byte bFeaturesReg;
            public byte bSectorCountReg;
            public byte bSectorNumberReg;
            public byte bCylLowReg;
            public byte bCylHighReg;
            public byte bDriveHeadReg;
            public byte bCommandReg;
            public byte bReserved;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct SENDCMDINPARAMS
        {
            public uint cBufferSize;
            public IDEREGS irDriveRegs;
            public byte bDriveNumber;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 3)]
            public byte[] bReserved;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
            public uint[] dwReserved;
            public byte bBuffer;
        }

        [StructLayout(LayoutKind.Sequential)]
        internal struct GETVERSIONOUTPARAMS
        {
            public byte bVersion;
            public byte bRevision;
            public byte bReserved;
            public byte bIDEDeviceMap;
            public uint fCapabilitIEs;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 4)]
            public uint[] dwReserved; // For future use.
        }

        [DllImport("kernel32.dll")]
        private static extern int CloseHandle(uint hObject);

        [DllImport("kernel32.dll")]
        private static extern int DeviceIoControl(uint hDevice,
        uint dwIoControlCode,
        ref SENDCMDINPARAMS lpInBuffer,
        int nInBufferSize,
        ref SENDCMDOUTPARAMS lpOutBuffer,
        int nOutBufferSize,
        ref uint lpbytesReturned,
        int lpOverlapped);

        [DllImport("kernel32.dll")]
        private static extern int DeviceIoControl(uint hDevice,
        uint dwIoControlCode,
        int lpInBuffer,
        int nInBufferSize,
        ref GETVERSIONOUTPARAMS lpOutBuffer,
        int nOutBufferSize,
        ref uint lpbytesReturned,
        int lpOverlapped);

        [DllImport("kernel32.dll")]
        private static extern uint CreateFile(string lpFileName,
        uint dwDesiredAccess,
        uint dwShareMode,
        int lpSecurityAttributes,
        uint dwCreationDisposition,
        uint dwFlagsAndAttributes,
        int hTemplateFile);

        private const uint GENERIC_READ = 0x80000000;
        private const uint GENERIC_WRITE = 0x40000000;
        private const uint FILE_SHARE_READ = 0x00000001;
        private const uint FILE_SHARE_WRITE = 0x00000002;
        private const uint OPEN_EXISTING = 3;
        private const uint INVALID_HANDLE_VALUE = 0xffffffff;
        private const uint DFP_GET_VERSION = 0x00074080;
        private const int IDE_ATAPI_IDENTIFY = 0xA1; // Returns ID sector for ATAPI.
        private const int IDE_ATA_IDENTIFY = 0xEC; // Returns ID sector for ATA.
        private const int IDENTIFY_BUFFER_SIZE = 512;
        private const uint DFP_RECEIVE_DRIVE_DATA = 0x0007c088;

        public static string Read(byte drive)
        {
            OperatingSystem os = Environment.OSVersion;
            if (os.Platform != PlatformID.Win32NT) throw new NotSupportedException("僅支持WindowsNT/2000/XP");
            //我沒有NT4，請哪位大大測試一下NT4下能不能用
            //if (os.Version.Major < 5) throw new NotSupportedException("僅支持WindowsNT/2000/XP");

            string driveName = "\\\\.\\PhysicalDrive" + drive.ToString();
            uint device = CreateFile(driveName,
            GENERIC_READ | GENERIC_WRITE,
            FILE_SHARE_READ | FILE_SHARE_WRITE,
            0, OPEN_EXISTING, 0, 0);
            if (device == INVALID_HANDLE_VALUE) return "";
            GETVERSIONOUTPARAMS verPara = new GETVERSIONOUTPARAMS();
            uint bytRv = 0;

            if (0 != DeviceIoControl(device, DFP_GET_VERSION,
            0, 0, ref verPara, Marshal.SizeOf(verPara),
            ref bytRv, 0))
            {
                if (verPara.bIDEDeviceMap > 0)
                {
                    byte bIDCmd = (byte)(((verPara.bIDEDeviceMap >> drive & 0x10) != 0) ? IDE_ATAPI_IDENTIFY : IDE_ATA_IDENTIFY);
                    SENDCMDINPARAMS scip = new SENDCMDINPARAMS();
                    SENDCMDOUTPARAMS scop = new SENDCMDOUTPARAMS();

                    scip.cBufferSize = IDENTIFY_BUFFER_SIZE;
                    scip.irDriveRegs.bFeaturesReg = 0;
                    scip.irDriveRegs.bSectorCountReg = 1;
                    scip.irDriveRegs.bCylLowReg = 0;
                    scip.irDriveRegs.bCylHighReg = 0;
                    scip.irDriveRegs.bDriveHeadReg = (byte)(0xA0 | ((drive & 1) << 4));
                    scip.irDriveRegs.bCommandReg = bIDCmd;
                    scip.bDriveNumber = drive;

                    if (0 != DeviceIoControl(device, DFP_RECEIVE_DRIVE_DATA,
                    ref scip, Marshal.SizeOf(scip), ref scop,
                    Marshal.SizeOf(scop), ref bytRv, 0))
                    {
                        StringBuilder s = new StringBuilder();
                        for (int i = 20; i < 40; i += 2)
                        {
                            s.Append((char)(scop.bBuffer[i + 1]));
                            s.Append((char)scop.bBuffer[i]);
                        }
                        CloseHandle(device);
                        return s.ToString().Trim();
                    }
                }
            }
            CloseHandle(device);
            return "";
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/




/*
dddd
取得硬碟資訊
            System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\");
            richTextBox1.Text += "TotalFreeSpace : " + di.TotalFreeSpace.ToString() + "\n";
            richTextBox1.Text += "VolumeLabel : " + di.VolumeLabel + "\n";

*/


