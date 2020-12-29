using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for SearchOption

namespace WindowsFormsApplication1aaa
{
    public partial class Form1 : Form
    {
        string directory = @"C:\______test_files\__test_directory_to_grayscale";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            txtDirectory.Text = @"C:\______test_files\_case1";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SearchOption search_option;
            search_option = SearchOption.TopDirectoryOnly;
            // Look for graphic files.
            string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(directory, pattern, search_option))
                {
                    richTextBox1.Text += "find file : " + filename + "\n";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SearchOption search_option;
            search_option = SearchOption.AllDirectories;
            // Look for graphic files.
            string[] patterns = { "*.png", "*.bmp", "*.jpg", "*.jpeg", "*.gif" };
            foreach (string pattern in patterns)
            {
                // Find the matching files.
                foreach (string filename in Directory.GetFiles(directory, pattern, search_option))
                {
                    richTextBox1.Text += "find file : " + filename + "\n";
                }
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        //搜尋檔案內的文字
        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            DirectoryInfo dir_info = new DirectoryInfo(txtDirectory.Text);

            ListFiles(cboPattern.Text, dir_info, txtTarget.Text);
        }

        // Add the files in this directory's subtree 
        // that match the pattern to the ListBox.
        private void ListFiles(string pattern, DirectoryInfo dir_info, string target)
        {
            // Get the files in this directory.
            FileInfo[] fs_infos = dir_info.GetFiles(pattern);
            foreach (FileInfo fs_info in fs_infos)
            {
                if (target.Length == 0)
                {
                    richTextBox1.Text += fs_info.FullName + "\n";
                }
                else
                {
                    string txt = File.ReadAllText(fs_info.FullName);
                    if (txt.IndexOf(target, StringComparison.OrdinalIgnoreCase) >= 0)
                    {
                        richTextBox1.Text += fs_info.FullName + "\n";
                    }
                }
            }

            // Search subdirectories.
            DirectoryInfo[] subdirs = dir_info.GetDirectories();
            foreach (DirectoryInfo subdir in subdirs)
            {
                ListFiles(pattern, subdir, target);
            }
        }







    }
}
