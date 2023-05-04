using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// Download and unzip the DotNetZip library at: http://dotnetzip.codeplex.com/
// Add a reference to the Ionic.Zip.dll library.

using System.IO;
using Ionic.Zip;

namespace vcs_Zip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // Add the file to the archive.
            string filename_zip = Application.StartupPath + "\\zip_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".zip";
            string filename = @"C:\______test_files1\orient1.jpg";

            richTextBox1.Text += "原檔案 : " + filename + "\n";
            richTextBox1.Text += "壓縮檔 : " + filename_zip + "\n";

            try
            {
                using (ZipFile zip = new ZipFile(filename_zip))
                {
                    // Add the file to the Zip archive's root folder.

                    //zip.AddFile(filename, "/"); //直接壓縮
                    zip.AddFile(filename, "/lion-mouse"); //多一層子目錄

                    // Save the Zip file.
                    zip.Save();
                }

                // Display the file sizes.
                FileInfo old_fi = new FileInfo(filename);
                richTextBox1.Text += "原檔案大小 : " + old_fi.Length.ToString("#,#") + "\n";
                FileInfo new_fi = new FileInfo(filename_zip);
                richTextBox1.Text += "壓縮後大小 : " + new_fi.Length.ToString("#,#") + "\n";
                richTextBox1.Text += "壓縮完成\n";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error adding file to archive.\n" + ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename_zip = @"C:\______test_files1\peony2.zip";
            string extract_path = Application.StartupPath + "\\unzip_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");

            richTextBox1.Text += "壓縮檔 : " + filename_zip + "\n";
            richTextBox1.Text += "解壓縮路徑 : " + extract_path + "\n";

            try
            {
                using (ZipFile zip = ZipFile.Read(filename_zip))
                {
                    // Loop through the archive's files.
                    foreach (ZipEntry zip_entry in zip)
                    {
                        zip_entry.Extract(extract_path);
                    }
                }
                richTextBox1.Text += "解壓縮完成\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "解壓縮失敗, 原因 : " + ex.Message + "\n";
            }
        }
    }
}
