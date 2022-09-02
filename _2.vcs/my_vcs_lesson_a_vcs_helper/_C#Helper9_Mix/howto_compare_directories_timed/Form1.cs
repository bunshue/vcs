using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;

namespace howto_compare_directories_timed
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCompare_Click(object sender, EventArgs e)
        {
            Cursor = Cursors.WaitCursor;

            txtGetFilesTime.Clear();
            txtLinqTwiceTime.Clear();
            txtLinqJoinsTime.Clear();
            txtGetFilesTime.Refresh();
            txtLinqTwiceTime.Refresh();
            txtLinqJoinsTime.Refresh();

            string dir1 = txtDir1.Text;
            if (!dir1.EndsWith("\\")) dir1 += "\\";
            string dir2 = txtDir2.Text;
            if (!dir2.EndsWith("\\")) dir2 += "\\";

            int num_trials = 10;

            Stopwatch stopwatch = new Stopwatch();

            stopwatch.Start();
            for (int i = 0; i < num_trials; i++) Compare_GetFiles(dir1, dir2);
            stopwatch.Stop();
            txtGetFilesTime.Text = stopwatch.Elapsed.TotalSeconds.ToString("0.00");
            txtGetFilesTime.Refresh();

            stopwatch.Reset();
            stopwatch.Start();
            for (int i = 0; i < num_trials; i++) Compare_LinqTwice(dir1, dir2);
            stopwatch.Stop();
            txtLinqTwiceTime.Text = stopwatch.Elapsed.TotalSeconds.ToString("0.00");
            txtLinqTwiceTime.Refresh();

            stopwatch.Reset();
            stopwatch.Start();
            for (int i = 0; i < num_trials; i++) Compare_LinqJoins(dir1, dir2);
            stopwatch.Stop();
            txtLinqJoinsTime.Text = stopwatch.Elapsed.TotalSeconds.ToString("0.00");
            txtLinqJoinsTime.Refresh();

            Cursor = Cursors.Default;
        }

        // Use Directory.GetFiles to compare the files in each directory.
        private void Compare_GetFiles(string dir1, string dir2)
        {
            // Get sorted lists of files in the directories.
            string[] file_names1 = Directory.GetFiles(dir1);
            for (int i = 0; i < file_names1.Length; i++)
            {
                file_names1[i] = file_names1[i].Replace(dir1, "");
            }
            Array.Sort(file_names1);

            string[] file_names2 = Directory.GetFiles(dir2);
            for (int i = 0; i < file_names2.Length; i++)
            {
                file_names2[i] = file_names2[i].Replace(dir2, "");
            }
            Array.Sort(file_names2);

            // Compare.
            int i1 = 0, i2 = 0;
            List<string> dir1_only = new List<string>();
            List<string> dir2_only = new List<string>();
            List<string> both = new List<string>();
            while ((i1 < file_names1.Length) && (i2 < file_names2.Length))
            {
                if (file_names1[i1] == file_names2[i2])
                {
                    // They match. Display them both.
                    both.Add(file_names1[i1]);
                    i1++;
                    i2++;
                }
                else if (file_names1[i1].CompareTo(file_names2[i2]) < 0)
                {
                    // Display the directory 1 file.
                    dir1_only.Add(file_names1[i1]);
                    i1++;
                }
                else
                {
                    // Display the directory 2 file.
                    dir2_only.Add(file_names1[i2]);
                    i2++;
                }
            }

            // Display remaining directory 1 files.
            for (int i = i1; i < file_names1.Length; i++)
            {
                dir1_only.Add(file_names1[i]);
            }

            // Display remaining directory 2 files.
            for (int i = i2; i < file_names2.Length; i++)
            {
                dir2_only.Add(file_names1[i]);
            }
        }

        // Use LINQ twice to compare the files in each directory.
        private void Compare_LinqTwice(string dir1, string dir2)
        {
            // Get sorted lists of files in the directories.
            DirectoryInfo dir1_info = new DirectoryInfo(dir1);
            var dir1_query =
                from FileInfo file_info in dir1_info.GetFiles()
                orderby file_info.Name
                select file_info.Name;
            string[] file_names1 = dir1_query.ToArray();

            DirectoryInfo dir2_info = new DirectoryInfo(dir2);
            var dir2_query =
                from FileInfo file_info in dir2_info.GetFiles()
                orderby file_info.Name
                select file_info.Name;
            string[] file_names2 = dir2_query.ToArray();

            // Compare.
            int i1 = 0, i2 = 0;
            List<string> dir1_only = new List<string>();
            List<string> dir2_only = new List<string>();
            List<string> both = new List<string>();
            while ((i1 < file_names1.Length) && (i2 < file_names2.Length))
            {
                if (file_names1[i1] == file_names2[i2])
                {
                    // They match. Display them both.
                    both.Add(file_names1[i1]);
                    i1++;
                    i2++;
                }
                else if (file_names1[i1].CompareTo(file_names2[i2]) < 0)
                {
                    // Display the directory 1 file.
                    dir1_only.Add(file_names1[i1]);
                    i1++;
                }
                else
                {
                    // Display the directory 2 file.
                    dir2_only.Add(file_names1[i2]);
                    i2++;
                }
            }

            // Display remaining directory 1 files.
            for (int i = i1; i < file_names1.Length; i++)
            {
                dir1_only.Add(file_names1[i]);
            }

            // Display remaining directory 2 files.
            for (int i = i2; i < file_names2.Length; i++)
            {
                dir2_only.Add(file_names1[i]);
            }
        }

        // Use LINQ joins to compare the files in each directory.
        private void Compare_LinqJoins(string dir1, string dir2)
        {
            // Get sorted lists of files in the directories.
            DirectoryInfo dir1_info = new DirectoryInfo(dir1);
            var dir1_query =
                from FileInfo file_info in dir1_info.GetFiles()
                //orderby file_info.Name
                select file_info.Name;
            string[] file_names1 = dir1_query.ToArray();

            DirectoryInfo dir2_info = new DirectoryInfo(dir2);
            var dir2_query =
                from FileInfo file_info in dir2_info.GetFiles()
                //orderby file_info.Name
                select file_info.Name;
            string[] file_names2 = dir2_query.ToArray();

            // Compare.
            var dir1_only_query =
                from string file_name in file_names1
                where (!file_names2.Contains(file_name))
                select file_name;
            List<string> dir1_only = dir1_only_query.ToList();

            var dir2_only_query =
                from string file_name in file_names2
                where (!file_names1.Contains(file_name))
                select file_name;
            List<string> dir2_only = dir2_only_query.ToList();

            var both_query =
                from string file_name in file_names1
                where (file_names2.Contains(file_name))
                select file_name;
            List<string> both = both_query.ToList();
        }
    }
}
