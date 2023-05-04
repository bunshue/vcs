using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

using System.IO;

namespace vcs_SearchFile2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = "angry_bird.jpg";
            textBox2.Text = @"C:\______test_files1";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();
            SerachFile(textBox2.Text);
            richTextBox1.Text += "搜尋完畢\n";
        }

        public void SerachFile(string fileDirectory)
        {
            DirectoryInfo dir = new DirectoryInfo(fileDirectory);
            FileSystemInfo[] f = dir.GetFileSystemInfos();
            foreach (FileSystemInfo i in f)
            {
                if (i is DirectoryInfo)
                {
                    SerachFile(i.FullName);
                }
                else
                {
                    if (i.Name == textBox1.Text)
                    {
                        FileInfo fin = new FileInfo(i.FullName);
                        listView1.Items.Add(fin.Name);//為ListView新增數據
                        listView1.Items[listView1.Items.Count - 1].SubItems.Add(fin.FullName);
                        listView1.Items[listView1.Items.Count - 1].SubItems.Add(fin.Length.ToString());
                        listView1.Items[listView1.Items.Count - 1].SubItems.Add(fin.CreationTime.ToString());
                    }
                }
            }
        }
    }
}



