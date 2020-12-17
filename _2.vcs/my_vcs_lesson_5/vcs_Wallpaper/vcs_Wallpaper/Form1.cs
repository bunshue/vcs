using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.IO;
using System.Drawing.Imaging;

namespace vcs_Wallpaper
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool SystemParametersInfo(uint uiAction, uint uiParam, String pvParam, uint fWinIni);

        private const uint SPI_SETDESKWALLPAPER = 0x14;
        private const uint SPIF_UPDATEINIFILE = 0x1;
        private const uint SPIF_SENDWININICHANGE = 0x2;

        public Form1()
        {
            InitializeComponent();
        }

        string dir_name = @"C:\______test_files\peony";

        // The list of files we will pick from.
        private List<string> FileNames = new List<string>();

        private void Form1_Load(object sender, EventArgs e)
        {
            // Load the list of files.
            if (Directory.Exists(dir_name))
                FileNames = FindFiles(dir_name, "*.bmp;*.png;*.jpg;*.tif;*.gif", false);
            else
                FileNames = new List<string>();

            for (int i = 0; i < FileNames.Count; i++)
                richTextBox1.Text += "get file \t" + FileNames[i] + "\n";

            // Display the first picture.
            ChangeDesktopPicture();
        }

        // See: Search for files that match multiple patterns in C#
        //      http://csharphelper.com/blog/2015/06/find-files-that-match-multiple-patterns-in-c/
        // Search for files matching the patterns.
        private List<string> FindFiles(string dir_name, string patterns, bool search_subdirectories)
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
                foreach (string filename in Directory.GetFiles(dir_name, pattern, search_option))
                {
                    if (!files.Contains(filename)) files.Add(filename);
                }
            }

            // Sort.
            files.Sort();

            // Return the result.
            return files;
        }

        // Display a random image.
        private Random Rand = new Random();

        private void timer1_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定桌面圖片\t" + DateTime.Now.ToString() + "\n";
            ChangeDesktopPicture();
        }


        // Display a random image.
        private void ChangeDesktopPicture()
        {
            // Repeat until we succeed or run out of files.
            for (; ; )
            {
                // Pick a random image.
                int file_num = Rand.Next(FileNames.Count);

                // Try to use that image.
                try
                {
                    // Set the desktop picture.
                    DisplayPicture(FileNames[file_num], checkBox1.Checked);
                    break;
                }
                catch
                {
                    // This file doesn't work. Remove it from the list.
                    FileNames.RemoveAt(file_num);

                    // If there are no more files, stop trying.
                    if (FileNames.Count == 0)
                    {
                        timer1.Enabled = false;
                        break;
                    }
                }
            }
        }

        // Display the file on the desktop.
        private void DisplayPicture(string file_name, bool update_registry)
        {
            try
            {
                // If we should update the registry,
                // set the appropriate flags.
                uint flags = 0;
                if (update_registry)
                    flags = SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE;

                // Set the desktop background to this file.
                if (!SystemParametersInfo(SPI_SETDESKWALLPAPER,
                    0, file_name, flags))
                {
                    MessageBox.Show("SystemParametersInfo failed.",
                        "Error", MessageBoxButtons.OK,
                        MessageBoxIcon.Exclamation);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error displaying picture " +
                    file_name + ".\n" + ex.Message,
                    "Error", MessageBoxButtons.OK,
                    MessageBoxIcon.Exclamation);
            }
        }


    }
}
