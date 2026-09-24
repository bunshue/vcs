using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for Directory, StreamReader, SearchOption
using System.Collections;  // for ArrayList
using System.Diagnostics;  // for Stopwatch
using System.Runtime.InteropServices;   //for DllImport, Marshal, StructLayout
using Microsoft.VisualBasic.FileIO;  // for 刪除檔案(使用資源回收筒)

//using MediaInfoNET; 不要用
using System.Globalization; //for CultureInfo

/*
使用MediaInfo獲取視頻或音頻的屬性
MediaInfo:	http://mediainfo.sourceforge.net/
把：
MediaInfoNET_v1.0_Binaries.7z裏面的：
MediaInfo.dll
MediaInfoNET.dll
放在 \bin\Debug 裏。
參考/加入參考/瀏覽/選取\bin\Debug\MediaInfoNET.dll
專案加入 MediaInfo.dll, 屬性選擇 有更新時才複製
加入命名空間  using MediaInfoNET;
*/

namespace vcs_DiskDirectoryFile1
{
    public partial class Form1 : Form
    {
        bool flag_my_file_manager = false;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\";
        string doc_foldername = string.Empty;
        string video_foldername = string.Empty;
        string video_player_path = String.Empty;
        string tb_foldername_text_old = string.Empty;
        string tb_filename_text_old = string.Empty;
        int filesize_min = 0;

        private const int PROCESS_FILE_MODE0 = 0x00;  // 0:預設只匯出檔名
        private const int PROCESS_FILE_MODE1 = 0x01;  // 1:只看大檔
        private const int PROCESS_FILE_MODE2 = 0x02;  // 2:顯示至 ListView
        private const int PROCESS_FILE_MODE3 = 0x03;  // 3:找空資料夾
        private const int PROCESS_FILE_MODE4 = 0x04;  // 4:找小資料夾
        private const int PROCESS_FILE_MODE5 = 0x05;  // 5:找特定檔案
        private const int PROCESS_FILE_MODE6 = 0x06;  // 6:指定附檔名檔案
        private const int PROCESS_FILE_MODE7 = 0x07;  // 7:只找資料夾 for 圖片整理
        private const int PROCESS_FILE_MODE8 = 0x08;  // 8:搜尋影片檔, 搜尋小影片檔<720, 特大影片檔>1080
        private const int PROCESS_FILE_MODE9 = 0x09;  // 9:匯出Katfile壓縮檔檔案資料

        int ProcessFile_mode = PROCESS_FILE_MODE0;  // 0:預設只匯出檔名

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

        public string TimeConversion(Int64 seconds)
        {
            if (seconds < 0)
            {
                return "不合法的數值";
            }
            else if (seconds < 60)
            {
                return seconds.ToString("D2") + " 秒";
            }
            else if (seconds < 60 * 60)
            {
                return (seconds / 60).ToString("D2") + " 分 " + (seconds % 60).ToString("D2") + " 秒";
            }
            else if (seconds < 60 * 60 * 24)
            {
                return (seconds / 60 / 60).ToString("D2") + " 時 " + ((seconds % 3600) / 60).ToString("D2") + " 分 " + (seconds % 60).ToString("D2") + " 秒";
            }
            else
            {
                return (seconds / 60 / 60 / 24).ToString() + " 天 " + ((seconds % (60 * 60 * 24)) / 60 / 60).ToString("D2") + " 時 " + ((seconds % 3600) / 60).ToString("D2") + " 分 " + (seconds % 60).ToString("D2") + " 秒";
            }
        }

        public class MyFileInfo
        {
            public string filename;
            public string fullfilename;
            public string shortfilename;
            public string filepath;
            public string fileextension;
            public long filesize;

            public int video_width;
            public int video_height;
            public int video_fps;
            public int video_duration;
            /*
            public MyFileInfo(string n, string p, string e, long s)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
            }

            public MyFileInfo(string n, string fn, string sn, string p, string e, long s)
            {
                this.filename = n;
                this.fullfilename = fn;
                this.shortfilename = sn;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
            }
            */
            //影片用
            public MyFileInfo(string n, string p, string e, long s, int w, int h, int f, int d)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;

                this.video_width = w;
                this.video_height = h;
                this.video_fps = f;
                this.video_duration = d;
            }
        }

        public class MyFolderInfo
        {
            public string foldername;
            public string folderpath;
            public long foldersize;
            public MyFolderInfo(string n, string p, long s)
            {
                this.foldername = n;
                this.folderpath = p;
                this.foldersize = s;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態
        List<MyFileInfo> fileinfos = new List<MyFileInfo>();
        List<MyFileInfo> fileinfos_match = new List<MyFileInfo>();
        List<MyFolderInfo> folderinfos = new List<MyFolderInfo>();

        Int64 total_size = 0;  // 所有的檔案大小
        Int64 total_files = 0;  // 所有的檔案個數
        Int64 total_folders = 0;  //所有的資料夾個數
        Int64 folder_files = 0;  // 資料夾內的檔案個數
        Int64 folder_size = 0;  // 資料夾的檔案大小 留做小資料夾用
        string text = string.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (flag_my_file_manager == true)
            {
                show_item_location_my_file_manager();
            }
            else
            {
                show_item_location();
            }

            //------------------------------------------------------------  # 60個

            listView1.View = View.Details;  // 定義列表顯示的方式
            listView1.FullRowSelect = true;  // 整行一起選取
            listView1.GridLines = true;
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("檔名", 180, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("格式", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 700, HorizontalAlignment.Left);
            listView1.MouseClick += new MouseEventHandler(listView1_MouseClick);
            listView1.MouseDoubleClick += new MouseEventHandler(listView1_MouseDoubleClick);
            listView1.ColumnClick += new ColumnClickEventHandler(listView1_ColumnClick);

            //------------------------------------------------------------  # 60個

            filesize_min = Properties.Settings.Default.filesize_min;
            video_player_path = Properties.Settings.Default.video_player_path;
            doc_foldername = Properties.Settings.Default.doc_foldername;
            video_foldername = Properties.Settings.Default.video_foldername;
            cb_size.Checked = Properties.Settings.Default.flag_check_filesize;
            cb_search_big_files.Checked = Properties.Settings.Default.flag_find_big_files;
            cb_search_small_files.Checked = Properties.Settings.Default.flag_find_small_files;
            tb_size.Text = filesize_min.ToString();
            tb_foldername1.Text = doc_foldername;
            tb_foldername2.Text = video_foldername;

            if (System.IO.File.Exists(Properties.Settings.Default.video_player_path) == false)
            {
                richTextBox1.Text += "播放影片程式不存在 : " + Properties.Settings.Default.video_player_path + "\n使用Windows預設播放影片程式\n";
                video_player_path = String.Empty;
            }
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (tb_foldername1.Text != "")
            {
                if (Directory.Exists(tb_foldername1.Text) == true)
                {
                    Properties.Settings.Default.doc_foldername = tb_foldername1.Text;
                    Properties.Settings.Default.Save();
                }
            }
            if (tb_foldername2.Text != "")
            {
                if (Directory.Exists(tb_foldername2.Text) == true)
                {
                    Properties.Settings.Default.video_foldername = tb_foldername2.Text;
                    Properties.Settings.Default.Save();
                }
            }
            int number = 0;
            bool conversionSuccessful = int.TryParse(tb_size.Text, out number);    //out為必須
            if (conversionSuccessful == true)
                richTextBox1.Text += "得到int數字： " + number + "\n";
            else
                richTextBox1.Text += "int.TryParse 失敗\n";
            Properties.Settings.Default.filesize_min = number;
            Properties.Settings.Default.flag_check_filesize = cb_size.Checked;
            Properties.Settings.Default.flag_find_big_files = cb_search_big_files.Checked;
            Properties.Settings.Default.flag_find_small_files = cb_search_small_files.Checked;

            Properties.Settings.Default.Save();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            int W = 1240;
            groupBox1.Size = new Size(W, 106 + 50);
            groupBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0 - 14);

            listView1.Size = new Size(W, 270 - 50);
            listView1.Location = new Point(x_st + dx * 3, y_st + dy * 1 + 24 + 50);
            bt_clear2.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear2.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear2.Size.Height);

            richTextBox1.Size = new Size(W, 340);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 5 + 24);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //button
            y_st += 24;

            bt_file00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_file01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_file02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_file03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_file04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_file05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_file06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_file07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_file08.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_file09.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_dir00.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_dir01.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_dir02.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_dir03.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_dir04.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_dir05.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_dir06.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            bt_dir07.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            bt_dir08.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            bt_dir09.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            bt_files00.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_files01.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_files02.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_files03.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            bt_files04.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            bt_files05.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            bt_files06.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            bt_files07.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            bt_files08.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            bt_files09.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            show_item_location_common();
        }

        void show_item_location_my_file_manager()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            label0.Visible = false;
            label1.Visible = false;
            label2.Visible = false;
            bt_file00.Visible = false;
            bt_file01.Visible = false;
            bt_file02.Visible = false;
            bt_file03.Visible = false;
            bt_file04.Visible = false;
            bt_file05.Visible = false;
            bt_file06.Visible = false;
            bt_file07.Visible = false;
            bt_file08.Visible = false;
            bt_file09.Visible = false;
            bt_dir00.Visible = false;
            bt_dir01.Visible = false;
            bt_dir02.Visible = false;
            bt_dir03.Visible = false;
            bt_dir04.Visible = false;
            bt_dir05.Visible = false;
            bt_dir06.Visible = false;
            bt_dir07.Visible = false;
            bt_dir08.Visible = false;
            bt_dir09.Visible = false;
            bt_files00.Visible = false;
            bt_files01.Visible = false;
            bt_files02.Visible = false;
            bt_files03.Visible = false;
            bt_files04.Visible = false;
            bt_files05.Visible = false;
            bt_files06.Visible = false;
            bt_files07.Visible = false;
            bt_files08.Visible = false;
            bt_files09.Visible = false;

            int W = 1500;
            groupBox1.Size = new Size(W, 106 + 50);
            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 16);

            listView1.Size = new Size(W, 270 - 50);
            listView1.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 24 + 50);
            bt_clear2.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear2.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear2.Size.Height);

            richTextBox1.Size = new Size(W, 410);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 5 + 24);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            show_item_location_common();
        }

        void show_item_location_common()
        {
            int x_st = 3;
            int y_st = 10;
            int dx = 45 + 3;
            int dy = 45 + 3;
            bt_export_doc.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_export_video.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_open_dir1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_open_dir2.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            tb_foldername1.Size = new Size(520, 100);
            tb_foldername1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 5);
            tb_foldername2.Size = new Size(520, 100);
            tb_foldername2.Location = new Point(x_st + dx * 2, y_st + dy * 1 + 5);

            bt_delete_file.Location = new Point(x_st + dx * 13, y_st + dy * 0);
            bt_setup.Location = new Point(x_st + dx * 14, y_st + dy * 0);
            bt_start_files.Location = new Point(x_st + dx * 15, y_st + dy * 0);
            bt_start_all_files.Location = new Point(x_st + dx * 16, y_st + dy * 0);
            bt_compare.Location = new Point(x_st + dx * 17, y_st + dy * 0);
            bt_test1.Location = new Point(x_st + dx * 13, y_st + dy * 2);
            bt_test2.Location = new Point(x_st + dx * 14, y_st + dy * 2);
            bt_test3.Location = new Point(x_st + dx * 15, y_st + dy * 2);
            bt_test4.Location = new Point(x_st + dx * 16, y_st + dy * 2);

            int yy = 7;
            cb_search.Location = new Point(x_st + dx * 13, y_st + dy * 1 + yy);
            cb_search.Text = "搜尋\n檔名";
            tb_search.Size = new Size(150 - 16, 100);
            tb_search.Location = new Point(x_st + dx * 14, y_st + dy * 1 + 5 + yy);
            cb_size.Location = new Point(x_st + dx * 17, y_st + dy * 1 + yy);
            cb_size.Text = "最小\nMB";
            tb_size.Size = new Size(50, 100);
            tb_size.Location = new Point(x_st + dx * 18, y_st + dy * 1 + 5 + yy);

            cb_search_big_files.Location = new Point(x_st + dx * 19 + 10, y_st + dy * 1 + yy);
            cb_search_small_files.Location = new Point(x_st + dx * 19 + 10 + 50, y_st + dy * 1 + yy);

            cb_search_big_files.Text = "搜尋\n大檔";
            cb_search_small_files.Text = "搜尋\n小檔";
            //cb_size.Text = "最小\nMB";

            //搜尋小檔 搜尋小檔

            lb_search_result1.Location = new Point(x_st + dx * 18, y_st + dy * 0);
            lb_search_result2.Location = new Point(x_st + dx * 18, y_st + dy * 0 + 26);
            lb_search_result1.Text = "";
            lb_search_result2.Text = "";

            int dd = 980;
            tb_foldername.Size = new Size(200, 100);
            tb_foldername.Location = new Point(x_st + 47 + dd, y_st + 5);
            tb_filename.Size = new Size(200, 100);
            tb_filename.Location = new Point(x_st + 47 + dd, y_st + 50);

            //針對某控件的邊緣 設定表單大小
            this.ClientSize = new Size(richTextBox1.Right + 10, richTextBox1.Bottom + 10);

            this.Text = "vcs_DiskDirectoryFile1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            fileinfos.Clear();
            lb_search_result1.Text = "";
        }

        //------------------------------------------------------------  # 60個

        void show_filenames(FileInfo[] fis)
        {
            int len = fis.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 個檔案\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += fis[i].Name + "\n";
            }
        }

        void show_filenames(string[] filenames)
        {
            int len = filenames.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 個檔案\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void DeleteDirectory(string foldername)
        {
            // 找資料夾, 一層
            string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
            Array.Sort(dirs);  // 排序
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "刪除子目錄 : " + dir + "\n";
                DeleteDirectory(dir);
            }

            // 找檔案, 一層
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            foreach (string filename in filenames)
            {
                richTextBox1.Text += "刪除檔案 : " + filename + "\n";
                File.SetAttributes(filename, FileAttributes.Normal);
                File.Delete(filename);  // 刪除檔案
            }
            Directory.Delete(foldername, false);  // 非遞迴
        }

        //刪除資料夾，recursive為True時，直接刪除資料夾及其資料夾下所有文件或資料夾;recursive為False時，需先將資料夾下所有文件或資料夾刪除
        private void DeleteDirectory(string foldername, bool recursive)
        {
            if (recursive)
            {
                Directory.Delete(foldername, true);  // 遞迴
                richTextBox1.Text += "已刪除資料夾: " + foldername + "\n";
            }
            else
            {
                richTextBox1.Text += "需要先把資料夾內的檔案刪除\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file00_Click(object sender, EventArgs e)
        {
            /*
            //File 的方法
            File.Exists()
            File.Create()
            File.Copy()  // 檔案拷貝
            File.Move()  // 檔案重新命名
            File.Delete()  // 刪除檔案
            File.Open()
            File.OpenRead()
            File.ReadAllText()  // 將檔案讀取為字串
            File.WriteAllText()
            File.AppendAllText()
            //取得檔案時間
            File.GetCreationTime()	檔案建立時間
            File.GetLastWriteTime()	檔案最後修改時間 或 資料夾最後修改時間
            File.GetLastAccessTime()檔案最後存取時間
            //設定檔案時間
            File.SetCreationTime()
            File.SetLastWriteTime()
            File.SetLastAccessTime()

            File.GetAttributes()  取得檔案屬性
            File.SetAttributes()  設定檔案屬性
            */

            //檢查檔案 新建檔案 複製檔案

            richTextBox1.Text += "檔案1 拷貝 到 檔案2\n";

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";

            if (File.Exists(filename1) == true)  // 確認檔案1是否存在
            {
                richTextBox1.Text += "檔案1存在, 準備複製\n";
                if (File.Exists(filename2) == false)  // 確認檔案2是否存在
                {
                    File.Copy(filename1, filename2);  // 檔案拷貝
                    richTextBox1.Text += "已複製檔案, 檔案1 拷貝 到 檔案2\n";
                }
                else
                {
                    richTextBox1.Text += "檔案2已存在，無法複製\n";

                    string filename3 = @"D:\_git\vcs\_1.data\______test_files1\picture1ccc.jpg";
                    //移動檔案，從 filename2 移動到 filename3
                    if (File.Exists(filename3) == false)  // 確認檔案3是否存在
                    {
                        File.Move(filename2, filename3);  // 檔案重新命名
                        richTextBox1.Text += "已移動檔案: " + filename2 + " 到 " + filename3 + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "檔案: " + filename3 + " 已存在，無法移動\n";

                        File.Delete(filename3);  // 刪除檔案
                        richTextBox1.Text += "檔案3已存在, 已刪除\n";
                    }
                }
            }
            else
            {
                richTextBox1.Text += "檔案1不存在，無法複製\n";

                // 偽執行 File.Create(filename1);
                richTextBox1.Text += "檔案1不存在, 已建立\n";
            }

            //------------------------------------------------------------  # 60個

            //建立檔案
            string filename4 = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";
            FileStream fs = File.Create(filename4);
            fs.Close();
            richTextBox1.Text += "已建立檔案: " + filename4 + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "各種 Directory/File 操作\n";

            string filename1b = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";
            string filename2b = @"D:\_git\vcs\_1.data\______test_files1\tmp_article.txt";
            string filename3b = @"D:\_git\vcs\_1.data\______test_files1\tmp_article_new.txt";

            if (File.Exists(filename1b) == false)
            {
                richTextBox1.Text += "檔案不存在, 建立之。\n";
            }

            if (File.Exists(filename2b) == false)
            {
                richTextBox1.Text += "檔案 : " + filename2b + ", 不存在, 建立之\n";
                File.Copy(filename1b, filename2b);  // 檔案拷貝
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "將檔案 : " + filename2b + ", 改檔名成 : " + filename3b + "\n";
            File.Move(filename2b, filename3b);  // 檔案重新命名

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            if (File.Exists(filename3b) == true)
            {
                richTextBox1.Text += "檔案 : " + filename3b + ", 已存在, 刪除之\n";
                richTextBox1.Text += "直接刪除, 不放進垃圾桶\n";
                File.Delete(filename3b);  // 刪除檔案
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //複製檔案
            string new_filename = "aaaaa.cs";
            if (File.Exists(new_filename) == true)
            {
                richTextBox1.Text += "檔案已存在, 無法複製檔案\n";
            }
            else
            {
                File.Copy(@"../../Form1.cs", new_filename);  // 檔案拷貝
                richTextBox1.Text += "複製檔案完成\n";
            }

            //------------------------------------------------------------  # 60個

            //檔案已存在的FileCopy/Move

            string filename_source = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            string filename_destination = @"D:\_git\vcs\_1.data\______test_files1\_cpfile\ccc.jpg";   //要寫完整檔名

            richTextBox1.Text += "檔案已存在的FileCopy/Move\n";
            try
            {
                //File.Copy(filename_source, filename_destination);  // 檔案拷貝     //若檔案已存在, 會出現IOException
                //File.Move(filename_source, filename_destination);  // 檔案重新命名     //若檔案已存在, 會出現IOException
                File.Copy(filename_source, filename_destination, true); //檔案拷貝, true : 覆蓋檔案
                //File.Move(filename_source, filename_destination, true);  // 檔案重新命名 //true : 覆蓋檔案
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息m : " + ex.Message + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file01_Click(object sender, EventArgs e)
        {
            //FileInfo 的方法

            //取得檔案資訊 FileInfo

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            get_FileInfo(filename);
        }

        //------------------------------------------------------------  # 60個

        private void bt_file02_Click(object sender, EventArgs e)
        {
            //File 屬性相關

            // 屬性相關 GetAttributes SetAttributes

            // 刪除檔案前，先設定檔案屬性為[正常的]
            // File.SetAttributes(filename, FileAttributes.Normal);

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            FileInfo fi = new FileInfo(filename);
            FileAttributes attr = fi.Attributes;

            if ((attr & FileAttributes.ReadOnly) > 0)
            {
                richTextBox1.Text += "唯讀檔案\n";
            }
            else
            {
                richTextBox1.Text += "一般檔案\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            /*
            FileAttributes attr = (new FileInfo(filename)).Attributes;
            Console.Write("UnAuthorizedAccessException: Unable to access file. ");
            if ((attr & FileAttributes.ReadOnly) > 0)
                Console.Write("The file is read-only.");
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //設定檔案屬性
            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_貓咪\cat1.png";

            fi = new FileInfo(filename);
            fi.Attributes = FileAttributes.ReadOnly;  // 唯讀
            fi.Attributes = FileAttributes.System;  // 系統
            fi.Attributes = FileAttributes.Archive;  // 存檔
            fi.Attributes = FileAttributes.Hidden;  // 隱藏

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "檔案屬性 : " + File.GetAttributes(filename).ToString() + "\n";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            //File.SetAttributes(filename, FileAttributes.Hidden);//隱藏
            richTextBox1.Text += File.GetAttributes(filename) + "\n";

            if ((File.GetAttributes(filename) & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
            {
                richTextBox1.Text += "檔案唯讀，不能修改檔案時間\n";
            }
            else
            {
                richTextBox1.Text += "修改檔案時間\n";
                File.SetAttributes(filename, FileAttributes.Archive);
                File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden);
                File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden | FileAttributes.ReadOnly);
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file03_Click(object sender, EventArgs e)
        {
            /*
            //File的檔案操作方法
            File.Create()
            File.Copy()  // 檔案拷貝
            File.Move()  // 檔案重新命名
            File.Delete()  // 刪除檔案
            */

            //根據時間建立文件
            //File.Create("D:\\______test_files\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//建立文件

            //建立臨時檔案
            //File.Create("tmp_" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件

            //刪除檔案 (不使用資源回收筒)
            string filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            FileInfo fi = new FileInfo(filename);
            if (fi.Exists == true)  // 確認檔案是否存在
            {
                fi.Delete();  // 刪除檔案
                richTextBox1.Text += "檔案刪除成功\n";
            }
            else
            {
                richTextBox1.Text += "找不到檔案\n";
            }

            //------------------------------------------------------------  # 60個

            //刪除檔案 (使用資源回收筒)

            //先將Microsoft.VisualBasic.Dll加入參考。
            //參考/加入參考/.NET/Microsoft.VisualBasic
            //加上 using Microsoft.VisualBasic.FileIO;    //引用Microsoft.VisualBasic.FileIO命名空間。

            string delete_filename = @"C:\Users\070601\Desktop\zzzzzzz.jpg";

            if (File.Exists(delete_filename) == true)
            {
                FileSystem.DeleteFile(delete_filename, UIOption.OnlyErrorDialogs, RecycleOption.SendToRecycleBin);
                richTextBox1.Text += "已將檔案 : " + delete_filename + " 移至資源回收筒\n";
            }
            else
            {
                richTextBox1.Text += "檔案 : " + delete_filename + " 不存在\n";
            }
        }

        //------------------------------------------------------------  # 60個

        void show_file_info(string filename)
        {
            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案建立時間 : " + File.GetCreationTime(filename) + "\n";
            richTextBox1.Text += "檔案最後修改時間 : " + File.GetLastWriteTime(filename) + "\n";
            richTextBox1.Text += "檔案最後存取時間 : " + File.GetLastAccessTime(filename) + "\n";
            richTextBox1.Text += "檔案屬性 : " + File.GetAttributes(filename).ToString() + "\n";
        }

        private void bt_file04_Click(object sender, EventArgs e)
        {
            //File的 Get / Set 方法

            // File.Get

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";

            filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";

            show_file_info(filename);

            richTextBox1.Text += "\n改變檔案時間 與 檔案屬性\n\n";

            File.SetCreationTime(filename, new DateTime(1985, 5, 4));
            File.SetLastWriteTime(filename, new DateTime(1995, 6, 5));
            File.SetLastAccessTime(filename, new DateTime(2005, 7, 6));
            //File.SetLastAccessTime(filename, DateTime.Now);  // touch
            //File.SetLastWriteTime(filename, DateTime.Now);  // touch

            show_file_info(filename);

            //------------------------------------------------------------  # 60個

            //讀取設定檔案時間
            filename = @"D:\_git\vcs\_1.data\______test_files1\mega.txt";

            show_file_info(filename);

            //一段時間以後的寫法
            DateTime dt_new1 = File.GetCreationTime(filename) + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            DateTime dt_new2 = File.GetLastWriteTime(filename) + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            DateTime dt_new3 = File.GetLastAccessTime(filename) + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒

            File.SetCreationTime(filename, dt_new1);
            File.SetLastWriteTime(filename, dt_new2);
            File.SetLastAccessTime(filename, dt_new3);
            richTextBox1.Text += "檔案: " + filename + "\t設定讀寫時間\n";
            richTextBox1.Text += "SetCreationTime\t" + dt_new1 + "\n";
            richTextBox1.Text += "SetLastWriteTime\t" + dt_new2 + "\n";
            richTextBox1.Text += "SetLastAccessTime\t" + dt_new3 + "\n";

            //------------------------------------------------------------  # 60個

            filename = @"D:\_git\vcs\_1.data\______test_files1\mega.txt";
            show_file_info(filename);
        }

        //------------------------------------------------------------  # 60個

        private void bt_file05_Click(object sender, EventArgs e)
        {
            //建立刪除檔案資料夾

            //建立一個新資料夾
            string new_foldername = @"D:/_git/vcs/_1.data/______test_files_file_name2/aaaa/bbbb";

            if (Directory.Exists(new_foldername) == false)  // 確認資料夾是否存在
            {
                // 新增資料夾
                Directory.CreateDirectory(new_foldername);  // 新增資料夾
                richTextBox1.Text += "新增資料夾 : " + new_foldername + "\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + new_foldername + " 已存在, 無法重新建立\n";
            }

            //------------------------------------------------------------  # 60個

            //刪除資料夾
            string delete_foldername = @"D:/_git/vcs/_1.data/______test_files_file_name2";

            /*
            // 僅能刪除空資料夾, 沒有 true/false
            if (Directory.Exists(delete_foldername) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + delete_foldername + " 不存在，不能刪除\n";
            }
            else
            {
                Directory.Delete(delete_foldername);  // 僅能刪除空資料夾
                richTextBox1.Text += "已刪除資料夾: " + delete_foldername + "\n";
            }
            */

            /*
            if (Directory.Exists(delete_foldername) == true)  // 確認資料夾是否存在
            {
                try
                {
                    //若有多層要用 true
                    Directory.Delete(delete_foldername, true);  // 遞迴
                    //Directory.Delete(delete_foldername, false);  // 非遞迴
                    richTextBox1.Text += "已刪除資料夾" + delete_foldername + "\n";
                }
                catch
                {
                    richTextBox1.Text += "無法刪除資料夾" + delete_foldername + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + delete_foldername + " 不存在，不能刪除\n";
            }
            */

            //------------------------------------------------------------  # 60個

            //刪除資料夾, 多層一一刪除檔案再刪除資料夾
            delete_foldername = @"D:/_git/vcs/_1.data/______test_files_file_name2";

            if (Directory.Exists(delete_foldername) == true)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "刪除資料夾: " + delete_foldername + "\n";
                try
                {
                    DeleteDirectory(delete_foldername);
                    //Directory.Delete(delete_foldername, true);   //recurrsive
                    //Directory.Delete(delete_foldername, false);   //not recurrsive
                    richTextBox1.Text += "OK\n";
                }
                catch
                {
                    richTextBox1.Text += "FAIL\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + delete_foldername + " 不存在，不能刪除\n";
            }


            return;

            //Directory.Delete 刪除資料夾

            string destDirName1 = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName2 = @"D:\_git\vcs\_1.data\______test_files1\folder22";
            DeleteDirectory(destDirName1, true);
            DeleteDirectory(destDirName2, true);

            //------------------------------------------------------------  # 60個

            //Directory.Delete 目錄不是空的

            delete_foldername = @"D:\_git\vcs\_1.data\______test_files1\_cpfile";

            richTextBox1.Text += "Directory.Delete 目錄不是空的\n";
            try
            {
                //Directory.Delete(delete_foldername); //若目錄不是空的, 會出現IOException
                Directory.Delete(delete_foldername, true);  // 遞迴, 強制刪除不是空的目錄
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息m : " + ex.Message + "\n";
            }

            //------------------------------------------------------------  # 60個

            //刪除資料夾下子資料夾(偽)

            delete_foldername = @"D:/_git/vcs/_1.data/______test_files1";
            DateTime dt = DateTime.Now;

            DirectoryInfo dinfo = new DirectoryInfo(delete_foldername);

            // 找資料夾, 一層
            DirectoryInfo[] dis = dinfo.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dis)
            {
                //建立時間
                if (di.CreationTime < Convert.ToDateTime(dt.AddDays(-(dt.Day) + 1)))
                {
                    //di.Delete();
                    richTextBox1.Text += "path = " + di + "\n";
                }
            }

            /*
            //File.Create()

            // 偽執行 File.Create(filename1);
            richTextBox1.Text += "檔案1不存在, 已建立\n";

            */

            //根據時間建立文件
            //File.Create("D:\\______test_files\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//建立文件

            //建立臨時檔案
            //File.Create("tmp_" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件

            //新增檔案
            string filename = "tmp_new_file.txt";
            if (File.Exists(filename) == true)
            {
                richTextBox1.Text += "檔案已存在, 無法重新建立\n";
            }
            else
            {
                StreamWriter sw = File.CreateText(filename);
                richTextBox1.Text += "新增檔案 完成\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file06_Click(object sender, EventArgs e)
        {
            // 搜尋檔案-檔名
            richTextBox1.Text += "搜尋檔案, 只找一層 IMG_20180228_215525.jpg\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon";
            DirectoryInfo di = new DirectoryInfo(foldername);

            // 搜尋完整檔名
            foreach (FileInfo fi in di.GetFiles("IMG_20180228_215525.jpg"))
            {
                richTextBox1.Text += "1找到 : " + fi.Name + "\n";
            }

            // 搜尋部分檔名
            foreach (FileInfo fi in di.GetFiles("IMG_20180228*"))
            {
                richTextBox1.Text += "2找到 : " + fi.Name + "\n";
            }

            // 搜尋一個資料夾內所有特定格式的檔案
            // 搜尋副檔名 *.jpg *.txt *.*
            foreach (FileInfo fi in di.GetFiles("*.gif"))
            {
                richTextBox1.Text += "3找到 : " + fi.Name + "\n";
            }

            //選出所有符合一定後綴的文件列表
            System.IO.SearchOption search_option = System.IO.SearchOption.AllDirectories;  // 在搜尋作業中包含目前目錄和所有子目錄
            FileInfo[] fis = di.GetFiles("*.*", search_option);
            foreach (FileInfo fi in fis)
            {
                //richTextBox1.Text += "4找到 : " + fi.Name + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file07_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        // 此方法所接收的兩個字串代表您所要比較的兩個檔案。
        // 如果兩個檔案的內容完全相同，將傳回 True；任何其他
        // 的傳回值都表示這兩個檔案的內容有所差異。
        private bool FileCompare(string file1, string file2)
        {
            // 判斷相同的檔案是否被參考兩次。
            if (file1 == file2)
            {
                return true;
            }

            int file1byte = 0;
            int file2byte = 0;
            using (FileStream fs1 = new FileStream(file1, FileMode.Open), fs2 = new FileStream(file2, FileMode.Open))
            {
                // 檢查檔案大小。如果兩個檔案的大小並不相同，則視為不相同。
                if (fs1.Length != fs2.Length)
                {
                    return false;
                }

                // 逐一比較兩個檔案的每一個位元組，直到發現不相符或已到達檔案尾端為止。

                do
                {
                    // 從每一個檔案讀取一個位元組。
                    file1byte = fs1.ReadByte();  // 讀一拜
                    file2byte = fs2.ReadByte();  // 讀一拜
                }
                while ((file1byte == file2byte) && (file1byte != -1));
            }

            // 傳回比較的結果。在這個時候，只有當兩個檔案
            // 的內容完全相同時，"file1byte" 才會等於 "file2byte"。
            return ((file1byte - file2byte) == 0);
        }

        private void bt_file08_Click(object sender, EventArgs e)
        {
            //比較兩個檔案
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\compare\ssss.txt";

            if (FileCompare(filename1, filename2) == true)
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename2 + " 相同。\n";
            }
            else
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename2 + " 不同。\n";
            }

            if (FileCompare(filename1, filename3) == true)
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename3 + " 相同。\n";
            }
            else
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename3 + " 不同。\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file09_Click(object sender, EventArgs e)
        {
            //用 FileInfo 的方法 讀寫檔案

            //新增檔案, 指定路徑建立檔案
            string filename = @"_tmp_aaaa.txt";
            FileInfo fi = new FileInfo(filename);

            FileStream fs = fi.Create();  // 用Create方法新增一個檔案
            fs.Close();//關閉檔案

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            filename = @"_tmp_bbbb.txt";
            fi = new FileInfo(filename);

            string text;
            StreamReader sr;
            StreamWriter sw;

            //1.寫入
            sw = fi.CreateText();  //開啟新檔
            text = "寫入AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
            //將輸入的資料覆蓋原檔並重新寫入
            sw.WriteLine(text);
            sw.Flush();
            sw.Close();

            //2.附加 
            sw = fi.AppendText();   //開啟舊檔
            text = "附加AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
            //將輸入的資料附加到資料檔的最後
            sw.WriteLine(text);
            sw.Flush();
            sw.Close();

            //以唯讀模式開檔
            sr = fi.OpenText();  //以唯讀模式開檔
            Console.WriteLine("資料檔內容如下：");
            Console.WriteLine(sr.ReadToEnd());//讀出資料
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //複製檔案
            filename = @"_tmp_cccc.txt";
            //目的檔案「Text.txttmp」
            String tagPath = filename + "tmp";
            fi = new FileInfo(filename);

            //以CopyTo方法複製檔案
            //fi.CopyTo(tagPath);  NG
            richTextBox1.Text += filename + " 已複製\n";

            filename = @"_tmp_dddd.txt";
            fi = new FileInfo(filename);
            //fi.Rename("test2.txt");
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir00_Click(object sender, EventArgs e)
        {
            //Directory 的方法
            /*            
            Directory.Exists()  // 確認資料夾是否存在
            Directory.CreateDirectory()  // 新增資料夾
            Directory.Move()
            Directory.Delete()
            Directory.GetParent()  // 由資料夾取得上層資料夾
            Directory.GetDirectories()  // 取得指定目錄中子目錄的名稱
            Directory.GetFiles()  // 取得指定目錄中檔案的名稱
            Directory.GetCurrentDirectory()  // 目前所在路徑, 目前工作目錄
            Directory.SetCurrentDirectory()  // 設定工作目錄
            Directory.GetLastWriteTime()  // 資料夾最後修改時間
            Directory.SetLastWriteTime()
            */

            //取得目前工作目錄

            richTextBox1.Text += "目前工作目錄 : " + Environment.CurrentDirectory + "\n";

            string currentPath = Directory.GetCurrentDirectory();  // 目前工作目錄
            richTextBox1.Text += "目前工作目錄 : " + currentPath + "\n";

            //Directory.SetCurrentDirectory("D:\\");  // 設定工作目錄


            string foldername = @"D:\_git\vcs\_1.data\______test_files3";

            richTextBox1.Text += "資料夾 : " + foldername + "\n";
            richTextBox1.Text += "上層資料夾 : " + Directory.GetParent(foldername) + "\n";

            //------------------------------------------------------------  # 60個

            if (Directory.Exists(foldername) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + foldername + " 不存在\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + foldername + " 存在\n";
            }

            //------------------------------------------------------------  # 60個

            //未完成
            string foldername_old = @"D:/_git/vcs/_1.data/______test_files_file_name1";
            string foldername_new = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            if (Directory.Exists(foldername_old) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "原始資料夾: " + foldername_old + " 不存在, 不能拷貝\n";
                return;
            }

            if (Directory.Exists(foldername_new) == false)  // 確認資料夾是否存在
            {
                //複製
            }
            else
            {
                richTextBox1.Text += "目的資料夾: " + foldername_new + " 已存在, 不能拷貝\n";
                return;
            }

            //------------------------------------------------------------  # 60個

            string Foldername_old = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            string Foldername_new = @"D:/_git/vcs/_1.data/______test_files_file_name3";
            if (Directory.Exists(Foldername_old) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "原始資料夾: " + Foldername_old + " 不存在, 不能拷貝\n";
                return;
            }

            if (Directory.Exists(Foldername_new) == true)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "目的資料夾: " + Foldername_new + " 已存在, 不能拷貝\n";
                return;
            }

            Directory.Move(Foldername_old, Foldername_new);  // 資料夾改名
            richTextBox1.Text += "移動/更名 完成，從原始資料夾: " + Foldername_old + " 到目的資料夾: " + Foldername_new + "\n";

            //移動資料夾，從 sourceDirName 移動到 destDirName
            string sourceDirName = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName = @"D:\_git\vcs\_1.data\______test_files1\folder22";

            if (Directory.Exists(sourceDirName) == true)  // 確認資料夾是否存在
            {
                if (Directory.Exists(destDirName) == false)  // 確認資料夾是否存在
                {
                    Directory.Move(sourceDirName, destDirName);  // 資料夾改名
                    richTextBox1.Text += "已移動資料夾: " + sourceDirName + " 到 " + destDirName + "\n";
                }
                else
                {
                    richTextBox1.Text += "資料夾: " + destDirName + " 已存在\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + sourceDirName + " 不存在\n";
            }
        }

        private void bt_dir01_Click(object sender, EventArgs e)
        {
            //DirectoryInfo 的方法

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare";
            get_DirectoryInfo(foldername);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得磁碟檔案資料
            // 由檔案取得檔案所在磁碟
            DriveInfo drive_info = new DriveInfo(@"D:\_git\vcs\_1.data\______test_files1");
            richTextBox1.Text += "由檔案取得檔案所在磁碟 : " + drive_info.RootDirectory + "\n";

            // Get the root directory and print out some information about it.
            DirectoryInfo dinfo9 = drive_info.RootDirectory;
            richTextBox1.Text += "根目錄 : " + dinfo9.Attributes.ToString() + "\n";

            // 找資料夾, 一層
            DirectoryInfo[] dis = dinfo9.GetDirectories("*.*");  // 由DI取得DI陣列, 一層資料夾資訊

            foreach (DirectoryInfo di in dis)
            {
                get_DirectoryInfo(di);
            }

            //------------------------------------------------------------  # 60個

            //遍歷文件夾實例 1

            //獲取指定目錄下的所有子目錄及文件類型

            //還沒加入listView之標題

            listView1.Items.Clear();

            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            DirectoryInfo dinfo = new DirectoryInfo(foldername);

            FileSystemInfo[] fsinfos = dinfo.GetFileSystemInfos();  // 獲取所有的文件
            foreach (FileSystemInfo fsinfo in fsinfos)  // 遍歷獲取到的文件
            {
                if (fsinfo is DirectoryInfo)    //判斷是否文件夾
                {
                    //使用獲取的文件夾名稱實例化DirectoryInfo對象
                    DirectoryInfo dirinfo = new DirectoryInfo(fsinfo.FullName);
                    //為ListView控件添加文件夾信息
                    listView1.Items.Add(dirinfo.Name);
                    listView1.Items[listView1.Items.Count - 1].SubItems.Add(dirinfo.FullName);
                    listView1.Items[listView1.Items.Count - 1].SubItems.Add("");
                    listView1.Items[listView1.Items.Count - 1].SubItems.Add(dirinfo.CreationTime.ToShortDateString());
                    richTextBox1.Text += dirinfo.Name + "\t" + dirinfo.FullName + "\t" + dirinfo.CreationTime.ToShortDateString() + "\n";
                }
                else
                {
                    //使用獲取的文件名稱實例化FileInfo對象
                    FileInfo finfo = new FileInfo(fsinfo.FullName);
                    //為ListView控件添加文件信息
                    listView1.Items.Add(finfo.Name);
                    listView1.Items[listView1.Items.Count - 1].SubItems.Add(finfo.FullName);
                    listView1.Items[listView1.Items.Count - 1].SubItems.Add(finfo.Length.ToString());
                    listView1.Items[listView1.Items.Count - 1].SubItems.Add(finfo.CreationTime.ToShortDateString());
                    richTextBox1.Text += finfo.Name + "\t" + finfo.FullName + "\t" + finfo.Length.ToString() + "\t" + finfo.CreationTime.ToShortDateString() + "\n";
                }
            }

            //------------------------------------------------------------  # 60個

            //使用递归法删除文件夹中的所有文件
            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare";

            DirectoryInfo dinfo2 = new DirectoryInfo(foldername);//创建DirectoryInfo对象
            //FileSystemInfo[]
            fsinfos = dinfo2.GetFileSystemInfos();  // 獲取所有的文件
            for (int i = 0; i < fsinfos.Length; i++)//遍歷獲取到的文件
            {
                FileInfo finfo = new FileInfo(foldername + "\\" + fsinfos[i].ToString());//创建FileInfo对象
                //finfo.Delete();  // 刪除檔案
                richTextBox1.Text += "偽刪除 " + foldername + "\\" + fsinfos[i].ToString() + "\n";
            }
            richTextBox1.Text += "删除成功\n";

            //------------------------------------------------------------  # 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare";

            // 建立DirectoryInfo類別的dinfo3物件，可用來操作資料夾目錄
            DirectoryInfo dinfo3 = new DirectoryInfo(foldername);
            if (dinfo3.Exists)
            {	// 判斷目錄是否存在
                richTextBox1.Text += foldername + ", 路徑存在, 不建立目錄\n";
            }
            else
            {
                richTextBox1.Text += foldername + ", 路徑不存在，建立目錄\n";
                dinfo3.Create();	// 建立目錄
                dinfo3.Refresh();	// 重新整理目錄
            }

            //刪除 資料夾
            try
            {
                dinfo3.Delete();	       // 刪除檔案
                richTextBox1.Text += "刪除成功" + "\n";
            }
            catch (Exception ex)   // 刪除檔案失敗會產生例外
            {
                richTextBox1.Text += "刪除失敗" + "\n";
                richTextBox1.Text += ex.Message + "\n";  // 顯示例外訊息
            }
            richTextBox1.Text += "------------------------------\n";  // 30個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare";

            DirectoryInfo dinfo4 = new DirectoryInfo(foldername);
            richTextBox1.Text += dinfo4.FullName + ", 資料夾下的子資料夾如下 :\n";

            // 找資料夾, 一層
            //DirectoryInfo[]
            dis = dinfo4.GetDirectories();  // 傳回目前目錄的子目錄, 一層

            richTextBox1.Text += "子目錄 :\n";
            foreach (DirectoryInfo di in dis)
            {
                get_DirectoryInfo(di);
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir02_Click(object sender, EventArgs e)
        {
            // Directory.GetFiles()  // 取得指定目錄中檔案的名稱, 撈出資料夾內的檔案(一層)

            string foldername = @"D:\_git\vcs\_1.data\______test_files3";

            // 找檔案, 一層, 全部
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            // 找檔案, 一層, 指名jpg檔
            filenames = Directory.GetFiles(foldername, "*.jpg");  // 取得指定目錄中檔案的名稱, 指定副檔名
            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "撈出資料夾內特定類型的檔案\t一層/多層\n";
            //SearchOption
            //  TopDirectoryOnly = 0,
            //      只在搜尋中包含目前目錄。
            //  AllDirectories = 1,
            //      在搜尋作業中包含目前目錄和所有子目錄。
            //      這個選項會在搜尋中包含重新剖析點 (例如掛接磁碟和符號連結)。

            // 一層
            System.IO.SearchOption search_option = System.IO.SearchOption.TopDirectoryOnly;  // 只在搜尋中包含目前目錄

            // 多層
            search_option = System.IO.SearchOption.AllDirectories;  // 在搜尋作業中包含目前目錄和所有子目錄

            // 找檔案, 一層/多層
            filenames = Directory.GetFiles(foldername, "*.*", search_option);
            show_filenames(filenames);
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir03_Click(object sender, EventArgs e)
        {
            //資料夾最後修改時間

            string foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\";

            //取得資料夾最後一次被存取的時間
            DateTime dt = Directory.GetLastWriteTime(foldername);  // 資料夾最後修改時間
            richTextBox1.Text += "資料夾建立的時間 : " + dt + "\n";

            richTextBox1.Text += "更新資料夾最後修改時間\n";

            //更新時間, touch
            Directory.SetLastWriteTime(foldername, DateTime.Now);  // touch
            dt = Directory.GetLastWriteTime(foldername);  // 資料夾最後修改時間
            richTextBox1.Text += "最後存取時間 : " + dt + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir04_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir05_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir06_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir07_Click(object sender, EventArgs e)
        {
            //MediaInfo
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_video\鹿港.mp4";
            get_MediaInfo(filename);

            //MediaInfo
            filename = @"D:\_git\vcs\_1.data\______test_files1\_mp3\02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
            get_MediaInfo(filename);
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir08_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void bt_dir09_Click(object sender, EventArgs e)
        {
            //轉出
            string foldername = @"D:\_git\vcs\_1.data\______test_files3";

            richTextBox1.Text += "方法1, 以此為準\n";
            text = string.Empty;
            ProcessFile_mode = PROCESS_FILE_MODE0;  // 0:預設只匯出檔名
            ProcessDirectory(foldername);
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "方法2\n";
            ProcessDirectoryInfo(foldername);

            return;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            richTextBox1.Text += "所有檔案\n";
            string[] filenames1 = Directory.GetFileSystemEntries(foldername);
            show_filenames(filenames1);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "限定檔案 *.txt\n";
            string[] filenames2 = Directory.GetFileSystemEntries(foldername, "*.txt");
            show_filenames(filenames2);
        }

        void show_file_info6(int sort_item, bool sort_type)
        {
            //sort_type  // false : ASCENDING, true : DESCENDING

            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            listView1.Items.Clear();

            if (sort_item == -1)
            {
                richTextBox1.Text += "無排序\n";
            }
            else if (sort_item == 0)
            {
                richTextBox1.Text += "依檔名排序, ";

                if (sort_type == false)
                {
                    richTextBox1.Text += "升冪\n";
                    //排序 由小到大, 升冪
                    fileinfos.Sort((x, y) => { return x.filename.CompareTo(y.filename); });
                }
                else
                {
                    richTextBox1.Text += "降冪\n";
                    //排序 由大到小, 降冪, 在return的地方多個負號
                    fileinfos.Sort((x, y) => { return -x.filename.CompareTo(y.filename); });
                }
            }
            else if (sort_item == 1)
            {
                richTextBox1.Text += "依檔案大小排序, ";

                if (sort_type == false)
                {
                    richTextBox1.Text += "升冪\n";
                    //排序 由小到大, 升冪
                    fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });
                }
                else
                {
                    richTextBox1.Text += "降冪\n";
                    //排序 由大到小, 降冪, 在return的地方多個負號
                    fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
                }
            }
            else if (sort_item == 2)
            {
                richTextBox1.Text += "依格式排序, ";

                if (sort_type == false)
                {
                    richTextBox1.Text += "升冪\n";
                    //排序 由小到大, 升冪
                    fileinfos.Sort((x, y) => { return x.video_height.CompareTo(y.video_height); });
                }
                else
                {
                    richTextBox1.Text += "降冪\n";
                    //排序 由大到小, 降冪, 在return的地方多個負號
                    fileinfos.Sort((x, y) => { return -x.video_height.CompareTo(y.video_height); });
                }
            }
            else
            {
                richTextBox1.Text += "其他排序XXXX\n";
                return;
            }

            int len = fileinfos.Count;
            for (int i = 0; i < len; i++)
            {
                string filename = fileinfos[i].filename;
                string foldername = fileinfos[i].filepath;
                //string ext = "AAAA";
                long file_size = fileinfos[i].filesize;
                int w = fileinfos[i].video_width;
                int h = fileinfos[i].video_height;
                int f = fileinfos[i].video_fps;
                int d = fileinfos[i].video_duration;

                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                i1.UseItemStyleForSubItems = false;
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();

                sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                i1.SubItems.Add(sub_i1a);

                sub_i1a.ForeColor = Color.Blue;
                sub_i1a.Font = new Font("Times New Roman", 10, FontStyle.Bold);

                string text = w.ToString() + "×" + h.ToString();

                sub_i1b.Text = text;
                i1.SubItems.Add(sub_i1b);

                sub_i1c.Text = fileinfos[i].filepath;
                i1.SubItems.Add(sub_i1c);

                listView1.Items.Add(i1);
            }

            if (listView1.Items.Count > 0)
            {
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_files00_Click(object sender, EventArgs e)
        {
            //Path的方法

            /*            
            Path.GetFullPath()完整路徑檔名
            Path.GetDirectoryName()路徑
            Path.GetFileName()檔名(包含副檔名)
            Path.GetFileNameWithoutExtension()檔名(不包含副檔名)
            Path.GetExtension()取得副檔名 包含.
            Path.GetPathRoot()根目錄
            Path.Combine()

            Path.GetRandomFileName()取得任意檔名
            Path.GetTempFileName()取得臨時檔名
            Path.GetTempPath()取得臨時路徑
            */

            richTextBox1.Text += "取得隨機檔名 : " + Path.GetRandomFileName() + "\n";
            richTextBox1.Text += "取得臨時檔名 : " + Path.GetTempFileName() + "\n";
            richTextBox1.Text += "取得臨時路徑 : " + Path.GetTempPath() + "\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            if (File.Exists(filename) == true)  // 確認檔案是否存在
            {
                //檔案資訊
                richTextBox1.Text += "完整路徑檔名 : " + Path.GetFullPath(filename) + "\n";  // 取得路徑

                richTextBox1.Text += "路徑 : " + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "檔名(包含副檔名) : " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名) : " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名 : " + Path.GetExtension(filename) + "\n";  // 取得副檔名 包含.
                richTextBox1.Text += "根目錄 : " + Path.GetPathRoot(filename) + "\n";  // 取得根目錄

                richTextBox1.Text += "修改成完整時間檔名 : " + Path.GetDirectoryName(filename) + "\\" + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "修改成時間檔名 : " + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
            }

            //------------------------------------------------------------  # 60個

            //Path.Combine()

            filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Form1.cs";
            richTextBox1.Text += filename + "\n";

            filename = Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) + "\\Form1.cs";
            richTextBox1.Text += filename + "\n";

            //取得本程式之Form1.cs所在的資料夾
            string dirname = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..\"));
            richTextBox1.Text += dirname + "\n";

            //由檔案取出檔案路徑
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = "picture1111.jpg";
            string new_filename = Path.Combine(Path.GetDirectoryName(filename), filename2);
            richTextBox1.Text += "new_filename : " + new_filename + "\n";

            /*
            讀Form1.cs所在位置的檔案純文字檔：
            string filename = Path.Combine(Application.StartupPath, "..\\..");

            將二進位檔讀出顯示出來
            txtCiphertextFile.Text = filename + "\\ciphertext.dat";
            txtCiphertext.Text = File.ReadAllBytes(txtCiphertextFile.Text).ToHex(' ');

            //------------------------------------------------------------  # 60個
            */
            string filename3 = Path.Combine(Application.StartupPath, @"..\..\Form1.cs");
            richTextBox1.Text += "filename : " + filename3 + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "資料夾 : " + foldername + "\n";
            richTextBox1.Text += "短檔名 : " + filename + "\n";
            richTextBox1.Text += "改名後的長檔名 : " + Path.Combine(foldername, filename.ToString().Replace("(", "").Replace(")", "")) + "\n";
            // 檔案重新命名
            //File.Move(Path.Combine(foldername, filename), Path.Combine(foldername, filename.ToString().Replace("(", "").Replace(")", "")));
        }

        //------------------------------------------------------------  # 60個

        private void bt_files01_Click(object sender, EventArgs e)
        {
            //顯示檔案大小

            //lblFileSize.Text = fi.Length.ToFileSizeApi();
            //int size = 12345678;
            //richTextBox1.Text += "size = " + size.tofil

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            FileInfo fi = new FileInfo(filename);
            richTextBox1.Text += fi.Length.ToString() + "\n";
            richTextBox1.Text += fi.Length.ToFileSizeApi() + "\n";

            int file_size = 12345678;   // double 才可以用 ToFileSize
            richTextBox1.Text += "file_size = " + file_size.ToString() + "\n";
            richTextBox1.Text += "file_size = " + ((double)file_size).ToFileSize() + "\n";
        }

        //------------------------------------------------------------  # 60個

        FileStream FormerOpen;
        FileStream ToFileOpen;
        /// <param FormerFile="string">源文件路徑</param>
        /// <param toFile="string">目的文件路徑</param> 
        /// <param SectSize="int">傳輸大小</param> 
        private void CopyFile(string FormerFile, string toFile, int SectSize)
        {
            FileStream fileToCreate = new FileStream(toFile, FileMode.Create);		//建立目的文件，如果已存在將被覆蓋
            fileToCreate.Close();										//關閉所有資源
            fileToCreate.Dispose();										//釋放所有資源
            FormerOpen = new FileStream(FormerFile, FileMode.Open, FileAccess.Read);//以只讀方式打開源文件
            ToFileOpen = new FileStream(toFile, FileMode.Append, FileAccess.Write);	//以寫方式打開目的文件
            //根據一次傳輸的大小，計算傳輸的個數
            int FileSize;												//要拷貝的文件的大小
            //如果分段拷貝，即每次拷貝內容小於文件總長度
            if (SectSize < FormerOpen.Length)
            {
                byte[] buffer = new byte[SectSize];							//根據傳輸的大小，定義一個字節數組
                int copied = 0;										//記錄傳輸的大小
                while (copied <= ((int)FormerOpen.Length - SectSize))			//拷貝主體部分
                {
                    FileSize = FormerOpen.Read(buffer, 0, SectSize);			//從0開始讀，每次最大讀SectSize
                    FormerOpen.Flush();								//清空快取
                    ToFileOpen.Write(buffer, 0, SectSize);					//向目的文件寫入字節
                    ToFileOpen.Flush();									//清空快取
                    ToFileOpen.Position = FormerOpen.Position;				//使源文件和目的文件流的位置相同
                    copied += FileSize;									//記錄已拷貝的大小
                }
                int left = (int)FormerOpen.Length - copied;						//取得剩餘大小
                FileSize = FormerOpen.Read(buffer, 0, left);					//讀取剩餘的字節
                FormerOpen.Flush();									//清空快取
                ToFileOpen.Write(buffer, 0, left);							//寫入剩餘的部分
                ToFileOpen.Flush();									//清空快取
            }
            //如果整體拷貝，即每次拷貝內容大於文件總長度
            else
            {
                byte[] buffer = new byte[FormerOpen.Length];				//取得文件的大小
                FormerOpen.Read(buffer, 0, (int)FormerOpen.Length);			//讀取源文件的字節
                FormerOpen.Flush();									//清空快取
                ToFileOpen.Write(buffer, 0, (int)FormerOpen.Length);			//寫放字節
                ToFileOpen.Flush();									//清空快取
            }
            FormerOpen.Close();										//釋放所有資源
            ToFileOpen.Close();										//釋放所有資源
            richTextBox1.Text += "文件複製完成\n";
        }

        private void bt_files02_Click(object sender, EventArgs e)
        {
            //拷貝檔案, 限定拷貝大小, 每次拷貝1024拜

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            CopyFile(filename1, filename2, 1024);
        }

        //------------------------------------------------------------  # 60個

        private const int MODE1 = 0x01;
        private const int MODE2 = 0x02;

        void copy_file(int mode)
        {
            richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";
            //取得檔案資訊
            string filename = "G:\\191128-1008.mp4";
            long filesize = 0;

            FileInfo fi = new FileInfo(filename);
            if (fi.Exists == true)      //確認檔案是否存在
            {
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + "\n";
                filesize = fi.Length;

                Stopwatch stopwatch = new Stopwatch();
                stopwatch.Start();

                FileStream sourceFile = new FileStream(filename, FileMode.Open, FileAccess.Read);
                //sourceFile 來源檔要先在該路徑中準備好

                FileStream targetFile = new FileStream(@"G:\tmp.mp4", FileMode.Create, FileAccess.Write);

                if (mode == MODE1)
                {
                    int bb = -1;
                    while ((bb = sourceFile.ReadByte()) != -1)  // 讀一拜
                    {
                        //一次1 byte的讀
                        targetFile.WriteByte((byte)bb);
                    }
                }
                else
                {
                    int count = -1;
                    byte[] bb = new byte[10240];
                    while ((count = sourceFile.Read(bb, 0, bb.Length)) > 0)
                    {
                        //一次讀10240個byte，相當於10k，效率較佳
                        targetFile.Write(bb, 0, bb.Length);
                    }
                }
                sourceFile.Close();
                targetFile.Close();

                stopwatch.Stop();
                richTextBox1.Text += "檔案大小: " + (filesize / 1024 / 1024).ToString() + " MB\n";
                richTextBox1.Text += "複製完畢！ 耗時: " + stopwatch.Elapsed.TotalSeconds.ToString() + " 秒\n";
                richTextBox1.Text += "速率: " + (filesize / 1024 / 1024 / stopwatch.Elapsed.TotalSeconds).ToString() + " MB/sec\n";
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
            }
            richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";
        }

        private void bt_files03_Click(object sender, EventArgs e)
        {
            //拷貝檔案1
            copy_file(MODE1);

            //拷貝檔案2
            copy_file(MODE2);
        }

        //------------------------------------------------------------  # 60個

        private void bt_files04_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        //根據文件頭判斷文件類型 ST
        private void bt_files05_Click(object sender, EventArgs e)
        {
            //根據文件頭判斷文件類型
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_哆啦A夢\doraemon1.jpg";
            string result = getFileType(filename);
            richTextBox1.Text += "File Type : " + result + "\n";
        }

        // 根據文件頭判斷文件類型
        private string getFileType(string filename)
        {
            try
            {
                FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
                BinaryReader br = new BinaryReader(fs);
                string fileClass;
                byte buffer;
                buffer = br.ReadByte();  // 讀一拜
                fileClass = buffer.ToString();
                buffer = br.ReadByte();  // 讀一拜
                fileClass += buffer.ToString();
                br.Close();
                fs.Close();

                //richTextBox1.Text += "fileClass == " + fileClass + "\t";

                if (fileClass == "255216")
                    return "jpg";
                else if (fileClass == "7173")
                    return "gif";
                else if (fileClass == "13780")
                    return "png";
                else if (fileClass == "6677")
                    return "bmp";
                else if (fileClass == "80114")
                    return "csv";
                else if (fileClass == "6063")
                    return "xml";
                else if (fileClass == "3780")
                    return "pdf";
                else if (fileClass == "4948")
                    return "txt";
                else if (fileClass == "8075")
                    return "zip";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else if (fileClass == "XXXX")
                    return "XXXX";
                else
                {
                    return fileClass + "\tunknown";
                }
                // 7790是exe,8297是rar 
            }
            catch
            {
                return "unknown";
            }
        }
        //根據文件頭判斷文件類型 SP

        //------------------------------------------------------------  # 60個

        void check_filetype(string filename)
        {
            int len = 10;
            int[] data = new int[len];
            string builtHex = string.Empty;
            using (Stream S = File.OpenRead(filename))
            {
                for (int i = 0; i < 10; i++)
                {
                    data[i] = S.ReadByte();  // 讀一拜
                    builtHex += data[i].ToString("X2") + " ";
                }
                richTextBox1.Text += "data : " + builtHex + "\n";
                if ((data[0] == 0x89) && (data[1] == 'P') && (data[2] == 'N') && (data[3] == 'G'))
                {
                    richTextBox1.Text += "PNG 檔案\n";
                }
                else if ((data[6] == 'J') && (data[7] == 'F') && (data[8] == 'I') && (data[9] == 'F'))
                {
                    richTextBox1.Text += "JPG 檔案\n";
                }
                else if ((data[0] == 'G') && (data[1] == 'I') && (data[2] == 'F') && (data[9] == '8') && (data[9] == '9'))
                {
                    richTextBox1.Text += "GIF 檔案\n";
                }
                else if ((data[0] == 'B') && (data[1] == 'M'))
                {
                    richTextBox1.Text += "BMP 檔案\n";
                }
                else if ((data[0] == 0xFF) && (data[1] == 0xFE))
                {
                    richTextBox1.Text += " 純文字Unicode 檔案\n";
                }
                else if ((data[0] == 'I') && (data[1] == 'D') && (data[2] == '3'))
                {
                    richTextBox1.Text += "MP3 檔案\n";
                }
                else
                {
                    richTextBox1.Text += "其他 檔案\n";
                }
            }
        }

        private void bt_files06_Click(object sender, EventArgs e)
        {
            //偵測原始檔案類型

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_csv\covid19_data2021_06_27.part.csv";
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\person.xml";
            string filename4 = @"C:\_git\vcs\_1.data\______test_files1\_anime\cat\cat1.png";
            string filename5 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";
            string filename6 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_mdb\db_09.mdb";
            string filename7 = @"C:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\eula.3081a.txt";
            string filename8 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_ini\ConnectString.ini";

            check_filetype(filename1);
            //check_filetype(filename2);
            //check_filetype(filename3);
            //check_filetype(filename4);
            //check_filetype(filename5);
            //check_filetype(filename6);
            //check_filetype(filename7);
            //check_filetype(filename8);
        }

        //------------------------------------------------------------  # 60個

        //取得檔案類型 ST

        //在shell32.dll導入函數SHGetFileInfo
        [DllImport("shell32.dll", EntryPoint = "SHGetFileInfo")]
        public static extern int GetFileInfo(string pszPath, int dwFileAttributes, ref FileInfomation psfi, int cbFileInfo, int uFlags);

        //定義SHFILEINFO結構(名字隨便起，這裡用FileInfomation)
        [StructLayout(LayoutKind.Sequential)]
        public struct FileInfomation
        {
            public IntPtr hIcon;
            public int iIcon;
            public int dwAttributes;

            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 260)]
            public string szDisplayName;

            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 80)]
            public string szTypeName;
        }

        //定義文件屬性標識
        public enum FileAttributeFlags : int
        {
            FILE_ATTRIBUTE_READONLY = 0x00000001,
            FILE_ATTRIBUTE_HIDDEN = 0x00000002,
            FILE_ATTRIBUTE_SYSTEM = 0x00000004,
            FILE_ATTRIBUTE_DIRECTORY = 0x00000010,
            FILE_ATTRIBUTE_ARCHIVE = 0x00000020,
            FILE_ATTRIBUTE_DEVICE = 0x00000040,
            FILE_ATTRIBUTE_NORMAL = 0x00000080,
            FILE_ATTRIBUTE_TEMPORARY = 0x00000100,
            FILE_ATTRIBUTE_SPARSE_FILE = 0x00000200,
            FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400,
            FILE_ATTRIBUTE_COMPRESSED = 0x00000800,
            FILE_ATTRIBUTE_OFFLINE = 0x00001000,
            FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 0x00002000,
            FILE_ATTRIBUTE_ENCRYPTED = 0x00004000
        }

        //定義獲取資源標識
        public enum GetFileInfoFlags : int
        {
            SHGFI_ICON = 0x000000100,     // get icon
            SHGFI_DISPLAYNAME = 0x000000200,     // get display name
            SHGFI_TYPENAME = 0x000000400,     // get type name
            SHGFI_ATTRIBUTES = 0x000000800,     // get attributes
            SHGFI_ICONLOCATION = 0x000001000,     // get icon location
            SHGFI_EXETYPE = 0x000002000,     // return exe type
            SHGFI_SYSICONINDEX = 0x000004000,     // get system icon index
            SHGFI_LINKOVERLAY = 0x000008000,     // put a link overlay on icon
            SHGFI_SELECTED = 0x000010000,     // show icon in selected state
            SHGFI_ATTR_SPECIFIED = 0x000020000,     // get only specifIEd attributes
            SHGFI_LARGEICON = 0x000000000,     // get large icon
            SHGFI_SMALLICON = 0x000000001,     // get small icon
            SHGFI_OPENICON = 0x000000002,     // get open icon
            SHGFI_SHELLICONSIZE = 0x000000004,     // get shell size icon
            SHGFI_PIDL = 0x000000008,     // pszPath is a pidl
            SHGFI_USEFILEATTRIBUTES = 0x000000010,     // use passed dwFileAttribute
            SHGFI_ADDOVERLAYS = 0x000000020,     // apply the appropriate overlays
            SHGFI_OVERLAYINDEX = 0x000000040      // Get the index of the overlay
        }

        private string GetTypeName(string fileName)
        {
            FileInfomation fileInfo = new FileInfomation();  //初始化FileInfomation結構

            //調用GetFileInfo函數，最後一個參數說明獲取的是文件類型(SHGFI_TYPENAME)
            int res = GetFileInfo(fileName, (int)FileAttributeFlags.FILE_ATTRIBUTE_NORMAL, ref fileInfo, Marshal.SizeOf(fileInfo), (int)GetFileInfoFlags.SHGFI_TYPENAME);

            return fileInfo.szTypeName;
        }

        private void bt_files07_Click(object sender, EventArgs e)
        {
            //取得檔案類型
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string fileTypeName = GetTypeName(filename);

            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案類型 : " + fileTypeName + "\n";
        }
        //取得檔案類型 SP

        //------------------------------------------------------------  # 60個

        private void bt_files08_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void bt_files09_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            int idx = listView1.SelectedIndices[0];
            /*
            richTextBox1.Text += "檔名:\t" + listView1.Items[idx].Text + "\n";
            richTextBox1.Text += "大小:\t" + listView1.Items[idx].SubItems[1].Text + "\n";
            richTextBox1.Text += "格式:\t" + listView1.Items[idx].SubItems[2].Text + "\n";
            richTextBox1.Text += "資料夾:\t" + listView1.Items[idx].SubItems[3].Text + "\n";
            string fullname = listView1.Items[idx].SubItems[3].Text + "\\" + listView1.Items[idx].Text;
            richTextBox1.Text += "完整路徑:\t" + fullname + "\n";
            */

            string foldername = listView1.Items[idx].SubItems[3].Text;
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            tb_foldername.Text = dinfo.Name;  //資料夾簡名
            tb_filename.Text = listView1.Items[idx].Text;  // 檔案名稱 或許不要副檔名
            tb_foldername_text_old = dinfo.Name;  //資料夾簡名
            tb_filename_text_old = listView1.Items[idx].Text;  // 檔案名稱 或許不要副檔名
            return;
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int idx = listView1.SelectedIndices[0];
            richTextBox1.Text += "檔名:\t" + listView1.Items[idx].Text + "\n";
            richTextBox1.Text += "大小:\t" + listView1.Items[idx].SubItems[1].Text + "\n";
            richTextBox1.Text += "格式:\t" + listView1.Items[idx].SubItems[2].Text + "\n";
            richTextBox1.Text += "資料夾:\t" + listView1.Items[idx].SubItems[3].Text + "\n";
            string fullname = listView1.Items[idx].SubItems[3].Text + "\\" + listView1.Items[idx].Text;
            richTextBox1.Text += "完整路徑:\t" + fullname + "\n";

            if (File.Exists(fullname) == true)
            {
                play_video_files(fullname);
            }
            else
            {
                richTextBox1.Text += "檔案 : " + fullname + " , 不存在\n";
            }
        }

        bool flag_sort_type0 = false;  // false : ASCENDING, true : DESCENDING
        bool flag_sort_type1 = false;  // false : ASCENDING, true : DESCENDING
        bool flag_sort_type2 = false;  // false : ASCENDING, true : DESCENDING
        bool flag_sort_type3 = false;  // false : ASCENDING, true : DESCENDING
        private void listView1_ColumnClick(object sender, ColumnClickEventArgs e)
        {
            //richTextBox1.Text += "你按了第 " + e.Column.ToString() + " 欄\n";
            //richTextBox1.Text += "aaa : " + listView1.Columns[e.Column] + "\n";
            //richTextBox1.Text += "bbb : " + e.Column.ToString() + "\n";

            if (e.Column == 0)
            {
                flag_sort_type0 = !flag_sort_type0;
                show_file_info6(0, flag_sort_type0);
            }
            else if (e.Column == 1)
            {
                flag_sort_type1 = !flag_sort_type1;
                show_file_info6(1, flag_sort_type1);
            }
            else if (e.Column == 2)
            {
                flag_sort_type2 = !flag_sort_type2;
                show_file_info6(2, flag_sort_type2);
            }
            else if (e.Column == 3)
            {
                flag_sort_type3 = !flag_sort_type3;
                show_file_info6(3, flag_sort_type3);
            }
            else
            {
                richTextBox1.Text += "XXXXXXX\n";
            }
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void bt_start_files_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;  // 總共選擇的個數
            if (selectCount == 0)
            {
                richTextBox1.Text += "未選取檔案\n";
                return;
            }

            string all_filename = string.Empty;
            for (int i = 0; i < selectCount; i++)
            {
                int idx = listView1.SelectedIndices[i];
                listView1.Items[idx].Selected = true;  // 選到的項目
                all_filename += " \"" + listView1.Items[idx].SubItems[3].Text + "\\" + listView1.Items[idx].Text + "\"";
            }
            play_video_files(all_filename);  // 播放
        }

        private void bt_start_all_files_Click(object sender, EventArgs e)
        {
            //播放全部

            // ListView 全部資料
            int len = listView1.Items.Count;
            richTextBox1.Text += "共有項目" + len.ToString() + " 個\n";
            string all_filename = string.Empty;
            for (int i = 0; i < len; i++)
            {
                //richTextBox1.Text += listView1.Items[i].Text + "\n";
                //richTextBox1.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\t" + listView1.Items[i].SubItems[2].Text + "\n";
                all_filename += " \"" + listView1.Items[i].SubItems[3].Text + "\\" + listView1.Items[i].Text + "\"";
            }
            play_video_files(all_filename);  // 播放
        }

        private void bt_delete_file_Click(object sender, EventArgs e)
        {
            int selectCount = listView1.SelectedIndices.Count;

            richTextBox1.Text += "你選擇了 : " + selectCount.ToString() + " 個檔案, 分別是\n";

            for (int i = 0; i < selectCount; i++)
            {
                richTextBox1.Text += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }

            richTextBox1.Text += "刪除\n";

            for (int i = selectCount - 1; i >= 0; i--)
            {
                richTextBox1.Text += "刪除檔案: " + listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";

                richTextBox1.Text += "目前不支援直接刪除檔案\n";
                /*  直接刪除檔案
                File.SetAttributes(listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text, FileAttributes.Normal);
                File.Delete(listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text);
                */
                listView1.SelectedItems[i].Remove();
            }
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        private void bt_open_dir1_Click(object sender, EventArgs e)
        {
            //folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_foldername1.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
        }

        private void bt_open_dir2_Click(object sender, EventArgs e)
        {
            //folderBrowserDialog1.SelectedPath = Application.StartupPath;    //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                tb_foldername2.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
        }

        private void bt_export_doc_Click(object sender, EventArgs e)
        {
            ProcessFile_mode = PROCESS_FILE_MODE0;  // 0:預設只匯出檔名
            ProcessFile_mode = PROCESS_FILE_MODE1;  // 1:只看大檔
            ProcessFile_mode = PROCESS_FILE_MODE2;  // 2:顯示至 ListView
            ProcessFile_mode = PROCESS_FILE_MODE3;  // 3:找空資料夾
            ProcessFile_mode = PROCESS_FILE_MODE4;  // 4:找小資料夾
            ProcessFile_mode = PROCESS_FILE_MODE5;  // 5:找特定檔案
            ProcessFile_mode = PROCESS_FILE_MODE6;  // 6:指定附檔名檔案
            ProcessFile_mode = PROCESS_FILE_MODE7;  // 7:只找資料夾 for 圖片整理
            ProcessFile_mode = PROCESS_FILE_MODE8;  // 8:搜尋影片檔, 搜尋小影片檔<720, 特大影片檔>1080
            ProcessFile_mode = PROCESS_FILE_MODE9;  // 9:匯出Katfile壓縮檔檔案資料

            ProcessFile_mode = PROCESS_FILE_MODE9;  // 9:匯出Katfile壓縮檔檔案資料

            foldername = Application.StartupPath;
            doc_foldername = tb_foldername1.Text;
            if (Directory.Exists(doc_foldername) == true)     //確認資料夾是否存在
            {
                foldername = doc_foldername;
            }

            do_my_export(foldername, bt_export_doc);

        }

        private void bt_export_video_Click(object sender, EventArgs e)
        {
            ProcessFile_mode = PROCESS_FILE_MODE0;  // 0:預設只匯出檔名
            ProcessFile_mode = PROCESS_FILE_MODE1;  // 1:只看大檔
            ProcessFile_mode = PROCESS_FILE_MODE2;  // 2:顯示至 ListView
            ProcessFile_mode = PROCESS_FILE_MODE3;  // 3:找空資料夾
            ProcessFile_mode = PROCESS_FILE_MODE4;  // 4:找小資料夾
            ProcessFile_mode = PROCESS_FILE_MODE5;  // 5:找特定檔案
            ProcessFile_mode = PROCESS_FILE_MODE6;  // 6:指定附檔名檔案
            ProcessFile_mode = PROCESS_FILE_MODE7;  // 7:只找資料夾 for 圖片整理
            ProcessFile_mode = PROCESS_FILE_MODE8;  // 8:搜尋影片檔, 搜尋小影片檔<720, 特大影片檔>1080
            ProcessFile_mode = PROCESS_FILE_MODE9;  // 9:匯出Katfile壓縮檔檔案資料

            ProcessFile_mode = PROCESS_FILE_MODE8;  // 8:搜尋影片檔, 搜尋小影片檔<720, 特大影片檔>1080

            foldername = Application.StartupPath;
            video_foldername = tb_foldername2.Text;
            if (Directory.Exists(video_foldername) == true)     //確認資料夾是否存在
            {
                foldername = video_foldername;
            }

            do_my_export(foldername, bt_export_video);

            listView1.Items.Clear();

            int len = fileinfos.Count;
            if (len == 0)
            {
                richTextBox1.Text += "無資料a\n";
            }
            else
            {
                richTextBox1.Text += "找到 " + len.ToString() + " 筆資料\n";
                show_file_info6(-1, false);
            }
        }

        void do_my_export(string foldername, Button btn)
        {
            //開始計時
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();
            btn.BackColor = Color.Red;
            lb_search_result1.Text = "";
            lb_search_result2.Text = "";
            Application.DoEvents();

            total_size = 0;
            total_files = 0;
            text = string.Empty;
            fileinfos.Clear();

            ProcessDirectory(foldername);

            richTextBox1.Text += text + "\n";

            if (total_files > 0)
            {
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
                richTextBox1.Text += "檔案個數 : " + total_files.ToString();
                richTextBox1.Text += ", 大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            }

            lb_search_result1.Text = total_files.ToString() + " / " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size));
            richTextBox1.Text += "檔案 : " + total_files.ToString() + " 個\n";
            richTextBox1.Text += "大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "(" + total_size.ToString() + "位元組)\n";
            //richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";

            stopwatch.Stop();
            richTextBox1.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " 毫秒\n";
            //lb_search_result2.Text = ((float)stopwatch.ElapsedMilliseconds / 1000).ToString("F2") + " 秒";
            lb_search_result2.Text = TimeConversion((Int64)(stopwatch.ElapsedMilliseconds / 1000));
            btn.BackColor = SystemColors.ControlLight;
        }

        private void bt_compare_Click(object sender, EventArgs e)
        {
            //fileinfos操作
            //比較

            int len = fileinfos.Count;
            if (len < 2)
            {
                richTextBox1.Text += "至少需要2筆資料\n";
                return;
            }

            fileinfos_match.Clear();

            for (int i = 0; i < len; i++)
            {
                for (int j = i + 1; j < (len - 1); j++)
                {
                    // case 1 : 比較真檔名
                    if (fileinfos[i].filename == fileinfos[j].filename)
                    {
                        richTextBox1.Text += "找到真檔名\n";
                        //richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                        //richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                        fileinfos_match.Add(fileinfos[i]);
                        fileinfos_match.Add(fileinfos[j]);
                    }

                    /*
                    // case 2 : 比較模糊檔名
                    if (fileinfos[i].shortfilename == fileinfos[j].shortfilename)
                    {
                        richTextBox1.Text += "找到模糊檔名\n";
                        //richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                        //richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                        fileinfos_match.Add(fileinfos[i]);
                        fileinfos_match.Add(fileinfos[j]);
                    }
                    */

                    // case 3 : 比較檔案大小
                    if (fileinfos[i].filesize == fileinfos[j].filesize)
                    {
                        richTextBox1.Text += "找到相同檔案大小\n";
                        //richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                        //richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                        fileinfos_match.Add(fileinfos[i]);
                        fileinfos_match.Add(fileinfos[j]);
                    }
                }
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "打印搜尋結果\n";
            len = fileinfos_match.Count;
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += fileinfos_match[i].filepath + "\t" + fileinfos_match[i].filename + "\t" + fileinfos_match[i].filesize + "\n";
            }
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        void get_DirectoryInfo(string foldername)
        {
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            get_DirectoryInfo(dinfo);
        }

        void get_DirectoryInfo(DirectoryInfo di)
        {
            //資料夾資訊
            richTextBox1.Text += "完整路徑：" + di.FullName + "\n";
            richTextBox1.Text += "屬性：" + di.Attributes + "\n";
            richTextBox1.Text += "存在與否：" + di.Exists + "\n";
            richTextBox1.Text += "資料夾名稱：" + di.Extension + "\n";
            richTextBox1.Text += "資料夾簡名：" + di.Name + "\n";
            richTextBox1.Text += "資料夾名稱：" + di.Parent + "\n";
            richTextBox1.Text += "上上層目錄 : " + di.Parent.Parent + "\n";
            richTextBox1.Text += "上上層目錄的全目錄 : " + di.Parent.Parent.FullName + "\n";
            richTextBox1.Text += "根資料夾：" + di.Root + "\n";
            richTextBox1.Text += "資料夾內資料夾數目：" + di.GetDirectories().Length + "\n";
            richTextBox1.Text += "資料夾內檔案數目：" + di.GetFiles().Length + "\n";
            richTextBox1.Text += "建立時間 : " + di.CreationTime + "\n";
            richTextBox1.Text += "建立時間 : " + di.LastAccessTime.ToString() + "\n";

            if (di.GetDirectories().Length > 0)
            {
                richTextBox1.Text += "下一層資料夾：";
                foreach (DirectoryInfo ddi in di.GetDirectories())
                {
                    get_DirectoryInfo(ddi);
                }
            }
            else
            {
                richTextBox1.Text += "\n";
            }
        }

        void get_FileInfo(string filename)
        {
            FileInfo fi = new FileInfo(filename);
            get_FileInfo(fi);
        }

        void get_FileInfo(FileInfo fi)
        {
            richTextBox1.Text += fi.Name + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

            return;

            if (fi.Exists == false)  // 確認檔案是否存在
            {
                richTextBox1.Text += "檔案不存在\n";
            }
            else
            {
                //由短檔案名取的短資料夾名

                richTextBox1.Text += "檔名：" + fi.Name + "\n";
                richTextBox1.Text += "全檔名：" + fi.FullName + "\n";
                richTextBox1.Text += "副檔名：" + fi.Extension + "\n";
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + "\n";
                richTextBox1.Text += "檔案大小：" + Convert.ToDouble(fi.Length / 1024).ToString() + " KB\n";
                richTextBox1.Text += "檔案大小：" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                richTextBox1.Text += "資料夾1：" + fi.Directory + "\n";
                richTextBox1.Text += "資料夾2：" + fi.Directory.Parent + "\n";
                richTextBox1.Text += "資料夾3：" + fi.DirectoryName + "\n";
                richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + "\n";
                richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + "\n";
                richTextBox1.Text += "CreationTime : " + fi.CreationTime + "\n";
                richTextBox1.Text += "CreationTimeUtc : " + fi.CreationTimeUtc + "\n";
                richTextBox1.Text += "最近修改時間：" + fi.LastWriteTime.ToString() + "\n";
                richTextBox1.Text += "最近修改時間：" + fi.LastWriteTime.ToShortDateString() + "\n";
                richTextBox1.Text += "最近修改時間：" + fi.LastWriteTimeUtc.ToString() + "\n";
                richTextBox1.Text += "存取日期：" + fi.LastAccessTime + "\n";
                richTextBox1.Text += "存取日期：" + fi.LastAccessTimeUtc + "\n";
                richTextBox1.Text += "屬性：" + fi.Attributes + "\n";
                richTextBox1.Text += "唯讀：" + fi.IsReadOnly + "\n";

                string fileSize = (fi.Length / 1024).ToString() + " KB";
                richTextBox1.Text += "fileSize = " + fileSize + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void ProcessDirectoryInfo(string foldername)
        {
            //使用 DirectoryInfo 和 FileInfo

            // 不能排序

            DirectoryInfo dinfo = new DirectoryInfo(foldername);

            // 找資料夾, 一層
            DirectoryInfo[] dis = dinfo.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dis)
            {
                // [System Volume Information] 資料夾是一個隱藏的系統資料夾，是「系統還原」工具用來儲存其資訊與還原點的地方。
                if (di.Name != "System Volume Information" && di.Name.Substring(0, 1) != "$")//避開此類folder權限問題
                {
                    ProcessDirectoryInfo(di.FullName);  // 利用遞迴把子資料夾也加進來
                }
            }

            // 找檔案, 一層
            FileInfo[] fis = dinfo.GetFiles();  // 由DI取得FI陣列, 一層檔案資訊
            foreach (FileInfo fi in fis)
            {
                get_FileInfo(fi);
            }
        }

        //------------------------------------------------------------  # 60個

        int files_in_folders = 0;
        string message = string.Empty;
        //以這個為標準, 使用 Directory.GetDirectories() 和 Directory.GetFiles()
        private void ProcessDirectory(string foldername)
        {
            //搜尋子目錄內的所有檔案   一層
            //使用 Directory.GetDirectories() 和 Directory.GetFiles()

            try
            {
                // 找資料夾, 一層
                string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
                Array.Sort(dirs);  // 排序
                foreach (string dir in dirs)
                {
                    try
                    {

                        // 資料夾
                        ProcessDirectory(dir);
                    }
                    catch (UnauthorizedAccessException)
                    {
                        Console.WriteLine("無法存取: " + dir);
                    }

                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("錯誤: " + ex.Message);
            }


            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            //text += "\n" + dinfo.Name + "\n";
            // 找檔案, 一層
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            Array.Sort(filenames);  // 排序
            message = string.Empty;
            files_in_folders = 0;
            foreach (string filename in filenames)
            {
                // 檔案
                ProcessFile(filename);
            }
            if (files_in_folders > 0)
            {
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
                DirectoryInfo d = new DirectoryInfo(foldername);
                richTextBox1.Text += "資料夾 : " + d.Name + "\n";
                richTextBox1.Text += "------------------------------\n";  // 30個
                richTextBox1.Text += message;
            }
        }

        private void ProcessFile(string filename)
        {
            FileInfo fi = new FileInfo(filename);

            if (cb_search.Checked == true)
            {
                if (fi.Name.Contains(tb_search.Text) == false)
                {
                    return;
                }
            }

            if (ProcessFile_mode == PROCESS_FILE_MODE0)  // 0:預設只匯出檔名
            {
                //text += fi.Name + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                text += "\t" + fi.Name + "\n";
            }
            else if (ProcessFile_mode == PROCESS_FILE_MODE1)  // 1:只看大檔
            {
                // 檢查檔案容量
                int min_size_mb = 1;  // MB
                if (fi.Length > (long)min_size_mb * 1024 * 1024)
                {
                    text += fi.Name + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                    return;
                }
            }
            else if (ProcessFile_mode == PROCESS_FILE_MODE2)  // 2:顯示至 ListView
            {
            }
            else if (ProcessFile_mode == PROCESS_FILE_MODE8)  // 8:搜尋影片檔, 搜尋小影片檔<720, 特大影片檔>1080
            {
                // 檢查檔案容量
                if (cb_size.Checked == true)
                {
                    int min_size_mb = int.Parse(tb_size.Text);
                    if (fi.Length < (long)min_size_mb * 1024 * 1024)
                    {
                        return;
                    }
                }
                text += fi.Name + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                //取得影片檔案資訊
                MediaInfoNET.MediaFile f = new MediaInfoNET.MediaFile(filename);
                if (f.InfoAvailable == true)
                {
                    if (f.Video.Count > 0)
                    {
                        int w = f.Video[0].Width;
                        int h = f.Video[0].Height;
                        int fps = (int)f.Video[0].FrameRate;

                        if (cb_search_big_files.Checked == true)
                        {
                            if (h <= 1080)
                            {
                                return;
                            }
                        }
                        if (cb_search_small_files.Checked == true)
                        {
                            if (h >= 1080)
                            {
                                return;
                            }
                        }

                        //短檔名    大小  格式       資料夾
                        //xxxx.mp4  4.8GB 1920X1080  AAAA/BBB/CCC
                        //richTextBox1.Text += "影片名稱: " + fi.Name + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                        //richTextBox1.Text += "影片長度: " + f.General.DurationString + "\n";
                        //richTextBox1.Text += "影片長度: " + f.General.DurationMillis + " 毫秒\n";
                        //richTextBox1.Text += "FrameCount: " + f.FrameCount.ToString() + "\n";
                        //richTextBox1.Text += "FPS: " + fps.ToString() + "\n";
                        //richTextBox1.Text += "time : " + ((int)(f.FrameCount / f.Video[0].FrameRate)).ToString() + " 秒\n";
                        //richTextBox1.Text += "輸入大小: " + w.ToString() + " × " + h.ToString() + "\n";

                        string n = fi.Name;
                        string p = fi.Directory.ToString();
                        string e = "AAAA";
                        long s = fi.Length;
                        int d = (int)(f.General.DurationMillis / 1000);

                        fileinfos.Add(new MyFileInfo(n, p, e, s, w, h, fps, d));
                        total_files++;
                        total_size += fi.Length;
                    }
                }
            }
            else if (ProcessFile_mode == PROCESS_FILE_MODE9)  // 9:匯出Katfile壓縮檔檔案資料
            {
                if ((fi.Extension.ToLower() == ".rar") || (fi.Extension.ToLower() == ".zip"))
                {
                    //message += "資料夾：" + fi.Directory + "\n";

                    message += "\t" + string.Format("{0,-30}{1,10}", fi.Name, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length))) + "\n";

                    //message += fi.Name + "\n";
                    //message += "副檔名：" + fi.Extension + "\n";
                    //message += "檔案大小：" + fi.Length.ToString() + "\n";
                    //message += "建立時間1：" + fi.CreationTime.ToString() + "\n";
                    //message += "建立時間2：" + fi.CreationTimeUtc.ToString() + "\n";
                    //message += "最近寫入時間：" + fi.LastWriteTime.ToString() + "\n";
                    //message += "檔案: " + filename + "\n";
                    //message += "------------------------------\n";  // 30個
                    total_files++;
                    total_size += fi.Length;
                    files_in_folders++;
                    return;
                }
            }
            if ((ProcessFile_mode != PROCESS_FILE_MODE8) && (ProcessFile_mode != PROCESS_FILE_MODE9))
            {
                total_files++;
                total_size += fi.Length;
            }
        }

        //------------------------------------------------------------  # 60個

        void get_MediaInfo(string filename)
        {
            MediaInfoNET.MediaFile f = new MediaInfoNET.MediaFile(filename);

            if (f.InfoAvailable == true)
            {
                richTextBox1.Text += "有MediaInfo資料, 全部資料:\n" + f.Info_Text + "\n\n";

                richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                richTextBox1.Text += "  Extension: " + f.Extension + "\n";

                // f.Video.Count

                int w = 0;
                int h = 0;

                if (f.Video.Count > 0)
                {
                    w = f.Video[0].Width;
                    h = f.Video[0].Height;
                    richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += string.Format("{0,5} X {1,5}{2,5}{3,10}",
                        w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
                }

                richTextBox1.Text += "有MediaInfo資料, 分項資料:\n";
                richTextBox1.Text += "File : " + f.File + "\n";
                richTextBox1.Text += "Name : " + f.Name + "\n";
                richTextBox1.Text += "Title : " + f.Title + "\n";
                richTextBox1.Text += "FileSize : " + f.FileSize.ToString() + " Bytes\n";
                richTextBox1.Text += "FrameCount : " + f.FrameCount.ToString() + "\n";
                richTextBox1.Text += "StreamCount : " + f.StreamCount.ToString() + "\n";
                richTextBox1.Text += "ParentFolder : " + f.ParentFolder + "\n";
                richTextBox1.Text += "Extension : " + f.Extension + "\n";
                richTextBox1.Text += "Description : \n" + f.Description + "\n";
                richTextBox1.Text += "Capacity : " + f.Text.Capacity.ToString() + "\n";

                //General
                richTextBox1.Text += "Format : " + f.General.Format + "\n";
                richTextBox1.Text += "Bitrate : " + f.General.Bitrate.ToString() + "\n";
                richTextBox1.Text += "CodecID : " + f.General.CodecID + "\n";
                richTextBox1.Text += "Description : " + f.General.Description + "\n";
                richTextBox1.Text += "DurationMillis : " + f.General.DurationMillis.ToString() + "\n";
                richTextBox1.Text += "DurationString : " + f.General.DurationString + "\n";
                richTextBox1.Text += "DurationStringAccurate : " + f.General.DurationStringAccurate + "\n";
                richTextBox1.Text += "Extension : " + f.General.Extension + "\n";
                richTextBox1.Text += "Format : " + f.General.Format + "\n";
                richTextBox1.Text += "FormatID : " + f.General.FormatID + "\n";
                richTextBox1.Text += "ID : " + f.General.ID.ToString() + "\n";
                richTextBox1.Text += "StreamSize : " + f.General.StreamSize.ToString() + "\n";
                richTextBox1.Text += "StreamType : " + f.General.StreamType + "\n";

                richTextBox1.Text += "\n";
                richTextBox1.Text += "Audio Count: " + f.Audio.Count.ToString() + "\n";
                richTextBox1.Text += "Video Count: " + f.Video.Count.ToString() + "\n";
                richTextBox1.Text += "\n";

                if (f.Audio.Count > 0)
                {
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Audio ---------------------------------" + "\n";
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Format : " + f.Audio[0].Format + "\n";
                    richTextBox1.Text += "Bitrate : " + f.Audio[0].Bitrate.ToString() + "\n";
                    richTextBox1.Text += "Channels : " + f.Audio[0].Channels.ToString() + "\n";
                    richTextBox1.Text += "Sampling : " + f.Audio[0].SamplingRate.ToString() + "\n";

                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "[音訊資訊]\n";
                    richTextBox1.Text += "  音訊編碼: " + f.Audio[0].Format + "\n";
                    richTextBox1.Text += "  取樣率: " + f.Audio[0].SamplingRate.ToString() + "\n";
                    richTextBox1.Text += "  聲道數: " + f.Audio[0].Channels.ToString() + "\n";
                    richTextBox1.Text += "  Bitrate: " + f.Audio[0].Bitrate.ToString() + " kbps\n";

                    /*
                    richTextBox1.Text += "CodecID : " + f.Audio[0].CodecID + "\n";
                    richTextBox1.Text += "Description : " + f.Audio[0].Description + "\n";
                    richTextBox1.Text += "DurationString : " + f.Audio[0].DurationString + "\n";
                    richTextBox1.Text += "Format : " + f.Audio[0].Format + "\n";
                    richTextBox1.Text += "FormatID : " + f.Audio[0].FormatID + "\n";
                    richTextBox1.Text += "ID : " + f.Audio[0].ID + "\n";
                    richTextBox1.Text += "MPlayerID : " + f.Audio[0].MPlayerID + "\n";
                    richTextBox1.Text += "StreamSize : " + f.Audio[0].StreamSize + "\n";
                    richTextBox1.Text += "StreamType : " + f.Audio[0].StreamType + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "\n無MediaInfo Audio資料\n";
                }

                if (f.Video.Count > 0)
                {
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Video ---------------------------------" + "\n";
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "Format : " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "Bit rate : " + f.Video[0].Bitrate.ToString() + "\n";
                    richTextBox1.Text += "Frame rate : " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += "Frame size : " + f.Video[0].FrameSize.ToString() + "\n";

                    richTextBox1.Text += "\n";
                    w = f.Video[0].Width;
                    h = f.Video[0].Height;

                    richTextBox1.Text += "[視訊資訊]\n";
                    richTextBox1.Text += "  視訊編碼: " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "  輸入格式: " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += "  Bitrate: " + f.Video[0].Bitrate.ToString() + " kbps\n";

                    /*
                    richTextBox1.Text += "Format : " + f.General.Format.ToString() + "\n";
                    richTextBox1.Text += "W : " + f.Video[0].Width.ToString() + "\n";
                    richTextBox1.Text += "H : " + f.Video[0].Height.ToString() + "\n";
                    richTextBox1.Text += "時間 : " + f.Video[0].DurationString + "\n";

                    richTextBox1.Text += "Description : " + f.Video[0].Description + "\n";
                    richTextBox1.Text += "Format : " + f.Video[0].Format + "\n";
                    richTextBox1.Text += "FrameRate : " + f.Video[0].FrameRate.ToString() + "\n";
                    richTextBox1.Text += "FrameSize : " + f.Video[0].FrameSize.ToString() + "\n";
                    richTextBox1.Text += "MPlayerID : " + f.Video[0].MPlayerID.ToString() + "\n";
                    richTextBox1.Text += "PixelFormat : " + f.Video[0].PixelFormat + "\n";
                    richTextBox1.Text += "Resolution : " + f.Video[0].Resolution.ToString() + "\n";
                    richTextBox1.Text += "StreamSize : " + f.Video[0].StreamSize.ToString() + "\n";
                    richTextBox1.Text += "StreamType : " + f.Video[0].StreamType + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "\n無MediaInfo Video資料\n";
                }
            }
            else
            {
                richTextBox1.Text += "非影片, 無MediaInfo資料\n";
            }

            //Info
            if (f.MediaInfo_Available == true)
            {
                richTextBox1.Text += "有MediaInfo資料, 全部資料:\n" + f.MediaInfo_Text + "\n";
            }
            else
            {
                richTextBox1.Text += "無MediaInfo資料\n";
            }
        }

        void play_video_files(string all_filename)
        {
            //richTextBox1.Text += "播放檔案 : " + all_filename + "\n";

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
            richTextBox1.Text += "target : " + target + "\n";
            richTextBox1.Text += "all_filename : " + all_filename + "\n";
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

        private void tb_foldername_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                //Enter


                e.Handled = true;
            }
            else if (e.KeyChar == (Char)27)  //撈取ESC
            {
                //ESC
                tb_foldername.Text = tb_foldername_text_old;  // 恢復

                e.Handled = true;
            }
            else
            {
                e.Handled = false;
            }


        }

        private void tb_filename_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)  //收到Enter後, 執行動作
            {
                //Enter


                e.Handled = true;
            }
            else if (e.KeyChar == (Char)27)  //撈取ESC
            {
                //ESC
                tb_filename.Text = tb_filename_text_old;  // 恢復

                e.Handled = true;
            }
            else
            {
                e.Handled = false;
            }
        }

        private void bt_test1_Click(object sender, EventArgs e)
        {
            //fileinfos操作

            //------------------------------------------------------------  # 60個

            //string longname = @"D:\內視鏡影片\Capsule Endoscopy Animation - ANKON NaviCam [720p].mp4";
            string longname = "jul-123-2.julia.mp4";

            string shortname = get_shortname(longname);
            richTextBox1.Text += "long name :  " + longname + "\n";
            richTextBox1.Text += "short name : " + shortname + "\n";

            //------------------------------------------------------------  # 60個

            //搜尋特定檔名

            string search_pattern = "maron";

            int len = fileinfos.Count;
            if (len < 2)
            {
                richTextBox1.Text += "至少需要2筆資料\n";
                return;
            }

            fileinfos_match.Clear();

            for (int i = 0; i < len; i++)
            {
                if (fileinfos[i].filename.ToLower().Contains(search_pattern.ToLower()) == true)
                {
                    fileinfos_match.Add(fileinfos[i]);
                }
            }

            //------------------------------------------------------------  # 60個

        }

        string get_shortname(string longname)
        {
            string shortname = longname;

            //一律轉小寫
            shortname = shortname.ToLower();

            //richTextBox1.Text += "old  = " + shortname + "\n";

            //先過濾掉一些字
            string[] remove_word = new string[] { "taxv.xyz_", "[javdb.com]", "[javdb.com]", "027_3xplanet_", "[Thz.la]"
                , "9288.pro@", "027_3xplanet_", "hhd800.com@", "big2048.com@", "[bbs.yzkof.com]"
                , "jav20s8.com@", "[javdb.com]", "松島楓", "桐原エリカ", "(Kirihara Erika)"
                , "[javdb.com]", "Abigaile Johnson ", "Heydoug", "heyzo_hd", "DLLAF"
                , "bbs2048.org@", "Abigaile Johnson ", "Heydoug", "avmans.com", "FHD"
                , "QQQQ", "僕とかえでの甘～い性活", "松島かえで", "[garea chinan]", "MIG"
                , "初剃り", "[44x.me]", "bbsxv.xyz", "@蜂鳥@fengniao151.vip", "18x78.com_"
                , "taxv.xyz", "jav20s8.com@", "shimohira", "hikari", "deeper.21"
                , "QQQQ", "QQQQ", "Caribbeancom", "[HD]", "104DANDAN"
                , "QQQQ", "jav4you.", "private", "52JAV.COM", "crv2000.com"
                , "javidol.com", "Prestige", "[thzu.cc]", "wowg.", "18x78.com_"
                , "(hibino)", "kpkp3.com", "bbyxv.xyz", "aaxv.xyz", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "-", "%", "$", "(", ")"};  //最後再刪除標點符號

            //重複刪除乾淨
            foreach (string r in remove_word)
            {
                shortname = shortname.Replace(r.ToLower(), "").Trim();
            }

            //richTextBox1.Text += "new 1 = " + shortname + "\n";

            //後面是7碼的
            string[] series7 = new string[] {
                  "fc2ppv", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
            };

            //後面是6碼的
            string[] series6 = new string[] {
                  "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
            };

            //後面是5碼的
            string[] series5 = new string[] {
                  "hodv", "kin", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
            };

            //後面是4碼的
            string[] series4 = new string[] {
                  "259luxu", "ofje", "nhdtb", "siro", "422ion", "kwbd", "heyzo"
                , "ppt", "583erkr", "525dht", "229scute", "200gana", "QQQQ", "QQQQ"
                , "hunb", "sprd", "luxu", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
            };

            //後面是3碼的
            string[] series3 = new string[] {
                  "390jac", "534ind", "590mcht", "300mium", "joymii.", "474musume", "594prgo"
                , "300ntk", "358with", "384shss", "393otim", "476mla", "491tkwa", "498ddh"
                , "hunta", "318lady", "300ntk", "326hgp", "428suke", "451hhh", "285endx"
                , "dgcemd", "dgcemd", "261ara", "529stcv", "230orec", "300maan", "345simm"
                , "336knb", "435mfcs", "546erofc", "502sei", "483pak", "210ako", "383reiw"
                , "292my", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                //5
                , "dldss", "hmdnv", "kmhrs", "dvdms", "stars", "fcdss", "fsdss"
                , "ftdss", "ptnoz", "dvdes", "svdvd", "QQQQ", "QQQQ", "QQQQ"
                , "favkh", "mxsps", "dandy", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"

                //4
                , "sdnm", "ssis", "kire", "iptd", "jufe", "mkmp", "natr"
                , "wanz", "mide", "cawd", "miaa", "pred", "azrd", "rctd"
                , "ksbj", "sdmu", "snis", "ssni", "vagu", "venu", "focs"
                , "mdbk", "vrtm", "mtall", "bacj", "mcsr", "mifd", "mrss"
                , "ngod", "homa", "mdtm", "urkk", "mukc", "venx", "ymdd"
                , "hzgd", "onsg", "mudr", "mvsd", "agav", "cadv", "hnds"
                , "mist", "mxgs", "pppd", "kawd", "ndra", "mudr", "mmkz"
                , "lulu", "ebod", "dvaj", "ipit", "mrhp", "ktra", "sdab"
                , "miad", "midd", "xvsr", "pppe", "ekdv", "dasd", "cemd"
                , "kmhr", "sdde", "shkd", "soav", "cjod", "ktkl", "star"
                , "mmks", "sqte", "mird", "sdmm", "nacr", "tppn", "pkpd"
                , "hgot", "atid", "cesd", "ktkc", "apns", "fset", "nkkd"
                , "ambi", "kdmi", "aukg", "pcde", "msfh", "fffs", "genm"
                , "akdl", "sama", "iesp", "waaa", "tysf", "avsa", "cpde"
                , "ktkz", "sdmf", "clot", "saba", "dnjr", "hdka", "kuse"
                , "royd", "mimk", "upsm", "sdjs", "cead", "kymi", "dpmi"
                , "eyan", "smcp", "onez", "bobb", "nnpj", "kray", "mdon"
                , "sace", "bijn", "rabs", "sapa", "crpd", "jufd", "misg"
                , "gnab", "docp", "bahp", "cetd", "urlh", "milk", "sksk"
                , "aqsh", "mism", "mond", "sspd", "mogi", "bban", "pfes"
                , "xmom", "zocm", "aqsh", "dtsg", "voss", "zmen", "dfdm"
                , "hawa", "dkwt", "real", "ekdv", "dvaj", "vema", "mgmj"
                , "omhd", "bacn", "ggen", "honb", "piyo", "hjmo", "csct"
                , "ikep", "josi", "oksn", "jjcc", "mmym", "post", "apkh"
                , "sora", "juny", "hbad", "crim", "miae", "mdyd", "mizd"
                , "sgrs", "mbyd", "apak", "apak", "nima", "tikp", "migd"
                , "okad", "oned", "sdmt", "annd", "ipsd", "lhjf", "masd"
                , "mama", "magd", "nass", "mild", "sdms", "onem", "sdmt"
                , "edrg", "myba", "supd", "nsfs", "baam", "tyod", "aldn"
                , "dass", "mlsm", "good", "jrze", "hthd", "iene", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                //3
                , "abp", "jul", "jux", "ipx", "adn", "meyd", "midv"
                , "chn", "abw", "pxh", "ped", "gvh", "gvg", "tek"
                , "vec", "dje", "arm", "roe", "blk", "ecb", "pgd"
                , "mgt", "hmn", "hnd", "rbd", "veo", "bbi", "tki"
                , "fch", "ttd", "rbk", "ipz", "rki", "soe", "crc"
                , "dkd", "ure", "bgn", "adz", "oyc", "raw", "leg"
                , "ebl", "sma", "san", "esk", "bur", "wnz", "man"
                , "dss", "dic", "kyk", "pla", "umd", "abs", "fir"
                , "ddk", "scd", "cmd", "kir", "omt", "xrw", "ktb"
                , "wkd", "sga", "ytr", "dtt", "jbs", "zex", "izm"
                , "bkd", "juy", "juc", "kbi", "jbd", "scg", "QQQQ"
                , "mdb", "tem", "cwp", "aka", "QQQQ", "QQQQ", "QQQQ"
                , "elo", "mek", "evo", "ban", "cwm", "egt", "ezd"
                , "jag", "kaz", "ksd", "mdb", "nsr", "sgv", "fax"
                , "ars", "rct", "bid", "blo", "nwf", "ufd", "vdd"
                , "vis", "wfs", "wif", "yzf", "veq", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                //2
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ", "QQQQ"
                , "dsam", "toen", "bt", "dllafbd", "QQQQ", "QQQQ", "QQQQ"
                , "xv", "sw", "bf", "sy", "gs", "QQQQ", "QQQQ"
            };

            int len = 0;
            int position = -1;

            if (position < 0)
            {
                foreach (string r in series7)   //後面是7碼的
                {
                    position = shortname.IndexOf(r, 0);
                    if (position > -1)
                    {
                        len = r.Length;
                        shortname = shortname.Substring(position, len + 7);
                        break;
                    }
                }
            }

            if (position < 0)
            {
                foreach (string r in series6)   //後面是6碼的
                {
                    position = shortname.IndexOf(r, 0);
                    if (position > -1)
                    {
                        len = r.Length;
                        shortname = shortname.Substring(position, len + 6);
                        break;
                    }
                }
            }

            if (position < 0)
            {
                foreach (string r in series5)   //後面是5碼的
                {
                    position = shortname.IndexOf(r, 0);
                    if (position > -1)
                    {
                        len = r.Length;
                        shortname = shortname.Substring(position, len + 5);
                        break;
                    }
                }
            }

            //richTextBox1.Text += "new 2 = " + shortname + "\n";
            if (position < 0)
            {
                foreach (string r in series4)   //後面是4碼的
                {
                    position = shortname.IndexOf(r, 0);
                    if (position > -1)
                    {
                        len = r.Length;
                        shortname = shortname.Substring(position, len + 4);
                        break;
                    }
                }
            }

            //richTextBox1.Text += "new 3 = " + shortname + "\n";
            if (position < 0)
            {
                foreach (string r in series3)   //後面是3碼的
                {
                    position = shortname.IndexOf(r, 0);
                    if (position > -1)
                    {
                        len = r.Length;
                        shortname = shortname.Substring(position, len + 3);
                        break;
                    }
                }
            }

            //richTextBox1.Text += "new 4 = " + shortname + "\n";
            /*
            //dv接4碼, 有點問題, 會誤判......
            if (position < 0)
            {
                string pattern = "dv";
                position = shortname.IndexOf(pattern, 0);
                if (position > -1)
                {
                    len = pattern.Length;
                    shortname = shortname.Substring(position, len + 4);
                    break;             
                }
            }
            */
            //richTextBox1.Text += "new =  " + shortname + "\n";

            return shortname;
        }

        //------------------------------------------------------------  # 60個

        private void bt_test2_Click(object sender, EventArgs e)
        {
            //優優檔

            int len = fileinfos.Count;
            if (len == 0)
            {
                richTextBox1.Text += "無資料c\n";
            }
            else
            {
                richTextBox1.Text += "找到 " + len.ToString() + " 筆資料\n";
            }

            if (len < 2)
            {
                richTextBox1.Text += "至少需要2筆資料\n";
                return;
            }

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

            for (int i = 0; i < len; i++)
            {
                foreach (string ptn in good_pattern)
                {
                    if (fileinfos[i].filename.ToLower().Contains(ptn) == true)
                    {
                        fileinfos_match.Add(fileinfos[i]);
                        break;
                    }
                }
            }
        }

        private void bt_test3_Click(object sender, EventArgs e)
        {
            //測試顯示時間

            //public string ByteConversionTBGBMBKB(Int64 size)

            Int64 elpased_time = 1234567;
            richTextBox1.Text += ByteConversionTBGBMBKB(Convert.ToInt64(elpased_time)) + "\n";

            elpased_time = 86400 - 1;
            richTextBox1.Text += TimeConversion(elpased_time) + "\n";

            elpased_time = 86400 + 1;
            richTextBox1.Text += TimeConversion(elpased_time) + "\n";

            elpased_time = 3600 + 1;
            richTextBox1.Text += TimeConversion(elpased_time) + "\n";
            elpased_time = 3600 - 1;
            richTextBox1.Text += TimeConversion(elpased_time) + "\n";

            //lb_search_result2.Text = ((float)elpased_time / 1000).ToString("F2") + " 秒";
        }

        private void bt_test4_Click(object sender, EventArgs e)
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

/*
public static void Rename(this FileInfo fi, string newName)
{
    fi.MoveTo(fi.Directory.FullName + "\\" + newName);
}

//------------------------------------------------------------  # 60個

待測
//File.AppendAllText("E:\\Time\\新建文檔夾 (2)" + "/" + strname, DateTime.Now+"\n");

//------------------------------------------------------------  # 60個

bool res;
res = fi.FullName.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));

//if (filename.Contains(".zip") == true)

//------------------------------------------------------------  # 60個

影片用
若是最底層資料夾 找出小資料夾
min_size_mb = 10;  // 最小值 10 MB
            if (dirs.Length == 0)
            {
                richTextBox1.Text += "資料夾 : " + foldername + " 是最底層的資料夾\n";
                if (folder_size < min_size_mb * 1024 * 1024)
                {
                    DirectoryInfo di = new DirectoryInfo(foldername);
                }
            }

//------------------------------------------------------------  # 60個

            int i;
            int len = fileinfos.Count;
            richTextBox1.Text += "找到 " + len.ToString() + " 筆資料\n";

            string save_filename = "filename_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileStream filestream = System.IO.File.Open(save_filename, FileMode.Create);
            StreamWriter str_writer = new StreamWriter(filestream);

            // RTB 直接存檔
            //str_writer.WriteLine(richTextBox1.Text);

            // 只存檔案名稱資料
            for (i = 0; i < len; i++)
            {
                string filename = fileinfos[i].filename;
                string mesg = string.Empty;
                //richTextBox1.Text += filename + "\n";

                FileInfo fi = new FileInfo(fileinfos[i].filepath + "\\" + filename);
                richTextBox1.Text += fi.FullName + "\t";
                richTextBox1.Text += ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                //mesg += fi.FullName + "\t";
                mesg += String.Format("{0,-50}", filename);
                //mesg += filename + "\t";
                //mesg += ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\t";
                mesg += String.Format("{0,-30}", ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)));
                richTextBox1.Text += "len = " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)).Length.ToString() + "\n";

                richTextBox1.Text += mesg + "\n";
                str_writer.WriteLine(mesg);
            }

            // Dispose StreamWriter
            str_writer.Dispose();
            // Close FileStream
            filestream.Close();

            richTextBox1.Text += "儲存資料完畢，檔案：" + save_filename + "\n";


                //StreamReader sr = new StreamReader(saveFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                FileStream filestream = System.IO.File.Open(saveFileDialog1.FileName, FileMode.Create);
                StreamWriter str_writer = new StreamWriter(filestream);

                str_writer.WriteLine(richTextBox1.Text);
                // Dispose StreamWriter
                str_writer.Dispose();
                // Close FileStream
                filestream.Close();

                richTextBox1.Text += "儲存資料完畢，檔案：" + saveFileDialog1.FileName + "\n";

//------------------------------------------------------------  # 60個

fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length));
fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
folderinfos.Add(new MyFolderInfo(foldername, foldername, folder_size, datetime.now));
               
//------------------------------------------------------------  # 60個

// 全部內容
int len = fileinfos.Count;
//richTextBox1.Text += "Name\tFolderName\tExt\tLength\tTime\n";
for (int i = 0; i < len; i++)
{
    //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,20} X {3,20}{4,20}{5,20}",
    //fileinfos[i].filename, ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)), 
    //fileinfos[i].filepath, fileinfos[i].fileextension) + "\n";

    //richTextBox1.Text += fileinfos[i].filename + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filesize + "\t" + "\n";

    //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
    //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

    //richTextBox1.Text += string.Format("{0,-60}{1,-60}{2,-60}{3,-60}{4,-60}", fileinfos[i].filename, fileinfos[i].filename, fileinfos[i].filename, fileinfos[i].filename, fileinfos[i].filename);
    //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
    richTextBox1.Text += string.Format("{0,-70}{1,-10}{2,-15}{3,-60}", fileinfos[i].filename, fileinfos[i].fileextension, ByteConversionTBGBMBKB(fileinfos[i].filesize), fileinfos[i].filepath) + "\n";
}

//------------------------------------------------------------  # 60個
// 合併 "filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

*/


/*
兩個相同
            int selectCount = listView1.SelectedIndices.Count;  // 總共選擇的個數
            int selectCount2 = listView1.SelectedItems.Count;
*/



