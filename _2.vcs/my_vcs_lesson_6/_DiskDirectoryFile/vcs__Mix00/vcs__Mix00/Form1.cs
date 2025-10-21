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
using System.Runtime.InteropServices;
using System.Security.Cryptography;

namespace vcs__Mix00
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
            dy = 75;

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

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 4 - 120);
            richTextBox1.Size = new Size(817, 330);
            listView1.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            listBox1.Location = new Point(x_st + dx * 5 + 60, y_st + dy * 7);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
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

        private void button1_Click(object sender, EventArgs e)
        {
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

        private void button2_Click(object sender, EventArgs e)
        {
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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
            richTextBox1.Text += "副檔名 GetExtension\t" + GetExtension + "\n";
            richTextBox1.Text += "GetPathRoot\t" + GetPathRoot + "\n";
            richTextBox1.Text += "GetRandomFileName\t" + GetRandomFileName + "\n";

            //檔案資訊
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";

            FileInfo fileInfo = new FileInfo(filename);
            string fileSize = (fileInfo.Length / 1024).ToString() + " KB";
            string temp = filename.Remove(filename.LastIndexOf('.'));
            string fileName = Path.GetFileNameWithoutExtension(filename);
            string fileExtension = Path.GetExtension(filename);

            richTextBox1.Text += "filename = " + filename + "\n";
            richTextBox1.Text += "fileSize = " + fileSize + "\n";
            richTextBox1.Text += "temp = " + temp + "\n";
            richTextBox1.Text += "fileName = " + fileName + "\n";
            richTextBox1.Text += "fileExtension = " + fileExtension + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //獲取文件的版本信息
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_material\_dll\AForge.Video.dll";

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
            {
                richTextBox1.Text += "檔案: " + filename + " 不存在\n";
            }
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
        }

        private void button14_Click(object sender, EventArgs e)
        {
            File.Copy(@"../../Form1.cs", @"aaaaa.cs");
            richTextBox1.Text += "複製檔案完成\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            string foldername = @"D:\_git\vcs\_1.data\______test_files1\__text";

            foreach (String a in Directory.GetDirectories(foldername))
            {
                richTextBox1.Text += "找到資料夾\t" + a + "\n";
            }

            foreach (String a in Directory.GetFiles(foldername))
            {
                richTextBox1.Text += "找到檔案\t" + a + "\n";
            }
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

        private void button16_Click(object sender, EventArgs e)
        {
            //偵測磁碟裝置型態

            DriveInfo[] allDrives = DriveInfo.GetDrives();

            foreach (DriveInfo d in allDrives)
            {
                richTextBox1.Text += "Drive : " + d.Name + "\tFile type : " + d.DriveType + "\n";
                if (d.DriveType == DriveType.Removable)
                {
                    richTextBox1.Text += "Removable Device : " + d.Name + "\n";
                }
            }

            //獲取計算機磁盤空間
            //在System.IO命名空間下的DriveInfo類的GetDrives()方法可以用來獲得計算機上的所有邏輯驅動器的名稱。DriveInfo類的TotalSize屬性可義獲得磁盤的空間大小。

            for (int i = 0; i < allDrives.Length; i++)
            {
                richTextBox1.Text += "取得磁碟 : " + allDrives[i].Name;

                if (allDrives[i].IsReady == true)
                {
                    richTextBox1.Text += "\t空間 : " + Convert.ToString(allDrives[i].TotalSize / 1024 / 1024 / 1024) + "GB\n";
                }
                else
                {
                    richTextBox1.Text += "\n";
                }
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //拷貝檔案, 限定拷貝大小
            //拷貝檔案, 每次拷貝1024拜

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

        private void button18_Click(object sender, EventArgs e)
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
                        //richTextBox1.LoadFile(openFileDialog1.FileName, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
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

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //刪除資料夾下子資料夾(偽)
            var pathstr = @"D:/_git/vcs/_1.data/______test_files1";
            if (Directory.Exists(pathstr))
            {
                //var strname=DateTime.Now.ToShortDateString().Replace("/","-")+".txt";
                var dt = DateTime.Now;
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
        }

        private void button21_Click(object sender, EventArgs e)
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

        private void button22_Click(object sender, EventArgs e)
        {
            //取得檔案類型

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string fileTypeName = GetTypeName(filename);

            richTextBox1.Text += "檔案 : " + filename + "\n";
            richTextBox1.Text += "檔案類型 : " + fileTypeName + "\n";
        }
        //取得檔案類型 SP

        private void button23_Click(object sender, EventArgs e)
        {
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";

            StreamReader sr1 = new StreamReader(filename1);
            StreamReader sr2 = new StreamReader(filename2);
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()) == true)
            {
                richTextBox1.Text += "兩個檔案相同\n";
            }
            else
            {
                richTextBox1.Text += "兩個檔案不相同\n";
            }
            sr1.Close();
            sr2.Close();


            filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            if (FileCompare(filename1, filename2) == true)
            {
                richTextBox1.Text += "兩個檔案相同\n";
            }
            else
            {
                richTextBox1.Text += "兩個檔案不相同\n";
            }
        }

        private bool FileCompare(string file1, string file2)
        {
            //　判斷相同的文件是否被參考兩次。
            if (file1 == file2)
            {
                return true;
            }
            int file1byte = 0;
            int file2byte = 0;
            using (FileStream fs1 = new FileStream(file1, FileMode.Open), fs2 = new FileStream(file2, FileMode.Open))
            {
                //　檢查文件大小。如果兩個文件的大小並不相同,則視為不相同。
                if (fs1.Length != fs2.Length)
                {
                    // 關閉文件。
                    fs1.Close();
                    fs2.Close();
                    return false;
                }
                //　逐一比較兩個文件的每一個字節，直到發現不相符或已到達文件尾端為止。
                do
                {
                    // 從每一個文件讀取一個字節。
                    file1byte = fs1.ReadByte();
                    file2byte = fs2.ReadByte();
                }
                while ((file1byte == file2byte) && (file1byte != -1));
                // 關閉文件。
                fs1.Close();
                fs2.Close();
            }
            //　返回比較的結果。在這個時候，只有當兩個文件的內容完全相同時， "file1byte" 才會等於 "file2byte"。
            return ((file1byte - file2byte) == 0);
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
            //創建唯一的檔案名, 考慮時間因素

            //創建唯一的檔案名, 考慮時間因素
            for (int i = 0; i < 10; i++)
            {
                string filename = string.Format("{0}{1}", DateTime.Now.ToString("yyyyMMddHHmmss"), GetUniqueKey());
                richTextBox1.Text += filename + "\n";
            }
        }

        //使用RNGCryptoServiceProvider類創建唯一的最多8位數字符串。
        private static string GetUniqueKey()
        {
            int maxSize = 8;
            //int minSize = 5;
            char[] chars = new char[62];
            string a;
            a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
            chars = a.ToCharArray();
            int size = maxSize;
            byte[] data = new byte[1];
            RNGCryptoServiceProvider crypto = new RNGCryptoServiceProvider();
            crypto.GetNonZeroBytes(data);
            size = maxSize;
            data = new byte[size];
            crypto.GetNonZeroBytes(data);
            StringBuilder result = new StringBuilder(size);
            foreach (byte b in data)
            {
                result.Append(chars[b % (chars.Length - 1)]);
            }
            return result.ToString();
        }

        //根據文件頭判斷上傳的文件類型 ST
        private void button28_Click(object sender, EventArgs e)
        {
            //根據文件頭判斷上傳的文件類型
            //根據文件頭判斷上傳的文件類型
            string filename = @"D:\_git\vcs\_1.data\______test_files1\doraemon.jpg";
            string result = getFileType(filename);
            richTextBox1.Text += "File Type : " + result + "\n";
        }

        /// <summary>
        /// 根據文件頭判斷上傳的文件類型
        /// </summary>
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

        private void button29_Click(object sender, EventArgs e)
        {

        }
    }
}
