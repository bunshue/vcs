using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

//參考/加入參考 /COM/Microsoft Shell Controls and Automation
using Shell32;

namespace vcs_Shell32b
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
            richTextBox1.Text += "取得檔案內容中的詳細資料\n";
           
            string filename = @"C:\______test_files\picture1.jpg";
           
            int i;
            for (i = 0; i < 30; i++)
            {
                string result = GetDetailValue(filename, i);
                richTextBox1.Text += i.ToString() + "\t" + result + "\n";

            }


        }

        static string GetDetailValue(string file, int column)
        {
            Shell shell = new Shell();
            Folder dir = shell.NameSpace(Path.GetDirectoryName(file));
            FolderItem item = dir.ParseName(Path.GetFileName(file));
            return dir.GetDetailsOf(item, column);
        }


    }
}
