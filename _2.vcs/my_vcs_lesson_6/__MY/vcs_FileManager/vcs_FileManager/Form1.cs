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

            show_item_location();
            update_default_setting();

            this.listBox1.Items.Clear();
            foreach (string sss in old_search_path)
            {
                richTextBox1.Text += "add " + sss + "\n";
                this.listBox1.Items.Add(sss);
            }

            check_filesize = int.Parse(tb_filesize.Text);
            skip_count = int.Parse(tb_count.Text);
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
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            //this.FormBorderStyle = FormBorderStyle.FixedSingle;
            //this.WindowState = FormWindowState.Maximized;  // 設定表單最大化

            //設定執行後的表單大小
            this.Size = new Size(1920, 1040);
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 100 + 10;
            dy = 50 + 10;

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
            tb_shortname.Location = new Point(x_st + dx * 0, y_st + dy * 11 - 5);

            x_st = 420;
            y_st = 12;
            int W = 1920;
            this.listView1.Location = new Point(x_st, y_st);
            this.listView1.Size = new Size(W - x_st - 12, 700);
            this.listBox1.BorderStyle = BorderStyle.Fixed3D;

            this.richTextBox1.Location = new Point(x_st, y_st + 700);
            this.richTextBox1.Size = new Size(W - x_st - 12, 325);

            x_st = 12;
            this.richTextBox2.Location = new Point(x_st, y_st + 700);
            this.richTextBox2.Size = new Size(400, 325);

            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Width - bt_clear1.Width, richTextBox1.Location.Y);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Width - bt_clear2.Width, richTextBox2.Location.Y);
            bt_clear3.Location = new Point(listView1.Location.X + listView1.Size.Width - bt_clear3.Size.Width, listView1.Location.Y + listView1.Size.Height - bt_clear3.Size.Height);
            lb_find.Location = new Point(bt_clear3.Location.X - 200, bt_clear3.Location.Y);
            lb_time.Location = new Point(bt_clear1.Location.X - 200, bt_clear1.Location.Y);

            bt_minimize_setup();
            bt_exit_setup();

            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";
            lb_time.Text = "";
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

        void update_default_setting()
        {
            video_player_path = Properties.Settings.Default.video_player_path;
            audio_player_path = Properties.Settings.Default.audio_player_path;
            picture_viewer_path = Properties.Settings.Default.picture_viewer_path;
            search_path = Properties.Settings.Default.search_path;

            if (System.IO.File.Exists(Properties.Settings.Default.video_player_path) == false)
            {
                richTextBox2.Text += "播放影片程式不存在 : " + Properties.Settings.Default.video_player_path + "\n使用Windows預設播放影片程式\n";
                //video_player_path = String.Empty;
                video_player_path = @"D:\___backup\PotPlayer\PotPlayerMini64.exe";
                //video_player_path = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
            }
            richTextBox1.Text += "video_player_path : " + video_player_path + "\n";

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
            tb_filesize.Text = Properties.Settings.Default.min_file_size.ToString();
            tb_count.Text = Properties.Settings.Default.search_count.ToString();
            tb_find.Text = Properties.Settings.Default.search_pattern;
        }

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
                        //richTextBox1.Text += "\n";
                        //richTextBox1.Text += di.Name + "\n";
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
            string shortname = string.Empty;
            if (flag_need_shortname == true)
            {
                shortname = get_shortname(fi.Name);  //過濾掉檔名的一些字 用以做比較用
            }

            //richTextBox1.Text += "fname = " + fi.FullName + "\n";
            //richTextBox1.Text += "dname = " + fi.DirectoryName + "\n";

            //把資料放進 List<MyFileInfo> fileinfos 中
            fileinfos.Add(new MyFileInfo(fi.Name, fi.FullName, shortname, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));
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
                    //richTextBox1.Text += directory_old + "\n";
                }

                /*
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
                */

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




                MediaFile f = new MediaFile(fis[i].filepath + "\\" + fis[i].filename);

                /*
                richTextBox1.Text += "  影片長度: " + f.General.DurationString + "\n";
                richTextBox1.Text += "  FileSize: " + f.FileSize.ToString() + "\n";
                richTextBox1.Text += "  Extension: " + f.Extension + "\n";
                */


                //richTextBox2.Text += "檔案 : " + fis[i].filename + "\t";
                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    //richTextBox2.Text += "影片\n";

                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    //richTextBox2.Text += "  輸入大小: " + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\n";
                    //richTextBox2.Text += "  FPS: " + f.Video[0].FrameRate.ToString() + "\n";
                    //richTextBox2.Text += string.Format("{0,-60}{1,-20}{2,5} X {3,5}{4,5}{5,10}",
                    //fi.FullName, ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)), w.ToString(), h.ToString(), f.Video[0].FrameRate.ToString(), f.General.DurationString) + "\n";

                    if (w != 1920)
                    {
                        itemg = w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)";

                        sub_i1g.Text = itemg;
                        i1.SubItems.Add(sub_i1g);
                    }



                }
                else
                {
                    richTextBox2.Text += "非影片\n";
                    //非影片




                    //richTextBox1.Text += "B";
                    //continue;
                }

                listView1.Items.Add(i1);

                //設置ListView最後一行可見
                //listView1.Items[listView1.Items.Count - 1].EnsureVisible();

            }

            /*
                        i1 = new ListViewItem(fis[i].filename);
                        i1.UseItemStyleForSubItems = false;

                        richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX1\n";
                        //richTextBox2.Text += "xxxxx" + fis[i].filename + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize)) + "\n";
                        sub_i1a.Text = fis[i].filepath;
                        i1.SubItems.Add(sub_i1a);
                        //sub_i1a.Text = fi.Length.ToString();
                        sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize));
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

                    i1 = new ListViewItem(fis[i].filename);
                    i1.UseItemStyleForSubItems = false;

                    richTextBox2.Text += "XXXXXXXXXXXXXXXXXXXXXXXXX2\n";
                    sub_i1a.Text = fis[i].filepath;
                    i1.SubItems.Add(sub_i1a);
                    //sub_i1a.Text = fi.Length.ToString();
                    sub_i1b.Text = ByteConversionTBGBMBKB(Convert.ToInt64(fis[i].filesize));
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

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "撈出資料夾一層檔案\n";
            //從一個資料夾中撈出所有檔案 標準版 一層 標準版

            if (listBox1.Items.Count == 0)
            {
                richTextBox2.Text += "未選擇資料夾\n";
                return;
            }

            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";
            lb_time.Text = "";
            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            button0.BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            //轉出一層
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

                    //show_file_info();
                }
                else
                {
                    richTextBox1.Text += "非合法路徑或檔案a\n";
                }
            }

            this.Cursor = Cursors.Default;
            button0.BackColor = System.Drawing.SystemColors.ControlLight;

            stopwatch.Stop();
            lb_time.Text = "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒";
            lb_files.Text = "檔案個數 : " + total_files.ToString();
            lb_filesize.Text = "總容量   : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size));
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
            lb_time.Text = "";
            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            button1.BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

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

            this.Cursor = Cursors.Default;
            button1.BackColor = System.Drawing.SystemColors.ControlLight;

            //stopwatch.Stop();
            lb_time.Text = "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒";
            lb_files.Text = "檔案個數 : " + total_files.ToString();
            lb_filesize.Text = "總容量   : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            lb_files.Text = "";
            lb_filesize.Text = "";
            lb_find.Text = "";
            lb_time.Text = "";
            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            button2.BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            show_file_info();

            this.Cursor = Cursors.Default;
            button2.BackColor = System.Drawing.SystemColors.ControlLight;

            //stopwatch.Stop();
            lb_time.Text = "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒";
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
            lb_time.Text = "";
            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            button3.BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

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
            this.Cursor = Cursors.Default;
            button3.BackColor = System.Drawing.SystemColors.ControlLight;

            stopwatch.Stop();
            lb_time.Text = "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒";
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
            richTextBox1.Text += "找低畫質影片, 不到720p的影片\n";





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
            using (Process p = new Process())
            {
                p.StartInfo = pInfo;
                p.Start();
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
            using (Process p = new Process())
            {
                p.StartInfo = pInfo;
                p.Start();
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
            lb_time.Text = "";
            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            button5.BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

            match_count = 0;
            fileinfos_match.Clear();

            int i;
            for (i = 0; i < len; i++)
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
            this.Cursor = Cursors.Default;
            button5.BackColor = System.Drawing.SystemColors.ControlLight;

            stopwatch.Stop();
            lb_time.Text = "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒";
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
            lb_time.Text = "";
            this.Cursor = Cursors.WaitCursor;   // set busy cursor
            button6.BackColor = Color.Red;
            Application.DoEvents();
            Stopwatch stopwatch = new Stopwatch();
            stopwatch.Start();

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
            this.Cursor = Cursors.Default;
            button6.BackColor = System.Drawing.SystemColors.ControlLight;

            stopwatch.Stop();
            lb_time.Text = "時間 : " + stopwatch.Elapsed.TotalSeconds.ToString("0.00") + " 秒";
            lb_find.Text = "個數 : " + fileinfos_match.ToString() + " 個";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //DDT 259 KBI.......
            //sga dtt kbi 
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //show all shortnames
            if (fileinfos.Count == 0)
                richTextBox1.Text += "無資料c\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料b\n";

            int len = fileinfos.Count;
            if (len < 2)
                return;

            int i;
            for (i = 0; i < len; i++)
            {
                if (fileinfos[i].shortfilename.Length > 6)
                {
                    richTextBox1.Text += fileinfos[i].filename.ToLower() + "\t\t" + fileinfos[i].shortfilename + "\n";
                    //richTextBox1.Text += fileinfos[i].shortfilename + "\n";
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            /*
            int len = fileinfos_match.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                //debug mesg
                richTextBox2.Text += "i = " + i.ToString() + ", filename : " + fileinfos_match[i].filepath + "\\" + fileinfos_match[i].filename + "\n";



            }
            */

            richTextBox1.Text += "listview len = " + listView1.Items.Count.ToString() + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //string longname = @"D:\內視鏡影片\Capsule Endoscopy Animation - ANKON NaviCam [720p].mp4";
            string longname = tb_shortname.Text;

            string shortname = get_shortname(longname);
            richTextBox1.Text += "long name :  " + longname + "\n";
            richTextBox1.Text += "short name : " + shortname + "\n";
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗

            update_default_setting();
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


//大檔資料存檔

