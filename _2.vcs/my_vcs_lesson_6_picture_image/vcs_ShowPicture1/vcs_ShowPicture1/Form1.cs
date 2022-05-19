using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Collections;

namespace vcs_ShowPicture1
{
    public partial class Form1 : Form
    {
        Hashtable ht = new Hashtable();

        string dirname = @"C:\______test_files\__pic\_MU";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo(dirname);
            GetAllFiles(dir);
            foreach (DictionaryEntry de in ht)
            {
                this.comboBox1.Items.Add(de.Key);
            }
            if (comboBox1.Items.Count > 0)
                comboBox1.SelectedIndex = 0;
        }

        public void GetAllFiles(DirectoryInfo dir)
        {
            FileSystemInfo[] fileinfo = dir.GetFileSystemInfos();
            foreach (FileSystemInfo i in fileinfo)
            {
                if (i is DirectoryInfo)
                {
                    GetAllFiles((DirectoryInfo)i);
                }
                else
                {
                    string str = i.FullName;
                    int b = str.LastIndexOf("\\");
                    string strType = str.Substring(b + 1);
                    if (strType.Substring(strType.Length - 3).ToLower() == "jpg" || strType.Substring(strType.Length - 3).ToLower() == "bmp")
                    {
                        ht.Add(strType.Substring(0, strType.Length - 4), strType);
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += comboBox1.SelectedIndex.ToString() + "\n";
            if (comboBox1.SelectedIndex == -1)
                return;
            if (ht.Values.Count > 0)
            {
                showPic(ht[this.comboBox1.Text].ToString());
            }
            else
            {
                MessageBox.Show("目前還沒有圖片相關訊息！！！");
            }
        }

        private void showPic(string name)
        {
            this.pictureBox1.ImageLocation = dirname + "\\" + name;
        }

    }
}
