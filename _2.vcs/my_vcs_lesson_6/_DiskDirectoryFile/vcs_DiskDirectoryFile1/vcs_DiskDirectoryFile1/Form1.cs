using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory
using System.Collections;   //for ArrayList

using Microsoft.VisualBasic.FileIO;

namespace vcs_DiskDirectoryFile1
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
            y_st = 30;
            dx = 200 + 10;
            dy = 50 + 5;

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 20);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 20);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 20);

            bt_file00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_file01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_file02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_file03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_file04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            bt_file05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_file06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            bt_file07.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            bt_file08.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            bt_file09.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            bt_file10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            bt_file11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            bt_file12.Location = new Point(x_st + dx * 0, y_st + dy * 12);

            bt_dir00.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_dir01.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_dir02.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_dir03.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_dir04.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_dir05.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            bt_dir06.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            bt_dir07.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            bt_dir08.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            bt_dir09.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            bt_dir10.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            bt_dir11.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            bt_dir12.Location = new Point(x_st + dx * 1, y_st + dy * 12);

            bt_files00.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_files01.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_files02.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_files03.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            bt_files04.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            bt_files05.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            bt_files06.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            bt_files07.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            bt_files08.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            bt_files09.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            bt_files10.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            bt_files11.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            bt_files12.Location = new Point(x_st + dx * 2, y_st + dy * 12);

            richTextBox1.Size = new Size(400, 600);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1100, 800);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        public bool DeleteDirectory(string target_dir)
        {
            bool result = false;
            string[] files = Directory.GetFiles(target_dir);
            string[] dirs = Directory.GetDirectories(target_dir);
            foreach (string file in files)
            {
                richTextBox1.Text += "刪除檔案: " + file + "\n";
                File.SetAttributes(file, FileAttributes.Normal);
                File.Delete(file);
            }
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "刪除資料夾: " + dir + "\n";
                DeleteDirectory(dir);
            }
            Directory.Delete(target_dir, false);
            return result;
        }

        // 此方法所接收的兩個字串代表您所要比較的兩個檔案。
        // 如果兩個檔案的內容完全相同，將傳回 True；任何其他
        // 的傳回值都表示這兩個檔案的內容有所差異。
        private bool FileCompare(string file1, string file2)
        {
            // 判斷相同的檔案是否被參考兩次。
            if (file1 == file2)
            {
                return true;
            }

            int file1byte = 0;
            int file2byte = 0;
            using (FileStream fs1 = new FileStream(file1, FileMode.Open), fs2 = new FileStream(file2, FileMode.Open))
            {
                // 檢查檔案大小。如果兩個檔案的大小並不相同，則視為不相同。
                if (fs1.Length != fs2.Length)
                {
                    // 關閉檔案。
                    fs1.Close();
                    fs2.Close();
                    return false;
                }

                // 逐一比較兩個檔案的每一個位元組，直到發現不相符或已到達檔案尾端為止。

                do
                {
                    // 從每一個檔案讀取一個位元組。
                    file1byte = fs1.ReadByte();
                    file2byte = fs2.ReadByte();
                }
                while ((file1byte == file2byte) && (file1byte != -1));
                // 關閉檔案。
                fs1.Close();
                fs2.Close();
            }

            // 傳回比較的結果。在這個時候，只有當兩個檔案
            // 的內容完全相同時，"file1byte" 才會等於 "file2byte"。
            return ((file1byte - file2byte) == 0);
        }

        //刪除資料夾，recursive為True時，直接刪除資料夾及其資料夾下所有文件或資料夾;recursive為False時，需先將資料夾下所有文件或資料夾刪除
        private void DeleteDirectory(string path, bool recursive)
        {
            if (Directory.Exists(path))     //確認資料夾是否存在
            {
                if (recursive)
                {
                    Directory.Delete(path, true);
                    richTextBox1.Text += "已刪除資料夾: " + path + "\n";
                }
                else
                    richTextBox1.Text += "需要先把資料夾內的檔案刪除\n";
            }
        }

        public static double DirSize(DirectoryInfo d)
        {
            double Size = 0;
            // Add file sizes.
            FileInfo[] fis = d.GetFiles();
            foreach (FileInfo fi in fis)
            {
                Size += fi.Length;
            }
            // Add subdirectory sizes.
            DirectoryInfo[] dis = d.GetDirectories();
            foreach (DirectoryInfo di in dis)
            {
                if (di.Name != "System Volume Information" && di.Name.Substring(0, 1) != "$")//避開此類folder權限問題
                    Size += DirSize(di);   //利用遞迴把子資料夾也計算進來
            }
            return (Size);
        }

        string message = "";
        double filesize_all = 0;

        public void GetAllFileNames(DirectoryInfo d)
        {
            // Add file sizes.
            FileInfo[] fis = d.GetFiles();
            foreach (FileInfo fi in fis)
            {
                message += fi.Name;
                message += "\t";
                message += fi.Length.ToString(); ;
                message += Environment.NewLine;
                filesize_all += fi.Length;
            }
            // Add subdirectory sizes.
            DirectoryInfo[] dis = d.GetDirectories();
            foreach (DirectoryInfo di in dis)
            {
                if (di.Name != "System Volume Information" && di.Name.Substring(0, 1) != "$")//避開此類folder權限問題
                {
                    GetAllFileNames(di);   //利用遞迴把子資料夾也加進來
                }
            }
            message += Environment.NewLine;
        }

        private void bt_file00_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaa.txt";
            string filename2 = @"D:/_git/vcs/_1.data/______test_files2/aaaa.txt";

            if (File.Exists(filename1) == false)            //確認檔案是否存在
                richTextBox1.Text += "檔案: " + filename1 + " 不存在\n";
            else
                richTextBox1.Text += "檔案: " + filename1 + " 存在\n";

            if (File.Exists(filename2) == false)  //確認檔案是否存在
                richTextBox1.Text += "檔案: " + filename2 + " 不存在\n";
            else
                richTextBox1.Text += "檔案: " + filename2 + " 存在\n";
        }

        private void bt_file01_Click(object sender, EventArgs e)
        {
            //建立檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaab.txt";
            if (File.Exists(filename) == false)         //確認檔案是否存在
            {
                File.Create(filename);
                richTextBox1.Text += "檔案: " + filename + " 不存在, 已建立\n";
            }
            else
                richTextBox1.Text += "檔案: " + filename + " 已存在, 無法再建立\n";

            //建立檔案
            string destFileName = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";
            FileStream fs = File.Create(destFileName);
            fs.Close();
            richTextBox1.Text += "已建立檔案: " + destFileName + "\n";

        }

        private void bt_file02_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaab.txt";

            if (File.Exists(filename1) == false)    //確認原始檔案是否存在
            {
                richTextBox1.Text += "原始檔案: " + filename1 + " 不存在, 無法拷貝\n";
                return;
            }
            if (File.Exists(filename2) == false)    //確認目標檔案是否存在
            {
                // Copy the file.
                File.Copy(filename1, filename2);
                richTextBox1.Text += "目標檔案: " + filename2 + " 不存在, 已拷貝\n";
            }
            else
                richTextBox1.Text += "檔案: " + filename2 + " 已存在, 無法再拷貝\n";

            //複製檔案，從 sourceFileName 複製到 destFileName
            string sourceFileName = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string destFileName = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";

            if (File.Exists(sourceFileName))    //確認原始檔案是否存在
            {
                if (!File.Exists(destFileName)) //確認目標檔案是否存在
                {
                    File.Copy(sourceFileName, destFileName);
                    richTextBox1.Text += "已複製檔案: " + sourceFileName + " 到 " + destFileName + "\n";
                }
                else
                    richTextBox1.Text += "目標檔案: " + destFileName + " 已存在，無法複製\n";

            }
            else
                richTextBox1.Text += "原始檔案: " + sourceFileName + " 不存在，無法複製\n";


        }

        private void bt_file03_Click(object sender, EventArgs e)
        {
            //刪除檔案
            //法一
            string filename = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaab.txt";
            if (File.Exists(filename) == false)     //確認檔案是否存在
                richTextBox1.Text += "檔案: " + filename + " 不存在, 無法刪除\n";
            else
            {
                File.Delete(filename);
                richTextBox1.Text += "檔案: " + filename + " 存在, 已刪除\n";
            }

            //刪除檔案
            //法二
            FileInfo f = new FileInfo(@"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt");
            if (f.Exists)       //確認檔案是否存在
            {
                f.Delete();
                richTextBox1.Text += "檔案刪除成功\n";
            }
            else
                richTextBox1.Text += "找不到檔案\n";

            string destFileName = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";
            string destFileName2 = @"D:\_git\vcs\_1.data\______test_files1\picture1b.jpg";

            //刪除檔案
            if (File.Exists(destFileName))      //確認檔案是否存在
            {
                File.Delete(destFileName);
                richTextBox1.Text += "已刪除檔案: " + destFileName + "\n";
            }
            else
                richTextBox1.Text += "檔案: " + destFileName + " 不存在，無法刪除\n";

            //刪除檔案
            if (File.Exists(destFileName2))     //確認檔案是否存在
            {
                File.Delete(destFileName2);
                richTextBox1.Text += "已刪除檔案: " + destFileName2 + "\n";
            }
            else
                richTextBox1.Text += "檔案: " + destFileName2 + " 不存在，無法刪除\n";

        }

        private void bt_file04_Click(object sender, EventArgs e)
        {
            //刪除檔案(使用資源回收筒)

            //先將Microsoft.VisualBasic.Dll加入參考。
            //參考/加入參考/.NET/Microsoft.VisualBasic
            //加上 using Microsoft.VisualBasic.FileIO;    //引用Microsoft.VisualBasic.FileIO命名空間。

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                FileSystem.DeleteFile(openFileDialog1.FileName, UIOption.OnlyErrorDialogs, RecycleOption.SendToRecycleBin);
                richTextBox1.Text += "已將檔案 : " + openFileDialog1.FileName + " 移至資源回收筒\n";
            }
            else
                richTextBox1.Text += "未選取檔案\n";
        }

        private void bt_file05_Click(object sender, EventArgs e)
        {
            string sourceFileName = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";
            string destFileName = @"D:\_git\vcs\_1.data\______test_files1\picture1b.jpg";

            //移動檔案，從 sourceFileName 移動到 destFileName
            if (File.Exists(sourceFileName))        //確認原始檔案是否存在
            {
                if (!File.Exists(destFileName))     //確認目標檔案是否存在
                {
                    File.Move(sourceFileName, destFileName);
                    richTextBox1.Text += "已移動檔案: " + sourceFileName + " 到 " + destFileName + "\n";
                }
                else
                    richTextBox1.Text += "檔案: " + destFileName + " 已存在，無法移動\n";
            }
            else
                richTextBox1.Text += "檔案: " + sourceFileName + " 不存在，無法移動\n";

        }

        private void bt_file06_Click(object sender, EventArgs e)
        {
            //取得檔案資訊
            //法一
            string filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.old.txt";
            if (File.Exists(filename) == false)   //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
            }
            else
            {
                //建立日期 2016  3 31 020339
                //修改日期 2016  7 18 010548
                //存取日期 2016  3 31 020339
                richTextBox1.Text += "檔案: " + filename + " 已存在\n";
                richTextBox1.Text += "建立時間: " + File.GetCreationTime(filename) + "\n";
                richTextBox1.Text += "修改時間: " + File.GetLastWriteTime(filename) + "\n";
                richTextBox1.Text += "存取時間: " + File.GetLastAccessTime(filename) + "\n";
                richTextBox1.Text += "檔案屬性: " + File.GetAttributes(filename).ToString() + "\n";
            }

            //法二
            FileInfo fi = new FileInfo(filename);
            if (fi.Exists == true)      //確認檔案是否存在
            {
                richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;
            }
            else
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";

        }

        private void bt_file07_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1bb\eula.3086b.txt";
            if (File.Exists(filename))      //確認檔案是否存在
            {
                richTextBox1.Text += "取得完整路徑檔名:\t" + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "取得路徑:\t\t" + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "取得檔名(包含附檔名):\t" + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "取得檔名(不包含附檔名):\t" + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "取得副檔名:\t\t" + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "資料根目錄:\t\t" + Path.GetPathRoot(filename) + "\n";
                richTextBox1.Text += "修改成完整時間檔名:\t" + Path.GetDirectoryName(filename) + "\\" + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "修改成時間檔名:\t\t" + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
            }
            richTextBox1.ScrollToCaret();   //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void bt_file08_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_case1\_case1a\eula.3085.txt";
            if (File.Exists(filename))  //確認檔案是否存在
            {
                richTextBox1.Text += "檔名(包含副檔名)： " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名)： " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名： " + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "根目錄： " + Path.GetPathRoot(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "路徑： " + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "取得任意檔名： " + Path.GetRandomFileName() + "\n";
                richTextBox1.Text += "取得臨時檔名： " + Path.GetTempFileName() + "\n";
                richTextBox1.Text += "取得臨時路徑： " + Path.GetTempPath() + "\n";
            }
            else
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";

        }

        private void bt_file09_Click(object sender, EventArgs e)
        {
            string pathname = @"D:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1bb\";
            string foldername = "";
            int got_slash = 0;
            richTextBox1.Text += "length = " + pathname.Length.ToString() + "\n";
            for (int i = (pathname.Length - 1); i >= 0; i--)
            {
                if (pathname[i] == '\\')
                {
                    got_slash++;
                    if (got_slash == 2)
                    {
                        richTextBox1.Text += "got \\ in length = " + i.ToString() + "\n";
                        //foldername = pathname.Substring(i,pathname.Length-2);
                        foldername = pathname.Substring(i + 1, pathname.Length - i - 2);
                        richTextBox1.Text += "path name = " + pathname + "\n";
                        richTextBox1.Text += "folder name = " + foldername + "\n";

                        break;
                    }
                }
            }
            richTextBox1.ScrollToCaret();   //RichTextBox顯示訊息自動捲動，顯示最後一行

        }

        int attr = 0;
        private void bt_file10_Click(object sender, EventArgs e)
        {
            //修改檔案時間 屬性
            string filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";
            if (File.Exists(filename) == false) //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                return;
            }
            if ((File.GetAttributes(filename) & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
                richTextBox1.Text += "檔案唯讀，不能修改檔案時間\n";
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 已存在\t原本檔案時間 與 檔案屬性\n";
                richTextBox1.Text += "建立時間: " + File.GetCreationTime(filename) + "\n";
                richTextBox1.Text += "修改時間: " + File.GetLastWriteTime(filename) + "\n";
                richTextBox1.Text += "存取時間: " + File.GetLastAccessTime(filename) + "\n";
                richTextBox1.Text += "檔案屬性: " + File.GetAttributes(filename).ToString() + "\n";

                richTextBox1.Text += "\n改變檔案時間 與 檔案屬性\n\n";

                File.SetCreationTime(filename, new DateTime(1985, 5, 4));
                File.SetLastWriteTime(filename, new DateTime(1995, 6, 5));
                File.SetLastAccessTime(filename, new DateTime(2005, 7, 6));
                //File.SetLastAccessTime(filename, DateTime.Now);   //touch
                //File.SetLastWriteTime(filename, DateTime.Now);    //touch

                if (attr == 0)
                    File.SetAttributes(filename, FileAttributes.Archive);
                else if (attr == 1)
                    File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden);
                else if (attr == 2)
                    File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden | FileAttributes.ReadOnly);
                attr++;
                if (attr > 2)
                    attr = 0;

                richTextBox1.Text += "檔案: " + filename + " 已存在\t更改後的檔案時間 與 檔案屬性\n";
                richTextBox1.Text += "建立時間: " + File.GetCreationTime(filename) + "\n";
                richTextBox1.Text += "修改時間: " + File.GetLastWriteTime(filename) + "\n";
                richTextBox1.Text += "存取時間: " + File.GetLastAccessTime(filename) + "\n";
                richTextBox1.Text += "檔案屬性: " + File.GetAttributes(filename).ToString() + "\n";
            }
        }

        private void bt_file11_Click(object sender, EventArgs e)
        {
            string RandomFileName = Path.GetRandomFileName();
            richTextBox1.Text += "建立隨機檔案: " + RandomFileName + "\n";
            string TempFileName = Path.GetTempFileName();
            richTextBox1.Text += "建立暫存檔案: " + TempFileName + "\n";
        }

        private void bt_file12_Click(object sender, EventArgs e)
        {
            //讀取設定檔案時間
            string filename = @"D:\_git\vcs\_1.data\______test_files1\mega.txt";

            richTextBox1.Text += "檔案: " + filename + "\t原讀寫時間\n";
            richTextBox1.Text += "CreationTime\t" + File.GetCreationTime(filename).ToString() + "\n";
            richTextBox1.Text += "ModifiedTime\t" + File.GetLastWriteTime(filename).ToString() + "\n";
            richTextBox1.Text += "AccessTime\t" + File.GetLastAccessTime(filename).ToString() + "\n";

            //一段時間以後的寫法
            DateTime dt_new1 = File.GetCreationTime(filename) + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            DateTime dt_new2 = File.GetLastWriteTime(filename) + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            DateTime dt_new3 = File.GetLastAccessTime(filename) + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒

            File.SetCreationTime(filename, dt_new1);
            File.SetLastWriteTime(filename, dt_new2);
            File.SetLastAccessTime(filename, dt_new3);
            richTextBox1.Text += "檔案: " + filename + "\t設定讀寫時間\n";
            richTextBox1.Text += "SetCreationTime\t" + dt_new1 + "\n";
            richTextBox1.Text += "SetLastWriteTime\t" + dt_new2 + "\n";
            richTextBox1.Text += "SetLastAccessTime\t" + dt_new3 + "\n";
        }

        private void bt_dir00_Click(object sender, EventArgs e)
        {
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";
        }

        private void bt_dir01_Click(object sender, EventArgs e)
        {
            //確認資料夾是否存在
            string Path = @"D:/_git/vcs/_1.data/______test_files1/aaaa/bbbb";
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
                richTextBox1.Text += "資料夾: " + Path + " 不存在\n";
            else
                richTextBox1.Text += "資料夾: " + Path + " 存在\n";
        }

        private void bt_dir02_Click(object sender, EventArgs e)
        {
            //刪除資料夾
            string Path = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            /*
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
                richTextBox1.Text += "資料夾: " + Path + " 不存在，不能刪除\n";
            else
            {
                Directory.Exists(Path);     //確認資料夾是否存在
                richTextBox1.Text += "已刪除資料夾: " + Path + "\n";
            }
            */
            if (Directory.Exists(Path))     //確認資料夾是否存在
            {
                try
                {
                    Directory.Delete(Path, true);   //recurrsive
                    //Directory.Delete(Path, false);   //not recurrsive
                    richTextBox1.Text += "已刪除資料夾" + Path + "\n";
                }
                catch
                {
                    richTextBox1.Text += "無法刪除資料夾" + Path + "\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + Path + " 不存在，不能刪除\n";
            }
        }

        private void bt_dir03_Click(object sender, EventArgs e)
        {
            string destDirName = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName2 = @"D:\_git\vcs\_1.data\______test_files1\folder22";
            DeleteDirectory(destDirName, true);
            DeleteDirectory(destDirName2, true);
        }

        private void bt_dir04_Click(object sender, EventArgs e)
        {
            //建立一個新資料夾
            string newPath = @"D:/_git/vcs/_1.data/______test_files_file_name2/aaaa/bbbb";
            if (Directory.Exists(newPath) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(newPath);
                richTextBox1.Text += "已建立一個新資料夾: " + newPath + "\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + newPath + " 已存在，不能再建立\n";
            }
        }

        private void bt_dir05_Click(object sender, EventArgs e)
        {
            //未完成
            string Path_old = @"D:/_git/vcs/_1.data/______test_files_file_name1";
            string Path_new = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            if (Directory.Exists(Path_old) == false)    //確認資料夾是否存在
            {
                richTextBox1.Text += "原始資料夾: " + Path_old + " 不存在, 不能拷貝\n";
                return;
            }
            if (Directory.Exists(Path_new) == false)     //確認資料夾是否存在
            {
                //複製
            }
            else
            {
                richTextBox1.Text += "目的資料夾: " + Path_new + " 已存在, 不能拷貝\n";
                return;
            }

        }

        private void bt_dir06_Click(object sender, EventArgs e)
        {
            string Path_old = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            string Path_new = @"D:/_git/vcs/_1.data/______test_files_file_name3";
            if (Directory.Exists(Path_old) == false)    //確認資料夾是否存在
            {
                richTextBox1.Text += "原始資料夾: " + Path_old + " 不存在, 不能拷貝\n";
                return;
            }
            if (Directory.Exists(Path_new) == true)     //確認資料夾是否存在
            {
                richTextBox1.Text += "目的資料夾: " + Path_new + " 已存在, 不能拷貝\n";
                return;
            }
            Directory.Move(Path_old, Path_new);
            richTextBox1.Text += "移動/更名 完成，從原始資料夾: " + Path_old + " 到目的資料夾: " + Path_new + "\n";

            //移動資料夾，從 sourceDirName 移動到 destDirName
            string sourceDirName = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName = @"D:\_git\vcs\_1.data\______test_files1\folder22";
            if (Directory.Exists(sourceDirName))        //確認資料夾是否存在
            {
                if (!Directory.Exists(destDirName))     //確認資料夾是否存在
                {
                    Directory.Move(sourceDirName, destDirName);
                    richTextBox1.Text += "已移動資料夾: " + sourceDirName + " 到 " + destDirName + "\n";
                }
                else
                    richTextBox1.Text += "資料夾: " + destDirName + " 已存在\n";
            }
            else
                richTextBox1.Text += "資料夾: " + sourceDirName + " 不存在\n";

        }

        private void bt_dir07_Click(object sender, EventArgs e)
        {
            //刪除資料夾
            string target_dir = @"D:/_git/vcs/_1.data/______test_files_file_name2";

            if (Directory.Exists(target_dir))       //確認資料夾是否存在
            {
                richTextBox1.Text += "刪除資料夾: " + target_dir + "\n";
                try
                {
                    DeleteDirectory(target_dir);
                    //Directory.Delete(Path, true);   //recurrsive
                    //Directory.Delete(Path, false);   //not recurrsive
                    richTextBox1.Text += "OK\n";
                }
                catch
                {
                    richTextBox1.Text += "FAIL\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + target_dir + " 不存在，不能刪除\n";
            }
        }

        private void bt_dir08_Click(object sender, EventArgs e)
        {

        }

        private void bt_dir09_Click(object sender, EventArgs e)
        {

        }

        private void bt_dir10_Click(object sender, EventArgs e)
        {

        }

        private void bt_dir11_Click(object sender, EventArgs e)
        {

        }

        private void bt_dir12_Click(object sender, EventArgs e)
        {

        }

        private void bt_files00_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\compare\ssss.txt";
            if (FileCompare(filename1, filename2))
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename2 + " 相同。\n";
            }
            else
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename2 + " 不同。\n";
            }
            if (FileCompare(filename1, filename3))
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename3 + " 相同。\n";
            }
            else
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename3 + " 不同。\n";
            }
        }

        private void bt_files01_Click(object sender, EventArgs e)
        {
        }

        public enum SizeFormat
        {
            Bytes,
            KiloBytes,
            MegaBytes,
            GigaBytes
        }

        private void bt_files02_Click(object sender, EventArgs e)
        {
            message = "";
            filesize_all = 0;
            //計算某個檔案夾下的檔案大小，並可以用不同的單位(KB,MB,GB)顯示。
            DirectoryInfo d = new DirectoryInfo(@"D:\_git\vcs\_1.data\______test_files1");//輸入檔案夾
            double size = DirSize(d);
            //SizeFormat sizeFormat = SizeFormat.KiloBytes;
            SizeFormat sizeFormat = SizeFormat.Bytes;
            switch (sizeFormat)
            {
                case SizeFormat.Bytes:
                    size = size / Math.Pow(1024, 0);
                    break;
                case SizeFormat.KiloBytes:
                    size = size / Math.Pow(1024, 1);
                    break;
                case SizeFormat.MegaBytes:
                    size = size / Math.Pow(1024, 2);
                    break;
                case SizeFormat.GigaBytes:
                    size = size / Math.Pow(1024, 3);
                    break;
            }

            //message += size.ToString();
            //message += Environment.NewLine;

            //message += "Get All FileNames";
            //message += Environment.NewLine;
            GetAllFileNames(d);
            message += "Total filesize: " + filesize_all.ToString() + " Bytes.\n";
            message += "Total filesize: " + size.ToString() + " Bytes.\n";
            message += Environment.NewLine;
            //richTextBox1.Text += message;     //無法捲到最後一行
            richTextBox1.AppendText(message);   //可以捲到最後一行
            richTextBox1.ScrollToCaret();   //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void bt_files03_Click(object sender, EventArgs e)
        {
            string target_dir = @"D:\_git\vcs\_1.data\______test_files1";
            ShowDirectory2(target_dir);
        }

        public bool ShowDirectory2(string target_dir)
        {
            bool result = false;
            string[] files = Directory.GetFiles(target_dir);
            string[] dirs = Directory.GetDirectories(target_dir);
            richTextBox1.Text += "資料夾: " + target_dir + "\n";
            foreach (string file in files)
            {
                File.SetAttributes(file, FileAttributes.Normal);
                richTextBox1.Text += file + "\t";
                richTextBox1.Text += file.Length.ToString() + "\n";
                //File.Delete(file);
            }
            richTextBox1.Text += "\n";
            foreach (string dir in dirs)
            {
                //richTextBox1.Text += dir + "\n";
                ShowDirectory(dir);
            }
            //Directory.Delete(target_dir, false);
            return result;
        }

        private void bt_files04_Click(object sender, EventArgs e)
        {
            message = "";

            DriveInfo di = new DriveInfo(@"D:\_git\vcs\_1.data\______test_files1");

            // Get the root directory and print out some information about it.
            DirectoryInfo dirInfo = di.RootDirectory;
            message += "data: ";
            message += dirInfo.Attributes.ToString();
            message += Environment.NewLine;

            // Get the files in the directory and print out some information about them.
            FileInfo[] fileNames = dirInfo.GetFiles("*.*");

            foreach (FileInfo fi in fileNames)
            {
                message += "data: ";
                message += fi.Name + "   " + fi.LastAccessTime + "   " + fi.Length;
                message += Environment.NewLine;
            }

            // Get the subdirectories directly that is under the root.
            // See "How to: Iterate Through a Directory Tree" for an example of how to
            // iterate through an entire tree.
            DirectoryInfo[] dirInfos = dirInfo.GetDirectories("*.*");

            foreach (DirectoryInfo d in dirInfos)
            {
                message += "data: " + "   " + d.Name;
                message += Environment.NewLine;
            }

            richTextBox1.Text += message;

        }

        private void bt_files05_Click(object sender, EventArgs e)
        {
            message = "";
            string strFolderPath = @"D:\_git\vcs\_1.data\______test_files1";
            DirectoryInfo DIFO = new DirectoryInfo(strFolderPath);
            if (DIFO.Exists)        //確認資料夾是否存在
            {
                message += "資料夾";
                message += Environment.NewLine;
                foreach (DirectoryInfo di in DIFO.GetDirectories())
                {
                    //資料夾資訊
                    message += "資料夾名稱：";
                    message += di.FullName;
                    message += "屬性：";
                    message += di.Attributes;
                    message += "存在與否：";
                    message += di.Exists;
                    //message += "資料夾名稱：";
                    //message += di.Extension;
                    message += "資料夾全名：";
                    message += di.FullName;
                    message += "資料夾簡名：";
                    message += di.Name;
                    //message += "資料夾名稱：";
                    //message += di.Parent;
                    message += "根資料夾：";
                    message += di.Root;

                    message += "資料夾內資料夾數目：";
                    message += di.GetDirectories().Length;

                    message += "資料夾內檔案數目：";
                    message += di.GetFiles().Length;

                    /*

                    message += "  資料夾數目：";
                    message += di.GetDirectories().Length;
                    message += "  ";
                    message += "  檔案數目：";
                    message += di.GetFiles().Length;
                    message += "  ";

                    if (di.GetDirectories().Length > 0)
                    {
                        message += "下一層資料夾：";
                        foreach (DirectoryInfo ddi in di.GetDirectories())
                        {
                            message += ddi.Name;
                            message += "  ";
                        }
                        message += Environment.NewLine;
                    }
                    else
                        message += Environment.NewLine;
                     */

                    message += Environment.NewLine;
                    message += Environment.NewLine;
                }

                /*  檢查每個檔案的資訊
                message += Environment.NewLine;
                message += "檔案";
                message += Environment.NewLine;
                foreach (FileInfo di in DIFO.GetFiles())
                {
                    message += "全檔名：";
                    message += di.FullName;
                    message += "  檔名：";
                    message += di.Name;
                    message += "  副檔名：";
                    message += di.Extension;
                    message += "  大小：";
                    if (di.Length > (1024 * 1024))
                    {
                        message += (di.Length / 1024 / 1024).ToString();
                        message += " MB( ";
                        message += di.Length;
                        message += " 位元組)";
                    }
                    else if (di.Length > (1024))
                    {
                        message += (di.Length / 1024).ToString();
                        message += " KB( ";
                        message += di.Length;
                        message += " 位元組)";
                    }
                    else
                    {
                        message += di.Length;
                        message += " 位元組";
                    }
                    message += "  建立日期：";
                    message += di.CreationTime;
                    //message += "  日期：";
                    //message += di.CreationTimeUtc;
                    message += "  存取日期：";
                    message += di.LastAccessTime;
                    //message += "  日期：";
                    //message += di.LastAccessTimeUtc;
                    message += "  修改日期：";
                    message += di.LastWriteTime;
                    //message += "  日期：";
                    //message += di.LastWriteTimeUtc;
                    message += "  屬性：";
                    message += di.Attributes;
                    message += "  資料夾：";
                    message += di.Directory;
                    message += "  資料夾名：";
                    message += di.DirectoryName;

                    message += "  唯讀：";
                    message += di.IsReadOnly;


                    message += Environment.NewLine;
                }
                */
            }
            else
                MessageBox.Show("No Exist");

            message += Environment.NewLine;
            richTextBox1.Text += message;
        }

        private void bt_files06_Click(object sender, EventArgs e)
        {
            message = "";
            //計算某個檔案夾下的檔案大小，並可以用不同的單位(KB,MB,GB)顯示。
            DirectoryInfo d = new DirectoryInfo(@"D:\_git\vcs\_1.data\______test_files1");//輸入檔案夾
            double size = DirSize(d);
            //SizeFormat sizeFormat = SizeFormat.KiloBytes;
            SizeFormat sizeFormat = SizeFormat.Bytes;
            switch (sizeFormat)
            {
                case SizeFormat.Bytes:
                    size = size / Math.Pow(1024, 0);
                    break;
                case SizeFormat.KiloBytes:
                    size = size / Math.Pow(1024, 1);
                    break;
                case SizeFormat.MegaBytes:
                    size = size / Math.Pow(1024, 2);
                    break;
                case SizeFormat.GigaBytes:
                    size = size / Math.Pow(1024, 3);
                    break;
            }

            message += size.ToString();
            message += Environment.NewLine;

            message += Environment.NewLine;
            message += Environment.NewLine;
            message += "Get All FileNames";
            message += Environment.NewLine;
            GetAllFileNames(d);
            message += "Total filesize: " + filesize_all.ToString();
            message += Environment.NewLine;
            richTextBox1.Text += message;
        }

        //讀取資料夾下所有資料夾
        private ArrayList GetDirectories(string path)
        {
            ArrayList directories = new ArrayList();

            if (Directory.Exists(path))     //確認資料夾是否存在
            {
                directories.AddRange(Directory.GetDirectories(path));
                richTextBox1.Text += "總共" + directories.Count.ToString() + "個資料夾\n";
            }
            //richTextBox1.Text += directories;

            return directories;
        }

        //讀取資料夾下所有檔案, 只看一層
        private ArrayList GetFiles(string path)
        {
            ArrayList files = new ArrayList();

            if (Directory.Exists(path))     //確認資料夾是否存在
            {
                files.AddRange(Directory.GetFiles(path));
                richTextBox1.Text += "總共" + files.Count.ToString() + "個檔案\n";
            }
            return files;
        }

        private void bt_files07_Click(object sender, EventArgs e)
        {
            string path = @"D:\_git\vcs\_1.data\______test_files1";
            GetDirectories(path);
        }

        private void bt_files08_Click(object sender, EventArgs e)
        {
            string path = @"D:\_git\vcs\_1.data\______test_files1";
            GetFiles(path);
        }

        private void bt_files09_Click(object sender, EventArgs e)
        {
            string target_dir = @"D:\_git\vcs\_1.data\______test_files1";
            richTextBox1.Text += "資料夾: " + target_dir + "\n";
            ShowDirectory(target_dir);
        }

        public bool ShowDirectory(string target_dir)
        {
            bool result = false;
            string[] files = Directory.GetFiles(target_dir);
            string[] dirs = Directory.GetDirectories(target_dir);
            richTextBox1.Text += "檔案個數 = " + files.Length.ToString() + "\n";
            foreach (string file in files)
            {
                richTextBox1.Text += "檔案: " + file + "\t";
                //richTextBox1.Text += "Size: " + file.Length.ToString() + " 拜\n"; wrong

            }
            richTextBox1.Text += "\n";
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "資料夾: " + dir + "\n";
                ShowDirectory(dir);
            }
            return result;
        }

        private void bt_files10_Click(object sender, EventArgs e)
        {
            if (GetFile())
            {
                MessageBox.Show("有找到");
            }
            else
            {
                MessageBox.Show("沒有找到");
            }
        }

        private Boolean GetFile()
        {
            richTextBox1.Text += "尋找檔案 IMG_20180228_215525.jpg\n";
            DirectoryInfo dirInfo = new DirectoryInfo(@"D:\_git\vcs\_1.data\______test_files1");
            foreach (FileInfo info in dirInfo.GetFiles("IMG_20180228_215525.jpg"))
            {
                return true;
            }
            return false;
        }

        private void bt_files11_Click(object sender, EventArgs e)
        {
            //撈出資料夾內所有jpg檔
            var dirnames = Directory.GetDirectories(@"D:\_git\vcs\_1.data\______test_files1");
            int i = 0;

            try
            {
                foreach (var dir in dirnames)
                {
                    richTextBox1.Text += "aaaa3 dir = " + dir + "\n";
                    var fnames = Directory.GetFiles(dir, "*.jpg").Select(Path.GetFileName);

                    DirectoryInfo d = new DirectoryInfo(dir);
                    FileInfo[] finfo = d.GetFiles("*.jpg");

                    foreach (var f in fnames)
                    {
                        i++;
                        //richTextBox1.Text += "The number of the file being renamed is: " + i.ToString() + "\n";

                        richTextBox1.Text += f + "\n";

                        if (!File.Exists(Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", ""))))
                        {
                            File.Move(Path.Combine(dir, f), Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", "")));
                        }
                        else
                        {
                            richTextBox1.Text += "The file you are attempting to rename already exists! The file path is " + dir + "\n";
                            foreach (FileInfo fi in finfo)
                            {
                                //richTextBox1.Text += "The file modify date is: " + File.GetLastWriteTime(dir) + "\n";
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            richTextBox1.Text += "dirnames : " + dirnames + "\n";
        }

        private void bt_files12_Click(object sender, EventArgs e)
        {
            //撈出資料夾內特定類型的檔案

            string searchDirectory = @"D:\_git\vcs\_1.data\______test_files1";
            string searchPattern = "*.cs;*.csv;*.ico";
            bool recurrsive = false;

            richTextBox1.Text += "撈出資料夾內特定類型的檔案\t單層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            List<string> filenames = FindFiles(searchDirectory, searchPattern, recurrsive);
            foreach (string filename in filenames)
            {
                richTextBox1.Text += filename + "\n";
            }

            recurrsive = true;
            richTextBox1.Text += "撈出資料夾內特定類型的檔案\t多層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            filenames.Clear();
            filenames = FindFiles(searchDirectory, searchPattern, recurrsive);
            foreach (string filename in filenames)
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        // Search for files matching the patterns.
        private List<string> FindFiles(string dir_name, string patterns, bool recurrsive)
        {
            // Make the result list.
            List<string> files = new List<string>();

            // Get the patterns.
            string[] pattern_array = patterns.Split(';');

            // Search.
            System.IO.SearchOption search_option = System.IO.SearchOption.TopDirectoryOnly;
            if (recurrsive)
            {
                search_option = System.IO.SearchOption.AllDirectories;
            }
            foreach (string pattern in pattern_array)
            {
                foreach (string filename in Directory.GetFiles(dir_name, pattern, search_option))
                {
                    if (!files.Contains(filename))
                        files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }
    }
}
