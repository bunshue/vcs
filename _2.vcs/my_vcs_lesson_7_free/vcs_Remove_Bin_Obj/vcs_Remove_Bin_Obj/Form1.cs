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
        List<string> filename_rename = new List<string>();  //宣告string型態的List
        string search_path = string.Empty;
        //string search_path = @"D:\_git\vcs\_2.vcs";
        string specified_search_path = String.Empty;

        int total_show_empty_folder_cnt = 0;
        int total_delete_empty_folder_cnt = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int x_st = 15;
            int y_st = 15;
            int dx = 230;
            int dy = 35;
            checkBox3.Location = new Point(x_st, y_st + dy * 0);
            checkBox1.Location = new Point(x_st, y_st + dy * 1);
            checkBox4.Location = new Point(x_st, y_st + dy * 2);
            checkBox2.Location = new Point(x_st, y_st + dy * 3);
            checkBox7.Location = new Point(x_st, y_st + dy * 4);
            checkBox8.Location = new Point(x_st, y_st + dy * 5);
            checkBox9.Location = new Point(x_st, y_st + dy * 6);
            checkBox10.Location = new Point(x_st, y_st + dy * 7);
            button1.Location = new Point(x_st, y_st + dy * 8);

            button2.Location = new Point(x_st, y_st + dy * 10);
            button3.Location = new Point(x_st, y_st + dy * 11 + 30);
            button4.Location = new Point(x_st + 115, y_st + dy * 10);
            bt_open_dir2.Location = new Point(x_st + 115 + 50, y_st + dy * 10 - 60);
            groupBox_remove.Location = new Point(x_st + 170, y_st + dy * 0);

            lb_main_mesg.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            listView1.Size = new Size(580, 550);
            listView1.Location = new Point(x_st + dx * 1 + 50, y_st + dy * 1);

            richTextBox1.Size = new Size(300, 550);
            richTextBox1.Location = new Point(x_st + dx * 1 + 630, y_st + dy * 1);

            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();

            this.Text = "目前位置 : " + currentPath;
            search_path = currentPath;
            specified_search_path = currentPath;
            lb_main_mesg.Text = "";

            this.Size = new Size(1200, 650);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            total_show_empty_folder_cnt = 0;
            total_delete_empty_folder_cnt = 0;
            lb_main_mesg.Text = "開始刪除檔案";
            this.Refresh();         //加上.Refresh()才可以讓人看清楚字的變化
            /*
            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前所在路徑: " + currentPath + "\n";

            //確認資料夾是否存在
            string Path = @"D:/_git/vcs/_1.data/______test_files2/aaaa/bbbb";
            if (Directory.Exists(Path) == false)    //確認資料夾是否存在
                richTextBox1.Text += "資料夾: " + Path + " 不存在\n";
            else
                richTextBox1.Text += "資料夾: " + Path + " 存在\n";
            */

            string path = string.Empty;

            if (rb_remove_vcs.Checked == true)
            {
                richTextBox1.Text += "清理 vcs\n";
                path = search_path;
            }
            else if (rb_remove_cuda.Checked == true)
            {
                richTextBox1.Text += "清理 CUDA\n";
                path = @"D:\_git\vcs\_3.cuda";
            }
            else if (rb_remove_opengl.Checked == true)
            {
                richTextBox1.Text += "清理 Open GL\n";
                path = @"D:\_git\vcs\_6.opengl";
            }
            else
            {
                path = search_path;
            }

            folder_name.Clear();

            richTextBox1.Text += "資料夾: " + path + "\n\n";
            if (Directory.Exists(path))
            {
                // This path is a directory
                ProcessDirectory(path);
            }

            ProcessDirectoryBinObj(folder_name);

            RemoveNeedlessFiles();

            if (checkBox9.Checked == true)
            {
                richTextBox1.Text += "共找到空資料夾 " + total_show_empty_folder_cnt.ToString() + " 個\n";
            }
            if (checkBox10.Checked == true)
            {
                richTextBox1.Text += "共刪除空資料夾 " + total_delete_empty_folder_cnt.ToString() + " 個\n";
            }
        }

        // Process all files in the directory passed in, recurse on any directories 
        // that are found, and process the files they contain.
        public void ProcessDirectory(string targetDirectory)
        {
            try
            {
                int file_cnt = 0;
                int dir_cnt = 0;

                // Process the list of files found in the directory.
                try
                {

                    string[] fileEntries = Directory.GetFiles(targetDirectory);
                    file_cnt = fileEntries.Length;
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
                    dir_cnt = subdirectoryEntries.Length;
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
                        else if (subdirectory.EndsWith("\\.vs"))
                        {
                            if (checkBox3.Checked == true)
                                richTextBox1.Text += subdirectory + "\n";
                            if (checkBox1.Checked == true)
                                folder_name.Add(subdirectory);
                        }
                        else if (subdirectory.EndsWith("\\x64"))
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
                        else if (subdirectory.EndsWith("\\Debug"))
                        {
                            if (checkBox3.Checked == true)
                                richTextBox1.Text += subdirectory + "\n";
                            if (checkBox1.Checked == true)
                                folder_name.Add(subdirectory);
                        }
                        DirectoryInfo di = new DirectoryInfo(subdirectory);
                        ProcessDirectory(subdirectory);
                    }
                }
                catch (UnauthorizedAccessException ex)
                {
                    richTextBox1.Text += ex.Message + "\n";
                }
                if ((file_cnt == 0) && (dir_cnt == 0))
                {
                    if (checkBox9.Checked == true)
                    {
                        richTextBox1.Text += targetDirectory + "是一個空資料夾\n";
                        total_show_empty_folder_cnt++;
                    }
                    if (checkBox10.Checked == true)
                    {
                        //richTextBox1.Text += "刪除 : " + targetDirectory + "是一個空資料夾\n";
                        Directory.Delete(targetDirectory, false);   //not recurrsive
                        richTextBox1.Text += "已刪除資料夾 : " + targetDirectory + "\n";
                        total_delete_empty_folder_cnt++;
                    }
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
                    else if ((folder_name[i].Contains("libemgucv")) && (!folder_name[i].Contains("Emgu.CV.Example")))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("References"))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("XXXXXXXXXXX"))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("_3.cuda"))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("GMap.NET.Core"))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("GMap.NET.WindowsForms"))
                    {
                        continue;
                    }
                }

                if (folder_name[i].Contains("obj"))
                {
                    //需要跳過的資料夾
                    if (folder_name[i].Contains("GMap.NET.Core"))
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("GMap.NET.WindowsForms"))
                    {
                        continue;
                    }
                }

                if (folder_name[i].Contains("\\.vs"))
                {
                    //需要跳過的資料夾
                    if (folder_name[i].Contains("_3.cuda") == true)
                    {
                        richTextBox1.Text += "跳過......\n";
                        //continue;
                    }
                }

                if (folder_name[i].Contains("x64"))
                {
                    //需要跳過的資料夾
                    if (folder_name[i].Contains("Common") == true)
                    {
                        continue;
                    }
                    else if (folder_name[i].Contains("References") == true)
                    {
                        continue;
                    }
                }

                if (folder_name[i].Contains("tmptmptmptmp"))
                {
                    continue;
                }

                //richTextBox1.Text += "刪除 : " + folder_name[i] + "\n";

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

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "檔名簡中轉正中\nTBD";
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        void RemoveNeedlessFiles()
        {
            string foldername = string.Empty;
            string[] filenames;

            foldername = @"D:\_git\vcs\_3.cuda\_code\bin\win64\Debug";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + foldername + " 存在\n";

                filenames = Directory.GetFiles(foldername); //獲得文件夾目錄下所有文件全路徑
                foreach (string filename in filenames)
                {
                    if ((filename.Contains("freeglut.dll") == false) && (filename.Contains("glew64.dll") == false))
                    {
                        richTextBox1.Text += "remove : " + filename + "\n";
                        if (File.Exists(filename))  //確認檔案是否存在
                        {
                            try
                            {
                                File.Delete(filename);
                                richTextBox1.Text += "已刪除檔案" + filename + "\n";
                            }
                            catch
                            {
                                richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                            }
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_3.cuda\bin\win64\Debug";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + foldername + " 存在\n";

                filenames = Directory.GetFiles(foldername); //獲得文件夾目錄下所有文件全路徑
                foreach (string filename in filenames)
                {
                    if ((filename.Contains("freeglut.dll") == false) && (filename.Contains("glew64.dll") == false))
                    {
                        richTextBox1.Text += "remove : " + filename + "\n";
                        if (File.Exists(filename))  //確認檔案是否存在
                        {
                            try
                            {
                                File.Delete(filename);
                                richTextBox1.Text += "已刪除檔案" + filename + "\n";
                            }
                            catch
                            {
                                richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                            }
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_6.opengl\bin_debug64";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + foldername + " 存在\n";

                filenames = Directory.GetFiles(foldername); //獲得文件夾目錄下所有文件全路徑
                foreach (string filename in filenames)
                {
                    if ((filename.Contains("freeglut.dll") == false) && (filename.Contains("glew64.dll") == false))
                    {
                        richTextBox1.Text += "remove : " + filename + "\n";
                        if (File.Exists(filename))  //確認檔案是否存在
                        {
                            try
                            {
                                File.Delete(filename);
                                richTextBox1.Text += "已刪除檔案" + filename + "\n";
                            }
                            catch
                            {
                                richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                            }
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_d_emgu\libemgucv-windows-x64-2.3.0.1416\bin";
            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + foldername + " 存在\n";

                //filenames = Directory.GetFiles(foldername); //獲得文件夾目錄下所有文件全路徑
                filenames = Directory.GetFiles(foldername, "*.exe"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("Example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.pdb"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.manifest"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.txt"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.config"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.jpg"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_d_emgu\libemgucv-windows-x86-2.3.0.1416\bin";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                richTextBox1.Text += "資料夾: " + foldername + " 存在\n";

                //filenames = Directory.GetFiles(foldername); //獲得文件夾目錄下所有文件全路徑
                filenames = Directory.GetFiles(foldername, "*.exe"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("Example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.pdb"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.manifest"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.txt"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }


                filenames = Directory.GetFiles(foldername, "*.config"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.jpg"); //獲得文件夾目錄下指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    richTextBox1.Text += "remove : " + filename + "\n";

                    if (filename.Contains("opencv"))
                        continue;
                    if (filename.Contains("example."))
                        continue;
                    if (filename.Contains("cvextern_test"))
                        continue;

                    if (File.Exists(filename))  //確認檔案是否存在
                    {
                        try
                        {
                            File.Delete(filename);
                            richTextBox1.Text += "已刪除檔案" + filename + "\n";
                        }
                        catch
                        {
                            richTextBox1.Text += "無法刪除檔案" + filename + "\n";
                        }
                    }
                }
            }

            string[] delete_filenames = {
            @"D:\_git\vcs\_3.cuda\_code\a\a.exe",
            @"D:\_git\vcs\_3.cuda\_code\a\a.exp",
            @"D:\_git\vcs\_3.cuda\_code\a\a.lib",
            @"C"};

            foreach (string filename in delete_filenames)
            {
                if (File.Exists(filename))  //確認檔案是否存在
                {
                    try
                    {
                        File.Delete(filename);
                        richTextBox1.Text += "已刪除檔案" + delete_filenames + "\n";
                    }
                    catch
                    {
                        richTextBox1.Text += "無法刪除檔案" + delete_filenames + "\n";
                    }
                }
            }
        }

        private void bt_open_dir2_Click(object sender, EventArgs e)
        {
            int cnt = listView1.SelectedItems.Count;
            if (cnt > 0)
            {
                int selNdx = listView1.SelectedIndices[0];
            }
            else
            {
                richTextBox1.Text += "尚未選擇\n";
            }
        }
    }
}
