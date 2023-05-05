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

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_clear2_Click(object sender, EventArgs e)
        {
            richTextBox2.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //ReadAllLines 1
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            StringBuilder sb = new StringBuilder();

            string[] Txt_All_Lines = File.ReadAllLines(filename, Encoding.Default);

            foreach (string Single_Line in Txt_All_Lines)
            {
                sb.AppendLine(Single_Line);
            }

            richTextBox1.Text += sb.ToString() + "\n";

            //ReadAllLines 2
            //將純文字檔拆成一行一行的字串陣列, 可以去除前後空白
            filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\poem.txt";
            string[] patterns;
            patterns = File.ReadAllLines(filename).Select(i => i.Trim()).Where(i => i != string.Empty).ToArray();
            int len = patterns.Length;
            //richTextBox1.Text += "len = " + len.ToString() + "\n";
            int ii;
            for (ii = 0; ii < len; ii++)
            {
                richTextBox1.Text += patterns[ii] + "\n";
            }

            //ReadAllLines 3
            //開檔ReadAllLines存檔
            filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
            // Read the whole file to a string array
            string[] input_lines = File.ReadAllLines(filename, Encoding.Default);

            List<string> output_lines = new List<string>();

            len = input_lines.Length;
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

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("big5"));   //指名編碼格式

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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
            //法一
            // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
            //richTextBox1.Text = System.IO.File.ReadAllText(filename, Encoding.Default);

            //法二
            //讀取檔案
            string y = File.ReadAllText(filename, Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "長度：" + y.Length.ToString() + "\n";
        }

        private const int ENCODING_1 = 1;	//encoding type 1, big5
        private const int ENCODING_2 = 2;	//encoding type 2, gb2312
        private const int ENCODING_3 = 3;	//encoding type 3, shift_jis
        private const int ENCODING_4 = 4;	//encoding type 4, unicode

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            read_text_file(filename, ENCODING_1);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__text\sc\襟裳岬.txt";
            read_text_file(filename, ENCODING_2);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__text\jap\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            read_text_file(filename, ENCODING_3);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__text\Form1.cs.txt";
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
            richTextBox2.Text += sr.ReadToEnd();	//一次性讀完所有文字內容
            sr.Close();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";

            //創建一個讀取器
            StreamReader sr = new StreamReader(filename);

            //一次性讀取完
            string all_text = sr.ReadToEnd();   //一次性讀完所有文字內容
            richTextBox1.Text += all_text + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
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

        private void button11_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            //write_text_file(filename, ENCODING_3);

            int i;
            //都はるみ全曲集２	shift_jis
            //byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x91, 0x53, 0x8B, 0xC8, 0x8F, 0x57, 0x82, 0x51 };

            //都はるみの三度笠
            byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x82, 0xCC, 0x8E, 0x4F, 0x93, 0x78, 0x8A, 0x7D };

            string str = Encoding.ASCII.GetString(data);
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

        private void button12_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            write_text_file(filename, ENCODING_2);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            write_text_file(filename, ENCODING_1);
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
            filename = @"C:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            b = File.ReadAllBytes(filename);
            s = Encoding.Default.GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用Big5編碼開啟\n";
            filename = @"C:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("big5").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用gb2312編碼開啟\n";
            filename = @"C:\_git\vcs\_1.data\______test_files1\__text\sc\001川の流れのように.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("gb2312").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用shift_jis編碼開啟\n";
            filename = @"C:\_git\vcs\_1.data\______test_files1\__text\jap\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("shift_jis").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用utf-8編碼開啟\n";
            filename = @"C:\_git\vcs\_1.data\______test_files1\__text\Form1.cs.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.UTF8.GetString(b);
            richTextBox1.Text += s + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            StreamWriter sw = new StreamWriter(filename);
            sw.WriteLine("鳳凰臺上鳳凰遊，鳳去臺空江自流");
            sw.WriteLine("吳宮花草埋幽徑，晉代衣冠成古邱");
            sw.WriteLine("三山半落青又外，二水中分白鷺洲");
            sw.WriteLine("總為浮雲能蔽日，長安不見使人愁");
            sw.Close();
            richTextBox1.Text += "\n製作TXT檔\t" + filename + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //ReadLine 1
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
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

            //ReadLine 2
            try
            {
                StreamReader sr = new StreamReader(filename, Encoding.Default);
                string line = string.Empty;
                while ((line = sr.ReadLine()) != null)
                {
                    richTextBox1.Text += line + "\n";
                }
            }
            catch
            {

            }

            //ReadLine 3

            //一行一行讀取文字檔
            filename = @"C:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\eula.3081a.txt";

            StreamReader SReader = new StreamReader(filename, Encoding.Default);
            string strLine = string.Empty;
            while ((strLine = SReader.ReadLine()) != null)
            {
                richTextBox1.Text += strLine + "\n";
            }



            //ReadLine 4

            filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
            try
            {
                StreamReader sr = new StreamReader(filename, Encoding.Default);
                string line = string.Empty;
                i = 0;

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

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //文字檔的整行寫入與讀出

            //寫入文字檔 
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_txt\txt_rw.txt";

            //StreamWriter sw = new StreamWriter(filename); // true 是資料可附加至檔案, open write
            StreamWriter sw = new StreamWriter(filename, true); // true 是資料可附加至檔案 open write append

            int i;
            int len = richTextBox1.Lines.Length;
            //richTextBox2.Text += "lines = " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox2.Text += "i = " + i.ToString() + " : " + richTextBox1.Lines[i] + "\n";
                sw.WriteLine(richTextBox1.Lines[i]); // 寫入一行
            }

            /*
            sw.WriteLine("白日依山盡"); // 寫入一行
            sw.WriteLine("黃河入海流");
            sw.WriteLine("欲窮千里目");
            sw.WriteLine("更上一層樓");
            */
            sw.Close(); // 關閉檔案

            //從文字檔讀出
            StreamReader sr = new StreamReader(filename); // 開啟檔案

            string str;  // 宣告字串變數

            /* 方法一
            richTextBox2.Clear();   // 文字方塊 先清空
            str = sr.ReadLine(); // 讀出一行
            while (str != null)
            {
                richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
                str = sr.ReadLine();
            }
            */

            //方法二
            richTextBox2.Clear();   // 文字方塊 先清空
            while (sr.Peek() != -1) // 傳回下一個可供使用的字元，但不消耗它
            {
                str = sr.ReadLine(); // 讀出一行 到字串 str
                richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
            }

            sr.Close(); // 關閉檔案
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //第一個檔案
            string filename1 = @"C:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            //第二個檔案
            string filename2 = @"C:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            //第三個檔案
            string filename3 = @"C:\_git\vcs\_1.data\______test_files1\compare\ssss.txt";

            StreamReader sr1;
            StreamReader sr2;
            StreamReader sr3;

            sr1 = new StreamReader(filename1);     //創建StreamReader對象
            sr2 = new StreamReader(filename2);     //創建StreamReader對象

            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))    //讀取文件內容并判斷
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 不相同\n";

            sr1 = new StreamReader(filename1);     //創建StreamReader對象
            sr3 = new StreamReader(filename3);     //創建StreamReader對象
            if (object.Equals(sr1.ReadToEnd(), sr3.ReadToEnd()))    //讀取文件內容并判斷
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 不相同\n";

            sr2 = new StreamReader(filename2);     //創建StreamReader對象
            sr3 = new StreamReader(filename3);     //創建StreamReader對象
            if (object.Equals(sr2.ReadToEnd(), sr3.ReadToEnd()))    //讀取文件內容并判斷
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 不相同\n";
        }

        private void button22_Click(object sender, EventArgs e)
        {
            int i;
            int N = 10;
            //建立一個txt檔
            string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            richTextBox1.Text += "建立一個txt檔, 檔名 : " + filename + "\n";

            FileInfo finfo1 = new FileInfo(filename);
            StreamWriter sw = finfo1.CreateText();
            for (i = 0; i < N; i++)
            {
                sw.WriteLine("aaa" + i.ToString());
                sw.WriteLine("bbb" + i.ToString());
                sw.WriteLine("ccc" + i.ToString());
            }
            sw.Flush();
            sw.Close();

            richTextBox1.Text += "讀取一個txt檔, 檔名 : " + filename + "\n";

            FileInfo finfo2 = new FileInfo(filename);
            StreamReader sr = finfo2.OpenText();

            i = 0;
            while (sr.Peek() >= 0)
            {
                richTextBox1.Text += "第1筆資料 : " + sr.ReadLine() + "\n";
                richTextBox1.Text += "第2筆資料 : " + sr.ReadLine() + "\n";
                richTextBox1.Text += "第3筆資料 : " + sr.ReadLine() + "\n";

                i++;
            }
            sr.Close();
            richTextBox1.Text += "共取得了 " + i.ToString() + " 筆資料\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //RW test

            string filepath = "this is filepath";
            string timer = "ttttt 1";
            string timer2 = "ttttt 2";
            string username = "david";
            string pwd = "123456";

            StreamWriter sw = new StreamWriter("info.txt");
            sw.WriteLine(filepath);
            sw.Flush();
            sw.WriteLine(timer);
            sw.Flush();
            sw.WriteLine(timer2);
            sw.Flush();
            sw.WriteLine(username);
            sw.Flush();
            sw.WriteLine(pwd);
            sw.Flush();
            sw.Close();
            richTextBox1.Text += "寫入成功!\n";

            string filepathb = string.Empty;
            string timerb = string.Empty;
            string timer2b = string.Empty;
            string usernameb = string.Empty;
            string pwdb = string.Empty;

            StreamReader sr = new StreamReader("info.txt");

            filepathb = sr.ReadLine();
            timerb = sr.ReadLine();
            timer2b = sr.ReadLine();
            usernameb = sr.ReadLine();
            pwdb = sr.ReadLine();

            sr.Close();
            sr.Dispose();
            GC.Collect();

            richTextBox1.Text += "filepathb = " + filepathb + "\n";
            richTextBox1.Text += "timerb = " + timerb + "\n";
            richTextBox1.Text += "timer2b = " + timer2b + "\n";
            richTextBox1.Text += "usernameb = " + usernameb + "\n";
            richTextBox1.Text += "pwdb = " + pwdb + "\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //檔案置換文字

            string filename = @"C:\_git\vcs\_3.cuda\Samples\5_Domain_Specific\binomialOptions\binomialOptions_vs2022.vcxproj";
            string pattern1 = @"CUDAPropsPath)\CUDA 11.6.";
            string pattern2 = @"CUDAPropsPath)\CUDA 11.7.";

            int flag_replace_pattern = 0;

            flag_replace_pattern = file_replace_pattern(filename,  pattern1, pattern2);

            if (flag_replace_pattern == 0)
            {
                richTextBox2.Text += "置換成功\n";
            }
            else if (flag_replace_pattern == 1)
            {
                richTextBox2.Text += "原始檔案不存在\n";
            }
            else if (flag_replace_pattern == 2)
            {
                richTextBox2.Text += "沒有找到pattern, 不用置換pattern\n";
            }
            else
            {
                richTextBox2.Text += "其他錯誤\n";
            }
        }

        int file_replace_pattern(string filename1, string pattern1, string pattern2)
        {
            bool flag_need_replace = false;

            if (File.Exists(filename1) == false)
            {
                richTextBox2.Text += "檔案 : " + filename1 + ", 不存在\n";
                return 1;   //1: 原始檔案不存在
            }

            string filename2 = filename1 + ".tmp";

            //從文字檔讀出
            StreamReader sr = new StreamReader(filename1); // 開啟檔案

            string str;  // 宣告字串變數

            str = sr.ReadLine(); // 讀出一行
            while (str != null)
            {
                //richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號

                if (str.Contains(pattern1))
                {
                    //richTextBox2.Text += "有找到pattern, 要置換pattern\n";
                    //richTextBox2.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
                    flag_need_replace = true;
                    break;

                }
                str = sr.ReadLine();
            }
            sr.Close(); // 關閉檔案

            if (flag_need_replace == false)
            {
                //richTextBox2.Text += "沒有找到pattern, 不用置換pattern\n";
                return 2;   //2: 沒有找到pattern, 不用置換pattern
            }
            else
            {
                //richTextBox2.Text += "有找到pattern, 要置換pattern\n";
            }

            if (File.Exists(filename2) == true)
            {
                //richTextBox2.Text += "delete filename2\n";
                File.Delete(filename2);
            }

            sr = new StreamReader(filename1); // 開啟檔案
            StreamWriter sw = new StreamWriter(filename2); // true 是資料可附加至檔案, open write
            //StreamWriter sw = new StreamWriter(filename2, true); // true 是資料可附加至檔案 open write append

            str = sr.ReadLine(); // 讀出一行
            while (str != null)
            {
                if (str.Contains(pattern1))
                {
                    //richTextBox2.Text += "replace\n";
                    str = str.Replace(pattern1, pattern2);
                }

                sw.WriteLine(str); // 寫入一行

                str = sr.ReadLine();
            }
            sr.Close(); // 關閉檔案
            sw.Close(); // 關閉檔案


            if (File.Exists(filename1) == true)
            {
                File.Delete(filename1);
            }
            File.Move(filename2, filename1);
            return 0;   //置換成功
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //資料夾內 檔案置換文字

            //撈出所有圖片檔 並存成一個List
            string foldername = @"C:\_git\vcs\_3.cuda\Samples";

            filenames.Clear();

            string extension = ".vcxproj";

            GetAllFiles(foldername, extension);
            int len = filenames.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            string pattern1 = @"CUDAPropsPath)\CUDA 11.6.";
            string pattern2 = @"CUDAPropsPath)\CUDA 11.7.";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += filenames[i] + "\n";


                int flag_replace_pattern = 0;

                flag_replace_pattern = file_replace_pattern(filenames[i], pattern1, pattern2);
            }
        }

        List<String> filenames = new List<String>();
        //多層 且指明副檔名
        public void GetAllFiles(string foldername, string extension)
        {
            DirectoryInfo di = new DirectoryInfo(foldername);
            //richTextBox1.Text += "資料夾 : " + di.FullName + "\n";
            FileSystemInfo[] fileinfo = di.GetFileSystemInfos();
            foreach (FileSystemInfo fi in fileinfo)
            {
                if (fi is DirectoryInfo)
                {
                    GetAllFiles(((DirectoryInfo)fi).FullName, extension);
                }
                else
                {
                    string fullname = fi.FullName;
                    string shortname = fi.Name;
                    string ext = fi.Extension.ToLower();
                    string forename = shortname.Substring(0, shortname.Length - ext.Length);    //前檔名

                    if (ext == extension)
                    {
                        //richTextBox1.Text += "長檔名: " + fullname + "\t副檔名: " + ext + "\n";
                        //richTextBox1.Text += "短檔名: " + shortname + "\n";
                        //richTextBox1.Text += "前檔名: " + forename + "\n";
                        filenames.Add(fullname);
                    }
                }
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {
        }
    }
}




