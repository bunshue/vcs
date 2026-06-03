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
            show_item_location();

            //------------------------------------------------------------  # 60個

            // 找磁碟分割區
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo drive in drives)
            {
                comboBox1.Items.Add(drive.ToString());
                richTextBox1.Text += "抓到磁碟分割區 : " + drive.ToString() + "\n";
            }

            if (comboBox1.Items.Count > 0)
            {
                comboBox1.SelectedIndex = 0;
            }
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            //richTextBox1.Size = new Size(300, 690);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1273, 750);
            this.Text = "vcs_DriveInfo1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個


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

        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //DriveInfo測試

            DriveInfo[] allDrives = DriveInfo.GetDrives();

            foreach (DriveInfo d in allDrives)
            {
                richTextBox1.Text += "磁碟名稱 : " + d.Name + "\n";
                richTextBox1.Text += "  磁碟類型 : " + d.DriveType + "\n";
                if (d.IsReady == true)
                {
                    richTextBox1.Text += "  檔案系統名稱 : " + d.DriveFormat + "\n";
                    richTextBox1.Text += "  目前可用空間量: \t{0, 15} bytes" + d.AvailableFreeSpace + "\n";
                    richTextBox1.Text += "  可用空間總量: \t{0, 15} bytes" + d.TotalFreeSpace + "\n";
                    richTextBox1.Text += "  可儲存空間總量: \t{0, 15} bytes " + d.TotalSize + "\n";
                }
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //偵測磁碟裝置型態

            DriveInfo[] allDrives = DriveInfo.GetDrives();

            foreach (DriveInfo d in allDrives)
            {
                richTextBox1.Text += "Drive : " + d.Name + "\tFile type : " + d.DriveType + "\n";
                if (d.DriveType == DriveType.Removable)
                {
                    richTextBox1.Text += "Removable Device : " + d.Name + "\n";
                }
            }

            //獲取計算機磁盤空間
            //在System.IO命名空間下的DriveInfo類的GetDrives()方法可以用來獲得計算機上的所有邏輯驅動器的名稱。DriveInfo類的TotalSize屬性可義獲得磁盤的空間大小。

            for (int i = 0; i < allDrives.Length; i++)
            {
                richTextBox1.Text += "取得磁碟 : " + allDrives[i].Name;

                if (allDrives[i].IsReady == true)
                {
                    richTextBox1.Text += "\t空間 : " + Convert.ToString(allDrives[i].TotalSize / 1024 / 1024 / 1024) + "GB\n";
                }
                else
                {
                    richTextBox1.Text += "\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

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
