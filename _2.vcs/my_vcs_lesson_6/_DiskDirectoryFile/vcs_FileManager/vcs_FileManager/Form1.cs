using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileInfo DirectoryInfo
using System.Diagnostics;   //for Process
using System.Globalization; //for CultureInfo

using MediaInfoNET;

namespace vcs_FileManager
{
    public partial class Form1 : Form
    {
        string video_player_path = String.Empty;
        string audio_player_path = String.Empty;
        string picture_viewer_path = String.Empty;
        //string text_editor_path = String.Empty;
        string search_path = String.Empty;

        List<String> old_search_path = new List<String>();

        Int64 total_size = 0;
        Int64 total_files = 0;
        //Int64 total_folders = 0;
        Int64 folder_size = 0;
        Int64 folder_files = 0;

        string FolederName = string.Empty;
        List<MyFileInfo> fileinfos = new List<MyFileInfo>();
        List<MyFileInfo> fileinfos_match = new List<MyFileInfo>();

        //bool flag_check_filesize = false;
        int check_filesize = 100;   //100 MB

        //bool flag_check_count = false;
        int skip_count = 100;
        int match_count = 0;

        bool flag_need_shortname = false;

        public class MyFileInfo
        {
            public string filename;
            public string fullfilename;
            public string shortfilename;
            public string filepath;
            public string fileextension;
            public long filesize;
            public DateTime filecreationtime;

            public int video_width;
            public int video_height;
            public int video_fps;
            public string video_duration;

            public MyFileInfo(string n, string p, string e, long s, DateTime c)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;
            }

            public MyFileInfo(string n, string fn, string sn, string p, string e, long s, DateTime c)
            {
                this.filename = n;
                this.fullfilename = fn;
                this.shortfilename = sn;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;
            }

            public MyFileInfo(string n, string p, string e, long s, DateTime c, int w, int h, int f, string d)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;

                this.video_width = w;
                this.video_height = h;
                this.video_fps = f;
                this.video_duration = d;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            listView1.GridLines = true;
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            listBox1.Items.Clear();

            foreach (string sss in old_search_path)
            {
                richTextBox1.Text += "add " + sss + "\n";
                listBox1.Items.Add(sss);
            }

            check_filesize = int.Parse(tb_filesize.Text);
            skip_count = int.Parse(tb_count.Text);

            string foldername = @"D:\_git\vcs\_1.data\______test_files3";
            listBox1.Items.Add(foldername);
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            int value = 0;
            bool conversionSuccessful = int.TryParse(tb_filesize.Text, out value);    //out為必須
            if (conversionSuccessful == true)
            {
                Properties.Settings.Default.min_file_size = value;
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
                richTextBox1.Text += "取得容量限制數字失敗\n";
            }

            conversionSuccessful = int.TryParse(tb_count.Text, out value);    //out為必須
            if (conversionSuccessful == true)
            {
                Properties.Settings.Default.search_count = value;
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
                richTextBox1.Text += "取得檔案個數數字失敗\n";
            }

            Properties.Settings.Default.Save();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 50 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            listBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            groupBox3.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            groupBox_file.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox2.Size = new Size(400 + 200, 250);
            richTextBox2.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            bt_add_dir.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0);
            bt_remove_dir.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0 + 30);
            bt_clear_dir.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0 + 60);

            listView1.Size = new Size(900, 650);
            listView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            richTextBox1.Size = new Size(900, 250);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 11);

            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_clear1.Width, richTextBox1.Location.Y);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Width - bt_clear2.Width, richTextBox2.Location.Y);
            bt_clear3.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear3.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear3.Size.Height);
            lb_find.Location = new Point(bt_clear3.Location.X - 200, bt_clear3.Location.Y);

            lb_files.Location = new Point(x_st + dx * 1 + 130, y_st + dy * 2);
            lb_filesize.Location = new Point(x_st + dx * 1 + 130, y_st + dy * 2 + 40);
            lb_find.Location = new Point(x_st + dx * 1 + 130, y_st + dy * 2 + 80);
            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";

            this.Size = new Size(1570, 980);
            this.Text = "vcs_FileManager";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        //------------------------------------------------------------  # 60個

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void bt_clear3_Click(object sender, EventArgs e)
        {
            listView1.Clear();
        }

        //------------------------------------------------------------  # 60個

        string get_shortname(string longname)
        {
            string shortname = longname;
            return shortname;
        }

        public void ProcessDirectory(string foldername)
        {
            string[] fileEntries = Directory.GetFiles(foldername);
            Array.Sort(fileEntries);
            folder_size = 0;
            folder_files = 0;
            foreach (string fileName in fileEntries)
            {
                ProcessFile(fileName);
            }
            //richTextBox1.Text += "folder_name = " + foldername + "\n";
            //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";
            //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
            if (folder_files == 0)
            {
                //richTextBox1.Text += "空資料夾 folder_name = " + foldername + "\n";
            }

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(foldername);
            Array.Sort(subdirectoryEntries);
            foreach (string subdirectory in subdirectoryEntries)
            {
                DirectoryInfo di = new DirectoryInfo(subdirectory);
                //richTextBox1.Text += "搜尋子目錄\t" + di.Name + "\n";
                FolederName = subdirectory;
                ProcessDirectory(subdirectory);
            }
        }

        public void ProcessFile(string filename)
        {
            //richTextBox1.Text += "處理File " + filename + "\n";

            FileInfo fi = new FileInfo(filename);

            //richTextBox2.Text += "folder = " + FolederName + ",  name = " + fi.Name + "\n";

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            if (cb_filesize.Checked == true)
            {
                check_filesize = int.Parse(tb_filesize.Text);
                if (fi.Length < (long)check_filesize * 1024 * 1024)
                {
                    return;
                }
            }

            string shortname = string.Empty;
            if (flag_need_shortname == true)
            {
                shortname = get_shortname(fi.Name);  //過濾掉檔名的一些字 用以做比較用
            }

            //richTextBox1.Text += "fname = " + fi.FullName + "\n";
            //richTextBox1.Text += "dname = " + fi.DirectoryName + "\n";

            //把資料放進 List<MyFileInfo> fileinfos 中
            fileinfos.Add(new MyFileInfo(fi.Name, fi.FullName, shortname, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));

            /*
            richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;
            */
        }


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

        private void check_cb_compare(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            /*
            int selNdx;
            string fullname;

            selNdx = listView1.SelectedIndices[0];

            richTextBox2.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox2.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox2.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox2.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            */

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

            /*
            richTextBox2.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox2.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox2.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox2.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            */

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

        private void bt_add_dir_Click(object sender, EventArgs e)
        {
            //folderBrowserDialog1.SelectedPath = search_path;  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                //path = folderBrowserDialog1.SelectedPath;
                richTextBox2.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                listBox1.Items.Add(folderBrowserDialog1.SelectedPath);
                old_search_path.Add(folderBrowserDialog1.SelectedPath);
            }
            else
            {
                richTextBox2.Text = "未選取資料夾\n";
            }
        }

        private void bt_remove_dir_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "移除了 " + listBox1.SelectedItem + "\n";
            old_search_path.Remove(folderBrowserDialog1.SelectedPath);
            listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void bt_clear_dir_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            old_search_path.Clear();
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

    }
}
