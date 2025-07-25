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

namespace vcs_DrAP
{
    public partial class Form1 : Form
    {
        private const int FUNCTION_NONE = 0x00;                     //無
        private const int FUNCTION_SEARCH_ALL_FILES = 0x01;         //轉出
        private const int FUNCTION_SEARCH_ONE_LAYER_FILES = 0x02;   //轉出一層
        private const int FUNCTION_FIND_SAME_FILES = 0x03;          //找同檔
        private const int FUNCTION_FIND_SAME_FILES2 = 0x04;         //找可能相同檔案
        private const int FUNCTION_FIND_SMALL_FOLDERS = 0x05;        //找小資料夾
        private const int FUNCTION_FIND_EMPTY_FOLDERS = 0x06;       //找空資料夾
        private const int FUNCTION_FIND_BIG_FILES = 0x07;           //找大檔案
        private const int FUNCTION_SEARCH_TEXT = 0x08;  //搜尋關鍵字, vcs, python, cuda...
        private const int FUNCTION_TEST = 0xFF;         //測試

        private const int FILETYPE_VIDEO = 0x00;        //影片
        private const int FILETYPE_AUDIO = 0x01;        //音樂
        private const int FILETYPE_ALL = 0x02;          //全部
        private const int FILETYPE_OTHERS = 0xFF;       //其他

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
        string FolederName;

        string video_player_path = String.Empty;
        string audio_player_path = String.Empty;
        string picture_viewer_path = String.Empty;
        string text_editor_path = String.Empty;
        string python_editor_path = String.Empty;
        string winmerge_path = String.Empty;
        string search_path = @"C:\_git\vcs\_2.vcs";
        string specified_search_path = @"C:\_git\vcs\_4.python\__code";
        string default_vcs_path = @"C:\_git\vcs\_2.vcs";
        string default_python_path = @"C:\_git\vcs\_4.python";
        string default_cuda_path = @"C:\_git\vcs\_3.cuda";
        string default_opengl_path = @"C:\_git\vcs\_6.opengl";

        private const int SEARCH_MODE_VCS = 0x00;	    //search vcs code, 搜尋vcs內的關鍵字
        private const int SEARCH_MODE_PYTHON = 0x01;	//search python code, 搜尋python內的關鍵字
        private const int SEARCH_MODE_CUDA = 0x03;	//search cuda code, 搜尋cuda內的關鍵字
        private const int SEARCH_MODE_OPENGL = 0x04;	//search opengl code, 搜尋opengl內的關鍵字

        int search_mode = SEARCH_MODE_VCS;
        bool flag_show_30_message = false;

        List<String> old_search_path = new List<String>();

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態
        List<MyFileInfo> fileinfos = new List<MyFileInfo>();
        List<MyFolderInfo> folderinfos = new List<MyFolderInfo>();

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

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            update_default_setting();

            //search_path = @"D:\vcs\astro\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";
            //this.listBox1.Items.Add(search_path);
            // 可用foreach 取出List 裡的值
            //richTextBox2.Text += "\n可用foreach 取出List 裡的值\n";
            this.listBox1.Items.Clear();
            foreach (string sss in old_search_path)
            {
                richTextBox1.Text += "add " + sss + "\n";
                this.listBox1.Items.Add(sss);
            }

            this.listView1.GridLines = true;

            //C# 提示視窗 ToolTip 
            //ToolTip：當游標停滯在某個控制項時，就會跳出一個小視窗
            ToolTip toolTip1 = new ToolTip();
            //SetToolTip：定義控制項會跳出提示的文字
            toolTip1.SetToolTip(bt_add_dir, "Add Directory");
            toolTip1.SetToolTip(bt_remove_dir, "Remove Directory");
            toolTip1.SetToolTip(bt_clear_dir, "Remove All Directory");

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

        void show_item_location()
        {
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            //設定執行後的表單大小
            this.Size = new Size(1920, 1040);
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);
            this.listBox1.BorderStyle = BorderStyle.Fixed3D;
            this.listView1.Size = new System.Drawing.Size(1900, 500);
            this.richTextBox2.Size = new System.Drawing.Size(594, 388);

            int x_st = 12;
            int y_st = 12;

            listBox1.Location = new Point(x_st, y_st);

            int dx = 10;
            int dy = 25;

            x_st += listBox1.Size.Width + dx;
            bt_add_dir.Location = new Point(x_st, y_st + dy * 0);
            bt_remove_dir.Location = new Point(x_st, y_st + dy * 1);
            bt_clear_dir.Location = new Point(x_st, y_st + dy * 2);

            x_st += bt_add_dir.Size.Width + dx;
            tb_search_text_pattern.Location = new Point(x_st, y_st + dy * 0);

            x_st += tb_search_text_pattern.Size.Width + dx;
            bt_find_big_files.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_find_big_files.Size.Width + dx;
            bt_start_files.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_start_files.Size.Width + dx;
            bt_save_data.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_save_data.Size.Width + dx;
            bt_search_all_files.Location = new Point(x_st, y_st + dy * 0);

            bt_find_same_files.Location = new Point(x_st, y_st + dy * 1);

            x_st += bt_search_all_files.Size.Width + dx;
            bt_search_one_layer_files.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_search_one_layer_files.Size.Width + dx;
            bt_clear_data.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_clear_data.Size.Width + dx;
            bt_copy_data.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_copy_data.Size.Width + dx;
            bt_help.Location = new Point(x_st, y_st + dy * 0);

            x_st += bt_help.Size.Width + dx;
            bt_delete_file.Location = new Point(x_st - 8, y_st + dy * 0);


            x_st = 1000;
            y_st = 15;

            textBox4.Location = new Point(x_st - 10, y_st);
            label3.Location = new Point(x_st + 35, y_st + 8);

            bt_find_empty_folders.Location = new Point(x_st + 55, y_st);
            bt_find_small_folders.Location = new Point(x_st + 55, y_st + 30);
            bt_find_same_files2.Location = new Point(x_st + 55, y_st + 60);

            textBox3.Location = new Point(x_st + 100 + 100 - 26, y_st);
            checkBox7.Location = new Point(x_st + 100 + 100 - 26, y_st + 50 + 6 - 20);
            bt_test1.Location = new Point(x_st + 100 + 100 - 26, y_st + 50 + 10);
            bt_test2.Location = new Point(x_st + 100 + 100 + 40 - 10 - 26, y_st + 50 + 10);
            dx = 85;
            dy = 35;
            cb_option1.Location = new Point(x_st + 100 + 100 + dx * 1 - 50, y_st + dy);
            cb_option2.Location = new Point(x_st + 100 + 100 + dx * 1 - 50, y_st + dy + 17);
            cb_option3.Location = new Point(x_st + 100 + 100 + dx * 1 - 50, y_st + dy + 34);

            x_st = 1318;
            y_st = 6;
            dx = 55;
            dy = 55;

            bt_search_pattern_vcs.Location = new Point(x_st, y_st);
            bt_search_pattern_cuda.Location = new Point(x_st, y_st + dy);
            bt_search_pattern_opengl.Location = new Point(x_st + dx * 1, y_st + dy);

            bt_open_dir2.Location = new Point(x_st + dx * 2, y_st);
            bt_save_file_data.Location = new Point(x_st + dx * 2, y_st + dy);

            bt_compare.Location = new Point(x_st + dx * 3, y_st);

            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Width - bt_clear2.Width, richTextBox2.Location.Y);
            bt_copy_rtb_data.Location = new Point(bt_clear2.Location.X, bt_copy_rtb_data.Location.Y);

            bt_setup.Location = new Point(this.ClientSize.Width - bt_setup.Width, 55);
            bt_clear3.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear3.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear3.Size.Height);

            x_st = 1540;
            y_st = 4;
            groupbox_python.Location = new Point(x_st, y_st);
            groupbox_python.Size = new Size(112, 106);
            groupbox_result.Location = new Point(x_st + 165, y_st);
            groupbox_result.Size = new Size(110, 106);
            lb_search_result1.Location = new Point(10, 25);
            lb_search_result2.Location = new Point(10, 60);
            lb_search_result1.Text = "";
            lb_search_result2.Text = "";

            x_st = 10;
            y_st = 15;
            dx = 100;
            dy = 22;
            rb_python_search0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            rb_python_search1.Location = new Point(x_st + dx * 0, y_st + dy * 1);

            bt_search_pattern_python.Size = new Size(45, 45);
            bt_search_pattern_python.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_edit_python_files.Size = new Size(45, 45);
            bt_edit_python_files.Location = new Point(x_st + dx * 0+50, y_st + dy * 2);

            /*
            richTextBox2.Text += "Form1 W1 " + this.Width.ToString() + "\n";
            richTextBox2.Text += "Form1 W2 " + this.ClientSize.Width.ToString() + "\n";
            richTextBox2.Text += "lsstview1 x_st = " + this.listView1.Location.X.ToString() + "\n";
            richTextBox2.Text += "lsstview1 y_st = " + this.listView1.Location.Y.ToString() + "\n";
            //this.richTextBox2.Location = new Point(1600, 600);
            */

            if (checkBox7.Checked == false)
            {
                richTextBox2.Visible = false;
                bt_clear2.Visible = false;
            }

            if (cb_video_only.Checked == true)
                groupBox_video.Enabled = true;
            else
                groupBox_video.Enabled = false;
            if (cb_file_size.Checked == true)
                groupBox_file.Enabled = true;
            else
                groupBox_file.Enabled = false;

            bt_minimize_setup();
            bt_exit_setup();
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2 - 2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
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
            Properties.Settings.Default.search_path = save_path;
            Properties.Settings.Default.Save();
        }

        private void bt_search_one_layer_files_Click(object sender, EventArgs e)
        {
            //轉出一層
            richTextBox2.Text += "開始計時\n";
            this.Text = "DrAP";

            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

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
            //path = @"D:\vcs\astro\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";

            FolederName = path;
            richTextBox1.Text += path + "\n\n";

            if (System.IO.File.Exists(path) == true)
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(path, 0);
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

                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                show_file_info1();
                flag_search_done = 1;
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案a\n";
                flag_search_done = 0;
            }

            stopwatch.Stop();
            richTextBox2.Text += "停止計時\t";
            richTextBox2.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
            this.Text = "DrAP (轉出時間 : " + (stopwatch.ElapsedMilliseconds / 1000).ToString() + " 秒)";
        }

        private void bt_open_dir_Click(object sender, EventArgs e)
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
                    res = fi.FullName.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
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
                fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
            }
        }

        void show_file_info1()  //轉出一層
        {
            if (cb_video_only.Checked == false)
                return;

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (cb_video_only.Checked == true)
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

            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });
            }

            if (fileinfos.Count == 0)
            {
                richTextBox2.Text += "找不到資料a\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                richTextBox2.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料a\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            for (int i = 0; i < fileinfos.Count; i++)
            {
                //ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                ListViewItem i1;

                ListViewItem.ListViewSubItem sub_i1s = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1c = new ListViewItem.ListViewSubItem();

                string item = string.Empty;
                string items = string.Empty;
                string itema = string.Empty;
                string itemb = string.Empty;
                string itemc = string.Empty;

                if (cb_video_only.Checked == true)
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
                        //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

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
                    }
                    else
                    {
                        if (cb_video_only.Checked == true)
                            continue;

                        if (cb_generate_text.Checked == false)
                            continue;

                        i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                        //richTextBox2.Text += "xxxxx" + fileinfos[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
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
                }
                else
                {
                    if (cb_video_only.Checked == true)
                        continue;

                    if (cb_generate_text.Checked == false)
                        continue;

                    i1 = new ListViewItem(fileinfos[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
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

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        void show_file_info2()  //目前像是都不會用到
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (cb_video_only.Checked == true)
            {
                listView1.Columns.Add("影片2", 100, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名2", 300, HorizontalAlignment.Left);
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

            if (fileinfos.Count == 0)
            {
                richTextBox2.Text += "找不到資料b\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                richTextBox2.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料b\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                bool res;
                res = fileinfos[i].filename.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
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

        void show_file_info3()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            listView1.Columns.Add("檔名3", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (fileinfos.Count == 0)
            {
                richTextBox2.Text += "找不到資料c\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                richTextBox2.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料c\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();

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

        void show_file_info6()
        {
            //找小資料夾

            richTextBox1.Text += "show_file_info6 ST\n";

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

                sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(folderinfos[i].foldersize));
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

        private void bt_search_all_files_Click(object sender, EventArgs e)
        {
            //轉出
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

                if (System.IO.File.Exists(path) == true)
                {
                    // This path is a file
                    richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                    ProcessFile(path, 0);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                    flag_search_done = 1;
                }
                else if (Directory.Exists(path) == true)
                {
                    // This path is a directory
                    FolederName = path;
                    ProcessDirectory(path);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                    if (flag_search_mode == 1)  //不會為1
                    {
                        show_file_info2();  //目前像是都不會用到
                    }
                    else
                    {
                        show_file_info1();
                    }
                    flag_search_done = 1;
                }
                else
                {
                    //Console.WriteLine("{0} is not a valid file or directory.", path);
                    richTextBox1.Text += "非合法路徑或檔案b\n";
                    flag_search_done = 0;
                }
            }

            // Stop timing
            stopwatch.Stop();
            // Write result
            richTextBox2.Text += "停止計時\t";
            richTextBox2.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
            this.Text = "DrAP (轉出時間 : " + (stopwatch.ElapsedMilliseconds / 1000).ToString() + " 秒)";
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            filetype = comboBox1.SelectedIndex;
            switch (filetype)
            {
                case FILETYPE_VIDEO:
                    filetype2 = "*.*";
                    break;
                case FILETYPE_AUDIO:
                    filetype2 = "*.mp3";
                    break;
                case FILETYPE_ALL:
                    filetype2 = "*.*";
                    break;
                default:
                    filetype2 = "*.*";
                    break;
            }
            //richTextBox2.Text += "change file type to " + filetype2 + "\n";
        }

        private void bt_clear_data_Click(object sender, EventArgs e)
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

            if (flag_function == FUNCTION_FIND_BIG_FILES)
            {
                richTextBox2.Text += "a你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;
            }
            else
            {
                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    //搜尋字串模式
                    richTextBox2.Text += "aaaa b1你選擇了檔名1:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
                    richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
                    fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
                }
                else
                {
                    //轉出模式
                    //richTextBox2.Text += "b你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                    //richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                    fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;
                }
            }

            if (flag_search_vcs_pattern == 0)
            {
                FileInfo fi = new FileInfo(fullname);

                //richTextBox2.Text += "fullname = " + fullname + ",  ext = " + fi.Extension + "\n";

                if (fi.Extension == ".txt")
                {
                    //Process.Start(text_editor_path, fullname);
                }
                else
                {
                    richTextBox2.Text += "video_player_path = " + video_player_path + "\n";
                    richTextBox2.Text += "fullname = " + fullname + "\n";

                    if (video_player_path == String.Empty)
                    {
                        //Process.Start(fullname); //使用預設程式開啟
                    }
                    else
                    {
                        //Process.Start(video_player_path, fullname);    //指名播放程式開啟
                    }
                }
            }
            else
            {
                //Process.Start(text_editor_path, fullname);
            }
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx;
            string fullname;

            if (flag_function == FUNCTION_FIND_SMALL_FOLDERS)
            {
                selNdx = listView1.SelectedIndices[0];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox2.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
                richTextBox2.Text += "你選擇了資料夾:\t" + listView1.Items[selNdx].Text + "\n";

                fullname = listView1.Items[selNdx].Text;

                richTextBox1.Text += "開啟路徑: " + fullname + "\n";
                /* old
                //開啟檔案總管
                if (Directory.GetParent(fullname) == null)
                    Process.Start(fullname);             //若是根目錄 不要擷取其父目錄的路徑
                else
                    Process.Start(Directory.GetParent(fullname).ToString()); //GetParent 擷取其父目錄的路徑
                */
                //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
                string file = @"C:\Windows\explorer.exe";
                string argument = @"/select, " + fullname;
                Process.Start(file, argument);

                return;
            }
            else
            {

            }

            selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox2.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            //richTextBox2.Text += "你選擇了檔名:\t" + listView1.Items[selNdx].Text + "\n";
            //richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";

            if (flag_function == FUNCTION_FIND_BIG_FILES)
            {
                //richTextBox2.Text += "a你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                //richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;
            }
            else
            {
                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    //搜尋字串模式
                    richTextBox2.Text += "aaaa b2你選擇了檔名2:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";
                    richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
                    fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
                }
                else
                {
                    //轉出模式
                    //richTextBox2.Text += "b你選擇了檔名:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
                    //richTextBox2.Text += "資料夾:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
                    fullname = listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text;
                }
            }

            if (flag_search_vcs_pattern == 0)
            {
                FileInfo fi = new FileInfo(fullname);

                //richTextBox2.Text += "fullname = " + fullname + ",  ext = " + fi.Extension + "\n";

                if (fi.Extension == ".txt")
                {
                    if (System.IO.File.Exists(text_editor_path) == true)
                    {
                        Process.Start(text_editor_path, fullname);
                    }
                }
                else if (fi.Extension == ".py")
                {
                    if (System.IO.File.Exists(python_editor_path) == true)
                    {
                        Process.Start(python_editor_path, fullname);
                    }
                }
                else
                {
                    richTextBox2.Text += "video_player_path = " + video_player_path + "\n";
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
            }
            else
            {
                //richTextBox2.Text += "text_editor_path = " + text_editor_path + "\t" + "fullname = " + fullname + "\n";
                if (System.IO.File.Exists(text_editor_path) == true)
                {
                    Process.Start(text_editor_path, fullname);
                }
                else
                {
                    richTextBox2.Text += "開啟程式不存在\n";
                }
            }
        }

        private void bt_start_files_Click(object sender, EventArgs e)
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

                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].Text + "\"";
                }
                else
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text + "\"";
                }
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
            else
            {
                if (System.IO.File.Exists(text_editor_path) == true)
                {
                    Process.Start(text_editor_path, all_filename);
                }
            }
        }

        private void bt_edit_python_files_Click(object sender, EventArgs e)
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

                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].Text + "\"";
                }
                else
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text + "\"";
                }
            }

            richTextBox2.Text += "all_filename : " + all_filename + "\n";

            string prog = @"C:\Users\070601\AppData\Local\Programs\Python\Python311\Lib\idlelib\idle.pyw";

            if (python_editor_path == string.Empty)
            {
                python_editor_path = prog;
            }

            Process.Start(python_editor_path, all_filename);

            return;

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
            else
            {
                if (System.IO.File.Exists(text_editor_path) == true)
                {
                    Process.Start(text_editor_path, all_filename);
                }
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
                //按Enter 等同於 bt_start_files_Click
                bt_start_files_Click(sender, e);
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

        private void bt_save_data_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "儲存資料成檔案\tTBD\n";
        }

        private void bt_copy_data_Click(object sender, EventArgs e)
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

        private void bt_find_big_files_Click(object sender, EventArgs e)
        {
            //搜尋大檔
            bt_start_files.BackgroundImage = vcs_DrAP.Properties.Resources.potplayer;
            bt_find_big_files.BackColor = Color.Red;

            Application.DoEvents();

            min_size_mb = 0;
            bool conversionSuccessful = int.TryParse(tb_file_l.Text, out min_size_mb);    //out為必須
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
            flag_function = FUNCTION_FIND_BIG_FILES;
            find_and_show_big_files();
            bt_find_big_files.BackColor = System.Drawing.SystemColors.ControlLight;
        }

        private void bt_delete_file_Click(object sender, EventArgs e)
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
                        //richTextBox2.Text += subdirectory + "\n";

                        if (search_mode == SEARCH_MODE_PYTHON)
                        {
                            string search_folder1 = @"C:\_git\vcs\_4.python\__code";    //書附光碟

                            if (rb_python_search0.Checked == true)
                            {
                                //python only 不包含 書附光碟
                                if (subdirectory.Contains(search_folder1))
                                {
                                    //跳過 書附光碟
                                    richTextBox2.Text += "跳過 " + subdirectory + "\n";
                                    continue;
                                }
                                else
                                {
                                    ProcessDirectoryS(subdirectory);
                                }
                            }
                            else if (rb_python_search1.Checked == true)
                            {
                                //全部
                                ProcessDirectoryS(subdirectory);
                            }
                            else
                            {
                                //impossible
                                richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n";
                                //python only 不包含新進檔案 與 書附光碟
                            }
                        }
                        else if ((search_mode == SEARCH_MODE_VCS) && (cb_option3.Checked == true))
                        {
                            string search_folder = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_c_example";
                            if (subdirectory.Contains(search_folder))
                            {
                                ProcessDirectoryS(subdirectory);
                            }
                            else
                            {
                                richTextBox2.Text += "跳過 " + subdirectory + "\n";
                                continue;
                            }
                        }
                        else if ((search_mode == SEARCH_MODE_VCS) && (cb_option3.Checked == false))
                        {
                            string skip_folder = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_c_example";
                            if (subdirectory.Contains(skip_folder))
                            {
                                richTextBox2.Text += "跳過 " + subdirectory + "\n";
                                continue;
                            }
                            else
                            {
                                ProcessDirectoryS(subdirectory);
                            }
                        }
                        else
                        {
                            //除了python 與 vcs, 全部搜尋
                            ProcessDirectoryS(subdirectory);
                        }
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
            if (cb_option1.Checked == true)
            {
                if (fileinfos.Count >= 30)
                {
                    if (flag_show_30_message == false)
                    {
                        flag_show_30_message = true;
                        richTextBox1.Text += "滿30結束\n";
                    }
                    return;
                }
            }

            FileInfo fi = new FileInfo(path);
            //richTextBox2.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            bool res;
            string pattern = string.Empty;// = "Form1.cs";

            if (search_mode == SEARCH_MODE_VCS)
                pattern = ".cs";
            else if (search_mode == SEARCH_MODE_PYTHON)
                pattern = "py";
            else if (search_mode == SEARCH_MODE_CUDA)
                pattern = ".cu";
            else if (search_mode == SEARCH_MODE_OPENGL)
                pattern = ".cpp";
            else
                pattern = ".cs";

            res = fi.FullName.ToLower().Replace(" ", "").EndsWith(pattern.ToLower());

            if (res == false)   //vcs加搜尋txt檔案
            {
                if (search_mode == SEARCH_MODE_VCS) //vcs 加搜尋 .txt
                {
                    res = fi.FullName.ToLower().Replace(" ", "").Contains("____txt");
                }
            }

            if (res == false)   //cuda加搜尋 .cpp 檔案
            {
                if (search_mode == SEARCH_MODE_CUDA) //cuda 加搜尋 .cpp
                {
                    res = fi.FullName.ToLower().Replace(" ", "").EndsWith(".cpp");
                }
            }

            if (res == false)   //cuda加搜尋 .c 檔案
            {
                if (search_mode == SEARCH_MODE_CUDA) //cuda 加搜尋 .c
                {
                    res = fi.FullName.ToLower().Replace(" ", "").EndsWith(".c");
                }
            }

            if (res == false)   //cuda加搜尋 .h 檔案
            {
                if (search_mode == SEARCH_MODE_CUDA) //cuda 加搜尋 .h
                {
                    res = fi.FullName.ToLower().Replace(" ", "").EndsWith(".h");
                }
            }

            if (res == false)   //opengl加搜尋 .c 檔案
            {
                if (search_mode == SEARCH_MODE_OPENGL) //opengl 加搜尋 .c
                {
                    res = fi.FullName.ToLower().Replace(" ", "").EndsWith(".c");
                }
            }

            if (res == false)   //opengl加搜尋 .h 檔案
            {
                if (search_mode == SEARCH_MODE_OPENGL) //opengl 加搜尋 .h
                {
                    res = fi.FullName.ToLower().Replace(" ", "").EndsWith(".h");
                }
            }

            if (res == true)
            {
                //richTextBox2.Text += "aaaa : " + fi.FullName + "\n";

                if (search_mode == SEARCH_MODE_VCS) //有一些vcs檔案 要跳開 (先改成小寫名)
                {
                    if (fi.FullName.ToLower().Replace(" ", "").Contains("program.cs"))
                    {
                        res = false;
                        return;
                    }
                    else if (fi.FullName.ToLower().Replace(" ", "").Contains("assemblyinfo.cs"))
                    {
                        res = false;
                        return;
                    }
                    else if (fi.FullName.ToLower().Replace(" ", "").Contains("csproj"))
                    {
                        res = false;
                        return;
                    }
                    /*
                    else if (fi.FullName.ToLower().Replace(" ", "").Contains("designer"))
                    {
                        res = false;
                        return;
                    }
                    */
                }

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
                    richTextBox2.Text += "上面搜尋到的資料在檔案\t" + fi.FullName + "\n\n";
                    fileinfos.Add(new MyFileInfo(fi.Name, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));
                }
                sr.Close();
            }
            else
            {
                return;
            }
        }

        private void bt_search_pattern_vcs_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_VCS);
            return;
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            //改用KeyDown
            /*
            if (e.KeyChar == (Char)13)      //Enter
            {
                bt_search_pattern_vcs_Click(sender, e);
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

        void show_file_info4()
        {
            //找同檔
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (cb_video_only.Checked == true)
            {
                listView1.Columns.Add("影片4", 100, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名4", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (fileinfos.Count == 0)
            {
                richTextBox2.Text += "找不到資料d\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                richTextBox2.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料d\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            for (int i = 0; i < (fileinfos.Count - 1); i++)
            {
                for (int j = i + 1; j < fileinfos.Count; j++)
                {
                    if (fileinfos[i].filesize == fileinfos[j].filesize)
                    {
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[i].filename + " 容量 " + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[j].filename + " 容量 " + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[j].filesize)) + "\n";

                        ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        i1.SubItems.Add(fileinfos[i].filepath);
                        sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        i1.SubItems.Add(sub_i1a);
                        i1.SubItems.Add(fileinfos[i].fileextension);
                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                        listView1.Items.Add(i1);

                        ListViewItem i2 = new ListViewItem(fileinfos[j].filename);
                        i2.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i2a = new ListViewItem.ListViewSubItem();
                        i2.SubItems.Add(fileinfos[j].filepath);
                        sub_i2a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[j].filesize));
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
                sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                */
            }
        }

        private void bt_find_same_files_Click(object sender, EventArgs e)
        {
            //找同檔
            show_file_info4();
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
            flag_search_done = 0;
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

        int total_number_files = 0;
        private void bt_test1_Click(object sender, EventArgs e)
        {
            /*
            //richTextBox2.Text += "flag_function = " + flag_function.ToString() + "\n";

            Properties.Settings.Default.search_path = "";

            Properties.Settings.Default.Save();
            */

            string foldername = @"C:\_git\vcs\_1.data\______test_files1\_case1\";
            richTextBox1.Text += "讀出一資料夾內所有檔案 -r, 資料夾\t" + foldername + "\n";

            //get_all_files(foldername);

            //轉出
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
            total_size = 0;
            total_files = 0;

            path = foldername;
            richTextBox2.Text += "\n搜尋路徑" + path + "\n";
            FolederName = path;
            ProcessDirectory(path);
            richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            show_file_info1();

            flag_search_done = 1;

            // Stop timing
            stopwatch.Stop();
            // Write result
            richTextBox2.Text += "停止計時\t";
            richTextBox2.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
            this.Text = "DrAP (轉出時間 : " + (stopwatch.ElapsedMilliseconds / 1000).ToString() + " 秒)";
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory4(string targetDirectory)
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
                        ProcessFile4(fileName, step);
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
                        ProcessDirectory4(subdirectory);
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
        public void ProcessFile4(string path, int step)
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
                    res = fi.FullName.ToLower().Replace(" ", "").Contains(tb_search_text_pattern.Text.ToLower().Replace("-", ""));
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
                fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
            }
        }

        void get_all_files(string foldername)
        {
            total_number_files = 0;
            DirectoryInfo temp3 = new DirectoryInfo(foldername);

            DirectoryInfo[] idr = temp3.GetDirectories();//獲取當前目錄下的所有子目錄.
            foreach (DirectoryInfo dir in idr)
            {
                richTextBox1.Text += "取得資料夾 : " + dir.FullName + "\n";


                FileInfo[] files1 = dir.GetFiles();

                foreach (FileInfo file in files1)
                {
                    richTextBox1.Text += "取得檔案 : " + file.FullName + "\n";
                    total_number_files++;

                    //Console.WriteLine(file.FullName);
                }



            }

            richTextBox1.Text += "目錄 : " + foldername + " 下\n";
            FileInfo[] files2 = temp3.GetFiles();

            foreach (FileInfo file in files2)
            {
                richTextBox1.Text += "取得檔案 : " + file.FullName + "\n";
                total_number_files++;

                //Console.WriteLine(file.FullName);
            }
            richTextBox1.Text += "共取得檔案 " + total_number_files.ToString() + " 個\n";
        }

        private void textBox3_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                //按Enter 等同於 bt_search_pattern_vcs_Click
                bt_search_pattern_vcs_Click(sender, e);
            }
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            removeDrawDiskSpace();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        void show_file_info5()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            //設置列名稱
            if (cb_video_only.Checked == true)
            {
                listView1.Columns.Add("影片5", 100, HorizontalAlignment.Left);
            }
            listView1.Columns.Add("檔名5", 300, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;

            if (fileinfos.Count == 0)
            {
                richTextBox2.Text += "找不到資料e\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                richTextBox2.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料e\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            for (int i = 0; i < (fileinfos.Count - 1); i++)
            {
                string filename1 = fileinfos[i].filename;
                //richTextBox1.Text += "filename1 : " + fileinfos[i].filename + "\n";

                for (int j = i + 1; j < fileinfos.Count; j++)
                {
                    string filename2 = fileinfos[j].filename;
                    richTextBox1.Text += "filename2 : " + fileinfos[j].filename + "\n";

                    richTextBox1.Text += "str1 = " + filename1.ToLower().Replace(" ", "").Replace("-", "") + "\n";
                    richTextBox1.Text += "str2 = " + filename2.ToLower().Replace(" ", "").Replace("-", "").Substring(0, 6) + "\n";


                    bool ret;

                    ret = filename1.ToLower().Replace(" ", "").Replace("-", "").Contains(filename2.ToLower().Replace(" ", "").Replace("-", "").Substring(0, 6));
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
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[i].filename + " 容量 " + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize)) + "\n";
                        richTextBox2.Text += "檔案大小相同 " + fileinfos[j].filename + " 容量 " + ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[j].filesize)) + "\n";

                        ListViewItem i1 = new ListViewItem(fileinfos[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        i1.SubItems.Add(fileinfos[i].filepath);
                        sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                        i1.SubItems.Add(sub_i1a);
                        i1.SubItems.Add(fileinfos[i].extension);
                        sub_i1a.ForeColor = System.Drawing.Color.Blue;
                        sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);

                        listView1.Items.Add(i1);

                        ListViewItem i2 = new ListViewItem(fileinfos[j].filename);
                        i2.UseItemStyleForSubItems = false;

                        ListViewItem.ListViewSubItem sub_i2a = new ListViewItem.ListViewSubItem();
                        i2.SubItems.Add(fileinfos[j].filepath);
                        sub_i2a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[j].filesize));
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
                sub_i1a.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fileinfos[i].filesize));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font("Times New Roman", 10, System.Drawing.FontStyle.Bold);
                */
            }
        }

        private void bt_find_same_files2_Click(object sender, EventArgs e)
        {
            //找可能相同檔案
            show_file_info5();
        }

        private void bt_find_small_folders_Click(object sender, EventArgs e)
        {
            //找小資料夾
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

            flag_function = FUNCTION_FIND_SMALL_FOLDERS;
            folderinfos.Clear();

            total_size = 0;
            total_files = 0;

            path = @"C:\_git\vcs\_1.data\______test_files1\_case1";

            richTextBox2.Text += "\n搜尋路徑 " + path + "\n";

            total_folders = 0;

            if (System.IO.File.Exists(path) == true)
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile2(path, 0);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                flag_search_done = 1;
            }
            else if (Directory.Exists(path) == true)
            {
                // This path is a directory
                FolederName = path;
                ProcessDirectory2(path);

                richTextBox1.Text += "\n類型:\t\t檔案資料夾\n";
                richTextBox1.Text += "位置:\t\t" + Directory.GetParent(path) + "\n";
                richTextBox1.Text += "大小:\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "(" + total_size.ToString() + "位元組)\n";
                richTextBox1.Text += "包含:\t\t" + total_files.ToString() + "個檔案，" + (total_folders - 1).ToString() + "個資料夾\n";

                DirectoryInfo di = new DirectoryInfo(path);
                richTextBox1.Text += "建立日期:\t" + di.CreationTime.ToString() + "\n\n";

                show_file_info6();
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案c\n";
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
            //richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

            //fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length));
        }

        private void bt_search_pattern_python_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_PYTHON);
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

                    if (System.IO.File.Exists(path) == true)
                    {
                        // This path is a file
                        richTextBox1.Text += "是個檔案\n";
                    }
                    else if (Directory.Exists(path) == true)
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
                                "使用空間 :", (drive.TotalSize - drive.AvailableFreeSpace).ToString("N0", CultureInfo.InvariantCulture), " 個位元組", ByteConversionTBGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace))) + "\n";
                            double percentage = (double)drive.AvailableFreeSpace / (double)drive.TotalSize;
                            richTextBox1.Text += string.Format("{0,-12}{1,17}{2,-7}{3,10}{4,-10}",
                                "可用空間 :", drive.AvailableFreeSpace.ToString("N0", CultureInfo.InvariantCulture), " 個位元組",
                                ByteConversionTBGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)),
                                " ( " + percentage.ToString("P", CultureInfo.InvariantCulture) + " )")
                                + "\n";
                            richTextBox1.Text += string.Format("{0,-12}{1,17}{2,-7}{3,10}",
                                "磁碟容量 :", drive.TotalSize.ToString("N0", CultureInfo.InvariantCulture), " 個位元組", ByteConversionTBGBMBKB(Convert.ToInt64(drive.TotalSize))) + "\n";

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
                        richTextBox1.Text += "非合法路徑或檔案d\n";
                    }
                }
            }
            richTextBox1.Text += "\n";

            richTextBox2.Text += "listbox 共有 " + listBox1.Items.Count.ToString() + " 個項目\n";
            for (int i = 0; i < listBox1.Items.Count; i++)
            {
                path = listBox1.Items[i].ToString();

                richTextBox2.Text += "\n搜尋路徑" + path + "\n";

                if (System.IO.File.Exists(path) == true)
                {
                    // This path is a file
                    richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                    ProcessFile(path, 0);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
                }
                else if (Directory.Exists(path) == true)
                {
                    // This path is a directory
                    FolederName = path;
                    ProcessDirectory(path);
                    richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";

                    if (cb_video_only.Checked == true)
                    {
                        show_file_info1();
                    }
                }
                else
                {
                    //Console.WriteLine("{0} is not a valid file or directory.", path);
                    richTextBox1.Text += "非合法路徑或檔案e\n";
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

                    if (System.IO.File.Exists(path) == true)
                    {
                        // This path is a file
                        richTextBox1.Text += "是個檔案\n";
                    }
                    else if (Directory.Exists(path) == true)
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
                        richTextBox1.Text += "非合法路徑或檔案f\n";
                    }

                }
                filename = "AP." + hddname + DateTime.Now.ToString(".yyyy.MMdd.HHmm") + ".txt";
            }
            else
            {
                filename = "AP." + DateTime.Now.ToString("yyyy.MMdd.HHmm") + ".txt";
            }

            //建立一個檔案
            //StreamWriter sw = System.IO.File.CreateText(filename);
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("UTF-8"));   //指名編碼格式
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";
            richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void bt_save_rtb_data_Click(object sender, EventArgs e)
        {
            save_log_to_local_drive();
        }

        private const int WIDTH = 100;
        void drawDiskSpace(long free, long total)
        {
            removeDrawDiskSpace();

            //產出panel, 畫硬碟使用空間占比圖
            Panel pnl = new Panel();
            pnl.Left = 1070;
            pnl.Top = 5;
            pnl.Width = WIDTH;
            pnl.Height = WIDTH;
            pnl.Tag = "dynamic";
            pnl.BackColor = Color.White;
            this.Controls.Add(pnl);

            Graphics g;
            g = pnl.CreateGraphics();
            /*  debug
            Pen p = new Pen(Color.Black, 1);
            p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            g.DrawRectangle(p, WIDTH / 10, WIDTH / 10, WIDTH * 80 / 100, WIDTH * 80 / 100);
            */

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
                bt_clear2.Visible = true;
                if (cb_generate_text.Checked == true)
                {
                    richTextBox1.Size = new Size(1300, 430);

                    bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_clear1.Width, bt_clear1.Location.Y);
                    bt_save_rtb_data.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_save_rtb_data.Width, bt_save_rtb_data.Location.Y);
                }
            }
            else
            {
                richTextBox2.Visible = false;
                bt_clear2.Visible = false;

                if (cb_generate_text.Checked == true)
                {
                    richTextBox1.Size = new Size(listView1.Width, 430);

                    bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_clear1.Width, bt_clear1.Location.Y);
                    bt_save_rtb_data.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_save_rtb_data.Width, bt_save_rtb_data.Location.Y);
                }
            }
        }

        private void cb_video_only_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_video_only.Checked == true)
                groupBox_video.Enabled = true;
            else
                groupBox_video.Enabled = false;
        }

        private void cb_file_size_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_file_size.Checked == true)
                groupBox_file.Enabled = true;
            else
                groupBox_file.Enabled = false;
        }

        private void cb_generate_text_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void cb_video_l_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void cb_video_m_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void cb_video_s_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void cb_file_l_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void cb_file_m_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void cb_file_s_CheckedChanged(object sender, EventArgs e)
        {
        }

        private void bt_search_pattern_cuda_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_CUDA);
            return;
        }

        private void bt_search_pattern_opengl_Click(object sender, EventArgs e)
        {
            do_search_mode(SEARCH_MODE_OPENGL);
            return;
        }

        void do_search_mode(int mode)
        {
            string path = string.Empty;
            richTextBox1.Clear();
            richTextBox2.Clear();
            listView1.Clear();
            removeDrawDiskSpace();
            flag_function = FUNCTION_SEARCH_TEXT;
            Application.DoEvents();

            richTextBox1.Text += "搜尋開始\t";
            richTextBox2.Text += "搜尋開始\t";
            lb_search_result1.Text = "";

            if (mode == SEARCH_MODE_VCS)
            {
                search_mode = SEARCH_MODE_VCS;
                richTextBox1.Text += "vcs\t";
                richTextBox2.Text += "vcs\t";

                bt_search_pattern_vcs.BackgroundImage = null;
                bt_search_pattern_vcs.BackColor = Color.Red;
                path = default_vcs_path;
            }
            else if (mode == SEARCH_MODE_PYTHON)
            {
                search_mode = SEARCH_MODE_PYTHON;
                richTextBox1.Text += "python\t";
                richTextBox2.Text += "python\t";

                bt_search_pattern_python.BackgroundImage = null;
                bt_search_pattern_python.BackColor = Color.Red;
                path = default_python_path;
            }
            else if (mode == SEARCH_MODE_CUDA)
            {
                search_mode = SEARCH_MODE_CUDA;
                richTextBox1.Text += "cuda\t";
                richTextBox2.Text += "cuda\t";

                bt_search_pattern_cuda.BackgroundImage = null;
                bt_search_pattern_cuda.BackColor = Color.Red;
                path = default_cuda_path;
            }
            else if (mode == SEARCH_MODE_OPENGL)
            {
                search_mode = SEARCH_MODE_OPENGL;
                richTextBox1.Text += "opengl\t";
                richTextBox2.Text += "opengl\t";

                bt_search_pattern_opengl.BackgroundImage = null;
                bt_search_pattern_opengl.BackColor = Color.Red;
                path = default_opengl_path;
            }
            else
            {
                //其他搜尋模式
            }
            richTextBox1.Text += textBox3.Text + "\n";
            richTextBox2.Text += textBox3.Text + "\n";

            bt_start_files.BackgroundImage = vcs_DrAP.Properties.Resources.ultraedit;
            Application.DoEvents();

            flag_show_30_message = false;

            if (textBox3.Text == "")
            {
                richTextBox2.Text += "未輸入搜尋內容\n";
                return;
            }

            fileinfos.Clear();

            if (path == String.Empty)
                path = search_path;

            if (cb_option2.Checked == true)
                path = specified_search_path;

            richTextBox1.Text += "搜尋資料夾: " + path + "\n\n";
            if (System.IO.File.Exists(path) == true)
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFileS(path);
            }
            else if (Directory.Exists(path) == true)
            {
                // This path is a directory
                ProcessDirectoryS(path);
            }
            show_file_info3();
            flag_search_vcs_pattern = 1;
            if (mode == SEARCH_MODE_VCS)
            {
                bt_search_pattern_vcs.BackColor = System.Drawing.SystemColors.ControlLight;
                bt_search_pattern_vcs.BackgroundImage = vcs_DrAP.Properties.Resources.vcs;
            }
            else if (mode == SEARCH_MODE_PYTHON)
            {
                bt_search_pattern_python.BackColor = System.Drawing.SystemColors.ControlLight;
                bt_search_pattern_python.BackgroundImage = vcs_DrAP.Properties.Resources.python;
            }
            else if (mode == SEARCH_MODE_CUDA)
            {
                bt_search_pattern_cuda.BackColor = System.Drawing.SystemColors.ControlLight;
                bt_search_pattern_cuda.BackgroundImage = vcs_DrAP.Properties.Resources.cuda;
            }
            else if (mode == SEARCH_MODE_OPENGL)
            {
                bt_search_pattern_opengl.BackColor = System.Drawing.SystemColors.ControlLight;
                bt_search_pattern_opengl.BackgroundImage = vcs_DrAP.Properties.Resources.opengl;
            }
            else
            {
                bt_search_pattern_vcs.BackColor = System.Drawing.SystemColors.ControlLight;
                bt_search_pattern_vcs.BackgroundImage = vcs_DrAP.Properties.Resources.vcs;
            }
            return;
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗

            update_default_setting();
        }

        void update_default_setting()
        {
            video_player_path = Properties.Settings.Default.video_player_path;
            audio_player_path = Properties.Settings.Default.audio_player_path;
            picture_viewer_path = Properties.Settings.Default.picture_viewer_path;
            text_editor_path = Properties.Settings.Default.text_editor_path;
            python_editor_path = Properties.Settings.Default.python_editor_path;
            winmerge_path = Properties.Settings.Default.winmerge_path;

            if (Properties.Settings.Default.search_path != "")
                search_path = Properties.Settings.Default.search_path;

            if (System.IO.File.Exists(Properties.Settings.Default.video_player_path) == false)
            {
                richTextBox2.Text += "播放影片程式不存在 : " + Properties.Settings.Default.video_player_path + "\n使用Windows預設播放影片程式\n";
                video_player_path = String.Empty;
            }
            if (System.IO.File.Exists(Properties.Settings.Default.audio_player_path) == false)
            {
                richTextBox2.Text += "播放音樂程式不存在 : " + Properties.Settings.Default.audio_player_path + "\n使用Windows預設播放音樂程式\n";
                audio_player_path = String.Empty;
            }
            if (System.IO.File.Exists(Properties.Settings.Default.picture_viewer_path) == false)
            {
                richTextBox2.Text += "播放圖片程式不存在 : " + Properties.Settings.Default.picture_viewer_path + "\n使用Windows預設播放圖片程式\n";
                picture_viewer_path = String.Empty;
            }
            if (System.IO.File.Exists(Properties.Settings.Default.text_editor_path) == false)
            {
                richTextBox2.Text += "文字編輯程式不存在 : " + Properties.Settings.Default.text_editor_path + "\n使用Windows預設文字編輯程式\n";
                text_editor_path = String.Empty;
            }
            if (System.IO.File.Exists(Properties.Settings.Default.python_editor_path) == false)
            {
                richTextBox2.Text += "python編輯程式不存在 : " + Properties.Settings.Default.python_editor_path + "\n使用Windows預設文字編輯程式\n";
                python_editor_path = String.Empty;
            }
            if (System.IO.File.Exists(Properties.Settings.Default.winmerge_path) == false)
            {
                richTextBox2.Text += "winmerge程式不存在 : " + Properties.Settings.Default.winmerge_path + "\n使用Windows預設文字編輯程式\n";
                winmerge_path = String.Empty;
            }

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

        private void bt_copy_rtb_data_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox2.Text + "\n");      //建議用此
            richTextBox2.Text += "已複製資料到系統剪貼簿\n";
        }

        private void bt_compare_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox2.Text += listView1.SelectedItems[i].SubItems[1].Text + "\\" + listView1.SelectedItems[i].SubItems[0].Text + "\n";
            }

            if (listView1.SelectedIndices.Count != 2)
            {
                richTextBox2.Text += "必須要選取2個檔案才能比較\n";
                return;
            }

            int selNdx;
            string all_filename = string.Empty;

            //richTextBox2.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox2.Text += listView1.Items[selNdx].Text + "\n";

                if (flag_function == FUNCTION_SEARCH_TEXT)
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].Text + "\"";
                }
                else
                {
                    all_filename += " \"" + listView1.Items[selNdx].SubItems[3].Text + "\\" + listView1.Items[selNdx].SubItems[2].Text + "\"";
                }
            }

            richTextBox2.Text += "all_filename : " + all_filename + "\n";

            string prog = @"C:/Program Files (x86)/WinMerge/WinMergeU.exe";

            if (winmerge_path == string.Empty)
            {
                winmerge_path = prog;
            }

            Process.Start(winmerge_path, all_filename);
            return;
        }
        //檢查空資料夾 ST

        int total_show_empty_folder_cnt = 0;
        int total_delete_empty_folder_cnt = 0;

        private void bt_find_empty_folders_Click(object sender, EventArgs e)
        {
            total_show_empty_folder_cnt = 0;
            total_delete_empty_folder_cnt = 0;

            /*
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";

            //確認資料夾是否存在
            string Path = @"C:/_git/vcs/_1.data/______test_files1/aaaa/bbbb";
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
                richTextBox1.Text += "搜尋資料夾: " + Path + " 不存在\n";
            else
                richTextBox1.Text += "搜尋資料夾: " + Path + " 存在\n";
            */

            //string path = default_vcs_path;
            string path = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw";
            //string path = search_path;


            //folder_name.Clear();

            //richTextBox1.Text += "搜尋資料夾: " + path + "\n\n";
            if (Directory.Exists(path) == true)
            {
                // This path is a directory
                ProcessDirectory3(path);
            }

            //if (checkBox9.Checked == true)
            {
                richTextBox1.Text += "共找到空資料夾 " + total_show_empty_folder_cnt.ToString() + " 個\n";
            }
            //if (checkBox10.Checked == true)
            {
                //richTextBox1.Text += "共刪除空資料夾 " + total_delete_empty_folder_cnt.ToString() + " 個\n";
            }
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory3(string targetDirectory)
        {
            try
            {
                int file_cnt = 0;
                int dir_cnt = 0;

                // Process the list of files found in the directory.
                try
                {

                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    file_cnt = fileEntries.Length;
                    Array.Sort(fileEntries);
                    foreach (string fileName in fileEntries)
                    {
                    }

                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    dir_cnt = subdirectoryEntries.Length;
                    Array.Sort(subdirectoryEntries);
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        //richTextBox1.Text += "subdirectory = " + subdirectory + "\n";

                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        ProcessDirectory3(subdirectory);
                    }
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
                if ((file_cnt == 0) && (dir_cnt == 0))
                {
                    /*
                    if (checkBox9.Checked == true)
                    {
                        richTextBox1.Text += targetDirectory + "是一個空資料夾\n";
                        total_show_empty_folder_cnt++;
                    }
                    if (checkBox10.Checked == true)
                    {
                        //richTextBox1.Text += "刪除 : " + targetDirectory + "是一個空資料夾\n";
                        Directory.Delete(targetDirectory, false);   //not recurrsive
                        richTextBox1.Text += "已刪除資料夾 : " + targetDirectory + "\n";
                        total_delete_empty_folder_cnt++;
                    }
                    */
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
            }
        }

        private void bt_help_Click(object sender, EventArgs e)
        {

        }

        private void bt_test2_Click(object sender, EventArgs e)
        {
            if (fileinfos.Count == 0)
            {
                richTextBox2.Text += "找不到資料a\n";
                lb_search_result1.Text = "0";
            }
            else
            {
                richTextBox2.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料a\n";
                lb_search_result1.Text = fileinfos.Count.ToString();
            }

            //排序 由小到大
            //fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            //排序 由大到小  在return的地方多個負號
            fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            for (int i = 0; i < fileinfos.Count; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + ", filename : " + fileinfos[i].filepath + "\\" + fileinfos[i].filename + "\n";
            }
        }

        private void textBox3_Click(object sender, EventArgs e)
        {
            textBox3.SelectAll();
        }

        private void bt_save_file_data_Click(object sender, EventArgs e)
        {

        }

        private void bt_open_dir2_Click(object sender, EventArgs e)
        {
            int cnt = listView1.SelectedItems.Count;
            if (cnt > 0)
            {
                int selNdx = listView1.SelectedIndices[0];

                richTextBox2.Text += "aaaa b3你選擇了檔名3:\t" + listView1.Items[selNdx].SubItems[0].Text + "\n";

                string foldername = listView1.Items[selNdx].SubItems[1].Text;
                richTextBox2.Text += "資料夾:\t" + foldername + "\n";

                string fullname = listView1.Items[selNdx].SubItems[1].Text + "\\" + listView1.Items[selNdx].SubItems[0].Text;
                richTextBox2.Text += "全檔名:\t" + fullname + "\n";

                /*
                //C# 呼叫檔案總管開啟某個資料夾，並讓某個檔案或資料夾呈現反白的樣子
                string file = @"C:\Windows\explorer.exe";
                string argument = @"/select, " + foldername;
                Process.Start(file, argument);
                */
                Process.Start(foldername);

            }
        }

        private void bt_clear3_Click(object sender, EventArgs e)
        {
            listView1.Clear();
        }

        private void cb_option2_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_option2.Checked == true)
            {
                richTextBox1.Text += "search_path = " + specified_search_path + "\n";
                folderBrowserDialog1.SelectedPath = specified_search_path;  //預設開啟的路徑
                if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
                {
                    specified_search_path = folderBrowserDialog1.SelectedPath;
                    richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                }
                else
                {
                    richTextBox1.Text = "未選取資料夾\n";
                    specified_search_path = String.Empty;
                    cb_option2.Checked = false;
                }
            }
            else
            {
                specified_search_path = String.Empty;
            }
        }
    }
}
