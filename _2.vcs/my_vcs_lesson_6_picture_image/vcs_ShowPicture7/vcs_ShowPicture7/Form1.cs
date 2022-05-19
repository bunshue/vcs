using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ShowPicture7
{
    public partial class Form1 : Form
    {
        bool debug_mode = false;

        //string foldername = @"C:\______test_files\__pic\_peony1";
        string foldername = @"C:\______test_files\__pic\_MU";

        // The list of files we will pick from.
        private List<string> FileNames = new List<string>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (Directory.Exists(foldername) == false)
            {
                richTextBox1.Text += "圖片資料夾不存在, 離開\n";
                return;
            }

            //this.WindowState = FormWindowState.Maximized;

            // Load the list of files.
            FileNames = FindFiles(foldername, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);

            for (int i = 0; i < FileNames.Count; i++)
            {
                richTextBox1.Text += "get file \t" + FileNames[i] + "\n";
            }
            richTextBox1.Text += "共有 " + FileNames.Count.ToString() + " 個檔案\n";

            show_item_location();
            this.TopMost = true;
        }

        // See: Search for files that match multiple patterns in C#
        //      http://csharphelper.com/blog/2015/06/find-files-that-match-multiple-patterns-in-c/
        // Search for files matching the patterns.
        private List<string> FindFiles(string fname, string patterns, bool search_subdirectories)
        {
            // Make the result list.
            List<string> files = new List<string>();

            // Get the patterns.
            string[] pattern_array = patterns.Split(';');

            // Search.
            SearchOption search_option = SearchOption.TopDirectoryOnly;
            if (search_subdirectories) search_option = SearchOption.AllDirectories;
            foreach (string pattern in pattern_array)
            {
                foreach (string filename in Directory.GetFiles(fname, pattern, search_option))
                {
                    if (!files.Contains(filename)) files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }

        void show_item_location()
        {
            this.Location = new Point(0, 50);
            if (debug_mode == false)
            {
                this.Size = new Size(200, 280);
                richTextBox1.Visible = false;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int len = FileNames.Count;
            if (len <= 0)
            {
                richTextBox1.Text += "無圖片, 離開\n";
                return;
            }

            Random r = new Random();
            int selected_index = r.Next(len);

            //string filename = @"C:\______test_files\picture1.jpg";
            string filename = FileNames[selected_index];
            Form2 f2 = new Form2(filename);
            f2.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int len = FileNames.Count;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + FileNames[i] + "\n";

            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            int cnt = 50;
            int i;
            for (i = 0; i < cnt; i++)
            {
                button1_Click(sender, e);
                Application.DoEvents();
                System.Threading.Thread.Sleep(50);


            }
        }
    }
}

