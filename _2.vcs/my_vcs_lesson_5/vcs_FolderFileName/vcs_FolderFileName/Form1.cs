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

namespace vcs_FolderFileName
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
        }

        string path = String.Empty;
        int filetype = 0;
        string filetype2 = String.Empty;
        Int64 total_size = 0;
        Int64 total_files = 0;

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
            if (path != String.Empty)
            {
                //只撈一層的所有檔案
                foreach (string fname in System.IO.Directory.GetFileSystemEntries(path))
                {
                    richTextBox1.Text += fname + "\n";
                }
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

        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        int step = 0;
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
                    foreach (string fileName in fileEntries)
                    {
                        ProcessFile(fileName, step);
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
            //richTextBox1.Text += fi.Name + "\t" + fi.Length.ToString() + "\n";

            if (checkBox1.Checked == true)
            {
                if (fi.Length > 2 * 1024 * 1024)
                {
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
            else
            {
                for (int i = 0; i < step * 2; i++)
                    richTextBox1.Text += " ";
                //richTextBox1.Text += fi.Name + " len = " + fi.Length.ToString() + "\n";
                //richTextBox1.Text += filename + "\n";
                richTextBox1.Text += fi.Name + "\n";
            }
        }

        void show_file_info()
        {
            listView1.View = View.Details;
            listView1.Clear();
            listView1.Columns.Add("檔名", 600, HorizontalAlignment.Center);
            listView1.Columns.Add("容量", 150, HorizontalAlignment.Center);

            //排序 由大到小
            fileinfos.Sort((x, y) => { return -x.size.CompareTo(y.size); });

            for (int i = 0; i < fileinfos.Count; i++)
            {
                ListViewItem i1 = new ListViewItem(fileinfos[i].filename);

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

            richTextBox1.Text += path + "\n\n";
            if (File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "XXXXXXXXXXXXXXX\n\n";
                ProcessFile(path, 0);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t容量 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessDirectory(path);
                richTextBox1.Text += "\n資料夾 " + path + "\t檔案個數 : " + total_files.ToString() + "\t容量 : " + ByteConversionGBMBKB(Convert.ToInt64(total_size)) + "\n";
                show_file_info();
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
            }     
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

        private void button4_Click(object sender, EventArgs e)
        {
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            listView1.Clear();
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


    }
}
