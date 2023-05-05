using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.IO;

// Use NuGet Manager to install System.IO.Compression.
// Add references to:
//      System.IO.Compression
//      System.IO.Compression.FileSystem

using System.IO.Compression;

namespace vcs_ReadWrite_Zip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //���Y�ɮ�

            List<String> filenames = new List<String>();

            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\picture2.jpg";
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            string filename4 = @"C:\_git\vcs\_1.data\______test_files1\bear.jpg";

            filenames.Clear();
            filenames.Add(filename1);
            filenames.Add(filename2);
            filenames.Add(filename3);
            filenames.Add(filename4);

            string zip_filename = Application.StartupPath + "\\Zip_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".zip";

            // Create the Zip archive for update.
            using (ZipArchive archive = ZipFile.Open(zip_filename, ZipArchiveMode.Update))
            {
                // Add the files to the archive.
                foreach (string filename in filenames)
                {
                    FileInfo file_info = new FileInfo(filename);

                    // Make an entry name for the file.
                    string entry_name = file_info.Name;
                    for (int version = 1; version < 10000; version++)
                    {
                        ZipArchiveEntry old_entry = archive.GetEntry(entry_name);
                        if (old_entry == null) break;
                        entry_name = Path.GetFileNameWithoutExtension(file_info.Name) + file_info.Extension;
                    }

                    // Add the file to this entry.
                    archive.CreateEntryFromFile(filename, entry_name);
                    richTextBox1.Text += "filename = " + filename + "\n";
                    richTextBox1.Text += "entry_name = " + entry_name + "\n";
                }
                richTextBox1.Text += "zip_file_name = " + zip_filename + "\n";
                richTextBox1.Text += "Done\n";
            }
        }
    }
}
