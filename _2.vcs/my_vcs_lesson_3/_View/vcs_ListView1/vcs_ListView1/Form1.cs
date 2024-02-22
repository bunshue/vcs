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

//ListView加入欄標題
//屬性 / 編輯資料行 / ColumnHeader集合編輯器 / 加入ColumnHeader

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
            listView1.Size = new Size(600, 600);
            this.Controls.Add(listView1);

            richTextBox1.Size = new Size(300, 600);
            this.Controls.Add(richTextBox1);

            this.Size = new Size(1270, 700);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 150 + 5;
            dy = 60 + 5;

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

            listView1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立listView 0
            richTextBox1.Text += "建立listView 0\n";
            listView1.Clear();
            //apply_listView0();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //建立listView 1
            richTextBox1.Text += "建立listView 1\n";
            listView1.Clear();
            apply_listView1();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //建立listView 2
            richTextBox1.Text += "建立listView 2\n";
            listView1.Clear();
            apply_listView2();
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
            richTextBox1.Text += "建立listView 6\n";
            listView1.Clear();
            apply_listView6();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //建立listView 7
            richTextBox1.Text += "建立listView 7\n";
            listView1.Clear();
            apply_listView7();

            rename_filename();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //建立listView 8
            richTextBox1.Text += "建立listView 8\n";
            listView1.Clear();
            apply_listView8();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //建立listView 9
            
        }

        void apply_listView1()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            listView1.GridLines = true;

            listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("檔名1", 400, HorizontalAlignment.Left);


            listView1.Items.Add("aaaaaaaa1");
            listView1.Items.Add("aaaaaaaa2");
            listView1.Items.Add("aaaaaaaa3");
            listView1.Items.Add("aaaaaaaa4");
            listView1.Items.Add("aaaaaaaa5");



        }


        void apply_listView2()
        {
            //listView1.Left = 12;
            //listView1.Top = 350;
            //listView1.Width = 700;
            //listView1.Height = 250;
            listView1.GridLines = true;    //顯示各個記錄的分隔線
            listView1.FullRowSelect = true;    //要選擇就是一行
            listView1.View = View.Details; //定義列表顯示的方式
            listView1.Scrollable = true;   //需要時候顯示滾動條
            listView1.MultiSelect = false; // 不可以多行選擇
            listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable;

            // 針對數據庫的字段名稱，建立與之適應顯示表頭
            listView1.Columns.Add("姓名", 60, HorizontalAlignment.Right);
            listView1.Columns.Add("住宅電話", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("辦公電話", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("移動電話", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("居住地點", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("工作單位", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("電子郵件", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            //添加資料
            int i;
            for (i = 0; i < 5; i++)
            {
                ListViewItem li = new ListViewItem();
                li.SubItems.Clear();
                li.SubItems[0].Text = "Name";
                li.SubItems.Add("HomePhone");
                li.SubItems.Add("WorkPhone");
                li.SubItems.Add("MobilePhone");
                li.SubItems.Add("City");
                li.SubItems.Add("Address");
                li.SubItems.Add("Email");
                listView1.Items.Add(li);
            }
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

        void apply_listView6()
        {
            listView1.View = View.Details;

            // Make some data.
            // Remove any existing items.
            listView1.Items.Clear();

            // Add data rows.
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

        void apply_listView7()
        {
            listView1.View = View.Details;

            listView1.Columns.Add("舊檔名", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("新檔名", 150, HorizontalAlignment.Left);

            int start_index = 8;
            string base_name = "ims_file";

            listView1.Items.Clear();

            string dirname = @"C:\_git\vcs\_1.data\______test_files1\_case1";

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
            string dirname = @"C:\_git\vcs\_1.data\______test_files1\_case1";
            foreach (ListViewItem item in listView1.Items)
            {
                string old_name = Path.Combine(dirname, item.Text);
                string new_name = Path.Combine(dirname, item.SubItems[1].Text);
                //File.Move(old_name, new_name);    //not really rename
            }
            int num_files = listView1.Items.Count;
            richTextBox1.Text += "(偽執行)總共改名" + num_files.ToString() + "個檔案\n";
        }

        private void apply_listView8()
        {
            // Create a new ListView control.
            //ListView listView1 = new ListView();
            //listView1.Bounds = new Rectangle(new Point(10, 10), new Size(600, 400));

            // Set the view to show details.
            listView1.View = View.Details;

            // Allow the user to edit item text.
            listView1.LabelEdit = true;
            // Allow the user to rearrange columns.
            listView1.AllowColumnReorder = true;
            // Display check boxes.
            listView1.CheckBoxes = true;
            // Select the item and subitems when selection is made.
            listView1.FullRowSelect = true;
            // Display grid lines.
            listView1.GridLines = true;
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
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic1.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic2.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"C:\_git\vcs\_1.data\______test_files1\_case1\pic4.jpg"));

            //Assign the ImageList objects to the ListView.
            listView1.LargeImageList = imageListLarge;
            listView1.SmallImageList = imageListSmall;

            // Add the ListView to the control collection.
            //this.Controls.Add(listView1);
        }


        //--------------------------------------------------------------------------------------------------------------------

        private void button10_Click(object sender, EventArgs e)
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

        private void button11_Click(object sender, EventArgs e)
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

        private void button12_Click(object sender, EventArgs e)
        {
            int len = listView1.Items.Count;
            //show
            if (len > 0)
            {
                for (int i = 0; i < len; i++)
                {
                    richTextBox1.Text += listView1.Items[i].ToString() + "\n";
                }

            }
            else
            {
                richTextBox1.Text += "無項目\n";
            }

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
            listView1.Clear();
        }

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


    }
}
