using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_FindFile
{
    public partial class Form1 : Form
    {
        List<string> all_filenames = new List<String>();
        List<String> all_strings = new List<String>();
        int filenames_count = 0;
        int strings_count = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //在Form1_Load時把資料讀出來
            txtDirectory.Text = Properties.Settings.Default.Directory;

            /*
            //檢查文字檔所在的資料夾
            //string Path = Application.StartupPath + "\\data";
            //string Path = @"C:\______test_files\__RW\_txt\vcs_FindFile_data";
            string Path = txtDirectory.Text;
            if (Directory.Exists(Path) == false)     //確認資料夾是否存在
            {
                //Directory.CreateDirectory(Path);
                //richTextBox1.Text += "已建立一個新資料夾: " + Path + "\n";
                richTextBox1.Text += "資料夾: " + Path + " 不存在，離開\n";
                return;
            }
            else
                richTextBox1.Text += "資料夾: " + Path + " 已存在，不用再建立\n";
            */

            find_files();
            load_data();
        }

        //在Form1_FormClosing時把資料存起來
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Directory = txtDirectory.Text;
            Properties.Settings.Default.Save();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "filenames_count = " + filenames_count.ToString() + "\n";
            richTextBox2.Text += "strings_count = " + strings_count.ToString() + "\n";

            int i;
            for (i = 0; i < strings_count; i++)
            {
                richTextBox2.Text += all_strings[i] + "\n";
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
            SearchOption search_option = SearchOption.TopDirectoryOnly;
            if (recurrsive)
            {
                search_option = SearchOption.AllDirectories;
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

        void find_files()
        {
            //撈出資料夾內特定類型的檔案
            //string searchDirectory = Application.StartupPath + "\\data";
            //string searchDirectory = @"C:\______test_files\__RW\_txt\vcs_FindFile_data";
            string searchDirectory = txtDirectory.Text;
            string searchPattern = "*.txt";
            bool recurrsive = false;

            //List<string> filenames;

            /*
            richTextBox2.Text += "撈出資料夾內特定類型的檔案\t單層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            all_filenames = FindFiles(searchDirectory, searchPattern, recurrsive);
            foreach (string filename in all_filenames)
            {
                richTextBox2.Text += filename + "\n";
            }
            */

            recurrsive = true;
            richTextBox2.Text += "撈出資料夾內特定類型的檔案\t多層\tPattern : " + searchPattern + "\n";
            // Search for the files.
            //all_filenames.Clear();
            all_filenames = FindFiles(searchDirectory, searchPattern, recurrsive);
            foreach (string filename in all_filenames)
            {
                richTextBox2.Text += filename + "\n";
            }
            filenames_count = all_filenames.Count;
        }

        void load_data()
        {
            foreach (string filename in all_filenames)
            {
                richTextBox2.Text += "解讀檔案\t" + filename + "\n";

                if (File.Exists(filename) == false)
                {
                    richTextBox1.Text += "檔案 " + filename + " 不存在，離開。\n";
                    //return false;
                }
                else
                {
                    richTextBox1.Text += "檔案 " + filename + " 存在, 開啟，並讀入文字資料\n";

                    string line;
                    StreamReader sr = new StreamReader(filename, Encoding.Default);

                    int i = 0;
                    while (!sr.EndOfStream)
                    {               // 每次讀取一行，直到檔尾
                        i++;
                        line = sr.ReadLine().Trim();            // 讀取文字到 line 變數

                        if (line.Length < 5)
                            continue;

                        //richTextBox1.Text += i.ToString() + "\t" + line + "\tlen = " + line.Length.ToString() + "\n";
                        all_strings.Add(line);
                    }

                    strings_count = all_strings.Count;
                    sr.Close();

                    richTextBox1.Text += "a可用行數 " + strings_count.ToString() + "\n";


                    for (i = 0; i < strings_count; i++)
                    {
                        richTextBox1.Text += all_strings[i] + "\n";
                    }
                }
            }
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            if (textBox1.Text.Length < 2)
                return;

            richTextBox2.Clear();
            int i;
            string pattern = textBox1.Text;

            for (i = 0; i < strings_count; i++)
            {
                //richTextBox1.Text += all_strings[i] + "\n";
                if (all_strings[i].Contains(pattern) == true)
                {
                    richTextBox2.Text += "符合條件\t" + all_strings[i] + "\n";
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (txtDirectory.Text == "")
            {
                folderBrowserDialog1.SelectedPath = "c:\\______test_files";  //預設開啟的路徑
            }
            else
            {
                folderBrowserDialog1.SelectedPath = txtDirectory.Text;  //預設開啟的路徑
            }

            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                txtDirectory.Text = folderBrowserDialog1.SelectedPath;
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
        }
    }
}

