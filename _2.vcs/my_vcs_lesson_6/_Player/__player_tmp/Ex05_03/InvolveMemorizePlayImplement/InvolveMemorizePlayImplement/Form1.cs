using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace InvolveMemorizePlayImplement
{
    public partial class Form1 : Form
    {
        string filename_r = @"C:\______test_files\_mp3\list.m3u";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Text = "mp3播放器";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void br_clear_listbox_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = @"C:\______test_files\_mp3";
            openFileDialog1.Multiselect = true;
            openFileDialog1.FileName = "";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                foreach (string str in openFileDialog1.FileNames)
                {
                    //richTextBox1.Text += "str = " + str + "\n";
                    listBox1.Items.Add(str);
                }

                if (openFileDialog1.FileNames.Length == listBox1.Items.Count)   //初次加入清單 預設播放第一首
                {
                    this.Text = listBox1.Items[0].ToString();
                    axWindowsMediaPlayer1.URL = listBox1.Items[0].ToString();
                }

                richTextBox1.Text += "本次開啟檔案 : " + openFileDialog1.FileNames.Length.ToString() + " 個\t";
                richTextBox1.Text += "清單內共有檔案 : " + listBox1.Items.Count.ToString() + " 個\n";
            }
        }

        private void listBox1_DoubleClick(object sender, EventArgs e)
        {
            string str = listBox1.Items[listBox1.SelectedIndex].ToString();
            this.Text = str;
            axWindowsMediaPlayer1.URL = str;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (button3.Text == "暫停")
            {
                button3.Text = "繼續";
                axWindowsMediaPlayer1.Ctlcontrols.pause();
            }
            else
            {
                button3.Text = "暫停";
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "old filename = " + openFileDialog1.FileName + "\n";
            richTextBox1.Text += "url = " + axWindowsMediaPlayer1.URL + "\n";
            if (axWindowsMediaPlayer1.URL == "")
            {
                richTextBox1.Text += "無檔可播\n";
            }
            else
            {
                this.Text = axWindowsMediaPlayer1.URL;
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            axWindowsMediaPlayer1.Ctlcontrols.stop();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //讀入清單
            richTextBox1.Text += "讀取檔案 : " + filename_r + "\n";
            StreamReader sr = new StreamReader(filename_r, Encoding.Default);
            while (sr.Peek() >= 0)
            {
                string line = sr.ReadLine();
                if (line != "")
                {
                    richTextBox1.Text += "加入項目 : " + line + "\n";
                    listBox1.Items.Add(line);
                }
            }
            sr.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //匯出清單
            string filename_w = Application.StartupPath + "\\m3u_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".m3u";

            int len = listBox1.Items.Count;
            if (len > 0)
            {
                FileStream fs = new FileStream(filename_w, FileMode.Create, FileAccess.Write);
                StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("Unicode"));   //指名編碼格式

                int i;
                for (i = 0; i < len; i++)
                {
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + listBox1.Items[i] + "\n";
                    sw.WriteLine(listBox1.Items[i]);
                }

                sw.Flush();
                sw.Close();

            }
            else
            {
                richTextBox1.Text += "播放清單內沒有項目\n";
            }
        }
    }
}
