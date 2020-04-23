using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_Bin2Hex
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int MODE_0 = 0x00;
        private const int MODE_1 = 0x01;

        void do_bin2hex(int mode)
        {
            openFileDialog1.Title = "二進位檔轉成文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.*";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 4;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();   //從目前目錄開始尋找檔案
            //openFileDialog1.InitialDirectory = "c:\\______test_files";            //預設開啟的路徑
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                string filename = openFileDialog1.FileName;
                byte[] data;
                long len;
                int i;

                if (mode == MODE_0)
                {
                    //全部binary讀取
                    data = File.ReadAllBytes(filename);
                    len = data.Length;

                    richTextBox1.Text += "檔案名稱 : " + filename + "\n";
                    richTextBox1.Text += "檔案長度 : " + len.ToString() + "\n";
                    //print_data(data, len);
                }
                else
                {
                    //前部分binary讀取
                    data = File.ReadAllBytes(filename);
                    long len_file = data.Length;

                    FileStream fs = File.Open(filename, FileMode.OpenOrCreate, FileAccess.ReadWrite);
                    BinaryReader br = new BinaryReader(fs);
                    //len = System.Convert.ToDouble(fs.Length);
                    len = fs.Length;
                    richTextBox1.Text += "讀取檔案 : " + filename + "\n";
                    richTextBox1.Text += "檔案長度 : " + len_file.ToString() + "\n";
                    len = int.Parse(textBox1.Text);
                    richTextBox1.Text += "讀取長度 : " + len.ToString() + "\n";

                    if (len > len_file)
                        len = len_file;
                    richTextBox1.Text += "讀前面 " + len.ToString() + " 拜\n";

                    //讀取位元陣列
                    data = br.ReadBytes((int)len);    //用ReadBytes讀取檔案的前幾拜(循序)

                    //釋放資源
                    br.Close();
                    fs.Close();



                }

                filename = filename + ".txt";

                FileStream fsw = new FileStream(filename, FileMode.Create, FileAccess.Write);
                StreamWriter sw;


                sw = new StreamWriter(fsw, Encoding.GetEncoding("unicode"));   //指名編碼格式

                for (i = 0; i < len; i++)
                {
                    sw.Write(data[i].ToString("X2") + "\n");
                }
                sw.Close();
                richTextBox1.Text += "存檔完成, 檔名 : " + filename + "\n\n";




            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";
            }



        }

        private void button1_Click(object sender, EventArgs e)
        {
            do_bin2hex(MODE_0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            do_bin2hex(MODE_1);
        }

        void print_data(byte[] data, int len)
        {
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % 32) == 31)
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += "  ";
            }
            richTextBox1.Text += "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

    }
}
