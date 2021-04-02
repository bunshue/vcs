using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Collections;

namespace ProductElectronQuote
{
    public partial class Form1 : Form
    {
        Hashtable ht=new Hashtable();
        string str;
        public Form1()
        {
            InitializeComponent();
            str = Environment.CurrentDirectory + "//Image";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DirectoryInfo dir = new DirectoryInfo(str);
            GetAllFiles(dir);
            foreach (DictionaryEntry de in ht)
                this.comboBox1.Items.Add(de.Key);

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
                    if (strType.Substring(strType.Length - 3) == "jpg" || strType.Substring(strType.Length - 3) == "bmp")
                    {
                        ht.Add(strType.Substring(0,strType.Length-4), strType);
                    }
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (ht.Values.Count > 0)
            {
                showPic(ht[this.comboBox1.Text].ToString());
            }
            else
            {
                MessageBox.Show("目前還沒有海報訊息！！！");
            }
        }

        private void showPic(string name)
        {
            this.pictureBox1.ImageLocation = str + "\\" + name;
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {

        }
    }
}