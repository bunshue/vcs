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
        private const int MODE_0 = 0x00;
        private const int MODE_1 = 0x01;
        int new_line = 1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void print_data(byte[] data)
        {
            int i;
            int len;
            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if ((i % new_line) == (new_line - 1))
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";
        }

        void do_bin2hex(int mode)
        {
            if (radioButton1.Checked == true)
                new_line = 1;
            else if (radioButton2.Checked == true)
                new_line = 2;
            else if (radioButton3.Checked == true)
                new_line = 8;
            else if (radioButton4.Checked == true)
                new_line = 16;
            else if (radioButton5.Checked == true)
                new_line = 32;
            else
                new_line = 4;

            openFileDialog1.Title = "二進位檔轉成文字檔";
            //openFileDialog1.ShowHelp = true;
            openFileDialog1.FileName = "";              //預設開啟的檔名
            openFileDialog1.DefaultExt = "*.*";
            openFileDialog1.Filter = "文字檔(*.txt)|*.txt|Word檔(*.doc)|*.txt|Excel檔(*.xls)|*.txt|所有檔案(*.*)|*.*";   //存檔類型
            openFileDialog1.FilterIndex = 4;    //預設上述種類的第幾項，由1開始。
            openFileDialog1.RestoreDirectory = true;
            //openFileDialog1.InitialDirectory = Directory.GetCurrentDirectory();   //從目前目錄開始尋找檔案
            openFileDialog1.InitialDirectory = @"C:\______test_files1\"; //預設開啟的路徑
            openFileDialog1.Multiselect = true;    //允許多選檔案
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "已選取檔案個數: " + openFileDialog1.FileNames.Length.ToString() + "\n\n";
                foreach (var filename in openFileDialog1.FileNames)
                {
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
                        //前/後部分binary讀取
                        data = File.ReadAllBytes(filename); //有全讀否? 如果檔案很大 但只要讀一點 會不會太浪費?
                        long len_file = data.Length;

                        FileStream fs = File.Open(filename, FileMode.OpenOrCreate, FileAccess.ReadWrite);
                        //len = System.Convert.ToDouble(fs.Length);
                        len = fs.Length;
                        richTextBox1.Text += "讀取檔案 : " + filename + "\n";
                        richTextBox1.Text += "檔案長度 : " + len_file.ToString() + "\n";
                        len = int.Parse(textBox1.Text);
                        richTextBox1.Text += "讀取長度 : " + len.ToString() + "\n";

                        if (len > len_file)
                            len = len_file;

                        if (radioButton6.Checked == true)
                        {
                            richTextBox1.Text += "讀前面 " + len.ToString() + " 拜\n";
                            BinaryReader br = new BinaryReader(fs);

                            //讀取位元陣列
                            data = br.ReadBytes((int)len);    //用ReadBytes讀取檔案的前幾拜(循序)

                            //釋放資源
                            br.Close();
                            fs.Close();
                        }
                        else
                        {
                            richTextBox1.Text += "讀後面 " + len.ToString() + " 拜\n";
                            Stream stream = fs;
                            stream.Seek(-len, SeekOrigin.End);
                            int result = 0;
                            data = new byte[len];
                            result = stream.Read(data, 0, (int)len);
                            fs.Close();
                            stream.Close();
                        }
                    }

                    if (radioButton8.Checked == true)
                    {
                        //顯示only
                        richTextBox1.Text += "印出資料內容, 長度 " + data.Length.ToString() + " 拜\n";
                        print_data(data);
                    }
                    else
                    {
                        //存檔only

                        string filename2 = filename + "." + new_line.ToString() + ".txt";

                        FileStream fsw = new FileStream(filename2, FileMode.Create, FileAccess.Write);
                        StreamWriter sw;

                        sw = new StreamWriter(fsw, Encoding.GetEncoding("unicode"));   //指名編碼格式

                        for (i = 0; i < len; i++)
                        {
                            sw.Write(data[i].ToString("X2"));
                            if ((i % new_line) == (new_line - 1))
                                sw.Write(data[i].ToString("\n"));
                            else
                                sw.Write(data[i].ToString(" "));
                        }

                        sw.Close();
                        richTextBox1.Text += "存檔完成, 檔名 : " + filename2 + "\n\n";
                    }
                }
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




    }
}
