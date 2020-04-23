using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_讀取二進位檔案
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string filename = "C:\\______test_files\\harumi.mp3";


        void print_data(byte[] data, int len)
        {
            bool flag_get_long_word = false;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");

                if (flag_get_long_word == true)
                {
                    flag_get_long_word = false;
                    richTextBox1.Text += " ";
                }
                else if (data[i] > 0x80)
                {
                    flag_get_long_word = true;
                }
                else
                {
                    richTextBox1.Text += " ";
                }
            }
            richTextBox1.Text += "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //循序binary讀取
            FileStream fs = File.Open(filename, FileMode.OpenOrCreate, FileAccess.ReadWrite);
            BinaryReader br = new BinaryReader(fs);
            //int len = System.Convert.ToInt16(fs.Length);

            richTextBox1.Text += "len = " + fs.Length.ToString() + "\n";

            richTextBox1.Text += "讀取檔案 : " + filename + "\n";
            //richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";

            richTextBox1.Text += "讀前面1/3\n";
            int len = 200;

            //讀取位元陣列
            byte[] data = br.ReadBytes(len);    //用ReadBytes讀取檔案的前幾拜(循序)

            //釋放資源
            br.Close();
            fs.Close();

            print_data(data, len);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


    }
}
