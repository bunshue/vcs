using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for StreamReader, SearchOption
using System.Runtime.InteropServices;   //for DllImport, Marshal, StructLayout
using System.Diagnostics;  // for Stopwatch

namespace vcs_DiskDirectoryFile2
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
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(530, 690);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1200, 750);
            this.Text = "vcs_DiskDirectoryFile2";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層)
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            SearchOption search_option;
            search_option = SearchOption.TopDirectoryOnly;
            //string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };     //指名搜尋pattern
            string[] patterns = { "*.*" };  //指名搜尋pattern
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(foldername, pattern, search_option))
                {
                    richTextBox1.Text += filename + "\n";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(多層)
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            SearchOption search_option;
            search_option = SearchOption.AllDirectories;
            //string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" }; //指名搜尋pattern
            string[] patterns = { "*.*" };  //指名搜尋pattern

            //多個搜尋pattern
            foreach (string pattern in patterns)
            {
                string[] filename = Directory.GetFiles(foldername, pattern, search_option);
                foreach (string fname in filename)
                {
                    richTextBox1.Text += fname + "\n";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層), 所有檔案
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            foreach (string filename in Directory.GetFileSystemEntries(foldername))
            {
                richTextBox1.Text += filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的TXT檔案(一層), 限定 *.txt
            foldername = @"D:\_git\vcs\_1.data\______test_files1";

            foreach (string filename in Directory.GetFileSystemEntries(foldername, "*.txt"))
            {
                richTextBox1.Text += filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            //取得一層檔案
            foldername = @"D:\_git\vcs\_1.data\______test_files1";

            DirectoryInfo dir = new DirectoryInfo(foldername);
            FileInfo[] files = dir.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in files)
            {
                richTextBox1.Text += file.Name + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的檔案(一層)
            foldername = @"D:\_git\vcs\_1.data\______test_files1";
            /*
            string[] files = Directory.GetFiles(foldername);
            for (int i = 0; i < files.Length; i++)
            {
                richTextBox1.Text += files[i] + "\n";
                //textBox2.Lines = files;
            }
            */

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的檔案(多層)
            foldername = @"D:\_git\vcs\_1.data\______test_files1";

            /*
            //單一搜尋pattern
            string[] filename = Directory.GetFiles(foldername, "*.*", SearchOption.AllDirectories);
            foreach (string fname in filename)
            {
                richTextBox1.Text += fname + "\n";
            }
            */

        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //搜尋子目錄內的所有檔案   一層
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            int cnt = 0;
            DirectoryInfo dir = new DirectoryInfo(foldername);
            richTextBox1.Text += "搜尋子目錄內的所有檔案, 子目錄 : " + dir.ToString() + "\n";

            DirectoryInfo[] dddd = dir.GetDirectories();
            cnt = 0;
            richTextBox1.Text += "子目錄 :\n";
            foreach (DirectoryInfo d in dddd)
            {
                cnt++;
                //richTextBox1.Text += cnt.ToString() + "\t" + d + "\n";
                richTextBox1.Text += d + "\n";
            }

            FileInfo[] aaaa = dir.GetFiles();
            cnt = 0;
            richTextBox1.Text += "子目錄 " + dir.Name + " 下的檔案 :\n";
            foreach (FileInfo b in aaaa)
            {
                cnt++;
                //richTextBox1.Text += cnt.ToString() + "\t" + b + "\n";
                richTextBox1.Text += b + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //轉出一層
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";
            if (foldername.CompareTo("") == 0)
                return;
            DirectoryInfo dir = new DirectoryInfo(foldername);
            DirectoryInfo[] dirs = dir.GetDirectories();
            FileInfo[] files = dir.GetFiles();

            //顯示本機文件夾及文件
            //資料夾部分
            foreach (DirectoryInfo di in dirs)
            {
                string str1 = di.Name;
                string str2 = di.FullName;
                string str3 = di.LastAccessTime.ToString();
                richTextBox1.Text += str1 + "\t" + str2 + "\t" + str3 + "\n";
            }

            //檔案部分
            foreach (FileInfo fi in files)
            {
                string str4 = fi.Name;
                string str5 = fi.FullName;
                string str6 = fi.Length.ToString();
                richTextBox1.Text += str4 + "\t" + str5 + "\t" + str6 + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

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

        public class MyFileInfo
        {
            public string filename;
            public string filepath;
            public string fileextension;
            public long filesize;
            public DateTime filecreationtime;

            public MyFileInfo(string n, string p, string e, long s, DateTime c)
            {
                this.filename = n;
                this.filepath = p;
                this.fileextension = e;
                this.filesize = s;
                this.filecreationtime = c;
            }
        }

        List<MyFileInfo> fileinfos = new List<MyFileInfo>();

        string FolederName;
        Int64 total_size = 0;
        Int64 total_files = 0;

        Int64 folder_size = 0;
        Int64 folder_files = 0;


        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
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
                    FolederName = subdirectory;
                    richTextBox1.Text += "\n\n" + FolederName + "\n";
                    ProcessDirectory(subdirectory);
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
            }

            /*
            richTextBox1.Text += "資料夾 " + targetDirectory + "\t檔案個數 : " + folder_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(folder_size)) + "\n";
            richTextBox1.Text += "\n";
            */
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

            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
            //richTextBox1.Text += fi.FullName + "\n";

            fileinfos.Add(new MyFileInfo(fi.Name, FolederName, fi.Extension, fi.Length, fi.CreationTime));
        }

        void export_filenames(string foldername)
        {
            fileinfos.Clear();

            richTextBox1.Text += "\n搜尋路徑" + foldername + "\n";

            if (File.Exists(foldername))
            {
                //給定的路徑是一個檔案
                ProcessFile(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(foldername))
            {
                //給定的路徑是一個資料夾
                FolederName = foldername;
                ProcessDirectory(foldername);
                richTextBox1.Text += "\n資料夾 " + foldername + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else
            {
                richTextBox1.Text += "非合法路徑或檔案\n";
            }


            richTextBox1.Text += "\n\n\n";


            richTextBox1.Text += "fileinfos len = " + fileinfos.Count.ToString() + "\n";

            richTextBox1.Text += "total_size = " + total_size.ToString() + "\n";
            richTextBox1.Text += "total_files = " + total_files.ToString() + "\n";
            //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
            //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            //string foldername = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\";
            //string foldername = @"C:\dddddddddd\_music_from_yt";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1\";

            export_filenames(foldername);
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            int i;
            int len = fileinfos.Count;

            if (len <= 0)
            {
                richTextBox1.Text += "無檔案\n";
                return;
            }

            richTextBox1.Text += "照檔名排序:\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\n";
                richTextBox1.Text += fileinfos[i].filename + "\n";
            }

            richTextBox1.Text += "照大小排序(由大到小):\n";

            //排序 由大到小  在return的地方多個負號
            fileinfos.Sort((x, y) => { return -x.filesize.CompareTo(y.filesize); });

            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";
                richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\n";
            }

            richTextBox1.Text += "照大小排序(由小到大):\n";

            //排序 由小到大
            fileinfos.Sort((x, y) => { return x.filesize.CompareTo(y.filesize); });

            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\t" + fileinfos[i].filepath + "\t" + fileinfos[i].fileextension + "\t" + fileinfos[i].filecreationtime.ToString() + "\n";
                richTextBox1.Text += "i = " + i.ToString() + "\t" + fileinfos[i].filename + "\t" + fileinfos[i].filesize.ToString() + "\n";
            }
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
                //richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                //richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                filesize = fi.Length;
                //richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                //richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                //richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;

                Stopwatch stopwatch = new Stopwatch();

                // Begin timing
                stopwatch.Start();

                FileStream sourceFile = new FileStream(filename, FileMode.Open, FileAccess.Read);
                //sourceFile 來源檔要先在該路徑中準備好

                FileStream targetFile = new FileStream(@"G:\tmp.mp4", FileMode.Create, FileAccess.Write);

                if (mode == MODE1)
                {
                    int bb = -1;
                    while ((bb = sourceFile.ReadByte()) != -1)
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

                // Stop timing
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

        private void button11_Click(object sender, EventArgs e)
        {
            //拷貝檔案1
            copy_file(MODE1);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //拷貝檔案2
            copy_file(MODE2);
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        //根據文件頭判斷上傳的文件類型 ST
        private void button16_Click(object sender, EventArgs e)
        {
            //根據文件頭判斷上傳的文件類型
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_哆啦A夢\doraemon1.jpg";
            string result = getFileType(filename);
            richTextBox1.Text += "File Type : " + result + "\n";
        }
        /// 根據文件頭判斷上傳的文件類型
        /// <param name="filePath">filePath是文件的完整路徑 </param>
        /// <returns>返回true或false</returns>
        public string getFileType(string filePath)
        {
            try
            {
                FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read);
                BinaryReader reader = new BinaryReader(fs);
                string fileClass;
                byte buffer;
                buffer = reader.ReadByte();
                fileClass = buffer.ToString();
                buffer = reader.ReadByte();
                fileClass += buffer.ToString();
                reader.Close();
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
        //根據文件頭判斷上傳的文件類型 SP

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

        private void button17_Click(object sender, EventArgs e)
        {
            //取得檔案類型

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string fileTypeName = GetTypeName(filename);

            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案類型 : " + fileTypeName + "\n";
        }
        //取得檔案類型 SP

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        FileStream FormerOpen;
        FileStream ToFileOpen;
        /// <summary>
        /// 文件的複製
        /// </summary>
        /// <param FormerFile="string">源文件路徑</param>
        /// <param toFile="string">目的文件路徑</param> 
        /// <param SectSize="int">傳輸大小</param> 
        /// <param progressBar="ProgressBar">ProgressBar控制元件</param> 
        public void CopyFile(string FormerFile, string toFile, int SectSize)
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

        private void button20_Click(object sender, EventArgs e)
        {
            //拷貝檔案, 限定拷貝大小
            //拷貝檔案, 限定拷貝大小, 每次拷貝1024拜

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            string filename2 = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            CopyFile(filename1, filename2, 1024);
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
            //偵測原始檔案類型

            OpenFileDialog openFileDialog1 = new OpenFileDialog();
            openFileDialog1.Title = "偵測原始檔案類型";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            //openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            //openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "檔案 : " + openFileDialog1.FileName + "\n";
                //richTextBox1.Text += "長度 : " + openFileDialog1.FileName.Length.ToString() + "\n";

                int len = openFileDialog1.FileName.Length;

                if (len < 10)
                {
                    richTextBox1.Text += "檔案太小, 忽略";
                    return;
                }

                len = 10;
                int[] data = new int[len];
                string builtHex = string.Empty;
                using (Stream S = File.OpenRead(openFileDialog1.FileName))
                {
                    for (int i = 0; i < 10; i++)
                    {
                        data[i] = S.ReadByte();
                        builtHex += data[i].ToString("X2") + " ";

                        //builtHex += S.ReadByte().ToString("X2");

                        /*
                        if (ImageTypes.ContainsKey(builtHex))
                        {
                            string 真實副檔名 = ImageTypes[builtHex];
                            break;
                        }
                        */
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
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
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


/*  可搬出

*/


