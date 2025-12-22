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
            dx = 180 + 5;
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

            groupBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            listView1.Size = new Size(300, 240);
            listView1.Location = new Point(x_st + dx * 2, y_st + dy * 3 - 20);

            listBox1.Size = new Size(300, 240);
            listBox1.Location = new Point(x_st + dx * 3 + 120, y_st + dy * 3 - 20);

            richTextBox1.Size = new Size(600, 300);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 7 - 30);

            x_st = 10;
            y_st = 10;
            dy = 25;
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            textBox2.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            textBox3.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            bt_rename.Location = new Point(x_st + dx * 2 + 20, y_st + dy * 4);
            groupBox1.Size = new Size(500, 170);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1040, 800);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }
        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
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
                StreamWriter Sw = File.CreateText(filename);
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

        private void button4_Click(object sender, EventArgs e)
        {
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

        [DllImport("kernel32.dll")]
        private static extern long GetVolumeInformation(
            string PathName,
            StringBuilder VolumeNameBuffer,
            UInt32 VolumeNameSize,
            ref UInt32 VolumeSerialNumber,
            ref UInt32 MaximumComponentLength,
            ref UInt32 FileSystemFlags,
            StringBuilder FileSystemNameBuffer,
            UInt32 FileSystemNameSize
        );

        private void button11_Click(object sender, EventArgs e)
        {
            //取得磁碟資訊
            string drive_letter = "C:";

            uint serial_number = 0;
            uint max_component_length = 0;
            StringBuilder sb_volume_name = new StringBuilder(256);
            UInt32 file_system_flags = new UInt32();
            StringBuilder sb_file_system_name = new StringBuilder(256);

            if (GetVolumeInformation(drive_letter, sb_volume_name,
                (UInt32)sb_volume_name.Capacity, ref serial_number,
                ref max_component_length, ref file_system_flags,
                sb_file_system_name,
                (UInt32)sb_file_system_name.Capacity) == 0)
            {
                richTextBox1.Text += "無法取得磁碟資訊\n";
            }
            else
            {
                richTextBox1.Text += "磁碟名稱 : " + drive_letter + "\n";
                richTextBox1.Text += "磁碟名稱 : " + sb_volume_name.ToString() + "\n";
                richTextBox1.Text += "序號 : " + serial_number.ToString() + "\n";
                richTextBox1.Text += "Max Component Length\t" + max_component_length.ToString() + "\n";
                richTextBox1.Text += "檔案系統 : " + sb_file_system_name.ToString() + "\n";
                richTextBox1.Text += "Flags\t" + "&&H" + file_system_flags.ToString("x") + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
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
    }
}


//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/


//string path = Application.StartupPath;

