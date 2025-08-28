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

            groupBox_replace.Size = new Size(550, 170);
            groupBox_replace.Location = new Point(x_st + dx * 0, y_st + dy * 17 - 10);
            tb_string_old.Size = new Size(350, 30);
            tb_string_new.Size = new Size(350, 30);

            x_st = 10;
            y_st = 20;
            dx = 70;
            dy = 40;
            lb_string_old.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 5);
            lb_string_new.Location = new Point(x_st + dx * 0, y_st + dy * 1 + 5);
            tb_string_old.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            tb_string_new.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_replace.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            cb_confirm.Location = new Point(x_st + dx * 1 + 40, y_st + dy * 2 + 10);
            bt_open_dir.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 2);
            lb_path.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 8);
            int dd = 20;
            dy = 30;
            rb_file_type0.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 0);
            rb_file_type1.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 1);
            rb_file_type2.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 2);
            rb_file_type3.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 3);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();

            this.Text = "目前位置 : " + currentPath;
            search_path = currentPath;
            specified_search_path = currentPath;
            lb_path.Text = search_path;
            lb_main_mesg.Text = "";

            this.Size = new Size(1200, 820);

            tb_string_old.Text = @"D:/_git/vcs/_1.data/______test_files2";
            tb_string_new.Text = @"D:/_git/vcs/_1.data/______test_files1/";
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

        private void bt_replace_Click(object sender, EventArgs e)
        {
            bool flag_really_replace = cb_confirm.Checked;
            richTextBox1.Text += "是否置換 : " + flag_really_replace.ToString() + "\n";
            string string_old = tb_string_old.Text;
            string string_new = tb_string_new.Text;
            if (string_old == "")
            {
                richTextBox1.Text += "無原字串, 不可置換, 離開\n";
                return;
            }
            if (string_new == "")
            {
                richTextBox1.Text += "無新字串, 不可置換, 離開\n";
                return;
            }
            richTextBox1.Text += "原字串 : " + string_old + "\n";
            richTextBox1.Text += "新字串 : " + string_new + "\n";

            string extension = ".cs";

            if (rb_file_type0.Checked == true)
            {
                richTextBox1.Text += "置換 vcs 檔案\n";
                extension = ".cs";
            }
            else if (rb_file_type1.Checked == true)
            {
                richTextBox1.Text += "置換 C/C++ 檔案\n";
                extension = ".cpp";
            }
            else if (rb_file_type2.Checked == true)
            {
                richTextBox1.Text += "置換 Python 檔案\n";
                extension = ".py";
            }
            else if (rb_file_type3.Checked == true)
            {
                richTextBox1.Text += "置換 任意 檔案\n";
                extension = ".*";
            }
            else
            {
                richTextBox1.Text += "未選定檔案格式, 不可置換, 離開\n";
                return;
            }

            //資料夾內 檔案置換文字

            //撈出所有圖片檔 並存成一個List
            string foldername = specified_search_path;
            if (foldername == "")
            {
                richTextBox1.Text += "無置換路徑, 離開\n";
                return;
            }
            richTextBox1.Text += "置換路徑 : " + foldername + "\n";

            filenames.Clear();

            GetAllFiles(foldername, extension);
            int len = filenames.Count;
            richTextBox1.Text += "找到檔案個數 : " + len.ToString() + "\n";

            //private Icon icon1 = new Icon(@"D:/_git/vcs/_1.data/______test_files1/_icon/快.ico");
            string pattern1 = string_old;
            string pattern2 = string_new;

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";

                int flag_replace_pattern = 0;
                flag_replace_pattern = file_replace_pattern(filenames[i], pattern1, pattern2);
            }
        }

        int file_replace_pattern(string filename1, string pattern1, string pattern2)
        {
            bool flag_need_replace = false;

            if (File.Exists(filename1) == false)
            {
                richTextBox1.Text += "檔案 : " + filename1 + ", 不存在\n";
                return 1;   //1: 原始檔案不存在
            }

            string filename2 = filename1 + ".tmp";

            //從文字檔讀出
            StreamReader sr = new StreamReader(filename1); // 開啟檔案

            string str;  // 宣告字串變數

            str = sr.ReadLine(); // 讀出一行
            while (str != null)
            {
                //richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號

                if (str.Contains(pattern1))
                {
                    //richTextBox2.Text += "有找到pattern, 要置換pattern\n";
                    //richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
                    flag_need_replace = true;
                    break;

                }
                str = sr.ReadLine();
            }
            sr.Close(); // 關閉檔案

            if (flag_need_replace == false)
            {
                //richTextBox2.Text += "沒有找到pattern, 不用置換pattern\n";
                return 2;   //2: 沒有找到pattern, 不用置換pattern
            }
            else
            {
                //richTextBox2.Text += "有找到pattern, 要置換pattern\n";
            }

            if (File.Exists(filename2) == true)
            {
                //richTextBox2.Text += "delete filename2\n";
                File.Delete(filename2);
            }

            sr = new StreamReader(filename1); // 開啟檔案
            StreamWriter sw = new StreamWriter(filename2); // true 是資料可附加至檔案, open write
            //StreamWriter sw = new StreamWriter(filename2, true); // true 是資料可附加至檔案 open write append

            str = sr.ReadLine(); // 讀出一行
            while (str != null)
            {
                if (str.Contains(pattern1))
                {
                    //richTextBox2.Text += "replace\n";
                    str = str.Replace(pattern1, pattern2);
                }

                sw.WriteLine(str); // 寫入一行

                str = sr.ReadLine();
            }
            sr.Close(); // 關閉檔案
            sw.Close(); // 關閉檔案


            if (File.Exists(filename1) == true)
            {
                File.Delete(filename1);
            }
            File.Move(filename2, filename1);
            return 0;   //置換成功
        }



        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername, string extension)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName, extension);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == extension)
                    {
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        //richTextBox1.Text += "短檔名: " + shortname + "\n";
                        //richTextBox1.Text += "前檔名: " + forename + "\n";
                        filenames.Add(fullname);
                    }
                }
            }
        }

        private void bt_open_dir_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "search_path = " + search_path + "\n";
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();
            folderBrowserDialog1.SelectedPath = search_path;  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                specified_search_path = folderBrowserDialog1.SelectedPath;
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
                specified_search_path = String.Empty;
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
