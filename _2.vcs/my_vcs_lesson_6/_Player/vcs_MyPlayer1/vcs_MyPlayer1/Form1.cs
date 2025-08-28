using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for FileStream, path

namespace vcs_MyPlayer1
{
    public partial class Form1 : Form
    {
        string file_path = string.Empty;
        String playlist_filename = "my_playlist.txt";

        public Form1()
        {
            InitializeComponent();
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //改成附加至播放清單，以下4行為清空播放清單
            //listView1.Clear();
            //listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            //listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);

            openFileDialog1.Title = "多選檔案";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.txt";
            //openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.Filter = "音樂檔(*.mp3)|*.mp3|Wave檔(*.wav)|*.wav|所有檔案(*.*)|*.*";   //檔案類型
            openFileDialog1.FilterIndex = 3;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();         //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"D:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案: " + openFileDialog1.FileName + "\n";
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n";
                richTextBox1.Text += "已選取檔案: \n";
                foreach (var strFilename in openFileDialog1.FileNames)
                {
                    richTextBox1.Text += "\t" + strFilename + "\n";

                    ListViewItem i1 = new ListViewItem(strFilename);
                    ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                    //sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                    sub_i1a.Text = string.Empty;
                    i1.SubItems.Add(sub_i1a);
                    listView1.Items.Add(i1);
                }
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();

                richTextBox1.Text += "\n";

            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            listView1.Clear();
            listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            if (System.IO.File.Exists(playlist_filename) == false)
            {
                richTextBox1.Text += "檔案 " + playlist_filename + " 不存在，離開。\n";
            }
            else
            {
                int i = 0;
                richTextBox1.Text += "檔案 " + playlist_filename + " 存在, 開啟，並讀入播放清單。\n";

                listView1.Clear();
                listView1.Columns.Add("檔名", 400, HorizontalAlignment.Center);
                listView1.Columns.Add("內容", 200, HorizontalAlignment.Center);

                String line;
                StreamReader sr = new StreamReader(playlist_filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    i++;
                    line = sr.ReadLine();            // 讀取文字到 line 變數
                    richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\tlength:" + line.Length.ToString() + "\n";
                    if (line.Length > 0)
                    {
                        ListViewItem i1 = new ListViewItem(line);
                        ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                        //sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                        sub_i1a.Text = string.Empty;
                        i1.SubItems.Add(sub_i1a);
                        listView1.Items.Add(i1);
                    }
                }
                sr.Close();
                //設置ListView最後一行可見
                listView1.Items[listView1.Items.Count - 1].EnsureVisible();

            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            int i = 0;
            int numberMusic = listView1.Items.Count;

            if (numberMusic <= 0)
            {
                richTextBox1.Text += "0首歌，不用存檔\n";
            }
            else
            {
                richTextBox1.Text += "共有 " + numberMusic.ToString() + " 首歌, 依序是：\n";
                StreamWriter sw = File.CreateText(playlist_filename);
                string content = "";

                //file_path = listView1.Items[selNdx].Text;
                for (i = 0; i < numberMusic; i++)
                {
                    richTextBox1.Text += listView1.Items[i].Text + "\n";
                    content += listView1.Items[i].Text + "\n";
                }
                sw.WriteLine(content);
                sw.Close();
            }
        }

        private void listView1_DoubleClick(object sender, EventArgs e)
        {
            if (this.listView1.SelectedIndices.Count <= 0)
                return;

            /* 一樣
            if (listView1.SelectedItems.Count <= 0)
                return;
            */

            /* 一樣
            //ListView.SelectedListViewItemCollection selected = listView1.SelectedItems;
            //file_path = selected[0].SubItems[0].Text;
            */

            int selNdx = listView1.SelectedIndices[0];
            file_path = listView1.Items[selNdx].Text;
            richTextBox1.Text += "選到檔案：" + file_path + "\n";

            System.Diagnostics.Process.Start(file_path);



        }


    }
}
