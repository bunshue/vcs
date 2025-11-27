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

            // 找磁碟分割區
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
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";

            DirectoryInfo dir = new DirectoryInfo(foldername);
            if (!dir.Exists)  //判斷資料夾路徑是否不存在
            {
                richTextBox1.Text += "路徑不存在\n";
            }
            richTextBox1.Text += dir.FullName + "資料夾下的檔案資訊如下：\n";

            //傳回FileInfo物件陣列，並指定給f陣列
            FileInfo[] f = dir.GetFiles();
            foreach (FileInfo r in f)
            {
                richTextBox1.Text += "完整路徑：" + r.FullName + "\n";
                richTextBox1.Text += "寫入時間：" + r.LastWriteTime + "\n";
                richTextBox1.Text += "檔案大小：" + r.Length.ToString() + "\n";
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = Path.Combine(Application.StartupPath, @"..\..\Form1.cs");

            richTextBox1.Text += "filename old = " + filename + "\n";

            string d_name = Path.GetDirectoryName(filename);
            string f_name = Path.GetFileNameWithoutExtension(filename);
            string ext_name = Path.GetExtension(filename);

            richTextBox1.Text += "取得 d_name : " + d_name + "\n";
            richTextBox1.Text += "取得 f_name : " + f_name + "\n";
            richTextBox1.Text += "取得 ext_name : " + ext_name + "\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU";
            var dinfo = new DirectoryInfo(foldername);
            var files = dinfo.GetFiles().OrderBy(p => p.Name).ToArray();
            foreach (var file in files)
            {
                if (file.FullName.Contains("id_card") == true)
                {
                    Console.WriteLine(file.FullName);

                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }
    }
}

