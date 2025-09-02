using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Directory

namespace vcs_DrAP
{
    public partial class Form_Replace : Form
    {
        string search_path = string.Empty;
        string specified_search_path = String.Empty;

        public Form_Replace()
        {
            InitializeComponent();
        }

        private void Form_Replace_Load(object sender, EventArgs e)
        {
            show_item_location();

            //取得目前所在路徑
            string currentPath = Directory.GetCurrentDirectory();

            this.Text = "目前位置 : " + currentPath;
            lb_path.Text = currentPath;
            search_path = currentPath;
            specified_search_path = currentPath;
            tb_string_old.Text = @"D:/_git/vcs/_1.data/______test_files2";
            tb_string_new.Text = @"D:/_git/vcs/_1.data/______test_files1/";
        }

        void show_item_location()
        {
            int x_st = 15;
            int y_st = 15;
            int dx = 230;
            int dy = 35;

            groupBox_replace.Size = new Size(550, 170);
            groupBox_replace.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            richTextBox1.Size = new Size(550, 360);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 5);

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
            bt_open_dir.Location = new Point(x_st + dx * 3 + 10, y_st + dy * 2);
            lb_path.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 8);
            int dd = 20;
            dy = 30;
            rb_file_type0.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 0);
            rb_file_type1.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 1);
            rb_file_type2.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 2);
            rb_file_type3.Location = new Point(x_st + dx * 6 + dd, y_st + dy * 3);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(800, 600);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        private void bt_replace_Click(object sender, EventArgs e)
        {
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

        private void bt_open_dir_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "search_path = " + search_path + "\n";
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();
            folderBrowserDialog1.SelectedPath = search_path;  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                specified_search_path = folderBrowserDialog1.SelectedPath;
                lb_path.Text = specified_search_path;
                search_path = specified_search_path;
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
                specified_search_path = String.Empty;
            }
        }
    }
}
