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

            listView1.Size = new Size(400, 340);
            listView1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            listBox1.Size = new Size(400, 340);
            listBox1.Location = new Point(x_st + dx * 4, y_st + dy * 5);

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1700, 750 + 20);
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
            string[] filenames = Directory.GetFiles(target_dir);  // 由資料夾取出檔案名稱串列
            string[] dirs = Directory.GetDirectories(target_dir);  // 由資料夾取出資料夾名稱串列
            foreach (string file in filenames)
            {
                richTextBox1.Text += "刪除檔案: " + file + "\n";
                File.SetAttributes(file, FileAttributes.Normal);
                File.Delete(file);  // 刪除檔案
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
            }

            // 傳回比較的結果。在這個時候，只有當兩個檔案
            // 的內容完全相同時，"file1byte" 才會等於 "file2byte"。
            return ((file1byte - file2byte) == 0);
        }

        //刪除資料夾，recursive為True時，直接刪除資料夾及其資料夾下所有文件或資料夾;recursive為False時，需先將資料夾下所有文件或資料夾刪除
        private void DeleteDirectory(string foldername, bool recursive)
        {
            if (Directory.Exists(foldername))     //確認資料夾是否存在
            {
                if (recursive)
                {
                    Directory.Delete(foldername, true);
                    richTextBox1.Text += "已刪除資料夾: " + foldername + "\n";
                }
                else
                    richTextBox1.Text += "需要先把資料夾內的檔案刪除\n";
            }
        }

        public static double DirSize(DirectoryInfo dinfo)
        {
            double Size = 0;

            // Add file sizes.
            FileInfo[] fis = dinfo.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo fi in fis)
            {
                Size += fi.Length;
            }

            // Add subdirectory sizes.
            DirectoryInfo[] dis = dinfo.GetDirectories();  // 由DI取得DI陣列, 單層資料夾資訊
            foreach (DirectoryInfo di in dis)
            {
                if (di.Name != "System Volume Information" && di.Name.Substring(0, 1) != "$")//避開此類folder權限問題
                    Size += DirSize(di);   //利用遞迴把子資料夾也計算進來
            }
            return (Size);
        }

        string message = "";
        double filesize_all = 0;

        public void GetAllFileNames(DirectoryInfo dinfo)
        {
            // Add file sizes.
            FileInfo[] fis = dinfo.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo fi in fis)
            {
                message += fi.Name;
                message += "\t";
                message += fi.Length.ToString(); ;
                message += "\n";
                filesize_all += fi.Length;
            }
            // Add subdirectory sizes.
            DirectoryInfo[] dis = dinfo.GetDirectories();  // 由DI取得DI陣列, 單層資料夾資訊
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
            /*
            //File 的方法
            File.Exists()
            File.Create()
            File.Copy()
            File.Move()
            File.Delete()
            File.Open()
            File.OpenRead()
            File.ReadAllText()
            File.WriteAllText()
            File.AppendAllText()

            File.GetAttributes()	檔案屬性
            File.GetCreationTime()	建立時間
            File.GetLastWriteTime()	修改時間
            File.GetLastAccessTime()存取時間

            File.SetAttributes()
            File.SetCreationTime()
            File.SetLastWriteTime()
            File.SetLastAccessTime()
            */

            //檢查檔案 新建檔案 複製檔案

            richTextBox1.Text += "檔案1 拷貝 到 檔案2\n";

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\picture1a.jpg";

            if (File.Exists(filename1) == true)  // 確認檔案1是否存在
            {
                richTextBox1.Text += "檔案1存在, 準備複製\n";
                if (File.Exists(filename2) == false)  // 確認檔案2是否存在
                {
                    File.Copy(filename1, filename2);  // 檔案拷貝
                    richTextBox1.Text += "已複製檔案, 檔案1 拷貝 到 檔案2\n";
                }
                else
                {
                    richTextBox1.Text += "檔案2已存在，無法複製\n";

                    string filename3 = @"D:\_git\vcs\_1.data\______test_files1\picture1ccc.jpg";
                    //移動檔案，從 filename2 移動到 filename3
                    if (File.Exists(filename3) == false)  // 確認檔案3是否存在
                    {
                        File.Move(filename2, filename3);  // 檔案重新命名
                        richTextBox1.Text += "已移動檔案: " + filename2 + " 到 " + filename3 + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "檔案: " + filename3 + " 已存在，無法移動\n";

                        File.Delete(filename3);  // 刪除檔案
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
                File.Copy(filename1b, filename2b);  // 檔案拷貝
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "將檔案 : " + filename2b + ", 改檔名成 : " + filename3b + "\n";
            File.Move(filename2b, filename3b);  // 檔案重新命名

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            if (File.Exists(filename3b) == true)
            {
                richTextBox1.Text += "檔案 : " + filename3b + ", 已存在, 刪除之\n";
                richTextBox1.Text += "直接刪除, 不放進垃圾桶\n";
                File.Delete(filename3b);  // 刪除檔案
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //複製檔案
            string new_filename = "aaaaa.cs";
            if (File.Exists(new_filename) == true)
            {
                richTextBox1.Text += "檔案已存在, 無法複製檔案\n";
            }
            else
            {
                File.Copy(@"../../Form1.cs", new_filename);  // 檔案拷貝
                richTextBox1.Text += "複製檔案完成\n";
            }

            /*
            File.Copy(oldName, newName, true);  // 檔案拷貝
            File.Copy(temp, strPathMdb, true);  // 檔案拷貝 //拷貝臨時數據庫到目標數據庫(覆蓋)
            */
        }

        //------------------------------------------------------------  # 60個

        private void bt_file01_Click(object sender, EventArgs e)
        {
            //FileInfo 的方法

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
            filename = @"D:\_git\vcs\_1.data\______test_files1\cat\cat1.png";

            fi = new FileInfo(filename);
            fi.Attributes = FileAttributes.ReadOnly;	//唯讀
            fi.Attributes = FileAttributes.System;	//系統
            fi.Attributes = FileAttributes.Archive;	//存檔
            fi.Attributes = FileAttributes.Hidden;	//隱藏

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

            //------------------------------------------------------------  # 60個

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            fi = new FileInfo(filename);//创建FileInfo对象
            //定义一个字符串数组，用来存储文件的相关属性
            string[] strAttribute = new string[] { fi.Name, Convert.ToDouble(fi.Length / 1024).ToString(), fi.Extension, fi.CreationTime.ToString(), fi.IsReadOnly.ToString(), fi.LastWriteTime.ToString() };
            var values = from str in strAttribute//使用LINQ为文件属性赋值
                         select new
                         {
                             Name = strAttribute[0].ToString(),
                             Size = strAttribute[1].ToString(),
                             Exten = strAttribute[2].ToString(),
                             CTime = strAttribute[3].ToString(),
                             ReadOnly = strAttribute[4].ToString(),
                             WTime = strAttribute[5].ToString()
                         };
            foreach (var v in values)
            {
                //richTextBox1.Text += "aaaa"+
                richTextBox1.Text += "檔名 : " + v.Name.ToString() + "\n";//显示文件名
                richTextBox1.Text += "大小 : " + v.Size.ToString() + "\n";//显示文件大小
                richTextBox1.Text += "副檔名 : " + v.Exten.ToString() + "\n";//显示文件扩展名
                richTextBox1.Text += "建立時間 : " + v.CTime.ToString() + "\n";//显示文件创建时间
                richTextBox1.Text += "修改時間 : " + v.WTime.ToString() + "\n";//显示文件最后修改时间
                richTextBox1.Text += "是否唯讀 : " + v.ReadOnly.ToString() + "\n";//显示文件是否只读
            }
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

        void show_file_info(string filename)
        {
            richTextBox1.Text += "檔案: " + filename + "\n";
            richTextBox1.Text += "建立時間: " + File.GetCreationTime(filename) + "\n";
            richTextBox1.Text += "修改時間: " + File.GetLastWriteTime(filename) + "\n";
            richTextBox1.Text += "存取時間: " + File.GetLastAccessTime(filename) + "\n";
            richTextBox1.Text += "檔案屬性: " + File.GetAttributes(filename).ToString() + "\n";
        }

        int attr = 0;
        private void bt_file05_Click(object sender, EventArgs e)
        {
            // File.Get

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            //File.SetAttributes(filename, FileAttributes.Hidden);//隱藏
            richTextBox1.Text += File.GetAttributes(filename) + "\n";

            filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";
            if ((File.GetAttributes(filename) & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
            {
                richTextBox1.Text += "檔案唯讀，不能修改檔案時間\n";
            }
            else
            {
                show_file_info(filename);

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

                show_file_info(filename);
            }

            //------------------------------------------------------------  # 60個

            //讀取設定檔案時間
            filename = @"D:\_git\vcs\_1.data\______test_files1\mega.txt";

            show_file_info(filename);

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

            filename = @"D:\_git\vcs\_1.data\______test_files1\mega.txt";
            show_file_info(filename);
        }

        private void bt_file06_Click(object sender, EventArgs e)
        {
            //Path 的方法
            /*            
            Path.GetFullPath()完整路徑檔名
            Path.GetDirectoryName()路徑
            Path.GetFileName()檔名(包含副檔名)
            Path.GetFileNameWithoutExtension()檔名(不包含副檔名)
            Path.GetExtension()副檔名
            Path.GetPathRoot()根目錄
            Path.Combine()

            Path.GetRandomFileName()取得任意檔名
            Path.GetTempFileName()取得臨時檔名
            Path.GetTempPath()取得臨時路徑
            */

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            if (File.Exists(filename))  // 確認檔案是否存在
            {
                richTextBox1.Text += "完整路徑檔名 : " + Path.GetFullPath(filename) + "\n";  // 取得路徑
                richTextBox1.Text += "路徑 : " + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "檔名(包含副檔名) : " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名) : " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名 : " + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "根目錄 : " + Path.GetPathRoot(filename) + "\n";  // 取得根目錄

                richTextBox1.Text += "修改成完整時間檔名 : " + Path.GetDirectoryName(filename) + "\\" + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "修改成時間檔名 : " + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
            }

            richTextBox1.Text += "取得隨機檔名 : " + Path.GetRandomFileName() + "\n";
            richTextBox1.Text += "取得臨時檔名 : " + Path.GetTempFileName() + "\n";
            richTextBox1.Text += "取得臨時路徑 : " + Path.GetTempPath() + "\n";

            //------------------------------------------------------------  # 60個

            /*
            //附隨檔案的寫法
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\AAAAA.BBBBB";
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";
            string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";
            richTextBox1.Text += filename + "\n\n";
            */

            //------------------------------------------------------------  # 60個

            //檔案資訊
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //檔案資訊
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";

            FileInfo fileInfo = new FileInfo(filename);
            string fileSize = (fileInfo.Length / 1024).ToString() + " KB";
            string temp = filename.Remove(filename.LastIndexOf('.'));

            richTextBox1.Text += "filename = " + filename + "\n";
            richTextBox1.Text += "fileSize = " + fileSize + "\n";
            richTextBox1.Text += "temp = " + temp + "\n";

            //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void bt_file09_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir00_Click(object sender, EventArgs e)
        {
            //Directory 的方法
            /*            
            Directory.Exists()
            Directory.CreateDirectory()
            Directory.Move()
            Directory.Delete()
            Directory.GetDirectories()  // 由資料夾取出資料夾名稱串列
            Directory.GetFiles()  // 由資料夾取出檔案名稱串列
            Directory.GetCurrentDirectory()  // 目前所在路徑, 目前的工作目錄
            Directory.SetCurrentDirectory()  // 設定工作目錄
            Directory.GetLastWriteTime()
            Directory.SetLastWriteTime()
            */

            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();  // 目前的工作目錄
            richTextBox1.Text += "目前所在路徑 : " + currentPath + "\n";

            //Directory.SetCurrentDirectory("D:\\");  // 設定工作目錄

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

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\";

            if (Directory.Exists(foldername) == false)
            {
                richTextBox1.Text += "路徑不存在, 建立之。\n";
                Directory.CreateDirectory(foldername);
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
            Directory.Move(Path_old, Path_new);  // 資料夾改名
            richTextBox1.Text += "移動/更名 完成，從原始資料夾: " + Path_old + " 到目的資料夾: " + Path_new + "\n";

            //移動資料夾，從 sourceDirName 移動到 destDirName
            string sourceDirName = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName = @"D:\_git\vcs\_1.data\______test_files1\folder22";
            if (Directory.Exists(sourceDirName))        //確認資料夾是否存在
            {
                if (!Directory.Exists(destDirName))     //確認資料夾是否存在
                {
                    Directory.Move(sourceDirName, destDirName);  // 資料夾改名
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

        }

        private void bt_dir01_Click(object sender, EventArgs e)
        {
            //DirectoryInfo 的方法

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            DirectoryInfo dinfo11 = new DirectoryInfo(foldername);
            if (!dinfo11.Exists)  //判斷資料夾路徑是否不存在
            {
                richTextBox1.Text += "路徑不存在\n";
                return;
            }
            richTextBox1.Text += dinfo11.FullName + "資料夾下的檔案資訊如下：\n";

            FileInfo[] fis = dinfo11.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo fi in fis)
            {
                richTextBox1.Text += "完整路徑：" + fi.FullName + "\n";
                richTextBox1.Text += "寫入時間：" + fi.LastWriteTime + "\n";
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + "\n";
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "==================================\n";

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            DirectoryInfo dinfo1 = new DirectoryInfo(foldername);
            if (dinfo1.Exists)        //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾\n";
                DirectoryInfo[] dis = dinfo1.GetDirectories();  // 由DI取得DI陣列, 單層資料夾資訊
                foreach (DirectoryInfo di in dis)
                {
                    //資料夾資訊
                    richTextBox1.Text += "資料夾名稱：" + di.FullName + "\n";
                    richTextBox1.Text += "屬性：" + di.Attributes + "\n";
                    richTextBox1.Text += "存在與否：" + di.Exists + "\n";
                    richTextBox1.Text += "資料夾名稱：" + di.Extension + "\n";
                    richTextBox1.Text += "資料夾全名：" + di.FullName + "\n";
                    richTextBox1.Text += "資料夾簡名：" + di.Name + "\n";
                    richTextBox1.Text += "資料夾名稱：" + di.Parent + "\n";
                    richTextBox1.Text += "根資料夾：" + di.Root + "\n";
                    richTextBox1.Text += "資料夾內資料夾數目：" + di.GetDirectories().Length + "\n";
                    richTextBox1.Text += "資料夾內檔案數目：" + di.GetFiles().Length + "\n";
                    richTextBox1.Text += "  資料夾數目：" + di.GetDirectories().Length + "\n";
                    richTextBox1.Text += "  檔案數目：" + di.GetFiles().Length + "\n";

                    if (di.GetDirectories().Length > 0)
                    {
                        richTextBox1.Text += "下一層資料夾：";
                        foreach (DirectoryInfo ddi in di.GetDirectories())
                        {
                            richTextBox1.Text += ddi.Name + "\n";
                        }
                    }
                    else
                        richTextBox1.Text += "\n";
                }

                //  檢查每個檔案的資訊
                richTextBox1.Text += "檔案\n";
                fis = dinfo1.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
                foreach (FileInfo fi in fis)
                {
                    richTextBox1.Text += "全檔名：" + fi.FullName + "\n";
                    richTextBox1.Text += "  檔名：" + fi.Name + "\n";
                    richTextBox1.Text += "  副檔名：" + fi.Extension + "\n";
                    richTextBox1.Text += "  大小：";
                    if (fi.Length > (1024 * 1024))
                    {
                        richTextBox1.Text += (fi.Length / 1024 / 1024).ToString() + " MB( " + fi.Length + " 位元組)\n";
                    }
                    else if (fi.Length > (1024))
                    {
                        richTextBox1.Text += (fi.Length / 1024).ToString() + " KB( " + fi.Length + " 位元組)\n";
                    }
                    else
                    {
                        richTextBox1.Text += fi.Length + " 位元組\n";
                    }
                    richTextBox1.Text += "  建立日期：" + fi.CreationTime + "\n";
                    richTextBox1.Text += "  日期：" + fi.CreationTimeUtc + "\n";
                    richTextBox1.Text += "  存取日期：" + fi.LastAccessTime + "\n";
                    richTextBox1.Text += "  日期：" + fi.LastAccessTimeUtc + "\n";
                    richTextBox1.Text += "  修改日期：" + fi.LastWriteTime + "\n";
                    richTextBox1.Text += "  日期：" + fi.LastWriteTimeUtc + "\n";
                    richTextBox1.Text += "  屬性：" + fi.Attributes + "\n";
                    richTextBox1.Text += "  資料夾：" + fi.Directory + "\n";
                    richTextBox1.Text += "  資料夾名：" + fi.DirectoryName + "\n";
                    richTextBox1.Text += "  唯讀：" + fi.IsReadOnly + "\n";
                }
            }
            else
            {
                MessageBox.Show("No Exist");
            }

            //------------------------------------------------------------  # 60個

            //使用递归法删除文件夹中的所有文件
            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            int file_no = 0;
            DirectoryInfo dinfo2 = new DirectoryInfo(foldername);//创建DirectoryInfo对象
            FileSystemInfo[] fsinfos = dinfo2.GetFileSystemInfos();  // 獲取所有的文件
            for (int i = 0; i < fsinfos.Length; i++)//遍歷獲取到的文件
            {
                FileInfo fi = new FileInfo(foldername + "\\" + fsinfos[i].ToString());//创建FileInfo对象
                //fi.Delete();//删除文件
                richTextBox1.Text += "偽刪除 " + foldername + "\\" + fsinfos[i].ToString() + "\n";
                file_no++;
            }
            richTextBox1.Text += "删除成功, 共刪除 " + file_no.ToString() + " 個檔案\n";

            //------------------------------------------------------------  # 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            string fnShow = "檔案清單---<*.TXT>";
            try
            {
                //取得檔案路徑訊息
                DirectoryInfo dinfo10 = new DirectoryInfo(foldername);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = dinfo10.GetFiles("*.txt");
                //設定檔案的標題
                //string header = fnShow + "\n" + $"{"檔名",-16}{"檔案長度",-12}{"修改日期"}" + "\n";
                string header = fnShow + "\n檔名\t檔案長度\t修改日期\n";
                richTextBox1.Text += header;

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

            //------------------------------------------------------------  # 60個

            string foldername_new = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd\aaaaaa";

            //DirectoryInfo 測試

            // 建立DirectoryInfo類別的dinfo3物件，可用來操作資料夾目錄
            DirectoryInfo dinfo3 = new DirectoryInfo(foldername_new);
            if (dinfo3.Exists)
            {	// 判斷目錄是否存在
                richTextBox1.Text += foldername_new + ", 路徑存在, 不建立目錄\n";
            }
            else
            {
                richTextBox1.Text += foldername_new + ", 路徑不存在，建立目錄\n";
                dinfo3.Create();	// 建立目錄
                dinfo3.Refresh();	// 重新整理目錄
            }
            richTextBox1.Text += dinfo3.FullName + " 檔案資訊如下 :\n";
            richTextBox1.Text += "建立時間 : " + dinfo3.CreationTime + "\n";
            richTextBox1.Text += "存取時間 : " + dinfo3.LastAccessTime + "\n";
            richTextBox1.Text += "資料夾名稱 : " + dinfo3.Name + "\n";
            richTextBox1.Text += "根目錄 : " + dinfo3.Parent + "\n";

            //刪除 資料夾
            try
            {
                dinfo3.Delete();	       // 刪除檔案
                richTextBox1.Text += "刪除成功" + "\n";
            }
            catch (Exception ex)   // 刪除檔案失敗會產生例外
            {
                richTextBox1.Text += "刪除失敗" + "\n";
                richTextBox1.Text += ex.Message + "\n";  // 顯示例外訊息
            }
            richTextBox1.Text += "------------------------------\n";  // 30個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            DirectoryInfo dinfo4 = new DirectoryInfo(foldername);
            if (!dinfo4.Exists)	//判斷路徑是否不存在
            {
                richTextBox1.Text += "路徑不存在" + "\n";
                return;
            }
            richTextBox1.Text += dinfo4.FullName + ", 資料夾下的子資料夾如下 :\n";
            DirectoryInfo[] subdir = dinfo4.GetDirectories();  // 由DI取得DI陣列, 單層資料夾資訊
            foreach (DirectoryInfo di in subdir)
            {
                richTextBox1.Text += "完整路徑 : " + di.FullName + "\t建立時間 : " + di.CreationTime + "\n";
            }

            //------------------------------------------------------------  # 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            List<FileInfo> myFiles = new List<FileInfo>();//创建List泛型对象

            // 由資料夾取出檔案名稱串列
            string[] filenames = Directory.GetFiles(foldername);  // 由資料夾取出檔案名稱串列
            foreach (string filename in filenames)//遍历选择文件夹中的所有文件
            {
                myFiles.Add(new FileInfo(filename));//将遍历的所有文件添加到List对象中
            }
            var values = from filename in myFiles//使用LINQ从List对象中查找文件
                         group filename by filename.Extension into FExten
                         orderby FExten.Key
                         select FExten;
            foreach (var vFiles in values)
            {
                foreach (var file in vFiles)
                {
                    richTextBox1.Text += file.FullName + "\n";
                }
            }
        }

        private void bt_dir02_Click(object sender, EventArgs e)
        {
            //Directory.GetFiles()  // 由資料夾取出檔案名稱串列

            string dir1 = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            string[] filenames = Directory.GetFiles(dir1);  // 由資料夾取出檔案名稱串列
            for (int i = 0; i < filenames.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + filenames[i] + "\n";
                filenames[i] = filenames[i].Replace(dir1, "");
                richTextBox1.Text += "i = " + i.ToString() + "\t" + filenames[i] + "\n";
            }
            Array.Sort(filenames);

            List<string> name_list = new List<string>();
            for (int i = 0; i < filenames.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + filenames[i] + "\n";
                name_list.Add(filenames[i]);
            }

            DirectoryInfo dinfo5 = new DirectoryInfo(dir1);
            FileInfo[] fis = dinfo5.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊

            int len = fis.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += fis[i].Name + "\n";
            }

            //------------------------------------------------------------  # 60個

            //取得資料夾下的所有檔案(包括子目錄)

            string foldername = String.Empty;
            string filetype = String.Empty;
            filetype = "*.*";

            //foldername = @"D:\_DATA2\_VIDEO_全為備份\百家??_清十二帝疑案";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            //C# 取得資料夾下的所有檔案(包括子目錄)
            //string[]
            filenames = Directory.GetFiles(foldername, filetype, System.IO.SearchOption.AllDirectories);  // 由資料夾取出檔案名稱串列
            foreach (string filename in filenames)
            {
                richTextBox1.Text += "原撈到的檔案 : " + filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出一層jpg檔
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";
            //string[]
            filenames = Directory.GetFiles(foldername, "*.jpg");  // 由資料夾取出檔案名稱串列

            foreach (string filename in filenames)
            {
                richTextBox1.Text += "取得檔案 : " + filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\__text";

            //string[]
            filenames = Directory.GetFiles(foldername);  // 由資料夾取出檔案名稱串列
            foreach (String filename in filenames)
            {
                richTextBox1.Text += "找到檔案\t" + filename + "\n";
            }

            string[] dirs = Directory.GetDirectories(foldername);  // 由資料夾取出資料夾名稱串列
            foreach (String dir in dirs)
            {
                richTextBox1.Text += "找到資料夾\t" + dir + "\n";
            }

            //------------------------------------------------------------  # 60個






            //------------------------------------------------------------  # 60個



            //------------------------------------------------------------  # 60個


            /*
              // 由資料夾取出檔案名稱串列
            string[] filenames = Directory.GetFiles(@"D:\項目\Web\Images\shiji"); //獲得文件夾目錄下所有文件全路徑
            string[] filenames = Directory.GetFiles(@"D:\項目\Web\Images\shiji", "*.jpg"); //獲得文件夾目錄下指定後綴名文件全路徑

            */
        }

        private void bt_dir03_Click(object sender, EventArgs e)
        {
            string destDirName = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName2 = @"D:\_git\vcs\_1.data\______test_files1\folder22";
            DeleteDirectory(destDirName, true);
            DeleteDirectory(destDirName2, true);
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir04_Click(object sender, EventArgs e)
        {
            //DirectoryInfo的方法2

            //DirectoryInfo

            //儲存要回傳的檔案路徑和檔案類型
            string path2 = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook";
            string fnShow = "檔案清單---<*.jpg>\n\n";

            //判斷資料夾是否存在，若是不存在會擲出例外情形
            try
            {    //取得檔案路徑訊息
                DirectoryInfo currentDir = new DirectoryInfo(path2);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = currentDir.GetFiles("*.jpg");
                //設定檔案的標題
                string sign = new string('-', 37);
                string fnName = "檔名", fnLength = "檔案長度";
                string fnDate = "修改日期";
                string header = fnShow + "\t" + fnName + "\t" + fnLength + "\t" + fnDate + "\n";
                richTextBox1.Text += header + "\n";
                richTextBox1.Text += sign + "\n";

                foreach (FileInfo getInfo in listFile)
                {
                    string dt = getInfo.LastWriteTime.ToShortDateString();
                    richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + dt + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無此資料夾 : " + ex.Message + "\n";
            }

            //------------------------------------------------------------  # 60個
            //DirectoryInfo
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1\";

            DirectoryInfo temp3 = new DirectoryInfo(foldername);

            DirectoryInfo[] idr = temp3.GetDirectories();//獲取當前目錄下的所有子目錄.
            foreach (DirectoryInfo dir in idr)
            {
                richTextBox1.Text += "取得資料夾 : " + dir.FullName + "\n";

                FileInfo[] files1 = dir.GetFiles();

                foreach (FileInfo file in files1)
                {
                    richTextBox1.Text += "取得檔案 : " + file.FullName + "\n";
                }
            }

            richTextBox1.Text += "目錄 : " + foldername + " 下\n";
            FileInfo[] files2 = temp3.GetFiles();

            foreach (FileInfo file in files2)
            {
                richTextBox1.Text += "取得檔案 : " + file.FullName + "\n";
            }

            //------------------------------------------------------------  # 60個

            //Path.Combine()

            /*
            string filename = Path.Combine(Application.StartupPath, @"..\..\Form1.cs");

            richTextBox1.Text += "filename old = " + filename + "\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU";
            var dinfo12 = new DirectoryInfo(foldername);
            var filenames = dinfo12.GetFiles().OrderBy(p => p.Name).ToArray();
            foreach (var file in filenames)
            {
                if (file.FullName.Contains("id_card") == true)
                {
                    Console.WriteLine(file.FullName);

                }
            }
            */

            //------------------------------------------------------------  # 60個

            //取得磁碟檔案資料
            // 由檔案取得檔案所在磁碟
            DriveInfo di = new DriveInfo(@"D:\_git\vcs\_1.data\______test_files1");
            richTextBox1.Text += "由檔案取得檔案所在磁碟 : " + di.RootDirectory + "\n";

            // Get the root directory and print out some information about it.
            DirectoryInfo dinfo9 = di.RootDirectory;
            richTextBox1.Text += "根目錄 : " + dinfo9.Attributes.ToString() + "\n";

            // Get the files in the directory and print out some information about them.
            FileInfo[] fis = dinfo9.GetFiles("*.*");

            foreach (FileInfo fi in fis)
            {
                richTextBox1.Text += "檔案 : " + fi.Name + "   " + fi.LastAccessTime + "   " + fi.Length + "\n";
            }

            // Get the subdirectories directly that is under the root.
            // See "How to: Iterate Through a Directory Tree" for an example of how to
            // iterate through an entire tree.
            DirectoryInfo[] dirInfos = dinfo9.GetDirectories("*.*");  // 由DI取得DI陣列, 單層資料夾資訊

            foreach (DirectoryInfo dinfo7 in dirInfos)
            {
                richTextBox1.Text += "資料夾 : " + "   " + dinfo7.Name + "\n";
            }
            richTextBox1.Text += message;

            //------------------------------------------------------------  # 60個

            //遍歷文件夾實例 1

            //還沒加入listView之標題

            listView1.Items.Clear();

            //foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";
            //實例化DirectoryInfo對象
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            //獲取指定目錄下的所有子目錄及文件類型
            FileSystemInfo[] fsinfos = dinfo.GetFileSystemInfos();  // 獲取所有的文件
            foreach (FileSystemInfo fsinfo in fsinfos)  // 遍歷獲取到的文件
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

            //------------------------------------------------------------  # 60個

            //遍歷文件夾實例 2
            //foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";
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

            //------------------------------------------------------------  # 60個

            //遍歷文件夾實例 3

            //找出資料夾內所有檔案
            //foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

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
                    MessageBox.Show("Error processing file '" + file_info.Name + "'\n" + ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            } // foreach file_info



        }

        //------------------------------------------------------------  # 60個

        private void bt_dir05_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir06_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir07_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir08_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

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
            DirectoryInfo dinfo6 = new DirectoryInfo(@"D:\_git\vcs\_1.data\______test_files1");//輸入檔案夾
            double size = DirSize(dinfo6);
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

            GetAllFileNames(dinfo6);
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
            string[] filenames = Directory.GetFiles(target_dir);  // 由資料夾取出檔案名稱串列
            string[] dirs = Directory.GetDirectories(target_dir);  // 由資料夾取出資料夾名稱串列
            richTextBox1.Text += "檔案個數 = " + filenames.Length.ToString() + "\n";
            richTextBox1.Text += "資料夾: " + target_dir + "\n";
            foreach (string file in filenames)
            {
                richTextBox1.Text += "檔案: " + file + "\t";
                //richTextBox1.Text += "Size: " + file.Length.ToString() + " 拜\n"; wrong
                File.SetAttributes(file, FileAttributes.Normal);
                richTextBox1.Text += file + "\t";
                richTextBox1.Text += file.Length.ToString() + "\n";
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

        //------------------------------------------------------------  # 60個

        private void bt_files04_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files05_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files06_Click(object sender, EventArgs e)
        {
            //讀取資料夾下所有資料夾
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            //讀取資料夾下所有資料夾
            GetDirectories(foldername);

            //讀取資料夾下所有檔案
            GetFiles(foldername);

            //------------------------------------------------------------  # 60個

            //搜尋檔案
            richTextBox1.Text += "尋找檔案 IMG_20180228_215525.jpg\n";
            DirectoryInfo dinfo8 = new DirectoryInfo(@"D:\_git\vcs\_1.data\______test_files1");
            foreach (FileInfo info in dinfo8.GetFiles("IMG_20180228_215525.jpg"))
            {
                MessageBox.Show("有找到");
            }
        }

        //------------------------------------------------------------  # 60個

        //讀取資料夾下所有資料夾
        private ArrayList GetDirectories(string foldername)
        {
            ArrayList directories = new ArrayList();

            if (Directory.Exists(foldername))     //確認資料夾是否存在
            {
                string[] dirs = Directory.GetDirectories(foldername);  // 由資料夾取出資料夾名稱串列
                directories.AddRange(dirs);
                richTextBox1.Text += "總共" + directories.Count.ToString() + "個資料夾\n";
            }
            return directories;
        }

        //讀取資料夾下所有檔案, 只看一層
        private ArrayList GetFiles(string foldername)
        {
            ArrayList files = new ArrayList();

            if (Directory.Exists(foldername))     //確認資料夾是否存在
            {
                string[] filenames = Directory.GetFiles(foldername);  // 由資料夾取出檔案名稱串列
                files.AddRange(filenames);
                richTextBox1.Text += "總共" + files.Count.ToString() + "個檔案\n";
            }
            return files;
        }

        //------------------------------------------------------------  # 60個

        private void bt_files07_Click(object sender, EventArgs e)
        {
            //撈出資料夾內所有jpg檔
            var dirs = Directory.GetDirectories(@"D:\_git\vcs\_1.data\______test_files1");  // 由資料夾取出資料夾名稱串列
            try
            {
                foreach (var dir in dirs)
                {
                    richTextBox1.Text += "aaaa3 dir = " + dir + "\n";
                    var fnames = Directory.GetFiles(dir, "*.jpg").Select(Path.GetFileName);

                    DirectoryInfo dinfo7 = new DirectoryInfo(dir);
                    FileInfo[] fis = dinfo7.GetFiles("*.jpg");
                    foreach (var filename in fnames)
                    {
                        richTextBox1.Text += filename + "\n";

                        if (!File.Exists(Path.Combine(dir, filename.ToString().Replace("(", "").Replace(")", ""))))
                        {
                            // 檔案重新命名
                            File.Move(Path.Combine(dir, filename), Path.Combine(dir, filename.ToString().Replace("(", "").Replace(")", "")));
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
            richTextBox1.Text += "dirs : " + dirs + "\n";
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
            List<string> filenames = new List<string>();

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
                    if (!filenames.Contains(filename))
                    {
                        filenames.Add(filename);
                    }
                }
            }
            // Sort.
            filenames.Sort();

            // Return the result.
            return filenames;
        }

        //------------------------------------------------------------  # 60個

        private void bt_files09_Click(object sender, EventArgs e)
        {
            //GetDirectories
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1\";
            richTextBox1.Text += "讀出一資料夾內所有檔案 -r, 資料夾\t" + foldername + "\n";

            get_all_files(foldername);
        }

        int total_number_files = 0;
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
                }
            }

            richTextBox1.Text += "目錄 : " + foldername + " 下\n";
            FileInfo[] files2 = temp3.GetFiles();

            foreach (FileInfo file in files2)
            {
                richTextBox1.Text += "取得檔案 : " + file.FullName + "\n";
                total_number_files++;
            }
            richTextBox1.Text += "共取得檔案 " + total_number_files.ToString() + " 個\n";
        }


        //------------------------------------------------------------  # 60個

        private void bt_files10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "CurrentDir1 : " + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "CurrentDir2 : " + new DirectoryInfo(Environment.CurrentDirectory).Parent + "\n";
            richTextBox1.Text += "CurrentDir3 : " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent + "\n";
            richTextBox1.Text += "CurrentDir4 : " + new DirectoryInfo(Environment.CurrentDirectory).Parent.Parent.FullName + "\n";

            //------------------------------------------------------------  # 60個

            //檔案已存在的FileCopy/Move

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

            //------------------------------------------------------------  # 60個

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

            //------------------------------------------------------------  # 60個

            //刪除資料夾下子資料夾(偽)

            string pathstr = @"D:/_git/vcs/_1.data/______test_files1";
            if (Directory.Exists(pathstr))
            {
                DateTime dt = DateTime.Now;
                DirectoryInfo pathinfo = new DirectoryInfo(pathstr);
                foreach (DirectoryInfo paths in pathinfo.GetDirectories())
                {
                    if (paths.CreationTime < Convert.ToDateTime(dt.AddDays(-(dt.Day) + 1)))
                    {
                        //paths.Delete();
                        richTextBox1.Text += "path = " + paths + "\n";
                    }
                }
            }
            else
            {
                richTextBox1.Text += "資料夾 " + pathstr + " 不存在\n";
            }

            //------------------------------------------------------------  # 60個




        }

        //------------------------------------------------------------  # 60個

        private void bt_files11_Click(object sender, EventArgs e)
        {
        }

        private void bt_files12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files13_Click(object sender, EventArgs e)
        {
            //取得資料夾下所有圖片檔資訊

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";

            IEnumerable<FileInfo> images = null;
            if (Directory.Exists(foldername) == true)
            {
                DirectoryInfo dirInfo = new DirectoryInfo(foldername);
                images = dirInfo.EnumerateFiles("*.jpg").OrderBy(i => i.Name[0]).ThenBy(i => i.Name.Length).ThenBy(i => i.Name);

                int len = images.Count();
                richTextBox1.Text += "len = " + len.ToString() + "\n";

                if (images != null && images.Count() > 0)
                {

                }

                foreach (var image in images)
                {
                    richTextBox1.Text += image.Name + "\n";
                    richTextBox1.Text += image.FullName + "\n";
                    richTextBox1.Text += image.Extension + "\n";
                    richTextBox1.Text += image.Length.ToString() + "\n";
                }
            }
        }

        private void bt_files14_Click(object sender, EventArgs e)
        {
            //取得上一層資料夾的名稱

            richTextBox1.Text += "原目錄 : " + Application.StartupPath + "\n";

            string str = Application.StartupPath;
            string[] split_str = new string[20];
            split_str = str.Split('\\'); //以\當分隔符號
            //richTextBox1.Text += "\n";
            //richTextBox1.Text += "共有 : " + split_str.Length.ToString() + " 個項目\n";

            richTextBox1.Text += "上一層資料夾的名稱 : " + split_str[split_str.Length - 1] + "\n";

            /*
            int i = 0;
            foreach (string tmp in split_str)
            {
                i++;
                richTextBox1.Text += i.ToString() + "\t" + tmp + "\n";
            }
            */
        }

        private void bt_files15_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void bt_files16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files17_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files18_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

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
        private void button2_Click(object sender, EventArgs e)
        {
            //新增檔案
            //指定路徑建立檔案
            string filename = @"_tmp_aaaa.txt";
            FileInfo createFile = new FileInfo(filename);
            //以Create方法新增一個檔案
            FileStream fs = createFile.Create();
            fs.Close();//關閉檔案
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"_tmp_bbbb.txt";
            string str;
            FileStream fs = new FileStream(filename, FileMode.OpenOrCreate, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.Unicode);

            //想儲存的文字
            str = "aaaaaaaaa";
            sw.WriteLine(str);  //將資料寫入檔案
            sw.Close();   //關閉sw資料流

            //檔案內所輸入的文字為
            FileStream fs = new FileStream(filename, FileMode.OpenOrCreate, FileAccess.Read);
            StreamReader sr = new StreamReader(fs, Encoding.Unicode);
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
                string foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\";
                //取得資料夾最後一次被存取的時間
                DateTime dt = Directory.GetLastWriteTime(foldername);
                //如果資料夾不存在就建立資料夾
                if (!Directory.Exists(foldername))
                {
                    Directory.CreateDirectory(foldername);
                }
                else
                {
                    richTextBox1.Text += "資料夾建立的時間 : " + dt + "\n";
                }
                //更新時間
                Directory.SetLastWriteTime(foldername, DateTime.Now);
                dt = Directory.GetLastWriteTime(foldername);
                richTextBox1.Text += "最後存取時間 : " + dt + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "無法建立 : " + e.ToString() + "\n";
            }
        }

//------------------------------------------------------------  # 60個

            string input, sel;
            StreamReader sr;
            StreamWriter sw;
            FileInfo fi;
            string filename = "tmp_aaaa.txt";

            fi = new FileInfo(filename);

            Console.Write("請選擇功能->1.寫入  2.附加   其他.離開：");

            sel = "1";
            if (sel == "1")
            {
                sw = fi.CreateText();  //開啟新檔
                input = "寫入AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
                //將輸入的資料覆蓋原檔並重新寫入
                sw.WriteLine(input);
                sw.Flush();
                sw.Close();

            }
            else if (sel == "2")
            {
                sw = fi.AppendText();   //開啟舊檔
                input = "附加AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
                //將輸入的資料附加到資料檔的最後
                sw.WriteLine(input);
                sw.Flush();
                sw.Close();
            }

            sr = fi.OpenText();  //以唯讀模式開檔
            Console.WriteLine("資料檔內容如下：");
            Console.WriteLine(sr.ReadToEnd());//讀出資料
            sr.Close();
            Console.WriteLine("================================");

//------------------------------------------------------------  # 60個

textBox1.Text = File.ReadAllText(@"D:\鹿柴.txt");

File.WriteAllText(@"setting.txt", folderPath);

//------------------------------------------------------------  # 60個

在 C# 中使用 File.ReadAllText() 方法將檔案讀取為字串
string text = File.ReadAllText(@"D:\File\file.txt");
Console.WriteLine(text);

在 C# 中使用 StreamReader.ReadToEnd() 方法將檔案讀取為字串
StreamReader fileReader = new StreamReader(@"D:\File\file.txt");
string text = fileReader.ReadToEnd();
Console.WriteLine(text);			

//------------------------------------------------------------  # 60個

            string filename = @"D:\______test_files\_case1\pic1.jpg";
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

待測
//File.AppendAllText("E:\\Time\\新建文檔夾 (2)" + "/" + strname, DateTime.Now+"\n");

//------------------------------------------------------------  # 60個

根據時間建立文件
File.Create("D:\\______test_files\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//建立文件

建立臨時檔案
File.Create("tmp_" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件

//------------------------------------------------------------  # 60個

            //刪除檔案
            filename = @"_tmp_aaaa.txt";
            FileInfo fi = new FileInfo(filename);
            if (fi.Exists == false)//查看檔案是否存在
            {
                MessageBox.Show("無此檔案");
            }
            else
            {
                fi.Delete();//刪除檔案
            }

            //複製檔案
            filename = @"_tmp_aaaa.txt";
            //目的檔案「Text.txttmp」
            String tagPath = filename + "tmp";
            FileInfo fi = new FileInfo(filename);
            try
            {
                //以CopyTo方法複製檔案
                fi.CopyTo(tagPath);
                richTextBox1.Text += filename + " 已複製";
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
*/

/*
                        string[] fileEntries = Directory.GetFiles(path);
                        Array.Sort(fileEntries);
                        foreach (string fileName in fileEntries)
                        {
                        }
*/

/*
//取得目前所在路徑
string currentPath = Directory.GetCurrentDirectory();
richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";

//確認資料夾是否存在
string Path = @"D:/_git/vcs/_1.data/______test_files1/aaaa/bbbb";
if (Directory.Exists(Path) == false)    //確認資料夾是否存在
    richTextBox1.Text += "搜尋資料夾: " + Path + " 不存在\n";
else
    richTextBox1.Text += "搜尋資料夾: " + Path + " 存在\n";
*/

//------------------------------------------------------------  # 60個

/*
	            if(!Directory.Exists(dirPath))  
	            {  
	                Directory.CreateDirectory(dirPath);  
	            }  

		String retval = "";
		
		// Delete all the files
		String[] filenames = Directory.GetFiles(pPath);
		foreach (String filename in filenames)
			File.Delete(filename);
		// Delete the directory
		Directory.Delete(pPath, true);
		return retval;

//------------------------------------------------------------  # 60個

            if (path == String.Empty)
                path = @"D:\_git\vcs\_1.data\______test_files1";

            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(path, filetype2, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                //richTextBox1.Text += filename + "\n";
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += fi.Name + "\n";
            }

//------------------------------------------------------------  # 60個

        public static void Rename(this FileInfo fileInfo, string newName)
        {
            fileInfo.MoveTo(fileInfo.Directory.FullName + "\\" + newName);
        }

FileInfo file = new FileInfo("c:\test.txt");
file.Rename("test2.txt");

//------------------------------------------------------------  # 60個


                        FileAttributes attr = (new FileInfo(filePath)).Attributes;
                        Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                        if ((attr & FileAttributes.ReadOnly) > 0)
                            Console.Write("The file is read-only.");

//------------------------------------------------------------  # 60個

//一般文件名按顺序排
string[] pngfiles = Directory.GetFileSystemEntries(directory, "*.png");

for (int i = 0, count = pngfiles.Length; i < count; i++)
{
    e.AddFrame(Image.FromFile(pngfiles[i]));
}

//------------------------------------------------------------  # 60個


*/

