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
                return size.ToString() + " Byte";  // 顯示Byte值
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
            //儲存搜尋路徑
            string save_path = string.Empty;
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                save_path += listBox1.Items[i];
                if (i < (listBox1.Items.Count - 1))
                    save_path += ";";
            }
            Properties.Settings.Default.video_player_path = video_player_path;
            Properties.Settings.Default.audio_player_path = audio_player_path;
            Properties.Settings.Default.picture_viewer_path = picture_viewer_path;
            Properties.Settings.Default.search_path = save_path;

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

            Properties.Settings.Default.search_pattern = tb_find.Text;

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
            tb_find.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            groupBox_file.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox2.Size = new Size(400 + 200, 250);
            richTextBox2.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            bt_add_dir.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0);
            bt_remove_dir.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0 + 30);
            bt_clear_dir.Location = new Point(x_st + dx * 2 + 10, y_st + dy * 0 + 60);

            bt_start_files.Location = new Point(x_st + dx * 2 + 50, y_st + dy * 0);
            bt_start_files2.Location = new Point(x_st + dx * 2 + 50, y_st + dy * 1);

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

        void show_file_info()
        {
            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料a\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料c\n";

            string directory_old = string.Empty;
            for (int i = 0; i < fileinfos.Count; i++)
            {
                //debug mesg
                //richTextBox1.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                if (fileinfos[i].filepath != directory_old)
                {
                    directory_old = fileinfos[i].filepath;
                    //richTextBox1.Text += directory_old + "\n";
                }

                /*
                richTextBox1.Text += "\tfname: " + fileinfos[i].fullfilename;
                richTextBox1.Text += "\tdname: " + fileinfos[i].filepath;
                richTextBox1.Text += "\tsn: " + fileinfos[i].shortfilename;
                richTextBox1.Text += "\tpath: " + fileinfos[i].filepath;
                richTextBox1.Text += "\text: " + fileinfos[i].fileextension;

                richTextBox1.Text += "\n";
                */

            }

            show_MyFileInfo(fileinfos);
            lb_find.Text = "個數 : " + fileinfos.Count.ToString() + " 個";
        }

        void show_MyFileInfo(List<MyFileInfo> fis)
        {
            if (fis.Count == 0)
            {
                richTextBox1.Text += "無資料b\n";
                return;
            }
            else
            {
                richTextBox1.Text += "找到 " + fis.Count.ToString() + " 筆資料b\n";
            }
            listView1.Clear();

            listView1.Columns.Add("檔名", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 90, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 500, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("簡名", 180, HorizontalAlignment.Left);
            listView1.Columns.Add("格式", 180, HorizontalAlignment.Left);
            listView1.Visible = true;

            for (int i = 0; i < fis.Count; i++)
            {
                //ListViewItem i1 = new ListViewItem(fis[i].filename);
                ListViewItem i1;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1d = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1e = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1f = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1g = new ListViewItem.ListViewSubItem();

                string itema = string.Empty;    //檔名
                string itemb = string.Empty;    //大小
                string itemc = string.Empty;    //資料夾
                string itemd = string.Empty;    //副檔名
                string iteme = string.Empty;    //修改日期
                string itemf = string.Empty;    //簡名
                string itemg = string.Empty;     //格式 W X H

                /*
                //debug mesg
                richTextBox2.Text += "i = " + i.ToString() + ", filename : " + fis[i].filepath + "\\" + fis[i].filename + "\t"
                    + fis[i].fileextension + "\t" + fis[i].filecreationtime + "\t" + fis[i].filesize + "\n";
                */

                itema = fis[i].filename;
                itemb = ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize));
                itemc = fis[i].filepath;
                itemd = fis[i].fileextension;
                iteme = fis[i].filecreationtime.ToString();
                itemf = get_shortname(fis[i].filename);  //過濾掉檔名的一些字 用以做比較用

                //i1 = new ListViewItem(fis[i].filename);
                //richTextBox2.Text += "aaaaaa : " + itema + "\n";
                i1 = new ListViewItem(itema);
                i1.UseItemStyleForSubItems = false;

                //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                sub_i1b.Text = itemb;
                i1.SubItems.Add(sub_i1b);

                sub_i1c.Text = itemc;
                i1.SubItems.Add(sub_i1c);
                //sub_i1a.Text = fis[i].filepath;
                //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                sub_i1d.Text = itemd;
                i1.SubItems.Add(sub_i1d);

                sub_i1e.Text = iteme;
                i1.SubItems.Add(sub_i1e);

                //sub_i1a.Text = fi.Length.ToString();
                //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize));
                //sub_i1c.Text = itemc;
                //i1.SubItems.Add(sub_i1c);

                sub_i1f.Text = itemf;
                i1.SubItems.Add(sub_i1f);

                sub_i1a.ForeColor = System.Drawing.Color.Blue;
                sub_i1b.ForeColor = System.Drawing.Color.Blue;
                sub_i1c.ForeColor = System.Drawing.Color.Blue;
                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                sub_i1c.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                listView1.Items.Add(i1);

                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "撈出資料夾多層檔案\n";
            //從一個資料夾中撈出所有檔案 標準版

            if (listBox1.Items.Count == 0)
            {
                richTextBox2.Text += "未選擇資料夾\n";
                return;
            }

            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";

            //轉出多層
            fileinfos.Clear();
            fileinfos_match.Clear();
            listView1.Clear();

            total_size = 0;
            total_files = 0;

            string path;
            richTextBox2.Text += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                path = listBox1.Items[i].ToString();

                richTextBox2.Text += "\n搜尋路徑" + path + "\n";

                if (System.IO.File.Exists(path) == true)
                {
                    // This path is a file
                    richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                    ProcessFile(path);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                }
                else if (Directory.Exists(path) == true)
                {
                    // This path is a directory
                    FolederName = path;
                    ProcessDirectory(path);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                }
                else
                {
                    //Console.WriteLine("{0} is not a valid file or directory.", path);
                    richTextBox1.Text += "非合法路徑或檔案b\n";
                }
            }

            //show_file_info();

            lb_files.Text = "檔案個數 : " + total_files.ToString();
            lb_filesize.Text = "總容量   : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";

            show_file_info();

            lb_files.Text = "檔案個數 : " + total_files.ToString();
            lb_filesize.Text = "總容量   : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size));
        }

        private void button3_Click(object sender, EventArgs e)
        {
            flag_need_shortname = true;

            button1_Click(sender, e);   //do_search_recurrsively

            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料c\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料b\n";

            int len = fileinfos.Count;
            if (len < 2)
                return;

            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";

            match_count = 0;
            fileinfos_match.Clear();

            int i;
            int j;
            for (i = 0; i < len; i++)
            {
                if (cb_compare4.Checked == true)    //僅影音檔案
                {
                    if ((fileinfos[i].filename.Contains(".zip") == true) || (fileinfos[i].filename.Contains(".rar") == true))
                    {
                        continue;
                    }
                }

                for (j = i + 1; j < (len - 1); j++)
                {
                    if (cb_compare4.Checked == true)    //僅影音檔案
                    {
                        if ((fileinfos[j].filename.Contains(".zip") == true) || (fileinfos[j].filename.Contains(".rar") == true))
                        {
                            continue;
                        }
                    }

                    if (cb_compare0.Checked == true)    //比較真檔名
                    {
                        if (fileinfos[i].filename == fileinfos[j].filename)
                        {
                            richTextBox1.Text += "找到真檔名\n";
                            richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                            richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                            fileinfos_match.Add(fileinfos[i]);
                            fileinfos_match.Add(fileinfos[j]);
                            match_count++;
                        }
                    }

                    if (cb_compare1.Checked == true)    //比較模糊檔名
                    {
                        if (fileinfos[i].shortfilename == fileinfos[j].shortfilename)
                        {
                            richTextBox1.Text += "找到模糊檔名\n";
                            richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                            richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                            fileinfos_match.Add(fileinfos[i]);
                            fileinfos_match.Add(fileinfos[j]);
                            match_count++;
                        }
                    }

                    if (cb_compare2.Checked == true)    //比較檔案大小
                    {
                        if (fileinfos[i].filesize == fileinfos[j].filesize)
                        {
                            richTextBox1.Text += "找到相同檔案大小\n";
                            richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                            richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                            fileinfos_match.Add(fileinfos[i]);
                            fileinfos_match.Add(fileinfos[j]);
                            match_count++;
                        }
                    }

                    if (cb_checkcount.Checked == true)
                    {
                        skip_count = int.Parse(tb_count.Text);
                        if (match_count > skip_count)
                        {
                            richTextBox1.Text += "滿 " + skip_count.ToString() + " 項, 提前結束\n";
                            break;
                        }
                    }
                }

                if (cb_checkcount.Checked == true)
                {
                    skip_count = int.Parse(tb_count.Text);
                    if (match_count > skip_count)
                    {
                        richTextBox1.Text += "滿 " + skip_count.ToString() + " 項, 提前結束\n";
                        break;
                    }
                }
            }

            richTextBox1.Text += "show match files\n";
            show_MyFileInfo(fileinfos_match);
            flag_need_shortname = false;

            lb_find.Text = "個數 : " + fileinfos_match.ToString() + " 個";
        }

        private void check_cb_compare(object sender, EventArgs e)
        {
            //richTextBox1.Text += "你按了 " + ((CheckBox)sender).Name + "\n";
            string name = ((CheckBox)sender).Name;
            if (name == "cb_compare0")
            {
                if (cb_compare0.Checked == true)
                {
                    cb_compare1.Checked = false;
                }
            }
            else if (name == "cb_compare1")
            {
                if (cb_compare1.Checked == true)
                {
                    cb_compare0.Checked = false;
                }
            }
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

        private void bt_start_files_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;
            richTextBox2.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < selectCount; i++)
            {
                richTextBox2.Text += listView1.SelectedItems[i].SubItems[2].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }
            richTextBox2.Text += "開啟\n";

            int selNdx;
            string all_filename = string.Empty;

            if (selectCount <= 0)  //總共選擇的個數
            {
                richTextBox2.Text += "無檔案\n";
                return;
            }

            //richTextBox2.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";

            //for (int i = 0; i < selectCount; i++) //same
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox2.Text += listView1.Items[selNdx].Text + "\n";

                all_filename += " \"" + listView1.Items[selNdx].SubItems[2].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text + "\"";
            }

            //指定應用程式路徑
            string target = String.Empty;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二

            target = video_player_path;

            ProcessStartInfo pInfo = new ProcessStartInfo(target);
            pInfo.Arguments = all_filename;

            /*
            // debug mesg
            richTextBox2.Text += "target : " + target + "\n";
            richTextBox2.Text += "all_filename : " + all_filename + "\n";
            */

            if (video_player_path == String.Empty)
            {
                all_filename = all_filename.Trim().Replace("\"", "");
                Process.Start(all_filename); //使用預設程式開啟, 無法一次播放多個檔案
            }
            else
            {
                Process.Start(video_player_path, all_filename);    //指名播放程式開啟
            }

            /*
            using (Process process = new Process())
            {
                process.StartInfo = pInfo;
                process.Start();
            }
            */
        }

        private void bt_start_files2_Click(object sender, EventArgs e)
        {
            //全選播放

            int len = listView1.Items.Count;
            for (int i = 0; i < len; i++)
            {
                listView1.Items[i].Selected = true;
            }

            int selectCount = listView1.SelectedIndices.Count;
            richTextBox2.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < selectCount; i++)
            {
                richTextBox2.Text += listView1.SelectedItems[i].SubItems[2].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }
            richTextBox2.Text += "開啟\n";

            int selNdx;
            string all_filename = string.Empty;

            if (selectCount <= 0)  //總共選擇的個數
            {
                richTextBox2.Text += "無檔案\n";
                return;
            }

            //richTextBox2.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";

            //for (int i = 0; i < selectCount; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox2.Text += listView1.Items[selNdx].Text + "\n";

                all_filename += " \"" + listView1.Items[selNdx].SubItems[2].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text + "\"";
            }

            //指定應用程式路徑
            string target = String.Empty;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二

            target = video_player_path;

            ProcessStartInfo pInfo = new ProcessStartInfo(target);
            pInfo.Arguments = all_filename;

            /*
            // debug mesg
            richTextBox2.Text += "target : " + target + "\n";
            richTextBox2.Text += "all_filename : " + all_filename + "\n";
            */

            if (video_player_path == String.Empty)
            {
                all_filename = all_filename.Trim().Replace("\"", "");
                Process.Start(all_filename); //使用預設程式開啟, 無法一次播放多個檔案
            }
            else
            {
                Process.Start(video_player_path, all_filename);    //指名播放程式開啟
            }

            /*
            using (Process process = new Process())
            {
                process.StartInfo = pInfo;
                process.Start();
            }
            */
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox2.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 bt_start_files_Click
                bt_start_files_Click(sender, e);
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
            //搜尋特定檔名

            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料c\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料b\n";

            int len = fileinfos.Count;
            if (len < 2)
                return;

            listView1.Clear();
            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";

            match_count = 0;
            fileinfos_match.Clear();

            for (int i = 0; i < len; i++)
            {

                if (fileinfos[i].filename.ToLower().Contains(tb_find.Text.ToLower()) == true)
                {
                    fileinfos_match.Add(fileinfos[i]);
                    match_count++;
                }
                if (cb_checkcount.Checked == true)
                {
                    skip_count = int.Parse(tb_count.Text);
                    if (match_count > skip_count)
                    {
                        richTextBox1.Text += "滿 " + skip_count.ToString() + " 項, 提前結束\n";
                        break;
                    }
                }
            }

            richTextBox1.Text += "show match files\n";
            show_MyFileInfo(fileinfos_match);

            lb_find.Text = "個數 : " + fileinfos_match.ToString() + " 個";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //優優檔
            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料c\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料b\n";

            int len = fileinfos.Count;
            if (len < 2)
                return;

            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";

            match_count = 0;
            fileinfos_match.Clear();

            string[] good_pattern = new string[] {
                  "asami", "yuna", "kaede", "hayashi", "julia", "jjjj", "chitose"    //A class
                , "nozomi", "anri", "jessica", "airi", "ths", "saeko", ""
                , "松島", "桐原", "冬月", "小川", "椎名", "宮瀬", "QQQQ"
                , "smr", "yama", "maria", "akari", "maron", "ryo", "QQQQ"
                , "mai", "karen", "rinne", "miu", "kano", "QQQQ", "QQQQ"
                , "suzu", "yuri", "sakura", "nanami", "minami", "iori", "QQQQ"
                , "1111", "3333", "7777", "9999", "mino", "megumi", "QQQQ"
                , "kurara", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "立花", "愛世", "美月", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "kana", "tia", "momo", "yui", "sho", "nene", "園田"    //B class
                , "ayaka", "jgj", "sora", "bt", "maki", "ayumi", "mion"
                , "本田岬", "lily", "lauren", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "gggg", "debut", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"    //new tmp
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
            };

            int i;
            for (i = 0; i < len; i++)
            {
                foreach (string ptn in good_pattern)
                {
                    if (fileinfos[i].filename.ToLower().Contains(ptn) == true)
                    {
                        fileinfos_match.Add(fileinfos[i]);
                        match_count++;
                        break;
                    }
                }
                if (cb_checkcount.Checked == true)
                {
                    skip_count = int.Parse(tb_count.Text);
                    if (match_count > skip_count)
                    {
                        richTextBox1.Text += "滿 " + skip_count.ToString() + " 項, 提前結束\n";
                        break;
                    }
                }
            }

            richTextBox1.Text += "show match files\n";
            show_MyFileInfo(fileinfos_match);
            lb_find.Text = "個數 : " + fileinfos_match.ToString() + " 個";
        }

        private void tb_find_KeyPress(object sender, KeyPressEventArgs e)
        {
            //e.Handled = check_textbox_hexadecimal(e);

            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                button5_Click(sender, e);
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

