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
            //都はるみ全曲集２	shift_jis
            byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x91, 0x53, 0x8B, 0xC8, 0x8F, 0x57, 0x82, 0x51 };

            string str = System.Text.Encoding.ASCII.GetString(data);
            richTextBox1.Text += "str = " + str + "\n";
            string filename2 = str + ".txt";

            int len = data.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            byte[] aaaaa = new byte[len];
            for (i = 0; i < len; i++)
            {
                aaaaa[i] = data[i];
            }
            File.WriteAllBytes(filename, aaaaa);
            //File.WriteAllBytes(filename2, aaaaa);
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

        private void button15_Click(object sender, EventArgs e)
        {
            string filename;
            byte[] data = new byte[16];

            filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            //都はるみ全曲集２ 	繁体中文(Big5) 	950 	big5 	B3 A3 3F 3F 3F A5 FE A6 B1 B6 B0 A2 B1
            //は C756
            //る C777
            //み C766

            data[0] = 0xB3;
            data[1] = 0xA3;
            data[2] = 0xC7;
            data[3] = 0x56;
            data[4] = 0xC7;
            data[5] = 0x77;
            data[6] = 0xC7;
            data[7] = 0x66;
            data[8] = 0xA5;
            data[9] = 0xFE;
            data[10] = 0xA6;
            data[11] = 0xB1;
            data[12] = 0xB6;
            data[13] = 0xB0;
            data[14] = 0xA2;
            data[15] = 0xB1;
            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

            filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            //都はるみ全曲集２ 	简体中文(GB2312) 	936 	gb2312 	B6 BC A4 CF A4 EB A4 DF C8 AB C7 FA BC AF A3 B2
            data[0] = 0xB6;
            data[1] = 0xBC;
            data[2] = 0xA4;
            data[3] = 0xCF;
            data[4] = 0xA4;
            data[5] = 0xEB;
            data[6] = 0xA4;
            data[7] = 0xDF;
            data[8] = 0xC8;
            data[9] = 0xAB;
            data[10] = 0xC7;
            data[11] = 0xFA;
            data[12] = 0xBC;
            data[13] = 0xAF;
            data[14] = 0xA3;
            data[15] = 0xB2;
            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

            filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            //都はるみ全曲集２ 	日语(Shift-JIS) 	932 	shift_jis 	93 73 82 CD 82 E9 82 DD 91 53 8B C8 8F 57 82 51
            data[0] = 0x93;
            data[1] = 0x73;
            data[2] = 0x82;
            data[3] = 0xCD;
            data[4] = 0x82;
            data[5] = 0xE9;
            data[6] = 0x82;
            data[7] = 0xDD;
            data[8] = 0x91;
            data[9] = 0x53;
            data[10] = 0x8B;
            data[11] = 0xC8;
            data[12] = 0x8F;
            data[13] = 0x57;
            data[14] = 0x82;
            data[15] = 0x51;
            //寫資料
            File.WriteAllBytes(filename, data);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

            filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";
            //都はるみ全曲集２ 	Unicode 		        1200 	utf-16 		FD 90 6F 30 8B 30 7F 30 68 51 F2 66 C6 96 12 FF     use this
            //都はるみ全曲集２ 	Unicode (Big-Endian) 	1201 	utf-16BE 	90 FD 30 6F 30 8B 30 7F 51 68 66 F2 96 C6 FF 12

            byte[] data2 = new byte[18];

            data2[0] = 0xFF;
            data2[1] = 0xFE;
            data2[2] = 0xFD;
            data2[3] = 0x90;
            data2[4] = 0x6F;
            data2[5] = 0x30;
            data2[6] = 0x8B;
            data2[7] = 0x30;
            data2[8] = 0x7F;
            data2[9] = 0x30;
            data2[10] = 0x68;
            data2[11] = 0x51;
            data2[12] = 0xF2;
            data2[13] = 0x66;
            data2[14] = 0xC6;
            data2[15] = 0x96;
            data2[16] = 0x12;
            data2[17] = 0xFF;
            //寫資料
            File.WriteAllBytes(filename, data2);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";




        }

    }
}
