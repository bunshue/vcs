using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;    //for FileInfo DirectoryInfo
using System.Diagnostics;
using System.Globalization; //for CultureInfo

using MediaInfoNET;

namespace vcs_DrAP
{
    public partial class Form1 : Form
    {
        void update_setup_file()
        {
            richTextBox2.Text += "update_setup_file ST\n";
            richTextBox2.Text += "length of old_search_path = " + old_search_path.Count.ToString() + "\n";

            StreamWriter sw = System.IO.File.CreateText(drap_setup_filename);
            string content = "";
            //定義系統版本
            Version ver = Environment.OSVersion.Version;
            //Major主版本號,Minor副版本號
            if (ver.Major == 6 && ver.Minor == 1)
            {
                //Windows7
                content += "\"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini.exe\"\n";
            }
            else
            {
                //Windows10
                content += "\"C:\\Program Files (x86)\\DAUM\\PotPlayer\\PotPlayerMini.exe\"\n";
            }
            content += "\"C:\\Program Files (x86)\\AIMP\\AIMP.exe\"\n";
            content += "\"C:\\Program Files (x86)\\ACDSee32\\ACDSee32.exe\"\n";
            content += "\"C:\\Program Files (x86)\\IDM Computer Solutions\\UltraEdit-32\\uedit32.exe\"\n";
            content += SelectedLanguage.ToString() + "\n";

            //Major主版本號,Minor副版本號
            if (ver.Major == 6 && ver.Minor == 1)
            {
                //Windows7
                video_player_path = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
            }
            else
            {
                //Windows10
                video_player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
            }
            audio_player_path = @"C:\Program Files (x86)\AIMP\AIMP.exe";
            picture_viewer_path = @"C:\Program Files (x86)\ACDSee32\ACDSee32.exe";
            text_editor_path = @"C:\Program Files (x86)\IDM Computer Solutions\UltraEdit-32\uedit32.exe";

            if (old_search_path.Count == 0)
            {
                content += "C:\\______test_files\n";
                old_search_path.Add("C:\\______test_files");
            }
            else
            {
                foreach (string sss in old_search_path)
                {
                    richTextBox2.Text += sss + "\n";
                    content += sss + "\n";
                }
            }
            content += "\n";

            sw.WriteLine(content, Encoding.UTF8);
            sw.Close();

        }

        void Read_Setup_File()
        {
            int i;
            if (System.IO.File.Exists(drap_setup_filename) == false)
            {
                richTextBox2.Text += "檔案 " + drap_setup_filename + " 不存在，製作一個。\n";
                update_setup_file();
            }
            else
            {
                richTextBox2.Text += "檔案 " + drap_setup_filename + " 存在, 開啟，並讀入設定\n";
                string line;
                StreamReader sr = new StreamReader(drap_setup_filename, Encoding.UTF8);
                i = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    line = sr.ReadLine().Trim();            // 讀取文字到 line 變數
                    richTextBox2.Text += "第 " + i.ToString() + " 行資料 : " + line + "\n";
                    switch (i)
                    {
                        case 0:
                            video_player_path = line;
                            break;
                        case 1:
                            audio_player_path = line;
                            break;
                        case 2:
                            picture_viewer_path = line;
                            break;
                        case 3:
                            text_editor_path = line;
                            break;
                        case 4:
                            SelectedLanguage = int.Parse(line);
                            break;
                        case 5:
                            search_path = line;
                            break;
                        default:
                            break;
                    }
                    if (i >= 5)
                    {
                        if (line.Length > 0)
                        {
                            richTextBox2.Text += "加入路徑 : " + line + "\n";
                            old_search_path.Add(line);
                        }
                        else
                        {
                            richTextBox2.Text += "空行\n";
                        }
                    }
                    i++;
                }
                sr.Close();
            }
        }

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            Read_Setup_File();
        }

        private const int FUNCTION_NONE = 0x00;         //無
        private const int FUNCTION_LIST_ONE = 0x01;     //轉出一層
        private const int FUNCTION_LIST = 0x02;         //轉出
        private const int FUNCTION_FIND_SAME_FILE = 0x03;    //找同檔
        private const int FUNCTION_FIND_SIMILAR_FILE = 0x04; //找可能相同檔案
        private const int FUNCTION_FIND_SMALL_FOLDER = 0x05;   //找小資料夾
        private const int FUNCTION_FIND_BIG_FILE = 0x06;   //找大檔案
        private const int FUNCTION_SEARCH = 0x07;       //搜尋

        private const int FUNCTION_TEST = 0xFF;         //測試

        int flag_function = FUNCTION_NONE;

        string path = String.Empty;
        int filetype = 0;
        string filetype2 = String.Empty;
        Int64 total_size = 0;
        Int64 total_files = 0;
        Int64 total_folders = 0;
        Int64 folder_size = 0;
        Int64 folder_files = 0;
        int min_size_mb = 0;
        int step = 0;
        int flag_search_mode = 0;
        int flag_search_done = 0;
        int flag_search_vcs_pattern = 0;
        int SelectedLanguage = 0;
        string drap_setup_filename = "drap_setup.ini";
        string FolederName;

        string video_player_path = String.Empty;
        string audio_player_path = String.Empty;
        string picture_viewer_path = String.Empty;
        string text_editor_path = String.Empty;
        string search_path = String.Empty;

        private const int SEARCH_MODE_VCS = 0x00;	//search vcs code
        private const int SEARCH_MODE_PYTHON = 0x01;	//search python code
        int search_mode = SEARCH_MODE_VCS;

        List<String> old_search_path = new List<String>();

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

        public class MyFolderInfo
        {
            public string foldername;
            public string folderpath;
            public long foldersize;
            public DateTime foldercreationtime;
            public MyFolderInfo(string n, string p, long s, DateTime c)
            {
                this.foldername = n;
                this.folderpath = p;
                this.foldersize = s;
                this.foldercreationtime = c;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態

        List<MyFileInfo> fileinfos = new List<MyFileInfo>();
        List<MyFolderInfo> folderinfos = new List<MyFolderInfo>();

        private void button2_Click(object sender, EventArgs e)
        {
            flag_search_mode = 0;
            flag_search_done = 0;
            flag_search_vcs_pattern = 0;

            fileinfos.Clear();
            if (path != String.Empty)
            {
                //只撈一層的所有檔案
                foreach (string fname in System.IO.Directory.GetFileSystemEntries(path))
                {
                    richTextBox1.Text += fname + "\n";
                }
            }

            //只撈一層的檔案
            total_size = 0;
            total_files = 0;

            if (path == String.Empty)
                path = search_path;
                //path = @"D:\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";

            FolederName = path;
            richTextBox1.Text += path + "\n\n";

            if (System.IO.File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(path, 0);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(path))
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
                            ProcessFile(fileName, step);
                        }
                        step = 0;
                    }
                    catch (UnauthorizedAccessException ex)
                    {
                        richTextBox1.Text += ex.Message + "\n";
                        //MessageBox.Show(ex.Message);
                        /*
                        FileAttributes attr = (new FileInfo(filePath)).Attributes;
                        Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                        if ((attr & FileAttributes.ReadOnly) > 0)
                            Console.Write("The file is read-only.");
                        */
                    }
                }
                catch (IOException ex)
                {
                    richTextBox1.Text += "IOException, " + ex.GetType().Name + "\n";
                    /*
                    Console.WriteLine(
                        "{0}: The write operation could not " +
                        "be performed because the specified " +
                        "part of the file is locked.",
                        e.GetType().Name);
                    */
                }

                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                show_file_info();
                flag_search_done = 1;
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
                flag_search_done = 0;
            }     


        }

        private void button8_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = search_path;  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                path = folderBrowserDialog1.SelectedPath;
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
            flag_search_done = 0;
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
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
                        ProcessFile(fileName, step);
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
                        if (cb_file_l.Checked == false)
                        {
                            richTextBox1.Text += "\n";
                            //for (int i = 0; i < step * 2; i++)
                            //richTextBox1.Text += " ";
                            richTextBox1.Text += di.Name + "\n";
                        }
                        step++;
                        FolederName = subdirectory;
                        ProcessDirectory(subdirectory);
                    }
                    step = 0;
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                    //MessageBox.Show(ex.Message);
                    /*
                    FileAttributes attr = (new FileInfo(filePath)).Attributes;
                    Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                    if ((attr & FileAttributes.ReadOnly) > 0)
                        Console.Write("The file is read-only.");
                    */
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
                /*
                Console.WriteLine(
                    "{0}: The write operation could not " +
                    "be performed because the specified " +
                    "part of the file is locked.",
                    e.GetType().Name);
                */
            }
        }

        // Insert logic for processing found files here.
        public void ProcessFile(string path, int step)
        {
            //richTextBox1.Text += path + "\n";

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

            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            if (((cb_file_l.Checked == true) && (fi.Length > min_size_mb * 1024 * 1024)) || (cb_file_l.Checked == false))
            {
                if (flag_search_mode == 1)
                {
                    bool res;
                    res = fi.FullName.ToLower().Replace(" ", "").Contains(textBox2.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        return;
                    else
                    {
                        richTextBox1.Text += "get file : " + fi.FullName + "\n";
                    }
                }

                for (int i = 0; i < step * 2; i++)
                    richTextBox1.Text += " ";
                //richTextBox1.Text += fi.Name + " len = " + fi.Length.ToString() + "\n";
                //richTextBox1.Text += filename + "\n";
                //richTextBox1.Text += fi.Name + "\n";
                //richTextBox1.Text += fi.Name + " \t\t " + ByteConversionGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

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
                    if (checkBox6.Checked)
                    {
                        richTextBox1.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                            fi.FullName, ByteConversionGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";
                    }
                }
                else
                {
                    if (checkBox6.Checked)
                    {
                        richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                    }
                }

                //richTextBox1.Text += fi.Directory + "\n";
                //richTextBox1.Text += fi.DirectoryName + "\n";

                /*
                ListViewItem i1 = new ListViewItem(fi.FullName);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fi.Length));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
                */

                //或許某些時候不需要
                fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
            }
        }

        void show_file_info()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (checkBox4.Checked == true)
            {
                listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
            }

            richTextBox2.Text += "fileinfos.Count = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < fileinfos.Count; i++)
            {
                //ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                ListViewItem i1;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();

                if (checkBox4.Checked == true)
                {
                    //debug mesg
                    //richTextBox2.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";

                    MediaFile f = new MediaFile(fileinfos[i].filepath + "\\" + fileinfos[i].filename);

                    //richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                    //richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                    //richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                    if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                    {
                        int w = f.Video[0].Width;
                        int h = f.Video[0].Height;
                        //richTextBox2.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                        //richTextBox2.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                        //richTextBox2.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                        //fi.FullName, ByteConversionGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                        if (cb_video_s.Checked == true)
                        {
                            if (h > 480)
                                continue;
                        }

                        string item = string.Empty;
                        string itema = string.Empty;
                        string itemb = string.Empty;
                        string itemc = string.Empty;

                        item = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                        itema = fileinfos[i].filename;
                        itemb = fileinfos[i].filepath;
                        itemc = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));

                        //i1 = new ListViewItem(fileinfos[i].filename);
                        i1 = new ListViewItem(item);
                        i1.UseItemStyleForSubItems = false;

                        //sub_i10.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                        sub_i1a.Text = itema;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fileinfos[i].filepath;
                        //sub_i1a.Text = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";
                        sub_i1b.Text = itemb;
                        i1.SubItems.Add(sub_i1b);

                        //sub_i1a.Text = fi.Length.ToString();
                        //sub_i1b.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
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
                    {
                        if (checkBox6.Checked == false)
                            continue;

                        i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                        //richTextBox2.Text += "xxxxx" + fileinfos[i].filename + "\t\t" + ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        sub_i1a.Text = fileinfos[i].filepath;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fi.Length.ToString();
                        sub_i1b.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        i1.SubItems.Add(sub_i1b);

                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1b.ForeColor = System.Drawing.Color.Blue;

                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                        sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    }







                }
                else
                {
                    if (checkBox6.Checked == false)
                        continue;

                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
                    sub_i1a.Text = fileinfos[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                    i1.SubItems.Add(sub_i1b);

                    sub_i1a.ForeColor = System.Drawing.Color.Blue;
                    sub_i1b.ForeColor = System.Drawing.Color.Blue;

                    sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                    sub_i1b.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                }

                if (flag_search_mode == 1)
                {
                    bool res;
                    res = i1.Name.ToLower().Replace(" ", "").Contains(textBox2.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        continue;
                    else
                    {
                        richTextBox1.Text += "aaaa get file : " + i1.Name + "\n";
                    }
                }

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        void show_file_info2()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (checkBox4.Checked == true)
            {
                listView1.Columns.Add("影片2", 100, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
            }

            richTextBox2.Text += "cnt = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                bool res;
                res = fileinfos[i].filename.ToLower().Replace(" ", "").Contains(textBox2.Text.ToLower().Replace("-", ""));
                if (res == false)
                    continue;
                else
                {
                    richTextBox2.Text += "get file : " + fileinfos[i].filename + "\n";
                }

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();

                sub_i1a.Text = fileinfos[i].filepath;
                i1.SubItems.Add(sub_i1a);
                //sub_i1a.Text = fi.Length.ToString();
                sub_i1b.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
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

        void show_file_info3()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("檔名", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            richTextBox2.Text += "fileinfos.Count = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();

                sub_i1a.Text = fileinfos[i].filepath;
                i1.SubItems.Add(sub_i1a);

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1b.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
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


        void show_file_info4()
        {
            richTextBox1.Text += "show_file_info4 ST\n";

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("最底層資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 250, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 250, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

                //排序 由大到小  在return的地方多個負號       先不排序
                //fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
            }

            for (int i = 0; i < folderinfos.Count; i++)
            {
                //richTextBox1.Text += "name : " + folderinfos[i].foldername + " path : " + folderinfos[i].folderpath + " size : " + folderinfos[i].filesize.ToString() + "\n";

                ListViewItem i1 = new ListViewItem(folderinfos[i].foldername);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();

                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(folderinfos[i].foldersize));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;
                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                sub_i1b.Text = folderinfos[i].foldercreationtime.ToString();
                i1.SubItems.Add(sub_i1b);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "開始計時\n";
            this.Text = "DrAP";
            // Create stopwatch
            Stopwatch stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            flag_search_mode = 0;
            flag_search_done = 0;
            flag_search_vcs_pattern = 0;

            fileinfos.Clear();
            /*  無法依子目錄排序 廢棄
            if (path == String.Empty)
                path = search_path;

            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(path, filetype2, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                //richTextBox1.Text += filename + "\n";
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += fi.Name + "\n";
            }
            */

            total_size = 0;
            total_files = 0;

            if (listBox1.Items.Count == 0)
            {
                richTextBox2.Text += "未選擇資料夾\n";
                return;
            }

            richTextBox2.Text += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                path = listBox1.Items[i].ToString();

                richTextBox2.Text += "\n搜尋路徑" + path + "\n";

                if (System.IO.File.Exists(path))
                {
                    // This path is a file
                    richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                    ProcessFile(path, 0);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                    flag_search_done = 1;
                }
                else if (Directory.Exists(path))
                {
                    // This path is a directory
                    FolederName = path;
                    ProcessDirectory(path);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                    if (flag_search_mode == 1)
                        show_file_info2();
                    else
                        show_file_info();
                    flag_search_done = 1;
                }
                else
                {
                    //Console.WriteLine("{0} is not a valid file or directory.", path);
                    richTextBox1.Text += "非合法路徑或檔案\n";
                    flag_search_done = 0;
                }
            }

            // Stop timing
            stopwatch.Stop();
            // Write result
            richTextBox2.Text += "停止計時\t";
            richTextBox2.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
            this.Text = "DrAP (轉出時間 : " + (stopwatch.ElapsedMilliseconds/1000).ToString() + " 秒)";
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            filetype = comboBox1.SelectedIndex;
            switch (filetype)
            { 
                case 0:
                    filetype2 = "*.*";
                    break;
                case 1:
                    filetype2 = "*.mp3";
                    break;
                case 2:
                    filetype2 = "*.txt";
                    break;
                default:
                    filetype2 = "*.*";
                    break;
            }
            richTextBox2.Text += "change file type to " + filetype2 + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            fileinfos.Clear();
            listView1.Clear();
            richTextBox1.Clear();
            richTextBox2.Clear();
            flag_search_vcs_pattern = 0;
        }

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(KSize / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (KSize / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(KSize / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (KSize / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(KSize / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (KSize / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(KSize / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return KSize.ToString() + " Byte";//顯示Byte值
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx;
            string fullname;

            if (flag_function == FUNCTION_FIND_SMALL_FOLDER)
            {
                selNdx = listView1.SelectedIndices[0];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
                richTextBox2.Text += "你選擇了資料夾:\t" + listView1.Items[selNdx].Text + "\n";

                fullname = listView1.Items[selNdx].Text;

                richTextBox1.Text += "開啟路徑: " + fullname + "\n";
                /* old
                //開啟檔案總管
                if (Directory.GetParent(fullname) == null)
                    System.Diagnostics.Process.Start(fullname);             //若是跟目錄 不要擷取其父目錄的路徑
                else
                    System.Diagnostics.Process.Start(Directory.GetParent(fullname).ToString()); //GetParent 擷取其父目錄的路徑
                */
                //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
                string file = @"C:\Windows\explorer.exe";
                string argument = @"/select, " + fullname;
                System.Diagnostics.Process.Start(file, argument);

                return;
            }
            else
            {



            }



            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            //richTextBox2.Text += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            //richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";

            richTextBox2.Text += "你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";


            fullname = listView1.Items[selNdx].SubItems[2].Text + "\\" + listView1.Items[selNdx].SubItems[1].Text;

            if (flag_search_vcs_pattern == 0)
            {
                richTextBox2.Text += "11111 fullname = " + fullname + "\n";

                FileInfo fi = new FileInfo(fullname);

                richTextBox2.Text += "fullname = " + fullname + ",  ext = " + fi.Extension + "\n";

                if (fi.Extension == ".txt")
                {
                    System.Diagnostics.Process.Start("uedit32.exe", fullname);
                }
                else
                {
                    richTextBox2.Text += "video_player_path = " + video_player_path + "\n";
                    richTextBox2.Text += "fullname = " + fullname + "\n";
                    System.Diagnostics.Process.Start(video_player_path, fullname);
                }
            }
            else
            {
                   System.Diagnostics.Process.Start("uedit32.exe", fullname);
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            /*
            richTextBox2.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox2.Text += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }
            richTextBox2.Text += "開啟\n";
            */

            int selNdx;
            string all_filename = string.Empty;

            if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
            {
                richTextBox2.Text += "無檔案\n";
                return;
            }

            //richTextBox2.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox2.Text += listView1.Items[selNdx].Text + "\n";
                all_filename += " \"" + listView1.Items[selNdx].SubItems[2].Text + "\\" + listView1.Items[selNdx].SubItems[1].Text + "\"";
            }

            //指定應用程式路徑
            string target = String.Empty;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二

            if (flag_search_vcs_pattern == 0)
            {
                target = video_player_path;
            }
            else
            {
                target = text_editor_path;
            }

            if (flag_search_vcs_pattern == 0)
            {
                ProcessStartInfo pInfo = new ProcessStartInfo(target);
                pInfo.Arguments = all_filename;

                /* debug mesg
                richTextBox2.Text += "target : " + target + "\n";
                richTextBox2.Text += "all_filename : " + all_filename + "\n";
                */

                using (Process p = new Process())
                {
                    p.StartInfo = pInfo;
                    p.Start();
                }
            }
            else
            {
                System.Diagnostics.Process.Start("uedit32.exe", all_filename);
            }
        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox2.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

            if (e.KeyCode == Keys.A)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    //richTextBox2.Text += "Ctrl + A\n";
                    //richTextBox2.Text += "共有項目" + listView1.Items.Count.ToString() + " 個\n";

                    for (int i = 0; i < listView1.Items.Count; i++)
                    {
                        //richTextBox2.Text += listView1.Items[i] + "\n";
                        listView1.Items[i].Selected = true;
                    }
                }
            }

            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 button9_Click
                button9_Click(sender, e);
            }

            if (e.KeyCode == Keys.F2)
            {
                richTextBox2.Text += "你按了F2\n";

                if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
                    return;

                int selNdx = listView1.SelectedIndices[0];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
                richTextBox2.Text += "你選擇了" + listView1.Items[selNdx].Text + "\t內容為：\n";

                //ListViewItem t = listView1.Items[selNdx]; //相同寫法
                //richTextBox1.Text += t.Text + "\t" + t.SubItems[1].Text + "\t" + t.SubItems[2].Text + "\n";
                richTextBox2.Text += listView1.Items[selNdx].Text + "\t" + listView1.Items[selNdx].SubItems[1].Text + "\t" + listView1.Items[selNdx].SubItems[2].Text + "\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";






            }
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (this.listView1.Items.Count <= 0)
            {
                richTextBox2.Text += "無內容可複製\n";
                return;
            }

            //C# – 複製資料到剪貼簿
            Clipboard.Clear();

            for (int i = 0; i < listView1.Items.Count; i++)
            {
                //richTextBox2.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\n";

                //C# – 複製資料到剪貼簿 累計
                Clipboard.SetDataObject(Clipboard.GetText() + listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\n");      //建議用此
            }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //C# 限制 TextBox只能輸入十進位碼、Backspace、Enter
            // e.KeyChar == (Char)48 ~ 57 -----> 0~9
            // e.KeyChar == (Char)8 -----------> Backspace
            // e.KeyChar == (Char)13-----------> Enter            
            if ((e.KeyChar >= (Char)48 && e.KeyChar <= (Char)57) || (e.KeyChar == (Char)8))
            {
                e.Handled = false;
            }
            else if (e.KeyChar == (Char)13)
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }

            /*
            //C# 限制textbox只能輸入數字
            if(e.KeyChar.CompareTo('0')<0 || e.KeyChar.CompareTo('9')>0) //比較輸入值的範圍是否超出數字
                e.Handled = true;// Handled 為是否鎖住輸入
            */
        }

        private void button4_Click(object sender, EventArgs e)
        {
            button9.BackgroundImage = vcs_DrAP.Properties.Resources.potplayer;
            min_size_mb = 0;
            bool conversionSuccessful = int.TryParse(textBox1.Text, out min_size_mb);    //out為必須
            if (conversionSuccessful == true)
            {
                //richTextBox1.Text += "容量限制： " + min_size_mb.ToString() + " MB\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
                richTextBox1.Text += "取得容量限制數字失敗\n";
                return;
            }
            flag_function = FUNCTION_FIND_BIG_FILE;
            find_and_show_big_files();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";

            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox2.Text += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }

            richTextBox2.Text += "刪除\n";

            for (int i = listView1.SelectedIndices.Count - 1; i >= 0; i--)
            {
                richTextBox2.Text += "刪除檔案: " + listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";

                richTextBox1.Text += "目前不支援直接刪除檔案\n";
                /*  直接刪除檔案
                File.SetAttributes(listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text, FileAttributes.Normal);
                File.Delete(listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text);
                */
                listView1.SelectedItems[i].Remove();
            }
        }

        void Setup_DrAP_Form()
        {
            this.FormBorderStyle = FormBorderStyle.FixedSingle;
            this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            //設定執行後的表單大小
            this.Size = new Size(1920, 1080);
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);
            this.listBox1.BorderStyle = BorderStyle.Fixed3D;
            this.listView1.Size = new System.Drawing.Size(1900, 500);

            this.richTextBox2.Size = new System.Drawing.Size(594, 388);
            button20.Location = new Point(richTextBox2.Location.X + richTextBox2.Width - button20.Width, richTextBox2.Location.Y);

            richTextBox2.Text += "Form1 W1 " + this.Width.ToString() + "\n";
            richTextBox2.Text += "Form1 W2 " + this.ClientSize.Width.ToString() + "\n";

            richTextBox2.Text += "lsstview1 x_st = " + this.listView1.Location.X.ToString() + "\n";
            richTextBox2.Text += "lsstview1 y_st = " + this.listView1.Location.Y.ToString() + "\n";


            //this.richTextBox2.Location = new Point(1600, 600);

            if (checkBox7.Checked == false)
            {
                richTextBox2.Visible = false;
                button20.Visible = false;
            }






        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Setup_DrAP_Form();

            //search_path = @"D:\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";
            //this.listBox1.Items.Add(search_path);
            // 可用foreach 取出List 裡的值
            //richTextBox2.Text += "\n可用foreach 取出List 裡的值\n";
            this.listBox1.Items.Clear();
            foreach (string sss in old_search_path)
            {
                //richTextBox1.Text += sss + "\n";
                this.listBox1.Items.Add(sss);
            }

            this.listView1.GridLines = true;


            //C# 提示視窗 ToolTip 
            //ToolTip：當游標停滯在某個控制項時，就會跳出一個小視窗
            ToolTip toolTip1 = new ToolTip();
            //SetToolTip：定義控制項會跳出提示的文字
            toolTip1.SetToolTip(button14, "Add Directory");
            toolTip1.SetToolTip(button15, "Delete Directory");
            toolTip1.SetToolTip(button16, "Delete All Directory");

            //以下為提示視窗的設定(通常會設定的部分)
            //ToolTipIcon：設定顯示在提示視窗的圖示類型。
            toolTip1.ToolTipIcon = ToolTipIcon.Info;
            //ForeColor：前景顏色
            toolTip1.ForeColor = Color.Blue;
            //BackColor：背景顏色
            toolTip1.BackColor = Color.Gray;
            //AutoPopDelay：當游標停滯在控制項，顯示提示視窗的時間。(以毫秒為單位)
            toolTip1.AutoPopDelay = 5000;
            //ToolTipTitle：設定提示視窗的標題。
            toolTip1.ToolTipTitle = "提示訊息";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "離開時儲存最後選擇的路徑\n";
            update_setup_file();
            Application.Exit();
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectoryS(string targetDirectory)
        {
            try
            {
                // Process the list of files found in the directory.
                try
                {
                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    Array.Sort(fileEntries);
                    foreach (string fileName in fileEntries)
                    {
                        ProcessFileS(fileName);
                    }

                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    Array.Sort(subdirectoryEntries);
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        ProcessDirectoryS(subdirectory);
                    }
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox2.Text += ex.Message + "\n";
                }
            }
            catch (IOException e)
            {
                richTextBox2.Text += "IOException, " + e.GetType().Name + "\n";
            }
        }

        // Insert logic for processing found files here.
        public void ProcessFileS(string path)
        {
            FileInfo fi = new FileInfo(path);
            //richTextBox2.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            bool res;
            string pattern = string.Empty;// = "Form1.cs";


            if(search_mode == SEARCH_MODE_VCS)
                pattern = "Form1.cs";
            else if (search_mode == SEARCH_MODE_PYTHON)
                pattern = "py";
            else
                pattern = "Form1.cs";

            res = fi.FullName.ToLower().Replace(" ", "").Contains(pattern.ToLower());

            if (res == true)
            {
                //richTextBox2.Text += fi.FullName + "\n";
                StreamReader sr = new StreamReader(fi.FullName, Encoding.UTF8);

                int flag_pattern_match = 0;
                int i = 0;
                String line;

                //寫法一
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine();            // 讀取文字到 line 變數
                    res = line.ToLower().Replace(" ", "").Contains(textBox3.Text.ToLower().Replace(" ", ""));
                    if (res == true)
                    {
                        //richTextBox2.Text += "第" + i.ToString() + "行： " + line + "\n";
                        richTextBox2.Text += line + "\n";
                        flag_pattern_match = 1;
                    }
                }
                if (flag_pattern_match == 1)
                {
                    richTextBox2.Text += fi.FullName + "\n";
                    fileinfos.Add(new MyFileInfo(fi.Name, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));
                }

                sr.Close();


            }
            else
            {
                return;
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            button9.BackgroundImage = vcs_DrAP.Properties.Resources.ultraedit;
            flag_function = FUNCTION_SEARCH;
            search_mode = SEARCH_MODE_VCS;
            if (textBox3.Text == "")
            {
                richTextBox2.Text += "未輸入搜尋內容\n";
                return;
            }

            fileinfos.Clear();

            string path = @"D:\___source_code\_git\part1\vcs\_2.vcs";

            if (path == String.Empty)
                path = search_path;

            richTextBox1.Text += "資料夾: " + path + "\n\n";
            if (System.IO.File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFileS(path);
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessDirectoryS(path);
            }
            show_file_info3();
            flag_search_vcs_pattern = 1;
            return;
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            //改用KeyDown
            /*
            if (e.KeyChar == (Char)13)      //Enter
            {
                button13_Click(sender, e);
            }
            */
        }

        private void richTextBox2_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox顯示訊息自動捲動 顯示最後一行
            richTextBox2.SelectionStart = richTextBox2.TextLength;
            richTextBox2.ScrollToCaret();
        }

        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            //RichTextBox顯示訊息自動捲動 顯示最後一行
            richTextBox1.SelectionStart = richTextBox1.TextLength;
            richTextBox1.ScrollToCaret();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (checkBox4.Checked == true)
            {
                listView1.Columns.Add("影片4", 100, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            richTextBox2.Text += "fileinfos.Count = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < (fileinfos.Count - 1); i++)
            {
                for (int j = i + 1; j < fileinfos.Count; j++)
                {
                    if (fileinfos[i].filesize == fileinfos[j].filesize)
                    {
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[i].filename + " 容量 " + ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[j].filename + " 容量 " + ByteConversionGBMBKB(Convert.ToInt64(fileinfos[j].filesize)) + "\n";

                        ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        i1.SubItems.Add(fileinfos[i].filepath);
                        sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
						i1.SubItems.Add(sub_i1a);
                        i1.SubItems.Add(fileinfos[i].fileextension);
                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                        listView1.Items.Add(i1);

                        ListViewItem i2 = new ListViewItem(fileinfos[j].filename);
                        i2.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i2a = new ListViewItem.ListViewSubItem();
                        i2.SubItems.Add(fileinfos[j].filepath);
                        sub_i2a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[j].filesize));
						i2.SubItems.Add(sub_i2a);
                        i2.SubItems.Add(fileinfos[j].fileextension);
                        sub_i2a.ForeColor = System.Drawing.Color.Blue;
                        sub_i2a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                        listView1.Items.Add(i2);





                        //設置ListView最後一行可見
                        //listView1.Items[listView1.Items.Count - 1].EnsureVisible();


                    }

                }

                /*
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                */


            }


        }

        private void button14_Click(object sender, EventArgs e)
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
            flag_search_done = 0;

        }

        private void button15_Click(object sender, EventArgs e)
        {
            listBox1.Items.Remove(listBox1.SelectedItem);
            old_search_path.Remove(folderBrowserDialog1.SelectedPath);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            old_search_path.Clear();
        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void textBox3_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 button13_Click
                button13_Click(sender, e);
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            removeDrawDiskSpace();
        }

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (checkBox4.Checked == true)
            {
                listView1.Columns.Add("影片5", 100, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            richTextBox2.Text += "fileinfos.Count = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < (fileinfos.Count - 1); i++)
            {
                string filename1 = fileinfos[i].filename;
                //richTextBox1.Text += "filename1 : " + fileinfos[i].filename + "\n";

                for (int j = i + 1; j < fileinfos.Count; j++)
                {
                    string filename2 = fileinfos[j].filename;
                    richTextBox1.Text += "filename2 : " + fileinfos[j].filename + "\n";

                    richTextBox1.Text += "str1 = " + filename1.ToLower().Replace(" ", "").Replace("-", "") + "\n";
                    richTextBox1.Text += "str2 = " + filename2.ToLower().Replace(" ", "").Replace("-", "").Substring(0,6) + "\n";


                    bool ret;

                    ret = filename1.ToLower().Replace(" ", "").Replace("-", "").Contains(filename2.ToLower().Replace(" ", "").Replace("-", "").Substring(0,6));
                    if (ret == true)
                    {
                        richTextBox1.Text += "YYYYYYYY\n";
                    }
                    else
                    {
                        richTextBox1.Text += "NNNNNNNNN\n";
                    }




                    if (fileinfos[i].filesize == fileinfos[j].filesize)
                    {
                        /*
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[i].filename + " 容量 " + ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[j].filename + " 容量 " + ByteConversionGBMBKB(Convert.ToInt64(fileinfos[j].filesize)) + "\n";

                        ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        i1.SubItems.Add(fileinfos[i].filepath);
                        sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        i1.SubItems.Add(sub_i1a);
                        i1.SubItems.Add(fileinfos[i].extension);
                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                        listView1.Items.Add(i1);

                        ListViewItem i2 = new ListViewItem(fileinfos[j].filename);
                        i2.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i2a = new ListViewItem.ListViewSubItem();
                        i2.SubItems.Add(fileinfos[j].filepath);
                        sub_i2a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[j].filesize));
                        i2.SubItems.Add(sub_i2a);
                        i2.SubItems.Add(fileinfos[j].extension);
                        sub_i2a.ForeColor = System.Drawing.Color.Blue;
                        sub_i2a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                        listView1.Items.Add(i2);
                        */




                        //設置ListView最後一行可見
                        //listView1.Items[listView1.Items.Count - 1].EnsureVisible();


                    }

                }

                /*
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                */


            }


        }

        private void button17_Click(object sender, EventArgs e)
        {
            min_size_mb = 0;
            bool conversionSuccessful = int.TryParse(textBox4.Text, out min_size_mb);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "容量限制： " + min_size_mb.ToString() + " MB\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
                richTextBox1.Text += "取得容量限制數字失敗\n";
                return;
            }
            richTextBox1.Text += "找小資料夾\n";

            flag_function = FUNCTION_FIND_SMALL_FOLDER;
            folderinfos.Clear();

            total_size = 0;
            total_files = 0;

            path = "C:\\______test_files\\_case1";

            richTextBox2.Text += "\n搜尋路徑 " + path + "\n";

            total_folders = 0;

            if (System.IO.File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile2(path, 0);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                flag_search_done = 1;
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                FolederName = path;
                ProcessDirectory2(path);

                richTextBox1.Text += "\n類型:\t\t檔案資料夾\n";
                richTextBox1.Text += "位置:\t\t" + Directory.GetParent(path) + "\n";
                richTextBox1.Text += "大小:\t\t" + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "(" + total_size.ToString() + "位元組)\n";
                richTextBox1.Text += "包含:\t\t" + total_files.ToString() + "個檔案，" + (total_folders - 1).ToString() + "個資料夾\n";

                DirectoryInfo di = new DirectoryInfo(path);
                richTextBox1.Text += "建立日期:\t" + di.CreationTime.ToString() + "\n\n";

                show_file_info4();
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
                flag_search_done = 0;
            }





        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory2(string targetDirectory)
        {
            try
            {
                //richTextBox1.Text += targetDirectory + "\n\n";
                //DirectoryInfo di = new DirectoryInfo(targetDirectory);
                //richTextBox1.Text += di.Name + "\n\n";

                // Process the list of files found in the directory.
                try
                {
                    total_folders++;
                    richTextBox1.Text += "\n開始處理資料夾 : " + targetDirectory + "\n";

                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    Array.Sort(fileEntries);
                    folder_size = 0;
                    folder_files = 0;
                    foreach (string fileName in fileEntries)
                    {
                        ProcessFile2(fileName, step);
                    }


                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    Array.Sort(subdirectoryEntries);

                    //richTextBox1.Text += "共有 " + subdirectoryEntries.Length.ToString() + " 個子目錄\n";
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        richTextBox1.Text += "dir = " + subdirectory + "\n";
                    }

                    richTextBox1.Text += "資料夾 : " + targetDirectory + " ";
                    richTextBox1.Text += "子目錄數 : " + subdirectoryEntries.Length.ToString() + "\t";
                    richTextBox1.Text += "檔案數 : " + folder_files.ToString() + "\t";
                    richTextBox1.Text += "檔案大小總計 : " + folder_size.ToString() + "\n";
                    if (folder_files == 0)
                    {
                        richTextBox1.Text += "空資料夾 folder_name = " + targetDirectory + "\n";
                    }

                    if (subdirectoryEntries.Length == 0)
                    {
                        richTextBox1.Text += "資料夾 : " + targetDirectory + " 是最底層的資料夾\n";
                        if (folder_size < min_size_mb * 1024 * 1024)
                        {
                            DirectoryInfo di = new DirectoryInfo(targetDirectory);
                            //richTextBox1.Text += "建立日期:\t" + di.CreationTime.ToString() + "\n\n";
                            folderinfos.Add(new MyFolderInfo(targetDirectory, targetDirectory, folder_size, di.CreationTime));
                        }
                    }

                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        if (cb_file_l.Checked == false)
                        {
                            richTextBox1.Text += "xxxxxxxxxxx\n";
                            richTextBox1.Text += "\n";
                            //for (int i = 0; i < step * 2; i++)
                            //richTextBox1.Text += " ";
                            richTextBox1.Text += di.Name + "\n";
                        }
                        step++;
                        FolederName = subdirectory;
                        ProcessDirectory2(subdirectory);
                    }
                    step = 0;
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                    //MessageBox.Show(ex.Message);
                    /*
                    FileAttributes attr = (new FileInfo(filePath)).Attributes;
                    Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                    if ((attr & FileAttributes.ReadOnly) > 0)
                        Console.Write("The file is read-only.");
                    */
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
                /*
                Console.WriteLine(
                    "{0}: The write operation could not " +
                    "be performed because the specified " +
                    "part of the file is locked.",
                    e.GetType().Name);
                */
            }
            richTextBox1.Text += "處理資料夾 : " + targetDirectory + " 結束\n";
            //此目錄狀況


        }

        // Insert logic for processing found files here.
        public void ProcessFile2(string path, int step)
        {
            //richTextBox1.Text += path + "\n";
            FileInfo fi = new FileInfo(path);

            //richTextBox2.Text += "folder = " + FolederName + ",  name = " + fi.Name + "\n";

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

            //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length));


        }

        private void button22_Click(object sender, EventArgs e)
        {
            button9.BackgroundImage = vcs_DrAP.Properties.Resources.ultraedit;
            flag_function = FUNCTION_SEARCH;
            search_mode = SEARCH_MODE_PYTHON;
            if (textBox3.Text == "")
            {
                richTextBox2.Text += "未輸入搜尋內容\n";
                return;
            }

            fileinfos.Clear();

            string path = @"D:\___source_code\_git\part1\vcs\_4.cmpp\_python_test";

            if (path == String.Empty)
                path = search_path;

            richTextBox1.Text += "資料夾: " + path + "\n\n";
            if (System.IO.File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFileS(path);
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessDirectoryS(path);
            }
            show_file_info3();
            flag_search_vcs_pattern = 1;
            return;
        }

        void find_and_show_big_files()
        {
            fileinfos.Clear();

            total_size = 0;
            total_files = 0;

            if (listBox1.Items.Count == 0)
            {
                richTextBox2.Text += "未選擇資料夾\n";
                return;
            }

            if (checkBox3.Checked == true)
            {
                richTextBox2.Text += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
                for (int i = 0; i < listBox1.Items.Count; i++)
                {
                    path = listBox1.Items[i].ToString();

                    //找資料夾所在的硬碟的標籤
                    //richTextBox1.Text += "\n資料夾路徑" + path + "\n";

                    if (System.IO.File.Exists(path))
                    {
                        // This path is a file
                        richTextBox1.Text += "是個檔案\n";
                    }
                    else if (Directory.Exists(path))
                    {
                        // This path is a directory
                        DirectoryInfo d = new DirectoryInfo(path);//輸入檔案夾
                        /*
                        richTextBox1.Text += "Name : " + d.Name + "\n";
                        richTextBox1.Text += "FullName : " + d.FullName + "\n";
                        richTextBox1.Text += "Parent : " + d.Parent + "\n";
                        richTextBox1.Text += "Root : " + d.Root + "\n";
                        */

                        DriveInfo drive = new DriveInfo(d.Root.ToString());

                        if (drive.IsReady == true)
                        {
                            richTextBox1.Text += "\nAP." + drive.VolumeLabel + DateTime.Now.ToString(".yyyy.MMdd.HHmm") + "\n\n";

                            richTextBox1.Text += string.Format("{0,-10}{1,-15}", "磁碟 :", drive.ToString()) + "\n";
                            richTextBox1.Text += string.Format("{0,-10}{1,-15}", "標籤 :", drive.VolumeLabel) + "\n";
                            //richTextBox1.Text += string.Format("{0,-12}{1,-25}", "名稱 :", drive.Name) + "\n";
                            richTextBox1.Text += string.Format("{0,-12}{1,17}{2,-7}{3,10}",
                                "使用空間 :", (drive.TotalSize - drive.AvailableFreeSpace).ToString("N0", CultureInfo.InvariantCulture), " 個位元組", ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace))) + "\n";
                            double percentage = (double)drive.AvailableFreeSpace / (double)drive.TotalSize;
                            richTextBox1.Text += string.Format("{0,-12}{1,17}{2,-7}{3,10}{4,-10}",
                                "可用空間 :", drive.AvailableFreeSpace.ToString("N0", CultureInfo.InvariantCulture), " 個位元組",
                                ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)),
                                " ( " + percentage.ToString("P", CultureInfo.InvariantCulture) + " )")
                                + "\n";
                            richTextBox1.Text += string.Format("{0,-12}{1,17}{2,-7}{3,10}",
                                "磁碟容量 :", drive.TotalSize.ToString("N0", CultureInfo.InvariantCulture), " 個位元組", ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize))) + "\n";

                            /*
                            richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                            richTextBox1.Text += "型態 : " + drive.DriveType + "\n";
                            richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";
                            */
                            drawDiskSpace(drive.AvailableFreeSpace, drive.TotalSize);
                        }
                        else
                        {
                            richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒\n";
                        }
                    }
                    else
                    {
                        //Console.WriteLine("{0} is not a valid file or directory.", path);
                        richTextBox1.Text += "非合法路徑或檔案\n";
                    }
                }
            }
            richTextBox1.Text += "\n";

            richTextBox2.Text += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                path = listBox1.Items[i].ToString();

                richTextBox2.Text += "\n搜尋路徑" + path + "\n";

                if (System.IO.File.Exists(path))
                {
                    // This path is a file
                    richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                    ProcessFile(path, 0);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                }
                else if (Directory.Exists(path))
                {
                    // This path is a directory
                    FolederName = path;
                    ProcessDirectory(path);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";

                    show_file_info();
                }
                else
                {
                    //Console.WriteLine("{0} is not a valid file or directory.", path);
                    richTextBox1.Text += "非合法路徑或檔案\n";
                }
            }
        }

        void save_log_to_local_drive()
        {
            string filename = string.Empty;

            if (checkBox3.Checked == true)
            {
                string hddname = string.Empty;

                richTextBox2.Text += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
                for (int i = 0; i < listBox1.Items.Count; i++)
                {
                    path = listBox1.Items[i].ToString();

                    //找資料夾所在的硬碟的標籤

                    //richTextBox1.Text += "\n資料夾路徑" + path + "\n";

                    if (System.IO.File.Exists(path))
                    {
                        // This path is a file
                        richTextBox1.Text += "是個檔案\n";
                    }
                    else if (Directory.Exists(path))
                    {
                        // This path is a directory
                        DirectoryInfo d = new DirectoryInfo(path);//輸入檔案夾
                        /*
                        richTextBox1.Text += "Name : " + d.Name + "\n";
                        richTextBox1.Text += "FullName : " + d.FullName + "\n";
                        richTextBox1.Text += "Parent : " + d.Parent + "\n";
                        richTextBox1.Text += "Root : " + d.Root + "\n";
                        */

                        DriveInfo drive = new DriveInfo(d.Root.ToString());

                        if (drive.IsReady == true)
                        {
                            hddname = drive.VolumeLabel;
                        }
                        else
                        {
                            richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
                            hddname = "NotReady";
                        }
                    }
                    else
                    {
                        //Console.WriteLine("{0} is not a valid file or directory.", path);
                        richTextBox1.Text += "非合法路徑或檔案\n";
                    }

                }
                filename = "AP." + hddname + DateTime.Now.ToString(".yyyy.MMdd.HHmm") + ".txt";
            }
            else
            {
                filename = "AP." + DateTime.Now.ToString("yyyy.MMdd.HHmm") + ".txt";
            }

            //建立一個檔案
            StreamWriter sw = System.IO.File.CreateText(filename);
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button23_Click(object sender, EventArgs e)
        {
            save_log_to_local_drive();
        }

        private const int WIDTH = 100;
        void drawDiskSpace(long free, long total)
        {
            removeDrawDiskSpace();

            //產出panel, 畫硬碟使用空間占比圖
            Panel pnl = new Panel();
            pnl.Left = 1010;
            pnl.Top = 5;
            pnl.Width = WIDTH;
            pnl.Height = WIDTH;
            pnl.Tag = "dynamic";
            pnl.BackColor = Color.White;
            this.Controls.Add(pnl);

            Graphics g;
            g = pnl.CreateGraphics();
            //Pen PenStyle = new Pen(Color.Black, 1);
            //PenStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            //g.DrawRectangle(PenStyle, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100);

            Brush b;
            long used = total - free;

            int used_angle = (int)(used * 360 / total);
            //richTextBox1.Text += "used_angle = " + used_angle.ToString() + "\n";

            b = new SolidBrush(Color.LightGreen);
            g.FillEllipse(b, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100);

            b = new SolidBrush(Color.Red);
            g.FillPie(b, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100, -180, used_angle);

            b = new SolidBrush(Color.White);
            g.FillEllipse(b, WIDTH / 4, WIDTH / 4, WIDTH / 2, WIDTH / 2);
        }

        //移除按鈕部分,  一趟並不會將所有panel上的button回傳, 所以加入while迴圈, 真是神奇驚訝 
        void removeDrawDiskSpace()
        {
            bool flag_do_remove = true;
            while (flag_do_remove == true)
            {
                bool flag_do_remove_this = false;
                foreach (Control con in this.Controls)
                {
                    //System.String strControlTag = con.Tag.ToString();//获得控件的標籤, 不能用此, 因為不一定有Tag可以ToString
                    if (con.Tag != null)
                    {
                        if (con.Tag.ToString() == "dynamic")
                        {
                            this.Controls.Remove(con);
                            flag_do_remove_this = true;
                        }
                    }
                }
                if (flag_do_remove_this == false)
                    flag_do_remove = false;
            }
        }

        private void checkBox7_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox7.Checked == true)
            {
                richTextBox2.Visible = true;
                button20.Visible = true;
                if (checkBox6.Checked == true)
                {
                    richTextBox1.Size = new Size(1300, 430);

                    button19.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - button19.Width, button19.Location.Y);
                    button23.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - button23.Width, button23.Location.Y);
                }

            }
            else
            {
                richTextBox2.Visible = false;
                button20.Visible = false;

                if (checkBox6.Checked == true)
                {
                    richTextBox1.Size = new Size(listView1.Width, 430);

                    button19.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - button19.Width, button19.Location.Y);
                    button23.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - button23.Width, button23.Location.Y);

                }




            }
        }


    }
}

