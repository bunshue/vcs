using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Text.RegularExpressions;

namespace vcs_ListView2
{
    public partial class Form1 : Form
    {
        ListView listView1 = new ListView();
        RichTextBox richTextBox1 = new RichTextBox();

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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
            apply_listView1();
        }

        void show_item_location()
        {
            listView1.Size = new Size(600, 600);
            this.Controls.Add(listView1);

            richTextBox1.Size = new Size(300 + 200, 450);
            this.Controls.Add(richTextBox1);

            this.Size = new Size(1170, 700);

            int x_st = 10;
            int y_st = 10;
            int dx = 150 + 5;
            int dy = 30;

            lb_main_mesg0.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            lb_main_mesg1.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            lb_main_mesg2.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            lb_main_mesg3.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            lb_main_mesg4.Location = new Point(x_st + dx * 4, y_st + dy * 4);

            listView1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 5);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_main_mesg0.Text = "各種 listView 之 方法";
            lb_main_mesg1.Text = "從外部拖曳檔案進listView DragEnter + DragDrop";
            lb_main_mesg2.Text = "DoubleClick      ColumnClick";
            lb_main_mesg3.Text = "ItemActivate";
            lb_main_mesg4.Text = "";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            richTextBox1.Clear();
        }

        void apply_listView1()
        {
            listView1.AllowDrop = true;
            listView1.AllowDrop = true;
            listView1.View = View.Details;

            listView1.DragEnter += Files_DragEnter;//物件拖拽事件
            listView1.DragDrop += Files_DragDrop;//拖拽操作完成事件
            listView1.DoubleClick += new EventHandler(listView1_DoubleClick);
            listView1.ColumnClick += new ColumnClickEventHandler(listView1_ColumnClick);
            listView1.ItemActivate += new EventHandler(listView1_ItemActivate);


            listView1.Columns.Add("簡檔名", 120, HorizontalAlignment.Left);
            listView1.Columns.Add("全檔名", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 80, HorizontalAlignment.Left);

            //加入3筆資料
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\bear.jpg";
            add_item_to_listview(filename1);
            add_item_to_listview(filename2);
            add_item_to_listview(filename3);
        }

        void add_item_to_listview(string filename)
        {
            FileInfo fi = new FileInfo(filename);

            richTextBox1.Text += "fullname = " + filename + ",  name = " + fi.Name + ",  ext = " + fi.Extension + ",  size = " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

            ListViewItem lvi = new ListViewItem();
            lvi.Text = fi.Name;
            lvi.SubItems.AddRange(new string[] { filename, fi.Extension, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) });

            listView1.Items.Add(lvi);
        }

        private void listView1_DoubleClick(object sender, EventArgs e)
        {
            if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
                return;

            int selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox1.Text += "你選擇了" + listView1.Items[selNdx].Text + "\t內容為：\n";

            //ListViewItem t = listView1.Items[selNdx]; //相同寫法
            //richTextBox1.Text += t.Text + "\t" + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
            richTextBox1.Text += listView1.Items[selNdx].Text + "\t" + listView1.Items[selNdx].SubItems[1].Text + "\t" + listView1.Items[selNdx].SubItems[2].Text + "\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";


            /*  另法

            //C# listview 取得點選的值
            string str1 = listView1.FocusedItem.Text;
            string str2 = listView1.FocusedItem.SubItems[1].Text;
            string str3 = listView1.FocusedItem.SubItems[2].Text;
            string str4 = listView1.FocusedItem.SubItems[3].Text;

            richTextBox1.Text += str1 + "\t" + str2 + "\t" + str3 + "\t" + str4 + "\n";
             
             */
        }

        private void listView1_ColumnClick(object sender, ColumnClickEventArgs e)
        {
            richTextBox1.Text += "你按了第 " + e.Column.ToString() + " 欄, 依此欄排序\n";

        }

        void listView1_ItemActivate(object sender, EventArgs e)
        {
            richTextBox1.Text += "listView1_ItemActivate\n";
            ListView lw = (ListView)sender; //將觸發此事件的對象轉換為該ListView對象

            /*
            string filename = lw.SelectedItems[0].Tag.ToString();
            if (lw.SelectedItems[0].ImageIndex != 0)
            {
                try
                {
                    //Process.Start(filename);
                }
                catch
                {
                    return;
                }
            }
            else
            {
                //ShowListView(filename);
                //foldCol.Add(filename);
            }
            */
        }



        //檔案拖拽進入
        private void Files_DragEnter(object sender, DragEventArgs e)
        {
            if (e.Data.GetDataPresent(DataFormats.FileDrop))
            {
                e.Effect = DragDropEffects.Link;
            }
            else
            {
                e.Effect = DragDropEffects.None;
            }
        }

        //拖拽操作完成事件
        private void Files_DragDrop(object sender, DragEventArgs e)
        {
            try
            {
                //string fileName, fileExtension, fileSize, temp;

                Array array = (Array)e.Data.GetData(DataFormats.FileDrop);

                //richTextBox1.Text += "len = " + array.Length.ToString() + "\n"; //一次拖曳的檔案個數

                Regex regex = new Regex("(\\.mp3|\\.wav|\\.wma)");
                string filename;
                for (int i = 0; i < array.Length; i++)
                {
                    filename = array.GetValue(i).ToString();

                    FileInfo fi = new FileInfo(filename);

                    richTextBox1.Text += "fullname = " + filename + ",  name = " + fi.Name + ",  ext = " + fi.Extension + ",  size = " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                    ListViewItem lvi = new ListViewItem();
                    lvi.Text = fi.Name;
                    lvi.SubItems.AddRange(new string[] { filename, fi.Extension, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) });

                    listView1.Items.Add(lvi);

                    //屬於音樂檔案 且列表中不存在
                    if (regex.IsMatch(filename))
                    {
                        //InsertPlayList(out fileName, out fileExtension, out fileSize, out temp, out fi, out lvi, filename);
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
