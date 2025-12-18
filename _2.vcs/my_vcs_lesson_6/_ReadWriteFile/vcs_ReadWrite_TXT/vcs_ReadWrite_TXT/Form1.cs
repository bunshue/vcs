using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for File
using System.Text.RegularExpressions;

namespace vcs_ReadWrite_TXT
{
    public partial class Form1 : Form
    {
        string line = string.Empty;
        string some_text = "白日依山盡，黃河入海流。 欲窮千里目，更上一層樓。";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            richTextBox1.Size = new Size(440, 640);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);

            this.Size = new Size(1100+210, 700);
        }

        private void bt_clear1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //File.ReadAllLines, 將純文字檔拆成一行一行的字串陣列

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\poem.txt";

            //File.ReadAllLines 將純文字檔拆成一行一行的字串陣列
            string[] all_lines = File.ReadAllLines(filename, Encoding.Default);

            foreach (string line in all_lines)
            {
                richTextBox1.Text += line + "\n";
            }

            for (int i = 0; i < all_lines.Length; i++)
            {
                richTextBox1.Text += all_lines[i] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //開檔ReadAllLines存檔
            filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";

            //File.ReadAllLines 將純文字檔拆成一行一行的字串陣列
            all_lines = File.ReadAllLines(filename, Encoding.Default);

            List<string> all_lines2 = new List<string>();
            foreach (string line in all_lines)
            {
                richTextBox1.Text += line + "\n";
                all_lines2.Add("取得資料\t" + line);
            }

            string filename2 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            //存檔
            File.WriteAllLines(filename2, all_lines2.ToArray());
            richTextBox1.Text += "\n製作TXT檔\t" + filename2 + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);

            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("big5"));   //指名編碼格式

            richTextBox1.Text += "RichTextBox1, 行數 : " + richTextBox1.Lines.Length.ToString() + "\t";
            richTextBox1.Text += "內容 :\n";
            int i;

            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + richTextBox1.Lines[i].Trim() + "\t長度 :\t" + richTextBox1.Lines[i].Trim().Length.ToString() + "\n";
            }

            for (i = 0; i < richTextBox1.Lines.Length; i++)
            {
                sw.WriteLine(richTextBox1.Lines[i]);
            }
            sw.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //File.ReadAllText / File.WriteAllText 大全

            //ReadAllText 讀取文件
            //使用ReadAllText可以直接讀取文件中的內容, 格式為:
            //File.ReadAllText(檔案位置及名稱)

            //WriteAllText 寫入/建立檔案
            //透過WriteAllText可以將文字寫入檔案(如果檔案不存在, 會自動建立), 格式為:
            //File.WriteAllText(檔案位置及名稱, 字串);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";
            //法一
            // 運用 ReadAllText 方法 (String, Encoding), 其中 Encoding 針對您txt檔案的編碼做變更, 讀出的資料才不會有亂碼
            //richTextBox1.Text += System.IO.File.ReadAllText(filename, Encoding.Default);

            //法二
            //讀取檔案
            //運用 ReadAllText 方法 (String, Encoding), 其中 Encoding 針對您txt檔案的編碼做變更, 讀出的資料才不會有亂碼
            string y = File.ReadAllText(filename, Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "長度 : " + y.Length.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //AppendAllText 將字串插入文件內容尾端
            richTextBox1.Text += "寫一筆資料到檔案尾端\n";
            filename = "myfilename.txt";
            File.AppendAllText(filename, " 寫一筆資料到檔案尾端");

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            filename = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".default.txt";
            //File.WriteAllText(filename, some_text);
            File.WriteAllText(filename, some_text, Encoding.Default);
            richTextBox1.Text += "已存檔 : " + filename + "\n";

            //讀取檔案
            y = File.ReadAllText(filename);
            richTextBox1.Text += "檔案內容 : " + y + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //ReadLine 1
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";

            FileStream fs = File.Open(filename, FileMode.Open);
            StreamReader sr = new StreamReader(fs);

            //read

            sr.Dispose();
            fs.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "sr.Read, 一次讀一拜\n";

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\vcs_test.txt";
            FileInfo fi = new FileInfo(filename);
            StreamReader sr = fi.OpenText();
            while (sr.Peek() > 0)
            {
                richTextBox1.Text += (char)sr.Read();
            }
            sr.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //StreamReader 大全

            //sr.ReadToEnd()  //讀取所有文字內容

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";
            filename = @"D:\_git\vcs\_1.data\______test_files1\read_file.txt";
            StreamReader sr = new StreamReader(filename, Encoding.Default);    //Windows預設, 就是big5
            sr = new StreamReader(filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            //FileInfo fi = new FileInfo(filename);same
            //sr = fi.OpenText();same            

            string all_text = sr.ReadToEnd();  //讀取所有文字內容
            richTextBox1.Text += all_text + "\n";
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //StreamWriter 大全


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private const int ENCODING_1 = 1;	//encoding type 1, big5
        private const int ENCODING_2 = 2;	//encoding type 2, gb2312
        private const int ENCODING_3 = 3;	//encoding type 3, shift_jis
        private const int ENCODING_4 = 4;	//encoding type 4, unicode

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "使用各種編碼讀取/寫入檔案\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取big5檔案
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            read_text_file(filename1, ENCODING_1);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取gb2312檔案
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\__text\sc\襟裳岬.txt";
            read_text_file(filename2, ENCODING_2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取shift_jis檔案
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\__text\jap\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            read_text_file(filename3, ENCODING_3);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取unicode檔案
            string filename4 = @"D:\_git\vcs\_1.data\______test_files1\__text\Form1.cs.txt";
            read_text_file(filename4, ENCODING_4);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //寫入big5檔案
            filename1 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            write_text_file(filename1, ENCODING_1);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //寫入gb2312檔案
            filename2 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            write_text_file(filename2, ENCODING_2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //寫入unicode檔案
            filename4 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";
            write_text_file(filename4, ENCODING_4);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        void read_text_file(string filename, int encodng_type)
        {
            //使用指定編碼, big5、gb2312、shift_jis、unicode不分大小寫

            StreamReader sr;

            switch (encodng_type)
            {
                case ENCODING_1:
                    richTextBox1.Text += "ENCODING_1, Big5\n";
                    //sr = new StreamReader(filename, Encoding.Default);    //Windows預設, 就是big5
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
            string all_text = sr.ReadToEnd();  //讀取所有文字內容
            richTextBox1.Text += all_text + "\n";
            sr.Close();
        }

        void write_text_file(string filename, int encodng_type)
        {
            //使用指定編碼，big5、gb2312、shift_jis、unicode不分大小寫

            string content = "漢字內碼陆羽茶经都はるみ123";

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
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //寫入shift_jis檔案

            string filename = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            //write_text_file(filename, ENCODING_3);

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
            int i;
            for (i = 0; i < len; i++)
            {
                aaaaa[i] = data[i];
            }
            File.WriteAllBytes(filename, aaaaa);
            //File.WriteAllBytes(filename2, aaaaa);
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //File.ReadAllBytes
            richTextBox1.Text += "File.ReadAllBytes()\n";

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes.bmp";
            string filename2 = "tmp_test_WriteAllBytes.bmp";

            //讀取資料
            byte[] b = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案 : " + filename1 + ", 長度 : " + b.Length.ToString() + "\n";

            //打印資料
            string bytes = string.Empty;
            foreach (byte by in b)
            {
                bytes += by.ToString("X2");
            }
            richTextBox1.Text += bytes;

            //修改資料
            for (int i = 54; i < b.Length; i++)
            {
                if (b[i] == 0xCC)
                    b[i] = 0xFF;
            }

            //寫資料
            File.WriteAllBytes(filename2, b);
            richTextBox1.Text += "寫成檔案" + filename2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            byte[] data_write = new byte[data_read.Length / 2];

            for (int i = 0; i < data_read.Length / 2; i++)
            {
                data_write[i] = data_read[i];
            }

            //寫資料
            //File.WriteAllBytes(filename2, data_write);
            string zzz = Convert.ToString(data_write);
            File.WriteAllText(filename2, zzz);
            richTextBox1.Text += "寫成檔案" + filename2 + "\n";
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string filename;
            string text;

            richTextBox1.Text += "用預設編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            b = File.ReadAllBytes(filename);
            text = Encoding.Default.GetString(b);
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "用Big5編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            b = File.ReadAllBytes(filename);
            text = Encoding.GetEncoding("big5").GetString(b);
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "用gb2312編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\sc\001川の流れのように.txt";
            b = File.ReadAllBytes(filename);
            text = Encoding.GetEncoding("gb2312").GetString(b);
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "用shift_jis編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\jap\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            b = File.ReadAllBytes(filename);
            text = Encoding.GetEncoding("shift_jis").GetString(b);
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "用utf-8編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Form1.cs.txt";
            b = File.ReadAllBytes(filename);
            text = Encoding.UTF8.GetString(b);
            richTextBox1.Text += text + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //File.WriteAllBytes
            int i;
            byte[] data = new byte[16];     //for TC, SC, JP
            byte[] data2 = new byte[18];    //for unicode

            string filename1 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            string filename2 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            string filename3 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            string filename4 = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";

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
            {
                data[i] = data_2[i];
            }

            //寫資料
            File.WriteAllBytes(filename2, data);

            for (i = 0; i < 16; i++)
            {
                data[i] = data_3[i];
            }

            //寫資料
            File.WriteAllBytes(filename3, data);

            data2[0] = 0xFF;
            data2[1] = 0xFE;
            for (i = 0; i < 16; i++)
            {
                data2[i + 2] = data_4[i];
            }

            //寫資料
            File.WriteAllBytes(filename4, data2);

            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename1 + "\n";
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename2 + "\n";
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename3 + "\n";
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename4 + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //文字檔的整行寫入與讀出
            //WriteLine 一次寫入檔案內一行資料
            //ReadLine  一次讀取檔案內一行資料
            richTextBox1.Text += "WriteLine寫入一行 / ReadLine讀出一行\n";

            string string1 = "白日依山盡";
            string string2 = "黃河入海流";
            string string3 = "欲窮千里目";
            string string4 = "更上一層樓";

            string filename = "tmp_poem.txt";
            //StreamWriter sw = new StreamWriter(filename); // true 是資料可附加至檔案, open write
            StreamWriter sw = new StreamWriter(filename, true); // true 是資料可附加至檔案 open write append

            sw.WriteLine("王之渙登鸛鵲樓"); // 寫入一行
            sw.Flush();
            sw.WriteLine(string1);  // 寫入一行
            sw.Flush();
            sw.WriteLine(string2);  // 寫入一行
            sw.Flush();
            sw.WriteLine(string3);  // 寫入一行
            sw.Flush();
            sw.WriteLine(string4);  // 寫入一行
            sw.Flush();
            sw.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //從文字檔讀出

            string string1b = string.Empty;
            string string2b = string.Empty;
            string string3b = string.Empty;
            string string4b = string.Empty;
            string string5b = string.Empty;

            filename = "tmp_poem.txt";
            StreamReader sr = new StreamReader(filename);

            string1b = sr.ReadLine();// 讀出一行
            string2b = sr.ReadLine();// 讀出一行
            string3b = sr.ReadLine();// 讀出一行
            string4b = sr.ReadLine();// 讀出一行
            string5b = sr.ReadLine();// 讀出一行

            sr.Close();
            sr.Dispose();
            GC.Collect();

            richTextBox1.Text += "讀出第1行資料 : " + string1b + "\n";
            richTextBox1.Text += "讀出第2行資料 : " + string2b + "\n";
            richTextBox1.Text += "讀出第3行資料 : " + string3b + "\n";
            richTextBox1.Text += "讀出第4行資料 : " + string4b + "\n";
            richTextBox1.Text += "讀出第5行資料 : " + string5b + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //從文字檔讀出

            filename = "tmp_poem.txt";
            //FileInfo fi = new FileInfo(filename); same
            //sr = fi.OpenText();//StreamReader  same
            sr = new StreamReader(filename);

            //while (sr.Peek() > 0) same
            while (sr.Peek() != -1) // 傳回下一個可供使用的字元, 但不消耗它
            {
                line = sr.ReadLine();// 讀出一行
                richTextBox1.Text += line + "\n";
            }
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            filename = "tmp_poem.txt";

            //一行一行讀取文字檔
            //sr = new StreamReader(filename, Encoding.Default);
            sr = new StreamReader(filename);
            while ((line = sr.ReadLine()) != null)// 讀出一行
            {
                richTextBox1.Text += line + "\n";
            }
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            filename = "tmp_poem.txt";

            //sr = new StreamReader(filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            sr = new StreamReader(filename);

            int i = 0;
            while (!sr.EndOfStream)
            {               // 每次讀取一行, 直到檔尾
                i++;
                line = sr.ReadLine(); // 讀出一行
                richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\n";
            }
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //ReadLine()


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //StreamReader + StreamWriter 大全

            int i;
            int N = 5;
            string filename = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileInfo fi1 = new FileInfo(filename);
            StreamWriter sw = fi1.CreateText();
            for (i = 0; i < N; i++)
            {
                sw.WriteLine("aaa" + i.ToString());
                sw.WriteLine("bbb" + i.ToString());
                sw.WriteLine("ccc" + i.ToString());
            }
            sw.Flush();
            sw.Close();

            richTextBox1.Text += "已存檔 : " + filename + "\n";

            FileInfo fi2 = new FileInfo(filename);
            StreamReader sr = fi2.OpenText();

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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {
            //編碼相關

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //比較兩個檔案
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";

            StreamReader sr1 = new StreamReader(filename1);     //創建StreamReader對象
            StreamReader sr2 = new StreamReader(filename2);     //創建StreamReader對象

            sr1 = new StreamReader(filename1, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            sr2 = new StreamReader(filename2, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))    //讀取文件內容並判斷
            {
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 完全相同\n";
            }
            else
            {
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 不相同\n";
            }

            sr1.Close();
            sr2.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //比較兩個檔案
            filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";

            if (FileCompare(filename1, filename2) == true)
            {
                richTextBox1.Text += "兩個檔案相同\n";
            }
            else
            {
                richTextBox1.Text += "兩個檔案不相同\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private bool FileCompare(string file1, string file2)
        {
            //　判斷相同的文件是否被參考兩次。
            if (file1 == file2)
            {
                return true;
            }
            int file1byte = 0;
            int file2byte = 0;
            using (FileStream fs1 = new FileStream(file1, FileMode.Open), fs2 = new FileStream(file2, FileMode.Open))
            {
                //　檢查文件大小。如果兩個文件的大小並不相同,則視為不相同。
                if (fs1.Length != fs2.Length)
                {
                    // 關閉文件。
                    fs1.Close();
                    fs2.Close();
                    return false;
                }
                //　逐一比較兩個文件的每一個字節, 直到發現不相符或已到達文件尾端為止。
                do
                {
                    // 從每一個文件讀取一個字節。
                    file1byte = fs1.ReadByte();
                    file2byte = fs2.ReadByte();
                }
                while ((file1byte == file2byte) && (file1byte != -1));
                // 關閉文件。
                fs1.Close();
                fs2.Close();
            }
            //　返回比較的結果。在這個時候, 只有當兩個文件的內容完全相同時, "file1byte" 才會等於 "file2byte"。
            return ((file1byte - file2byte) == 0);
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //儲存檔案 多種
            //儲存檔案1
            string filename = @"tmp_vcs_test.txt";

            FileInfo fi = new FileInfo(filename);
            StreamWriter sw = fi.CreateText();
            //sw = File.CreateText(filename); same

            sw.WriteLine("AAAAAAAAAAAAAAAAAAAAAA");
            sw.Write(some_text);

            sw.Flush();
            sw.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //儲存檔案4     儲存二進位檔
            filename = "tmp_save_file_test.bin";
            byte[] cbuffer = new byte[256];
            for (int i = 0; i < 256; i++)
                cbuffer[i] = (byte)i;

            // 建立檔案串流
            FileStream fs = new FileStream(filename, FileMode.OpenOrCreate, FileAccess.Write);
            //byte[] byteSave = Encoding.ASCII.GetBytes(txtHTML.Text.ToString());

            // 以FileStream類別的Write方法將HTML內容寫入檔案中
            fs.Write(cbuffer, 0, cbuffer.Length);

            // 關閉檔案串流
            fs.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //儲存檔案5
            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };
            //把資料儲存成檔案
            filename = "tmp_aaaaaaa.txt";
            //FileStream
            fs = File.Open(filename, FileMode.Create);
            sw = new StreamWriter(fs);
            for (int ii = 0; ii < 16; ii++)
            {
                line = ii.ToString() + "\t" + x[ii].ToString() + "\t" + y[ii].ToString();
                sw.WriteLine(line);
            }
            sw.Dispose();
            fs.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //檔案置換文字

            string filename = @"D:\_git\vcs\_3.cuda\Samples\5_Domain_Specific\binomialOptions\binomialOptions_vs2022.vcxproj";
            string pattern1 = @"CUDAPropsPath)\CUDA 11.6.";
            string pattern2 = @"CUDAPropsPath)\CUDA 11.7.";

            int flag_replace_pattern = 0;

            flag_replace_pattern = file_replace_pattern(filename, pattern1, pattern2);

            if (flag_replace_pattern == 0)
            {
                richTextBox1.Text += "置換完成\n";
            }
            else if (flag_replace_pattern == 1)
            {
                richTextBox1.Text += "原始檔案不存在\n";
            }
            else if (flag_replace_pattern == 2)
            {
                richTextBox1.Text += "沒有找到pattern, 不用置換pattern\n";
            }
            else
            {
                richTextBox1.Text += "其他錯誤\n";
            }
        }

        int file_replace_pattern(string filename1, string pattern1, string pattern2)
        {
            bool flag_need_replace = false;

            if (File.Exists(filename1) == false)
            {
                richTextBox1.Text += "檔案 : " + filename1 + ", 不存在\n";
                return 1;   //1: 原始檔案不存在
            }

            string filename2 = filename1 + ".tmp";

            //從文字檔讀出
            StreamReader sr = new StreamReader(filename1); // 開啟檔案

            string line = string.Empty;
            line = sr.ReadLine(); // 讀出一行
            while (line != null)
            {
                //richTextBox1.Text += str + "\n";    //一次讀一行 每一行都要加換行符號

                if (line.Contains(pattern1))
                {
                    //richTextBox1.Text += "有找到pattern, 要置換pattern\n";
                    //richTextBox1.Text += str + "\n";    //一次讀一行 每一行都要加換行符號
                    flag_need_replace = true;
                    break;
                }
                line = sr.ReadLine(); // 讀出一行
            }
            sr.Close(); // 關閉檔案

            if (flag_need_replace == false)
            {
                //richTextBox1.Text += "沒有找到pattern, 不用置換pattern\n";
                return 2;   //2: 沒有找到pattern, 不用置換pattern
            }
            else
            {
                //richTextBox1.Text += "有找到pattern, 要置換pattern\n";
            }

            if (File.Exists(filename2) == true)
            {
                //richTextBox1.Text += "delete filename2\n";
                File.Delete(filename2);
            }

            sr = new StreamReader(filename1); // 開啟檔案
            StreamWriter sw = new StreamWriter(filename2); // true 是資料可附加至檔案, open write
            //StreamWriter sw = new StreamWriter(filename2, true); // true 是資料可附加至檔案 open write append

            line = sr.ReadLine(); // 讀出一行
            while (line != null)
            {
                if (line.Contains(pattern1))
                {
                    //richTextBox1.Text += "replace\n";
                    line = line.Replace(pattern1, pattern2);
                }

                sw.WriteLine(line); // 寫入一行

                line = sr.ReadLine(); // 讀出一行
            }
            sr.Close(); // 關閉檔案
            sw.Close(); // 關閉檔案

            if (File.Exists(filename1) == true)
            {
                File.Delete(filename1);
            }
            File.Move(filename2, filename1);
            return 0;   //置換完成
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //資料夾內 檔案置換文字

            //撈出所有圖片檔 並存成一個List
            string foldername = @"D:\_git\vcs\_3.cuda\Samples";

            filenames.Clear();

            string extension = ".vcxproj";

            GetAllFiles(foldername, extension);
            int len = filenames.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            string pattern1 = @"CUDAPropsPath)\CUDA 11.6.";
            string pattern2 = @"CUDAPropsPath)\CUDA 11.7.";

            for (int i = 0; i < len; i++)
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
            //接續寫入檔案

            string filename = "tmp_append_text.txt";

            StreamWriter sw;

            if (File.Exists(filename) == false) //確認檔案是否存在
            {
                //新建檔案
                richTextBox1.Text += "檔案 : " + filename + " 不存在, 建立之。";
                sw = File.CreateText(filename);
                sw.Write(some_text);
                sw.Close();
            }
            else
            {
                //附加檔案
                richTextBox1.Text += "檔案 : " + filename + " 存在, 開啟, 並接續寫入資料";

                //sw = File.AppendText(filename); same
                FileInfo fi = new FileInfo(filename);
                sw = fi.AppendText();

                sw.WriteLine("寫入文字資料AAAAAAAA" + DateTime.Now.ToString(), Encoding.Default);
                sw.Write(some_text);
                sw.Flush();
                sw.Close();
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            string filename = "tmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            //XXX richTextBox1.SaveFile(filename, RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔, 這樣會出現怪字型, 還是一行一行儲存比較好

            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式            
            sw.Write(some_text);
            sw.Close();
            richTextBox1.Text += "已存檔 : " + filename + "\n";
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button28_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "各種 Directory/File 操作\n";

            // 目前路徑
            string folderpath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前路徑: " + folderpath + "\n";

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";
            string filename2 = "tmp_article.txt";
            string filename3 = "tmp_article_new.txt";

            string path = @"D:\_git\vcs\_1.data\______test_files1\";

            if (Directory.Exists(path) == false)
            {
                richTextBox1.Text += "路徑不存在, 建立之。\n";
                Directory.CreateDirectory(path);
            }

            if (File.Exists(path + filename1) == false)
            {
                richTextBox1.Text += "檔案不存在, 建立之。\n";
            }

            if (File.Exists(filename2) == false)
            {
                richTextBox1.Text += "檔案 : " + filename2 + ", 不存在, 建立之\n";
                File.Copy(filename1, filename2);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "將檔案 : " + filename2 + ", 改檔名成 : " + filename3 + "\n";
            File.Move(filename2, filename3);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            if (File.Exists(filename3) == true)
            {
                richTextBox1.Text += "檔案 : " + filename3 + ", 已存在, 刪除之\n";
                richTextBox1.Text += "直接刪除, 不放進垃圾桶\n";
                File.Delete(filename3);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            //File.SetAttributes(filename, FileAttributes.Hidden);//隱藏
            richTextBox1.Text += File.GetAttributes(filename) + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //取得檔案資訊 FileInfo

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            FileInfo fi = new FileInfo(filename);
            richTextBox1.Text += "Name : " + fi.Name + "\n";
            richTextBox1.Text += "FullName : " + fi.FullName + "\n";
            richTextBox1.Text += "Extension : " + fi.Extension + "\n";
            richTextBox1.Text += "Directory : " + fi.Directory + "\n";
            richTextBox1.Text += "DirectoryName : " + fi.DirectoryName + "\n";
            richTextBox1.Text += "長度 : " + fi.Length.ToString() + "\n";
            richTextBox1.Text += "IsReadOnly : " + fi.IsReadOnly + "\n";
            richTextBox1.Text += "CreationTime : " + fi.CreationTime + "\n";
            richTextBox1.Text += "CreationTimeUtc : " + fi.CreationTimeUtc + "\n";
            richTextBox1.Text += "LastAccessTime : " + fi.LastAccessTime + "\n";
            richTextBox1.Text += "LastAccessTimeUtc : " + fi.LastAccessTimeUtc + "\n";
            richTextBox1.Text += "LastWriteTime : " + fi.LastWriteTime + "\n";
            richTextBox1.Text += "LastWriteTimeUtc : " + fi.LastWriteTimeUtc + "\n";
        }


        private const int SEARCH_LEN_MAX = 20;	//搜尋最大長度
        private const int SEARCH_LEN_MIN = 4;	//搜尋最短長度

        int same_count = 0;

        //統計每個單詞在文章中出現的次數 用的資料
        string text = @"var query = from info in infoList 
    where info.AuditFlag == null || info.AuditFlag == false 
    join emp in empList 
       on info.SaleMan equals emp.EmployeeCode 
    join house in houseList 
       on info.WareHouse equals house.WareHouseCode 
    join client in clientList 
       on info.ClientCode equals client.ClientCode 
    join dictPayMode in dictList 
       on info.PayMode equals dictPayMode.ValueCode 
    where dictPayMode.TypeCode == 'PayMode\' 
    join dictInvoiceType in dictList 
       on info.InvoiceType equals dictInvoiceType.ValueCode 
    where dictInvoiceType.TypeCode == 'InvoiceType'
    select new 
    { 
       id = info.ID,
       SaleBillCode = info.SaleBillCode,
       SaleMan = emp.Name,
       SaleDate = info.SaleDate,
       Provider = client.ShortName,
       WareHouse = house.ShortName,
       PayMode = dictPayMode.ValueName,
       InvoiceType = dictInvoiceType.ValueName,
       InvoiceCode = info.InvoiceCode,
       AuditFlag = info.AuditFlag 
    };";

        public class WordInfo
        {
            public int keyword_len;
            public string keyword;
            public int keyword_cnt;
            public WordInfo(int l, string s, int c)
            {
                this.keyword_len = l;
                this.keyword = s;
                this.keyword_cnt = c;
            }
        }

        List<WordInfo> word_statistics = new List<WordInfo>();

        private void button30_Click(object sender, EventArgs e)
        {
            /*
            try
            {
                richTextBox1.LoadFile("pipa.txt", RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
            }
            catch (System.IO.FileNotFoundException)
            {
                MessageBox.Show("找不到檔案");
            }
            */

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\novel.txt";
            string y = File.ReadAllText(filename, System.Text.Encoding.Default);
            //richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "總長度：" + y.Length.ToString() + "\n";

            word_statistics.Clear();

            int i, j, k;
            int t;
            int ignore = 0;
            string pattern = string.Empty;
            string word;
            int find_pattern_count = 0;

            for (k = SEARCH_LEN_MIN; k < SEARCH_LEN_MAX; k++)
            {
                find_pattern_count = 0;
                richTextBox1.Text += "\n搜尋長度：" + (k + 1).ToString() + "\n";
                for (i = 0; i < (y.Length - (k + 1)); i++)
                {
                    same_count = 1;
                    ignore = 0;
                    for (t = 0; t <= k; t++)
                    {
                        /*
                        //需要跳過的字眼
                        if ((y[i + t] == '，') || (y[i + t] == '。') || (y[i + t] == '\n') || (y[i + t] == 0x0d) || (y[i + t] == 0x0a) || (y[i + t] == ' ') || (y[i + t] == 0x20) || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
                        {
                            ignore = 1;
                            break;
                        }
                        if ((y[i + t] == '：') || (y[i + t] == '﹒') || (y[i + t] == '「') || (y[i + t] == '」') || (y[i + t] == '？') || (y[i + t] == '…') || (y[i + t] == '、') || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
                        {
                            ignore = 1;
                            break;
                        }
                        */
                        if ((y[i + t] < 13000) || (y[i + t] > 60000))
                        {
                            ignore = 1;
                            break;
                        }
                    }

                    //跳過已經找過的
                    for (int s = 0; s < word_statistics.Count; s++)
                    {
                        word = word_statistics[s].keyword;
                        if (y.Substring(i, (k + 1)) == word)
                        {
                            //richTextBox1.Text += "X " + y.Substring(i, (k + 1));
                            ignore = 1;
                            break;
                        }
                    }

                    if (ignore == 1)
                        continue;

                    int find_pattern = 1;
                    for (j = i + (k + 1); j < (y.Length - k); j++)
                    {
                        find_pattern = 1;
                        for (t = 0; t <= k; t++)
                        {
                            if (y[i + t] == y[j + t])
                            {
                                find_pattern *= 1;
                            }
                            else
                            {
                                find_pattern *= 0;
                            }
                        }

                        if (find_pattern == 1)
                        {
                            same_count++;
                        }

                        /*
                        if (k == 0)
                        {
                            if (y[i] == y[j])
                            {
                                //richTextBox1.Text += "取得 " + y[i] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        else if (k == 1)
                        {
                            if ((y[i] == y[j]) && (y[i + 1] == y[j + 1]))
                            {
                                //richTextBox1.Text += "取得 " + y[i] + y[i + 1] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        else if (k == 2)
                        {
                            if ((y[i] == y[j]) && (y[i + 1] == y[j + 1]) && (y[i + 2] == y[j + 2]))
                            {
                                //richTextBox1.Text += "取得 " + y[i] + y[i + 1] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        else if (k == 3)
                        {
                            if ((y[i] == y[j]) && (y[i + 1] == y[j + 1]) && (y[i + 2] == y[j + 2]) && (y[i + 3] == y[j + 3]))
                            {
                                //richTextBox1.Text += "取得 " + y[i] + y[i + 1] + " i = " + i.ToString() + " j = " + j.ToString() + "\t";
                                same_count++;
                            }
                        }
                        */

                        if (j == (y.Length - (k + 1)))
                        {
                            if (same_count > 2)
                            {
                                find_pattern_count++;
                                richTextBox1.Text += "取得 \"";
                                for (t = 0; t <= k; t++)
                                {
                                    richTextBox1.Text += y[i + t];
                                }
                                richTextBox1.Text += "\" 共 " + same_count.ToString() + " 個\n";

                                pattern = y.Substring(i, (k + 1));

                                word_statistics.Add(new WordInfo(k, pattern, same_count));


                            }
                        }
                    }
                }
                richTextBox1.Text += "find_pattern_count = " + find_pattern_count.ToString() + "\n";
                if (find_pattern_count == 0)
                {
                    richTextBox1.Text += "不用再找了\n";
                    break;
                }
            }
        }

        private void button31_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "word_statistics.Count = " + word_statistics.Count.ToString() + "\n";

            int len;
            string word;
            int count;

            for (int i = 0; i < word_statistics.Count; i++)
            {
                len = word_statistics[i].keyword_len;
                word = word_statistics[i].keyword;
                count = word_statistics[i].keyword_cnt;

                richTextBox1.Text += "len = " + len.ToString() + " word = " + word + " count = " + count.ToString() + "\n";
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {
            int i;
            //if ((y[i + t] == '：') || (y[i + t] == '﹒') || (y[i + t] == '「') || (y[i + t] == '」') || (y[i + t] == '？') || (y[i + t] == '…') || (y[i + t] == '、') || (y[i + t] == '\t') || (y[i + t] == '　') || (y[i + t] == '"'))
            richTextBox1.Text += "：\t" + ((int)'：').ToString() + "\n";

            string ss = "俄羅斯火槍手作亂　";
            for (i = 0; i < ss.Length; i++)
            {
                richTextBox1.Text += ss[i] + "\t" + ((int)ss[i]).ToString() + "\n";
            }

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\novel.txt";
            string y = File.ReadAllText(filename, System.Text.Encoding.Default);
            richTextBox1.Text += "\n總長度：" + y.Length.ToString() + "\n";

            for (i = 0; i < y.Length; i++)
            //for (i = 0; i < 5000; i++)
            {
                if ((i % 5) == 4)
                {
                    richTextBox1.Text += "\n";
                }

                if (y[i] == 0x0A)
                    continue;
                if (y[i] == 0x0D)
                    continue;
                if (y[i] == 0x20)
                    continue;
                if (y[i] == 0x22)
                    continue;

                //if (y[i] < 13000)
                //richTextBox1.Text += "i = " + i.ToString() + "\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";

                if ((y[i] >= 0x2E80) && (y[i] <= 0x33FF))
                {
                    richTextBox1.Text += "_A\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }

                if ((y[i] >= 0x3400) && (y[i] <= 0x4DFF))
                {
                    richTextBox1.Text += "_B\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }
                if ((y[i] >= 0x4E00) && (y[i] <= 0x9FFF))
                {
                    richTextBox1.Text += "_C\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }
                if ((y[i] >= 0xA000) && (y[i] <= 0xA4FF))
                {
                    richTextBox1.Text += "_D\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }
                if ((y[i] >= 0xAC00) && (y[i] <= 0xD7FF))
                {
                    richTextBox1.Text += "_E\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }
                if ((y[i] >= 0xF900) && (y[i] <= 0xFAFF))
                {
                    richTextBox1.Text += "_F\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }
                if ((y[i] >= 0xFB00) && (y[i] <= 0xFFFD))
                {
                    richTextBox1.Text += "_X\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                }

                /*
                A   2E80～33FFh：中日韓符號區。收容康熙字典部首、中日韓輔助部首、注音符號、日本假名、韓文音符，中日韓的符號、標點、帶圈或帶括符文數字、月份，以及日本的假名組合、單位、年號、月份、日期、時間等。
                B   3400～4DFFh：中日韓認同表意文字擴充A區，總計收容6,582個中日韓漢字。
                C   4E00～9FFFh：中日韓認同表意文字區，總計收容20,902個中日韓漢字。
                D   A000～A4FFh：彝族文字區，收容中國南方彝族文字和字根。
                E   AC00～D7FFh：韓文拼音組合字區，收容以韓文音符拼成的文字。
                F   F900～FAFFh：中日韓兼容表意文字區，總計收容302個中日韓漢字。
                X   FB00～FFFDh：文字表現形式區，收容組合拉丁文字、希伯來文、阿拉伯文、中日韓直式標點、小符號、半角符號、全角符號等。
                */
            }
        }

        private void button33_Click(object sender, EventArgs e)
        {
            int i;
            //int j = 0;
            string aaa = string.Empty;
            for (i = 0x4E2D; i < 0x4FFF; i++)
            {
                //richTextBox1.Text += "_A\t|" + y[i] + "|\t" + ((int)y[i]).ToString("X2") + "\t" + ((int)y[i]).ToString() + "\t";
                //richTextBox1.Text += (string)(i) + "\t";
                //aaa[j] = (char)i;
                //j++;
            }
        }

        //統計每個單詞在文章中出現的次數
        private void button34_Click(object sender, EventArgs e)
        {
            //將單詞轉換為數組
            string[] allWords = text.Split(new char[] { '.', '?', '!', ' ', ';', ':', ',' }, StringSplitOptions.RemoveEmptyEntries);
            string[] distinctWords = allWords.Distinct().ToArray<string>(); //去掉單詞數組中重複的單詞
            int[] counts = new int[distinctWords.Length];//創建一個存放詞頻統計信息的數組
            for (int i = 0; i < distinctWords.Length; i++)//遍歷每個單詞
            {
                string tempWord = distinctWords[i];
                //計算每個單詞出現的次數
                var query = from item in allWords
                            where item.ToLower() == tempWord.ToLower()
                            select item;
                counts[i] = query.Count();
            }

            //輸出詞頻統計結果
            for (int i = 0; i < counts.Count(); i++)
            {
                richTextBox1.Text += distinctWords[i] + " 出現 " + counts[i].ToString() + " 次\n";
            }
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //純文字統計
            // Get the file's text.
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            FileInfo file_info = new FileInfo(filename);
            string extension = file_info.Extension.ToLower();
            string txt;
            richTextBox1.Text += "plain text files\n";
            txt = File.ReadAllText(filename);

            richTextBox1.Text += "原資料\n" + txt + "\n";

            // Use regular expressions to replace characters
            // that are not letters or numbers with spaces.
            Regex reg_exp = new Regex("[^a-zA-Z0-9]");
            txt = reg_exp.Replace(txt, " ");

            richTextBox1.Text += "去標點符號後的資料\n" + txt + "\n";

            // Split the text into words.
            string[] words = txt.Split(
                new char[] { ' ' },
                StringSplitOptions.RemoveEmptyEntries);

            // Use LINQ to get the unique words.
            var word_query =
                (from string word in words
                 orderby word
                 select word).Distinct();

            // Display the result.
            string[] result = word_query.ToArray();

            richTextBox1.Text += "\n\n\n" + result.Length.ToString() + "\n";
            int len = result.Length;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += i.ToString() + "\t" + result[i] + "\n";
            }

            richTextBox1.Text += "\n共 " + result.Length.ToString() + " 字\n";

            foreach (string res in result)
            {
                richTextBox1.Text += res + "\n";
            }
        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        private void button37_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
        {

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個


//6060
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出


                string[] strArray = line.Split('\t');
                for (int i = 0; i < strArray.Length; i++)
                {
                    richTextBox1.Text += strArray[i] + "\n";
                }


*/



/*
StreamReader sr 的方法
sr.ReadLine()   // 讀出一行
sr.ReadToEnd()  //讀取所有文字內容


*/


//創建一個讀取器

//琵琶 filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\琵琶行.txt";


/*
            string filename = @"D:\_git\vcs\_1.data\______test_files1\my_2d_array.txt";
            String line;
            StreamReader sr;

            //sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"), true);
            sr = new StreamReader(filename, Encoding.GetEncoding("big5"), true);
            while (!sr.EndOfStream)
            {               // 每次讀取一行，直到檔尾
                line = sr.ReadLine();            // 讀取文字到 line 變數
                if (line.Length > 0)
                {
                    
                }
            }
            sr.Close();



            string filename = "tmp_my_2d_array_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            StreamWriter sw = File.CreateText(filename);

            //sw.Write(richTextBox1.Text);

            for (j = 0; j < ROWS; j++)
            {
                for (i = 0; i < COLUMNS; i++)
                {
                    sw.WriteLine(gray[j, i].ToString());
                }
            }
            sw.Dispose();
            sw.Close();
            richTextBox1.Text += "存檔檔名: " + filename + "\n";



richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            int len = richTextBox1.Lines.Length;
            //richTextBox1.Text += "lines = " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + " : " + richTextBox1.Lines[i] + "\n";
                sw.WriteLine(richTextBox1.Lines[i]); // 寫入一行
            }


*/





/*
_X	|～|	FF5E	65374	
_X	|：|	FF1A	65306	
_C	|中|	4E2D	20013	_C	|日|	65E5	26085	_C	|韓|	97D3	38867	_C	|符|	7B26	31526	_C	|號|	865F	34399	
_C	|區|	5340	21312	_A	|。|	3002	12290	_C	|收|	6536	25910	_C	|容|	5BB9	23481	_C	|康|	5EB7	24247	
_C	|熙|	7199	29081	_C	|字|	5B57	23383	_C	|典|	5178	20856	_C	|部|	90E8	37096	_C	|首|	9996	39318	
_A	|、|	3001	12289	_C	|中|	4E2D	20013	_C	|日|	65E5	26085	_C	|韓|	97D3	38867	_C	|輔|	8F14	36628	
_C	|助|	52A9	21161	_C	|部|	90E8	37096	_C	|首|	9996	39318	_A	|、|	3001	12289	_C	|注|	6CE8	27880	
_C	|音|	97F3	38899	_C	|符|	7B26	31526	_C	|號|	865F	34399	_A	|、|	3001	12289	_C	|日|	65E5	26085	
_C	|本|	672C	26412	_C	|假|	5047	20551	_C	|名|	540D	21517	_A	|、|	3001	12289	_C	|韓|	97D3	38867	
_C	|文|	6587	25991	_C	|音|	97F3	38899	_C	|符|	7B26	31526	_X	|，|	FF0C	65292	_C	|中|	4E2D	20013	
_C	|日|	65E5	26085	_C	|韓|	97D3	38867	_C	|的|	7684	30340	_C	|符|	7B26	31526	_C	|號|	865F	34399	
_A	|、|	3001	12289	_C	|標|	6A19	27161	_C	|點|	9EDE	40670	_A	|、|	3001	12289	_C	|帶|	5E36	24118	
_C	|圈|	5708	22280	_C	|或|	6216	25110	_C	|帶|	5E36	24118	_C	|括|	62EC	25324	_C	|符|	7B26	31526	
_C	|文|	6587	25991	_C	|數|	6578	25976	_C	|字|	5B57	23383	_A	|、|	3001	12289	_C	|月|	6708	26376	
_C	|份|	4EFD	20221	_X	|，|	FF0C	65292	_C	|以|	4EE5	20197	_C	|及|	53CA	21450	_C	|日|	65E5	26085	
_C	|本|	672C	26412	_C	|的|	7684	30340	_C	|假|	5047	20551	_C	|名|	540D	21517	_C	|組|	7D44	32068	
_C	|合|	5408	21512	_A	|、|	3001	12289	_C	|單|	55AE	21934	_C	|位|	4F4D	20301	_A	|、|	3001	12289	
*/