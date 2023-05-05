using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FolderBrowserDialog
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = @"C:\_git\vcs\_1.data\______test_files1";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
                richTextBox1.Text += "RootFolder: " + folderBrowserDialog1.RootFolder + "\n";
                richTextBox1.Text += "Container: " + folderBrowserDialog1.Container + "\n";
                richTextBox1.Text += "Description: " + folderBrowserDialog1.Description + "\n";
                richTextBox1.Text += "ShowNewFolderButton: " + folderBrowserDialog1.ShowNewFolderButton + "\n";
                richTextBox1.Text += "Site: " + folderBrowserDialog1.Site + "\n";
                richTextBox1.Text += "Tag: " + folderBrowserDialog1.Tag + "\n";

            }
            else
            {
                richTextBox1.Text = "未選取資料夾\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {


        }
    }
}
