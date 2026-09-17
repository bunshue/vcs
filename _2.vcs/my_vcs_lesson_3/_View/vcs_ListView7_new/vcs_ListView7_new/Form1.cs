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

            listView1.Size = new Size(830, 690);
            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox1.Size = new Size(410, 690);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1500, 750);
            this.Text = "vcs_ListView7_new";

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

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

        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {

        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
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






//listView1.SelectedItems[0].Text

/*

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox1.Text += "你選擇了\t" + listView1.Items[selNdx].Text + "\n";
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox1.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

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

                //richTextBox1.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
                //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
                for (int i = 0; i < listView1.SelectedItems.Count; i++)
                {
                    selNdx = listView1.SelectedIndices[i];
                    listView1.Items[selNdx].Selected = true;    //選到的項目
                    //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                    all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
                }
            }
        }

//------------------------------------------------------------  # 60個

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            int selNdx;
            string fullname;
            selNdx = listView1.SelectedIndices[0];
            richTextBox2.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox2.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox2.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox2.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";

            int selNdx;
            //string fullname;

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目

            int selectCount = listView1.SelectedIndices.Count;
            richTextBox2.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案\t";
            richTextBox2.Text += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx;
            string fullname;
            selNdx = listView1.SelectedIndices[0];
            richTextBox2.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox2.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox2.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox2.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目

            int selectCount = listView1.SelectedIndices.Count;
            richTextBox2.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案\t";
            richTextBox2.Text += "你選擇了資料夾:\t" + listView1.Items[selNdx].Text + "\n";

            fullname = listView1.Items[selNdx].SubItems[2].Text + "\\" + listView1.Items[selNdx].Text;

            richTextBox1.Text += "開啟路徑: " + fullname + "\n";

            //richTextBox2.Text += "video_player_path = " + video_player_path + "\n";
            richTextBox2.Text += "fullname = " + fullname + "\n";

            if (video_player_path == String.Empty)
            {
                Process.Start(fullname); //使用預設程式開啟
            }
            else
            {
                if (System.IO.File.Exists(video_player_path) == true)
                {
                    Process.Start(video_player_path, fullname);    //指名播放程式開啟
                }
            }
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox2.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

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

                richTextBox2.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
                for (int i = 0; i < selectCount; i++)
                {
                    string filename = listView1.SelectedItems[i].SubItems[2].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text;
                    richTextBox2.Text += "刪除 : " + filename + "\n";
                    System.IO.File.Delete(filename);

                    int selectIndex = listView1.SelectedItems[i].Index;
                    listView1.Items.RemoveAt(selectIndex);
                }
            }
        }

//------------------------------------------------------------  # 60個

        void show_listView()
        {
            listView1.View = View.Details;  // 定義列表顯示的方式
            listView1.FullRowSelect = true;  // 整行一起選取
            listView1.Clear();

            listView1.GridLines = true;  // 網格線
            listView1.Size = new Size(640 * 2, 480 * 2);

            //設置列名稱
            listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("檔名1", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.MouseClick += new MouseEventHandler(listView1_MouseClick);

            this.Controls.Add(listView1);

            //加入
        }


void show_MyFileInfo(List<MyFileInfo> fis)
{
    listView1.Columns.Add("檔名", 300, HorizontalAlignment.Left);
    listView1.Columns.Add("大小", 90, HorizontalAlignment.Left);
    listView1.Columns.Add("資料夾", 500, HorizontalAlignment.Left);
    listView1.Columns.Add("副檔名", 80, HorizontalAlignment.Left);
    listView1.Columns.Add("修改日期", 150, HorizontalAlignment.Left);
    listView1.Columns.Add("簡名", 180, HorizontalAlignment.Left);
    listView1.Columns.Add("格式", 180, HorizontalAlignment.Left);

    for (int i = 0; i < fis.Count; i++)
    {
        //itemf = get_shortname(fis[i].filename);  //過濾掉檔名的一些字 用以做比較用

        //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

        //sub_i1a.Text = fis[i].filepath;
        //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

        //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize));
    }
}

//------------------------------------------------------------  # 60個

            listView1.GridLines = true;
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

//------------------------------------------------------------  # 60個


*/


