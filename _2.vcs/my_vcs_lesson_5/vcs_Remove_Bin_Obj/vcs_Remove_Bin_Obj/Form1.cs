using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

namespace vcs_Remove_Bin_Obj
{
    public partial class Form1 : Form
    {
        List<string> folder_name = new List<string>();   //宣告string型態的List

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";



            //確認資料夾是否存在
            string Path = "C:\\______test_files_file_name2\\aaaa\\bbbb";
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
                richTextBox1.Text += "資料夾: " + Path + " 不存在\n";
            else
                richTextBox1.Text += "資料夾: " + Path + " 存在\n";
            */

            //string path = @"c:\______test_files";
            //string path = @"D:\___source_code\_git\part1\vcs\_2.vcs\my_vcs_lesson_6_draw";

            //string path = @"C:\_git\vcs\_2.vcs";
            string path = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw";

            folder_name.Clear();

            richTextBox1.Text += "資料夾: " + path + "\n\n";

            richTextBox1.Text += "資料夾: " + path + "\n\n";
            if (Directory.Exists(path))
            {
                richTextBox1.Text += "path = " + path + "\n";
                // This path is a directory
                ProcessDirectory(path);
            }
            
            
            ProcessDirectoryBinObj(folder_name);
        }


        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
            try
            {
                // Process the list of files found in the directory.
                try
                {
                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    Array.Sort(fileEntries);
                    foreach (string fileName in fileEntries)
                    {
                        if (fileName.EndsWith(".suo"))
                            folder_name.Add(fileName);
                    }


                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    Array.Sort(subdirectoryEntries);
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        //richTextBox1.Text += "subdirectory = " + subdirectory + "\n";
                        if (subdirectory.EndsWith("\\bin"))
                            folder_name.Add(subdirectory);
                        else if (subdirectory.EndsWith("\\obj"))
                            folder_name.Add(subdirectory);
                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        ProcessDirectory(subdirectory);
                    }
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
            }
            catch (IOException e)
            {
                richTextBox1.Text += "IOException, " + e.GetType().Name + "\n";
            }
        }


        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectoryBinObj(List<string> folder_name)
        {
            int i;
            int len;
            len = folder_name.Count;
            richTextBox1.Text += "len = " + len + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "subdirectory = " + folder_name[i] + "\n";

                if (Directory.Exists(folder_name[i]))     //確認資料夾是否存在
                {
                    try
                    {
                        Directory.Delete(folder_name[i], true);   //recurrsive
                        //Directory.Delete(folder_name[i], false);   //not recurrsive
                        richTextBox1.Text += "已刪除資料夾" + folder_name[i] + "\n";
                    }
                    catch
                    {
                        richTextBox1.Text += "無法刪除資料夾" + folder_name[i] + "\n";
                    }
                }
                else if (File.Exists(folder_name[i]))     //確認檔案是否存在
                {
                    try
                    {
                        File.Delete(folder_name[i]);
                        richTextBox1.Text += "已刪除檔案" + folder_name[i] + "\n";
                    }
                    catch
                    {
                        richTextBox1.Text += "無法刪除檔案" + folder_name[i] + "\n";
                    }
                }
                else
                {
                    richTextBox1.Text += "資料夾或檔案: " + folder_name[i] + " 不存在，不能刪除\n";
                }




            }



        }








    }
}
