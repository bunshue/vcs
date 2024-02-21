using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//各種 listView 之加入資料
//簡單的加入資料  不含各種方法


namespace vcs_ListView1
{
    public partial class Form1 : Form
    {
        ListView listView1 = new ListView();
        RichTextBox richTextBox1 = new RichTextBox();

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
            listView1.Size = new Size(500, 600);
            this.Controls.Add(listView1);

            richTextBox1.Size = new Size(350, 600);
            this.Controls.Add(richTextBox1);

            this.Size = new Size(1120, 700);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 170 + 10;
            dy = 70 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立listView 0
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立listView 1
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //建立listView 2
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //建立listView 3
            richTextBox1.Text += "羅列出磁盤信息 在 listView 上\n";
            listView1.Clear();
            apply_listView3();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //建立listView 4
            richTextBox1.Text += "顯示本機文件夾及文件在ListView上\n";
            listView1.Clear();
            apply_listView4();

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //建立listView 5

            richTextBox1.Text += "在ListView加入圖片\n";
            listView1.Clear();
            apply_listView5();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //建立listView 6

        }

        private void button7_Click(object sender, EventArgs e)
        {
            listView1.Clear();
        }




        void apply_listView3()
        {
            listView1.View = View.Details;

            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "Disk Name";
            ch1.Width = 85;
            listView1.Columns.Add(ch1);
            ColumnHeader ch2 = new ColumnHeader();
            ch2.Text = "Type";
            ch2.Width = 85;
            listView1.Columns.Add(ch2);
            ColumnHeader ch3 = new ColumnHeader();
            ch3.Text = "All Size";
            ch3.Width = 85;
            listView1.Columns.Add(ch3);
            ColumnHeader ch4 = new ColumnHeader();
            ch4.Text = "Free Size";
            ch4.Width = 85;
            listView1.Columns.Add(ch4);
            string[] drive = Environment.GetLogicalDrives();
            for (int i = 0; i < drive.Length; i++)
            {
                //實例化一個listview對象的子項
                ListViewItem lvi1 = new ListViewItem();
                lvi1.Text = drive[i];//第一列數據
                lvi1.SubItems.Add(i.ToString());//第二列
                lvi1.SubItems.Add(GetHardDiskTotalSize(i).ToString() + " G");//第三列
                lvi1.SubItems.Add(GetHardDiskFreeSize(i).ToString() + " G");//第四列
                listView1.Items.Add(lvi1);//添加列
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

        void apply_listView4()
        {
            listView1.View = View.Details;

            createHeadersAndFillListView();

            string foldername = @"C:\_git\vcs\_1.data\______test_files1";

            ShowListView(foldername);
        }

        void createHeadersAndFillListView()
        {
            ColumnHeader colHead;
            colHead = new ColumnHeader();
            colHead.Text = "Filename";
            colHead.Width = 200;
            colHead.TextAlign = HorizontalAlignment.Left;
            listView1.Columns.Add(colHead);

            colHead = new ColumnHeader();
            colHead.Text = "Size";
            colHead.Width = 100;
            colHead.TextAlign = HorizontalAlignment.Left;
            listView1.Columns.Add(colHead);

            colHead = new ColumnHeader();
            colHead.Text = "Last Accessed";
            colHead.Width = 200;
            colHead.TextAlign = HorizontalAlignment.Left;
            listView1.Columns.Add(colHead);
        }

        void ShowListView(string root)
        {
            try
            {
                ListViewItem lvi;
                ListViewItem.ListViewSubItem lvsi;

                if (root.CompareTo("") == 0)
                    return;
                DirectoryInfo dir = new DirectoryInfo(root);
                DirectoryInfo[] dirs = dir.GetDirectories();
                FileInfo[] files = dir.GetFiles();

                //顯示本機文件夾及文件

                listView1.Items.Clear();

                //labPathName.Text = root;
                listView1.BeginUpdate();

                foreach (DirectoryInfo di in dirs)
                {
                    lvi = new ListViewItem();
                    lvi.Text = di.Name;
                    lvi.ImageIndex = 0;
                    lvi.Tag = di.FullName;

                    lvsi = new ListViewItem.ListViewSubItem();
                    lvsi.Text = "";

                    lvi.SubItems.Add(lvsi);

                    lvsi = new ListViewItem.ListViewSubItem();
                    lvsi.Text = di.LastAccessTime.ToString();
                    lvi.SubItems.Add(lvsi);

                    listView1.Items.Add(lvi);
                }

                foreach (FileInfo fi in files)
                {
                    lvi = new ListViewItem();
                    lvi.Text = fi.Name;
                    lvi.ImageIndex = 1;
                    lvi.Tag = fi.FullName;

                    lvsi = new ListViewItem.ListViewSubItem();
                    lvsi.Text = fi.Length.ToString();
                    lvi.SubItems.Add(lvsi);

                    listView1.Items.Add(lvi);
                }
                listView1.EndUpdate();
            }
            catch (Exception err)
            {
                MessageBox.Show("Error:" + err.Message);
            }
        }

        void apply_listView5()
        {
            listView1.View = View.LargeIcon;

            var list = new List<string>();
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_01.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_02.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_03.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_04.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_05.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_06.jpg");
            list.Add(@"C:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_07.jpg");

            ImageList imglist = new ImageList();
            imglist.ImageSize = new Size(200, 200);
            imglist.ColorDepth = ColorDepth.Depth32Bit;
            foreach (var filename in list)
            {
                imglist.Images.Add(Image.FromFile(filename));
            }
            listView1.LargeImageList = imglist;

            for (int i = 0; i < imglist.Images.Count; i++)
            {
                var lvi = new ListViewItem();
                lvi.ImageIndex = 0;
                lvi.Text = "第 " + i.ToString() + " 張圖";
                //lvi.ToolTipText = "P" + i;
                listView1.Items.Add(lvi);
            }
        }


    }
}
