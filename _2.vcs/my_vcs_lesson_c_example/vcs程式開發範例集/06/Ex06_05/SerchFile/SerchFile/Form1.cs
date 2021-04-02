using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace SerchFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listView1.Items.Clear();
            SerachFile(textBox2.Text);
           // MessageBox.Show("搜索完畢");
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
                        listView1.Items[listView1.Items.Count-1].SubItems.Add( fin.FullName);
                        listView1.Items[listView1.Items.Count - 1].SubItems.Add(fin.Length.ToString());
                        listView1.Items[listView1.Items.Count - 1].SubItems.Add(fin.CreationTime.ToString());
                    }
                }
            }
        }
    }
}