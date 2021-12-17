using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

using System.Diagnostics;   //for FileVersionInfo

namespace test4_filename
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_case1\_case1a\_case1aa\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //string filename = @"C:\______test_files\picture1.jpg";

            var GetFileName = Path.GetFileName(filename);
            var GetFileNameWithoutExtension = Path.GetFileNameWithoutExtension(filename);
            var GetDirectoryName = Path.GetDirectoryName(filename);
            var GetFullPath = Path.GetFullPath(filename);

            //richTextBox1.Text += "filename\t" + filename + "\n";
            richTextBox1.Text += "GetFullPath\t" + GetFullPath + "\n";
            richTextBox1.Text += "GetDirectoryName\t" + GetDirectoryName + "\n";
            //richTextBox1.Text += "GetFileName\t" + GetFileName + "\n";
            richTextBox1.Text += "GetFileNameWithoutExtension\t" + GetFileNameWithoutExtension + "\n";

            label1.Text = "原檔名 :";
            textBox1.Text = filename;

            label2.Text = "檔名 :";
            textBox2.Text = GetFileNameWithoutExtension;

            label3.Text = "新檔名 :";
            textBox3.Text = GetFileNameWithoutExtension;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            listView1.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            listBox1.Location = new Point(x_st + dx * 4 + 60, y_st + dy * 5);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例
            //還沒加入listView之標題

            listView1.Items.Clear();

            //遍歷文件夾實例
            string foldername = @"C:\______test_files\_pic";
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

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            var ext = Path.GetExtension(filename);


            richTextBox1.Text += "副檔名 : " + ext + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例

            //還沒加入listView之標題

            listView1.Items.Clear();

            //遍歷文件夾實例
            string foldername = @"C:\______test_files\_pic";
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

        private void button3_Click(object sender, EventArgs e)
        {
            //新增資料夾
            //新增資料夾
            string path = Application.StartupPath;
            string folder = textBox1.Text;
            NewFolder(folder, path);
        }

        /// <summary>
        /// 新建文件夾
        /// </summary>
        /// <param name="filename">文件夾名</param>
        /// <param name="path">文件夾路徑</param>
        public static void NewFolder(string foldername, string path)
        {
            foldername.Trim();
            //如果輸入信息為空，提示
            if (foldername == "")
            {
                MessageBox.Show("目錄名不能為空");
                return;
            }
            else
            {
                string FullName = path + "\\" + foldername;
                //如果該文件以及存在
                if (Directory.Exists(FullName))
                {
                    MessageBox.Show("該目錄已經存在，請重命名");
                    return;
                }
                else
                {
                    //新建文件夾
                    Directory.CreateDirectory(FullName);
                    MessageBox.Show("新建文件夾 完成");
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //新增文件
            //新增文件
            string path = Application.StartupPath;
            string filename = textBox2.Text;
            NewFile(filename, path);
        }

        /// <summary>
        /// 新建文件
        /// </summary>
        /// <param name="filename">文件名</param>
        /// <param name="path">文件路徑</param>
        public static void NewFile(string filename, string path)
        {
            filename.Trim();
            if (filename == "")
            {
                MessageBox.Show("文件名不能為空~！");
            }
            else
            {
                if (File.Exists(path + "\\" + filename + ".txt"))
                {
                    MessageBox.Show("該文件名已經存在，請重命名");
                }
                else
                {
                    string FullName = path + "\\" + filename + ".txt";　　 //獲得文件完整信息
                    StreamWriter Sw = File.CreateText(FullName);
                    MessageBox.Show("新建文件 完成");
                }
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //檔案資訊
            string filename = @"C:\______test_files\picture1.jpg";

            var GetFileName = Path.GetFileName(filename);
            var GetFileNameWithoutExtension = Path.GetFileNameWithoutExtension(filename);
            var GetExtension = Path.GetExtension(filename);
            var GetDirectoryName = Path.GetDirectoryName(filename);
            var GetFullPath = Path.GetFullPath(filename);

            var GetPathRoot = Path.GetPathRoot(filename);
            var GetRandomFileName = Path.GetRandomFileName();

            richTextBox1.Text += "filename\t" + filename + "\n";
            richTextBox1.Text += "GetFullPath\t" + GetFullPath + "\n";
            richTextBox1.Text += "GetDirectoryName\t" + GetDirectoryName + "\n";
            richTextBox1.Text += "GetFileName\t" + GetFileName + "\n";
            richTextBox1.Text += "GetFileNameWithoutExtension\t" + GetFileNameWithoutExtension + "\n";
            richTextBox1.Text += "GetExtension\t" + GetExtension + "\n";
            richTextBox1.Text += "GetPathRoot\t" + GetPathRoot + "\n";
            richTextBox1.Text += "GetRandomFileName\t" + GetRandomFileName + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例
            string foldername = @"C:\______test_files\_pic";
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

        private void button7_Click(object sender, EventArgs e)
        {
            //遍歷文件夾實例

            string foldername = @"C:\______test_files\_pic";

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
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //獲取文件的版本信息
            string filename = @"C:\______test_files\_material\AForge.Video.dll";

            FileVersionInfo myFileVersionInfo1 = FileVersionInfo.GetVersionInfo(filename);
            richTextBox1.Text += "版本號: " + myFileVersionInfo1.FileVersion + "\n";
        }


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
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";

            richTextBox1.Text += "時間 : " + DateTime.Now.ToString() + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            copy_file(MODE1);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            copy_file(MODE2);
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            FileInfo fi = new FileInfo(filename);
            //取得檔案資訊
            //fi.CopyTo(@"C:\練習資料夾\TT2.txt");
            //MessageBox.Show("複製成功！");

            richTextBox1.Text += fi.Length.ToString() + " Bytes";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            /*
            //測不出來
            File.Encrypt(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\aaa.txt");
            richTextBox1.Text += "加密成功！\n";
            */

            File.Copy(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\aaa.txt", @"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug\bbb.txt");
            //檔案複製，注意要確認C:\VS2012\TT.txt有檔案
            richTextBox1.Text += "複製成功！\n";

        }

        private void button15_Click(object sender, EventArgs e)
        {
            String result = "";
            foreach (String a in Directory.GetDirectories(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug"))
                result += "資料夾\t" + a + "\r\n";
            //取得C:\VS2012下的資料夾資訊
            foreach (String a in Directory.GetFiles(@"C:\_git\vcs_test_all_02\vcs_test_all_02\bin\Debug"))
                result += "檔案\t" + a + "\r\n";
            //取得C:\VS2012下的檔案資訊
            richTextBox1.Text += result + "\n";
        }

        private void bt_rename_Click(object sender, EventArgs e)
        {
            var GetFileName = Path.GetFileName(filename);
            var GetFileNameWithoutExtension = Path.GetFileNameWithoutExtension(filename);
            var GetExtension = Path.GetExtension(filename);
            var GetDirectoryName = Path.GetDirectoryName(filename);
            var GetFullPath = Path.GetFullPath(filename);

            richTextBox1.Text += "GetFullPath\t" + GetFullPath + "\n";
            richTextBox1.Text += "GetDirectoryName\t" + GetDirectoryName + "\n";
            richTextBox1.Text += "GetFileName\t" + GetFileName + "\n";
            richTextBox1.Text += "GetFileNameWithoutExtension\t" + GetFileNameWithoutExtension + "\n";
            richTextBox1.Text += "GetExtension\t" + GetExtension + "\n";



            richTextBox1.Text += "新全檔名 : " + GetDirectoryName + "\\" + textBox3.Text + GetExtension + "\n";

        }
    }
}

