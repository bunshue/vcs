using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileInfo DirectoryInfo
using System.Diagnostics;

namespace vcs_DrAP
{
    public partial class Form1 : Form
    {
        void Read_Setup_File()
        {
            int i;
            if (System.IO.File.Exists(drap_setup_filename) == false)
            {
                //MessageBox.Show("檔案 " + drap_setup_filename + " 不存在，製作一個。");
                StreamWriter sw = File.CreateText(drap_setup_filename);
                string content = "";
                //content += SelectedLanguage.ToString();
                content += "\n";
                //content += ezisp_path;
                content += "\n";

                sw.WriteLine(content);
                sw.Close();
            }
            else
            {
                //MessageBox.Show("檔案 " + drap_setup_filename + " 存在, 開啟，並讀入設定");

                string line;
                StreamReader sr = new StreamReader(drap_setup_filename);
                for (i = 0; i < 2; i++)
                {
                    line = sr.ReadLine();
                    //MessageBox.Show(line);
                    if (i == 0)
                    {
                        //SelectedLanguage = int.Parse(line);
                        //comboBox3.SelectedIndex = SelectedLanguage;
                        //Update_Language(SelectedLanguage);
                    }
                    if (i == 1)
                    {
                        //ezisp_path = line;
                    }
                }
                sr.Close();
            }
        }

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
            Read_Setup_File();
        }

        string path = String.Empty;
        int filetype = 0;
        string filetype2 = String.Empty;
        Int64 total_size = 0;
        Int64 total_files = 0;
        Int64 folder_size = 0;
        Int64 folder_files = 0;
        int step = 0;
        int flag_search_mode = 0;
        int flag_search_done = 0;
        int flag_search_vcs_pattern = 0;
        string drap_setup_filename = "drap_setup.ini";

        public class MyFileInfo
        {
            public string filename;
            public long size;
            public MyFileInfo(string n, long s)
            {
                this.filename = n;
                this.size = s;
            }
        }

        //不用宣告長度的陣列(Array)
        // 宣告fileinfos 為List
        // 以下List 裡為MyFileInfo 型態

        List<MyFileInfo> fileinfos = new List<MyFileInfo>();

        private void button2_Click(object sender, EventArgs e)
        {
            flag_search_mode = 0;
            flag_search_done = 0;

            fileinfos.Clear();
            if (path != String.Empty)
            {
                //只撈一層的所有檔案
                foreach (string fname in System.IO.Directory.GetFileSystemEntries(path))
                {
                    richTextBox1.Text += fname + "\n";
                }
            }

            //只撈一層的檔案
            total_size = 0;
            total_files = 0;

            if (path == String.Empty)
                path = "C:\\______test_vcs";
                //path = @"D:\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";

            richTextBox1.Text += path + "\n\n";

            if (File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(path, 0);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                //ProcessDirectory(path);


                try
                {
                    //richTextBox1.Text += targetDirectory + "\n\n";
                    //DirectoryInfo di = new DirectoryInfo(targetDirectory);
                    //richTextBox1.Text += di.Name + "\n\n";

                    // Process the list of files found in the directory.
                    try
                    {
                        string[] fileEntries = Directory.GetFiles(path);
                        Array.Sort(fileEntries);
                        foreach (string fileName in fileEntries)
                        {
                            ProcessFile(fileName, step);
                        }
                        step = 0;
                    }
                    catch (UnauthorizedAccessException ex)
                    {
                        richTextBox1.Text += ex.Message + "\n";
                        //MessageBox.Show(ex.Message);
                        /*
                        FileAttributes attr = (new FileInfo(filePath)).Attributes;
                        Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                        if ((attr & FileAttributes.ReadOnly) > 0)
                            Console.Write("The file is read-only.");
                        */
                    }
                }
                catch (IOException ex)
                {
                    richTextBox1.Text += "IOException, " + ex.GetType().Name + "\n";
                    /*
                    Console.WriteLine(
                        "{0}: The write operation could not " +
                        "be performed because the specified " +
                        "part of the file is locked.",
                        e.GetType().Name);
                    */
                }




                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                show_file_info();
                flag_search_done = 1;
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
                flag_search_done = 0;
            }     


        }

        private void button8_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "c:\\______test_vcs";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                path = folderBrowserDialog1.SelectedPath;
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
            flag_search_done = 0;
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
            try
            {
                //richTextBox1.Text += targetDirectory + "\n\n";
                //DirectoryInfo di = new DirectoryInfo(targetDirectory);
                //richTextBox1.Text += di.Name + "\n\n";

                // Process the list of files found in the directory.
                try
                {
                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    Array.Sort(fileEntries);
                    folder_size = 0;
                    folder_files = 0;
                    foreach (string fileName in fileEntries)
                    {
                        ProcessFile(fileName, step);
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
                        if (checkBox1.Checked == false)
                        {
                            richTextBox1.Text += "\n";
                            //for (int i = 0; i < step * 2; i++)
                            //richTextBox1.Text += " ";
                            richTextBox1.Text += di.Name + "\n";
                        }
                        step++;
                        ProcessDirectory(subdirectory);
                    }
                    step = 0;
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                    //MessageBox.Show(ex.Message);
                    /*
                    FileAttributes attr = (new FileInfo(filePath)).Attributes;
                    Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                    if ((attr & FileAttributes.ReadOnly) > 0)
                        Console.Write("The file is read-only.");
                    */
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
                /*
                Console.WriteLine(
                    "{0}: The write operation could not " +
                    "be performed because the specified " +
                    "part of the file is locked.",
                    e.GetType().Name);
                */
            }
        }

        // Insert logic for processing found files here.
        public void ProcessFile(string path, int step)
        {
            //richTextBox1.Text += path + "\n";
            FileInfo fi = new FileInfo(path);
            total_size += fi.Length;
            total_files++;
            folder_size += fi.Length;
            folder_files++;

            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";
            int min_size_mb = int.Parse(textBox1.Text);
            if (((checkBox1.Checked == true) && (fi.Length > min_size_mb * 1024 * 1024)) || (checkBox1.Checked == false))
            {
                if (flag_search_mode == 1)
                {
                    bool res;
                    res = fi.FullName.ToLower().Replace(" ", "").Contains(textBox2.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        return;
                    else
                    {
                        richTextBox1.Text += "get file : " + fi.FullName + "\n";
                    }
                }

                for (int i = 0; i < step * 2; i++)
                    richTextBox1.Text += " ";
                //richTextBox1.Text += fi.Name + " len = " + fi.Length.ToString() + "\n";
                //richTextBox1.Text += filename + "\n";
                //richTextBox1.Text += fi.Name + "\n";
                //richTextBox1.Text += fi.Name + " \t\t " + ByteConversionGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                richTextBox1.Text += fi.FullName + "\t\t" + ByteConversionGBMBKB(Convert.ToInt64(fi.Length)) + "\n";
                //richTextBox1.Text += fi.Directory + "\n";
                //richTextBox1.Text += fi.DirectoryName + "\n";

                /*
                ListViewItem i1 = new ListViewItem(fi.FullName);

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fi.Length));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font(
                    "Times New Roman", 10, System.Drawing.FontStyle.Bold);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
                */

                fileinfos.Add(new MyFileInfo(fi.FullName, fi.Length));
                //fileinfos.Add(new MyFileInfo(fi.FullName.ToString(), fi.Length));
                //fileinfos.Add(new MyFileInfo("aaaaaaa", 12345));

            }

        }

        void show_file_info()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.Clear();
            //設置列名稱
            listView1.Columns.Add("名稱", 900, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Center);
            listView1.Visible = true;

            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.size.CompareTo(y.size); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.size.CompareTo(y.size); });
            }

            richTextBox2.Text += "fileinfos.Count = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                if (flag_search_mode == 1)
                {
                    bool res;
                    res = i1.Name.ToLower().Replace(" ", "").Contains(textBox2.Text.ToLower().Replace("-", ""));
                    if (res == false)
                        continue;
                    else
                    {
                        richTextBox1.Text += "aaaa get file : " + i1.Name + "\n";
                    }
                }

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].size));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font(
                    "Times New Roman", 10, System.Drawing.FontStyle.Bold);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
        }

        void show_file_info2()
        {
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.Clear();
            //設置列名稱
            listView1.Columns.Add("名稱", 900, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 150, HorizontalAlignment.Center);
            listView1.Visible = true;

            if (checkBox2.Checked == true)
            {
                //排序 由小到大
                //fileinfos.Sort((x, y) => { return x.size.CompareTo(y.size); });

                //排序 由大到小  在return的地方多個負號
                fileinfos.Sort((x, y) => { return -x.size.CompareTo(y.size); });
            }

            richTextBox2.Text += "cnt = " + fileinfos.Count.ToString() + "\n";
            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

                bool res;
                res = fileinfos[i].filename.ToLower().Replace(" ", "").Contains(textBox2.Text.ToLower().Replace("-", ""));
                if (res == false)
                    continue;
                else
                {
                    richTextBox2.Text += "get file : " + fileinfos[i].filename + "\n";
                }

                i1.UseItemStyleForSubItems = false;

                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();

                //sub_i1a.Text = fi.Length.ToString();
                sub_i1a.Text = ByteConversionGBMBKB(Convert.ToInt64(fileinfos[i].size));
                i1.SubItems.Add(sub_i1a);
                sub_i1a.ForeColor = System.Drawing.Color.Blue;

                sub_i1a.Font = new System.Drawing.Font(
                    "Times New Roman", 10, System.Drawing.FontStyle.Bold);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "開始計時\n";
            // Create stopwatch
            Stopwatch stopwatch = new Stopwatch();
            // Begin timing
            stopwatch.Start();

            flag_search_mode = 0;
            flag_search_done = 0;

            fileinfos.Clear();
            /*  無法依子目錄排序 廢棄
            if (path == String.Empty)
                path = "C:\\______test_vcs";

            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(path, filetype2, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                //richTextBox1.Text += filename + "\n";
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += fi.Name + "\n";
            }
            */

            total_size = 0;
            total_files = 0;

            if (path == String.Empty)
                path = "C:\\______test_vcs";
                //path = @"D:\_DATA2\_VIDEO_全為備份\百家讲坛_清十二帝疑案";

            richTextBox1.Text += path + "\n\n";
            if (File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(path, 0);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                flag_search_done = 1;
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessDirectory(path);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t大小 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                if (flag_search_mode == 1)
                    show_file_info2();
                else
                    show_file_info();
                flag_search_done = 1;
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
                flag_search_done = 0;
            }

            // Stop timing
            stopwatch.Stop();
            // Write result
            richTextBox2.Text += "停止計時\t";
            richTextBox2.Text += "總時間: " + stopwatch.ElapsedMilliseconds.ToString() + " msec\n";
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            filetype = comboBox1.SelectedIndex;
            switch (filetype)
            { 
                case 0:
                    filetype2 = "*.*";
                    break;
                case 1:
                    filetype2 = "*.mp3";
                    break;
                case 2:
                    filetype2 = "*.txt";
                    break;
                default:
                    filetype2 = "*.*";
                    break;
            }
            richTextBox1.Text += "change file type to " + filetype2 + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            fileinfos.Clear();
            listView1.Clear();
            richTextBox1.Clear();
            richTextBox2.Clear();
        }

        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(KSize / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (KSize / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(KSize / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (KSize / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(KSize / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return KSize.ToString() + "Byte";//顯示Byte值
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox1.Text += "你選擇了\t" + listView1.Items[selNdx].Text + "\n";
            System.Diagnostics.Process.Start(listView1.Items[selNdx].Text);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            /*
            richTextBox1.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox1.Text += listView1.SelectedItems[i] + "\n";
            }

            richTextBox1.Text += "播放\n";
            */

            int selNdx;
            string all_filename = string.Empty;
            string player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
            if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
            {
                richTextBox1.Text += "無檔可播\n";
                return;
            }

            //richTextBox1.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
            }

            //指定應用程式路徑
            //string target = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
            string target = player_path;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二
            ProcessStartInfo pInfo = new ProcessStartInfo(target);
            pInfo.Arguments = all_filename;

            richTextBox1.Text += "target : " + target + "\n";
            richTextBox1.Text += "all_filename : " + all_filename + "\n";

            using (Process p = new Process())
            {
                p.StartInfo = pInfo;
                p.Start();
            }
           

        }

        private void listView1_KeyDown(object sender, KeyEventArgs e)
        {
            //richTextBox1.Text += "KeyDown, 按鍵是：" + e.KeyCode + "\n";

            if (e.KeyCode == Keys.A)
            {
                if ((Control.ModifierKeys & Keys.Control) == Keys.Control)
                {
                    //richTextBox1.Text += "Ctrl + A\n";
                    //richTextBox1.Text += "共有項目" + listView1.Items.Count.ToString() + " 個\n";

                    for (int i = 0; i < listView1.Items.Count; i++)
                    {
                        //richTextBox1.Text += listView1.Items[i] + "\n";
                        listView1.Items[i].Selected = true;
                    }
                }
            }

            if (e.KeyCode == Keys.Enter)
            {
                //等同於 button9_Click , 以後要改成只是呼叫函數

                /*
                richTextBox1.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
                for (int i = 0; i < listView1.SelectedIndices.Count; i++)
                {
                    richTextBox1.Text += listView1.SelectedItems[i] + "\n";
                }

                richTextBox1.Text += "播放\n";
                */

                int selNdx;
                string all_filename = string.Empty;
                string player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
                if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
                {
                    richTextBox1.Text += "無檔可播\n";
                    return;
                }

                //richTextBox1.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
                //for (int i = 0; i < listView1.SelectedIndices.Count; i++)
                for (int i = 0; i < listView1.SelectedItems.Count; i++)
                {
                    selNdx = listView1.SelectedIndices[i];
                    listView1.Items[selNdx].Selected = true;    //選到的項目
                    //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                    all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
                }

                //指定應用程式路徑
                //string target = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
                string target = player_path;

                //方法一
                //Process.Start(target, "參數");
                //Process.Start(target, all_filename);

                //方法二
                ProcessStartInfo pInfo = new ProcessStartInfo(target);
                pInfo.Arguments = all_filename;

                richTextBox1.Text += "target : " + target + "\n";
                richTextBox1.Text += "all_filename : " + all_filename + "\n";

                using (Process p = new Process())
                {
                    p.StartInfo = pInfo;
                    p.Start();
                }

            }


        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
            if (this.listView1.Items.Count <= 0)
            {
                richTextBox2.Text += "無內容可複製\n";
                return;
            }

            //C# – 複製資料到剪貼簿
            Clipboard.Clear();

            for (int i = 0; i < listView1.Items.Count; i++)
            {
                //richTextBox2.Text += listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\n";

                //C# – 複製資料到剪貼簿 累計
                Clipboard.SetDataObject(Clipboard.GetText() + listView1.Items[i].SubItems[0].Text + "\t" + listView1.Items[i].SubItems[1].Text + "\n");      //建議用此
            }
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            //C# 限制textbox只能輸入數字
            if(e.KeyChar.CompareTo('0')<0 || e.KeyChar.CompareTo('9')>0) //比較輸入值的範圍是否超出數字
                e.Handled = true;// Handled 為是否鎖住輸入
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_search_done == 1)
            {
                flag_search_mode = 1;
                show_file_info2();
                flag_search_mode = 0;
            }
            else
            {
                richTextBox2.Text += "111";
                flag_search_mode = 1;
                button1_Click(sender, e);
                flag_search_mode = 0;
            }


        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你選擇了 : " + listView1.SelectedIndices.Count.ToString() + " 個檔案, 分別是\n";
            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox1.Text += listView1.SelectedItems[i] + "\n";
            }

            richTextBox1.Text += "刪除\n";

            for (int i = 0; i < listView1.SelectedIndices.Count; i++)
            {
                richTextBox1.Text += "刪除檔案: " + listView1.SelectedItems[i].Name + "\n";
                //File.SetAttributes(listView1.SelectedItems[i].Name, FileAttributes.Normal);
                //File.Delete(listView1.SelectedItems[i].ToString());
            }



        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Size = new Size(1920, 1080);
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            if (textBox3.Text == "")
            {
                richTextBox2.Text += "未輸入搜尋內容\n";
                return;
            }
            flag_search_vcs_pattern = 1;

        }



    }
}

