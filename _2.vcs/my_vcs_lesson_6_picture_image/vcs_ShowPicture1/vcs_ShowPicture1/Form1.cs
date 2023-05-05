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

        string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic\_MU";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            GetAllFiles(foldername);

            foreach (DictionaryEntry de in ht)
            {
                this.comboBox1.Items.Add(de.Key);
            }
            if (comboBox1.Items.Count > 0)
                comboBox1.SelectedIndex = 0;
        }

        //多層 且指明副檔名
        public void GetAllFiles(string foldername)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                    {
                        //ht.add(key, value), key不能重複
                        ht.Add(forename, fullname);

                        richTextBox1.Text += "加入 前檔名 : " + forename + "\t長檔名 : " + fullname + "\n";
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
            this.pictureBox1.ImageLocation = name;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int len = ht.Count;

            richTextBox1.Text += "len = " + len.ToString() + "\n";

            //方法一：遍歷traversal 1:
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key = " + de.Key + "\t" + "value = " + de.Value + "\n";
            }

            //方法二：遍歷traversal 2:
            IDictionaryEnumerator d = ht.GetEnumerator();
            while (d.MoveNext())
            {
                //richTextBox1.Text += "key = " + d.Entry.Key + "\t" + "value = " + d.Entry.Value + "\n";
            }


        }

    }
}
