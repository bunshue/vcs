using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for Directory, StreamReader, SearchOption
using System.Collections;  // for ArrayList
using System.Diagnostics;  // for Stopwatch
using System.Runtime.InteropServices;   //for DllImport, Marshal, StructLayout
using Microsoft.VisualBasic.FileIO;  // for 刪除檔案(使用資源回收筒)

namespace vcs_DiskDirectoryFile1
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string foldername = @"D:\_git\vcs\_1.data\______test_files1\";

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
            bt_files20.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_files21.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            bt_files22.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            bt_files23.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            bt_files24.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            bt_files25.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            bt_files26.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            bt_files27.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            bt_files28.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            bt_files29.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            listView1.Size = new Size(400, 340);
            listView1.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            listBox1.Size = new Size(400, 340);
            listBox1.Location = new Point(x_st + dx * 5, y_st + dy * 5);

            richTextBox1.Size = new Size(300, 690);
            richTextBox1.Location = new Point(x_st + dx * 7, y_st + 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1810, 750 + 20);
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

        public void DeleteDirectory(string foldername)
        {
            string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "刪除子目錄 : " + dir + "\n";
                DeleteDirectory(dir);
            }

            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            foreach (string filename in filenames)
            {
                richTextBox1.Text += "刪除檔案 : " + filename + "\n";
                File.SetAttributes(filename, FileAttributes.Normal);
                File.Delete(filename);  // 刪除檔案
            }

            Directory.Delete(foldername, false);
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
                    file1byte = fs1.ReadByte();  // 讀一拜
                    file2byte = fs2.ReadByte();  // 讀一拜
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
            if (recursive)
            {
                Directory.Delete(foldername, true);
                richTextBox1.Text += "已刪除資料夾: " + foldername + "\n";
            }
            else
            {
                richTextBox1.Text += "需要先把資料夾內的檔案刪除\n";
            }
        }

        public static double DirSize(DirectoryInfo dinfo)
        {
            double Size = 0;

            // Add file sizes.
            FileInfo[] fis = dinfo.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo finfo in fis)
            {
                Size += finfo.Length;
            }

            // Add subdirectory sizes.
            DirectoryInfo[] dinfos = dinfo.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dinfos)
            {
                if (di.Name != "System Volume Information" && di.Name.Substring(0, 1) != "$")//避開此類folder權限問題
                {
                    Size += DirSize(di);   //利用遞迴把子資料夾也計算進來
                }
            }
            return (Size);
        }

        string message = "";
        double filesize_all = 0;

        public void GetAllFileNames(DirectoryInfo dinfo)
        {
            // Add file sizes.
            FileInfo[] fis = dinfo.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo finfo in fis)
            {
                message += finfo.Name;
                message += "\t";
                message += finfo.Length.ToString(); ;
                message += "\n";
                filesize_all += finfo.Length;
            }
            // Add subdirectory sizes.
            DirectoryInfo[] dinfos = dinfo.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dinfos)
            {
                if (di.Name != "System Volume Information" && di.Name.Substring(0, 1) != "$")//避開此類folder權限問題
                {
                    GetAllFileNames(di);   //利用遞迴把子資料夾也加進來
                }
            }
            message += "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_file00_Click(object sender, EventArgs e)
        {
            /*
            //File 的方法
            File.Exists()
            File.Create()
            File.Copy()  // 檔案拷貝
            File.Move()  // 檔案重新命名
            File.Delete()  // 刪除檔案
            File.Open()
            File.OpenRead()
            File.ReadAllText()  // 將檔案讀取為字串
            File.WriteAllText()
            File.AppendAllText()
            //取得檔案時間
            File.GetCreationTime()	檔案建立時間
            File.GetLastWriteTime()	檔案最後修改時間
            File.GetLastAccessTime()檔案最後存取時間
            //設定檔案時間
            File.SetCreationTime()
            File.SetLastWriteTime()
            File.SetLastAccessTime()

            File.GetAttributes()  取得檔案屬性
            File.SetAttributes()  設定檔案屬性
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

            //------------------------------------------------------------  # 60個

            //檔案已存在的FileCopy/Move

            string filename_source = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
            string filename_destination = @"D:\_git\vcs\_1.data\______test_files1\_cpfile\ccc.jpg";   //要寫完整檔名

            richTextBox1.Text += "檔案已存在的FileCopy/Move\n";
            try
            {
                //File.Copy(filename_source, filename_destination);  // 檔案拷貝     //若檔案已存在, 會出現IOException
                //File.Move(filename_source, filename_destination);  // 檔案重新命名     //若檔案已存在, 會出現IOException
                File.Copy(filename_source, filename_destination, true); //檔案拷貝, true : 覆蓋檔案
                //File.Move(filename_source, filename_destination, true);  // 檔案重新命名 //true : 覆蓋檔案
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_file01_Click(object sender, EventArgs e)
        {
            //FileInfo 的方法

            //取得檔案資訊 FileInfo

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            FileInfo finfo = new FileInfo(filename);

            if (finfo.Exists == false)      //確認檔案是否存在
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
            }
            else
            {
                richTextBox1.Text += "資料夾：" + finfo.Directory + "\n";
                //由短檔案名取的短資料夾名
                richTextBox1.Text += "資料夾：" + finfo.Directory + "\n";
                richTextBox1.Text += "資料夾：" + finfo.Directory.Parent + "\n";

                richTextBox1.Text += "檔名：" + finfo.Name + "\n";
                richTextBox1.Text += "檔案大小：" + finfo.Length.ToString() + "\n";
                richTextBox1.Text += "建立時間1：" + finfo.CreationTime.ToString() + "\n";
                richTextBox1.Text += "建立時間2：" + finfo.CreationTimeUtc.ToString() + "\n";
                richTextBox1.Text += "最近寫入時間：" + finfo.LastWriteTime.ToString() + "\n";
                richTextBox1.Text += "FullName :" + finfo.FullName + "\n";
                richTextBox1.Text += "Directory :" + finfo.Directory + "\n";
                richTextBox1.Text += "DirectoryName :" + finfo.DirectoryName + "\n";
                richTextBox1.Text += "Extension :" + finfo.Extension + "\n";  // 取得副檔名
                richTextBox1.Text += "Length :" + finfo.Length.ToString() + "\n";
                //C# 取得檔案建立日期,及最後修改日期 
                richTextBox1.Text += "檔案建立日期" + finfo.CreationTime.ToString() + "\n";
                richTextBox1.Text += "檔案最後修改日期" + finfo.LastWriteTime.ToString() + "\n";
                //C# 取得檔案路徑、副檔名、檔案大小
                richTextBox1.Text += "檔案路徑： " + filename.ToString() + "\n";
                richTextBox1.Text += "副檔名： " + filename.Substring(filename.LastIndexOf(".") + 1, filename.Length - filename.LastIndexOf(".") - 1) + "\n";    //取得副檔名
                richTextBox1.Text += "檔案大小： " + File.Open(filename, FileMode.Open).Length.ToString() + " 位元組\n";
                richTextBox1.Text += "\n";
                richTextBox1.Text += "IsReadOnly : " + finfo.IsReadOnly + "\n";
                richTextBox1.Text += "CreationTime : " + finfo.CreationTime + "\n";
                richTextBox1.Text += "CreationTimeUtc : " + finfo.CreationTimeUtc + "\n";
                richTextBox1.Text += "LastAccessTime : " + finfo.LastAccessTime + "\n";
                richTextBox1.Text += "LastAccessTimeUtc : " + finfo.LastAccessTimeUtc + "\n";
                richTextBox1.Text += "LastWriteTime : " + finfo.LastWriteTime + "\n";
                richTextBox1.Text += "LastWriteTimeUtc : " + finfo.LastWriteTimeUtc + "\n";

                string fileSize = (finfo.Length / 1024).ToString() + " KB";
                string temp = filename.Remove(filename.LastIndexOf('.'));

                richTextBox1.Text += "filename = " + filename + "\n";
                richTextBox1.Text += "fileSize = " + fileSize + "\n";
                richTextBox1.Text += "前檔名 : " + temp + "\n";
            }

            //------------------------------------------------------------  # 60個

            //刪除檔案 (不使用資源回收筒)
            filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            finfo = new FileInfo(filename);
            if (finfo.Exists == true)  // 確認檔案是否存在
            {
                finfo.Delete();  // 刪除檔案
                richTextBox1.Text += "檔案刪除成功\n";
            }
            else
            {
                richTextBox1.Text += "找不到檔案\n";
            }

            //------------------------------------------------------------  # 60個

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            finfo = new FileInfo(filename);  // 创建FileInfo对象

            //定义一个字符串数组，用来存储文件的相关属性
            string[] strAttribute = new string[] { finfo.Name, Convert.ToDouble(finfo.Length / 1024).ToString(), finfo.Extension, finfo.CreationTime.ToString(), finfo.IsReadOnly.ToString(), finfo.LastWriteTime.ToString() };
            var values = from str in strAttribute  // 使用LINQ为文件属性赋值
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
                richTextBox1.Text += "檔名 : " + v.Name.ToString() + "\n";//显示文件名
                richTextBox1.Text += "大小 : " + v.Size.ToString() + "\n";//显示文件大小
                richTextBox1.Text += "副檔名 : " + v.Exten.ToString() + "\n";//显示文件扩展名
                richTextBox1.Text += "建立時間 : " + v.CTime.ToString() + "\n";//显示文件创建时间
                richTextBox1.Text += "修改時間 : " + v.WTime.ToString() + "\n";//显示文件最后修改时间
                richTextBox1.Text += "是否唯讀 : " + v.ReadOnly.ToString() + "\n";//显示文件是否只读
            }
        }

        //------------------------------------------------------------  # 60個

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

        //------------------------------------------------------------  # 60個

        private void bt_file03_Click(object sender, EventArgs e)
        {
            /*
            //File的檔案操作方法
            File.Create()
            File.Copy()  // 檔案拷貝
            File.Move()  // 檔案重新命名
            File.Delete()  // 刪除檔案
            */

            //根據時間建立文件
            //File.Create("D:\\______test_files\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".jpg");//建立文件

            //建立臨時檔案
            //File.Create("tmp_" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件

            //------------------------------------------------------------  # 60個



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
            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案建立時間 : " + File.GetCreationTime(filename) + "\n";
            richTextBox1.Text += "檔案最後修改時間 : " + File.GetLastWriteTime(filename) + "\n";
            richTextBox1.Text += "檔案最後存取時間 : " + File.GetLastAccessTime(filename) + "\n";
        }

        private void bt_file05_Click(object sender, EventArgs e)
        {
            // File.Get

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";

            filename = @"D:\_git\vcs\_1.data\______test_files1\article.txt";

            show_file_info(filename);

            richTextBox1.Text += "\n改變檔案時間 與 檔案屬性\n\n";

            File.SetCreationTime(filename, new DateTime(1985, 5, 4));
            File.SetLastWriteTime(filename, new DateTime(1995, 6, 5));
            File.SetLastAccessTime(filename, new DateTime(2005, 7, 6));
            //File.SetLastAccessTime(filename, DateTime.Now);  // touch
            //File.SetLastWriteTime(filename, DateTime.Now);  // touch

            show_file_info(filename);

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
            Path.GetExtension()取得副檔名 包含.
            Path.GetPathRoot()根目錄
            Path.Combine()

            Path.GetRandomFileName()取得任意檔名
            Path.GetTempFileName()取得臨時檔名
            Path.GetTempPath()取得臨時路徑
            */

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            if (File.Exists(filename) == true)  // 確認檔案是否存在
            {
                richTextBox1.Text += "完整路徑檔名 : " + Path.GetFullPath(filename) + "\n";  // 取得路徑
                richTextBox1.Text += "路徑 : " + Path.GetDirectoryName(filename) + "\n";
                richTextBox1.Text += "檔名(包含副檔名) : " + Path.GetFileName(filename) + "\n";
                richTextBox1.Text += "檔名(不包含副檔名) : " + Path.GetFileNameWithoutExtension(filename) + "\n";
                richTextBox1.Text += "副檔名 : " + Path.GetExtension(filename) + "\n";  // 取得副檔名 包含.
                richTextBox1.Text += "根目錄 : " + Path.GetPathRoot(filename) + "\n";  // 取得根目錄

                richTextBox1.Text += "修改成完整時間檔名 : " + Path.GetDirectoryName(filename) + "\\" + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
                richTextBox1.Text += "修改成時間檔名 : " + Path.GetFileNameWithoutExtension(filename) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + Path.GetExtension(filename) + "\n";
            }

            richTextBox1.Text += "取得隨機檔名 : " + Path.GetRandomFileName() + "\n";
            richTextBox1.Text += "取得臨時檔名 : " + Path.GetTempFileName() + "\n";
            richTextBox1.Text += "取得臨時路徑 : " + Path.GetTempPath() + "\n";

            //------------------------------------------------------------  # 60個

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            richTextBox1.Text += "檔案 : " + filename + "\n";

            string strOne = System.IO.Path.GetFileNameWithoutExtension(filename);
            richTextBox1.Text += "取得前檔名\n";
            richTextBox1.Text += strOne + "\n";

            //------------------------------------------------------------  # 60個

            //Path.Combine()

            filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Form1.cs";
            richTextBox1.Text += filename + "\n";

            filename = Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) + "\\Form1.cs";
            richTextBox1.Text += filename + "\n";

            //取得本程式之Form1.cs所在的資料夾
            string dirname = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..\"));
            richTextBox1.Text += dirname + "\n";

            //D:\_git\vcs\_1.data\______test_files1\_case1

            //由檔案取出檔案路徑
            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string ccc = Path.GetDirectoryName(filename);
            richTextBox1.Text += "ccc : " + ccc + "\n";
            string filename2 = "picture1111.jpg";

            string new_filename = Path.Combine(Path.GetDirectoryName(filename), filename2);
            richTextBox1.Text += "new_filename : " + new_filename + "\n";

            /*
            讀Form1.cs所在位置的檔案純文字檔：
            string filename = Path.Combine(Application.StartupPath, "..\\..");

            將二進位檔讀出顯示出來
            txtCiphertextFile.Text = filename + "\\ciphertext.dat";
            txtCiphertext.Text = File.ReadAllBytes(txtCiphertextFile.Text).ToHex(' ');

            //------------------------------------------------------------  # 60個
            */

        }

        //------------------------------------------------------------  # 60個

        private void bt_file07_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_file08_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_file09_Click(object sender, EventArgs e)
        {
            //用 FileInfo 的方法 讀寫檔案

            //新增檔案, 指定路徑建立檔案
            string filename = @"_tmp_aaaa.txt";
            FileInfo finfo = new FileInfo(filename);

            FileStream fs = finfo.Create();  // 用Create方法新增一個檔案
            fs.Close();//關閉檔案

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            filename = @"_tmp_bbbb.txt";
            finfo = new FileInfo(filename);

            string text;
            StreamReader sr;
            StreamWriter sw;

            //1.寫入
            sw = finfo.CreateText();  //開啟新檔
            text = "寫入AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
            //將輸入的資料覆蓋原檔並重新寫入
            sw.WriteLine(text);
            sw.Flush();
            sw.Close();

            //2.附加 
            sw = finfo.AppendText();   //開啟舊檔
            text = "附加AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
            //將輸入的資料附加到資料檔的最後
            sw.WriteLine(text);
            sw.Flush();
            sw.Close();

            //以唯讀模式開檔
            sr = finfo.OpenText();  //以唯讀模式開檔
            Console.WriteLine("資料檔內容如下：");
            Console.WriteLine(sr.ReadToEnd());//讀出資料
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //複製檔案
            filename = @"_tmp_cccc.txt";
            //目的檔案「Text.txttmp」
            String tagPath = filename + "tmp";
            finfo = new FileInfo(filename);

            //以CopyTo方法複製檔案
            //finfo.CopyTo(tagPath);  NG
            richTextBox1.Text += filename + " 已複製\n";

            filename = @"_tmp_dddd.txt";
            finfo = new FileInfo(filename);
            //finfo.Rename("test2.txt");
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir00_Click(object sender, EventArgs e)
        {
            //Directory 的方法
            /*            
            Directory.Exists()
            Directory.CreateDirectory()  // 新建資料夾
            Directory.Move()
            Directory.Delete()
            Directory.GetDirectories()  // 取得指定目錄中子目錄的名稱
            Directory.GetFiles()  // 取得指定目錄中檔案的名稱
            Directory.GetCurrentDirectory()  // 目前所在路徑, 目前工作目錄
            Directory.SetCurrentDirectory()  // 設定工作目錄
            Directory.GetLastWriteTime()  // 資料夾最後修改時間
            Directory.SetLastWriteTime()
            */

            //取得目前工作目錄

            richTextBox1.Text += "目前工作目錄 : " + Environment.CurrentDirectory + "\n";

            string currentPath = Directory.GetCurrentDirectory();  // 目前工作目錄
            richTextBox1.Text += "目前工作目錄 : " + currentPath + "\n";

            //Directory.SetCurrentDirectory("D:\\");  // 設定工作目錄

            //------------------------------------------------------------  # 60個

            string Path = @"D:/_git/vcs/_1.data/______test_files1/aaaa/bbbb";
            if (Directory.Exists(Path) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + Path + " 不存在\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + Path + " 存在\n";
            }

            //------------------------------------------------------------  # 60個

            //建立一個新資料夾
            string new_foldername = @"D:/_git/vcs/_1.data/______test_files_file_name2/aaaa/bbbb";
            if (Directory.Exists(new_foldername) == false)  // 確認資料夾是否存在
            {
                Directory.CreateDirectory(new_foldername);  // 新建資料夾
                richTextBox1.Text += "已建立一個新資料夾: " + new_foldername + "\n";
            }
            else
            {
                richTextBox1.Text += "資料夾: " + new_foldername + " 已存在，不能再建立\n";
            }

            //------------------------------------------------------------  # 60個

            //一般文件名按顺序排
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\";

            string[] filenames = Directory.GetFileSystemEntries(foldername, "*.png");
            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            //刪除資料夾
            Path = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            /*
            if (Directory.Exists(Path) == false)  // 確認資料夾是否存在
                richTextBox1.Text += "資料夾: " + Path + " 不存在，不能刪除\n";
            else
            {
                Directory.Exists(Path);  // 確認資料夾是否存在
                richTextBox1.Text += "已刪除資料夾: " + Path + "\n";
            }
            */
            if (Directory.Exists(Path) == true)  // 確認資料夾是否存在
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

            //未完成
            string foldername_old = @"D:/_git/vcs/_1.data/______test_files_file_name1";
            string foldername_new = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            if (Directory.Exists(foldername_old) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "原始資料夾: " + foldername_old + " 不存在, 不能拷貝\n";
                return;
            }

            if (Directory.Exists(foldername_new) == false)  // 確認資料夾是否存在
            {
                //複製
            }
            else
            {
                richTextBox1.Text += "目的資料夾: " + foldername_new + " 已存在, 不能拷貝\n";
                return;
            }

            //------------------------------------------------------------  # 60個

            string Foldername_old = @"D:/_git/vcs/_1.data/______test_files_file_name2";
            string Foldername_new = @"D:/_git/vcs/_1.data/______test_files_file_name3";
            if (Directory.Exists(Foldername_old) == false)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "原始資料夾: " + Foldername_old + " 不存在, 不能拷貝\n";
                return;
            }

            if (Directory.Exists(Foldername_new) == true)  // 確認資料夾是否存在
            {
                richTextBox1.Text += "目的資料夾: " + Foldername_new + " 已存在, 不能拷貝\n";
                return;
            }

            Directory.Move(Foldername_old, Foldername_new);  // 資料夾改名
            richTextBox1.Text += "移動/更名 完成，從原始資料夾: " + Foldername_old + " 到目的資料夾: " + Foldername_new + "\n";

            //移動資料夾，從 sourceDirName 移動到 destDirName
            string sourceDirName = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName = @"D:\_git\vcs\_1.data\______test_files1\folder22";

            if (Directory.Exists(sourceDirName))  // 確認資料夾是否存在
            {
                if (!Directory.Exists(destDirName))  // 確認資料夾是否存在
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
            foldername = @"D:/_git/vcs/_1.data/______test_files_file_name2";

            if (Directory.Exists(foldername))  // 確認資料夾是否存在
            {
                richTextBox1.Text += "刪除資料夾: " + foldername + "\n";
                try
                {
                    DeleteDirectory(foldername);
                    //Directory.Delete(foldername, true);   //recurrsive
                    //Directory.Delete(foldername, false);   //not recurrsive
                    richTextBox1.Text += "OK\n";
                }
                catch
                {
                    richTextBox1.Text += "FAIL\n";
                }
            }
            else
            {
                richTextBox1.Text += "資料夾: " + foldername + " 不存在，不能刪除\n";
            }
        }

        private void bt_dir01_Click(object sender, EventArgs e)
        {
            //DirectoryInfo 的方法

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            DirectoryInfo dinfo11 = new DirectoryInfo(foldername);
            richTextBox1.Text += dinfo11.FullName + "資料夾下的檔案資訊如下：\n";

            FileInfo[] fis = dinfo11.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo finfo in fis)
            {
                richTextBox1.Text += "完整路徑：" + finfo.FullName + "\n";
                richTextBox1.Text += "寫入時間：" + finfo.LastWriteTime + "\n";
                richTextBox1.Text += "檔案大小：" + finfo.Length.ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            DirectoryInfo dinfo1 = new DirectoryInfo(foldername);
            richTextBox1.Text += "資料夾\n";
            DirectoryInfo[] dinfos = dinfo1.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dinfos)
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

                if (di.GetDirectories().Length > 0)
                {
                    richTextBox1.Text += "下一層資料夾：";
                    foreach (DirectoryInfo ddi in di.GetDirectories())
                    {
                        richTextBox1.Text += ddi.Name + "\n";
                    }
                }
                else
                {
                    richTextBox1.Text += "\n";
                }
            }

            //  檢查每個檔案的資訊
            richTextBox1.Text += "檔案\n";
            fis = dinfo1.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            foreach (FileInfo finfo in fis)
            {
                richTextBox1.Text += "全檔名：" + finfo.FullName + "\n";
                richTextBox1.Text += "  檔名：" + finfo.Name + "\n";
                richTextBox1.Text += "  副檔名：" + finfo.Extension + "\n";  // 取得副檔名
                richTextBox1.Text += "  大小：";
                if (finfo.Length > (1024 * 1024))
                {
                    richTextBox1.Text += (finfo.Length / 1024 / 1024).ToString() + " MB( " + finfo.Length + " 位元組)\n";
                }
                else if (finfo.Length > (1024))
                {
                    richTextBox1.Text += (finfo.Length / 1024).ToString() + " KB( " + finfo.Length + " 位元組)\n";
                }
                else
                {
                    richTextBox1.Text += finfo.Length + " 位元組\n";
                }
                richTextBox1.Text += "  建立日期：" + finfo.CreationTime + "\n";
                richTextBox1.Text += "  日期：" + finfo.CreationTimeUtc + "\n";
                richTextBox1.Text += "  存取日期：" + finfo.LastAccessTime + "\n";
                richTextBox1.Text += "  日期：" + finfo.LastAccessTimeUtc + "\n";
                richTextBox1.Text += "  修改日期：" + finfo.LastWriteTime + "\n";
                richTextBox1.Text += "  日期：" + finfo.LastWriteTimeUtc + "\n";
                richTextBox1.Text += "  屬性：" + finfo.Attributes + "\n";
                richTextBox1.Text += "  資料夾：" + finfo.Directory + "\n";
                richTextBox1.Text += "  資料夾名：" + finfo.DirectoryName + "\n";
                richTextBox1.Text += "  唯讀：" + finfo.IsReadOnly + "\n";
            }

            //------------------------------------------------------------  # 60個

            //使用递归法删除文件夹中的所有文件
            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";

            int file_no = 0;
            DirectoryInfo dinfo2 = new DirectoryInfo(foldername);//创建DirectoryInfo对象
            FileSystemInfo[] fsinfos = dinfo2.GetFileSystemInfos();  // 獲取所有的文件
            for (int i = 0; i < fsinfos.Length; i++)//遍歷獲取到的文件
            {
                FileInfo finfo = new FileInfo(foldername + "\\" + fsinfos[i].ToString());//创建FileInfo对象
                //finfo.Delete();  // 刪除檔案
                richTextBox1.Text += "偽刪除 " + foldername + "\\" + fsinfos[i].ToString() + "\n";
                file_no++;
            }
            richTextBox1.Text += "删除成功, 共刪除 " + file_no.ToString() + " 個檔案\n";

            //------------------------------------------------------------  # 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd\aaaaaa";

            // 建立DirectoryInfo類別的dinfo3物件，可用來操作資料夾目錄
            DirectoryInfo dinfo3 = new DirectoryInfo(foldername);
            if (dinfo3.Exists)
            {	// 判斷目錄是否存在
                richTextBox1.Text += foldername + ", 路徑存在, 不建立目錄\n";
            }
            else
            {
                richTextBox1.Text += foldername + ", 路徑不存在，建立目錄\n";
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
            richTextBox1.Text += dinfo4.FullName + ", 資料夾下的子資料夾如下 :\n";
            //DirectoryInfo[]
            dinfos = dinfo4.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dinfos)
            {
                richTextBox1.Text += "完整路徑 : " + di.FullName + "\t建立時間 : " + di.CreationTime + "\n";
            }
        }

        private void bt_dir02_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\compare\ddddd";
            richTextBox1.Text += "檔案清單---<*.TXT>";

            DirectoryInfo dinfo10 = new DirectoryInfo(foldername);

            //從指定路徑傳回指定的檔案類型
            FileInfo[] listFile = dinfo10.GetFiles("*.txt");

            richTextBox1.Text += "\n檔名\t檔案長度\t修改日期\n";

            // 讀取資料夾中有關於 --檔名(Name)、長度(Length) 和 修改日期(LastWriteTime)
            foreach (FileInfo getInfo in listFile)
            {
                richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + getInfo.LastWriteTime.ToShortDateString() + "\n";
            }

            //------------------------------------------------------------  # 60個

            //DirectoryInfo的方法2

            //儲存要回傳的檔案路徑和檔案類型
            foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook";
            richTextBox1.Text += "檔案清單---<*.jpg>\n\n";

            DirectoryInfo dinfo = new DirectoryInfo(foldername);

            //從指定路徑傳回指定的檔案類型
            //FileInfo[]
            listFile = dinfo.GetFiles("*.jpg");
            //設定檔案的標題
            string sign = new string('-', 37);
            string fnName = "檔名", fnLength = "檔案長度";
            string fnDate = "修改日期";
            richTextBox1.Text += "\t" + fnName + "\t" + fnLength + "\t" + fnDate + "\n";
            richTextBox1.Text += sign + "\n";

            foreach (FileInfo getInfo in listFile)
            {
                string dt = getInfo.LastWriteTime.ToShortDateString();
                richTextBox1.Text += getInfo.Name + "\t" + getInfo.Length.ToString() + "\t" + dt + "\n";
            }

            //------------------------------------------------------------  # 60個

            //Path.Combine()

            /*
            string filename = Path.Combine(Application.StartupPath, @"..\..\Form1.cs");

            richTextBox1.Text += "filename old = " + filename + "\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU";
            DirectoryInfo dinfo12 = new DirectoryInfo(foldername);
            string[] filenames = dinfo12.GetFiles().OrderBy(p => p.Name).ToArray();
            foreach (string filename in filenames)
            {
                if (filename.FullName.Contains("id_card") == true)
                {
                    Console.WriteLine(filename.FullName);
                }
            }
            */

            //------------------------------------------------------------  # 60個

            //取得磁碟檔案資料
            // 由檔案取得檔案所在磁碟
            DriveInfo drive_info = new DriveInfo(@"D:\_git\vcs\_1.data\______test_files1");
            richTextBox1.Text += "由檔案取得檔案所在磁碟 : " + drive_info.RootDirectory + "\n";

            // Get the root directory and print out some information about it.
            DirectoryInfo dinfo9 = drive_info.RootDirectory;
            richTextBox1.Text += "根目錄 : " + dinfo9.Attributes.ToString() + "\n";

            // Get the files in the directory and print out some information about them.
            FileInfo[] fis = dinfo9.GetFiles("*.*");

            foreach (FileInfo finfo in fis)
            {
                richTextBox1.Text += "檔案 : " + finfo.Name + "\n";
                richTextBox1.Text += "存取日期：" + finfo.LastAccessTime + "\n";
                richTextBox1.Text += "大小：" + finfo.Length + "\n";
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

            //獲取指定目錄下的所有子目錄及文件類型

            //還沒加入listView之標題

            listView1.Items.Clear();

            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_book_magazine";

            //DirectoryInfo
            dinfo = new DirectoryInfo(foldername);

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
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir03_Click(object sender, EventArgs e)
        {
            //Directory.GetFiles()  // 取得指定目錄中檔案的名稱

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1";
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            show_filenames(filenames);

            DirectoryInfo dinfo5 = new DirectoryInfo(foldername);
            FileInfo[] fis = dinfo5.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
            show_filenames(fis);

            //------------------------------------------------------------  # 60個

            //取得資料夾下的所有檔案(包括子目錄)

            string filetype = String.Empty;
            filetype = "*.*";

            foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            // 取得指定目錄中檔案的名稱
            filenames = Directory.GetFiles(foldername, filetype, System.IO.SearchOption.AllDirectories);  // 由資料夾取出檔案名稱串列
            show_filenames(filenames);
            /*
            // 由資料夾取出檔案名稱串列
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱 //獲得文件夾目錄下所有文件全路徑
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱 //獲得文件夾目錄下指定後綴名文件全路徑

            Array.Sort(filenames);  // 排序
            */

            //------------------------------------------------------------  # 60個

            //撈出一層jpg檔
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";
            //string[]
            filenames = Directory.GetFiles(foldername, "*.jpg");  // 取得指定目錄中檔案的名稱
            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            foldername = @"D:\_git\vcs\_1.data\______test_files1\__text";

            //string[]
            filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            //Directory.GetFiles()
            //撈出資料夾內的檔案(一層)
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            //string[]
            filenames = Directory.GetFiles(foldername);
            for (int i = 0; i < filenames.Length; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的檔案(多層)
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            //單一搜尋pattern
            //string[]
            filenames = Directory.GetFiles(foldername, "*.*", System.IO.SearchOption.AllDirectories);
            foreach (string filename in filenames)
            {
                richTextBox1.Text += filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的檔案(一層)
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            System.IO.SearchOption search_option = System.IO.SearchOption.TopDirectoryOnly;
            //string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };     //指名搜尋pattern
            string[] patterns = { "*.*" };  //指名搜尋pattern
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                string[] filenames2 = Directory.GetFiles(foldername, pattern, search_option);
                foreach (string filename in filenames2)
                {
                    richTextBox1.Text += filename + "\n";
                }
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的檔案(多層)
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            //System.IO.SearchOption
            search_option = System.IO.SearchOption.AllDirectories;
            //string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" }; //指名搜尋pattern
            string[] patterns2 = { "*.*" };  //指名搜尋pattern

            //多個搜尋pattern
            foreach (string pattern in patterns2)
            {
                string[] filenames3 = Directory.GetFiles(foldername, pattern, search_option);
                foreach (string filename in filenames3)
                {
                    richTextBox1.Text += filename + "\n";
                }
            }

        }

        //------------------------------------------------------------  # 60個

        private void bt_dir04_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir05_Click(object sender, EventArgs e)
        {
            string destDirName1 = @"D:\_git\vcs\_1.data\______test_files1\folder2";
            string destDirName2 = @"D:\_git\vcs\_1.data\______test_files1\folder22";
            DeleteDirectory(destDirName1, true);
            DeleteDirectory(destDirName2, true);

            //------------------------------------------------------------  # 60個

            //Directory.Delete 目錄不是空的

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_cpfile";

            richTextBox1.Text += "Directory.Delete 目錄不是空的\n";
            try
            {
                //Directory.Delete(foldername); //若目錄不是空的, 會出現IOException
                Directory.Delete(foldername, true); //強制刪除不是空的目錄
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息m : " + ex.Message + "\n";
            }

            //------------------------------------------------------------  # 60個

            //刪除資料夾下子資料夾(偽)

            foldername = @"D:/_git/vcs/_1.data/______test_files1";
            DateTime dt = DateTime.Now;
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            foreach (DirectoryInfo paths in dinfo.GetDirectories())
            {
                if (paths.CreationTime < Convert.ToDateTime(dt.AddDays(-(dt.Day) + 1)))
                {
                    //paths.Delete();
                    richTextBox1.Text += "path = " + paths + "\n";
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_dir06_Click(object sender, EventArgs e)
        {
            //資料夾最後修改時間

            string foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_bookbook\";

            //取得資料夾最後一次被存取的時間
            DateTime dt = Directory.GetLastWriteTime(foldername);  // 資料夾最後修改時間
            richTextBox1.Text += "資料夾建立的時間 : " + dt + "\n";

            //更新時間
            Directory.SetLastWriteTime(foldername, DateTime.Now);  // touch
            dt = Directory.GetLastWriteTime(foldername);  // 資料夾最後修改時間
            richTextBox1.Text += "最後存取時間 : " + dt + "\n";
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
            //計算某個檔案夾下的檔案大小，並可以用不同的單位(KB,MB,GB)顯示

            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            message = "";
            filesize_all = 0;

            DirectoryInfo dinfo6 = new DirectoryInfo(foldername);

            double size = DirSize(dinfo6);
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
        }

        //------------------------------------------------------------  # 60個

        private void bt_files07_Click(object sender, EventArgs e)
        {
            //撈出資料夾內所有jpg檔
            string foldername = @"D:\_git\vcs\_1.data\______test_files1";
            string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
            foreach (string dir in dirs)
            {
                richTextBox1.Text += "取得子目錄 : " + dir + "\n";

                // 取得指定目錄中檔案的名稱
                var filenames = Directory.GetFiles(dir, "*.jpg").Select(Path.GetFileName);

                DirectoryInfo dinfo7 = new DirectoryInfo(dir);
                FileInfo[] fis = dinfo7.GetFiles("*.jpg");
                foreach (var filename in filenames)
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
                        foreach (FileInfo finfo in fis)
                        {
                            //檔案最後修改時間
                            richTextBox1.Text += "The file modify date is: " + File.GetLastWriteTime(dir) + "\n";
                        }
                    }
                }
            }
            richTextBox1.Text += "dirs : " + dirs + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_files08_Click(object sender, EventArgs e)
        {
            //撈出資料夾內特定類型的檔案

            string foldername = @"D:\_git\vcs\_1.data\______test_files1";
            string searchPattern = "*.cs;*.csv;*.ico";

            richTextBox1.Text += "撈出資料夾內特定類型的檔案\t單層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            List<string> filenames = FindFiles(foldername, searchPattern, false);  // false : 單層
            show_filenames(filenames);

            richTextBox1.Text += "撈出資料夾內特定類型的檔案\t多層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            filenames.Clear();
            filenames = FindFiles(foldername, searchPattern, true);  // true : 多層
            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            //FindFiles()
            //撈出所有圖片檔 並存成一個List 2

            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony1";

            //List<String>
            filenames = new List<String>();
            filenames = FindFiles(foldername, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);

            show_filenames(filenames);

            //------------------------------------------------------------  # 60個

            //FindFiles()3

            //撈出資料夾內特定類型的檔案
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt";
            //string
            searchPattern = "*.txt";
            bool recurrsive = false;

            //List<string> filenames;

            /*
            richTextBox2.Text += "撈出資料夾內特定類型的檔案\t單層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            filenames = FindFiles(foldername, searchPattern, recurrsive);
            foreach (string filename in filenames)
            {
                richTextBox1.Text += filename + "\n";
            }
            */

            recurrsive = true;
            richTextBox1.Text += "撈出資料夾內特定類型的檔案\t多層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            //filenames.Clear();
            filenames = FindFiles(foldername, searchPattern, recurrsive);
            foreach (string filename in filenames)
            {
                richTextBox1.Text += filename + "\n";
            }

            //------------------------------------------------------------  # 60個
        }

        // 搜尋符合格式的文件
        // recurrsive =  false : 單層
        // recurrsive =  true  : 多層
        private List<string> FindFiles(string foldername, string patterns, bool recurrsive)
        {
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
                // 取得指定目錄中檔案的名稱
                string[] filenames = Directory.GetFiles(foldername, pattern, search_option);
                foreach (string filename in filenames)
                {
                    if (!files.Contains(filename))
                    {
                        files.Add(filename);
                    }
                }
            }

            files.Sort();  // 排序

            return files;
        }

        //------------------------------------------------------------  # 60個

        private void bt_files09_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void bt_files10_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";

            richTextBox1.Text += "全目錄 : " + foldername + "\n";
            richTextBox1.Text += "上層目錄 : " + new DirectoryInfo(foldername).Parent + "\n";
            richTextBox1.Text += "上上層目錄 : " + new DirectoryInfo(foldername).Parent.Parent + "\n";
            richTextBox1.Text += "上上層目錄的全目錄 : " + new DirectoryInfo(foldername).Parent.Parent.FullName + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void bt_files11_Click(object sender, EventArgs e)
        {
            //test 
            //lblFileSize.Text = finfo.Length.ToFileSizeApi();
            //int size = 12345678;
            //richTextBox1.Text += "size = " + size.tofil

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            FileInfo finfo = new FileInfo(filename);
            richTextBox1.Text += finfo.Length.ToString() + "\n";
            richTextBox1.Text += finfo.Length.ToFileSizeApi() + "\n";

            int ccc = 12345678;   // double 才可以用 ToFileSize
            richTextBox1.Text += "ccc = " + ccc.ToString() + "\n";
            richTextBox1.Text += "ccc = " + ((double)ccc).ToFileSize() + "\n";

        }

        //------------------------------------------------------------  # 60個

        void check_filetype(string filename)
        {
            int len = 10;
            int[] data = new int[len];
            string builtHex = string.Empty;
            using (Stream S = File.OpenRead(filename))
            {
                for (int i = 0; i < 10; i++)
                {
                    data[i] = S.ReadByte();  // 讀一拜
                    builtHex += data[i].ToString("X2") + " ";

                    //builtHex += S.ReadByte().ToString("X2");  // 讀一拜

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

        private void bt_files12_Click(object sender, EventArgs e)
        {
            //偵測原始檔案類型

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_csv\covid19_data2021_06_27.part.csv";
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\person.xml";
            string filename4 = @"C:\_git\vcs\_1.data\______test_files1\_anime\cat\cat1.png";
            string filename5 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";
            string filename6 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_mdb\db_09.mdb";
            string filename7 = @"C:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\eula.3081a.txt";
            string filename8 = @"C:\_git\vcs\_1.data\______test_files1\__RW\_ini\ConnectString.ini";

            check_filetype(filename1);
            //check_filetype(filename2);
            //check_filetype(filename3);
            //check_filetype(filename4);
            //check_filetype(filename5);
            //check_filetype(filename6);
            //check_filetype(filename7);
            //check_filetype(filename8);
        }

        //------------------------------------------------------------  # 60個

        private void bt_files13_Click(object sender, EventArgs e)
        {
            //取得資料夾下所有圖片檔資訊

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";

            IEnumerable<FileInfo> filenames = null;
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            filenames = dinfo.EnumerateFiles("*.jpg").OrderBy(i => i.Name[0]).ThenBy(i => i.Name.Length).ThenBy(i => i.Name);

            int len = filenames.Count();
            richTextBox1.Text += "共有 " + len.ToString() + " 個檔案\n";

            if (filenames != null && filenames.Count() > 0)
            {

            }

            foreach (var filename in filenames)
            {
                richTextBox1.Text += filename.Name + "\n";
                richTextBox1.Text += filename.FullName + "\n";
                richTextBox1.Text += filename.Extension + "\n";
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

        //------------------------------------------------------------  # 60個

        private void bt_files15_Click(object sender, EventArgs e)
        {
            //搜尋檔案

            richTextBox1.Text += "搜尋檔案, 只找一層 IMG_20180228_215525.jpg\n";
            foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic\_icon";
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            foreach (FileInfo info in dinfo.GetFiles("IMG_20180228_215525.jpg"))
            {
                richTextBox1.Text += "有找到\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_files16_Click(object sender, EventArgs e)
        {
            // 屬性相關 GetAttributes SetAttributes

            // 刪除檔案前，先設定檔案屬性為[正常的]
            // File.SetAttributes(filename, FileAttributes.Normal);

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            FileInfo finfo = new FileInfo(filename);
            FileAttributes attr = finfo.Attributes;

            if ((attr & FileAttributes.ReadOnly) > 0)
            {
                richTextBox1.Text += "唯讀檔案\n";
            }
            else
            {
                richTextBox1.Text += "一般檔案\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //設定檔案屬性
            filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_貓咪\cat1.png";

            finfo = new FileInfo(filename);
            finfo.Attributes = FileAttributes.ReadOnly;  // 唯讀
            finfo.Attributes = FileAttributes.System;  // 系統
            finfo.Attributes = FileAttributes.Archive;  // 存檔
            finfo.Attributes = FileAttributes.Hidden;  // 隱藏

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "檔案屬性 : " + File.GetAttributes(filename).ToString() + "\n";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            //File.SetAttributes(filename, FileAttributes.Hidden);//隱藏
            richTextBox1.Text += File.GetAttributes(filename) + "\n";


            if ((File.GetAttributes(filename) & FileAttributes.ReadOnly) == FileAttributes.ReadOnly)
            {
                richTextBox1.Text += "檔案唯讀，不能修改檔案時間\n";
            }
            else
            {

            }

            File.SetAttributes(filename, FileAttributes.Archive);
            File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden);
            File.SetAttributes(filename, FileAttributes.Archive | FileAttributes.Hidden | FileAttributes.ReadOnly);
        }

        //------------------------------------------------------------  # 60個

        private void bt_files17_Click(object sender, EventArgs e)
        {
            //FindAllFiles 各種方法會出多層 同一資料夾

            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            FindAllFiles2(foldername);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            FindAllFiles1(foldername);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            FindAllFiles3(foldername);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            ProcessDirectoryA(foldername);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            DirectoryInfo dinfo = new DirectoryInfo(foldername);

            foreach (DirectoryInfo d_info in dinfo.GetDirectories())
            {
                richTextBox1.Text += d_info.FullName + "\n";
                richTextBox1.Text += d_info.Name + "\n";
            }

            foreach (FileInfo finfo in dinfo.GetFiles())
            {
                richTextBox1.Text += finfo.FullName + "\n";
                //richTextBox1.Text += finfo.Name + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //GetDirectories(), GetFiles()

            //DirectoryInfo
            dinfo = new DirectoryInfo(foldername);

            DirectoryInfo[] dinfos = dinfo.GetDirectories();  // 傳回目前目錄的子目錄, 一層
            foreach (DirectoryInfo di in dinfos)
            {
                richTextBox1.Text += "------------------------------\n";  // 30個
                richTextBox1.Text += "取得資料夾 : " + di.FullName + "\n";

                FileInfo[] files1 = di.GetFiles();

                foreach (FileInfo finfo in files1)
                {
                    richTextBox1.Text += "取得檔案 : " + finfo.FullName + "\n";
                }
            }

            richTextBox1.Text += "目錄 : " + foldername + " 下\n";
            FileInfo[] files2 = dinfo.GetFiles();

            foreach (FileInfo finfo in files2)
            {
                richTextBox1.Text += "取得檔案 : " + finfo.FullName + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的檔案(一層), 所有檔案
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            foreach (string filename in Directory.GetFileSystemEntries(foldername))
            {
                richTextBox1.Text += filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            //撈出資料夾內的TXT檔案(一層), 限定 *.txt
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            foreach (string filename in Directory.GetFileSystemEntries(foldername, "*.txt"))
            {
                richTextBox1.Text += filename + "\n";
            }

            //------------------------------------------------------------  # 60個

            //取得一層檔案
            foldername = @"D:\_git\vcs\_1.data\______test_files3";

            //DirectoryInfo
            dinfo = new DirectoryInfo(foldername);
            FileInfo[] finfos = dinfo.GetFiles();
            StringBuilder sb = new StringBuilder();
            foreach (FileInfo file in finfos)
            {
                richTextBox1.Text += file.Name + "\n";
            }

            //------------------------------------------------------------  # 60個

            //------------------------------------------------------------  # 60個

        }

        public void ProcessDirectoryA(string foldername)
        {
            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            richTextBox1.Text += dinfo.Name + "\n";

            string[] fileEntries = Directory.GetFiles(foldername);
            Array.Sort(fileEntries);
            foreach (string filename in fileEntries)
            {
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
                // fi.FullName, fi.Extension, fi.Length, fi.CreationTime
                // richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionTBGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
            }

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(foldername);
            Array.Sort(subdirectoryEntries);

            //richTextBox1.Text += "共有 " + subdirectoryEntries.Length.ToString() + " 個子目錄\n";
            foreach (string subdirectory in subdirectoryEntries)
            {
                richTextBox1.Text += "dir = " + subdirectory + "\n";
            }

            //richTextBox1.Text += "資料夾 : " + foldername + " ";
            //richTextBox1.Text += "子目錄數 : " + subdirectoryEntries.Length.ToString() + "\t";

            foreach (string subdirectory in subdirectoryEntries)
            {
                ProcessDirectoryA(subdirectory);
            }
        }

        //------------------------------------------------------------  # 60個

        private void FindAllFiles2(string foldername)
        {
            //使用 DirectoryInfo() 和 FileInfo()

            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            FileSystemInfo[] fsinfos = dinfo.GetFileSystemInfos();  // 獲取所有的文件
            foreach (FileSystemInfo fsinfo in fsinfos)  // 遍歷獲取到的文件
            {
                if (fsinfo is DirectoryInfo)
                {
                    FindAllFiles2(fsinfo.FullName);
                }
                else
                {
                    FileInfo finfo = new FileInfo(fsinfo.FullName);
                    richTextBox1.Text += finfo.FullName + "\n";
                }
            }

            /*
            DirectoryInfo dinfo = new DirectoryInfo(foldername);

            richTextBox1.Text += "遍歷文件夾\n";
            foreach (DirectoryInfo di in dinfo.GetDirectories())
            {
                richTextBox1.Text += di.Name + "\n";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "遍歷文件\n";
            foreach (FileInfo NextFile in dinfo.GetFiles())
            {
                richTextBox1.Text += NextFile.Name + "\n";
            }
            */
        }

        private void FindAllFiles1(string foldername)
        {
            //使用 Directory.GetDirectories() 和 Directory.GetFiles()

            //richTextBox1.Text += "讀取資料夾下的資料夾, 只看一層\n";
            string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
            //richTextBox1.Text += "總共" + dirs.Length.ToString() + "個資料夾\n";
            foreach (string dir in dirs)
            {
                //richTextBox1.Text += "取得子目錄 : " + dir + "\n";
                FindAllFiles1(dir);
            }

            //richTextBox1.Text += "讀取資料夾下的檔案, 只看一層\n";
            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            //richTextBox1.Text += "總共" + filenames.Length.ToString() + "個檔案\n";
            foreach (string filename in filenames)
            {
                richTextBox1.Text += filename + "\n";
            }
        }

        //多層 且指明副檔名
        private void FindAllFiles3(string foldername)
        {
            //使用 DirectoryInfo() 和 Directory.GetFiles()??

            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + dinfo.FullName + "\n";
            FileSystemInfo[] fsinfos = dinfo.GetFileSystemInfos();  // 獲取所有的文件
            foreach (FileSystemInfo fsinfo in fsinfos)  // 遍歷獲取到的文件
            {
                if (fsinfo is DirectoryInfo)
                {
                    FindAllFiles3(((DirectoryInfo)fsinfo).FullName);
                }
                else
                {
                    string fullname = fsinfo.FullName;
                    string shortname = fsinfo.Name;
                    string ext = fsinfo.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        richTextBox1.Text += fullname + "\n";
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        //richTextBox1.Text += "短檔名: " + shortname + "\n";
                        //richTextBox1.Text += "前檔名: " + forename + "\n";
                    }
                }
            }
        }

        //------------------------------------------------------------  # 60個

        private void bt_files18_Click(object sender, EventArgs e)
        {
            //FindAllFiles2
            //搜尋子目錄內的所有檔案   一層
            string foldername = @"D:\_git\vcs\_1.data\______test_files3";

            DirectoryInfo dinfo = new DirectoryInfo(foldername);
            richTextBox1.Text += "搜尋子目錄內的所有檔案, 子目錄 : " + dinfo.ToString() + "\n";

            DirectoryInfo[] dinfos = dinfo.GetDirectories();
            richTextBox1.Text += "子目錄 :\n";
            foreach (DirectoryInfo di in dinfos)
            {
                richTextBox1.Text += di + "\n";
            }

            FileInfo[] finfos = dinfo.GetFiles();
            richTextBox1.Text += "子目錄 " + dinfo.Name + " 下的檔案 :\n";
            foreach (FileInfo finfo in finfos)
            {
                richTextBox1.Text += finfo + "\n";
            }
            richTextBox1.Text += "\n";

            //------------------------------------------------------------  # 60個

            //轉出一層
            foldername = @"D:\_git\vcs\_1.data\______test_files3";
            if (foldername.CompareTo("") == 0)
            {
                return;
            }

            //DirectoryInfo
            dinfo = new DirectoryInfo(foldername);

            DirectoryInfo[] dirs = dinfo.GetDirectories();
            //FileInfo[]
            finfos = dinfo.GetFiles();

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
            foreach (FileInfo fi in finfos)
            {
                string str4 = fi.Name;
                string str5 = fi.FullName;
                string str6 = fi.Length.ToString();
                richTextBox1.Text += str4 + "\t" + str5 + "\t" + str6 + "\n";
            }


        }

        //------------------------------------------------------------  # 60個

        private void bt_files19_Click(object sender, EventArgs e)
        {
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
        public void ProcessDirectory(string foldername)
        {
            string[] filenames = Directory.GetFiles(foldername);
            Array.Sort(filenames);
            folder_size = 0;
            folder_files = 0;
            foreach (string filename in filenames)
            {
                ProcessFile(filename);
            }
            //richTextBox1.Text += "folder_name = " + foldername + "\n";
            //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";
            //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
            if (folder_files == 0)
            {
                //richTextBox1.Text += "空資料夾 folder_name = " + foldername + "\n";
            }

            // Recurse into subdirectories of this directory.
            string[] subdirectoryEntries = Directory.GetDirectories(foldername);
            Array.Sort(subdirectoryEntries);
            foreach (string subdirectory in subdirectoryEntries)
            {
                DirectoryInfo di = new DirectoryInfo(subdirectory);
                FolederName = subdirectory;
                richTextBox1.Text += "\n\n" + FolederName + "\n";
                ProcessDirectory(subdirectory);
            }

            /*
            richTextBox1.Text += "資料夾 " + foldername + "\t檔案個數 : " + folder_files.ToString() + "\t大小 : " + ByteConversionTBGBMBKB(Convert.ToInt64(folder_size)) + "\n";
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

            richTextBox1.Text += "\n\nfileinfos len = " + fileinfos.Count.ToString() + "\n";

            richTextBox1.Text += "total_size = " + total_size.ToString() + "\n";
            richTextBox1.Text += "total_files = " + total_files.ToString() + "\n";
            //richTextBox1.Text += "folder_size = " + folder_size.ToString() + "\n";
            //richTextBox1.Text += "folder_files = " + folder_files.ToString() + "\n";
        }

        private void bt_files20_Click(object sender, EventArgs e)
        {
            //我的轉出
            //string foldername = @"D:\_git\vcs\_1.data\______test_files1\__pic";
            //string foldername = @"D:\vcs\astro\_DATA2\_________整理_mp3\_mp3_台語\_陳一郎\";
            //string foldername = @"C:\dddddddddd\_music_from_yt";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1\";

            export_filenames(foldername);
        }

        //------------------------------------------------------------  # 60個

        private void bt_files21_Click(object sender, EventArgs e)
        {
            //拷貝檔案, 限定拷貝大小
            //拷貝檔案, 限定拷貝大小, 每次拷貝1024拜

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            string filename2 = Application.StartupPath + "\\jpg_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";

            CopyFile(filename1, filename2, 1024);
        }

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

        //------------------------------------------------------------  # 60個

        private void bt_files22_Click(object sender, EventArgs e)
        {
            //info
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
                    while ((bb = sourceFile.ReadByte()) != -1)  // 讀一拜
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

        private void bt_files23_Click(object sender, EventArgs e)
        {
            //拷貝檔案1
            copy_file(MODE1);
        }

        //------------------------------------------------------------  # 60個

        private void bt_files24_Click(object sender, EventArgs e)
        {
            //拷貝檔案2
            copy_file(MODE2);
        }

        //------------------------------------------------------------  # 60個

        //根據文件頭判斷上傳的文件類型 ST
        private void bt_files25_Click(object sender, EventArgs e)
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
                BinaryReader br = new BinaryReader(fs);
                string fileClass;
                byte buffer;
                buffer = br.ReadByte();  // 讀一拜
                fileClass = buffer.ToString();
                buffer = br.ReadByte();  // 讀一拜
                fileClass += buffer.ToString();
                br.Close();
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

        //------------------------------------------------------------  # 60個

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

        private void bt_files26_Click(object sender, EventArgs e)
        {
            //取得檔案類型
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string fileTypeName = GetTypeName(filename);

            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案類型 : " + fileTypeName + "\n";
        }
        //取得檔案類型 SP

        //------------------------------------------------------------  # 60個

        private void bt_files27_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void bt_files28_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void bt_files29_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        void show_filenames(FileInfo[] fis)
        {
            int len = fis.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 個檔案\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += fis[i].Name + "\n";
            }
        }

        void show_filenames(List<String> filenames)
        {
            int len = filenames.Count;
            richTextBox1.Text += "共有 " + len.ToString() + " 個檔案\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }
        }

        void show_filenames(string[] filenames)
        {
            int len = filenames.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 個檔案\n";

            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";
            }
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
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

在 C# 中使用 StreamReader.ReadToEnd() 方法將檔案讀取為字串
StreamReader sr = new StreamReader(@"D:\File\file.txt");
string text = sr.ReadToEnd();
Console.WriteLine(text);			

//------------------------------------------------------------  # 60個

string filename = @"D:\______test_files\_case1\pic1.jpg";

圖片檔讀取：非鎖定檔方法 [Image.FromFile 釋放]

content from http://jashliao.pixnet.net/blog/post/223534989

FileStream fs = File.OpenRead(StrDestFilePath); //OpenRead[二進位讀檔]
int filelength = 0;
filelength = (int)fs.Length; //獲得檔長度
Byte[] image = new Byte[filelength]; //建立一個位元組陣列
fs.Read(image, 0, filelength); //按位元組流讀取
System.Drawing.Image result = System.Drawing.Image.FromStream(fs);
fs.Close();

//pictureBox1.Image = (Image)image;

//------------------------------------------------------------  # 60個

        public static void Rename(this FileInfo finfo, string newName)
        {
            finfo.MoveTo(finfo.Directory.FullName + "\\" + newName);
        }

//------------------------------------------------------------  # 60個

待測
//File.AppendAllText("E:\\Time\\新建文檔夾 (2)" + "/" + strname, DateTime.Now+"\n");

//------------------------------------------------------------  # 60個

使用 File.ReadAllText() 方法將檔案讀取為字串
string all_text = File.ReadAllText(filename);
File.WriteAllText(@"setting.txt", folderPath);

//------------------------------------------------------------  # 60個

List<FileInfo> myFiles = new List<FileInfo>();//创建List泛型对象
myFiles.Add(new FileInfo(filename));//将遍历的所有文件添加到List对象中

//------------------------------------------------------------  # 60個



*/


/*
FileInfo[] fis = dinfo.GetFiles();  // 由DI取得FI陣列, 單層檔案資訊
FileInfo[] fis = dinfo.GetFiles("IMG_20180228_215525.jpg"))
FileInfo[] fis = dinfo.GetFiles("*.jpg");
FileInfo[] fis = dinfo.GetFiles("*.txt");
FileInfo[] fis = dinfo.GetFiles("*.*");

*/



