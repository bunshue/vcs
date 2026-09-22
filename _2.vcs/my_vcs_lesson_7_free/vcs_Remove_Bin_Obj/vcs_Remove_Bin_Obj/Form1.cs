using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;  // for Directory
using System.Diagnostics;   //for Process

namespace vcs_Remove_Bin_Obj
{
    public partial class Form1 : Form
    {
        //建立 一維字串串列
        List<string> folder_name = new List<string>();
        //建立 一維字串串列
        List<string> filename_rename = new List<string>();

        string search_path = string.Empty;
        //string search_path = @"D:\_git\vcs\_2.vcs";
        string specified_search_path = String.Empty;
        string result_str = string.Empty;

        int total_show_empty_folder_cnt = 0;
        int total_delete_empty_folder_cnt = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            //------------------------------------------------------------  # 60個

            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();
            search_path = currentPath;
            specified_search_path = currentPath;
            lb_main_mesg.Text = "";
            this.Text = "目前位置 : " + currentPath;
        }

        void show_item_location()
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
            button5.Location = new Point(x_st, y_st + dy * 9 + 10);

            button3.Location = new Point(x_st, y_st + dy * 12 + 30);
            bt_setup.Location = new Point(x_st + 120, y_st + dy * 12 + 30);
            bt_open_dir2.Location = new Point(x_st + 115 + 50, y_st + dy * 11 - 60);
            groupBox_remove.Location = new Point(x_st + 170, y_st + dy * 0);

            lb_main_mesg.Location = new Point(x_st + dx * 1 + 50, y_st + dy * 0);
            listView1.Size = new Size(570, 550);
            listView1.Location = new Point(x_st + dx * 1 + 50, y_st + dy * 1);

            richTextBox1.Size = new Size(500, 550);
            richTextBox1.Location = new Point(x_st + dx * 1 + 630, y_st + dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 650);
            this.Text = "vcs_Remove_Bin_Obj";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            result_str = "";
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            result_str = "";
            total_show_empty_folder_cnt = 0;
            total_delete_empty_folder_cnt = 0;
            lb_main_mesg.Text = "開始刪除檔案";
            this.Refresh();         //加上.Refresh()才可以讓人看清楚字的變化

            string path = string.Empty;

            if (rb_remove_vcs.Checked == true)
            {
                result_str += "清理 vcs\n";
                path = search_path;
            }
            else if (rb_remove_cuda.Checked == true)
            {
                result_str += "清理 CUDA\n";
                path = @"D:\_git\vcs\_3.cuda";
            }
            else if (rb_remove_opengl.Checked == true)
            {
                result_str += "清理 Open GL\n";
                path = @"D:\_git\vcs\_6.opengl";
            }
            else
            {
                path = search_path;
            }

            folder_name.Clear();

            // 搜尋路徑 是個 資料夾
            ProcessDirectory(path);

            ProcessDirectoryBinObj(folder_name);

            RemoveNeedlessFiles();

            if (checkBox9.Checked == true)
            {
                result_str += "共找到空資料夾 : " + total_show_empty_folder_cnt.ToString() + " 個\n";
            }
            if (checkBox10.Checked == true)
            {
                result_str += "共刪除空資料夾 : " + total_delete_empty_folder_cnt.ToString() + " 個\n";
                lb_main_mesg.Text += ", 刪除空資料夾 : " + total_delete_empty_folder_cnt.ToString() + " 個";
            }
            richTextBox1.Text += result_str;
        }

        private void ProcessDirectory(string foldername)
        {
            int file_cnt = 0;
            int dir_cnt = 0;

            //搜尋子目錄內的所有檔案   一層
            //使用 Directory.GetDirectories() 和 Directory.GetFiles()

            // 找資料夾, 一層
            string[] dirs = Directory.GetDirectories(foldername);  // 取得指定目錄中子目錄的名稱, 一層
            dir_cnt = dirs.Length;
            Array.Sort(dirs);  // 排序
            foreach (string dir in dirs)
            {
                if (dir.EndsWith("\\bin"))
                {
                    if (checkBox3.Checked == true)
                        result_str += dir + "\n";
                    if (checkBox1.Checked == true)
                        folder_name.Add(dir);
                }
                else if (dir.EndsWith("\\obj"))
                {
                    if (checkBox3.Checked == true)
                        result_str += dir + "\n";
                    if (checkBox1.Checked == true)
                        folder_name.Add(dir);
                }
                else if (dir.EndsWith("\\.vs"))
                {
                    if (checkBox3.Checked == true)
                        result_str += dir + "\n";
                    if (checkBox1.Checked == true)
                        folder_name.Add(dir);
                }
                else if (dir.EndsWith("\\x64"))
                {
                    if (checkBox3.Checked == true)
                        result_str += dir + "\n";
                    if (checkBox1.Checked == true)
                        folder_name.Add(dir);
                }
                else if ((dir.EndsWith("\\_UpgradeReport_Files")) || (dir.EndsWith("Backup")))
                {
                    if (checkBox7.Checked == true)
                        result_str += dir + "\n";   //僅顯示
                    if (checkBox8.Checked == true)
                        folder_name.Add(dir);              //加入刪除準備
                }
                else if (dir.EndsWith("\\Debug"))
                {
                    if (checkBox3.Checked == true)
                        result_str += dir + "\n";
                    if (checkBox1.Checked == true)
                        folder_name.Add(dir);
                }
                // 資料夾
                ProcessDirectory(dir);
            }

            string[] filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
            file_cnt = filenames.Length;
            Array.Sort(filenames);  // 排序
            foreach (string filename in filenames)
            {
                if ((filename.EndsWith(".suo")) || (filename.EndsWith(".csproj.user")))
                {
                    if (checkBox4.Checked == true)
                    {
                        result_str += filename + "\n";   //僅顯示
                    }
                    if (checkBox2.Checked == true)
                    {
                        folder_name.Add(filename);              //加入刪除準備
                    }
                }
                if ((filename.EndsWith("UpgradeLog.XML")) || (filename.EndsWith("UpgradeLog.XML")))
                {
                    if (checkBox7.Checked == true)
                    {
                        result_str += filename + "\n";   //僅顯示
                    }
                    if (checkBox8.Checked == true)
                    {
                        folder_name.Add(filename);              //加入刪除準備
                    }
                }
            }

            if ((file_cnt == 0) && (dir_cnt == 0))
            {
                if (checkBox9.Checked == true)
                {
                    result_str += foldername + "是一個空資料夾\n";
                    total_show_empty_folder_cnt++;
                }
                if (checkBox10.Checked == true)
                {
                    //result_str += "刪除 : " + foldername + "是一個空資料夾\n";
                    Directory.Delete(foldername, false);   //not recurrsive
                    result_str += "已刪除資料夾 : " + foldername + "\n";
                    total_delete_empty_folder_cnt++;
                }
            }
        }

        private void ProcessDirectoryBinObj(List<string> folder_name)
        {
            bool flag_rename_fail = false;
            int i;
            int len;
            len = folder_name.Count;
            result_str += "欲刪除個數 : " + len + "\n";
            for (i = 0; i < len; i++)
            {
                //result_str += "資料夾 : " + folder_name[i] + "\n";

                if (folder_name[i].Contains("bin"))
                {
                    //需要跳過的資料夾
                    if (folder_name[i].Contains("xxxxxxxxxxxxxxxx"))
                    {
                        result_str += "iiiiiiiiiiiiiiiiiiiii\n";
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
                        result_str += "跳過......\n";
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

                //result_str += "刪除 : " + folder_name[i] + "\n";

                if (Directory.Exists(folder_name[i]))     //確認資料夾是否存在
                {
                    try
                    {
                        Directory.Delete(folder_name[i], true);   //recurrsive
                        //Directory.Delete(folder_name[i], false);   //not recurrsive
                        result_str += "已刪除資料夾 : " + folder_name[i] + "\n";
                    }
                    catch
                    {
                        result_str += "無法刪除資料夾 : " + folder_name[i] + "\n";
                        flag_rename_fail = true;
                    }
                }
                else if (File.Exists(folder_name[i]))     //確認檔案是否存在
                {
                    try
                    {
                        File.Delete(folder_name[i]);
                        result_str += "已刪除檔案 : " + folder_name[i] + "\n";
                    }
                    catch
                    {
                        result_str += "無法刪除檔案 : " + folder_name[i] + "\n";
                        flag_rename_fail = true;
                    }
                }
                else
                {
                    result_str += "資料夾或檔案 : " + folder_name[i] + " 不存在，不能刪除\n";
                    flag_rename_fail = true;
                }
            }

            lb_main_mesg.Text = "刪除檔案 : " + len + " 個, 完成";
            if (flag_rename_fail == true)
            {
                lb_main_mesg.Text += "\t有錯誤";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            result_str = "";
            result_str += "檔名簡中轉正中\nTBD";
        }

        void RemoveNeedlessFiles()
        {
            string foldername = string.Empty;
            string[] filenames;

            foldername = @"D:\_git\vcs\_3.cuda\_code\bin\win64\Debug";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                result_str += "資料夾 : " + foldername + " 存在\n";

                filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
                foreach (string filename in filenames)
                {
                    if ((filename.Contains("freeglut.dll") == false) && (filename.Contains("glew64.dll") == false))
                    {
                        result_str += "remove : " + filename + "\n";
                        if (File.Exists(filename))  //確認檔案是否存在
                        {
                            try
                            {
                                File.Delete(filename);
                                result_str += "已刪除檔案 : " + filename + "\n";
                            }
                            catch
                            {
                                result_str += "無法刪除檔案 : " + filename + "\n";
                            }
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_3.cuda\bin\win64\Debug";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                result_str += "資料夾 : " + foldername + " 存在\n";

                filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
                foreach (string filename in filenames)
                {
                    if ((filename.Contains("freeglut.dll") == false) && (filename.Contains("glew64.dll") == false))
                    {
                        result_str += "remove : " + filename + "\n";
                        if (File.Exists(filename))  //確認檔案是否存在
                        {
                            try
                            {
                                File.Delete(filename);
                                result_str += "已刪除檔案 : " + filename + "\n";
                            }
                            catch
                            {
                                result_str += "無法刪除檔案 : " + filename + "\n";
                            }
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_6.opengl\bin_debug64";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                result_str += "資料夾 : " + foldername + " 存在\n";

                filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
                foreach (string filename in filenames)
                {
                    if ((filename.Contains("freeglut.dll") == false) && (filename.Contains("glew64.dll") == false))
                    {
                        result_str += "remove : " + filename + "\n";
                        if (File.Exists(filename))  //確認檔案是否存在
                        {
                            try
                            {
                                File.Delete(filename);
                                result_str += "已刪除檔案 : " + filename + "\n";
                            }
                            catch
                            {
                                result_str += "無法刪除檔案 : " + filename + "\n";
                            }
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_d_emgu\libemgucv-windows-x64-2.3.0.1416\bin";
            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                result_str += "資料夾 : " + foldername + " 存在\n";

                //filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
                filenames = Directory.GetFiles(foldername, "*.exe");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.pdb");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.manifest");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.txt");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.config");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.jpg");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }
            }

            foldername = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_d_emgu\libemgucv-windows-x86-2.3.0.1416\bin";

            if (Directory.Exists(foldername) == true)    //確認資料夾是否存在
            {
                result_str += "資料夾: " + foldername + " 存在\n";

                //filenames = Directory.GetFiles(foldername);  // 取得指定目錄中檔案的名稱
                filenames = Directory.GetFiles(foldername, "*.exe");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.pdb");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.manifest");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.txt");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }


                filenames = Directory.GetFiles(foldername, "*.config");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
                        }
                    }
                }

                filenames = Directory.GetFiles(foldername, "*.jpg");  // 取得指定目錄中檔案的名稱, 指定後綴名文件全路徑
                foreach (string filename in filenames)
                {
                    result_str += "remove : " + filename + "\n";

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
                            result_str += "已刪除檔案 : " + filename + "\n";
                        }
                        catch
                        {
                            result_str += "無法刪除檔案 : " + filename + "\n";
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
                        result_str += "已刪除檔案 : " + delete_filenames + "\n";
                    }
                    catch
                    {
                        result_str += "無法刪除檔案 : " + delete_filenames + "\n";
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
                result_str += "尚未選擇\n";
            }
        }

        private void bt_setup_Click(object sender, EventArgs e)
        {
            Form_Setup frm = new Form_Setup();    //實體化 Form_Setup 視窗物件
            frm.StartPosition = FormStartPosition.CenterScreen;      //設定視窗居中顯示
            frm.ShowDialog();   //顯示 frm 視窗
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            //button1_Click(sender, e);

            //------------------------------------------------------------  # 60個

            string git_command = Properties.Settings.Default.git_command;
            richTextBox1.Text += git_command + "\n";

            if (git_command == "")
            {
                richTextBox1.Text += "無 git 指令\n";
                return;
            }

            //TBD for git
            string exe_filename = "cmd";
            //string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin";
            //string parameters = @" /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o " + filename;
            string parameters = " /C C:/Users/070601/AppData/Local/Programs/Git/bin/git.exe pull --progress -v --no-rebase \"origin\"";

            //string git_command = " /C " + git_command + " pull --progress -v --no-rebase \"origin\"";
            //string parameters = " /C C:/Users/070601/AppData/Local/Programs/Git/bin/git.exe pull --progress -v --no-rebase \"origin\"";
            richTextBox1.Text += git_command + "\n";

            //parameters = git_command;
            run_command_line_process_async(exe_filename, git_command);
        }

        //非同步 Process使用
        void run_command_line_process_async(string exe_filename, string command)
        {
            Process process_async = new Process();    //創建一個進程用於調用外部程序

            process_async.StartInfo.FileName = exe_filename;  //設定要啟動的程式
            //process_async.StartInfo.Arguments = "/c " + command; //設定程式執行參數, 也可直接把command寫在這裡, 就不用後面的 StandardInput.WriteLine 了, 要加/c
            //process_async.StartInfo.Arguments = "/c systeminfo";  //可, 要加/c
            process_async.StartInfo.Arguments = command;
            //process_async.StandardInput.AutoFlush = true;

            process_async.StartInfo.UseShellExecute = false;  //false, 關閉Shell的使用, 是否指定操作系統外殼進程啟動程序, 可能接受來自調用程序的輸入信息
            process_async.StartInfo.RedirectStandardInput = true; //重定向標準輸入, 可能接受來自調用程序的輸入信息
            process_async.StartInfo.RedirectStandardOutput = true; //重定向標準輸出, 由調用程序獲取輸出信息
            process_async.StartInfo.RedirectStandardError = true; //重定向錯誤輸出
            process_async.StartInfo.CreateNoWindow = true; //true: 設置不顯示程式窗口, false: 出現cmd的黑窗體
            process_async.StartInfo.ErrorDialog = false;
            //process_async.StartInfo.WindowStyle = ProcessWindowStyle.Normal;  //測不出來
            //process_async.StartInfo.WindowStyle = ProcessWindowStyle.Hidden,

            process_async.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;

            //設定非同步資料處理 output and error handlers
            process_async.OutputDataReceived += new DataReceivedEventHandler(OutputHandler);
            process_async.ErrorDataReceived += new DataReceivedEventHandler(OutputHandler);

            process_async.Start();    //啟動程式

            //啟動讀取資料輸出與錯誤輸出
            process_async.BeginOutputReadLine();
            process_async.BeginErrorReadLine();

            richTextBox1.Text += "等待程式結束.......\n";
            process_async.WaitForExit();	//等待退出
            richTextBox1.Text += "程式結束\n";
        }

        void OutputHandler(object sendingProcess, DataReceivedEventArgs outLine)
        {
            //目前無法做到換行, 也不能操作richTextBox的內容
            richTextBox1.Text += outLine.Data;

            //跳至最後面 fail
            //richTextBox1.Focus();
            //richTextBox1.Select(richTextBox1.Text.Length, 0);
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

