using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                Stream reader = File.Open(openFileDialog1.FileName, FileMode.Open, FileAccess.Read);
                Encoding encoder = null;
                byte[] header = new byte[4];
                // 讀取前四個Byte
                reader.Read(header, 0, 4);
                if (header[0] == 0xFF && header[1] == 0xFE)
                {
                    richTextBox1.Text += "get UniCode File\n";
                    // UniCode File
                    reader.Position = 2;
                    encoder = Encoding.Unicode;
                }
                else if (header[0] == 0xEF && header[1] == 0xBB && header[2] == 0xBF)
                {
                    richTextBox1.Text += "get UTF-8 File\n";
                    // UTF-8 File
                    reader.Position = 3;
                    encoder = Encoding.UTF8;
                }
                else
                {
                    richTextBox1.Text += "get Default Encoding File\n";
                    // Default Encoding File
                    reader.Position = 0;
                    encoder = Encoding.Default;
                }
                byte[] buffer = new byte[32];
                int source = reader.Read(buffer, 0, 32);
                richTextBox1.Text += "source = " + source.ToString() + "\n";
                string sSource = string.Empty;
                int i;

                if (source > 0)
                {
                    if (encoder != Encoding.Default)
                    {
                        sSource += encoder.GetString(buffer, 0, source);
                        //reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                    }
                    else
                    {
                        richTextBox1.Text += "\ntry default\n";
                        encoder = Encoding.Default;
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "\ntry big5\n";
                        encoder = Encoding.GetEncoding("big5");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "\ntry gb2312\n";
                        encoder = Encoding.GetEncoding("gb2312");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";

                        richTextBox1.Text += "\ntry shift_JIS\n";
                        encoder = Encoding.GetEncoding("shift_jis");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox1.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox1.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox1.Text += "\n";



                    }
                }
                reader.Close();

                //richTextBox1.Text += "文件內容: " + sSource + "\n";


            }
            else
            {
                richTextBox1.Text += "未選取檔案\n";

            }

            richTextBox1.Text += "\n文字編碼都是Unicode編碼 Unicode (Big-Endian) 	1201 	utf-16BE\n";


        }

        private void button3_Click(object sender, EventArgs e)
        {
            var badstringFromDatabase = "ƒ`ƒƒƒlƒ‹ƒp[ƒgƒi[‚Ì‘I‘ð";
            var hopefullyRecovered = Encoding.GetEncoding(1252).GetBytes(badstringFromDatabase);
            var oughtToBeJapanese = Encoding.GetEncoding("shift_jis").GetString(hopefullyRecovered);
            richTextBox1.Text += "result : " + oughtToBeJapanese + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //ABCDEFG
            byte[] data_0 = { 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47 };
            //都はるみ全曲集２ 	繁体中文(Big5) 	950 	big5 	B3 A3 3F 3F 3F A5 FE A6 B1 B6 B0 A2 B1
            //は C756 る C777 み C766
            byte[] data_1 = { 0xB3, 0xA3, 0xC7, 0x56, 0xC7, 0x77, 0xC7, 0x66, 0xA5, 0xFE, 0xA6, 0xB1, 0xB6, 0xB0, 0xA2, 0xB1 };
            //都はるみ全曲集２ 	简体中文(GB2312) 	936 	gb2312 	B6 BC A4 CF A4 EB A4 DF C8 AB C7 FA BC AF A3 B2
            byte[] data_2 = { 0xB6, 0xBC, 0xA4, 0xCF, 0xA4, 0xEB, 0xA4, 0xDF, 0xC8, 0xAB, 0xC7, 0xFA, 0xBC, 0xAF, 0xA3, 0xB2 };
            //都はるみ全曲集２ 	日语(Shift-JIS) 	932 	shift_jis 	93 73 82 CD 82 E9 82 DD 91 53 8B C8 8F 57 82 51
            byte[] data_3 = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x91, 0x53, 0x8B, 0xC8, 0x8F, 0x57, 0x82, 0x51 };
            //都はるみ全曲集２ 	Unicode 		        1200 	utf-16 		FD 90 6F 30 8B 30 7F 30 68 51 F2 66 C6 96 12 FF     use this
            //都はるみ全曲集２ 	Unicode (Big-Endian) 	1201 	utf-16BE 	90 FD 30 6F 30 8B 30 7F 51 68 66 F2 96 C6 FF 12
            byte[] data_4 = { 0xFD, 0x90, 0x6F, 0x30, 0x8B, 0x30, 0x7F, 0x30, 0x68, 0x51, 0xF2, 0x66, 0xC6, 0x96, 0x12, 0xFF };

            string str;
            byte[] data;

            data = data_0;
            print_data(data);
            str = Encoding.ASCII.GetString(data);
            richTextBox1.Text += "str = " + str + "\n";

            data = data_1;
            print_data(data);
            str = Encoding.GetEncoding("big5").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += "str = " + str + "\n";

            data = data_2;
            print_data(data);
            str = Encoding.GetEncoding("gb2312").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += "str = " + str + "\n";

            data = data_3;
            print_data(data);
            str = Encoding.GetEncoding("shift_jis").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += "str = " + str + "\n";

            data = data_4;
            print_data(data);
            str = Encoding.GetEncoding("unicode").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += "str = " + str + "\n";
        }

        void print_data(byte[] data)
        {
            int i;
            int len;
            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += data[i].ToString("X2");
                if (i != (len - 1))
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

        }

        void translate_encoding0(byte[] data)
        {
            string str;

            richTextBox1.Text += "\t轉成預設編碼 :\t";
            str = Encoding.Default.GetString(data);
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "\t轉成正中編碼 :\t";
            str = Encoding.GetEncoding("big5").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "\t轉成簡中編碼 :\t";
            str = Encoding.GetEncoding("gb2312").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "\t轉成日文編碼 :\t";
            str = Encoding.GetEncoding("shift_jis").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += str + "\n";

            richTextBox1.Text += "\t轉成統一編碼 :\t";
            str = Encoding.GetEncoding("unicode").GetString(data); // 簡體中文 (GB2312) 
            richTextBox1.Text += str + "\n";
        }

        void translate_encoding(string str)
        {
            byte[] data;
            richTextBox1.Text += "原字串 :\t" + str + "\n";

            richTextBox1.Text += "預設編碼 :\t";
            data = Encoding.Default.GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox1.Text += "正中編碼 :\t";
            data = Encoding.GetEncoding("big5").GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox1.Text += "簡中編碼 :\t";
            data = Encoding.GetEncoding("gb2312").GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox1.Text += "日文編碼 :\t";
            data = Encoding.GetEncoding("shift_jis").GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox1.Text += "統一編碼 :\t";
            data = Encoding.GetEncoding("unicode").GetBytes(str);
            print_data(data);
            translate_encoding0(data);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string str_old;

            str_old = "ABCDEFG";
            translate_encoding(str_old);
            richTextBox1.Text += "\n";

            str_old = "都はるみ全曲集２";
            translate_encoding(str_old);
            richTextBox1.Text += "\n";

            str_old = "琵琶行";
            translate_encoding(str_old);
            richTextBox1.Text += "\n";

        }

    }
}
