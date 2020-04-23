using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_ReadWrite_TXT
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("big5"));   //指名編碼格式

            richTextBox2.Text += "RichTextBox1, lines = " + richTextBox1.Lines.Length.ToString() + "\t";
            richTextBox2.Text += "content : \n";
            int i;

            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                richTextBox2.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i].Trim() + "\tlen = \t" + richTextBox1.Lines[i].Trim().Length.ToString() + "\n";
            }
            
            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                sw.WriteLine(richTextBox1.Lines[i]);
            }

            sw.Close();

            richTextBox2.Text += "\n存檔完成, 檔名 : " + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_txt\\琵琶行.txt";
            try
            {
                richTextBox1.LoadFile(filename, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_txt\\琵琶行.txt";
            //法一
            // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
            //richTextBox1.Text = System.IO.File.ReadAllText(filename, System.Text.Encoding.Default);

            //法二
            //讀取檔案
            string y = File.ReadAllText(filename, System.Text.Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "長度：" + y.Length.ToString() + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_txt\\琵琶行.txt";
            try
            {
                StreamReader sr = new StreamReader(filename, Encoding.Default);
                string line = string.Empty;
                int i = 0;

                /*
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    line = sr.ReadLine();            // 讀取文字到 line 變數
                    if (line.Length > 0)
                    {
                    }
                }
                */

                while ((line = sr.ReadLine()) != null)  // 讀取文字到 line 變數
                {
                    i++;
                    richTextBox2.Text += "第" + i.ToString() + "行\t" + line + "\tlength:" + line.Length.ToString() + "\n";
                }
                sr.Close();
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }
        }

        private const int ENCODING_1 = 1;	//encoding type 1, big5
        private const int ENCODING_2 = 2;	//encoding type 2, gb2312
        private const int ENCODING_3 = 3;	//encoding type 3, shift_jis
        private const int ENCODING_4 = 4;	//encoding type 4, unicode

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__text\\Compressor.c";
            read_text_file(filename, ENCODING_1);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__text\\sc\\襟裳岬.txt";
            read_text_file(filename, ENCODING_2);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__text\\jap\\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            read_text_file(filename, ENCODING_3);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__text\\Form1.cs.txt";
            read_text_file(filename, ENCODING_4);
        }

        void read_text_file(string filename, int encodng_type)
        {
            //使用指定編碼，big5、gb2312、shift_jis、unicode不分大小寫

            StreamReader sr;

            switch (encodng_type)
            {
                case ENCODING_1:
                    richTextBox1.Text += "ENCODING_1, Big5\n";
                    //sr = new StreamReader(filename, Encoding.Default);    //Windows預設，就是big5
                    //sr = new StreamReader(filename, Encoding.GetEncoding("big5"));
                    sr = new StreamReader(filename, Encoding.GetEncoding(950)); //same
                    break;
                case ENCODING_2:
                    richTextBox1.Text += "ENCODING_2, gb2312\n";
                    //sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"));    //以gb2312編碼讀取文字檔案中的漢字, same
                    sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"), true);
                    break;
                case ENCODING_3:
                    richTextBox1.Text += "ENCODING_3, Shift_jis\n";
                    sr = new StreamReader(filename, Encoding.GetEncoding("shift_jis"));
                    break;
                case ENCODING_4:
                    richTextBox1.Text += "ENCODING_4, Unicode\n";
                    //sr = new StreamReader(filename, Encoding.Default);    //同
                    //sr = new StreamReader(filename, Encoding.UTF8);       //同
                    sr = new StreamReader(filename, Encoding.Unicode);      //同
                    break;
                default:
                    richTextBox1.Text += "ENCODING unknown, xxxxxxxx\n";
                    sr = new StreamReader(filename, Encoding.Default);  //使用默認編碼格式, 作業系統目前 ANSI 字碼頁的編碼方式
                    break;
            }
            richTextBox2.Text += sr.ReadToEnd();
            sr.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            richTextBox2.Clear();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            write_text_file(filename, ENCODING_1);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            write_text_file(filename, ENCODING_2);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            //write_text_file(filename, ENCODING_3);

            int i;
            byte[] data = { 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x82, 0xCC, 0x8E, 0x4F, 0x93, 0x78, 0x8A, 0x7D };

            int len = data.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] aaaaa = new byte[len];
            for (i = 0; i < len; i++)
            {
                aaaaa[i] = data[i];
            }
            File.WriteAllBytes(filename, aaaaa);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";
            write_text_file(filename, ENCODING_4);
        }

        void write_text_file(string filename, int encodng_type)
        {
            //使用指定編碼，big5、gb2312、shift_jis、unicode不分大小寫

            string content = "";
            content = "漢字內碼陆羽茶经都はるみ123";

            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw;

            switch (encodng_type)
            {
                case ENCODING_1:
                    richTextBox1.Text += "ENCODING_1, Big5\n";
                    try
                    {
                        sw = new StreamWriter(fs, Encoding.GetEncoding("big5"));   //指名編碼格式
                        sw.WriteLine(content);
                        sw.Close();
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                        return;
                    }
                    break;
                case ENCODING_2:
                    richTextBox1.Text += "ENCODING_2, gb2312\n";
                    try
                    {
                        sw = new StreamWriter(fs, Encoding.GetEncoding("gb2312"));   //指名編碼格式
                        sw.WriteLine(content);
                        sw.Close();
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                        return;
                    }
                    break;
                case ENCODING_3:
                    richTextBox1.Text += "ENCODING_3, Shift_jis\n";
                    try
                    {
                        sw = new StreamWriter(fs, Encoding.GetEncoding("shift_jis"));   //指名編碼格式
                        sw.WriteLine(content);
                        sw.Close();
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                        return;
                    }
                    break;
                case ENCODING_4:
                    richTextBox1.Text += "ENCODING_4, Unicode\n";
                    try
                    {
                        //sw = new StreamWriter(fs, Encoding.GetEncoding("utf-8"));   //指名編碼格式 the same
                        sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式
                        sw.WriteLine(content);
                        sw.Close();
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                        return;
                    }
                    break;
                default:
                    richTextBox1.Text += "ENCODING unknown, xxxxxxxx\n";
                    try
                    {
                        sw = new StreamWriter(fs, Encoding.Default);   //指名編碼格式
                        sw.WriteLine(content);
                        sw.Close();
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "xxx錯誤訊息n : " + ex.Message + "\n";
                        return;
                    }
                    break;
            }
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".default.txt";
            richTextBox1.Clear();
            int i;
            for (i = 0; i < 256; i++)
            {
                richTextBox1.Text += i.ToString() + " ";
            }
            File.WriteAllText(filename, richTextBox1.Text, Encoding.Default);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";
        }

    }
}
