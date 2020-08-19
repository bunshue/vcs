using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;            //for DriveInfo
using System.Management;    //for ManagementObject, 需加入參考System.Management

using System.Globalization; //for CultureInfo

namespace vcs_DriveInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void HDD_Scan()
        {
            comboBox_drive.Items.Clear();   //Clear All items in Combobox

            //使用 DriveInfo 類別來顯示目前系統上所有磁片磁碟機的相關資訊
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo d in drives)
            {
                comboBox_drive.Items.Add(d.Name);
            }

            /*   same
            if (comboBox_drive.Items.Count > 0)
                comboBox_drive.Text = comboBox_drive.Items[0].ToString();
            */
            if (drives.Length > 0)
                comboBox_drive.Text = drives[0].ToString();


            /*
            //法一
            comboBox_drive.Items.Clear();   //Clear All items in Combobox
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo drive in drives)
            {
                comboBox_drive.Items.Add(drive.ToString());
            }

            // same
            //if (comboBox_drive.Items.Count > 0)
                //comboBox_drive.Text = comboBox_drive.Items[0].ToString();

            if (drives.Length > 0)
                comboBox_drive.Text = drives[0].ToString();
			*/
            //法二
            comboBox_drive.Items.Clear();
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in searcher.Get())
            {
                comboBox_drive.Items.Add(disk["Name"].ToString());
            }

            if (comboBox_drive.Items.Count > 0)
                comboBox_drive.Text = comboBox_drive.Items[0].ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            HDD_Scan();
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            HDD_Scan();
        }

        private void button3_Click(object sender, EventArgs e)
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
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //找資料夾所在的硬碟的標籤
            string path = String.Empty;

            path = "C:\\______test_files\\_case1";

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

        private const int WIDTH = 100;
        void drawDiskSpace(long free, long total)
        {
            removeDrawDiskSpace();

            //產出panel, 畫硬碟使用空間占比圖
            Panel pnl = new Panel();
            pnl.Left = richTextBox1.Location.X + richTextBox1.Width - WIDTH - 30;
            pnl.Top = 10;
            pnl.Width = WIDTH;
            pnl.Height = WIDTH;
            pnl.Tag = "dynamic";
            pnl.BackColor = Color.White;
            //this.Controls.Add(pnl);
            this.richTextBox1.Controls.Add(pnl);

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
                foreach (Control con in this.richTextBox1.Controls)
                {
                    //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString
                    if (con.Tag != null)
                    {
                        if (con.Tag.ToString() == "dynamic")
                        {
                            this.richTextBox1.Controls.Remove(con);
                            flag_do_remove_this = true;
                        }
                    }
                }
                if (flag_do_remove_this == false)
                    flag_do_remove = false;
            }
        }





    }
}
