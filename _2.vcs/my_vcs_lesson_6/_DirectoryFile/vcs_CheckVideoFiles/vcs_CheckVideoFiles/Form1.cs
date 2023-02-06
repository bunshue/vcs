using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Diagnostics;   //for Process
using System.Threading;

using System.IO;    //for FileInfo DirectoryInfo
using System.Globalization; //for CultureInfo

using MediaInfoNET;


namespace vcs_CheckVideoFiles
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
        List<MyFolderInfo> folderinfos = new List<MyFolderInfo>();  //沒用到

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
            show_item_location();
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 185;
            dy = 85;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            int w = 0;
            int h = 0;

            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            w = this.ClientSize.Width - richTextBox1.Location.X - 10;   //border : 10
            h = this.ClientSize.Height - richTextBox1.Location.Y - 10;   //border : 10
            richTextBox1.Size = new Size(w, h);

            listView1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            w = this.ClientSize.Width - richTextBox1.Size.Width - listView1.Location.X - 20;   //border : 10
            h = this.ClientSize.Height - listView1.Location.Y - 10;   //border : 10
            listView1.Size = new Size(w, h);

            bt_clear1.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear1.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear2.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear2.Size.Height);

            bt_exit_setup();
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            fileinfos.Clear();
            listView1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            string foldername = @"C:\______test_files\_mp4";

            FindAllFiles(foldername);
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

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string dir)
        {
            try
            {
                richTextBox1.Text += "\n" + dir + "\n";
                //DirectoryInfo di = new DirectoryInfo(dir);
                //richTextBox1.Text += di.Name + "\n\n";

                // Process the list of files found in the directory.
                try
                {
                    string[] fileEntries = Directory.GetFiles(dir);
                    Array.Sort(fileEntries);
                    folder_size = 0;
                    folder_files = 0;
                    foreach (string fileName in fileEntries)
                    {
                        ProcessFile(fileName);
                    }
                    //richTextBox1.Text += "folder_name = " + dir + "\n";
                    //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";
                    //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
                    if (folder_files == 0)
                    {
                        //richTextBox1.Text += "空資料夾 folder_name = " + dir + "\n";
                    }

                    // Recurse into subdirectories of this directory.
                    string[] subdirEntries = Directory.GetDirectories(dir);
                    Array.Sort(subdirEntries);
                    foreach (string subdir in subdirEntries)
                    {
                        DirectoryInfo di = new DirectoryInfo(subdir);
                        //richTextBox1.Text += "搜尋子目錄\t" + di.Name + "\n";
                        FolederName = subdir;
                        ProcessDirectory(subdir);
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



        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
            show_button_text(sender);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);


        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //檔案資訊
            string filename = @"C:\______test_files\picture1.jpg";

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
            show_button_text(sender);
            //搜尋一個資料夾內所有特定格式的檔案
            string foldername = @"C:\______test_files\_mp4";

            ///根據路徑實例化一個對象
            var di = new DirectoryInfo(foldername);

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
            show_button_text(sender);

        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }


    }
}

