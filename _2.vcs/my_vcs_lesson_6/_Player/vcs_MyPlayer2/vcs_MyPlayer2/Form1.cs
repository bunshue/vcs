using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;    //FileInfo
using System.Diagnostics;

namespace vcs_MyPlayer2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string folder_name = String.Empty;
        private void button2_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("容量", 200, HorizontalAlignment.Center);
            //listView1.Columns.Add("日期", 200, HorizontalAlignment.Center);

            if (folder_name != String.Empty)
            {
                //只撈一層的所有檔案
                foreach (string filename in System.IO.Directory.GetFileSystemEntries(folder_name))
                {
                    richTextBox1.Text += filename + "\n";

                    ListViewItem i1 = new ListViewItem(filename);

                    FileInfo fi = new FileInfo(filename);
                    if (fi.Exists == true)      //確認檔案是否存在
                    {
                        richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                        richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                        richTextBox1.Text += "副檔名：" + fi.Extension + Environment.NewLine;
                        richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                        richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                        richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                        richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;
                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        sub_i1a.Text = fi.Length.ToString();
                        i1.SubItems.Add(sub_i1a);
                    }
                    else
                        richTextBox1.Text += "檔案: " + filename + " 不存在\n";

                    listView1.Items.Add(i1);
                    //設置ListView最後一行可見
                    listView1.Items[listView1.Items.Count - 1].EnsureVisible();
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                folder_name = folderBrowserDialog1.SelectedPath;
                //richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
            }
            else
            {
                //richTextBox1.Text = "未選取資料夾\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("容量", 200, HorizontalAlignment.Center);
            //listView1.Columns.Add("日期", 200, HorizontalAlignment.Center);

            if (folder_name != String.Empty)
            {

                //C# 取得資料夾下的所有檔案(包括子目錄)
                string[] files = System.IO.Directory.GetFiles(folder_name, "*.*", System.IO.SearchOption.AllDirectories);
                foreach (string filename in files)
                {
                    richTextBox1.Text += filename + "\n";
                    ListViewItem i1 = new ListViewItem(filename);

                    FileInfo fi = new FileInfo(filename);
                    if (fi.Exists == true)      //確認檔案是否存在
                    {
                        richTextBox1.Text += "資料夾：" + fi.Directory + Environment.NewLine;
                        richTextBox1.Text += "檔名：" + fi.Name + Environment.NewLine;
                        richTextBox1.Text += "副檔名：" + fi.Extension + Environment.NewLine;
                        richTextBox1.Text += "檔案大小：" + fi.Length.ToString() + Environment.NewLine;
                        richTextBox1.Text += "建立時間1：" + fi.CreationTime.ToString() + Environment.NewLine;
                        richTextBox1.Text += "建立時間2：" + fi.CreationTimeUtc.ToString() + Environment.NewLine;
                        richTextBox1.Text += "最近寫入時間：" + fi.LastWriteTime.ToString() + Environment.NewLine;
                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        sub_i1a.Text = fi.Length.ToString();
                        i1.SubItems.Add(sub_i1a);
                    }
                    else
                        richTextBox1.Text += "檔案: " + filename + " 不存在\n";

                    listView1.Items.Add(i1);
                    //設置ListView最後一行可見
                    listView1.Items[listView1.Items.Count - 1].EnsureVisible();


                }
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void listView1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            int selNdx = listView1.SelectedIndices[0];
            listView1.Items[selNdx].Selected = true;    //選到的項目
            //richTextBox1.Text += "count = " + this.listView1.SelectedIndices.Count.ToString() + "\t";
            richTextBox1.Text += "你選擇了" + listView1.Items[selNdx].Text + "\n";
            System.Diagnostics.Process.Start(listView1.Items[selNdx].Text);
        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click_1(object sender, EventArgs e)
        {
            int selNdx;
            string all_filename = string.Empty;
            string player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
            if (this.listView1.SelectedIndices.Count <= 0)  //總共選擇的個數
                return;

            //richTextBox1.Text += "總共選了 : " + listView1.SelectedItems.Count.ToString() + " 個檔案，分別是 : \n";
            for (int i = 0; i < listView1.SelectedItems.Count; i++)
            {
                selNdx = listView1.SelectedIndices[i];
                listView1.Items[selNdx].Selected = true;    //選到的項目
                //richTextBox1.Text += listView1.Items[selNdx].Text + "\n";
                all_filename += " \"" + listView1.Items[selNdx].Text + "\"";
            }

            //指定應用程式路徑
            //string target = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
            string target = player_path;

            //方法一
            //Process.Start(target, "參數");
            //Process.Start(target, all_filename);

            //方法二
            ProcessStartInfo pInfo = new ProcessStartInfo(target);
            pInfo.Arguments = all_filename;

            richTextBox1.Text += "target : " + target + "\n";
            richTextBox1.Text += "all_filename : " + all_filename + "\n";

            using (Process process = new Process())
            {
                process.StartInfo = pInfo;
                process.Start();    //啟動程式
            }
        }
    }
}
