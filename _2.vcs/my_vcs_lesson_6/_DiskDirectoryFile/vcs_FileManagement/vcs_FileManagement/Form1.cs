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
using System.Globalization; //for CultureInfo

using MediaInfoNET;

/*
參考/加入參考/選 MediaInfoNET.dll
加入/現有項目/選 MediaInfo.dll, 改屬性為 永遠複製
*/

namespace vcs_FileManagement
{
    public partial class Form1 : Form
    {
        //string video_foldername = @"D:\_git\vcs\_1.data\______test_files1\_mp4";
        string video_foldername = @"D:\vcs\astro\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";

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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

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

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            listView1.Size = new Size(800, 340 - 30);
            listView1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 30);
            richTextBox1.Size = new Size(800, 340);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1280, 820);
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

        private void button0_Click(object sender, EventArgs e)
        {
            //增加影片
            FindAllFiles(video_foldername);
        }

        void FindAllFiles(string foldername)
        {
            fileinfos.Clear();
            total_size = 0;
            total_files = 0;

            richTextBox1.Text += "\n搜尋路徑" + foldername + "\n";

            if (System.IO.File.Exists(foldername))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(foldername))
            {
                // This path is a directory
                FolederName = foldername;
                ProcessDirectory(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案b\n";
            }
        }

        bool flag_need_shortname = false;

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
            //richTextBox1.Text += "處理Directory " + targetDirectory + "\n";
            try
            {
                //richTextBox1.Text += targetDirectory + "\n\n";
                //DirectoryInfo di = new DirectoryInfo(targetDirectory);
                //richTextBox1.Text += di.Name + "\n\n";

                // Process the list of files found in the directory.
                try
                {
                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    Array.Sort(fileEntries);
                    folder_size = 0;
                    folder_files = 0;
                    foreach (string fileName in fileEntries)
                    {
                        ProcessFile(fileName);
                    }
                    //richTextBox1.Text += "folder_name = " + targetDirectory + "\n";
                    //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";
                    //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
                    if (folder_files == 0)
                    {
                        //richTextBox1.Text += "空資料夾 folder_name = " + targetDirectory + "\n";
                    }

                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    Array.Sort(subdirectoryEntries);
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        //richTextBox1.Text += "搜尋子目錄\t" + di.Name + "\n";
                        FolederName = subdirectory;
                        ProcessDirectory(subdirectory);
                    }
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
            }
        }

        // Insert logic for processing found files here.
        public void ProcessFile(string path)
        {
            //richTextBox1.Text += "處理File " + path + "\n";

            FileInfo fi;

            try
            {   //可能會產生錯誤的程式區段
                fi = new FileInfo(path);
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "錯誤訊息1 : " + ex.Message + "\n";
                return;
            }
            finally
            {
                //一定會被執行的程式區段
            }

            //richTextBox1.Text += "folder = " + FolederName + ",  name = " + fi.Name + "\n";

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            //if (((cb_file_l.Checked == true) && (fi.Length > min_size_mb * 1024 * 1024)) || (cb_file_l.Checked == false))
            {
                //搜尋檔名用
                if (flag_search_mode == 1)
                {
                    /*
                    bool res;
                    res = fi.FullName.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        return;
                    else
                    */
                    {
                        richTextBox1.Text += "get file : " + fi.FullName + "\n";
                    }
                }

                //richTextBox1.Text += fi.Name + " len = " + fi.Length.ToString() + "\n";
                //richTextBox1.Text += filename + "\n";
                //richTextBox1.Text += fi.Name + "\n";
                //richTextBox1.Text += fi.Name + " \t\t " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                MediaFile f = new MediaFile(fi.FullName);

                //richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                //richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                //richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    //richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    //richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    //if (cb_generate_text.Checked == true)
                    {
                        richTextBox1.Text += "影片\t";
                        richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                            fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                        fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
                    }
                }
                else
                {
                    //if (cb_generate_text.Checked == true)
                    {
                        richTextBox1.Text += "非影片\t";
                        richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                        fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
                    }
                }

                //richTextBox1.Text += fi.Directory + "\n";
                //richTextBox1.Text += fi.DirectoryName + "\n";

                /*
                ListViewItem i1 = new ListViewItem(fi.FullName);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
                */

                //或許某些時候不需要
                //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));

                string shortname = string.Empty;
                if (flag_need_shortname == true)
                {
                    //shortname = get_shortname(fi.Name);  //過濾掉檔名的一些字 用以做比較用
                }

                //richTextBox1.Text += "fname = " + fi.FullName + "\n";
                //richTextBox1.Text += "dname = " + fi.DirectoryName + "\n";

                //把資料放進 List<MyFileInfo> fileinfos 中
                //fileinfos.Add(new MyFileInfo(fi.Name, fi.FullName, shortname, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));


            }
        }


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
            //搜尋一個資料夾內所有特定格式的檔案
            //搜尋一個資料夾內所有特定格式的檔案

            ///根據路徑實例化一個對象
            var di = new DirectoryInfo(video_foldername);

            ///選出所有符合一定後綴的文件列表
            FileInfo[] files = di.GetFiles("*.*", SearchOption.AllDirectories).Where(info => IsRight(info)).ToArray();

            foreach (FileInfo f in files)
            {
                richTextBox1.Text += f.FullName + "\n";
            }
        }

        private bool IsRight(FileInfo info)
        {
            //選擇的文件後綴名
            //List<string> patterns = new List<string>() { ".png", ".jpg", ".bmp", ".tif" };
            List<string> patterns = new List<string>() { ".png" };
            return patterns.Contains(info.Extension);
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        //獲得指定目錄下的所有文檔 ST

        double total_size1 = 0;
        int no_files = 0;
        int no_folders = 0;

        private void button10_Click(object sender, EventArgs e)
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


        private void button11_Click(object sender, EventArgs e)
        {
            //轉出一層 標準版
            richTextBox1.Text += "轉出一層 標準版\n";

            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            ((Button)sender).BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            //轉出一層
            fileinfos.Clear();

            total_size = 0;
            total_files = 0;

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            richTextBox1.Text += "\n搜尋路徑" + foldername + "\n";

            if (System.IO.File.Exists(foldername) == true)
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(foldername) == true)
            {
                // This path is a directory
                //FolederName = foldername;
                //ProcessDirectory(foldername);

                try
                {
                    //richTextBox1.Text += targetDirectory + "\n\n";
                    //DirectoryInfo di = new DirectoryInfo(targetDirectory);
                    //richTextBox1.Text += di.Name + "\n\n";

                    // Process the list of files found in the directory.
                    try
                    {
                        string[] fileEntries = Directory.GetFiles(foldername);
                        Array.Sort(fileEntries);
                        foreach (string fileName in fileEntries)
                        {
                            ProcessFile(fileName);
                        }
                    }
                    catch (UnauthorizedAccessException ex)
                    {
                        richTextBox1.Text += ex.Message + "\n";
                    }
                }
                catch (IOException ex)
                {
                    richTextBox1.Text += "IOException, " + ex.GetType().Name + "\n";
                }

                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else
            {
                richTextBox1.Text += "非合法路徑或檔案a\n";
            }
            this.Cursor = Cursors.Default;
            ((Button)sender).BackColor = SystemColors.ControlLight;

            stopwatch.Stop();
            richTextBox1.Text += "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";
            richTextBox1.Text += "檔案個數 : " + total_files.ToString() + "\n";
            richTextBox1.Text += "總容量   : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";

            show_file_info();

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //轉出全部 標準版
            richTextBox1.Text += "轉出全部 標準版\n";

            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            ((Button)sender).BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            //轉出全部
            fileinfos.Clear();

            total_size = 0;
            total_files = 0;

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            richTextBox1.Text += "\n搜尋路徑" + foldername + "\n";

            if (System.IO.File.Exists(foldername) == true)
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(foldername) == true)
            {
                // This path is a directory
                FolederName = foldername;
                ProcessDirectory(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else
            {
                richTextBox1.Text += "非合法路徑或檔案b\n";
            }
            this.Cursor = Cursors.Default;
            ((Button)sender).BackColor = SystemColors.ControlLight;

            stopwatch.Stop();
            richTextBox1.Text += "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";
            richTextBox1.Text += "檔案個數 : " + total_files.ToString() + "\n";
            richTextBox1.Text += "總容量   : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";

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
            //test
            richTextBox1.Text += "轉出全部 標準版\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            richTextBox1.Text += "\n搜尋路徑" + foldername + "\n";

            if (System.IO.File.Exists(foldername) == true)
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(foldername) == true)
            {
                // This path is a directory
                FolederName = foldername;
                ProcessDirectory(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else
            {
                richTextBox1.Text += "非合法路徑或檔案b\n";
            }


        }

        //以下的沒用到

        void show_file_info()  //轉出一層
        {
            richTextBox1.Text += "show_file_info show_file_info show_file_info\n";
            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            if (fileinfos.Count == 0)
            {
                richTextBox1.Text += "無資料a\n";
                return;
            }
            else
            {
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料c\n";
                int i;
                for (i = 0; i < fileinfos.Count; i++)
                {
                    //richTextBox1.Text += fileinfos[i].filename + "\n";
                    richTextBox1.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                    MediaFile f = new MediaFile(fileinfos[i].filepath + "\\" + fileinfos[i].filename);

                    //richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                    //richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                    //richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                    if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                    {
                        int w = f.Video[0].Width;
                        int h = f.Video[0].Height;
                        //richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                        //richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                        //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                        //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
                        /*
                        if (((cb_video_l.Checked == true) && (h >= 1080)) || ((cb_video_m.Checked == true) && (h < 1080) && (h > 480)) || ((cb_video_s.Checked == true) && (h <= 480)))
                        {
                            item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                            if (h >= 1080)
                                items = "大";
                            else if (h <= 480)
                                items = "小";
                            else
                                items = "中";
                            itema = fileinfos[i].filename;
                            itemb = fileinfos[i].filepath;
                            itemc = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));

                            //i1 = new ListViewItem(fileinfos[i].filename);
                            i1 = new ListViewItem(item);
                            i1.UseItemStyleForSubItems = false;

                            //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                            sub_i1s.Text = items;
                            i1.SubItems.Add(sub_i1s);

                            sub_i1a.Text = itema;
                            i1.SubItems.Add(sub_i1a);
                            //sub_i1a.Text = fileinfos[i].filepath;
                            //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                            sub_i1b.Text = itemb;
                            i1.SubItems.Add(sub_i1b);

                            //sub_i1a.Text = fi.Length.ToString();
                            //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                            sub_i1c.Text = itemc;
                            i1.SubItems.Add(sub_i1c);

                            sub_i1a.ForeColor = System.Drawing.Color.Blue;
                            sub_i1b.ForeColor = System.Drawing.Color.Blue;
                            sub_i1c.ForeColor = System.Drawing.Color.Blue;

                            sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                            sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                            sub_i1c.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        }
                        else
                            continue;
                        */
                    }
                    else
                    {
                        /*
                        if (cb_video_only.Checked == true)
                            continue;

                        if (cb_generate_text.Checked == false)
                            continue;

                        i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                        //richTextBox1.Text += "xxxxx" + fileinfos[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        sub_i1a.Text = fileinfos[i].filepath;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fi.Length.ToString();
                        sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        i1.SubItems.Add(sub_i1b);

                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1b.ForeColor = System.Drawing.Color.Blue;

                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        */
                    }
                }
            }
        }

        void show_file_info1()  //轉出一層
        {
            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
            richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";


            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            //if (cb_video_only.Checked == true)
            {
                listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("檔名1", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            /*
            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
            }
            */

            if (fileinfos.Count == 0)
                richTextBox1.Text += "找不到資料a\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料a\n";

            for (int i = 0; i < fileinfos.Count; i++)
            {
                //ListViewItem i1 = new ListViewItem(fileinfos[i].filename);


                ListViewItem.ListViewSubItem sub_i1s = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();

                string item = string.Empty;
                string items = string.Empty;
                string itema = string.Empty;
                string itemb = string.Empty;
                string itemc = string.Empty;

                //if (cb_video_only.Checked == true)
                {
                    ListViewItem i1;

                    //debug mesg
                    //richTextBox1.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                    MediaFile f = new MediaFile(fileinfos[i].filepath + "\\" + fileinfos[i].filename);

                    //richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                    //richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                    //richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                    if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                    {
                        int w = f.Video[0].Width;
                        int h = f.Video[0].Height;
                        //richTextBox1.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                        //richTextBox1.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                        //richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                        //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                        //if (((cb_video_l.Checked == true) && (h >= 1080)))
                        {
                            item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                            if (h >= 1080)
                                items = "大";
                            else if (h <= 480)
                                items = "小";
                            else
                                items = "中";
                            itema = fileinfos[i].filename;
                            itemb = fileinfos[i].filepath;
                            itemc = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));

                            //i1 = new ListViewItem(fileinfos[i].filename);
                            i1 = new ListViewItem(item);
                            i1.UseItemStyleForSubItems = false;

                            //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                            sub_i1s.Text = items;
                            i1.SubItems.Add(sub_i1s);

                            sub_i1a.Text = itema;
                            i1.SubItems.Add(sub_i1a);
                            //sub_i1a.Text = fileinfos[i].filepath;
                            //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                            sub_i1b.Text = itemb;
                            i1.SubItems.Add(sub_i1b);

                            //sub_i1a.Text = fi.Length.ToString();
                            //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                            sub_i1c.Text = itemc;
                            i1.SubItems.Add(sub_i1c);

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
                    else
                    {
                        i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                        //richTextBox1.Text += "xxxxx" + fileinfos[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        sub_i1a.Text = fileinfos[i].filepath;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fi.Length.ToString();
                        sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        i1.SubItems.Add(sub_i1b);

                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1b.ForeColor = System.Drawing.Color.Blue;

                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        listView1.Items.Add(i1);
                        //設置ListView最後一行可見
                        //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
                    }




                }
                /*
                else
                {
                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
                    sub_i1a.Text = fileinfos[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = System.Drawing.Color.Blue;
                    sub_i1b.ForeColor = System.Drawing.Color.Blue;

                    sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                }
                */
            }
        }
    }
}

