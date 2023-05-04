using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_FolderInfo
{
    public partial class Form1 : Form
    {
        double total_size = 0;
        int no_files = 0;
        int no_folders = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void btn_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            listView1.Clear();
            label1.Text = "路徑";
        }

        private void btn_test6_Click(object sender, EventArgs e)
        {
            total_size = 0;
            no_files = 0;
            no_folders = 0;

            listView1.Columns.Add("名稱", 200, HorizontalAlignment.Center);
            listView1.Columns.Add("大小", 200, HorizontalAlignment.Center);
            listView1.Columns.Add("修改日期", 200, HorizontalAlignment.Center);
            //string filePath = @"c:/______test_files/";
            string filePath = @"C:\______test_files1\__pic\_book_magazine";

            /*
            richTextBox1.Text += "轉出一層,獲得指定目錄下的所有文檔：\n";
            List<FileInfo> list1 = GetFilesByDir(filePath);
            foreach (FileInfo fi in list1)
            {
                //richTextBox1.Text += "完整路徑：" + fi.FullName.ToString() + " 文檔名：" + fi.Name + "\n";
                //richTextBox1.Text += "資料夾：" + fi.Directory + "\n";
                richTextBox1.Text += "檔名：" + fi.Name + "\t";
                richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + "\t";
                richTextBox1.Text += "修改日期：" + fi.LastWriteTime.ToString() + "\n";

                total_size += fi.Length;
                no_files++;

                ListViewItem i1 = new ListViewItem(fi.Name);
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                sub_i1a.Text = fi.Length.ToString();
                i1.SubItems.Add(sub_i1a);
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                sub_i1b.Text = fi.LastWriteTime.ToString();
                i1.SubItems.Add(sub_i1b);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();
            }
            */

            richTextBox1.Text += "轉出全部,列出指定目錄下及所有子目錄及子目錄裏更深層目錄裏的文檔：\n";
            GetAllFiles(filePath);

            label1.Text = "路徑：" + filePath + "\n大小：" + total_size.ToString() + " 位元組\n內含：" + no_files.ToString() + " 個檔案，" + (no_folders - 1).ToString() + " 個資料夾";

            //大小：	xxxxx 位元組
            //內含：   143個檔案，18個資料夾

        }

        /// <summary>
        /// 獲得指定目錄下的所有文檔
        /// </summary>
        /// <param name="path"></param>
        /// <returns></returns>
        public List<FileInfo> GetFilesByDir(string path)
        {
            DirectoryInfo di = new DirectoryInfo(path);

            //找到該目錄下的文檔
            FileInfo[] fi = di.GetFiles();

            //把FileInfo[]數組轉換為List
            List<FileInfo> list = fi.ToList<FileInfo>();
            return list;
        }

        /// <summary>
        /// 列出指定目錄下及所其有子目錄及子目錄裏更深層目錄裏的文檔（需要遞歸）
        /// </summary>
        /// <param name="path"></param>
        public void GetAllFiles(string path)
        {
            DirectoryInfo dir = new DirectoryInfo(path);

            //找到該目錄下的文檔
            FileInfo[] fi = dir.GetFiles();
            foreach (FileInfo f in fi)
            {
                //richTextBox1.Text += "完整路徑：" + f.FullName.ToString() + " 文檔名：" + f.Name + "\n";
                //richTextBox1.Text += "資料夾：" + f.Directory + "\n";
                richTextBox1.Text += "檔名：" + f.Name + "\t";
                richTextBox1.Text += "大小：" + f.Length.ToString() + "\t";
                richTextBox1.Text += "日期：" + f.LastWriteTime.ToString() + "\n";

                total_size += f.Length;
                no_files++;

                ListViewItem i1 = new ListViewItem(f.Name);
                ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                sub_i1a.Text = f.Length.ToString();
                i1.SubItems.Add(sub_i1a);
                ListViewItem.ListViewSubItem sub_i1b = new ListViewItem.ListViewSubItem();
                sub_i1b.Text = f.LastWriteTime.ToString();
                i1.SubItems.Add(sub_i1b);

                listView1.Items.Add(i1);
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();


            }

            //找到該目錄下的所有目錄再遞歸
            DirectoryInfo[] subDir = dir.GetDirectories();
            no_folders++;
            foreach (DirectoryInfo d in subDir)
            {
                GetAllFiles(d.FullName);
            }
        }

        private void btn_test7_Click(object sender, EventArgs e)
        {

        }

        private void btn_test8_Click(object sender, EventArgs e)
        {

        }
    }
}
