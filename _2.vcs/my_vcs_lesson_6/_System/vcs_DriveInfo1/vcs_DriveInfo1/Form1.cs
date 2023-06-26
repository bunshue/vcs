using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Runtime.InteropServices;
using System.Management;    //參考/加入參考/.NET/System.Management

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
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            /*
            // 找磁碟分割區方法一, 要用System.Management
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");//查询磁盘信息
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);//创建WMI查询对象
            foreach (ManagementObject disk in searcher.Get())//遍历所有磁盘
            {
                comboBox1.Items.Add(disk["Name"].ToString());//将磁盘名称添加到下拉列表中
                richTextBox1.Text += "抓到磁碟分割區 : " + disk["Name"].ToString() + "\n";
            }
            */

            // 找磁碟分割區方法二
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo drive in drives)
            {
                comboBox1.Items.Add(drive.ToString());
                richTextBox1.Text += "抓到磁碟分割區 : " + drive.ToString() + "\n";
            }

            if (comboBox1.Items.Count > 0)
                comboBox1.SelectedIndex = 0;
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            DriveInfo drive = new DriveInfo(comboBox1.SelectedItem.ToString());
            if (drive.IsReady)
            {
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
                richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {

            draw_drive_info(comboBox1.Text);
        }

        void draw_drive_info(string drive)
        {
            DriveInfo dinfo = new DriveInfo(drive);//实例化DriveInfo
            if (dinfo.IsReady == true)
            {
                float tsize = dinfo.TotalSize;//获得磁盘的总容量
                float fsize = dinfo.TotalFreeSpace;//获取剩余容量
                Graphics g = this.CreateGraphics();//创建Graphics绘图对象
                g.Clear(Color.White);
                Pen pen1 = new Pen(Color.Red);//创建画笔对象
                Brush brush1 = new SolidBrush(Color.WhiteSmoke);//创建笔刷
                Brush brush2 = new SolidBrush(Color.LimeGreen);//创建笔刷
                Brush brush3 = new SolidBrush(Color.RoyalBlue);//创建笔刷
                Font font1 = new Font("Courier New", 16, FontStyle.Bold);//设置字体
                Font font2 = new Font("標楷體", 9);//设置字体
                g.DrawString("磁碟容量分析", font1, brush2, new Point(60, 50));//绘制文本
                float angle1 = Convert.ToSingle((360 * (Convert.ToSingle(fsize / 100000000000) / Convert.ToSingle(tsize / 100000000000))));//计算绿色饼形图的范围
                float angle2 = Convert.ToSingle((360 * (Convert.ToSingle((tsize - fsize) / 100000000000) / Convert.ToSingle(tsize / 100000000000))));//计算蓝色饼形图的范围
                //调用Graphics对象的FillPie方法绘制饼形图
                g.FillPie(brush2, 60, 80, 150, 150, 0, angle1);
                g.FillPie(brush3, 60, 80, 150, 150, angle1, angle2);
                g.DrawRectangle(pen1, 30, 235, 200, 50);
                g.FillRectangle(brush2, 35, 245, 20, 10);
                g.DrawString("磁碟剩餘容量:" + dinfo.TotalFreeSpace / 1000 + "KB", font2, brush2, 55, 245);
                g.FillRectangle(brush3, 35, 265, 20, 10);
                g.DrawString("磁碟已用容量:" + (dinfo.TotalSize - dinfo.TotalFreeSpace) / 1000 + "KB", font2, brush3, 55, 265);
            }
            else
            {
                richTextBox1.Text += "硬碟 : " + drive + " 未Ready\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲得硬盤序號

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            string strHardDiskID = "";
            foreach (ManagementObject mo in mos.Get())
            {
                strHardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            richTextBox1.Text += "獲得硬盤序號 : " + strHardDiskID + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //檢查硬碟容量
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject mo in mos.Get())
            {
                string disk_name = mo["Name"].ToString();
                richTextBox1.Text += "取得硬碟 : " + disk_name + "\n";

                DriveInfo dinfo = new DriveInfo(disk_name);
                if (dinfo.IsReady == true)
                {
                    richTextBox1.Text += "驅動器總容量：" + dinfo.TotalSize + " B\n";
                    richTextBox1.Text += "驅動器剩餘容量：" + dinfo.TotalFreeSpace + " B\n"; ;
                }
            }
        }

        //取得硬碟資訊 ST
        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);

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

        private void button4_Click(object sender, EventArgs e)
        {
            //取得硬碟資訊
            //取得硬碟資訊
            long fb, ftb, tfb;
            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__RW\_excel";

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
    }
}

