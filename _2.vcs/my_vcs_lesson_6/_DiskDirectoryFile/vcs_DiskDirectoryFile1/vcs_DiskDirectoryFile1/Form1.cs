using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for Directory
using System.Collections;  // for ArrayList
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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            y_st += 20;

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
            bt_files10.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            bt_files11.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            bt_files12.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            bt_files13.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            bt_files14.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            bt_files15.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            bt_files16.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            bt_files17.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            bt_files18.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            bt_files19.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            richTextBox1.Size = new Size(430, 690);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 750 + 20);
            this.Text = "vcs_DiskDirectoryFile1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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
                message += "\n";
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
            message += "\n";
        }

        private void bt_file00_Click(object sender, EventArgs e)
        {
            //File的方法

            //檢查檔案 新建檔案 複製檔案

            richTextBox1.Text += "檔案1 拷貝 到 檔案2\n";

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";

            if (File.Exists(filename1) == true)  // 確認檔案1是否存在
            {
                richTextBox1.Text += "檔案1存在, 準備複製\n";
                if (File.Exists(filename2) == false)  // 確認檔案2是否存在
                {
                    File.Copy(filename1, filename2);
                    richTextBox1.Text += "已複製檔案, 檔案1 拷貝 到 檔案2\n";
                }
                else
                {
                    richTextBox1.Text += "檔案2已存在，無法複製\n";

                    string filename3 = @"D:\_git\vcs\_1.data\______test_files1\picture1ccc.jpg";
                    //移動檔案，從 filename2 移動到 filename3
                    if (File.Exists(filename3) == false)  // 確認檔案3是否存在
                    {
                        File.Move(filename2, filename3);
                        richTextBox1.Text += "已移動檔案: " + filename2 + " 到 " + filename3 + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "檔案: " + filename3 + " 已存在，無法移動\n";

                        //刪除檔案
                        File.Delete(filename3);
                        richTextBox1.Text += "檔案3已存在, 已刪除\n";
                    }
                }
            }
            else
            {
                richTextBox1.Text += "檔案1不存在，無法複製\n";

                // 偽執行 File.Create(filename1);
                richTextBox1.Text += "檔案1不存在, 已建立\n";
            }

            //------------------------------------------------------------  # 60個

            //建立檔案
            string filename4 = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";
            FileStream fs = File.Create(filename4);
            fs.Close();
            richTextBox1.Text += "已建立檔案: " + filename4 + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "各種 Directory/File 操作\n";

            // 目前路徑
            string folderpath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前路徑: " + folderpath + "\n";

            string filename1b = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";
            string filename2b = @"D:\_git\vcs\_1.data\______test_files1\tmp_article.txt";
            string filename3b = @"D:\_git\vcs\_1.data\______test_files1\tmp_article_new.txt";

            if (File.Exists(filename1b) == false)
            {
                richTextBox1.Text += "檔案不存在, 建立之。\n";
            }

            if (File.Exists(filename2b) == false)
            {
                richTextBox1.Text += "檔案 : " + filename2b + ", 不存在, 建立之\n";
                File.Copy(filename1b, filename2b);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "將檔案 : " + filename2b + ", 改檔名成 : " + filename3b + "\n";
            File.Move(filename2b, filename3b);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            if (File.Exists(filename3b) == true)
            {
                richTextBox1.Text += "檔案 : " + filename3b + ", 已存在, 刪除之\n";
                richTextBox1.Text += "直接刪除, 不放進垃圾桶\n";
                File.Delete(filename3b);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            //File.SetAttributes(filename, FileAttributes.Hidden);//隱藏
            richTextBox1.Text += File.GetAttributes(filename) + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        //------------------------------------------------------------  # 60個

        private void bt_file01_Click(object sender, EventArgs e)
        {
            //FileInfo的方法

            //取得檔案資訊
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            FileInfo fi = new FileInfo(filename);
            if (fi.Exists == false)      //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
            }
            else
            {
                richTextBox1.Text += "資料夾：" + fi.Directory + "\n";
                richTextBox1.Text += "檔名：" + fi.Name + "\n";
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + "\n";

                richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + "\n";
                richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + "\n";
                richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + "\n";
                //Response.Write("修改時間：" + fi.LastWriteTime.ToString() + "<br>");
                //Response.Write("創建時間：" + fi.CreationTime.ToString() + "<br>");

                richTextBox1.Text += "Name :" + fi.Name + "\n";
                richTextBox1.Text += "FullName :" + fi.FullName + "\n";
                richTextBox1.Text += "Directory :" + fi.Directory + "\n";
                richTextBox1.Text += "DirectoryName :" + fi.DirectoryName + "\n";
                richTextBox1.Text += "Extension :" + fi.Extension + "\n";
                richTextBox1.Text += "Length :" + fi.Length.ToString() + "\n";
                //C# 取得檔案建立日期,及最後修改日期 
                richTextBox1.Text += "檔案建立日期" + fi.CreationTime.ToString() + "\n";
                richTextBox1.Text += "檔案最後修改日期" + fi.LastWriteTime.ToString() + "\n";
                //C# 取得檔案路徑、副檔名、檔案大小
                richTextBox1.Text += "檔案路徑： " + filename.ToString() + "\n";
                richTextBox1.Text += "副檔名： " + filename.Substring(filename.LastIndexOf(".") + 1, filename.Length - filename.LastIndexOf(".") - 1) + "\n";    //取得副檔名
                richTextBox1.Text += "檔案大小： " + File.Open(filename, FileMode.Open).Length.ToString() + " 位元組\n";
                richTextBox1.Text += "\n";
            }

            return;

            //------------------------------------------------------------  # 60個

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            FileAttributes attr = (new FileInfo(filename)).Attributes;
            if ((attr & FileAttributes.ReadOnly) > 0)
            {
                richTextBox1.Text += "唯讀檔案\n";
            }
            else
            {
                richTextBox1.Text += "一般檔案\n";
            }

            //------------------------------------------------------------  # 60個

            //設定檔案屬性
            filename = @"C:\_git\vcs\_1.data\______test_files1\cat\cat1.png";

            FileInfo f = new FileInfo(filename);
            f.Attributes = FileAttributes.ReadOnly;	//唯讀
            f.Attributes = FileAttributes.System;	//系統
            f.Attributes = FileAttributes.Archive;	//存檔
            f.Attributes = FileAttributes.Hidden;	//隱藏

            //------------------------------------------------------------  # 60個

            //刪除檔案 (不使用資源回收筒)
            fi = new FileInfo(@"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt");
            if (fi.Exists)       //確認檔案是否存在
            {
                fi.Delete();
                richTextBox1.Text += "檔案刪除成功\n";
            }
            else
            {
                richTextBox1.Text += "找不到檔案\n";
            }

            //------------------------------------------------------------  # 60個

            //取得檔案資訊 FileInfo

            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            fi = new FileInfo(filename);
            richTextBox1.Text += "Name : " + fi.Name + "\n";
            richTextBox1.Text += "FullName : " + fi.FullName + "\n";
            richTextBox1.Text += "Extension : " + fi.Extension + "\n";
            richTextBox1.Text += "Directory : " + fi.Directory + "\n";
            richTextBox1.Text += "DirectoryName : " + fi.DirectoryName + "\n";
            richTextBox1.Text += "長度 : " + fi.Length.ToString() + "\n";
            richTextBox1.Text += "IsReadOnly : " + fi.IsReadOnly + "\n";
            richTextBox1.Text += "CreationTime : " + fi.CreationTime + "\n";
            richTextBox1.Text += "CreationTimeUtc : " + fi.CreationTimeUtc + "\n";
            richTextBox1.Text += "LastAccessTime : " + fi.LastAccessTime + "\n";
            richTextBox1.Text += "LastAccessTimeUtc : " + fi.LastAccessTimeUtc + "\n";
            richTextBox1.Text += "LastWriteTime : " + fi.LastWriteTime + "\n";
            richTextBox1.Text += "LastWriteTimeUtc : " + fi.LastWriteTimeUtc + "\n";

        }

        private void bt_file02_Click(object sender, EventArgs e)
        {
            //新增資料夾/新增檔案/複製檔案

            //新增資料夾
            string new_foldername = "FFFFFFF/AAA/BBB/CCC/DDD";

            if (Directory.Exists(new_foldername) == true)
            {
                richTextBox1.Text += "資料夾已存在, 無法重新建立\n";
            }
            else
            {
                //新增資料夾
                Directory.CreateDirectory(new_foldername);
                richTextBox1.Text += "新增資料夾 完成\n";
            }

            //新增檔案
            string filename = "tmp_new_file.txt";
            if (File.Exists(filename) == true)
            {
                richTextBox1.Text += "檔案已存在, 無法重新建立\n";
            }
            else
            {
                StreamWriter sw = File.CreateText(filename);
                richTextBox1.Text += "新增檔案 完成\n";
            }

            //複製檔案
            string new_filename = "aaaaa.cs";
            if (File.Exists(new_filename) == true)
            {
                richTextBox1.Text += "檔案已存在, 無法複製檔案\n";
            }
            else
            {
                File.Copy(@"../../Form1.cs", new_filename);
                richTextBox1.Text += "複製檔案完成\n";
            }

        }

        private void bt_file03_Click(object sender, EventArgs e)
        {
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
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        //------------------------------------------------------------  # 60個

        int attr = 0;
        private void bt_file05_Click(object sender, EventArgs e)
        {
            //檔案時間
            //修改檔案時間 屬性
            string filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";
            if (File.Exists(filename) == false)  // 確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
                return;
            }
            if ((File.GetAttributes(filename) & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
            {
                richTextBox1.Text += "檔案唯讀，不能修改檔案時間\n";
            }
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
                {
                    File.SetAttributes(filename, FileAttributes.Archive);
                }
                else if (attr == 1)
                {
                    File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden);
                }
                else if (attr == 2)
                {
                    File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden | FileAttributes.ReadOnly);
                }
                attr++;
                if (attr > 2)
                {
                    attr = 0;
                }
                richTextBox1.Text += "檔案: " + filename + " 已存在\t更改後的檔案時間 與 檔案屬性\n";
                richTextBox1.Text += "建立時間: " + File.GetCreationTime(filename) + "\n";
                richTextBox1.Text += "修改時間: " + File.GetLastWriteTime(filename) + "\n";
                richTextBox1.Text += "存取時間: " + File.GetLastAccessTime(filename) + "\n";
                richTextBox1.Text += "檔案屬性: " + File.GetAttributes(filename).ToString() + "\n";
            }

            //------------------------------------------------------------  # 60個

            //讀取設定檔案時間
            filename = @"D:\_git\vcs\_1.data\______test_files1\mega.txt";

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

            //------------------------------------------------------------  # 60個

            if (File.Exists(filename) == false)  // 確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
            }
            else
            {
                richTextBox1.Text += "檔案: " + filename + " 已存在\n";
                richTextBox1.Text += "建立時間: " + File.GetCreationTime(filename) + "\n";
                richTextBox1.Text += "修改時間: " + File.GetLastWriteTime(filename) + "\n";
                richTextBox1.Text += "存取時間: " + File.GetLastAccessTime(filename) + "\n";
                richTextBox1.Text += "檔案屬性: " + File.GetAttributes(filename).ToString() + "\n";
            }

            //------------------------------------------------------------  # 60個


        }

        private void bt_file06_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            if (File.Exists(filename))  // 確認檔案是否存在
            {
                richTextBox1.Text += "完整路徑檔名 : " + Path.GetFullPath(filename) + "\n";
                richTextBox1.Text += "路徑 : " + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "檔名(包含副檔名) : " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名) : " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名 : " + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "根目錄 : " + Path.GetPathRoot(filename) + "\n";

                richTextBox1.Text += "修改成完整時間檔名 : " + Path.GetDirectoryName(filename) + "\\" + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "修改成時間檔名 : " + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
            }

            richTextBox1.Text += "取得任意檔名 : " + Path.GetRandomFileName() + "\n";
            richTextBox1.Text += "取得臨時檔名 : " + Path.GetTempFileName() + "\n";
            richTextBox1.Text += "取得臨時路徑 : " + Path.GetTempPath() + "\n";

            string RandomFileName = Path.GetRandomFileName();
            richTextBox1.Text += "建立隨機檔案: " + RandomFileName + "\n";
            string TempFileName = Path.GetTempFileName();
            richTextBox1.Text += "建立暫存檔案: " + TempFileName + "\n";

            //------------------------------------------------------------  # 60個

            //檔名處理

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            richTextBox1.Text += "全檔名 : " + filename + "\n";

            string d_name = Path.GetDirectoryName(filename);
            string f_name = Path.GetFileNameWithoutExtension(filename);
            string ext_name = Path.GetExtension(filename);

            string filename2 = "tmp_" + f_name + "_new" + ext_name;

            richTextBox1.Text += "新全檔名 : " + filename2 + "\n";

            //自動檔名 與 存檔語法
            string filename3 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            richTextBox1.Text += "新全檔名 : " + filename3 + "\n";



        }

        private void bt_file07_Click(object sender, EventArgs e)
        {
            //取得檔名與副檔名
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
        }

        private void bt_file08_Click(object sender, EventArgs e)
        {

        }

        private void bt_file09_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir00_Click(object sender, EventArgs e)
        {
            //Directory的方法

            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";

            //------------------------------------------------------------  # 60個

            //確認資料夾是否存在
            string Path = @"D:/_git/vcs/_1.data/______test_files1/aaaa/bbbb";
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + Path + " 不存在\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + Path + " 存在\n";
            }

            //------------------------------------------------------------  # 60個

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

            //------------------------------------------------------------  # 60個

            //刪除資料夾
            Path = @"D:/_git/vcs/_1.data/______test_files_file_name2";
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

            //------------------------------------------------------------  # 60個

            string path = @"D:\_git\vcs\_1.data\______test_files1\";

            if (Directory.Exists(path) == false)
            {
                richTextBox1.Text += "路徑不存在, 建立之。\n";
                Directory.CreateDirectory(path);
            }

            //------------------------------------------------------------  # 60個

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

            //------------------------------------------------------------  # 60個

            Path_old = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            Path_new = @"D:/_git/vcs/_1.data/______test_files_file_name3";
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
                {
                    richTextBox1.Text += "資料夾: " + destDirName + " 已存在\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + sourceDirName + " 不存在\n";
            }

            //------------------------------------------------------------  # 60個

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

            //------------------------------------------------------------  # 60個

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__text";

            foreach (String a in Directory.GetDirectories(foldername))
            {
                richTextBox1.Text += "找到資料夾\t" + a + "\n";
            }

            foreach (String a in Directory.GetFiles(foldername))
            {
                richTextBox1.Text += "找到檔案\t" + a + "\n";
            }

            //------------------------------------------------------------  # 60個



        }

        private void bt_dir01_Click(object sender, EventArgs e)
        {
            //DirectoryInfo的方法
            //DirectoryInfo
        }

        private void bt_dir02_Click(object sender, EventArgs e)
        {
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
        }

        private void bt_dir05_Click(object sender, EventArgs e)
        {
        }

        private void bt_dir06_Click(object sender, EventArgs e)
        {
        }

        private void bt_dir07_Click(object sender, EventArgs e)
        {
        }

        private void bt_dir08_Click(object sender, EventArgs e)
        {
        }

        private void bt_dir09_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files00_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\compare\ssss.txt";
            if (FileCompare(filename1, filename2) == true)
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename2 + " 相同。\n";
            }
            else
            {
                richTextBox1.Text += "檔案 " + filename1 + " 和 檔案 " + filename2 + " 不同。\n";
            }
            if (FileCompare(filename1, filename3) == true)
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

            message += size.ToString() + "\n";
            message += "Get All FileNames\n";

            GetAllFileNames(d);
            message += "Total filesize: " + filesize_all.ToString() + " Bytes.\n";
            message += "Total filesize: " + size.ToString() + " Bytes.\n";
            richTextBox1.Text += message + "\n";
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
            richTextBox1.Text += "檔案個數 = " + files.Length.ToString() + "\n";
            richTextBox1.Text += "資料夾: " + target_dir + "\n";
            foreach (string file in files)
            {
                richTextBox1.Text += "檔案: " + file + "\t";
                //richTextBox1.Text += "Size: " + file.Length.ToString() + " 拜\n"; wrong
                File.SetAttributes(file, FileAttributes.Normal);
                richTextBox1.Text += file + "\t";
                richTextBox1.Text += file.Length.ToString() + "\n";
                //File.Delete(file);
            }
            richTextBox1.Text += "\n";
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "資料夾: " + dir + "\n";
                ShowDirectory2(dir);
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
            message += dirInfo.Attributes.ToString() + "\n";

            // Get the files in the directory and print out some information about them.
            FileInfo[] fis = dirInfo.GetFiles("*.*");

            foreach (FileInfo fi in fis)
            {
                message += "data: ";
                message += fi.Name + "   " + fi.LastAccessTime + "   " + fi.Length + "\n";
            }

            // Get the subdirectories directly that is under the root.
            // See "How to: Iterate Through a Directory Tree" for an example of how to
            // iterate through an entire tree.
            DirectoryInfo[] dirInfos = dirInfo.GetDirectories("*.*");

            foreach (DirectoryInfo d in dirInfos)
            {
                message += "data: " + "   " + d.Name + "\n";
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
                message += "資料夾\n";
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
                    }
                    else
                    */
                    message += "\n";
                }

                /*  檢查每個檔案的資訊
                message += "檔案\n";
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
                    message += di.IsReadOnly + "\n";
                }
                */
            }
            else
            {
                MessageBox.Show("No Exist");
            }
            richTextBox1.Text += message + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_files06_Click(object sender, EventArgs e)
        {
            //讀取資料夾下所有資料夾
            string path = @"D:\_git\vcs\_1.data\______test_files1";

            //讀取資料夾下所有資料夾
            GetDirectories(path);

            //讀取資料夾下所有檔案
            GetFiles(path);

            //------------------------------------------------------------  # 60個

            //搜尋檔案
            if (GetFile() == true)
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

        //------------------------------------------------------------  # 60個

        private void bt_files07_Click(object sender, EventArgs e)
        {
            //撈出資料夾內所有jpg檔
            //撈出資料夾內所有jpg檔
            var dirnames = Directory.GetDirectories(@"D:\_git\vcs\_1.data\______test_files1");
            try
            {
                foreach (var dir in dirnames)
                {
                    richTextBox1.Text += "aaaa3 dir = " + dir + "\n";
                    var fnames = Directory.GetFiles(dir, "*.jpg").Select(Path.GetFileName);

                    DirectoryInfo d = new DirectoryInfo(dir);
                    FileInfo[] fis = d.GetFiles("*.jpg");
                    foreach (var f in fnames)
                    {
                        richTextBox1.Text += f + "\n";

                        if (!File.Exists(Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", ""))))
                        {
                            File.Move(Path.Combine(dir, f), Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", "")));
                        }
                        else
                        {
                            richTextBox1.Text += "The file you are attempting to rename already exists! The file path is " + dir + "\n";
                            foreach (FileInfo fi in fis)
                            {
                                richTextBox1.Text += "The file modify date is: " + File.GetLastWriteTime(dir) + "\n";
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

        //------------------------------------------------------------  # 60個

        private void bt_files08_Click(object sender, EventArgs e)
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
                    {
                        files.Add(filename);
                    }
                }
            }
            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }

        //------------------------------------------------------------  # 60個

        private void bt_files09_Click(object sender, EventArgs e)
        {
        }

        private void bt_files10_Click(object sender, EventArgs e)
        {
        }

        private void bt_files11_Click(object sender, EventArgs e)
        {
        }

        private void bt_files12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files13_Click(object sender, EventArgs e)
        {

        }

        private void bt_files14_Click(object sender, EventArgs e)
        {

        }

        private void bt_files15_Click(object sender, EventArgs e)
        {

        }

        private void bt_files16_Click(object sender, EventArgs e)
        {

        }

        private void bt_files17_Click(object sender, EventArgs e)
        {

        }

        private void bt_files18_Click(object sender, EventArgs e)
        {

        }

        private void bt_files19_Click(object sender, EventArgs e)
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

/*
string dir1 = @"C:\______test_files\compare1";

string[] file_names1 = Directory.GetFiles(dir1);
for (int i = 0; i < file_names1.Length; i++)
{
    richTextBox1.Text += "i = " + i.ToString() + "\t" + file_names1[i] + "\n";
    file_names1[i] = file_names1[i].Replace(dir1, "");
    richTextBox1.Text += "i = " + i.ToString() + "\t" + file_names1[i] + "\n";
}
Array.Sort(file_names1);

List<string> name_list = new List<string>();
for (int i = 0; i < file_names1.Length; i++)
{
    richTextBox1.Text += "i = " + i.ToString() + "\t" + file_names1[i] + "\n";
    name_list.Add(file_names1[i]);
}

DirectoryInfo dir1_info = new DirectoryInfo(dir1);
FileInfo[] fi = dir1_info.GetFiles();

int len = fi.Length;
richTextBox1.Text += "len = " + len.ToString() + "\n";

for (int i = 0; i < len; i++)
{
    richTextBox1.Text += fi[i].Name + "\n";
}

//------------------------------------------------------------  # 60個

	//C# 取得資料夾下的所有檔案(包括子目錄)
	//顯示每個檔案的資訊
        private void button1_Click(object sender, EventArgs e)
        {
            string path = String.Empty;
            string filetype = String.Empty;
            filetype = "*.*";

            //path = @"D:\_DATA2\_VIDEO_全為備份\百家??_清十二帝疑案";
            path = @"C:\______test_files";

            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(path, filetype, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                richTextBox1.Text += "原撈到的檔案 : " + filename + "\n";
            }
        }

//------------------------------------------------------------  # 60個

            //使用递归法删除文件夹中的所有文件
            string foldername = @"D:\_git\vcs\_1.data\______test_files2\_book_magazine";

            int file_no = 0;
            DirectoryInfo DInfo = new DirectoryInfo(foldername);//创建DirectoryInfo对象
            FileSystemInfo[] FSInfo = DInfo.GetFileSystemInfos();  // 獲取所有的文件
            for (int i = 0; i < FSInfo.Length; i++)//遍歷獲取到的文件
            {
                FileInfo FInfo = new FileInfo(foldername + "\\" + FSInfo[i].ToString());//创建FileInfo对象
                //FInfo.Delete();//删除文件
                richTextBox1.Text += "偽刪除 " + foldername + "\\" + FSInfo[i].ToString() + "\n";
                file_no++;
            }
            richTextBox1.Text += "删除成功\n共刪除 " + file_no.ToString() + " 個檔案\n";

//------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            string path2 = @"../../data";
            string fnShow = "檔案清單---<*.TXT>";
            try
            {
                //取得檔案路徑訊息
                DirectoryInfo currentDir = new
                   DirectoryInfo(path2);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = currentDir.GetFiles("*.txt");
                //設定檔案的標題
                //string header = fnShow + "\n" + $"{"檔名",-16}{"檔案長度",-12}{"修改日期"}" + "\n";
                string header = fnShow + "\n" + "檔名" + "檔案長度" + "修改日期" + "\n";
                richTextBox1.Text = header;

                // 讀取資料夾中有關於 --檔名(Name)、長度(Length) 和 修改日期(LastWriteTime)
                foreach (FileInfo getInfo in listFile)
                {
                    // richTextBox1.Text += $"{getInfo.Name,-15}" +
                    //   $"{getInfo.Length.ToString(),-11}" +
                    //   $"{getInfo.LastWriteTime.ToShortDateString(),15}" + "\n";
                    richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + getInfo.LastWriteTime.ToShortDateString() + "\n";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //新增檔案
            //指定路徑建立檔案
            string path = @"_tmp_aaaa.txt";
            FileInfo createFile = new FileInfo(path);
            //以Create方法新增一個檔案
            FileStream fs = createFile.Create();
            fs.Close();//關閉檔案

            //複製檔案
            path = @"_tmp_aaaa.txt";
            //目的檔案「Text.txttmp」
            String tagPath = path + "tmp";
            FileInfo copyFile = new FileInfo(path);
            try
            {
                //以CopyTo方法複製檔案
                copyFile.CopyTo(tagPath);
                richTextBox1.Text = path + " 已複製";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }

            //刪除檔案
            path = @"_tmp_aaaa.txt";
            copyFile = new FileInfo(path);
            if (copyFile.Exists == false)//查看檔案是否存在
            {
                MessageBox.Show("無此檔案");
            }
            else
            {
                copyFile.Delete();//刪除檔案
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string path = @"_tmp_bbbb.txt";
            string str;
            FileStream fs = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.Unicode);

            //想儲存的文字
            str = "aaaaaaaaa";
            sw.WriteLine(str);  //將資料寫入檔案
            sw.Close();   //關閉sw資料流

            //檔案內所輸入的文字為
            FileStream f = new FileStream(path, FileMode.OpenOrCreate, FileAccess.Read);
            StreamReader sr = new StreamReader(f, Encoding.Unicode);
            sr.BaseStream.Seek(0, SeekOrigin.Begin);
            while (sr.Peek() > -1)
            {
                richTextBox1.Text += sr.ReadLine() + "\n";//讀出檔案
            }
            sr.Close();  //關閉資料流
        }

//------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                string path = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\";
                //取得資料夾最後一次被存取的時間
                DateTime dt = Directory.GetLastWriteTime(path);
                //如果資料夾不存在就建立資料夾
                if (!Directory.Exists(path))
                {
                    Directory.CreateDirectory(path);
                }
                else
                {
                    richTextBox1.Text += "資料夾建立的時間 : " + dt + "\n";
                }
                //更新時間
                Directory.SetLastWriteTime(path, DateTime.Now);
                dt = Directory.GetLastWriteTime(path);
                richTextBox1.Text += "最後存取時間 : " + dt + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無法建立 : " + e.ToString() + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //BinaryReader

            BinaryReader readBit;
            FileStream objStream;
            //設定欲讀取檔案的路徑
            string path = @"D:\_git\vcs\_1.data\______test_files1\__RW\_bin\vcs_ReadWrite_BIN.bin";

            int count = 0;
            try
            {
                objStream = new FileStream(path, FileMode.Open, FileAccess.Read);

                //使用using陳述詞，確保資源的釋放
                using (readBit = new BinaryReader(objStream))
                {
                    do
                    {
                        //以位元組為單位讀取檔案內容，16進位方式顯示
                        richTextBox1.Text += readBit.ReadByte().ToString() + " ";
                        count += 1;
                        //'** 換行
                        if (count == 10)
                        {
                            richTextBox1.Text += "\n";
                            count = 0;
                        }
                    } while (true);
                }
            }
            catch (IndexOutOfRangeException ex)
            {
                richTextBox1.Text += "沒有指定檔案\n";
            }

            catch (EndOfStreamException ex)
            {
                richTextBox1.Text += "檔案讀取完畢\n";
            }

            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //BinaryWriter

            BinaryWriter objWriter;
            FileStream objStream;
            string path = @"tmp_BinaryWriter.txt";
            try
            {
                objStream = new FileStream(path, FileMode.Append, FileAccess.Write);
                //使用using敘詞，寫入完墓會自動釋放資源
                using (objWriter = new BinaryWriter(objStream))
                {
                    // 寫入字串
                    objWriter.Write("空山不見人");
                    objWriter.Write("Visual C# 7.0");
                    // 寫入數值
                    objWriter.Write(640526);
                }
            }
            catch (IndexOutOfRangeException ex)
            {
                richTextBox1.Text += "沒有指定檔案\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }

            //------------------------------------------------------------  # 60個

            BinaryReader objReader;
            //FileStream objStream;
            path = @"tmp_03aa.txt";
            try
            {
                objStream = new FileStream(path, FileMode.Open, FileAccess.Read);
                objReader = new BinaryReader(objStream);
                richTextBox1.Text += objReader.ReadString() + "\n";
                richTextBox1.Text += objReader.ReadInt32() + "\n";
                objReader.Close();
            }
            catch (IndexOutOfRangeException ex)
            {
                richTextBox1.Text += "沒有指定檔案\n";
            }

            catch (EndOfStreamException ex)
            {
                richTextBox1.Text += "檔案讀取完畢\n";
            }

            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
        }

//------------------------------------------------------------  # 60個

            //DirectoryInfo 測試

            // 建立DirectoryInfo類別的dir物件，可用來操作資料夾目錄
            DirectoryInfo dir = new DirectoryInfo("D:\\_git\\vcs\\CSharp");
            if (dir.Exists)
            {	// 判斷目錄是否存在
                richTextBox1.Text += "D:\\_git\\vcs\\CSharp 路徑存在, 不建立目錄\n";
            }
            else
            {
                richTextBox1.Text += "D:\\_git\\vcs\\CSharp 路徑不存在，建立目錄\n";
                dir.Create();	// 建立目錄
                dir.Refresh();	// 重新整理目錄
            }
            richTextBox1.Text += dir.FullName + " 檔案資訊如下 :\n";
            richTextBox1.Text += "建立時間 : " + dir.CreationTime + "\n";
            richTextBox1.Text += "存取時間 : " + dir.LastAccessTime + "\n";
            richTextBox1.Text += "資料夾名稱 : " + dir.Name + "\n";
            richTextBox1.Text += "根目錄 : " + dir.Parent + "\n";

            Console.Write("是否刪除 D:\\_git\\vcs\\CSharp 資料夾   1.刪除  2.不刪除->");
            if (Console.ReadLine() == "1")
            {
                try
                {
                    dir.Delete();	       // 刪除檔案
                    richTextBox1.Text += "刪除成功" + "\n";
                }
                catch (Exception ex)   // 刪除檔案失敗會產生例外
                {
                    richTextBox1.Text += "刪除失敗" + "\n";
                    richTextBox1.Text += ex.Message + "\n";  // 顯示例外訊息
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //Console.Write("請輸入路徑->");
            //string fpath = Console.ReadLine();

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            DirectoryInfo dir2 = new DirectoryInfo(foldername);
            if (!dir2.Exists)	//判斷路徑是否不存在
            {
                richTextBox1.Text += "路徑不存在" + "\n";
                return;
            }
            richTextBox1.Text += dir2.FullName + ", 資料夾下的子資料夾如下 :\n";
            DirectoryInfo[] subdir = dir2.GetDirectories();
            foreach (DirectoryInfo r in subdir)
            {
                richTextBox1.Text += "完整路徑 : " + r.FullName + "\t建立時間 : " + r.CreationTime + "\n";
            }

//------------------------------------------------------------  # 60個

            string input, sel;
            StreamReader sr;
            StreamWriter sw;
            FileInfo f;
            string filename = "tmp_aaaa.txt";

            f = new FileInfo(filename);

            Console.Write("請選擇功能->1.寫入  2.附加   其他.離開：");

            sel = "1";
            if (sel == "1")
            {
                sw = f.CreateText();  //開啟新檔
                input = "寫入AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
                //將輸入的資料覆蓋原檔並重新寫入
                sw.WriteLine(input);
                sw.Flush();
                sw.Close();

            }
            else if (sel == "2")
            {
                sw = f.AppendText();   //開啟舊檔
                input = "附加AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
                //將輸入的資料附加到資料檔的最後
                sw.WriteLine(input);
                sw.Flush();
                sw.Close();
            }

            sr = f.OpenText();  //以唯讀模式開檔
            Console.WriteLine("資料檔內容如下：");
            Console.WriteLine(sr.ReadToEnd());//讀出資料
            sr.Close();
            Console.WriteLine("================================");

//------------------------------------------------------------  # 60個

file.
            //拷貝臨時數據庫到目標數據庫(覆蓋)
            File.Copy(temp, strPathMdb, true);
            
            //最後刪除臨時數據庫
            File.Delete(temp);

//------------------------------------------------------------  # 60個

textBox1.Text = File.ReadAllText(@"C:\鹿柴.txt");
textBox1.Text = File.ReadAllText(@"C:\鹿柴.txt");
textBox1.Text = File.ReadAllText(@"C:\春曉.txt");
textBox1.Text = File.ReadAllText(@"C:\夜思.txt");

            if (File.ReadAllText("setting.txt") != null)
            {
                folderPath = File.ReadAllText("setting.txt");
            }
            else
            {

                    File.WriteAllText(@"setting.txt", folderPath);
//------------------------------------------------------------  # 60個

在 C# 中使用 File.ReadAllText() 方法將檔案讀取為字串
string text = File.ReadAllText(@"C:\File\file.txt");
Console.WriteLine(text);

在 C# 中使用 StreamReader.ReadToEnd() 方法將檔案讀取為字串
StreamReader fileReader = new StreamReader(@"C:\File\file.txt");
string text = fileReader.ReadToEnd();
Console.WriteLine(text);			

//------------------------------------------------------------  # 60個

            string filename = @"C:\______test_files\_case1\pic1.jpg";
            FileStream fs = File.OpenRead(filename); //OpenRead[二進位讀檔]
            int filelength = 0;
            filelength = (int)fs.Length; //獲得檔長度
            Byte[] image = new Byte[filelength]; //建立一個位元組陣列
            fs.Read(image, 0, filelength); //按位元組流讀取
            System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
            fs.Close();

            //pictureBox1.Image = (Image)image;

//------------------------------------------------------------  # 60個

[C#] 圖片檔讀取：非鎖定檔方法 [Image.FromFile 釋放]

content from http://jashliao.pixnet.net/blog/post/223534989


FileStream fs = File.OpenRead(StrDestFilePath); //OpenRead[二進位讀檔]
int filelength = 0;
filelength = (int)fs.Length; //獲得檔長度
Byte[] image = new Byte[filelength]; //建立一個位元組陣列
fs.Read(image, 0, filelength); //按位元組流讀取
System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
fs.Close();

//------------------------------------------------------------  # 60個

    [C#] 幾個常用的取路徑及檔名的方法

string file = @"d:\abc\123.txt"

Path.GetFileNameWithoutExtension(file) 取得檔案名,不包含副檔名,本例得到123

Path.GetExtension(file) 取得副檔名txt

Path.GetPathRoot(file) 取得根目錄

Path.GetFullPath(file) 取得路徑

//------------------------------------------------------------  # 60個

待測
//File.AppendAllText("E:\\Time\\新建文檔夾 (2)" + "/" + strname, DateTime.Now+"\r\n");

//------------------------------------------------------------  # 60個

根據時間建立文件
File.Create("C:\\______test_files\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//建立文件

建立臨時檔案
File.Create("tmp_" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件

//------------------------------------------------------------  # 60個

//開啟檔案
FileStream myFile = File.Open(@"C:\myWriter.txt", FileMode.OpenOrCreate, FileAccess.ReadWrite);

BinaryReader myReader = new BinaryReader(myFile);

int dl = System.Convert.ToInt16(myFile.Length);
//讀取位元陣列

byte[] myData = myReader.ReadBytes(dl);
//釋放資源

myReader.Close();

myFile.Close();

//------------------------------------------------------------  # 60個

            //資料夾改名
            Directory.Move(textBox1.Text,textBox2.Text);
            //檔案改名
            File.Move(textBox1.Text+"\\"+listBox1.SelectedItem.ToString(), textBox1.Text+"\\"+textBox2.Text);

//------------------------------------------------------------  # 60個

用C#重命名文件
File.Move("oldfilename", "newfilename");
File.Move(oldNameFullPath, newNameFullPath);

//Delete the file if exists, else no exception thrown.

File.Delete(newFileName); // Delete the existing file if exists
File.Move(oldFileName,newFileName); // Rename the oldFileName into newFileName

//------------------------------------------------------------  # 60個

您可以将其复制为新文件，然后使用File类删除旧文件：

if (File.Exists(oldName))
{
    File.Copy(oldName, newName, true);
    File.Delete(oldName);
}

using System.IO;

string oldFilePath = @"C:\OldFile.txt"; // Full path of old file
string newFilePath = @"C:\NewFile.txt"; // Full path of new file

if (File.Exists(newFilePath))
{
    File.Delete(newFilePath);
}
File.Move(oldFilePath, newFilePath);

//------------------------------------------------------------  # 60個

Directory.
            //撈出一層jpg檔
            string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";
            string[] filenames = Directory.GetFiles(foldername, "*.jpg");

            foreach (string filename in filenames)
            {
                richTextBox1.Text += "取得檔案 : " + filename + "\n";
            }

//------------------------------------------------------------  # 60個

ffff dddd
檔名資料夾名處理 大整理 在 vcs_Mix00

                richTextBox1.Text += "原完整檔名 : " + textBox1.Text + "\n";
                string filename = textBox1.Text;
                filename = filename.Substring(filename.LastIndexOf("\\") + 1, filename.Length - filename.LastIndexOf("\\") - 1);
                richTextBox1.Text += "原簡單檔名 : " + filename + "\n";


取得檔案副檔名:
string extension = Path.GetExtension("C:\\soar.jpg");
string extension = Path.GetExtension(filename);
        
        private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;

            richTextBox1.Text += "CurrentDir1 = " + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "CurrentDir2 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent + "\n";
            richTextBox1.Text += "CurrentDir3 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent + "\n";
            richTextBox1.Text += "CurrentDir4 = " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName + "\n";
            richTextBox1.Text += "CurrentDir5 = " + CurrentDir + "\n";

            CurrentDir1 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap\bin\Debug
            CurrentDir2 = bin
            CurrentDir3 = vcs_GMap
            CurrentDir4 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap
            CurrentDir5 = C:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Network\vcs_GMap\vcs_GMap

            //private string CurrentDir = new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName;

string[] s = Directory.GetFiles(@"D:\項目\Web\Images\shiji"); //獲得文件夾目錄下所有文件全路徑
string[] s = Directory.GetFiles(@"D:\項目\Web\Images\shiji","*.jpg"); //獲得文件夾目錄下指定後綴名文件全路徑
string[] s = Directory.GetDirectories(@"D:\項目\Web\Images"); //獲得文件夾目錄下的文件夾的全路徑

//附隨檔案的寫法
string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\AAAAA.BBBBB";
string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";
string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";

richTextBox1.Text += filename + "\n\n";

//------------------------------------------------------------  # 60個



*/

