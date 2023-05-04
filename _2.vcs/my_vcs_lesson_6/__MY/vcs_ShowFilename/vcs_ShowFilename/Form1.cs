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
using System.Management;
using System.Globalization; //for CultureInfo

using MediaInfoNET;

namespace vcs_ShowFilename
{
    public partial class Form1 : Form
    {
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
            int x_st;
            int y_st;
            int dx;
            int dy;
            //button
            x_st = 10;
            y_st = 10;
            dx = 160 + 10;
            dy = 70 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        Int64 total_size = 0;
        Int64 total_files = 0;
        //Int64 total_folders = 0;
        Int64 folder_size = 0;
        Int64 folder_files = 0;

        string FolederName = string.Empty;
        List<MyFileInfo> fileinfos = new List<MyFileInfo>();

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

            //richTextBox1.Text += "folder = " + FolederName + ",  name = " + fi.Name + "\n";

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
            string shortname = string.Empty;
            if (flag_need_shortname == true)
            {
                //shortname = get_shortname(fi.Name);  //過濾掉檔名的一些字 用以做比較用
            }

            //richTextBox1.Text += "fname = " + fi.FullName + "\n";
            //richTextBox1.Text += "dname = " + fi.DirectoryName + "\n";

            //把資料放進 List<MyFileInfo> fileinfos 中
            fileinfos.Add(new MyFileInfo(fi.Name, fi.FullName, shortname, fi.DirectoryName, fi.Extension, fi.Length, fi.CreationTime));
        }

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

        private void button0_Click(object sender, EventArgs e)
        {
            //轉出一層 標準版
            richTextBox1.Text += "你按了 " + ((Button)sender).Name + "\n";

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

            string foldername = @"C:\______test_files1\__pic\_book_magazine";

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

        private void button1_Click(object sender, EventArgs e)
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

            string foldername = @"C:\______test_files1\__pic\_book_magazine";

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

            show_file_info();

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //尋找硬碟序號


            //读取U盘序列号


            int len = _serialNumber.Count;

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            matchDriveLetterWithSerial();

            len = _serialNumber.Count;

            richTextBox1.Text += "len = " + len.ToString() + "\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + _serialNumber[i].ToString() + "\n";

            }

        }

        private List<string> _serialNumber = new List<string>();

        /// <summary>
        /// 调用这个函数将本机所有U盘序列号存储到_serialNumber中
        /// </summary>
        private void matchDriveLetterWithSerial()
        {
            string[] diskArray;
            string driveNumber;
            var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDiskToPartition");
            foreach (ManagementObject dm in searcher.Get())
            {
                richTextBox1.Text += "A\n";
                getValueInQuotes(dm["Dependent"].ToString());
                diskArray = getValueInQuotes(dm["Antecedent"].ToString()).Split(',');
                driveNumber = diskArray[0].Remove(0, 6).Trim();
                var disks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
                foreach (ManagementObject disk in disks.Get())
                {
                    richTextBox1.Text += "B\t" + disk["Name"].ToString() + "\n";

                    if (disk["Name"].ToString() == ("\\\\.\\PHYSICALDRIVE" + driveNumber) & disk["InterfaceType"].ToString() == "USB")
                    {
                        richTextBox1.Text += "C\t" + parseSerialFromDeviceID(disk["PNPDeviceID"].ToString()) + "\n";

                        _serialNumber.Add(parseSerialFromDeviceID(disk["PNPDeviceID"].ToString()));
                    }
                }
            }
        }
        private static string parseSerialFromDeviceID(string deviceId)
        {
            var splitDeviceId = deviceId.Split('\\');
            var arrayLen = splitDeviceId.Length - 1;
            var serialArray = splitDeviceId[arrayLen].Split('&');
            var serial = serialArray[0];
            return serial;
        }

        private static string getValueInQuotes(string inValue)
        {
            var posFoundStart = inValue.IndexOf("\"");
            var posFoundEnd = inValue.IndexOf("\"", posFoundStart + 1);
            var parsedValue = inValue.Substring(posFoundStart + 1, (posFoundEnd - posFoundStart) - 1);
            return parsedValue;
        }
    }
}
