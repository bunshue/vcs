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

namespace vcs_test_all_06_DirectoryFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //確認資料夾是否存在
            string Path = "C:\\______test_files_file_name2\\aaaa\\bbbb";
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
                richTextBox1.Text += "資料夾: " + Path + " 不存在\n";
            else
                richTextBox1.Text += "資料夾: " + Path + " 存在\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //刪除資料夾
            string Path = "C:\\______test_files_file_name2";
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

        private void button4_Click(object sender, EventArgs e)
        {
            //建立一個新資料夾
            string newPath = "C:\\______test_files_file_name2\\aaaa\\bbbb";
            if (Directory.Exists(newPath) == false)     //確認資料夾是否存在
            {
                Directory.CreateDirectory(newPath);
                richTextBox1.Text += "已建立一個新資料夾: " + newPath + "\n";
            }
            else
                richTextBox1.Text += "資料夾: " + newPath + " 已存在，不能再建立\n";
        }

        //public static bool DeleteDirectory(string target_dir)
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

        private void button5_Click(object sender, EventArgs e)
        {
            //刪除資料夾
            string target_dir = "C:\\______test_files_file_name2";

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

        //public static bool DeleteDirectory(string target_dir)
        public bool ShowDirectory(string target_dir)
        {
            bool result = false;
            string[] files = Directory.GetFiles(target_dir);
            string[] dirs = Directory.GetDirectories(target_dir);
            richTextBox1.Text += "檔案個數 = " + files.Length.ToString() + "\n";
            foreach (string file in files)
            {
                richTextBox1.Text += "檔案: " + file + "\t";
                richTextBox1.Text += "Size: " + file.Length.ToString() + " 拜\n";
            }
            richTextBox1.Text += "\n";
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "資料夾: " + dir + "\n";
                ShowDirectory(dir);
            }
            return result;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string target_dir = "C:\\______test_files_file_name1";
            richTextBox1.Text += "資料夾: " + target_dir + "\n";
            ShowDirectory(target_dir);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //取得檔案資訊
            //法一
            string filename = "c:\\______test_files\\vcs_test.old.txt";
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

        private void button10_Click(object sender, EventArgs e)
        {
            string filename1 = "C:\\______test_files\\aaaaaaa.txt";
            string filename2 = "C:\\aaaa.txt";

            if (File.Exists(filename1) == false)            //確認檔案是否存在
                richTextBox1.Text += "檔案: " + filename1 + " 不存在\n";
            else
                richTextBox1.Text += "檔案: " + filename1 + " 存在\n";

            if (System.IO.File.Exists(filename2) == false)  //確認檔案是否存在
                richTextBox1.Text += "檔案: " + filename2 + " 不存在\n";
            else
                richTextBox1.Text += "檔案: " + filename2 + " 存在\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //建立檔案
            string filename = "C:\\______test_files\\aaaaaaab.txt";
            if (File.Exists(filename) == false)         //確認檔案是否存在
            {
                File.Create(filename);
                richTextBox1.Text += "檔案: " + filename + " 不存在, 已建立\n";
            }
            else
                richTextBox1.Text += "檔案: " + filename + " 已存在, 無法再建立\n";

            //建立檔案
            string destFileName = @"c:\______test_files\picture1a.jpg";
            FileStream fs = File.Create(destFileName);
            fs.Close();
            richTextBox1.Text += "已建立檔案: " + destFileName + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //刪除檔案
            //法一
            string filename = "C:\\______test_files\\aaaaaaab.txt";
            if (File.Exists(filename) == false)     //確認檔案是否存在
                richTextBox1.Text += "檔案: " + filename + " 不存在, 無法刪除\n";
            else
            {
                File.Delete(filename);
                richTextBox1.Text += "檔案: " + filename + " 存在, 已刪除\n";
            }

            //刪除檔案
            //法二
            FileInfo f = new FileInfo("c:\\______test_files\\vcs_test.txt");
            if (f.Exists)       //確認檔案是否存在
            {
                f.Delete();
                richTextBox1.Text += "檔案刪除成功\n";
            }
            else
                richTextBox1.Text += "找不到檔案\n";


            string destFileName = @"c:\______test_files\picture1a.jpg";
            string destFileName2 = @"c:\______test_files\picture1b.jpg";

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

        private void button13_Click(object sender, EventArgs e)
        {
            string filename1 = "C:\\______test_files\\aaaaaaa.txt";
            string filename2 = "C:\\______test_files\\aaaaaaab.txt";

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
            string sourceFileName = @"c:\______test_files\picture1.jpg";
            string destFileName = @"c:\______test_files\picture1a.jpg";

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

        int attr = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            //修改檔案時間 屬性
            string filename = @"C:\\cccc.txt";
            if (File.Exists(filename) == false) //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                return;
            }
            if ((File.GetAttributes(filename) & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
                richTextBox1.Text += "檔案唯讀，不能修改檔案時間";
            else
            {
                richTextBox1.Text += "改變檔案時間";
                File.SetCreationTime(filename, new DateTime(1985, 5, 4));
                File.SetLastWriteTime(filename, new DateTime(1995, 6, 5));
                File.SetLastAccessTime(filename, new DateTime(2005, 7, 6));
            }
            if(attr == 0)
                File.SetAttributes(filename, FileAttributes.Archive);
            else if (attr == 1)
                File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden);
            else if (attr == 2)
                File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden | FileAttributes.ReadOnly);
            attr++;
            if (attr > 2)
                attr = 0;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //未完成
            string Path_old = "C:\\______test_files_file_name1";
            string Path_new = "C:\\______test_files_file_name2";
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

        private void button15_Click(object sender, EventArgs e)
        {
            string Path_old = "C:\\______test_files_file_name2";
            string Path_new = "C:\\______test_files_file_name3";
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
            string sourceDirName = @"c:\______test_files\folder2";
            string destDirName = @"c:\______test_files\folder22";
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

        private void button19_Click(object sender, EventArgs e)
        {
            string filename1 = "c:\\______test_files\\compare\\aaaa.txt";
            string filename2 = "c:\\______test_files\\compare\\bbbb.txt";
            string filename3 = "c:\\______test_files\\compare\\ssss.txt";
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

        private void button18_Click(object sender, EventArgs e)
        {
            StreamReader sr1 = new StreamReader("c:\\______test_files\\compare\\aaaa.txt", Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            StreamReader sr2 = new StreamReader("c:\\______test_files\\compare\\bbbb.txt", Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            StreamReader sr3 = new StreamReader("c:\\______test_files\\compare\\ssss.txt", Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))
            {
                richTextBox1.Text += "兩個文件相等\n";
            }
            else
            {
                richTextBox1.Text += "兩個文件不相等\n";
            }
            if (object.Equals(sr1.ReadToEnd(), sr3.ReadToEnd()))
            {
                richTextBox1.Text += "兩個文件相等\n";
            }
            else
            {
                richTextBox1.Text += "兩個文件不相等\n";
            }
            sr1.Close();
            sr2.Close();
            sr3.Close();
        }

        private void button20_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_case1\_case1a\eula.3085.txt";
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

        private void button23_Click(object sender, EventArgs e)
        {
            //讀取中文檔案
            String pathname = "C:\\______test_files\\read_file.txt";

            if (File.Exists(pathname) == false) //確認檔案是否存在
            {
                MessageBox.Show("檔案: " + pathname + "不存在，無法開啟。\n");
                return;
            }
            else
            {
                richTextBox1.Clear();
                //讀取中文檔案
                StreamReader sw = new StreamReader(@"c:/______test_files/read_file.txt", Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                richTextBox1.Text += sw.ReadToEnd();
            }

        }

        private void button41_Click(object sender, EventArgs e)
        {
            //建立時間檔案
            string filename = "Stage_Speed_Current." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
            richTextBox1.Text += "建立時間檔案：" + filename + "\n";

            //儲存檔案1
            FileInfo f = new FileInfo("c:\\______test_files\\vcs_test.txt");
            StreamWriter sw1 = f.CreateText();
            sw1.Write(richTextBox1.Text);
            sw1.Flush();
            sw1.Close();
            richTextBox1.Text += "儲存檔案1 OK，檔名：c:\\______test_files\\vcs_test.txt\n";

            //儲存檔案2
            string filename2 = "c:\\______test_files\\SaveDataToFile.txt";
            StreamWriter sw2 = File.CreateText(filename2);
            string content = "";
            for (int i = 0; i < 10; i++)
            {
                content += i + "\t";
                content += "aaa" + "\t";
                content += "bbb" + "\t";
                content += "ccc" + "\t";
                content += "\n";
            }
            sw2.WriteLine(content);
            sw2.Close();
            richTextBox1.Text += "儲存檔案2 OK，檔名：" + filename2 + "\n";

            //儲存檔案3     把textbox資料存檔
            string filename3 = "data." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
            StreamWriter sw = File.CreateText(filename3);
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "儲存檔案3 OK，檔名：" + filename3 + "\n";

            //儲存檔案4     儲存二進位檔
            string filename4 = "c:\\______test_files\\save_file_test.bin";
            byte[] cbuffer = new byte[256];
            for (int i = 0; i < 256; i++)
                cbuffer[i] = (byte)i;

            // 建立檔案串流
            System.IO.FileStream fileStream = new FileStream(filename4, FileMode.OpenOrCreate, FileAccess.Write);
            //byte[] byteSave = Encoding.ASCII.GetBytes(txtHTML.Text.ToString());

            // 以FileStream類別的Write方法將HTML內容寫入檔案中
            fileStream.Write(cbuffer, 0, cbuffer.Length);

            // 關閉檔案串流
            fileStream.Close();
            richTextBox1.Text += "儲存檔案4 OK，檔名：" + filename4 + "\n";

            //儲存檔案5
            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };
            //把資料儲存成檔案
            string filename5 = "C:\\______test_files\\aaaaaaa.txt";
            string context = string.Empty;
            FileStream filestream = File.Open(filename5, FileMode.Create);
            StreamWriter str_writer = new StreamWriter(filestream);
            for (int ii = 0; ii < 16; ii++)
            {
                context = ii.ToString() + "\t" + x[ii].ToString() + "\t" + y[ii].ToString();
                str_writer.WriteLine(context);
            }
            // Dispose StreamWriter
            str_writer.Dispose();
            // Close FileStream
            filestream.Close();
            richTextBox1.Text += "儲存檔案5 OK，檔名：" + filename5 + "\n";

        }

        private void button40_Click(object sender, EventArgs e)
        {
            //附加檔案
            FileInfo f = new FileInfo("c:\\______test_files\\vcs_test.txt");
            StreamWriter sw = f.AppendText();
            sw.Write(richTextBox1.Text);
            sw.Flush();
            sw.Close();

        }

        private void button39_Click(object sender, EventArgs e)
        {
            //讀檔1
            //一次讀取檔案內所有資料
            FileInfo f = new FileInfo("c:\\______test_files\\vcs_test.txt");
            StreamReader sr = f.OpenText();
            richTextBox1.Text += sr.ReadToEnd();
            sr.Close();

        }

        private void button38_Click(object sender, EventArgs e)
        {
            //讀檔2
            //一次讀取檔案內一行資料
            FileInfo f = new FileInfo("c:\\______test_files\\vcs_test.txt");
            StreamReader sr = f.OpenText();
            while (sr.Peek() > 0)
            {
                richTextBox1.Text += sr.ReadLine() + "\n";
            }
            sr.Close();

        }

        private void button37_Click(object sender, EventArgs e)
        {
            //讀檔3
            //一次讀取檔案內一個字元
            FileInfo f = new FileInfo("c:\\______test_files\\vcs_test.txt");
            StreamReader sr = f.OpenText();
            while (sr.Peek() > 0)
            {
                richTextBox1.Text += (char)sr.Read();
            }
            sr.Close();

        }

        private void button27_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            string filepath = "C:\\______test_files\\aaaaaaa.txt";

            string[] rowdat = new string[3];
            string[] paraname = new string[16];
            int[] value = new int[16];
            string context = string.Empty;
            int t1 = 0;
            int t2 = 0;

            int[] xx = new int[16];
            int[] yy = new int[16];

            FileStream filestream = File.Open(filepath, FileMode.Open);
            StreamReader str_reader = new StreamReader(filestream);
            // Read File text
            for (int ii = 0; ii < 16; ii++)
            {
                context = str_reader.ReadLine();
                richTextBox1.Text += "原始context " + ii + " = " + context + "\n";
                t1 = t2 = 0;
                //for (int jj = 0; jj < 3; jj++)
                for (int jj = 0; jj < 2; jj++)
                {
                    t2 = context.IndexOf("\t", t1);
                    rowdat[jj] = context.Substring(t1, t2 - t1);
                    richTextBox1.Text += "分割context = " + context + " jj = " + jj + " t1= " + t1 + " t2= " + t2 + " rowdat =" + rowdat[jj] + "\n";

                    t1 = t2 + 1;
                    if (jj == 0)
                        xx[ii] = Int32.Parse(rowdat[jj]);
                    else if (jj == 1)
                        yy[ii] = Int32.Parse(rowdat[jj]);
                }
                paraname[ii] = rowdat[1];
                //value[ii] = Int32.Parse(rowdat[2]);
            }

            MessageBox.Show("Result: \n" + xx[0].ToString() + " " + xx[1].ToString() + " " + xx[2].ToString() + " " + xx[3].ToString() + " " + xx[4].ToString() + " " + xx[5].ToString() + " " + xx[6].ToString() + " " + xx[7].ToString() + " " + xx[8].ToString() + " " + xx[9].ToString() + " " + xx[10].ToString() + " " + xx[11].ToString() + " " + xx[12].ToString() + " " + xx[13].ToString() + " " + xx[14].ToString() + " " + xx[15].ToString() + "\n" + yy[0].ToString() + " " + yy[1].ToString() + " " + yy[2].ToString() + " " + yy[3].ToString() + " " + yy[4].ToString() + " " + yy[5].ToString() + " " + yy[6].ToString() + " " + yy[7].ToString() + " " + yy[8].ToString() + " " + yy[9].ToString() + " " + yy[10].ToString() + " " + yy[11].ToString() + " " + yy[12].ToString() + " " + yy[13].ToString() + " " + yy[14].ToString() + " " + yy[15].ToString());

            // Dispose StreamReader
            str_reader.Dispose();
            // Close FileStream
            filestream.Close();

        }

        private void button24_Click(object sender, EventArgs e)
        {
            //ReadAllText 讀取文件
            //使用ReadAllText可以直接讀取文件中的內容，格式為:
            //File.ReadAllText(檔案位置及名稱);
            //建立檔案 & 讀取檔案 範例:

            //建立檔案
            string x = "Hello text";
            File.WriteAllText("myfilename.txt", x);
            richTextBox1.Text += "寫檔完成\n";

            //讀取檔案
            string y = File.ReadAllText("myfilename.txt");
            richTextBox1.Text += "檔案內容 : " + y + "\n";
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

        //讀取資料夾下所有檔案
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

        private void button49_Click(object sender, EventArgs e)
        {
            string sourceFileName = @"c:\______test_files\picture1a.jpg";
            string destFileName = @"c:\______test_files\picture1b.jpg";

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

        private void button47_Click(object sender, EventArgs e)
        {
            string destDirName = @"c:\______test_files\folder2";
            string destDirName2 = @"c:\______test_files\folder22";
            DeleteDirectory(destDirName, true);
            DeleteDirectory(destDirName2, true);
        }

        private void button53_Click(object sender, EventArgs e)
        {
            string path = @"c:\______test_files";
            GetDirectories(path);
        }

        private void button52_Click(object sender, EventArgs e)
        {
            string path = @"c:\______test_files";
            GetFiles(path);
        }

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            string filepath = string.Empty;
            string context = string.Empty;

            OpenFileDialog P_OpenFileDialog = new OpenFileDialog();
            if (P_OpenFileDialog.ShowDialog() == DialogResult.OK)
            {
                filepath = P_OpenFileDialog.FileName;
                FileStream filestream = File.Open(filepath, FileMode.Open);
                StreamReader str_reader = new StreamReader(filestream);
                try
                {
                    // Read File text
                    for (int ii = 0; ii < 5; ii++)
                    {
                        context = str_reader.ReadLine();
                        richTextBox1.Text += "Line " + ii.ToString() + ", context : " + context + "\n";

                        string[] strArray = context.Split('\t');
                        for (int i = 0; i < strArray.Length; i++)
                        {
                            richTextBox1.Text += strArray[i] + "\n";
                        }
                    }

                    //this.Disp_Message("開啟檔案 : " + filepath, 0);
                    //this.Disp_Message("讀取檔案成功 !!", 1);
                    MessageBox.Show("Open File : " + filepath);
                    MessageBox.Show("Read File Successfully !!");
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.ToString());
                    //this.Disp_Message("開啟檔案 : " + filepath, 0);
                    //this.Disp_Message("讀取檔案失敗 !!", 2);
                    MessageBox.Show("Open File : " + filepath);
                    MessageBox.Show("Read File Fail !!");
                }

                // Dispose StreamReader
                str_reader.Dispose();
                // Close FileStream
                filestream.Close();
            }
        }

        private void button34_Click(object sender, EventArgs e)
        {
            string filepath = "C:\\______test_files\\aaaaaaab.txt";

            string[] rowdat = new string[3];
            string[] paraname = new string[16];
            string context = string.Empty;
            int t1 = 0;
            int t2 = 0;
            string rowdata = string.Empty;

            FileStream filestream = File.Open(filepath, FileMode.Open);
            StreamReader str_reader = new StreamReader(filestream);
            // Read File text
            for (int ii = 0; ii < 1; ii++)
            {
                context = str_reader.ReadLine();
                MessageBox.Show("context " + ii + " = " + context + "  len = " + context.Length);
                //MessageBox.Show("context[41] = " + Convert.ToString(context[41], 16));
                //MessageBox.Show("context[42] = " + Convert.ToString(context[42], 16));

                //MessageBox.Show("data = 0x" + Convert.ToString(value, 16) + " =" + value);

                t1 = 0;
                t2 = context.IndexOf("\t", t1);
                rowdata = context.Substring(t1, t2 - t1);
                MessageBox.Show("t1 = " + t1 + " t2 = " + t2 + " rowdata = " + rowdata);

                do
                {
                    t1 = t2 + 1;
                    t2 = context.IndexOf("\t", t1);
                    if (t2 != -1)
                    {
                        rowdata = context.Substring(t1, t2 - t1);
                        MessageBox.Show("t1 = " + t1 + " t2 = " + t2 + " rowdata = " + rowdata);
                    }
                    else
                    {
                        t2 = context.Length;
                        rowdata = context.Substring(t1, t2 - t1);
                        MessageBox.Show("t1 = " + t1 + " t2 = " + t2 + " rowdata = " + rowdata);
                        break;
                    }
                }
                while (t2 != -1);
            }
            // Dispose StreamReader
            str_reader.Dispose();
            // Close FileStream
            filestream.Close();
        }

        private void button33_Click(object sender, EventArgs e)
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
            richTextBox1.Text += "尋找檔案 start.wav \n";
            DirectoryInfo dirInfo = new DirectoryInfo(@"C:\______test_files");
            foreach (FileInfo info in dirInfo.GetFiles("start.wav"))
            {
                return true;
            }
            return false;
        }

        string message = "";
        double filesize_all = 0;

        private void button32_Click(object sender, EventArgs e)
        {
            message = "";
            //計算某個檔案夾下的檔案大小，並可以用不同的單位(KB,MB,GB)顯示。
            DirectoryInfo d = new DirectoryInfo(@"C:\______test_files");//輸入檔案夾
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
        public enum SizeFormat
        {
            Bytes,
            KiloBytes,
            MegaBytes,
            GigaBytes
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

        private void button51_Click(object sender, EventArgs e)
        {
            message = "";

            System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\______test_files");

            // Get the root directory and print out some information about it.
            System.IO.DirectoryInfo dirInfo = di.RootDirectory;
            message += "data: ";
            message += dirInfo.Attributes.ToString();
            message += Environment.NewLine;

            // Get the files in the directory and print out some information about them.
            System.IO.FileInfo[] fileNames = dirInfo.GetFiles("*.*");

            foreach (System.IO.FileInfo fi in fileNames)
            {
                message += "data: ";
                message += fi.Name + "   " + fi.LastAccessTime + "   " + fi.Length;
                message += Environment.NewLine;
            }

            // Get the subdirectories directly that is under the root.
            // See "How to: Iterate Through a Directory Tree" for an example of how to
            // iterate through an entire tree.
            System.IO.DirectoryInfo[] dirInfos = dirInfo.GetDirectories("*.*");

            foreach (System.IO.DirectoryInfo d in dirInfos)
            {
                message += "data: " + "   " + d.Name;
                message += Environment.NewLine;
            }

            richTextBox1.Text += message;


        }

        private void button50_Click(object sender, EventArgs e)
        {
            message = "";
            string strFolderPath = @"C:\______test_files";
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

        private void button17_Click_1(object sender, EventArgs e)
        {
            string pathname = @"C:\______test_files\_case1\_case1a\_case1bb\";
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

        private void button21_Click_1(object sender, EventArgs e)
        {
            message = "";
            filesize_all = 0;
            //計算某個檔案夾下的檔案大小，並可以用不同的單位(KB,MB,GB)顯示。
            DirectoryInfo d = new DirectoryInfo(@"C:\______test_files");//輸入檔案夾
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

        private void button22_Click_1(object sender, EventArgs e)
        {
            string target_dir = @"C:\______test_files";
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

        private void button26_Click_1(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\_case1\_case1a\_case1bb\eula.3086b.txt";
            if (File.Exists(filename))      //確認檔案是否存在
            {
                richTextBox1.Text += "取得完整路徑檔名:\t" + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "取得路徑:\t\t" + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "取得檔名(包含附檔名):\t" + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "取得檔名(不包含附檔名):\t" + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "取得副檔名:\t\t" + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "資料根目錄:\t\t" + Path.GetPathRoot(filename) + "\n";
            }
            richTextBox1.ScrollToCaret();   //RichTextBox顯示訊息自動捲動，顯示最後一行
        }

        private void button14_Click(object sender, EventArgs e)
        {
            string fileReadName = @"c:\______test_files\data.txt";
            ReadFile(fileReadName);

        }

        //讀檔案
        private string ReadFile(string fileName)
        {
            string content = "";
            content = File.ReadAllText(fileName);
            richTextBox1.Text += "檔案: " + fileName + " 內容：\n";
            richTextBox1.Text += content;
            richTextBox1.Text += "\n";
            return content;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            string RandomFileName = System.IO.Path.GetRandomFileName();
            richTextBox1.Text += "建立隨機檔案: " + RandomFileName + "\n";
            string TempFileName = System.IO.Path.GetTempFileName();
            richTextBox1.Text += "建立暫存檔案: " + TempFileName + "\n";

        }

        private void button42_Click(object sender, EventArgs e)
        {
            //string wmi_data_filename = "wmi-" + DateTime.Now.ToString("yyyy-MMdd-HHmm") + ".txt";
            string wmi_data_filename = "C:\\vcs-" + DateTime.Now.ToString("yyyy-MMdd-HHmm") + ".txt";
            if (System.IO.File.Exists(wmi_data_filename) == false)
            {
                MessageBox.Show("檔案 " + wmi_data_filename + " 不存在，製作一個。");
                StreamWriter sw = File.CreateText(wmi_data_filename);
                sw.Write(richTextBox1.Text);
                sw.Close();
            }
            else
            {
                MessageBox.Show("檔案 " + wmi_data_filename + " 存在, 開啟，並接續寫入資料");
                StreamWriter sw = File.AppendText(wmi_data_filename);
                sw.Write(richTextBox1.Text);
                sw.Close();
            }

        }

        private void button48_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "測試讀取一個純文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                //StreamReader sr = new StreamReader(openFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);
                StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                richTextBox1.Text += sr.ReadToEnd();
                sr.Close();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "測試讀取一個純文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

        }

        private void button36_Click(object sender, EventArgs e)
        {
            int i = 0;
            String line;
            openFileDialog1.Title = "測試讀取一個純文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "文字檔|*.*|C#文件|*.cs|所有檔|*.*";   //限定檔案格式
            //openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
            openFileDialog1.FilterIndex = 1;
            openFileDialog1.RestoreDirectory = true;

            //openFileDialog1.InitialDirectory = "c:\\";
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"C:\______test_files\";
            openFileDialog1.RestoreDirectory = true;
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get filename : " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "length : " + openFileDialog1.FileName.Length.ToString() + "\n";

                //StreamReader sr = new StreamReader(openFileDialog1.FileName);
                //StreamReader sr = new StreamReader(fileName, Encoding.Default);
                StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                //richTextBox1.Text += sr.ReadToEnd();
                //寫法一
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine();            // 讀取文字到 line 變數
                    richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\n";
                }

                /*
                //寫法二
                while ((line = sr.ReadLine()) != null)
                {
                    i++;
                    richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\n";
                }
                */
                sr.Close();
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

        }

        private void button29_Click(object sender, EventArgs e)
        {
            openFileDialog1.Title = "單選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 1;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = "c:\\______test_files";  //預設開啟的路徑
            openFileDialog1.Multiselect = false;    //單選
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                FileInfo f = new FileInfo(openFileDialog1.FileName);
                richTextBox1.Text += "Name: " + f.Name + "\n";
                richTextBox1.Text += "FullName: " + f.FullName + "\n";
                richTextBox1.Text += "Extension: " + f.Extension + "\n";
                richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
                richTextBox1.Text += "Directory: " + f.Directory + "\n";
                richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }

        }

        private void button44_Click(object sender, EventArgs e)
        {
            string folderpath;          // 紀錄資料夾路徑
            string filename;            // 檔案名稱
            string fullpath;
            FileStream fs;

            folderpath = System.IO.Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前路徑: " + folderpath + "\n";

            // 使用現在時間建立檔案名稱
            filename = DateTime.Now.Year.ToString();
            filename += DateTime.Now.Month.ToString("00");
            filename += DateTime.Now.Day.ToString("00");
            filename += DateTime.Now.Hour.ToString("00");
            filename += DateTime.Now.Minute.ToString("00");
            filename += DateTime.Now.Second.ToString("00");
            filename += ".txt";
            richTextBox1.Text += "檔案名稱: " + filename + "\n";

            fullpath = folderpath + "\\" + filename;
            richTextBox1.Text += "完整路徑與檔名: " + fullpath + "\n";

            //開啟檔案
            fs = File.Open(fullpath, FileMode.Create);



            fs.Close();


        }

        private void button45_Click(object sender, EventArgs e)
        {
            string path = @"C:\______test_files\";
            string fileName = "filewrite.txt";

            if (!System.IO.Directory.Exists(path))
            {
                richTextBox1.Text += "路徑不存在，建立之。\n";
                System.IO.Directory.CreateDirectory(path);
            }
            if (!System.IO.File.Exists(path + fileName))
            {
                richTextBox1.Text += "檔案不存在，建立之。\n";
                FileStream fs = System.IO.File.Create(path + fileName);
                fs.Close();
            }
            using (StreamWriter w = System.IO.File.AppendText(path + fileName))
            {
                //System.IO.File.SetAttributes(path + fileName, FileAttributes.Hidden);//隱藏
                w.WriteLine(richTextBox1.Text, Encoding.Default);
                richTextBox1.Text += "寫入檔案完成\n";
            }

        }

        private void button43_Click(object sender, EventArgs e)
        {
            string fileName1 = "c:\\______test_files\\test_ReadAllBytes.bmp";
            string fileName2 = "c:\\______test_files\\test_WriteAllBytes.bmp";

            //讀取資料
            byte[] data_read = File.ReadAllBytes(fileName1);
            richTextBox1.Text += "讀取檔案" + fileName1 + "\t";
            richTextBox1.Text += "len = " + data_read.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            //修改資料
            for (int i = 54; i < data_read.Length; i++)
            {
                if (data_read[i] == 0xCC)
                    data_read[i] = 0xFF;
            }

            //寫資料
            File.WriteAllBytes(fileName2, data_read);
            richTextBox1.Text += "寫成檔案" + fileName2 + "\n";

        }

        private void button30_Click(object sender, EventArgs e)
        {
            string fileName1 = "c:\\______test_files\\test_ReadAllBytes.bmp";
            string fileName2 = "c:\\______test_files\\test_ReadAllBytes_half.bmp";

            //讀取資料
            byte[] data_read = File.ReadAllBytes(fileName1);
            richTextBox1.Text += "讀取檔案" + fileName1 + "\t";
            richTextBox1.Text += "len = " + data_read.Length.ToString() + "\n";

            byte[] data_write = new byte[data_read.Length / 2];

            for (int i = 0; i < data_read.Length / 2; i++)
            {
                data_write[i] = data_read[i];

            }

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */


            //寫資料
            //File.WriteAllBytes(fileName2, data_write);
            string zzz = Convert.ToString(data_write);
            File.WriteAllText(fileName2, zzz);
            richTextBox1.Text += "寫成檔案" + fileName2 + "\n";

        }

        private void button59_Click(object sender, EventArgs e)
        {
            //WriteAllText 寫入/建立檔案
            //透過WriteAllText可以將文字寫入檔案(如果檔案不存在，會自動建立)，格式為:
            //File.WriteAllText(檔案位置及名稱, 字串);

            string x = "Hello text";
            File.WriteAllText("myfilename.txt", x);
            richTextBox1.Text += "寫檔完成\n";
        }

        private void button64_Click(object sender, EventArgs e)
        {
            //AppendAllText 插入文字
            //C# 將字串插入文件內容尾端
            richTextBox1.Text += "寫一筆資料到檔案尾端\n";
            File.AppendAllText("myfilename.txt", " append text to the end.");

            //讀取檔案
            // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
            string y = File.ReadAllText("myfilename.txt", System.Text.Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + y + "\n";
        }

    }
}

