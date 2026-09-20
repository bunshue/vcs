using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//新進的 ListView 測試

namespace vcs_ListView7_new
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

            // listView1的共同設定, 設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true;  // 顯示格線
            listView1.LabelEdit = true;  // 設定listView1的可編輯屬性為真 listView可修改Label
            listView1.LabelEdit = true;  // 允許使用者修改listView的資料
            listView1.MultiSelect = true;// 是否允許多行選擇
            listView1.Scrollable = true;   //需要時候顯示滾動條
            //listView1.CheckBoxes = true;//使用CheckBox(核取方塊)
            //listView1.HeaderStyle = ColumnHeaderStyle.Nonclickable; ??

            //設定欄位, 欄名, 欄寬, 對齊方式
            listView1.Columns.Add("中文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("英文名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("體重", 60, HorizontalAlignment.Left);

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
            item4.SubItems.Add("8");

            /*
            // listView1.ContextMenuStrip = contextMenuStrip1;
            listView1.KeyDown += new KeyEventHandler(listView1_KeyDown);
            listView1.MouseMove += new MouseEventHandler(listView1_MouseMove);

            listView1.AfterLabelEdit += new LabelEditEventHandler(listView1_AfterLabelEdit);
            */
            listView1.SelectedIndexChanged += new EventHandler(listView1_SelectedIndexChanged);
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
            int dd = 40;
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd * 1);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd * 2);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd * 3);
            label5.Location = new Point(x_st + dx * 0, y_st + dy * 5 + dd * 4);

            listView1.Size = new Size(830, 690);
            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Size = new Size(410, 690);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1500, 750);
            this.Text = "vcs_ListView7_new";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        void show_listView()
        {
            listView1.View = View.Details;  // 定義列表顯示的方式
            listView1.FullRowSelect = true;  // 整行一起選取
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("檔名", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 90, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("簡名", 180, HorizontalAlignment.Left);
            listView1.Columns.Add("格式", 180, HorizontalAlignment.Left);

            for (int i = 0; i < 10; i++)
            {
                //w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                //fis[i].filepath;
                //ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize));
            }

            //this.Controls.Add(listView1);

            //加入
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_listView();
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "listView1_MouseClick\n";
            int selNdx;
            string fullname;
            selNdx = listView1.SelectedIndices[0];
            richTextBox1.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox1.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox1.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            //richTextBox1.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";

            listView1.Items[selNdx].Selected = true;    //選到的項目

            int selectCount = listView1.SelectedIndices.Count;
            richTextBox1.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案\t";
            richTextBox1.Text += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox1.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox1.Text += "你選擇了\t" + listView1.Items[selNdx].Text + "\n";

            string fullname;
            selNdx = listView1.SelectedIndices[0];
            richTextBox1.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox1.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox1.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            //richTextBox1.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目

            int selectCount = listView1.SelectedIndices.Count;
            richTextBox1.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案\t";
            richTextBox1.Text += "你選擇了資料夾:\t" + listView1.Items[selNdx].Text + "\n";

            fullname = listView1.Items[selNdx].SubItems[2].Text + "\\" + listView1.Items[selNdx].Text;

            richTextBox1.Text += "開啟路徑: " + fullname + "\n";

            // 準備開啟所選擇的項目
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            richTextBox1.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

            if (e.KeyCode == Keys.A)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    //richTextBox1.Text += "Ctrl + A\n";
                    //richTextBox1.Text += "共有項目" + listView1.Items.Count.ToString() + " 個\n";

                    for (int i = 0; i < listView1.Items.Count; i++)
                    {
                        //richTextBox1.Text += listView1.Items[i] + "\n";
                        listView1.Items[i].Selected = true;
                    }
                }
            }

            if (e.KeyCode == Keys.Enter)
            {
                //等同於 button9_Click , 以後要改成只是呼叫函數

                richTextBox1.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
                for (int i = 0; i < listView1.SelectedIndices.Count; i++)
                {
                    richTextBox1.Text += listView1.SelectedItems[i] + "\n";
                }

                richTextBox1.Text += "播放\n";

                int selNdx;
                string all_filename = string.Empty;
                string player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
                if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
                {
                    richTextBox1.Text += "無檔可播\n";
                    return;
                }

                int SelectedItemsCount = listView1.SelectedItems.Count;
                //richTextBox1.Text += "總共選了 : " + SelectedItemsCount.ToString() + " 個檔案，分別是 : \n";
                //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
                for (int i = 0; i < SelectedItemsCount; i++)
                {
                    selNdx = listView1.SelectedIndices[i];
                    listView1.Items[selNdx].Selected = true;    //選到的項目
                    //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                    all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
                }
            }


            //richTextBox1.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 播放
                //TBD
            }
            else if (e.KeyCode == Keys.Delete)
            {
                int selectCount = listView1.SelectedIndices.Count;
                if (selectCount <= 0)  //總共選擇的個數
                {
                    richTextBox1.Text += "未選擇要刪除的項目\n";
                    return;
                }

                richTextBox1.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
                for (int i = 0; i < selectCount; i++)
                {
                    string filename = listView1.SelectedItems[i].SubItems[2].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text;
                    richTextBox1.Text += "刪除 : " + filename + "\n";
                    System.IO.File.Delete(filename);

                    int selectIndex = listView1.SelectedItems[i].Index;
                    listView1.Items.RemoveAt(selectIndex);
                }
            }
        }

        private void listView1_MouseMove(object sender, MouseEventArgs e)
        {
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null)
            {
                return;
            }
            ListViewItem item = hti.Item;

            label1.Text = "列 : " + item.Index.ToString();
            label2.Text = "欄 : " + item.SubItems.IndexOf(hti.SubItem).ToString();

            ListViewItem.ListViewSubItem subitem = hti.SubItem;
            label3.Text = "內容 : " + subitem.Text.ToString();

            //此列長度
            label4.Text = "列長度 : " + item.SubItems.Count.ToString();

            string mesg = string.Empty;

            for (int i = 0; i < item.SubItems.Count; i++)
            {
                //richTextBox1.Text += item.SubItems[i].Text + " ";
                mesg += item.SubItems[i].Text + " ";
                if (item.SubItems[i] == subitem)
                {
                    //label4.Text = i.ToString();
                    //richTextBox1.Text += i.ToString() + " ";
                }
            }
            //richTextBox1.Text += "\n";

            label5.Text = mesg;
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int SelectedItemsCount = listView1.SelectedItems.Count;

            richTextBox1.Text += "SelectedIndexChanged, 選擇個數 : " + SelectedItemsCount.ToString() + "\n";

            if (SelectedItemsCount > 0)
            {
                richTextBox1.Text += "總共選了 : " + SelectedItemsCount.ToString() + " 項，分別是 : \n";
                for (int i = 0; i < SelectedItemsCount; i++)
                {
                    richTextBox1.Text += listView1.SelectedItems[i].Text + "\n";
                    //idx = listView1.SelectedIndices[i];
                }
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//listView1.SelectedItems[0].Text

/*
            //播放 listview 多選的檔案
int selectCount = listView1.SelectedIndices.Count;
            int selNdx;
            string all_filename = string.Empty;
            string player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
            if (selectCount <= 0)  //總共選擇的個數
                return;

            int SelectedItemsCount = listView1.SelectedItems.Count;
            //richTextBox1.Text += "總共選了 : " + SelectedItemsCount.ToString() + " 個檔案，分別是 : \n";
            for (int i = 0; i < SelectedItemsCount; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
            }

            //指定應用程式路徑
            //string target = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
            string target = player_path;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二
            ProcessStartInfo pInfo = new ProcessStartInfo(target);
            pInfo.Arguments = all_filename;

            richTextBox1.Text += "target : " + target + "\n";
            richTextBox1.Text += "all_filename : " + all_filename + "\n";

            using (Process process = new Process())
            {
                process.StartInfo = pInfo;
                process.Start();    //啟動程式
            }
*/


/*
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                richTextBox2.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\n";
            }
*/

/*
            //設定欄位
            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "文件名稱";
            ch1.Width = 330;
            listView1.Columns.Add(ch1);

            listView1.GridLines = true;  // 網格線
            listView1.View = View.Details;  //定義列表顯示的方式

            listView1.Items.Clear();

            listView1.Items.Add(fi.FullName);
*/


