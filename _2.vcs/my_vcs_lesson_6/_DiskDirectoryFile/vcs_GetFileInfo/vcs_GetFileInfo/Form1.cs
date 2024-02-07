using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_GetFileInfo
{
    public partial class Form1 : Form
    {
        string foldername = @"C:\_git\vcs\_1.data\______test_files1";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = foldername;

            listView1.Items.Clear();
            List<FileInfo> fi = new List<FileInfo>();
            foreach (string strFile in Directory.GetFiles(textBox1.Text))
            {
                fi.Add(new FileInfo(strFile));
            }
            var values = from strFile in fi
                         group strFile by strFile.Extension into FExten
                         orderby FExten.Key
                         select FExten;
            foreach (var vFiles in values)
            {
                foreach (var f in vFiles)
                {
                    listView1.Items.Add(f.FullName);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                listView1.Items.Clear();
                textBox1.Text = folderBrowserDialog1.SelectedPath;
                List<FileInfo> fi = new List<FileInfo>();
                foreach (string strFile in Directory.GetFiles(textBox1.Text))
                {
                    fi.Add(new FileInfo(strFile));
                }
                var values = from strFile in fi
                             group strFile by strFile.Extension into FExten
                             orderby FExten.Key
                             select FExten;
                foreach (var vFiles in values)
                {
                    foreach (var f in vFiles)
                    {
                        listView1.Items.Add(f.FullName);
                    }
                }
            }
        }

        private void listView1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (listView1.SelectedItems.Count != 0)
            {
                FileInfo fi = new FileInfo(listView1.SelectedItems[0].Text);
                string[] strAttribute = new string[] { fi.Name, Convert.ToDouble(fi.Length / 1024).ToString(), fi.Extension, fi.CreationTime.ToString(), fi.IsReadOnly.ToString(), fi.LastWriteTime.ToString() };
                var values = from str in strAttribute
                             select new
                             {
                                 Name = strAttribute[0].ToString(),
                                 Size = strAttribute[1].ToString(),
                                 Exten = strAttribute[2].ToString(),
                                 CTime = strAttribute[3].ToString(),
                                 ReadOnly = strAttribute[4].ToString(),
                                 WTime = strAttribute[5].ToString()
                             };
                foreach (var v in values)
                {
                    string fileinfo = string.Empty;
                    fileinfo += "檔案訊息 :\n";
                    fileinfo += "檔案名 : \t" + v.Name.ToString() + "\n";
                    fileinfo += "副檔名 : \t" + v.Exten.ToString() + "\n";
                    fileinfo += "檔案大小 : \t" + v.Size.ToString() + " KB\n";
                    fileinfo += "建立時間 : \t" + v.CTime.ToString() + "\n";
                    fileinfo += "最後修改時間 : \t" + v.WTime.ToString() + "\n";
                    fileinfo += "唯讀 : \t" + v.ReadOnly.ToString() + "\n";

                    richTextBox_fileinfo.Text = fileinfo;
                }

                string ext = fi.Extension.ToLower();
                if ((ext == ".bmp") || (ext == ".jpg") || (ext == ".png"))
                {
                    pictureBox1.Image = Image.FromFile(listView1.SelectedItems[0].Text);
                }
                else
                {
                    pictureBox1.Image = null;
                }
            }
        }
    }
}

