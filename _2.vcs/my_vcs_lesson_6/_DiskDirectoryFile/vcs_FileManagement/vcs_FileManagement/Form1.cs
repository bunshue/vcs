using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;
using System.Globalization;  // for CultureInfo

using MediaInfoNET;

/*
參考/加入參考/選 MediaInfoNET.dll
加入/現有項目/選 MediaInfo.dll, 改屬性為 永遠複製
*/

namespace vcs_FileManagement
{
    public partial class Form1 : Form
    {
        string path = String.Empty;
        int filetype = 0;
        string filetype2 = String.Empty;
        Int64 total_size = 0;
        Int64 total_files = 0;
        Int64 total_folders = 0;
        Int64 folder_size = 0;
        Int64 folder_files = 0;
        int min_size_mb = 0;
        int flag_search_mode = 0;
        int flag_search_done = 0;
        int flag_search_vcs_pattern = 0;
        string FolederName;

        string video_player_path = String.Empty;
        string audio_player_path = String.Empty;
        string picture_viewer_path = String.Empty;
        string text_editor_path = String.Empty;
        string search_path = String.Empty;

        List<String> old_search_path = new List<String>();

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態
        List<MyFileInfo> fileinfos = new List<MyFileInfo>();

        public class MyFileInfo
        {
            public string filename;
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
                return size.ToString() + " Byte";//顯示Byte值
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            listView1.View = View.Details;//圖示
            listView1.GridLines = true;//網格線
        }

        private void show_item_location()
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
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            listView1.Size = new Size(800, 340 - 30);
            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 30);
            richTextBox1.Size = new Size(800, 340);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1050, 750);
            this.Text = "vcs_FileManagement";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            fileinfos.Clear();
            listView1.Clear();
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //資訊

            if (fileinfos.Count == 0)
            {
                richTextBox1.Text += "找不到資料a\n";
            }
            else
            {
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料\n";
            }


            //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));

            //richTextBox1.Text += "Name\tFolderName\tExt\tLength\tTime\n";
            for (int i = 0; i < fileinfos.Count; i++)
            {
                //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,20} X {3,20}{4,20}{5,20}",
                //fileinfos[i].filename, ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)), 
                //fileinfos[i].filepath, fileinfos[i].fileextension, fileinfos[i].filecreationtime) + "\n";


                //richTextBox1.Text += fileinfos[i].filename + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filesize + "\t" + fileinfos[i].filecreationtime + "\n";


                //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";


                //richTextBox1.Text += string.Format("{0,-60}{1,-60}{2,-60}{3,-60}{4,-60}", fileinfos[i].filename, fileinfos[i].filename, fileinfos[i].filename, fileinfos[i].filename, fileinfos[i].filename);
                //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
                richTextBox1.Text += string.Format("{0,-70}{1,-10}{2,-15}{3,-60}{4,-20}", fileinfos[i].filename, fileinfos[i].fileextension, ByteConversionTBGBMBKB(fileinfos[i].filesize), fileinfos[i].filepath, fileinfos[i].filecreationtime) + "\n";




                //ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //完全比對

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //搜尋同樣大小檔案

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //搜尋同樣檔名檔案
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //模糊比對

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //檔案資訊
            //檔案資訊
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            var GetFileName = Path.GetFileName(filename);
            var GetFileNameWithoutExtension = Path.GetFileNameWithoutExtension(filename);
            var GetExtension = Path.GetExtension(filename);
            var GetDirectoryName = Path.GetDirectoryName(filename);
            var GetFullPath = Path.GetFullPath(filename);

            var GetPathRoot = Path.GetPathRoot(filename);
            var GetRandomFileName = Path.GetRandomFileName();

            richTextBox1.Text += "filename\t" + filename + "\n";
            richTextBox1.Text += "GetFullPath\t" + GetFullPath + "\n";
            richTextBox1.Text += "GetDirectoryName\t" + GetDirectoryName + "\n";
            richTextBox1.Text += "GetFileName\t" + GetFileName + "\n";
            richTextBox1.Text += "GetFileNameWithoutExtension\t" + GetFileNameWithoutExtension + "\n";
            richTextBox1.Text += "GetExtension\t" + GetExtension + "\n";
            richTextBox1.Text += "GetPathRoot\t" + GetPathRoot + "\n";
            richTextBox1.Text += "GetRandomFileName\t" + GetRandomFileName + "\n";


        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        //獲得指定目錄下的所有文檔 ST

        double total_size1 = 0;
        int no_files = 0;
        int no_folders = 0;

        private void button9_Click(object sender, EventArgs e)
        {
            //獲得指定目錄下的所有文檔
            total_size1 = 0;
            no_files = 0;
            no_folders = 0;

            listView1.Columns.Add("名稱", 200, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 200, HorizontalAlignment.Center);
            listView1.Columns.Add("修改日期", 200, HorizontalAlignment.Center);
            //string filePath = @"D:/_git/vcs/_1.data/______test_files1/";
            string filePath = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            /*
            richTextBox1.Text += "轉出一層,獲得指定目錄下的所有文檔：\n";
            List<FileInfo> list1 = GetFilesByDir(filePath);
            foreach (FileInfo fi in list1)
            {
                //richTextBox1.Text += "完整路徑：" + fi.FullName.ToString() + " 文檔名：" + fi.Name + "\n";
                //richTextBox1.Text += "資料夾：" + fi.Directory + "\n";
                richTextBox1.Text += "檔名：" + fi.Name + "\t";
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + "\t";
                richTextBox1.Text += "修改日期：" + fi.LastWriteTime.ToString() + "\n";

                total_size1 += fi.Length;
                no_files++;

                ListViewItem i1 = new ListViewItem(fi.Name);
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                sub_i1a.Text = fi.Length.ToString();
                i1.SubItems.Add(sub_i1a);
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                sub_i1b.Text = fi.LastWriteTime.ToString();
                i1.SubItems.Add(sub_i1b);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
            */

            richTextBox1.Text += "轉出全部,列出指定目錄下及所有子目錄及子目錄裏更深層目錄裏的文檔：\n";
            GetAllFiles(filePath);

            label1.Text = "路徑：" + filePath + "\n大小：" + total_size1.ToString() + " 位元組\n內含：" + no_files.ToString() + " 個檔案，" + (no_folders - 1).ToString() + " 個資料夾";

            //大小：	xxxxx 位元組
            //內含：   143個檔案，18個資料夾

        }

        /// <summary>
        /// 獲得指定目錄下的所有文檔
        /// </summary>
        /// <param name="path"></param>
        /// <returns></returns>
        public List<FileInfo> GetFilesByDir(string path)
        {
            DirectoryInfo di = new DirectoryInfo(path);

            //找到該目錄下的文檔
            FileInfo[] fi = di.GetFiles();

            //把FileInfo[]數組轉換為List
            List<FileInfo> list = fi.ToList<FileInfo>();
            return list;
        }

        /// <summary>
        /// 列出指定目錄下及所其有子目錄及子目錄裏更深層目錄裏的文檔（需要遞歸）
        /// </summary>
        /// <param name="path"></param>
        public void GetAllFiles(string path)
        {
            DirectoryInfo dir = new DirectoryInfo(path);

            //找到該目錄下的文檔
            FileInfo[] fi = dir.GetFiles();
            foreach (FileInfo f in fi)
            {
                //richTextBox1.Text += "完整路徑：" + f.FullName.ToString() + " 文檔名：" + f.Name + "\n";
                //richTextBox1.Text += "資料夾：" + f.Directory + "\n";
                richTextBox1.Text += "檔名：" + f.Name + "\t";
                richTextBox1.Text += "大小：" + f.Length.ToString() + "\t";
                richTextBox1.Text += "日期：" + f.LastWriteTime.ToString() + "\n";

                total_size1 += f.Length;
                no_files++;

                ListViewItem i1 = new ListViewItem(f.Name);
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                sub_i1a.Text = f.Length.ToString();
                i1.SubItems.Add(sub_i1a);
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                sub_i1b.Text = f.LastWriteTime.ToString();
                i1.SubItems.Add(sub_i1b);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();


            }

            //找到該目錄下的所有目錄再遞歸
            DirectoryInfo[] subDir = dir.GetDirectories();
            no_folders++;
            foreach (DirectoryInfo d in subDir)
            {
                GetAllFiles(d.FullName);
            }
        }
        //獲得指定目錄下的所有文檔 SP
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

