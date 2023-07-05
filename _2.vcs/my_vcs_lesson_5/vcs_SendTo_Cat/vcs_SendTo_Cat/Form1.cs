using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_SendTo_Cat
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string sendto_folder = Environment.GetFolderPath(Environment.SpecialFolder.SendTo);
            //richTextBox1.Text += "[傳送到]資料夾位置:\n" + sendto_folder + "\n";

            //label1.Text = "檔案總管 右鍵 傳送到 XXX, 可用XXX開啟檔案\n\n拉一個捷徑到\n%APPDATA%\\Microsoft\\Windows\\SendTo\n或\n" + sendto_folder;

            int len = System.Environment.GetCommandLineArgs().Length;
            int i;
            //richTextBox1.Text += "參數長度\t" + len.ToString() + "\t分別是:\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "第 " + i.ToString() + " 項\t" + System.Environment.GetCommandLineArgs()[i] + "\n";
            }

            for (i = 1; i < len; i++)
            {
                print_file_content(System.Environment.GetCommandLineArgs()[i]);
            }
        }

        void print_file_content(string filename)
        {
            StringBuilder sb = new StringBuilder();

            string[] Txt_All_Lines = File.ReadAllLines(filename, Encoding.Default);

            foreach (string Single_Line in Txt_All_Lines)
            {
                sb.AppendLine(Single_Line);
            }

            richTextBox1.Text += sb.ToString() + "\n";

        }
    }
}
