using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_bin2hex
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        void do_bin2hex(string filename_load)
        {
            int i;
            //string filename_load = @"./files/DISABLE_CONFIGURE.cod";
            string filename_save = filename_load + ".txt";

            richTextBox1.Text += "filename_load = " + filename_load + "\n";
            richTextBox1.Text += "filename_save = " + filename_save + "\n";

            //讀取二進位檔案
            //開啟檔案
            FileStream myFile = File.Open(filename_load, FileMode.OpenOrCreate, FileAccess.ReadWrite);

            BinaryReader myReader = new BinaryReader(myFile);

            int dl = System.Convert.ToInt16(myFile.Length);

            richTextBox1.Clear();
            //richTextBox1.Text += "length = " + dl.ToString() + "\n";


            //讀取位元陣列
            byte[] myData = myReader.ReadBytes(dl);

            int cmd_len = 0;
            int cmd_start = 0;

            richTextBox1.Text += filename_load + "\n\n";
            richTextBox1.Text += "sync\tlen\tcmd\tdata";

            for (i = 0; i < dl; i++)
            {
                if ((myData[i] == 0xFF) && (myData[i + 1] == 0xAA))     //sync
                {
                    cmd_len = myData[i + 2];
                    cmd_start = i;
                }

                if (i == cmd_start)
                    richTextBox1.Text += "\n";

                if ((i > cmd_start + cmd_len + 1) && (myData[i] == 0))
                {
                    richTextBox1.Text += ".";
                }
                else
                {
                    richTextBox1.Text += myData[i].ToString("X2");
                }
                if ((i == (cmd_start + 1)) || (i == (cmd_start + 2)) || (i == (cmd_start + 3)))
                {
                    richTextBox1.Text += "\t";
                }
                else if ((i <= cmd_start + cmd_len + 1))// && (myData[i] == 0))
                {
                    richTextBox1.Text += "  ";
                }
                else if (myData[i] != 0)
                {
                    richTextBox1.Text += "  ";
                }
            }
            richTextBox1.Text += "\n\n";

            StreamWriter sw = File.CreateText(filename_save);

            sw.WriteLine(richTextBox1.Text);
            sw.Close();

            //釋放資源
            myReader.Close();
            myFile.Close();

        
        
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "get file numbers : " + openFileDialog1.FileNames.Length.ToString() + "\n";
                for (i = 0; i < openFileDialog1.FileNames.Length; i++)
                {
                    richTextBox1.Text += "filename : " + openFileDialog1.FileNames[i] + "\n";

                    do_bin2hex(openFileDialog1.FileNames[i]);

                }
            
            }



        }
    }
}
