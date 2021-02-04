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
            richTextBox2.Text += sr.ReadToEnd();	//讀取所有文字內容
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
            //byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x91, 0x53, 0x8B, 0xC8, 0x8F, 0x57, 0x82, 0x51 };

            //都はるみの三度笠
            byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x82, 0xCC, 0x8E, 0x4F, 0x93, 0x78, 0x8A, 0x7D };

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
            int i;
            byte[] data = new byte[16];     //for TC, SC, JP
            byte[] data2 = new byte[18];    //for unicode

            string filename1 = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            string filename2 = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            string filename3 = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            string filename4 = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";

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

            for (i = 0; i < 16; i++)
                data[i] = data_1[i];

            //寫資料
            File.WriteAllBytes(filename1, data);

            for (i = 0; i < 16; i++)
                data[i] = data_2[i];
            
            //寫資料
            File.WriteAllBytes(filename2, data);

            for (i = 0; i < 16; i++)
                data[i] = data_3[i];

            //寫資料
            File.WriteAllBytes(filename3, data);

            data2[0] = 0xFF;
            data2[1] = 0xFE;
            for (i = 0; i < 16; i++)
                data2[i + 2] = data_4[i];

            //寫資料
            File.WriteAllBytes(filename4, data2);

            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename1 + "\n";
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename2 + "\n";
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename3 + "\n";
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename4 + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            string filename;
            byte[] b;
            string s;

            richTextBox1.Text += "用預設編碼開啟\n";
            filename = "C:\\______test_files\\__text\\Compressor.c";
            b = File.ReadAllBytes(filename);
            s = Encoding.Default.GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用Big5編碼開啟\n";
            filename = "C:\\______test_files\\__text\\Compressor.c";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("big5").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用gb2312編碼開啟\n";
            filename = "C:\\______test_files\\__text\\sc\\001川の流れのように.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("gb2312").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用shift_jis編碼開啟\n";
            filename = "C:\\______test_files\\__text\\jap\\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("shift_jis").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用utf-8編碼開啟\n";
            filename = "C:\\______test_files\\__text\\Form1.cs.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.UTF8.GetString(b);
            richTextBox1.Text += s + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            StreamWriter filewriter = new StreamWriter(filename);
            filewriter.WriteLine("鳳凰臺上鳳凰遊，鳳去臺空江自流");
            filewriter.WriteLine("吳宮花草埋幽徑，晉代衣冠成古邱");
            filewriter.WriteLine("三山半落青又外，二水中分白鷺洲");
            filewriter.WriteLine("總為浮雲能蔽日，長安不見使人愁");
            filewriter.Close();
            richTextBox1.Text += "\n製作TXT檔\t" + filename + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_txt\\琵琶行.txt";
            // Read the whole file to a string array
            string[] input_lines = File.ReadAllLines(filename, Encoding.Default);

            List<string> output_lines = new List<string>();

            int len = input_lines.Length;
            richTextBox1.Text += "共有 " + len.ToString() + " 行\n";
            int n = 0;
            foreach (string line in input_lines)
            {
                n++;
                richTextBox1.Text += n.ToString() + "\t" + line + "\n";
                output_lines.Add("取得資料\t" + line);
            }

            string filename2 = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            // Save the result.
            File.WriteAllLines(filename2, output_lines.ToArray());
            richTextBox1.Text += "\n製作TXT檔\t" + filename2 + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            string filename = "C:\\______test_files\\__RW\\_txt\\琵琶行.txt";
            int i;

            richTextBox1.Text += "\n檔案 : " + filename + "\t內容\n";
            using (TextReader reader = new StreamReader(filename, Encoding.Default))
            {
                i = 0;
                string line;
                line = reader.ReadLine();
                while (line != null)
                {
                    i++;
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + line + "\n";
                    line = reader.ReadLine();
                }
            }
        }
    }
}
