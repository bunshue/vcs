using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_SendTo_Convert
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_copy.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_copy.Size.Width, richTextBox1.Location.Y);
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

            List<String> filenames = new List<String>();

            for (i = 1; i < len; i++)
                filenames.Add(System.Environment.GetCommandLineArgs()[i]);

            filenames.Sort();

            for (i = 0; i < (len - 1); i++)
            {
                string filename = filenames[i];
                print_file_content(filename);
            }
        }

        void print_file_content(string filename)
        {
            richTextBox1.Text += "\n#檔案 : " + filename + "\n\n";

            StringBuilder sb = new StringBuilder();

            string[] Txt_All_Lines = File.ReadAllLines(filename, Encoding.GetEncoding("utf-8"));   //指名編碼格式

            foreach (string Single_Line in Txt_All_Lines)
            {
                sb.AppendLine(Single_Line);
            }

            richTextBox1.Text += sb.ToString() + "\n";

            richTextBox1.Text += "print('------------------------------------------------------------')	#60個\n";

        }

        private void bt_copy_Click(object sender, EventArgs e)
        {
            //C# – 複製資料到剪貼簿
            //Clipboard.SetData(DataFormats.Text, richTextBox1.Text + "\n");
            Clipboard.SetDataObject(richTextBox1.Text + "\n");      //建議用此
            richTextBox1.Text += "已複製資料到系統剪貼簿\n";
        }
    }
}
