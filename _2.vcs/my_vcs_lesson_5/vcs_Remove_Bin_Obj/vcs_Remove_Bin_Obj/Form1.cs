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
        List<string> folder_name = new List<string>();      //宣告string型態的List
        List<string> filename_backup = new List<string>();  //宣告string型態的List
        string search_path = string.Empty;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();

            label1.Text = "目前位置 : " + currentPath;
            //richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";
            search_path = currentPath;
            lb_main_mesg.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "開始刪除檔案";
            this.Refresh();         //加上.Refresh()才可以讓人看清楚字的變化
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

            //string path = @"C:\_git\vcs\_2.vcs";
            //string path = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw";
            string path = search_path;

            folder_name.Clear();

            richTextBox1.Text += "資料夾: " + path + "\n\n";
            if (Directory.Exists(path))
            {
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
                        if ((fileName.EndsWith(".suo")) || (fileName.EndsWith(".csproj.user")))
                        {
                            if (checkBox4.Checked == true)
                            {
                                richTextBox1.Text += fileName + "\n";   //僅顯示
                            }
                            if (checkBox2.Checked == true)
                            {
                                folder_name.Add(fileName);              //加入刪除準備
                            }
                        }
                        if ((fileName.EndsWith("UpgradeLog.XML")) || (fileName.EndsWith("UpgradeLog.XML")))
                        {
                            if (checkBox7.Checked == true)
                            {
                                richTextBox1.Text += fileName + "\n";   //僅顯示
                            }
                            if (checkBox8.Checked == true)
                            {
                                folder_name.Add(fileName);              //加入刪除準備
                            }
                        }
                    }

                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    Array.Sort(subdirectoryEntries);
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        //richTextBox1.Text += "subdirectory = " + subdirectory + "\n";

                        if (subdirectory.EndsWith("\\bin"))
                        {
                            if (checkBox3.Checked == true)
                                richTextBox1.Text += subdirectory + "\n";
                            if (checkBox1.Checked == true)
                                folder_name.Add(subdirectory);
                        }
                        else if (subdirectory.EndsWith("\\obj"))
                        {
                            if (checkBox3.Checked == true)
                                richTextBox1.Text += subdirectory + "\n";
                            if (checkBox1.Checked == true)
                                folder_name.Add(subdirectory);
                        }
                        else if ((subdirectory.EndsWith("\\_UpgradeReport_Files")) || (subdirectory.EndsWith("Backup")))
                        {
                            if (checkBox7.Checked == true)
                                richTextBox1.Text += subdirectory + "\n";   //僅顯示
                            if (checkBox8.Checked == true)
                                folder_name.Add(subdirectory);              //加入刪除準備
                        }
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
            bool flag_rename_fail = false;
            int i;
            int len;
            len = folder_name.Count;
            richTextBox1.Text += "欲刪除個數 : " + len + "\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "資料夾 : " + folder_name[i] + "\n";

                if (folder_name[i].Contains("bin"))
                {
                    //需要跳過的資料夾
                    if (folder_name[i].Contains("xxxxxxxxxxxxxxxx"))
                    {
                        richTextBox1.Text += "iiiiiiiiiiiiiiiiiiiii\n";
                        continue;
                    }
                    else if (folder_name[i].Contains("vcs_programming"))
                    {
                        continue;
                    }
                    else if ((folder_name[i].Contains("libemgucv")) && (!folder_name[i].Contains("Emgu.CV.Example")))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("XXXXXXXXXXX"))
                    {
                        continue;
                    }
                }

                if (folder_name[i].Contains("tmptmptmptmp"))
                {
                    continue;
                }

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
                        flag_rename_fail = true;
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
                        flag_rename_fail = true;
                    }
                }
                else
                {
                    richTextBox1.Text += "資料夾或檔案: " + folder_name[i] + " 不存在，不能刪除\n";
                    flag_rename_fail = true;
                }
            }
            lb_main_mesg.Text = "欲刪除個數 : " + len + ", 完成";
            if (flag_rename_fail == true)
                lb_main_mesg.Text += "\t有錯誤";
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessRenameDirectory(string targetDirectory)
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
                        if (fileName.EndsWith(" 的副本"))
                        {
                            if (checkBox5.Checked == true)
                                richTextBox1.Text += fileName + "\n";
                            if (checkBox6.Checked == true)
                                filename_backup.Add(fileName);
                        }
                    }

                    // Recurse into subdirectories of this directory.
                    string[] subdirectoryEntries = Directory.GetDirectories(targetDirectory);
                    Array.Sort(subdirectoryEntries);
                    foreach (string subdirectory in subdirectoryEntries)
                    {
                        //richTextBox1.Text += "subdirectory = " + subdirectory + "\n";
                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        ProcessRenameDirectory(subdirectory);
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

        public void ProcessRenameBackup(List<string> filename_backup)
        {
            bool flag_rename_fail = false;
            int i;
            int len;
            len = filename_backup.Count;
            richTextBox1.Text += "欲更名個數 : " + len + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "檔案 : " + filename_backup[i] + "\n";


                richTextBox1.Text += "new 檔案 : " + filename_backup[i].Replace(" 的副本", "") + "\n";

                //if (!File.Exists(Path.Combine(dir, f.ToString().Replace("(", "").Replace(")", "")         )))


                if (File.Exists(filename_backup[i]))     //確認檔案是否存在
                {

                    string sourceFileName = filename_backup[i];
                    string destFileName = filename_backup[i].Replace(" 的副本", "");

                    //移動檔案，從 sourceFileName 移動到 destFileName
                    if (File.Exists(sourceFileName))        //確認原始檔案是否存在
                    {
                        if (!File.Exists(destFileName))     //確認目標檔案是否存在
                        {
                            File.Move(sourceFileName, destFileName);
                            richTextBox1.Text += "已移動檔案: " + sourceFileName + " 到 " + destFileName + "\n";
                        }
                        else
                        {
                            richTextBox1.Text += "檔案: " + destFileName + " 已存在，無法移動\n";
                            flag_rename_fail = true;
                        }
                    }
                    else
                    {
                        richTextBox1.Text += "檔案: " + sourceFileName + " 不存在，無法移動\n";
                        flag_rename_fail = true;
                    }

                }
                else
                {
                    richTextBox1.Text += "資料夾或檔案: " + filename_backup[i] + " 不存在，不能刪除\n";
                    flag_rename_fail = true;
                }
            }

            lb_main_mesg.Text = "更名個數 : " + len + ", 完成";
            if (flag_rename_fail == true)
                lb_main_mesg.Text += "\t有錯誤";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            lb_main_mesg.Text = "開始改名檔案";
            this.Refresh();         //加上.Refresh()才可以讓人看清楚字的變化
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

            //string path = @"C:\_git\vcs\_2.vcs";
            //string path = @"C:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw";
            string path = search_path;

            filename_backup.Clear();

            richTextBox1.Text += "資料夾: " + path + "\n\n";
            if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessRenameDirectory(path);
            }

            ProcessRenameBackup(filename_backup);

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }






    }
}
