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
        //string foldername = @"C:\______test_files_file_manager";    //欲搜尋的資料夾
        //string foldername = @"D:\vcs\astro\_DATA2\_________整理_mp3\wen2";
        string foldername = @"C:\______test_files\__RW\_avi";

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
                return (Math.Round(size / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return size.ToString() + " Byte";//顯示Byte值
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.listView1.GridLines = true;
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //先不急
            //show_item_location();
            //update_default_setting();
        }

        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //Properties.Settings.Default.search_path = save_path;
            Properties.Settings.Default.Save();

        }

        void show_item_location()
        {

        }

        void update_default_setting()
        {
            search_path = Properties.Settings.Default.search_path;

            //預設搜尋路徑
            string PATH = Properties.Settings.Default.search_path;
            //richTextBox2.Text += "PATH = " + PATH + "\n";

            string[] path = PATH.Split(';');

            foreach (string p in path)
            {
                if (p.Length > 0)
                {
                    //check existency
                    if (Directory.Exists(p) == true)
                    {
                        //richTextBox2.Text += "len = " + p.Length.ToString() + "\t" + p + "\n";
                        richTextBox2.Text += "加入路徑 : " + p + "\n";
                        old_search_path.Add(p);       //目前只能 儲存/加入 一個路徑
                    }
                    else
                    {
                        richTextBox2.Text += "搜尋預設路徑不存在 : " + p + "\tskip\n";
                    }
                }
            }
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }


        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
            richTextBox1.Text += "處理Directory " + targetDirectory + "\n";
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
                        richTextBox1.Text += "\n";
                        richTextBox1.Text += di.Name + "\n";
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
            richTextBox1.Text += "處理File " + path + "\n";

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

            //richTextBox2.Text += "folder = " + FolederName + ",  name = " + fi.Name + "\n";

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            /*
            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            if (((cb_file_l.Checked == true) && (fi.Length > min_size_mb * 1024 * 1024)) || (cb_file_l.Checked == false))
            {
                if (flag_search_mode == 1)
                {
                    bool res;
                    res = fi.FullName.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        return;
                    else
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
                    if (cb_generate_text.Checked == true)
                    {
                        richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                            fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
                    }
                }
                else
                {
                    if (cb_generate_text.Checked == true)
                    {
                        richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                    }
                }

                //richTextBox1.Text += fi.Directory + "\n";
                //richTextBox1.Text += fi.DirectoryName + "\n";
            */

            //過濾掉檔名的一些字 用以做比較用
            string shortname = fi.Name;
            string[] remove_word = new string[] { "BCP", "pc", "-", "-", "-", "-", "-" };
            foreach (string r in remove_word)
            {
                shortname = shortname.Replace(r, "");
            }

            //只取前7字
            if (shortname.Length > 7)
                shortname = shortname.Substring(0, 7);

            //一律轉小寫
            shortname = shortname.ToLower();

            //richTextBox1.Text += "fname = " + fi.FullName + "\n";
            //richTextBox1.Text += "dname = " + fi.DirectoryName + "\n";

            //把資料放進 List<MyFileInfo> fileinfos 中
            fileinfos.Add(new MyFileInfo(fi.Name, fi.FullName, shortname, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));
        }

        void show_file_info()  //轉出一層
        {
            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });


            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料a\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料c\n";

            if (rb_sort0.Checked == true)
            {
                richTextBox1.Text += "依檔名排序\n";
            }
            else if (rb_sort0.Checked == true)
            {
                richTextBox1.Text += "依檔案大小排序\n";
            }
            else if (rb_sort0.Checked == true)
            {
                richTextBox1.Text += "依檔案日期排序\n";
            }
            else
            {
                richTextBox1.Text += "依 其他 排序\n";
            }

            string directory_old = string.Empty;
            for (int i = 0; i < fileinfos.Count; i++)
            {
                //debug mesg
                //richTextBox1.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                if (fileinfos[i].filepath != directory_old)
                {
                    directory_old = fileinfos[i].filepath;
                    richTextBox1.Text += directory_old + "\n";
                }


                if (cb_show0.Checked == true)
                {
                    richTextBox1.Text += "\t" + fileinfos[i].filename;
                }
                if (cb_show1.Checked == true)
                {
                    richTextBox1.Text += "\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                }
                if (cb_show2.Checked == true)
                {
                    richTextBox1.Text += "\t" + fileinfos[i].filecreationtime;
                }

                richTextBox1.Text += "\tfname: " + fileinfos[i].fullfilename;
                richTextBox1.Text += "\tdname: " + fileinfos[i].filepath;
                richTextBox1.Text += "\tsn: " + fileinfos[i].shortfilename;
                richTextBox1.Text += "\tpath: " + fileinfos[i].filepath;
                richTextBox1.Text += "\text: " + fileinfos[i].fileextension;


                richTextBox1.Text += "\n";

                /*
                                    bool res;
                                    res = i1.Name.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
                                    if (res == false)
                                        continue;
                                    else
                                    {
                                        richTextBox1.Text += "aaaa get file : " + i1.Name + "\n";
                                    }
                */


            }
        }

        void show_match_files()
        {
            if (fileinfos_match.Count == 0)
            {
                richTextBox1.Text += "無資料b\n";
                return;
            }
            else
            {
                richTextBox1.Text += "找到 " + fileinfos_match.Count.ToString() + " 筆資料b\n";
            }
            listView1.Clear();

            listView1.Columns.Add("檔名", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 80, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 180, HorizontalAlignment.Left);
            listView1.Visible = true;

            for (int i = 0; i < fileinfos_match.Count; i++)
            {
                //ListViewItem i1 = new ListViewItem(fileinfos_match[i].filename);
                ListViewItem i1;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1d = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1e = new ListViewItem.ListViewSubItem();

                string item = string.Empty; //useless
                string items = string.Empty;
                string itema = string.Empty;
                string itemb = string.Empty;
                string itemc = string.Empty;
                string itemd = string.Empty;
                string iteme = string.Empty;

                //debug mesg
                //richTextBox2.Text += "i = " + i.ToString() + ", filename : " + fileinfos_match[i].filepath + "\\" + fileinfos_match[i].filename + "\n";

                MediaFile f = new MediaFile(fileinfos_match[i].filepath + "\\" + fileinfos_match[i].filename);

                richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                richTextBox1.Text += "  Extension: " + f.Extension + "\n";

                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    //richTextBox2.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    //richTextBox2.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    //richTextBox2.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                    //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                    item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                    itema = fileinfos_match[i].filename;
                    itemb = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos_match[i].filesize));
                    itemc = fileinfos_match[i].filepath;
                    itemd = fileinfos_match[i].fileextension;
                    iteme = fileinfos_match[i].filecreationtime.ToString();

                    //i1 = new ListViewItem(fileinfos_match[i].filename);
                    i1 = new ListViewItem(itema);
                    i1.UseItemStyleForSubItems = false;

                    //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                    sub_i1b.Text = itemb;
                    i1.SubItems.Add(sub_i1b);

                    sub_i1c.Text = itemc;
                    i1.SubItems.Add(sub_i1c);
                    //sub_i1a.Text = fileinfos_match[i].filepath;
                    //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                    sub_i1d.Text = itemd;
                    i1.SubItems.Add(sub_i1d);

                    sub_i1e.Text = iteme;
                    i1.SubItems.Add(sub_i1e);

                    //sub_i1a.Text = fi.Length.ToString();
                    //sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos_match[i].filesize));
                    //sub_i1c.Text = itemc;
                    //i1.SubItems.Add(sub_i1c);

                    sub_i1a.ForeColor = System.Drawing.Color.Blue;
                    sub_i1b.ForeColor = System.Drawing.Color.Blue;
                    sub_i1c.ForeColor = System.Drawing.Color.Blue;

                    sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1c.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);


                    listView1.Items.Add(i1);
                    richTextBox1.Text += "A";
                }
                else
                {
                    richTextBox1.Text += "B";
                    //continue;
                }

                
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();

            }

            /*
                        i1 = new ListViewItem(fileinfos_match[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                        //richTextBox2.Text += "xxxxx" + fileinfos_match[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos_match[i].filesize)) + "\n";
                        sub_i1a.Text = fileinfos_match[i].filepath;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fi.Length.ToString();
                        sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos_match[i].filesize));
                        i1.SubItems.Add(sub_i1b);

                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1b.ForeColor = System.Drawing.Color.Blue;

                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    }
                }
                else
                {
                    if (cb_video_only.Checked == true)
                        continue;

                    if (cb_generate_text.Checked == false)
                        continue;

                    i1 = new ListViewItem(fileinfos_match[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
                    sub_i1a.Text = fileinfos_match[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos_match[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = System.Drawing.Color.Blue;
                    sub_i1b.ForeColor = System.Drawing.Color.Blue;

                    sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                }

                if (flag_search_mode == 1)
                {
                    bool res;
                    res = i1.Name.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        continue;
                    else
                    {
                        richTextBox1.Text += "aaaa get file : " + i1.Name + "\n";
                    }
                }
            */




        }

        private void button1_Click(object sender, EventArgs e)
        {
            //從一個資料夾中撈出所有檔案 標準版

            string path = foldername;

            //轉出一層

            fileinfos.Clear();

            //只撈一層的檔案
            total_size = 0;
            total_files = 0;

            string FolederName = path;
            richTextBox1.Text += path + "\n\n";

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
                //ProcessDirectory(path);

                try
                {
                    //richTextBox1.Text += targetDirectory + "\n\n";
                    //DirectoryInfo di = new DirectoryInfo(targetDirectory);
                    //richTextBox1.Text += di.Name + "\n\n";

                    // Process the list of files found in the directory.
                    try
                    {
                        string[] fileEntries = Directory.GetFiles(path);
                        Array.Sort(fileEntries);
                        foreach (string fileName in fileEntries)
                        {
                            ProcessFile(fileName);
                        }
                        //step = 0;
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

                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";

                show_file_info();
            }
            else
            {
                richTextBox1.Text += "非合法路徑或檔案a\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string path = foldername;

            //轉出多層

            fileinfos.Clear();
            total_size = 0;
            total_files = 0;

            richTextBox1.Text += "\n搜尋路徑" + path + "\n";

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

            show_file_info();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_file_info();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料c\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料b\n";

            int len = fileinfos.Count;
            if (len < 2)
                return;

            fileinfos_match.Clear();

            int i;
            int j;
            for (i = 0; i < len; i++)
            {
                for (j = i + 1; j < (len - 1); j++)
                {
                    if (cb_compare0.Checked == true)    //比較真檔名
                    {
                        if (fileinfos[i].filename == fileinfos[j].filename)
                        {
                            richTextBox1.Text += "找到真檔名\n";
                            richTextBox1.Text += fileinfos[i].fullfilename + "\n";
                            richTextBox1.Text += fileinfos[j].fullfilename + "\n";
                            fileinfos_match.Add(fileinfos[i]);
                            fileinfos_match.Add(fileinfos[j]);
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
                        }
                    }



                }
            }

            richTextBox1.Text += "show match files\n";
            show_match_files();
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

        private void button5_Click(object sender, EventArgs e)
        {
            /*
            listView1.Clear();
            listView1.Columns.Add("檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 500, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);

            // + 影片格式

            listView1.Visible = true;
            */

            string filename = @"C:\______test_files\__RW\_avi\i2c.avi";

            MediaFile f = new MediaFile(filename);

            richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
            richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
            richTextBox1.Text += "  Extension: " + f.Extension + "\n";




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
            string fullname;

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            richTextBox2.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox2.Text += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
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

            string video_player_path = @"D:\___backup\PotPlayer\PotPlayerMini64.exe";

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox2.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
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
            richTextBox2.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox2.Text += listView1.SelectedItems[i].SubItems[2].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }
            richTextBox2.Text += "開啟\n";

            int selNdx;
            string all_filename = string.Empty;

            if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
            {
                richTextBox2.Text += "無檔案\n";
                return;
            }

            string video_player_path = @"D:\___backup\PotPlayer\PotPlayerMini64.exe";

            //richTextBox2.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
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
            using (Process p = new Process())
            {
                p.StartInfo = pInfo;
                p.Start();
            }
            */
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            richTextBox2.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";


        }
    }
}
