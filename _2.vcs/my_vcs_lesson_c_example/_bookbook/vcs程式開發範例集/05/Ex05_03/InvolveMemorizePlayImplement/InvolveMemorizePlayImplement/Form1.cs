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
        static int index = 0;
        string filename_r = @"C:\______test_files\_mp3\list.m3u";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
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
                    listBox1.Items.Add(str);
                }
            }
        }

        private void listBox1_DoubleClick(object sender, EventArgs e)
        {
            string strPath = listBox1.Items[listBox1.SelectedIndex].ToString();
            ShowPlay(strPath);
        }

        private void ShowPlay(string Path)
        {
            label2.Text = Path;
            axWindowsMediaPlayer1.URL = Path;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            index += 1;
            if (index % 2 == 0)
            {
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }
            else
            {
                axWindowsMediaPlayer1.Ctlcontrols.pause();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ShowPlay(openFileDialog1.FileName);
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
                string strk = sr.ReadLine();
                if (strk != "")
                {
                    richTextBox1.Text += "加入項目 : " + strk + "\n";
                    listBox1.Items.Add(strk);
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
                StreamWriter sw = new StreamWriter(filename_w, true);

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
