using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                        //for StreamReader, SearchOption

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
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

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

            listView1.Size = new Size(240, 240);
            listView1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            listBox1.Size = new Size(200, 240);
            listBox1.Location = new Point(x_st + dx * 3 + 250, y_st + dy * 0);

            richTextBox1.Size = new Size(450, 380);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            this.Size = new Size(1100, 700);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

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
            //撈出資料夾內的檔案(多層)
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            //單一搜尋pattern
            string[] filename = Directory.GetFiles(foldername, "*.*", SearchOption.AllDirectories);
            foreach (string fname in filename)
            {
                richTextBox1.Text += fname + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層), 所有檔案
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            foreach (string filename in Directory.GetFileSystemEntries(foldername))
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的TXT檔案(一層), 限定 *.txt
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            foreach (string filename in Directory.GetFileSystemEntries(foldername, "*.txt"))
            {
                richTextBox1.Text += filename + "\n";
            }
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
            //取得一層檔案
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            DirectoryInfo dir = new DirectoryInfo(foldername);
            FileInfo[] files = dir.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in files)
            {
                richTextBox1.Text += file.Name + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //撈出資料夾內的檔案(一層)
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            string[] files = Directory.GetFiles(foldername);
            for (int i = 0; i < files.Length; i++)
            {
                richTextBox1.Text += files[i] + "\n";
                //textBox2.Lines = files;
            }
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
            string foldername = @"C:\dddddddddd\_music_from_yt";

            export_filenames(foldername);

        }

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

        private void button11_Click(object sender, EventArgs e)
        {
            string filename_source = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            string filename_destination = @"D:\_git\vcs\_1.data\______test_files1\_cpfile\ccc.jpg";   //要寫完整檔名

            richTextBox1.Text += "檔案已存在的FileCopy/Move\n";
            try
            {
                //File.Copy(filename_source, filename_destination);     //若檔案已存在, 會出現IOException
                //File.Move(filename_source, filename_destination);     //若檔案已存在, 會出現IOException
                File.Copy(filename_source, filename_destination, true); //覆蓋檔案
                //File.Move(filename_source, filename_destination, true); //覆蓋檔案
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //Directory.Delete 目錄不是空的

            string pathname = @"D:\_git\vcs\_1.data\______test_files1\_cpfile";

            richTextBox1.Text += "Directory.Delete 目錄不是空的\n";
            try
            {
                //Directory.Delete(pathname); //若目錄不是空的, 會出現IOException
                Directory.Delete(pathname, true); //強制刪除不是空的目錄
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
            }
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

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例1
            //遍歷文件夾實例 1
            //還沒加入listView之標題

            listView1.Items.Clear();

            //遍歷文件夾實例
            //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";
            //實例化DirectoryInfo對象
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            //獲取指定目錄下的所有子目錄及文件類型
            FileSystemInfo[] fsinfos = dinfo.GetFileSystemInfos();
            foreach (FileSystemInfo fsinfo in fsinfos)
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

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例2
            //遍歷文件夾實例 2
            //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";
            DirectoryInfo TheFolder = new DirectoryInfo(foldername);

            richTextBox1.Text += "遍歷文件夾\n";
            //遍歷文件夾
            foreach (DirectoryInfo NextFolder in TheFolder.GetDirectories())
            {
                this.listBox1.Items.Add(NextFolder.Name);
                richTextBox1.Text += NextFolder.Name + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "遍歷文件\n";
            foreach (FileInfo NextFile in TheFolder.GetFiles())
            {
                this.listBox1.Items.Add(NextFile.Name);
                richTextBox1.Text += NextFile.Name + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例3
            //遍歷文件夾實例 3
            //找出資料夾內所有檔案
            //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            // Enumerate the files.
            DirectoryInfo dir_info = new DirectoryInfo(foldername);

            foreach (DirectoryInfo d_info in dir_info.GetDirectories())
            {
                richTextBox1.Text += d_info.FullName + "\n";
                richTextBox1.Text += d_info.Name + "\n";
            }

            richTextBox1.Text += "\n\n";

            foreach (FileInfo file_info in dir_info.GetFiles())
            {
                try
                {
                    richTextBox1.Text += file_info.FullName + "\n";
                    //richTextBox1.Text += file_info.Name + "\n";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error processing file '" +
                        file_info.Name + "'\n" + ex.Message,
                        "Error",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error);
                }
            } // foreach file_info
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
