﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                        //for FileAccess, File
using System.Diagnostics;               //for Process
using System.Runtime.InteropServices;   //for DllImport
using System.Globalization; //for CultureInfo

using MediaInfoNET;

namespace vcs_SendTo_All
{
    public partial class Form1 : Form
    {
        int flag_operation_mode = MODE6;

        bool flag_debug_mode = true;  //debug模式

        private const int MODE0 = 0x00;   //顯示檔案名稱
        private const int MODE1 = 0x01;   //檢視檔案內容
        private const int MODE2 = 0x02;   //簡中轉正中
        private const int MODE3 = 0x03;   //計算檔案之MD5值
        private const int MODE4 = 0x04;   //grep 一層
        private const int MODE5 = 0x05;   //grep 多層
        private const int MODE6 = 0x06;   //轉出檔案目錄資料 目錄下檔名轉出純文字 右鍵匯出資料夾內的檔案資料

        string open_folder_directory = Application.StartupPath;

        ListView listView1 = new ListView();

        bool flag_show_big_files_only = false;  //false : 顯示所有檔案, true : 僅顯示大檔
        long file_size_limit = 0;   //檔案界限

        Int64 total_size = 0;
        Int64 total_files = 0;
        Int64 total_folders = 0;
        Int64 folder_size = 0;
        Int64 folder_files = 0;

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

        //使用系統 kernel32.dll LCMapString進行轉換
        internal const int LOCALE_SYSTEM_DEFAULT = 0x0800;
        internal const int LCMAP_SIMPLIFIED_CHINESE = 0x02000000;
        internal const int LCMAP_TRADITIONAL_CHINESE = 0x04000000;
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        internal static extern int LCMapString(int Locale, int dwMapFlags, string lpSrcStr, int cchSrc, [Out] string lpDestStr, int cchDest);

        /// <summary>
        /// 將簡體中文字元轉換成繁體中文
        /// </summary>
        /// <param name="strGB2312"></param>
        /// <returns></returns>
        private string GB2312translateBig5(string strGB2312)
        {
            String tTarget = new String(' ', strGB2312.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_TRADITIONAL_CHINESE, strGB2312, strGB2312.Length, tTarget, strGB2312.Length);
            return tTarget;
        }

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
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (flag_operation_mode == MODE0)
                this.Text = "顯示檔案名稱";
            else if (flag_operation_mode == MODE1)
                this.Text = "檢視檔案內容";
            else if (flag_operation_mode == MODE2)
                this.Text = "簡中轉正中";
            else if (flag_operation_mode == MODE3)
                this.Text = "計算檔案之MD5值";
            else if (flag_operation_mode == MODE6)
            {
                //this.Text = "右鍵匯出資料夾內的檔案資料";
                flag_show_big_files_only = Properties.Settings.Default.show_big_files_only;
                if (flag_show_big_files_only == false)
                {
                    richTextBox1.Text += "顯示所有檔案\n";
                    this.Text = "轉出檔案目錄資料 目錄下檔名轉出純文字(全部)";
                }
                else
                {
                    richTextBox1.Text += "僅顯示大檔\n";
                    this.Text = "轉出檔案目錄資料 目錄下檔名轉出純文字(僅大檔)";
                }
                //檔案界限
                file_size_limit = Properties.Settings.Default.file_size_limit * 1024 * 1024;
                richTextBox1.Text += "檔案界限 : " + Properties.Settings.Default.file_size_limit.ToString() + " MB\n\n";
            }
            else
                this.Text = "未定義";

            show_item_location();

            /* debug
            string sendto_folder = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
            richTextBox1.Text += "[傳送到]資料夾位置:\n" + sendto_folder + "\n";
            richTextBox1.Text += "檔案總管 右鍵 傳送到 XXX, 可用XXX開啟檔案\n\n拉一個捷徑到\n%APPDATA%\\Microsoft\\Windows\\SendTo\n或\n" + sendto_folder;
            */

            int len = System.Environment.GetCommandLineArgs().Length;
            int i;
            //richTextBox1.Text += "參數長度\t" + len.ToString() + "\t分別是:\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "第 " + i.ToString() + " 項\t" + System.Environment.GetCommandLineArgs()[i] + "\n";
            }

            List<String> filenames = new List<String>();

            for (i = 1; i < len; i++)
                filenames.Add(System.Environment.GetCommandLineArgs()[i]);

            filenames.Sort();

            fileinfos.Clear();
            total_size = 0;
            total_files = 0;

            for (i = 0; i < (len - 1); i++)
            {
                string filename = filenames[i];

                if (flag_operation_mode == MODE0)
                {
                    richTextBox1.Text += filename + "\t";

                    if (System.IO.File.Exists(filename) == true)
                    {
                        FileInfo fi;

                        try
                        {   //可能會產生錯誤的程式區段
                            fi = new FileInfo(filename);
                            richTextBox1.Text += "檔案, 大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

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
                    }
                    else if (Directory.Exists(filename) == true)
                    {
                        richTextBox1.Text += "資料夾\n";
                    }
                    else
                    {
                        richTextBox1.Text += "XXXXXXXXXXXX\n";
                    }
                }
                else if (flag_operation_mode == MODE1)
                {
                    //檢視檔案內容
                    print_file_content(filename);
                }
                else if (flag_operation_mode == MODE2)
                {
                    //簡中轉正中
                    convert_sc_to_tc(filename);
                }
                else if (flag_operation_mode == MODE6)
                {
                    //轉出檔案目錄資料 目錄下檔名轉出純文字 全部
                    export_filename(filename);//轉出檔案目錄資料 目錄下檔名轉出純文字

                    richTextBox1.Text += "右鍵匯出資料夾內的檔案資料1\n";
                    richTextBox1.Text += filename + "\n";
                }
            }

            if (flag_operation_mode == MODE6)
            {
                //顯示檔案目錄資料
                show_filename_data();
            }

            if (flag_debug_mode == true)
            {
                //以下為 MODE6 的 debug
                if (flag_operation_mode == MODE6)
                {
                    richTextBox1.Text += "右鍵匯出資料夾內的檔案資料2 debug\n";
                    fileinfos.Clear();
                    total_size = 0;
                    total_files = 0;

                    //string foldername = @"D:\vcs\astro\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案\小赠品";
                    string foldername = @"D:\內視鏡影片\錄影效果比較";
                    export_filename(foldername);//轉出檔案目錄資料 目錄下檔名轉出純文字

                    //顯示檔案目錄資料
                    show_filename_data();

                    show_listView();
                }
            }
        }

        void show_item_location()
        {
            richTextBox1.Dock = DockStyle.Fill;
            bt_copy.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width, 0);
            bt_save.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width * 2, 0);
            bt_open_folder.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width * 2, 0 + bt_refresh.Size.Height);
            bt_refresh.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width * 2, 0 + bt_refresh.Size.Height*2);
            bt_clear.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width, 0 + bt_setup.Size.Height);
            bt_setup.Location = new Point(this.ClientSize.Width - bt_copy.Size.Width, 0 + bt_setup.Size.Height * 2);

            bt_open_folder.BackgroundImage = vcs_SendTo_All.Properties.Resources.folder_open;
            bt_refresh.BackgroundImage = vcs_SendTo_All.Properties.Resources.refresh;
        }

        void show_listView()
        {
            this.Size = new Size(640 * 2, 480 * 2);

            //richTextBox1.Dock = DockStyle.Right;

            richTextBox1.Text += "W = " + this.ClientSize.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + this.ClientSize.Height.ToString() + "\n";

            richTextBox1.Text += "W = " + richTextBox1.Size.Width.ToString() + "\n";
            richTextBox1.Text += "H = " + richTextBox1.Size.Height.ToString() + "\n";

            //richTextBox1.Visible = false;
            richTextBox1.Dock = DockStyle.None;
            richTextBox1.Size = new Size(1000, 400);
            richTextBox1.Location = new Point(0, 400);

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.Clear();

            this.listView1.GridLines = true;
            this.listView1.Size = new Size(640 * 2, 480 * 2);

            listView1.Columns.Add("影片1", 200, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 50, HorizontalAlignment.Left);
            listView1.Columns.Add("檔名1", 400, HorizontalAlignment.Left);
            listView1.Columns.Add("資料夾", 900, HorizontalAlignment.Left);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Left);
            listView1.Columns.Add("副檔名", 100, HorizontalAlignment.Left);
            listView1.Columns.Add("修改日期", 100, HorizontalAlignment.Left);
            listView1.Visible = true;
            listView1.MouseClick += new MouseEventHandler(listView1_MouseClick);

            this.Controls.Add(listView1);


            //加入

        }

        private void listView1_MouseClick(object sender, MouseEventArgs e)
        {
            /*
            int selNdx;
            string fullname;

            selNdx = listView1.SelectedIndices[0];


            richTextBox1.Text += "aaa:\t" + listView1.Items[selNdx].Text + "\n";
            richTextBox1.Text += "bbb:\t" + listView1.Items[selNdx].SubItems[1].Text + "\n";
            richTextBox1.Text += "ccc:\t" + listView1.Items[selNdx].SubItems[2].Text + "\n";
            richTextBox1.Text += "ddd:\t" + listView1.Items[selNdx].SubItems[3].Text + "\n";
            */

        }

        void show_filename_data()
        {
            int i;
            if (fileinfos.Count == 0)
                richTextBox1.Text += "show_filename_data 找不到資料\n";
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料a\n";

            for (i = 0; i < fileinfos.Count; i++)
            {
                string filename = fileinfos[i].filename;
                //richTextBox1.Text += filename + "\n";

                FileInfo fi = new FileInfo(fileinfos[i].filepath + "\\" + filename);
                richTextBox1.Text += fi.FullName + "\t";
                //richTextBox1.Text += fi.Length.ToString() + "\t";
                richTextBox1.Text += ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                MediaFile f = new MediaFile(fileinfos[i].filepath + "\\" + filename);

                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    /*
                    richTextBox1.Text += "影片檔案\t"+w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\t";
                    richTextBox1.Text += f.Video[0].FrameRate.ToString() + "\t";
                    richTextBox1.Text += f.General.DurationString + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "非 影片檔案\n";
                }
            }
        }

        private void bt_copy_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }

        void print_file_content(string filename)
        {
            richTextBox1.Text += "\n#檔案 : " + filename + "\n\n";

            /*
            //二進位檔轉成文字檔
            byte[] data;
            long len;
            int i;

            //全部binary讀取
            data = System.IO.File.ReadAllBytes(filename);
            len = data.Length;

            //richTextBox1.Text += "檔案名稱 : " + filename + "\n";
            //richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";
            //print_data(data, len);

            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

            return;
            */

            //純文字
            StringBuilder sb = new StringBuilder();

            string[] Txt_All_Lines = System.IO.File.ReadAllLines(filename, Encoding.GetEncoding("utf-8"));   //指名編碼格式

            foreach (string Single_Line in Txt_All_Lines)
            {
                sb.AppendLine(Single_Line);
            }

            richTextBox1.Text += sb.ToString() + "\n";
            richTextBox1.Text += "print(\"------------------------------------------------------------\")  # 60個\n";
        }

        void convert_sc_to_tc(string filename)
        {
            richTextBox1.Text += "\n#檔案 : " + filename + "\n\n";

            if (System.IO.File.Exists(filename) == true)  //確認檔案是否存在
            {
                richTextBox1.Text += "檔名(包含副檔名)： " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名)： " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名： " + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "根目錄： " + Path.GetPathRoot(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetDirectoryName(filename) + "\n";

                string fore_filename = Path.GetFileNameWithoutExtension(filename);
                string ext_filename = Path.GetExtension(filename);
                string foldername = Path.GetDirectoryName(filename);
                string backup_filename = Path.Combine(foldername, fore_filename + "_old" + ext_filename);

                richTextBox1.Text += "新檔名： " + backup_filename + "\n";

                if (System.IO.File.Exists(backup_filename) == false)
                {
                    System.IO.File.Copy(filename, backup_filename);     //若檔案已存在, 會出現IOException
                }
                else
                {
                    MessageBox.Show("備份檔案已存在, 跳過");
                    return;
                }
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                return;
            }

            try
            {
                string all_text = System.IO.File.ReadAllText(filename, Encoding.UTF8);

                //簡中轉正中
                string all_tc_text = GB2312translateBig5(all_text);

                //string filename_new = @"C:\_git\vcs\_4.python\test10_new08_test_sc_tc_ccccc.py";
                //覆蓋原檔
                FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
                StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);   //指名編碼格式            
                sw.Write(all_tc_text);
                sw.Close();

                MessageBox.Show("簡中轉正中完成, 檔名 : " + filename);
            }
            catch (FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }
        }

        //轉出檔案目錄資料 目錄下檔名轉出純文字
        void export_filename(string target_dir)
        {
            if (Directory.Exists(target_dir) == false)     //確認資料夾是否存在
                return;
            //撈出多層
            //richTextBox1.Text += "資料夾: " + target_dir + "\n";
            ShowDirectory(target_dir);
        }

        public bool ShowDirectory(string target_dir)
        {
            bool result = false;
            string[] files = Directory.GetFiles(target_dir);
            string[] dirs = Directory.GetDirectories(target_dir);
            //richTextBox1.Text += "資料夾: " + target_dir + "\t檔案個數 = " + files.Length.ToString() + "\n";

            foreach (string file in files)
            {
                FileInfo fi = new FileInfo(file);
                long filesize = fi.Length;

                /*
                richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;
                */

                if ((flag_show_big_files_only == false) || (filesize > file_size_limit))
                {
                    richTextBox1.Text += "檔案: " + file + "\t";
                    richTextBox1.Text += "Size: " + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";

                    string FolederName = fi.Directory.ToString();
                    fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
                }
            }
            richTextBox1.Text += "\n";
            foreach (string dir in dirs)
            {
                //richTextBox1.Text += "資料夾: " + dir + "\n";
                ShowDirectory(dir);
            }
            return result;
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            int i;
            if (fileinfos.Count == 0)
            {
                richTextBox1.Text += "show_filename_data 找不到資料\n";
                richTextBox1.Text += "無資料, 不存檔\n";
            }
            else
                richTextBox1.Text += "找到 " + fileinfos.Count.ToString() + " 筆資料a\n";

            string save_filename = "filename_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileStream filestream = System.IO.File.Open(save_filename, FileMode.Create);
            StreamWriter str_writer = new StreamWriter(filestream);

            // RTB 直接存檔
            //str_writer.WriteLine(richTextBox1.Text);

            // 只存檔案名稱資料
            for (i = 0; i < fileinfos.Count; i++)
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

                MediaFile f = new MediaFile(fileinfos[i].filepath + "\\" + filename);

                if ((f.InfoAvailable == true) && (f.Video.Count > 0))
                {
                    int w = f.Video[0].Width;
                    int h = f.Video[0].Height;
                    /*
                    richTextBox1.Text += "影片檔案\t"+w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\t";
                    richTextBox1.Text += f.Video[0].FrameRate.ToString() + "\t";
                    richTextBox1.Text += f.General.DurationString + "\n";
                    */
                    //mesg += "\t" + w.ToString() + " × " + h.ToString() + "(" + ((double)w / (double)h).ToString("N2", CultureInfo.InvariantCulture) + ":1)" + "\t";
                    //mesg += f.Video[0].FrameRate.ToString() + "\t";
                    //mesg += f.General.DurationString;
                }
                else
                {
                    richTextBox1.Text += "非 影片檔案\n";
                }

                richTextBox1.Text += mesg+"\n";
                str_writer.WriteLine(mesg);


            }

            // Dispose StreamWriter
            str_writer.Dispose();
            // Close FileStream
            filestream.Close();

            richTextBox1.Text += "儲存資料完畢，檔案：" + save_filename + "\n";

            /* 使用對話框選取檔案再存檔
            saveFileDialog1.Title = "儲存資料";
            saveFileDialog1.FileName = filename;
            saveFileDialog1.Filter = "文字檔|*.txt|所有檔|*.*";   //限定檔案格式
            saveFileDialog1.FilterIndex = 1;
            saveFileDialog1.RestoreDirectory = true;
            saveFileDialog1.InitialDirectory = Application.StartupPath; //從目前目錄開始尋找檔案

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
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
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
            */
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            //設定頁
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_refresh_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 refresh\n";
        }

        private void Form1_SizeChanged(object sender, EventArgs e)
        {
            show_item_location();
        }

        private void bt_open_folder_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            Process.Start(open_folder_directory);
        }
    }
}
