using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FolderFileName
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 0;
        }

        string folder_name = String.Empty;
        int filetype = 0;
        string filetype2 = String.Empty;

        private void button2_Click(object sender, EventArgs e)
        {
            if (folder_name != String.Empty)
            {
                //只撈一層的所有檔案
                foreach (string fname in System.IO.Directory.GetFileSystemEntries(folder_name))
                {
                    richTextBox1.Text += fname + "\n";
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            folderBrowserDialog1.SelectedPath = "c:\\______test_vcs";  //預設開啟的路徑
            if (folderBrowserDialog1.ShowDialog() == DialogResult.OK)
            {
                folder_name = folderBrowserDialog1.SelectedPath;
                //richTextBox1.Text += "選取資料夾: " + folderBrowserDialog1.SelectedPath + "\n";
            }
            else
            {
                //richTextBox1.Text = "未選取資料夾\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (folder_name != String.Empty)
            {
                //C# 取得資料夾下的所有檔案(包括子目錄)
                string[] files = System.IO.Directory.GetFiles(folder_name, filetype2, System.IO.SearchOption.AllDirectories);
                foreach (string filename in files)
                {
                    richTextBox1.Text += filename + "\n";
                }
            }

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            filetype = comboBox1.SelectedIndex;
            switch (filetype)
            { 
                case 0:
                    filetype2 = "*.*";
                    break;
                case 1:
                    filetype2 = "*.mp3";
                    break;
                case 2:
                    filetype2 = "*.txt";
                    break;
                default:
                    filetype2 = "*.*";
                    break;
            }
            richTextBox1.Text += "change file type to " + filetype2 + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }
    }
}
