using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;//for Path, Directory

//各種 listView 之 加入資料

//簡單的加入資料  不含各種方法

//ListView加入欄標題
//屬性 / 編輯資料行 / ColumnHeader集合編輯器 / 加入ColumnHeader

namespace vcs_ListView1
{
    public partial class Form1 : Form
    {
        int flag_check_score_done = 0;

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
            richTextBox1.Size = new Size(300, 600);

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
            richTextBox1.Text += "建立listView 0\n";
            listView1.Clear();
            apply_listView00();

            listView1.MultiSelect = true;// 是否允許多行選擇
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 1\n";
            listView1.Clear();
            apply_listView01();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 2\n";
            listView1.Clear();
            apply_listView02();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 3\n";
            listView1.Clear();
            apply_listView03();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 4\n";
            listView1.Clear();
            apply_listView04();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 5 包含checkbox\n";
            listView1.Clear();
            apply_listView05();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 6 加入圖片\n";
            listView1.Clear();
            apply_listView06();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 7\n";
            listView1.Clear();
            apply_listView07();

            rename_filename();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "建立listView 8 xxxx\n";
            listView1.Clear();
            apply_listView08();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //具有多選核取框的ListView控件
            richTextBox1.Text += "建立listView 9 包含checkbox\n";
            listView1.Clear();
            apply_listView09();

            test_listView09();
        }

        void apply_data()
        {
            //加入項目(列資料)
            ListViewItem item1 = listView1.Items.Add("mouse");
            item1.SubItems.Add("米老鼠");
            item1.SubItems.Add("3");

            ListViewItem item2 = listView1.Items.Add("ox");
            item2.SubItems.Add("班尼牛");
            item2.SubItems.Add("48");

            ListViewItem item3 = listView1.Items.Add("tiger");
            item3.SubItems.Add("跳跳虎");
            item3.SubItems.Add("33");

            ListViewItem item4 = listView1.Items.Add("rabbit");
            item4.SubItems.Add("彼得兔");

            /*
            ListViewItem item1 = new ListViewItem("mouse");
            item1.SubItems.Add("米老鼠");
            item1.SubItems.Add("3");
            listView1.Items.Add(item1);

            ListViewItem item2 = new ListViewItem("ox");
            item2.SubItems.Add("班尼牛");
            item2.SubItems.Add("48");
            listView1.Items.Add(item2);

            ListViewItem item3 = new ListViewItem("tiger");
            item3.SubItems.Add("跳跳虎");
            item3.SubItems.Add("33");
            listView1.Items.Add(item3);
            */

            ListViewItem li = new ListViewItem();
            li.SubItems.Clear();
            li.SubItems[0].Text = "rabbit";
            li.SubItems.Add("彼得兔");
            li.SubItems.Add("8");
            listView1.Items.Add(li);


            /*
            //實例化一個listview對象的子項
            ListViewItem item1 = new ListViewItem();
            item1.Text = "mouse";//第一欄數據
            item1.SubItems.Add("米老鼠");//第二欄
            item1.SubItems.Add("3");//第三欄
            listView1.Items.Add(item1);//添加列

            ListViewItem item2 = new ListViewItem();
            item2.Text = "ox";//第一欄數據
            item2.SubItems.Add("班尼牛");//第二欄
            item2.SubItems.Add("48");//第三欄
            listView1.Items.Add(item2);//添加列

            ListViewItem item3 = new ListViewItem();
            item3.Text = "tiger";//第一欄數據
            item3.SubItems.Add("跳跳虎");//第二欄
            item3.SubItems.Add("33");//第三欄
            listView1.Items.Add(item3);//添加列
            */


            /*
            //加入項目(列資料)
            ListViewItem item1 = new ListViewItem();
            item1.Text = "mouse";
            item1.ImageIndex = 0;
            item1.Tag = "米老鼠的說明";
            ListViewItem.ListViewSubItem item1_sub = new ListViewItem.ListViewSubItem();
            item1_sub.Text = "米老鼠";
            item1.SubItems.Add(item1_sub);
            item1_sub = new ListViewItem.ListViewSubItem();
            item1_sub.Text = "3";
            item1.SubItems.Add(item1_sub);
            listView1.Items.Add(item1);

            ListViewItem item2 = new ListViewItem();
            item2.Text = "ox";
            item2.ImageIndex = 1;
            item2.Tag = "班尼牛的說明";
            ListViewItem.ListViewSubItem item2_sub = new ListViewItem.ListViewSubItem();
            item2_sub.Text = "班尼牛";
            item2.SubItems.Add(item2_sub);
            listView1.Items.Add(item2);
            */
        }

        void apply_listView00()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.Scrollable = true;   //需要時候顯示滾動條
            listView1.MultiSelect = false;// 是否允許多行選擇
            //listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable;
            //listView1.AllowColumnReorder = true;//允許使用者拖曳欄位
            listView1.Font = new Font("Microsoft Sans Serif", 12.75F, FontStyle.Regular, GraphicsUnit.Point, ((byte)(0)));

            //設定欄位
            listView1.Columns.Add("英文名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("中文名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);

            //加入項目(列資料)
            apply_data();
        }

        void apply_listView01()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //清除所有的欄位
            listView1.Columns.Clear();//看似與清除整個listView一樣

            //設定欄位 寬度-2代表自動欄寬??
            listView1.Columns.Add("英文名", -1, HorizontalAlignment.Center);
            listView1.Columns.Add("中文名", -1, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", -1, HorizontalAlignment.Right);

            //設定欄寬 1
            foreach (ColumnHeader col in listView1.Columns)
            {
                //col.Width = -2;   //自動欄寬, 寬度-2代表自動欄寬
                col.Width = 80;     //固定欄寬
            }

            //設定欄寬 2
            int C = listView1.Columns.Count;//欄數
            for (int i = 0; i < C; i++)
            {
                listView1.Columns[i].Width = -2;//寬度-2代表自動欄寬
            }

            //加入項目(列資料)
            apply_data();
        }

        void apply_listView02()
        {

        }

        void apply_listView03()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //設定欄位
            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "英文名";
            ch1.Width = 85;
            listView1.Columns.Add(ch1);

            ColumnHeader ch2 = new ColumnHeader();
            ch2.Text = "中文名";
            ch2.Width = 85;
            listView1.Columns.Add(ch2);

            ColumnHeader ch3 = new ColumnHeader();
            ch3.Text = "體重";
            ch3.Width = 85;
            listView1.Columns.Add(ch3);

            //加入項目(列資料)
            apply_data();
        }

        void apply_listView04()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //設定欄位
            ColumnHeader colHead;
            colHead = new ColumnHeader();
            colHead.Text = "英文名";
            colHead.Width = 200;
            colHead.TextAlign = HorizontalAlignment.Left;
            listView1.Columns.Add(colHead);

            colHead = new ColumnHeader();
            colHead.Text = "中文名";
            colHead.Width = 100;
            colHead.TextAlign = HorizontalAlignment.Left;
            listView1.Columns.Add(colHead);

            colHead = new ColumnHeader();
            colHead.Text = "體重";
            colHead.Width = 200;
            colHead.TextAlign = HorizontalAlignment.Left;
            listView1.Columns.Add(colHead);

            //加入項目(列資料)
            apply_data();
        }

        void apply_listView05()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.LabelEdit = true;//允許使用者修改listView的資料
            listView1.AllowColumnReorder = true;//允許使用者拖曳欄位

            // Display check boxes.
            listView1.CheckBoxes = true;//使用CheckBox(核取方塊)
            // Sort the items in the list in ascending order.
            listView1.Sorting = SortOrder.Ascending;

            //設定欄位
            // Create columns for the items and subitems.
            // Width of -2 indicates auto-size.
            //寬度-2代表自動欄寬
            listView1.Columns.Add("中文名", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", -2, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);
            listView1.Columns.Add("代表", 120, HorizontalAlignment.Center);

            //加入項目(列資料)
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

            listView1.Items.AddRange(new ListViewItem[] { item1, item2, item3, item4 });

            // Create two ImageList objects.
            ImageList imageListSmall = new ImageList();
            ImageList imageListLarge = new ImageList();

            // Initialize the ImageList objects with bitmaps.
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic1.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic2.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg"));
            imageListSmall.Images.Add(Bitmap.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic4.jpg"));

            listView1.LargeImageList = imageListLarge;
            listView1.SmallImageList = imageListSmall;
        }

        void apply_listView06()
        {
            //設定ListView與設定欄位
            listView1.View = View.LargeIcon;  //定義列表顯示的方式

            var list = new List<string>();
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_01.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_02.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_03.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_04.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_05.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_06.jpg");
            list.Add(@"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\poster_07.jpg");

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
                var item = new ListViewItem();
                item.ImageIndex = 0;
                item.Text = "第 " + i.ToString() + " 張圖";
                //item.ToolTipText = "P" + i;
                listView1.Items.Add(item);
            }
        }

        void apply_listView07()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //設定欄位
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
        }

        void rename_filename()
        {
            string dirname = @"D:\_git\vcs\_1.data\______test_files1\_case1";
            foreach (ListViewItem item in listView1.Items)//循環遍歷listView控件中的每一項
            {
                string old_name = Path.Combine(dirname, item.Text);
                string new_name = Path.Combine(dirname, item.SubItems[1].Text);
                //File.Move(old_name, new_name);    //not really rename
            }
            int R = listView1.Items.Count;//列數
            richTextBox1.Text += "(偽執行)總共改名" + R.ToString() + "個檔案\n";
        }

        private void apply_listView08()
        {
        }

        void apply_listView09()
        {
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.CheckBoxes = true;//使用CheckBox(核取方塊)//設置listView1的複選框屬性為真

            //設定欄位
            listView1.Columns.Add("文件名稱", 150, HorizontalAlignment.Left);//向listView1中添加「文件名稱」列
            listView1.Columns.Add("創建時間", 200, HorizontalAlignment.Left);//向listView1中添加「創建時間」列

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_angry_bird";

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
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //設定欄位
            listView1.Columns.Add("中文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);
            listView1.Columns.Add("代表", 120, HorizontalAlignment.Center);
            listView1.Columns.Add("出生年", 120, HorizontalAlignment.Center);

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
            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            //設定欄位
            //設定欄位 名稱、大小與對齊
            listView1.Columns.Add("座號", 60, HorizontalAlignment.Center);
            listView1.Columns.Add("姓名", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("國文", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("英文", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("數學", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("總分", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("平均", 100, HorizontalAlignment.Center);
            listView1.Columns.Add("名次", 100, HorizontalAlignment.Center);

            int C = listView1.Columns.Count;//欄數
            richTextBox1.Text += "目前共有 : " + C.ToString() + " 欄\n";

            //加入項目(列資料)
            Random Rnd = new Random(); //加入Random，產生的數字不會重覆
            string name_string;
            int score_chi;
            int score_eng;
            int score_math;

            int R = listView1.Items.Count;//列數

            for (int i = 0; i < 10; i++)
            {
                var str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
                //var next = new Random();
                //Random Rnd = new Random(); //加入Random，產生的數字不會重覆
                var builder = new StringBuilder();
                int length = 8;
                int j;

                builder.Append("A");
                builder.Append(((R + 1) / 100).ToString());
                builder.Append(((R + 1) / 10).ToString());
                builder.Append(((R + 1) % 10).ToString());
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
            listView1.Items[R - 1].EnsureVisible();
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
            test_listView11();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "xxx\n";
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

        private void button20_Click(object sender, EventArgs e)
        {
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
            int R = listView1.Items.Count;//列數
            if (R > 0)
            {
                for (int i = 0; i < R; i++)
                {
                    ListViewItem item = listView1.Items[i];
                    richTextBox1.Text += item.ToString() + "\n";
                    if (item.Tag != null)
                    {
                        richTextBox1.Text += "取得Tag : " + item.Tag.ToString() + "\n";
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

            foreach (ListViewItem item in listView1.Items)//循環遍歷listView控件中的每一項
            {
                if (item.Checked == false)//如果當前項處於未選中狀態
                {
                    item.Checked = true;//設置當前項為選中狀態
                }
            }

            /*
            richTextBox1.Text += "清空\n";

            foreach (ListViewItem item in listView1.Items)//循環遍歷listView控件中的每一項
            {
                if (item.Checked == true)//如果當前項處於選中狀態
                {
                    item.Checked = false;//設置當前項為未選中狀態
                }
            }

            richTextBox1.Text += "Info\n";

            int R = listView1.Items.Count;//列數
            richTextBox1.Text += "共有 " + R.ToString() + " 項\n";
            foreach (ListViewItem item in listView1.Items)//循環遍歷listView控件中的每一項
            {
                richTextBox1.Text += "項目 : " + item.Text + "\t" + item.SubItems[1].Text + "\t";

                if (item.Checked == true)//如果當前項處於選中狀態
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
            int selCount = listView1.SelectedIndices.Count;
            if (selCount <= 0)  //總共選擇的個數
            {
                richTextBox1.Text += "未選擇要刪除的項目\n";
                return;
            }
            richTextBox1.Text += "共選擇 " + selCount.ToString() + " 個項目, 分別是\n";
            for (int i = (selCount - 1); i >= 0; i--)
            {
                int selNdx = listView1.SelectedItems[i].Index;
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

        void test_listView11()
        {
            //測試listView 1 製作成績
            if (flag_check_score_done == 1)
            {
                richTextBox1.Text += "已做過成績\n";
                return;
            }

            int R = listView1.Items.Count;//列數

            if (R < 1)
            {
                richTextBox1.Text += "無資料\n";
                return;
            }

            int i;
            int j;
            StudentData[] StudentDataArray = new StudentData[R];
            int[] scores = new int[R];
            int total;
            float average;
            for (i = 0; i < R; i++)
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

                richTextBox1.Text += item.SubItems[0].Text + "\t"
                    + item.SubItems[1].Text + "\t"
                    + item.SubItems[2].Text + "\t"
                    + item.SubItems[3].Text + "\t"
                    + item.SubItems[4].Text + "\n";

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
            int[] scores_new = new int[R];
            int[] rank = new int[R];

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

            for (i = 0; i < R; i++)
            {
                ListViewItem item = listView1.Items[i];
                item.SubItems.Add((rank[i] + 1).ToString());
            }

            flag_check_score_done = 1;
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        int type = 0;
        private void button26_Click(object sender, EventArgs e)
        {
            //各種View
            if (type == 0)
            {
                listView1.View = View.Details;  //定義列表顯示的方式
            }
            else if (type == 1)
            {
                listView1.View = View.LargeIcon;  //定義列表顯示的方式
            }
            else if (type == 2)
            {
                listView1.View = View.List;  //定義列表顯示的方式
            }
            else if (type == 3)
            {
                listView1.View = View.SmallIcon;  //定義列表顯示的方式
            }
            else if (type == 4)
            {
                listView1.View = View.Tile;  //定義列表顯示的方式
            }
            else
            {
                richTextBox1.Text += "xxxxxxxx\n";
            }
            type++;
            if (type > 4)
                type = 0;
        }

        private void button27_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "目前排列方向 : " + listView1.Sorting.ToString() + "\n";

            listView1.Sorting = SortOrder.Descending;
            richTextBox1.Text += "目前排列方向 : " + listView1.Sorting.ToString() + "\n";

            listView1.Sorting = SortOrder.Ascending;
            richTextBox1.Text += "目前排列方向 : " + listView1.Sorting.ToString() + "\n";

            listView1.Sorting = SortOrder.Ascending;

            listView1.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Ascending);
            listView1.Sort();
            listView1.ListViewItemSorter = new ListViewAllColumnComparer(SortOrder.Descending);
            listView1.Sort();
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //讀取ListView資料
            richTextBox1.Text += "讀取ListView資料\n";

            //listView1.LabelEdit = true;//允許使用者修改listView的資料

            listView1.AllowColumnReorder = true;//允許使用者拖曳欄位

            int C = listView1.Columns.Count;//欄數
            int R = listView1.Items.Count;//列數
            richTextBox1.Text += "共有 : " + C.ToString() + " 欄\n";
            richTextBox1.Text += "共有 : " + R.ToString() + " 列\n";

            int i;
            //欄資訊
            for (i = 0; i < C; i++)
            {
                richTextBox1.Text += listView1.Columns[i].Text + "\n";

                //設定自動欄寬
                //listView1.Columns[i].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
                //設定自動欄寬
                //listView1.Columns[0].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
                //listView1.Columns[1].AutoResize(ColumnHeaderAutoResizeStyle.ColumnContent);
            }

            foreach (ColumnHeader col in listView1.Columns)
            {
                richTextBox1.Text += col.Text + "\n";
            }

            //列資訊
            foreach (ListViewItem item in listView1.Items)//循環遍歷listView控件中的每一列
            {
                richTextBox1.Text += item + "\n";
                richTextBox1.Text += item.Text + "\n";
                richTextBox1.Text += item.SubItems[1].Text + "\n";
            }

            richTextBox1.Text += "共有 : " + R.ToString() + " 個項目(列), 每個列的大小\n";
            for (i = 0; i < R; i++)
            {
                Rectangle item_rect = listView1.GetItemRect(i);   //找出listview的周框 列
                richTextBox1.Text += "第 " + i.ToString() + " 列 : ";
                richTextBox1.Text += item_rect.ToString() + "\t";

                richTextBox1.Text += item_rect.Left.ToString() + "\t";
                richTextBox1.Text += item_rect.Width.ToString() + "\t";
                richTextBox1.Text += item_rect.Left.ToString() + "\n";
            }

            for (i = 0; i < R; i++)
            {
                ListViewItem item = listView1.Items[i];
                richTextBox1.Text += item.SubItems[0].Text + "\n";
                /*
                richTextBox1.Text += item.SubItems[0].Text + "\t"
                    + item.SubItems[1].Text + "\t"
                    + item.SubItems[2].Text + "\t"
                    + item.SubItems[3].Text + "\t"
                    + item.SubItems[4].Text + "\n";
                */
            }

            int selCount = listView1.SelectedIndices.Count;
            richTextBox1.Text += "你目前選了 : " + selCount.ToString() + " 項\n";

            if (R <= 0)
            {
                richTextBox1.Text += "listView無內容\n";
                return;
            }

            richTextBox1.Text += "共有" + R.ToString() + "個項目(列)，分別是：\n";
            for (i = 0; i < R; i++)
            {
                //ListViewItem t = lv.Items[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += listView1.Items[i].SubItems[0].Text + "\t"
                    + listView1.Items[i].SubItems[1].Text + "\n";
            }

            if (listView1.SelectedItems.Count <= 0)
            {
                richTextBox1.Text += "未選擇listView項目\n";
                return;
            }

            richTextBox1.Text += "選擇" + listView1.SelectedItems.Count.ToString() + "個項目(列)，分別是：\n";
            for (i = 0; i < listView1.SelectedItems.Count; i++)
            {
                //ListViewItem t = lv.SelectedItems[i];  //相同寫法
                //richTextBox1.Text += "i=" + i.ToString() + " ：" + t.SubItems[0].Text + " " + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox1.Text += listView1.SelectedItems[i].SubItems[0].Text + "\t"
                    + listView1.SelectedItems[i].SubItems[1].Text + "\t"
                    + listView1.SelectedItems[i].SubItems[2].Text + "\n";
            }

            richTextBox1.Text += "選擇" + listView1.SelectedIndices.Count.ToString() + "個項目(列)，Index分別是：\n";
            for (i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox1.Text += listView1.SelectedIndices[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

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
            listView1.Items[R - 1].EnsureVisible();

listView1.FullRowSelect = true; //整行一起選取
listView1.GridLines = true; //顯示格線
listView1.Scrollable = true;   //需要時候顯示滾動條
listView1.MultiSelect = false;// 是否允許多行選擇
listView1.CheckBoxes = true;//使用CheckBox(核取方塊)
listView1.Items[listView1.Items.Count - 1].EnsureVisible();
listView1.Font = new Font("Microsoft Sans Serif", 12.75F, FontStyle.Regular, GraphicsUnit.Point, ((byte)(0)));
//listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable;

*/

