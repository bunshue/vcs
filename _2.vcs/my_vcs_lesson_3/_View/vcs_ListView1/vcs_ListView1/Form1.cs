using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//各種 listView 之 加入資料

//簡單的加入資料  不含各種方法

//ListView加入欄標題
//屬性 / 編輯資料行 / ColumnHeader集合編輯器 / 加入ColumnHeader

namespace vcs_ListView1
{
    public partial class Form1 : Form
    {
        int flag_check_score_done = 0;

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
            listView1.Size = new Size(600, 600);
            this.Controls.Add(listView1);

            richTextBox1.Size = new Size(300, 600);
            this.Controls.Add(richTextBox1);

            this.Size = new Size(1430, 700);

            int x_st = 10;
            int y_st = 10;
            int dx = 150 + 5;
            int dy = 60 + 5;

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
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            listView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            richTextBox1.Clear();
            flag_check_score_done = 0;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立listView 0
            richTextBox1.Text += "建立listView 0 基本款\n";
            listView1.Clear();
            apply_listView00();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立listView 1
            richTextBox1.Text += "建立listView 1\n";
            listView1.Clear();
            apply_listView01();
            test_listView01();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //建立listView 2
            richTextBox1.Text += "建立listView 2\n";
            listView1.Clear();
            apply_listView02();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //建立listView 3
            richTextBox1.Text += "羅列出磁盤信息 在 listView 上\n";
            listView1.Clear();
            apply_listView03();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //建立listView 4
            richTextBox1.Text += "顯示本機文件夾及文件在ListView上\n";
            listView1.Clear();
            apply_listView04();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //建立listView 5
            richTextBox1.Text += "在ListView加入圖片\n";
            listView1.Clear();
            apply_listView05();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //建立listView 6
            richTextBox1.Text += "建立listView 6\n";
            listView1.Clear();
            apply_listView06();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //建立listView 7
            richTextBox1.Text += "建立listView 7\n";
            listView1.Clear();
            apply_listView07();

            rename_filename();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //建立listView 8
            richTextBox1.Text += "建立listView 8\n";
            listView1.Clear();
            apply_listView08();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //具有多選核取框的ListView控件

            //建立listView 9
            richTextBox1.Text += "建立listView 9 包含checkbox\n";
            listView1.Clear();
            apply_listView09();

            test_listView09();
        }

        void apply_listView00()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.Scrollable = true;   //需要時候顯示滾動條
            listView1.MultiSelect = false; // 不可以多行選擇
            //listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable;
            //listView1.AllowColumnReorder = true;
            listView1.Font = new Font("Microsoft Sans Serif", 12.75F, FontStyle.Regular, GraphicsUnit.Point, ((byte)(0)));

            //設定欄位
            listView1.Columns.Add("中文名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);

            //加入項目
            ListViewItem listViewItem1 = new ListViewItem("鼠");
            listViewItem1.SubItems.Add("mouse");
            listViewItem1.SubItems.Add("3");
            listView1.Items.Add(listViewItem1);

            ListViewItem listViewItem2 = new ListViewItem("牛");
            listViewItem2.SubItems.Add("ox");
            listViewItem2.SubItems.Add("48");
            listView1.Items.Add(listViewItem2);

            ListViewItem listViewItem3 = new ListViewItem("虎");
            listViewItem3.SubItems.Add("tiger");
            listViewItem3.SubItems.Add("33");
            listView1.Items.Add(listViewItem3);

            //加入項目
            for (int i = 0; i < 5; i++)
            {
                ListViewItem li = new ListViewItem();
                li.SubItems.Clear();
                li.SubItems[0].Text = "蛇";
                li.SubItems.Add("snake");
                li.SubItems.Add("16");
                listView1.Items.Add(li);
            }
        }

        void apply_listView01()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //設置標題
            //設置列名稱、大小與對齊
            listView1.Columns.Add("座號", 60, HorizontalAlignment.Center);
            listView1.Columns.Add("姓名", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("國文", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("英文", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("數學", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("總分", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("平均", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("名次", 100, HorizontalAlignment.Center);

            richTextBox1.Text += "目前共有 : " + listView1.Columns.Count.ToString() + " 欄\n";

            richTextBox1.Text += "加入列資料\n";

            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            string name_string;
            int score_chi;
            int score_eng;
            int score_math;

            for (int i = 0; i < 10; i++)
            {
                var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                //var next = new Random();
                //Random Rnd = new Random(); //加入Random，產生的數字不會重覆
                var builder = new StringBuilder();
                int length = 8;
                int j;

                builder.Append("A");
                builder.Append(((listView1.Items.Count + 1) / 100).ToString());
                builder.Append(((listView1.Items.Count + 1) / 10).ToString());
                builder.Append(((listView1.Items.Count + 1) % 10).ToString());
                builder.Append("_");

                for (j = 5; j < length; j++)
                {
                    builder.Append(str[Rnd.Next(0, str.Length)]);
                }
                name_string = builder.ToString();

                score_chi = Rnd.Next(55, 90) + 1;
                score_eng = Rnd.Next(50, 80) + 1;
                score_math = Rnd.Next(40, 70) + 1;

                /* debug
                name_string = "david";

                score_chi = 80;
                score_eng = 90;
                score_math = 100;
                */

                //建立一行資料的檔頭與第0筆資料(座號)
                ListViewItem item = new ListViewItem((i + 1).ToString());

                //建立這一筆資料的第1個子項目(姓名)
                ListViewItem.ListViewSubItem sub_item_1 = new ListViewItem.ListViewSubItem();
                sub_item_1.Text = name_string;
                item.SubItems.Add(sub_item_1);

                //建立這一筆資料的第2個子項目(國文)
                ListViewItem.ListViewSubItem sub_item_2 = new ListViewItem.ListViewSubItem();
                sub_item_2.Text = score_chi.ToString();
                item.SubItems.Add(sub_item_2);

                //建立這一筆資料的第3個子項目(英文)
                ListViewItem.ListViewSubItem sub_item_3 = new ListViewItem.ListViewSubItem();
                sub_item_3.Text = score_eng.ToString();
                item.SubItems.Add(sub_item_3);

                /*  這項改成直接加入
                //建立這一筆資料的第4個子項目(數學)
                ListViewItem.ListViewSubItem sub_item_4 = new ListViewItem.ListViewSubItem();
                sub_item_4.Text = score_math.ToString();
                item.SubItems.Add(sub_item_4);
                */
                //直接加入
                item.SubItems.Add(score_math.ToString());

                //整行資料一次加入到listView1
                listView1.Items.Add(item);

                /*
                //添加item另法 AddRange
                ListViewItem item = new ListViewItem((i + 1).ToString());
                item.SubItems.Add(name_string);
                item.SubItems.Add(score_chi.ToString());
                item.SubItems.Add(score_eng.ToString());
                item.SubItems.Add(score_math.ToString());
                listView1.Items.AddRange(new ListViewItem[] { item });
                */
            }

            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();
        }

        void apply_listView02()
        {
        }

        void apply_listView03()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

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

        void apply_listView04()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //建立欄資料
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

            //建立列資料
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            try
            {
                ListViewItem lvi;
                ListViewItem.ListViewSubItem lvsi;

                if (foldername.CompareTo("") == 0)
                    return;
                DirectoryInfo dir = new DirectoryInfo(foldername);
                DirectoryInfo[] dirs = dir.GetDirectories();
                FileInfo[] files = dir.GetFiles();

                //顯示本機文件夾及文件

                //labPathName.Text = foldername;
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

        void apply_listView05()
        {
            listView1.View = View.LargeIcon;

            var list = new List<string>();
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_01.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_02.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_03.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_04.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_05.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_06.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_MU\poster_07.jpg");

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

        void apply_listView06()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            // 製作列資料
            ListViewMakeRow(listView1, "B", new string[] { "B", "B", "1000" });
            ListViewMakeRow(listView1, "B", new string[] { "B", "B", "1000", "4/1/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "C" });
            ListViewMakeRow(listView1, "C", new string[] { "B", "C", "1000", "4/1/2014" });
            ListViewMakeRow(listView1, "A", new string[] { "B", "C", "1000", "4/1/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "9", "12/20/2013", "C" });
            ListViewMakeRow(listView1, "B", new string[] { "B" });
            ListViewMakeRow(listView1, "C", new string[] { "C", "C", "1000", "4/1/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A" });
            ListViewMakeRow(listView1, "B", new string[] { "B", "B", "20" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "9", "12/20/2013", "A" });
            ListViewMakeRow(listView1, "C", new string[] { "C", "C", "1001", "8/20/2014" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "9", "4/1/2014" });
            ListViewMakeRow(listView1, "C", new string[] { "C", "C", "100", "1/2/2014", "F" });
            ListViewMakeRow(listView1, "A", new string[] { "A", "A", "10" });

            // Make the ListView column headers.
            ListViewMakeColumnHeaders(listView1,
                new object[] {
                    "1", HorizontalAlignment.Left,
                    "2", HorizontalAlignment.Left,
                    "3", HorizontalAlignment.Left,
                    "4", HorizontalAlignment.Right,
                    "5", HorizontalAlignment.Right,
                    "6", HorizontalAlignment.Left
                });

            // Size the columns.
            foreach (ColumnHeader col in listView1.Columns)
            {
                //col.Width = -2;   //自動欄寬
                col.Width = 80;     //固定欄寬
            }
        }

        // Make a ListView row.
        private void ListViewMakeRow(ListView lvw, String item_title, string[] subitem_titles)
        {
            // Make the item.
            ListViewItem new_item = lvw.Items.Add(item_title);

            // Make the sub-items.
            for (int i = subitem_titles.GetLowerBound(0); i <= subitem_titles.GetUpperBound(0); i++)
            {
                new_item.SubItems.Add(subitem_titles[i]);
            }
        }

        // Make the ListView's column headers.
        // The ParamArray entries should alternate between
        // strings and HorizontalAlignment values.
        private void ListViewMakeColumnHeaders(ListView lvw, Object[] header_info)
        {
            // Remove any existing headers.
            lvw.Columns.Clear();

            // Make the column headers.
            for (int i = header_info.GetLowerBound(0); i <= header_info.GetUpperBound(0); i += 2)
            {
                lvw.Columns.Add(
                    (string)header_info[i],
                    -1,
                    (HorizontalAlignment)header_info[i + 1]);
            }
        }

        void apply_listView07()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.Columns.Add("舊檔名", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("新檔名", 150, HorizontalAlignment.Left);

            int start_index = 8;
            string base_name = "ims_file";

            string dirname = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            string[] filenames = Directory.GetFiles(dirname);
            if (filenames.Length == 0)
                return;

            Array.Sort(filenames);

            string format = "{0:D2}";
            List<string> old_names = new List<string>();

            foreach (string filename in filenames)
            {
                string old_name = Path.GetFileName(filename);
                old_names.Add(old_name);
                ListViewItem item = listView1.Items.Add(old_name);
                richTextBox1.Text += "old = " + old_name + "\t\t";

                string new_name = base_name + string.Format(format, start_index) + Path.GetExtension(filename);
                richTextBox1.Text += "new = " + new_name + "\n";

                if (old_names.Contains(new_name))
                {
                    MessageBox.Show("Name " + new_name + " is already in use.");
                    break;
                }

                item.SubItems.Add(new_name);
                start_index++;
            }

            //listView 自動欄寬
            //listView1.Columns[0].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
            //listView1.Columns[1].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
        }

        void rename_filename()
        {
            string dirname = @"D:\_git\vcs\_1.data\______test_files1\_case1";
            foreach (ListViewItem item in listView1.Items)
            {
                string old_name = Path.Combine(dirname, item.Text);
                string new_name = Path.Combine(dirname, item.SubItems[1].Text);
                //File.Move(old_name, new_name);    //not really rename
            }
            int num_files = listView1.Items.Count;
            richTextBox1.Text += "(偽執行)總共改名" + num_files.ToString() + "個檔案\n";
        }

        private void apply_listView08()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線


            // Allow the user to edit item text.
            listView1.LabelEdit = true;
            // Allow the user to rearrange columns.
            listView1.AllowColumnReorder = true;
            // Display check boxes.
            listView1.CheckBoxes = true;
            // Sort the items in the list in ascending order.
            listView1.Sorting = SortOrder.Ascending;

            //加入欄資料 標題
            // Create columns for the items and subitems.
            // Width of -2 indicates auto-size.
            listView1.Columns.Add("中文名", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);
            listView1.Columns.Add("代表", 120, HorizontalAlignment.Center);

            //加入列資料
            // Create three items and three sets of subitems for each item.
            ListViewItem item1 = new ListViewItem("鼠", 0);
            // Place a check mark next to the item.
            item1.Checked = true;
            item1.SubItems.Add("mouse");
            item1.SubItems.Add("3");
            item1.SubItems.Add("米老鼠");
            ListViewItem item2 = new ListViewItem("牛", 1);
            item2.SubItems.Add("ox");
            item2.SubItems.Add("48");
            item2.SubItems.Add("班尼牛");
            ListViewItem item3 = new ListViewItem("虎", 0);
            // Place a check mark next to the item.
            item3.Checked = true;
            item3.SubItems.Add("tiger");
            item3.SubItems.Add("33");
            item3.SubItems.Add("跳跳虎");
            ListViewItem item4 = new ListViewItem("兔", 0);
            // Place a check mark next to the item.
            item4.Checked = true;
            item4.SubItems.Add("rabbit");
            item4.SubItems.Add("8");
            item4.SubItems.Add("彼得兔");

            //Add the items to the ListView.
            listView1.Items.AddRange(new ListViewItem[] { item1, item2, item3, item4 });

            // Create two ImageList objects.
            ImageList imageListSmall = new ImageList();
            ImageList imageListLarge = new ImageList();

            // Initialize the ImageList objects with bitmaps.
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic1.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic2.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic4.jpg"));

            //Assign the ImageList objects to the ListView.
            listView1.LargeImageList = imageListLarge;
            listView1.SmallImageList = imageListSmall;

            // Add the ListView to the control collection.
            //this.Controls.Add(listView1);
        }

        void apply_listView09()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.CheckBoxes = true;//設置listView1的復選框屬性為真
            listView1.Columns.Add("文件名稱", 150, HorizontalAlignment.Left);//向listView1中添加「文件名稱」列
            listView1.Columns.Add("創建時間", 200, HorizontalAlignment.Left);//向listView1中添加「創建時間」列

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_angry_bird";

            foreach (String fileName in Directory.GetFiles(foldername)) //循環遍歷指定資料夾的內容
            {
                FileInfo file = new FileInfo(fileName);//定義一個操作文件的實例
                ListViewItem OptionItem = new ListViewItem(file.Name);//定義一個listView選擇項的實例
                OptionItem.SubItems.Add(file.CreationTime.ToString());//向listView控件中添加文件創建時間列
                listView1.Items.Add(OptionItem);//執行添加操作
                richTextBox1.Text += "加入listView : " + file.Name + "\t" + file.CreationTime.ToString() + "\n";
            }
        }

        void apply_listView10()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.Columns.Add("中文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);
            listView1.Columns.Add("代表", 120, HorizontalAlignment.Center);
            listView1.Columns.Add("出生年", 120, HorizontalAlignment.Center);

            // Add some groups to the ListView.
            ListViewGroup group1 = new ListViewGroup("Group 1");
            ListViewGroup group2 = new ListViewGroup("Group 2");
            listView1.Groups.Add(group1);
            listView1.Groups.Add(group2);

            ListViewItem new_item;
            // Group 1
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "鼠",
                    "mouse", 
                    "3", 
                    "米老鼠", "2014"},
                group1));
            new_item.Tag = "1111";
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "牛",
                    "ox", 
                    "48", 
                    "班尼牛", "2013"},
                group1));
            new_item.Tag = "2222";

            // Group 2
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "龍",
                    "dragon", 
                    "38", 
                    "逗逗龍", "2012"},
                group2));
            new_item.Tag = "5555";
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "蛇",
                    "snake", 
                    "16", 
                    "貪吃蛇", "2008"},
                group2));
            new_item.Tag = "6666";

            // Misc.
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "猴",
                    "monkey", 
                    "22", 
                    "山道猴", "2013"}));
            new_item.Tag = "9999";
            new_item = listView1.Items.Add(new ListViewItem(new string[]
                {   "雞", 
                    "chicken", 
                    "6", 
                    "肯德雞", "2011"}));
            new_item.Tag = "aaaa";
        }

        void apply_listView11()
        {
            //基本設定
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            // 加入列資料
            listView1.AddRow(new string[] { "鼠", "mouse", "3", "米老鼠", "2014" });
            listView1.AddRow(new string[] { "牛", "ox", "48", "班尼牛", "2013" });
            listView1.AddRow(new string[] { "虎", "tiger", "33", "跳跳虎", "2012" });
            listView1.AddRow("兔", "rabbit", "8", "彼得兔", "2013");
            listView1.AddRow("龍", "dragon", "38", "逗逗龍", "2008");
            listView1.AddRow("蛇", "snake", "16", "貪吃蛇", "2011");

            // Make the ListView column headers.
            listView1.MakeColumnHeaders(
                "中文名", HorizontalAlignment.Left,
                "英文名", HorizontalAlignment.Left,
                "體重", HorizontalAlignment.Left,
                "代表", HorizontalAlignment.Right,
                "Year", HorizontalAlignment.Right
            );

            // Size the columns to fit the data and colummn headers.
            listView1.SizeColumns(-2);
        }

        //--------------------------------------------------------------------------------------------------------------------

        private void button10_Click(object sender, EventArgs e)
        {
            //建立listView 10
            richTextBox1.Text += "建立listView 10 用 group 分群\n";
            listView1.Clear();
            apply_listView10();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //建立listView 11
            richTextBox1.Text += "建立listView 11\n";
            listView1.Clear();
            apply_listView11();
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

        //--------------------------------------------------------------------------------------------------------------------

        void print_listView_data(ListView lv)
        {
            richTextBox1.Text += "共有 : " + lv.Columns.Count.ToString() + " 個欄目(欄)\n";
            richTextBox1.Text += "共有 : " + lv.Items.Count.ToString() + " 個項目(列)\n";

            if (lv.Items.Count <= 0)
            {
                richTextBox1.Text += "listView無內容\n";
                return;
            }

            richTextBox1.Text += "共有" + lv.Items.Count.ToString() + "個項目(列)，分別是：\n";
            for (int i = 0; i < lv.Items.Count; i++)
            {
                //ListViewItem t = lv.Items[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += lv.Items[i].SubItems[0].Text + "\t" + lv.Items[i].SubItems[1].Text + "\t" + lv.Items[i].SubItems[2].Text + "\t" + lv.Items[i].SubItems[3].Text + "\n";
            }

            if (lv.SelectedItems.Count <= 0)
            {
                //richTextBox1.Text += "未選擇listView項目\n";
                return;
            }
            richTextBox1.Text += "選擇" + lv.SelectedItems.Count.ToString() + "個項目(列)，分別是：\n";
            for (int i = 0; i < lv.SelectedItems.Count; i++)
            {
                //ListViewItem t = lv.SelectedItems[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += lv.SelectedItems[i].SubItems[0].Text + "\t" + lv.SelectedItems[i].SubItems[1].Text + "\t" + lv.SelectedItems[i].SubItems[2].Text + lv.SelectedItems[i].SubItems[3].Text + "\n";
            }

            richTextBox1.Text += "選擇" + lv.SelectedIndices.Count.ToString() + "個項目(列)，Index分別是：\n";
            for (int i = 0; i < lv.SelectedIndices.Count; i++)
            {
                richTextBox1.Text += lv.SelectedIndices[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //讀取資料
            richTextBox1.Text += "讀取資料\n";
            //print_listView_data(listView1);

            int len = listView1.Items.Count;
            richTextBox1.Text += "共有 : " + len.ToString() + " 個項目(列)\n";

            for (int row = 0; row < len; row++)
            {
                Rectangle item_rect = listView1.GetItemRect(row);   //找出listview的周框 列
                richTextBox1.Text += "row = " + row.ToString() + "\t";
                richTextBox1.Text += item_rect.ToString() + "\t";

                richTextBox1.Text += item_rect.Left.ToString() + "\t";
                richTextBox1.Text += item_rect.Width.ToString() + "\t";
                richTextBox1.Text += item_rect.Left.ToString() + "\n";
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "依第一欄排列\n";
            richTextBox1.Text += "遞增\n";

            // Create a comparer.
            listView1.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Ascending);

            listView1.Sort();

            /*
            richTextBox1.Text += "遞減\n";

            // Create a comparer.
            listView1.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Descending);

            listView1.Sort();
            */
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //show

            int len = listView1.Items.Count;
            if (len > 0)
            {
                for (int i = 0; i < len; i++)
                {
                    richTextBox1.Text += listView1.Items[i].ToString() + "\n";
                    if (listView1.Items[i].Tag != null)
                    {
                        richTextBox1.Text += "取得Tag : " + listView1.Items[i].Tag.ToString() + "\n";
                    }
                }

            }
            else
            {
                richTextBox1.Text += "無項目\n";
            }
        }

        void test_listView09()
        {
            richTextBox1.Text += "測試listView 9\n";

            richTextBox1.Text += "全選\n";

            foreach (ListViewItem tempItem in listView1.Items)//循環遍歷listView控件中的每一項
            {
                if (tempItem.Checked == false)//如果當前項處於未選中狀態
                {
                    tempItem.Checked = true;//設置當前項為選中狀態
                }
            }

            /*
            richTextBox1.Text += "清空\n";

            foreach (ListViewItem tempItem in listView1.Items)//循環遍歷listView控件中的每一項
            {
                if (tempItem.Checked == true)//如果當前項處於選中狀態
                {
                    tempItem.Checked = false;//設置當前項為未選中狀態
                }
            }

            richTextBox1.Text += "Info\n";

            int len = listView1.Items.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 項\n";
            foreach (ListViewItem tempItem in listView1.Items)//循環遍歷listView控件中的每一項
            {
                richTextBox1.Text += "項目 : " + tempItem.Text + "\t" + tempItem.SubItems[1].Text + "\t";

                if (tempItem.Checked == true)//如果當前項處於選中狀態
                {
                    richTextBox1.Text += "已選取\n";
                }
                else
                {
                    richTextBox1.Text += "未選取\n";
                }
            }
            */
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {
            //刪除資料
            int selNdx;
            int selCount;

            selCount = listView1.SelectedIndices.Count;
            if (selCount <= 0)  //總共選擇的個數
            {
                richTextBox1.Text += "未選擇要刪除的項目\n";
                return;
            }
            richTextBox1.Text += "共選擇 " + selCount.ToString() + " 個項目, 分別是\n";
            for (int i = (selCount - 1); i >= 0; i--)
            {
                selNdx = listView1.SelectedItems[i].Index;
                richTextBox1.Text += "item : " + listView1.SelectedItems[i].Text + " index = " + selNdx.ToString() + "\n";
                listView1.Items.RemoveAt(selNdx);
            }
            return;
        }

        class StudentData
        {
            public int number { get; set; }
            public string name { get; set; }
            public int score_chi { get; set; }
            public int score_eng { get; set; }
            public int score_math { get; set; }
            public int total { get; set; }
            public float average { get; set; }
            public int rank { get; set; }
        }

        void test_listView01()
        {
            //測試listView 1 製作成績
            if (flag_check_score_done == 1)
            {
                richTextBox1.Text += "已做過成績\n";
                return;
            }

            if (listView1.Items.Count < 1)
            {
                richTextBox1.Text += "無資料\n";
                return;
            }

            int i;
            int j;
            StudentData[] StudentDataArray = new StudentData[listView1.Items.Count];
            int[] scores = new int[listView1.Items.Count];
            int total;
            float average;
            for (i = 0; i < listView1.Items.Count; i++)
            {
                ListViewItem item = listView1.Items[i];
                item.UseItemStyleForSubItems = false;
                if (int.Parse(item.SubItems[2].Text) < 60)  //這一筆資料的第2個子項目(國文)
                {
                    item.SubItems[2].ForeColor = Color.Red;
                }
                if (int.Parse(item.SubItems[3].Text) < 60)  //這一筆資料的第3個子項目(英文)
                {
                    item.SubItems[3].ForeColor = Color.Red;
                }
                if (int.Parse(item.SubItems[4].Text) < 60)  //這一筆資料的第4個子項目(數學)
                {
                    item.SubItems[4].ForeColor = Color.Red;
                }
                total = int.Parse(item.SubItems[2].Text) + int.Parse(item.SubItems[3].Text) + int.Parse(item.SubItems[4].Text);
                average = (float)total / 3;
                item.SubItems.Add(total.ToString());
                item.SubItems.Add(average.ToString("#0.00"));

                richTextBox1.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\t" + listView1.Items[i].SubItems[2].Text + "\t" + listView1.Items[i].SubItems[3].Text + "\t" + listView1.Items[i].SubItems[4].Text + "\n";

                StudentDataArray[i] = new StudentData { };
                StudentDataArray[i].number = i;
                StudentDataArray[i].name = item.SubItems[1].Text;
                StudentDataArray[i].score_chi = int.Parse(item.SubItems[2].Text);
                StudentDataArray[i].score_eng = int.Parse(item.SubItems[3].Text);
                StudentDataArray[i].score_math = int.Parse(item.SubItems[4].Text);
                StudentDataArray[i].total = total;
                StudentDataArray[i].average = average;
                scores[i] = total;
            }

            /*  不是成績單用的排序
            richTextBox1.Text += "排序前：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (StudentData str in StudentDataArray)
            {
                richTextBox1.Text += str.name + "\t" + str.score_chi.ToString() + "\t" + str.score_eng.ToString() + "\t" + str.score_math.ToString() + "\t" + str.total.ToString() + "\t" + str.average.ToString("#0.00") + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "依Name_C排序, ";
            Array.Sort(StudentDataArray, delegate(StudentData s1, StudentData s2)
            {
                return s1.total.CompareTo(s2.total);
            });
            richTextBox1.Text += "排序後：\nName_C\tName_E\tName_N\tAge\tWeight\tBirthday\n";
            foreach (StudentData str in StudentDataArray)
            {
                richTextBox1.Text += str.name + "\t" + str.score_chi.ToString() + "\t" + str.score_eng.ToString() + "\t" + str.score_math.ToString() + "\t" + str.total.ToString() + "\t" + str.average.ToString("#0.00") + "\n";
            }
            richTextBox1.Text += "\n";
            */

            //排名次
            int[] scores_new = new int[listView1.Items.Count];
            int[] rank = new int[listView1.Items.Count];

            Array.Copy(scores, scores_new, scores.Length);
            Array.Sort(scores_new);
            Array.Reverse(scores_new);

            int score_last = -1;
            for (i = 0; i < scores_new.Length; i++)
            {
                if (scores_new[i] == score_last)
                    continue;
                else
                    score_last = scores_new[i];

                //richTextBox1.Text += i.ToString() + "\t" + names[i] + "\t" + scores_new[i] + "\n";
                for (j = 0; j < scores_new.Length; j++)
                {
                    if (scores[j] == scores_new[i])
                    {
                        rank[j] = i;
                    }
                }

            }
            richTextBox1.Text += "排名次：\n";
            for (i = 0; i < scores.Length; i++)
            {
                //richTextBox1.Text += (i + 1).ToString() + "\t" + names[i] + "\t" + scores[i] + "\t" + (rank[i] + 1).ToString() + "\n";
                richTextBox1.Text += (i + 1).ToString() + "\t" + scores[i] + "\t" + (rank[i] + 1).ToString() + "\n";
            }
            richTextBox1.Text += "\n";

            for (i = 0; i < listView1.Items.Count; i++)
            {
                ListViewItem t = listView1.Items[i];
                t.SubItems.Add((rank[i] + 1).ToString());
            }

            flag_check_score_done = 1;
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //各種View
            listView1.View = View.Details;

            listView1.View = View.LargeIcon;

            listView1.View = View.List;

            listView1.View = View.SmallIcon;

            listView1.View = View.Tile;

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //Info
            richTextBox1.Text += "目前排列方向 : " + listView1.Sorting.ToString() + "\n";
            listView1.Sorting = SortOrder.Descending;
            richTextBox1.Text += "目前排列方向 : " + listView1.Sorting.ToString() + "\n";
            listView1.Sorting = SortOrder.Ascending;
            richTextBox1.Text += "目前排列方向 : " + listView1.Sorting.ToString() + "\n";

        }

        private void button29_Click(object sender, EventArgs e)
        {
            listView1.Clear();

        }
    }
}

/*

ListView 之 排序
// Sort.
listView1.Sorting = SortOrder.Ascending;
listView1.FullRowSelect = true;



listview auto resize columns
lvwValues.AutoResizeColumns(ColumnHeaderAutoResizeStyle.ColumnContent);


//listView 捲到最下一行
            // Scroll to the last entry.
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();


//listView 自動欄寬
            listView1.Columns[0].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
            listView1.Columns[1].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
			
            lvMemory.Columns[0].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
            lvMemory.Columns[1].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);

*/

