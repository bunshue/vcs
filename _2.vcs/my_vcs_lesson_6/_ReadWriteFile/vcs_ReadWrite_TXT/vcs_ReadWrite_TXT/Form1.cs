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

            button40.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button48.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            richTextBox1.Size = new Size(400, 300);
            richTextBox2.Size = new Size(400, 300);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            richTextBox2.Location = new Point(x_st + dx * 5, y_st + dy * 5);

            bt_clear1.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear1.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear1.Size.Height);
            bt_clear2.Location = new Point(richTextBox2.Location.X + richTextBox2.Size.Width - bt_clear2.Size.Width, richTextBox2.Location.Y + richTextBox2.Size.Height - bt_clear2.Size.Height);

            this.Size = new Size(1500, 700);
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
            //File.ReadAllLines

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            StringBuilder sb = new StringBuilder();

            string[] Txt_All_Lines = File.ReadAllLines(filename, Encoding.Default);

            foreach (string Single_Line in Txt_All_Lines)
            {
                sb.AppendLine(Single_Line);
            }

            richTextBox1.Text += sb.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //將純文字檔拆成一行一行的字串陣列, 可以去除前後空白
            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\poem.txt";
            string[] patterns;
            patterns = File.ReadAllLines(filename).Select(i => i.Trim()).Where(i => i != string.Empty).ToArray();
            int len = patterns.Length;
            //richTextBox1.Text += "len = " + len.ToString() + "\n";
            int ii;
            for (ii = 0; ii < len; ii++)
            {
                richTextBox1.Text += patterns[ii] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //開檔ReadAllLines存檔
            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
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

            string filename2 = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            // Save the result.
            File.WriteAllLines(filename2, output_lines.ToArray());
            richTextBox1.Text += "\n製作TXT檔\t" + filename2 + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            //XXX richTextBox1.SaveFile(filename, RichTextBoxStreamType.PlainText);    //將richTextBox的資料寫入到指定的文字檔, 這樣會出現怪字型, 還是一行一行儲存比較好

            FileStream fs = new FileStream(filename, FileMode.Create, FileAccess.Write);
            StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式            
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "存檔完成, 檔名 : " + filename + "\n";
            */
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
            richTextBox1.LoadFile(filename, RichTextBoxStreamType.PlainText);  //將指定的文字檔載入到richTextBox
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
            //法一
            // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
            //richTextBox1.Text = System.IO.File.ReadAllText(filename, Encoding.Default);

            //法二
            //讀取檔案
            string y = File.ReadAllText(filename, Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + y + "\n";
            richTextBox1.Text += "長度：" + y.Length.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀檔4
            string fileReadName = @"D:\_git\vcs\_1.data\______test_files1\data.txt";
            ReadFile(fileReadName);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //AppendAllText 插入文字
            //C# 將字串插入文件內容尾端
            richTextBox1.Text += "寫一筆資料到檔案尾端\n";
            File.AppendAllText("myfilename.txt", " append text to the end.");

            //讀取檔案
            // 運用 ReadAllText 方法 (String, Encoding) ，其中 Encoding 針對您txt檔案的編碼做變更，讀出的資料才不會有亂碼
            string str = File.ReadAllText("myfilename.txt", System.Text.Encoding.Default);
            richTextBox1.Text += "檔案內容 : " + str + "\n";

        }

        //讀檔案
        private string ReadFile(string filename)
        {
            string content = "";
            content = File.ReadAllText(filename);
            richTextBox1.Text += "檔案: " + filename + " 內容：\n";
            richTextBox1.Text += content;
            richTextBox1.Text += "\n";
            return content;
        }

        private const int ENCODING_1 = 1;	//encoding type 1, big5
        private const int ENCODING_2 = 2;	//encoding type 2, gb2312
        private const int ENCODING_3 = 3;	//encoding type 3, shift_jis
        private const int ENCODING_4 = 4;	//encoding type 4, unicode

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            read_text_file(filename, ENCODING_1);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\sc\襟裳岬.txt";
            read_text_file(filename, ENCODING_2);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\jap\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            read_text_file(filename, ENCODING_3);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Form1.cs.txt";
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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";

            //創建一個讀取器
            //StreamReader sr = new StreamReader(filename);
            StreamReader sr = new StreamReader(filename, Encoding.Default);    //Windows預設，就是big5

            //一次性讀取完
            string all_text = sr.ReadToEnd();   //一次性讀完所有文字內容
            richTextBox1.Text += all_text + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀檔1
            //一次讀取檔案內所有資料
            filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            FileInfo f = new FileInfo(filename);
            sr = f.OpenText();
            richTextBox1.Text += sr.ReadToEnd();	//讀取所有文字內容
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取中文檔案
            filename = @"D:\_git\vcs\_1.data\______test_files1\read_file.txt";

            if (File.Exists(filename) == false) //確認檔案是否存在
            {
                MessageBox.Show("檔案: " + filename + "不存在，無法開啟。\n");
                return;
            }
            else
            {
                richTextBox1.Clear();
                //讀取中文檔案
                StreamReader sw = new StreamReader(@"D:\_git\vcs\_1.data\______test_files1/read_file.txt", Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
                richTextBox1.Text += sw.ReadToEnd();	//讀取所有文字內容
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            filename = @"D:\_git\vcs\_1.data\______test_files1\read_file.txt";

            //StreamReader sr = new StreamReader(filename);
            //StreamReader sr = new StreamReader(filename, Encoding.Default);
            sr = new StreamReader(filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            richTextBox1.Text += sr.ReadToEnd();	//讀取所有文字內容
            sr.Close();
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";

            richTextBox2.Text += filename + "\n";
            richTextBox2.Text += filename + "\n";
            richTextBox2.Text += filename + "\n";

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
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
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
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            write_text_file(filename, ENCODING_2);
        }

        private void button13_Click(object sender, EventArgs e)
        {
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            write_text_file(filename, ENCODING_1);
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

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
            int i;
            string line = string.Empty;

            //ReadLine 1
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";

            richTextBox1.Text += "\n檔案 : " + filename + "\t內容\n";
            using (TextReader reader = new StreamReader(filename, Encoding.Default))
            {
                i = 0;
                line = reader.ReadLine();
                while (line != null)
                {
                    i++;
                    richTextBox1.Text += "i = " + i.ToString() + "\t" + line + "\n";
                    line = reader.ReadLine();
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //ReadLine 2
                StreamReader sr = new StreamReader(filename, Encoding.Default);
                while ((line = sr.ReadLine()) != null)
                {
                    richTextBox1.Text += line + "\n";
                }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //ReadLine 3

            //一行一行讀取文字檔
            filename = @"D:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\eula.3081a.txt";

            sr = new StreamReader(filename, Encoding.Default);
            string strLine = string.Empty;
            while ((strLine = sr.ReadLine()) != null)
            {
                richTextBox1.Text += strLine + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //ReadLine 4

            filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\琵琶行.txt";
            try
            {
                sr = new StreamReader(filename, Encoding.Default);
                line = string.Empty;
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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\txt_rw.txt";

            //StreamWriter sw = new StreamWriter(filename); // true 是資料可附加至檔案, open write
            StreamWriter sw = new StreamWriter(filename, true); // true 是資料可附加至檔案 open write append

            int len = richTextBox1.Lines.Length;
            //richTextBox2.Text += "lines = " + len.ToString() + "\n";
            for (int i = 0; i < len; i++)
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
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\compare\ssss.txt";

            StreamReader sr1 = new StreamReader(filename1);     //創建StreamReader對象
            StreamReader sr2 = new StreamReader(filename2);     //創建StreamReader對象
            StreamReader sr3 = new StreamReader(filename3);     //創建StreamReader對象

            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))    //讀取文件內容并判斷
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 不相同\n";

            if (object.Equals(sr1.ReadToEnd(), sr3.ReadToEnd()))    //讀取文件內容并判斷
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 不相同\n";

            if (object.Equals(sr2.ReadToEnd(), sr3.ReadToEnd()))    //讀取文件內容并判斷
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 不相同\n";
        }

        private void button22_Click(object sender, EventArgs e)
        {
            int i;
            int N = 10;
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

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
            //比較兩個檔案
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            string filename3 = @"D:\_git\vcs\_1.data\______test_files1\compare\ssss.txt";
            StreamReader sr1 = new StreamReader(filename1, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            StreamReader sr2 = new StreamReader(filename2, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            StreamReader sr3 = new StreamReader(filename3, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//讀取所有文字內容
            {
                richTextBox1.Text += "兩個文件相等\n";
            }
            else
            {
                richTextBox1.Text += "兩個文件不相等\n";
            }
            if (object.Equals(sr1.ReadToEnd(), sr3.ReadToEnd()))	//讀取所有文字內容
            {
                richTextBox1.Text += "兩個文件相等\n";
            }
            else
            {
                richTextBox1.Text += "兩個文件不相等\n";
            }
            sr1.Close();
            sr2.Close();
            sr3.Close();
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //RW test

            string filename = "this is filename";
            string timer = "ttttt 1";
            string timer2 = "ttttt 2";
            string username = "david";
            string pwd = "123456";

            StreamWriter sw = new StreamWriter("info.txt");
            sw.WriteLine(filename);
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

            string filenameb = string.Empty;
            string timerb = string.Empty;
            string timer2b = string.Empty;
            string usernameb = string.Empty;
            string pwdb = string.Empty;

            StreamReader sr = new StreamReader("info.txt");

            filenameb = sr.ReadLine();
            timerb = sr.ReadLine();
            timer2b = sr.ReadLine();
            usernameb = sr.ReadLine();
            pwdb = sr.ReadLine();

            sr.Close();
            sr.Dispose();
            GC.Collect();

            richTextBox1.Text += "filenameb = " + filenameb + "\n";
            richTextBox1.Text += "timerb = " + timerb + "\n";
            richTextBox1.Text += "timer2b = " + timer2b + "\n";
            richTextBox1.Text += "usernameb = " + usernameb + "\n";
            richTextBox1.Text += "pwdb = " + pwdb + "\n";
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

            string path = @"D:\_git\vcs\_1.data\______test_files1\";
            string filename = "filewrite.txt";

            if (!Directory.Exists(path))
            {
                richTextBox1.Text += "路徑不存在，建立之。\n";
                Directory.CreateDirectory(path);
            }
            if (!File.Exists(path + filename))
            {
                richTextBox1.Text += "檔案不存在，建立之。\n";
                FileStream fs = File.Create(path + filename);
                fs.Close();
            }
            using (StreamWriter sw = File.AppendText(path + filename))
            {
                //File.SetAttributes(path + filename, FileAttributes.Hidden);//隱藏
                sw.WriteLine(richTextBox1.Text, Encoding.Default);
                richTextBox1.Text += "寫入檔案完成\n";
            }
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //儲存檔案 多種
            //建立時間檔案
            string filename = "Stage_Speed_Current." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
            richTextBox1.Text += "建立時間檔案：" + filename + "\n";

            //儲存檔案1
            string filename1 = @"D:\_git\vcs\_1.data\______test_files2\vcs_test.txt";
            FileInfo f = new FileInfo(filename1);
            StreamWriter sw1 = f.CreateText();
            sw1.Write(richTextBox1.Text);
            sw1.Flush();
            sw1.Close();
            richTextBox1.Text += @"儲存檔案1 OK，檔名：D:\_git\vcs\_1.data\______test_files2\vcs_test.txt\n";

            //儲存檔案2
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\SaveDataToFile.txt";
            StreamWriter sw2 = File.CreateText(filename2);
            string content = "";
            for (int i = 0; i < 10; i++)
            {
                content += i + "\t";
                content += "aaa" + "\t";
                content += "bbb" + "\t";
                content += "ccc" + "\t";
                content += "\n";
            }
            sw2.WriteLine(content);
            sw2.Close();
            richTextBox1.Text += "儲存檔案2 OK，檔名：" + filename2 + "\n";

            //儲存檔案3     把textbox資料存檔
            string filename3 = "data." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
            StreamWriter sw = File.CreateText(filename3);
            sw.Write(richTextBox1.Text);
            sw.Close();
            richTextBox1.Text += "儲存檔案3 OK，檔名：" + filename3 + "\n";

            //儲存檔案4     儲存二進位檔
            string filename4 = @"D:\_git\vcs\_1.data\______test_files1\save_file_test.bin";
            byte[] cbuffer = new byte[256];
            for (int i = 0; i < 256; i++)
                cbuffer[i] = (byte)i;

            // 建立檔案串流
            FileStream fs = new FileStream(filename4, FileMode.OpenOrCreate, FileAccess.Write);
            //byte[] byteSave = Encoding.ASCII.GetBytes(txtHTML.Text.ToString());

            // 以FileStream類別的Write方法將HTML內容寫入檔案中
            fs.Write(cbuffer, 0, cbuffer.Length);

            // 關閉檔案串流
            fs.Close();
            richTextBox1.Text += "儲存檔案4 OK，檔名：" + filename4 + "\n";

            //儲存檔案5
            int[] x = { 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600 };
            int[] y = { 200, 328, 396, 373, 268, 131, 26, 3, 71, 200, 328, 396, 373, 268, 131, 26 };
            //把資料儲存成檔案
            string filename5 = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaa.txt";
            string context = string.Empty;
            //FileStream
            fs = File.Open(filename5, FileMode.Create);
            sw = new StreamWriter(fs);
            for (int ii = 0; ii < 16; ii++)
            {
                context = ii.ToString() + "\t" + x[ii].ToString() + "\t" + y[ii].ToString();
                sw.WriteLine(context);
            }
            sw.Dispose();
            fs.Close();
            richTextBox1.Text += "儲存檔案5 OK，檔名：" + filename5 + "\n";
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //附加檔案
            string filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            FileInfo f = new FileInfo(filename);
            StreamWriter sw = f.AppendText();
            sw.Write(richTextBox1.Text);
            sw.Flush();
            sw.Close();
        }

        private void button30_Click(object sender, EventArgs e)
        {
            richTextBox2.Text += "各種 File 操作\n";

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";
            string filename2 = "tmp_article.txt";
            string filename3 = "tmp_article_new.txt";

            if (File.Exists(filename2) == false)
            {
                richTextBox2.Text += "檔案 : " + filename2 + ", 不存在, 建立之\n";
                File.Copy(filename1, filename2);
            }

            richTextBox2.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox2.Text += "將檔案 : " + filename2 + ", 改檔名成 : " + filename3 + "\n";
            File.Move(filename2, filename3);

            richTextBox2.Text += "------------------------------------------------------------\n";  // 60個

            if (File.Exists(filename3) == true)
            {
                richTextBox2.Text += "檔案 : " + filename3 + ", 已存在, 刪除之\n";
                richTextBox2.Text += "直接刪除, 不放進垃圾桶\n";
                File.Delete(filename3);
            }

            richTextBox2.Text += "------------------------------------------------------------\n";  // 60個

            string filename = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";

            richTextBox1.Text += File.GetAttributes(filename) + "\n";
            File.SetAttributes(filename, FileAttributes.ReadOnly);
            richTextBox1.Text += File.GetAttributes(filename) + "\n";
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //File.ReadAllBytes

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes.bmp";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\test_WriteAllBytes.bmp";

            //讀取資料
            byte[] data_read = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + data_read.Length.ToString() + "\n";

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            //修改資料
            for (int i = 54; i < data_read.Length; i++)
            {
                if (data_read[i] == 0xCC)
                    data_read[i] = 0xFF;
            }

            //寫資料
            File.WriteAllBytes(filename2, data_read);
            richTextBox1.Text += "寫成檔案" + filename2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes.bmp";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes_half.bmp";

            //讀取資料
            byte[] data_read = File.ReadAllBytes(filename1);
            richTextBox1.Text += "讀取檔案" + filename1 + "\t";
            richTextBox1.Text += "len = " + data_read.Length.ToString() + "\n";

            byte[] data_write = new byte[data_read.Length / 2];

            for (int i = 0; i < data_read.Length / 2; i++)
            {
                data_write[i] = data_read[i];

            }
            */

            /*
            打印資料
            string data_read_result = string.Empty;
            foreach (byte b in data_read)
            {
                data_read_result += b.ToString("X2");
            }
            richTextBox1.Text += data_read_result;
            */

            /*
            //寫資料
            //File.WriteAllBytes(filename2, data_write);
            string zzz = Convert.ToString(data_write);
            File.WriteAllText(filename2, zzz);
            richTextBox1.Text += "寫成檔案" + filename2 + "\n";
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string filename;
            byte[] b;
            string s;

            richTextBox1.Text += "用預設編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            b = File.ReadAllBytes(filename);
            s = Encoding.Default.GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用Big5編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Compressor.c";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("big5").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用gb2312編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\sc\001川の流れのように.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("gb2312").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用shift_jis編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\jap\饩Ⓚ丗钡冦冦葢轿瘅.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.GetEncoding("shift_jis").GetString(b);
            richTextBox1.Text += s + "\n";

            richTextBox1.Text += "用utf-8編碼開啟\n";
            filename = @"D:\_git\vcs\_1.data\______test_files1\__text\Form1.cs.txt";
            b = File.ReadAllBytes(filename);
            s = Encoding.UTF8.GetString(b);
            richTextBox1.Text += s + "\n";
        }

        private void button32_Click(object sender, EventArgs e)
        {
            int i;
            byte[] data = new byte[16];     //for TC, SC, JP
            byte[] data2 = new byte[18];    //for unicode

            string filename1 = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".big5.txt";
            string filename2 = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".gb2312.txt";
            string filename3 = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".shift_jis.txt";
            string filename4 = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";

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

        private void button33_Click(object sender, EventArgs e)
        {
            string filename = "tmp_txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".default.txt";
            richTextBox1.Clear();
            for (int i = 0; i < 256; i++)
            {
                richTextBox1.Text += i.ToString() + " ";
            }
            File.WriteAllText(filename, richTextBox1.Text, Encoding.Default);
            richTextBox1.Text += "\n存檔完成, 檔名 : " + filename + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //ReadAllText 讀取文件
            //使用ReadAllText可以直接讀取文件中的內容，格式為:
            //File.ReadAllText(檔案位置及名稱)

            //WriteAllText 寫入/建立檔案
            //透過WriteAllText可以將文字寫入檔案(如果檔案不存在，會自動建立)，格式為:
            //File.WriteAllText(檔案位置及名稱, 字串);

            //建立檔案
            string x = "Hello text";
            File.WriteAllText("myfilename.txt", x);
            richTextBox1.Text += "寫檔完成\n";

            //讀取檔案
            string y = File.ReadAllText("myfilename.txt");
            richTextBox1.Text += "檔案內容 : " + y + "\n";
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //sr.Read

            //讀檔3
            //一次讀取檔案內一個字元
            string filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            FileInfo f = new FileInfo(filename);
            StreamReader sr = f.OpenText();
            while (sr.Peek() > 0)
            {
                richTextBox1.Text += (char)sr.Read();
            }
            sr.Close();
        }

        private void button35_Click(object sender, EventArgs e)
        {

        }

        private void button36_Click(object sender, EventArgs e)
        {
            //string filename = "wmi-" + DateTime.Now.ToString("yyyy-MMdd-HHmm") + ".txt";
            string filename = @"D:/_git/vcs/_1.data/______test_files2/vcs-" + DateTime.Now.ToString("yyyy-MMdd-HHmm") + ".txt";
            if (File.Exists(filename) == false)
            {
                MessageBox.Show("檔案 " + filename + " 不存在，製作一個。");
                StreamWriter sw = File.CreateText(filename);
                sw.Write(richTextBox1.Text);
                sw.Close();
            }
            else
            {
                MessageBox.Show("檔案 " + filename + " 存在, 開啟，並接續寫入資料");
                StreamWriter sw = File.AppendText(filename);
                sw.Write(richTextBox1.Text);
                sw.Close();
            }
        }

        private void button37_Click(object sender, EventArgs e)
        {
            //製作暫存檔案2
            string folderpath;          // 紀錄資料夾路徑
            string filename;            // 檔案名稱
            string fullpath;
            FileStream fs;

            folderpath = Directory.GetCurrentDirectory();
            richTextBox1.Text += "目前路徑: " + folderpath + "\n";

            // 使用現在時間建立檔案名稱
            filename = DateTime.Now.Year.ToString();
            filename += DateTime.Now.Month.ToString("00");
            filename += DateTime.Now.Day.ToString("00");
            filename += DateTime.Now.Hour.ToString("00");
            filename += DateTime.Now.Minute.ToString("00");
            filename += DateTime.Now.Second.ToString("00");
            filename += ".txt";
            richTextBox1.Text += "檔案名稱: " + filename + "\n";

            fullpath = folderpath + "\\" + filename;
            richTextBox1.Text += "完整路徑與檔名: " + fullpath + "\n";

            //開啟檔案
            fs = File.Open(fullpath, FileMode.Create);

            fs.Close();
        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
        {
            //讀檔案的一部分 bmp
            richTextBox1.Text += "讀檔案的一部分\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\test_ReadAllBytes.bmp";
            int len = 100;
            richTextBox1.Text += "讀bmp檔, 從頭讀\t長度: " + len.ToString() + " 拜\n";

            byte[] bmpdata = new byte[len];
            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            fs.Seek(0, SeekOrigin.Begin);
            fs.Read(bmpdata, 0, len);
            fs.Close();

            //打印資料
            string data_read_result;
            int cnt = 0;

            data_read_result = string.Empty;
            foreach (byte b in bmpdata)
            {
                data_read_result += b.ToString("X2");
                cnt++;
                if ((cnt % 16) == 0)
                {
                    data_read_result += "\n";
                }
                else
                {
                    data_read_result += " ";
                }
            }
            richTextBox1.Text += data_read_result + "\n";

            data_read_result = string.Empty;
            cnt = 0;
            foreach (byte b in bmpdata)
            {
                if (char.IsLetterOrDigit((char)b) == true)
                {
                    data_read_result += (char)b;
                }
                else
                {
                    data_read_result += ".";
                }

                cnt++;
                if ((cnt % 16) == 0)
                {
                    data_read_result += "\n";
                }
                else
                {
                    data_read_result += " ";
                }
            }
            richTextBox1.Text += data_read_result + "\n";
        }

        private void button40_Click(object sender, EventArgs e)
        {
            //ReadLine
            //讀檔2
            //一次讀取檔案內一行資料
            string filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            FileInfo f = new FileInfo(filename);
            StreamReader sr = f.OpenText();
            while (sr.Peek() > 0)
            {
                richTextBox1.Text += sr.ReadLine() + "\n";
            }
            sr.Close();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int i = 0;
            String line;

            filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";

            //StreamReader sr = new StreamReader(filename);
            //StreamReader sr = new StreamReader(filename, Encoding.Default);
            sr = new StreamReader(filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

            //richTextBox1.Text += sr.ReadToEnd();	//讀取所有文字內容
            //寫法一
            while (!sr.EndOfStream)
            {               // 每次讀取一行，直到檔尾
                i++;
                line = sr.ReadLine();            // 讀取文字到 line 變數
                richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\n";
            }

            /*
            //寫法二
            while ((line = sr.ReadLine()) != null)
            {
                i++;
                richTextBox1.Text += "第" + i.ToString() + "行： " + line + "\n";
            }
            */
            sr.Close();
        }

        private void button41_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\vcs_test.txt";
            string context = string.Empty;

            FileStream fs = File.Open(filename, FileMode.Open);
            StreamReader sr = new StreamReader(fs);
            try
            {
                // Read File text
                for (int ii = 0; ii < 5; ii++)
                {
                    context = sr.ReadLine();
                    richTextBox1.Text += "Line " + ii.ToString() + ", context : " + context + "\n";

                    string[] strArray = context.Split('\t');
                    for (int i = 0; i < strArray.Length; i++)
                    {
                        richTextBox1.Text += strArray[i] + "\n";
                    }
                }

                //this.Disp_Message("開啟檔案 : " + filename, 0);
                //this.Disp_Message("讀取檔案成功 !!", 1);
                MessageBox.Show("Open File : " + filename);
                MessageBox.Show("Read File Successfully !!");
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
                //this.Disp_Message("開啟檔案 : " + filename, 0);
                //this.Disp_Message("讀取檔案失敗 !!", 2);
                MessageBox.Show("Open File : " + filename);
                MessageBox.Show("Read File Fail !!");
            }
            sr.Dispose();
            fs.Close();
        }

        private void button42_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaab.txt";

            string[] rowdat = new string[3];
            string[] paraname = new string[16];
            string context = string.Empty;
            int t1 = 0;
            int t2 = 0;
            string rowdata = string.Empty;

            FileStream fs = File.Open(filename, FileMode.Open);
            StreamReader sr = new StreamReader(fs);
            // Read File text
            for (int ii = 0; ii < 1; ii++)
            {
                context = sr.ReadLine();
                MessageBox.Show("context " + ii + " = " + context + "  len = " + context.Length);
                //MessageBox.Show("context[41] = " + Convert.ToString(context[41], 16));
                //MessageBox.Show("context[42] = " + Convert.ToString(context[42], 16));

                //MessageBox.Show("data = 0x" + Convert.ToString(value, 16) + " =" + value);

                t1 = 0;
                t2 = context.IndexOf("\t", t1);
                rowdata = context.Substring(t1, t2 - t1);
                MessageBox.Show("t1 = " + t1 + " t2 = " + t2 + " rowdata = " + rowdata);

                do
                {
                    t1 = t2 + 1;
                    t2 = context.IndexOf("\t", t1);
                    if (t2 != -1)
                    {
                        rowdata = context.Substring(t1, t2 - t1);
                        MessageBox.Show("t1 = " + t1 + " t2 = " + t2 + " rowdata = " + rowdata);
                    }
                    else
                    {
                        t2 = context.Length;
                        rowdata = context.Substring(t1, t2 - t1);
                        MessageBox.Show("t1 = " + t1 + " t2 = " + t2 + " rowdata = " + rowdata);
                        break;
                    }
                }
                while (t2 != -1);
            }
            sr.Dispose();
            fs.Close();
        }

        private void button43_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            string filename = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaa.txt";

            string[] rowdat = new string[3];
            string[] paraname = new string[16];
            int[] value = new int[16];
            string context = string.Empty;
            int t1 = 0;
            int t2 = 0;

            int[] xx = new int[16];
            int[] yy = new int[16];

            FileStream fs = File.Open(filename, FileMode.Open);
            StreamReader sr = new StreamReader(fs);
            // Read File text
            for (int ii = 0; ii < 16; ii++)
            {
                context = sr.ReadLine();
                richTextBox1.Text += "原始context " + ii + " = " + context + "\n";
                t1 = t2 = 0;
                //for (int jj = 0; jj < 3; jj++)
                for (int jj = 0; jj < 2; jj++)
                {
                    t2 = context.IndexOf("\t", t1);
                    rowdat[jj] = context.Substring(t1, t2 - t1);
                    richTextBox1.Text += "分割context = " + context + " jj = " + jj + " t1= " + t1 + " t2= " + t2 + " rowdat =" + rowdat[jj] + "\n";

                    t1 = t2 + 1;
                    if (jj == 0)
                        xx[ii] = Int32.Parse(rowdat[jj]);
                    else if (jj == 1)
                        yy[ii] = Int32.Parse(rowdat[jj]);
                }
                paraname[ii] = rowdat[1];
                //value[ii] = Int32.Parse(rowdat[2]);
            }
            MessageBox.Show("Result: \n" + xx[0].ToString() + " " + xx[1].ToString() + " " + xx[2].ToString() + " " + xx[3].ToString() + " " + xx[4].ToString() + " " + xx[5].ToString() + " " + xx[6].ToString() + " " + xx[7].ToString() + " " + xx[8].ToString() + " " + xx[9].ToString() + " " + xx[10].ToString() + " " + xx[11].ToString() + " " + xx[12].ToString() + " " + xx[13].ToString() + " " + xx[14].ToString() + " " + xx[15].ToString() + "\n" + yy[0].ToString() + " " + yy[1].ToString() + " " + yy[2].ToString() + " " + yy[3].ToString() + " " + yy[4].ToString() + " " + yy[5].ToString() + " " + yy[6].ToString() + " " + yy[7].ToString() + " " + yy[8].ToString() + " " + yy[9].ToString() + " " + yy[10].ToString() + " " + yy[11].ToString() + " " + yy[12].ToString() + " " + yy[13].ToString() + " " + yy[14].ToString() + " " + yy[15].ToString());
            sr.Dispose();
            fs.Close();
        }

        private void button44_Click(object sender, EventArgs e)
        {
            //取得檔案資訊

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\article.txt";

            FileInfo f = new FileInfo(filename);
            richTextBox1.Text += "Name: " + f.Name + "\n";
            richTextBox1.Text += "FullName: " + f.FullName + "\n";
            richTextBox1.Text += "Extension: " + f.Extension + "\n";
            richTextBox1.Text += "size: " + f.Length.ToString() + "\n";
            richTextBox1.Text += "Directory: " + f.Directory + "\n";
            richTextBox1.Text += "DirectoryName: " + f.DirectoryName + "\n";
        }

        const int MAX_CAPACITY = 50;
        string[] name = new string[MAX_CAPACITY];
        int[,] scores = new int[2, MAX_CAPACITY];
        int counter = 0;

        // 更新界面上顯示的訊息
        void ShowData()
        {
            richTextBox1.Text += "共有" + counter + "人\n";

            string res = "名字\t國文\t數學\r\n";
            for (int i = 0; i < counter; i++)
            {
                res += name[i] + "\t" + scores[0, i] + "\t" + scores[1, i] + "\r\n";
            }
            richTextBox1.Text = res;
        }

        private void button45_Click(object sender, EventArgs e)
        {
            if (counter < MAX_CAPACITY)
            {
                name[counter] = "david";
                scores[0, counter] = 100;
                scores[1, counter] = 90;

                counter++;

                ShowData(); // 更新界面上顯示的訊息
            }
            else
            {
                richTextBox2.Text += "容量已滿\n";
            }
        }

        private void button46_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\score.txt";
            richTextBox2.Text += "開啟檔案 : " + filename + "\n";

            FileInfo finfo = new FileInfo(filename);
            StreamReader sr = finfo.OpenText();

            int i = 0;
            while (sr.Peek() >= 0)
            {
                name[i] = sr.ReadLine();
                scores[0, i] = Convert.ToInt32(sr.ReadLine());
                scores[1, i] = Convert.ToInt32(sr.ReadLine());
                i++;
            }

            sr.Close();

            counter = i;
            ShowData();
        }

        private void button47_Click(object sender, EventArgs e)
        {
            string filename = "tmp_score_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";

            FileInfo finfo = new FileInfo(filename);
            StreamWriter sw = finfo.CreateText();

            // 透過StreamWriter物件sw來寫入資料
            for (int i = 0; i < counter; i++)
            {
                sw.WriteLine(name[i]);
                sw.WriteLine(scores[0, i]);
                sw.WriteLine(scores[1, i]);
            }

            sw.Flush();
            sw.Close();

            richTextBox2.Text += "已存檔 : " + filename + "\n";
        }

        private void button48_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_bin\score.dat";

            richTextBox2.Text += "開啟檔案 : " + filename + "\n";

            FileStream fs = new FileStream(filename, FileMode.Open);
            BinaryReader br = new BinaryReader(fs);

            int i = 0;

            while (br.PeekChar() >= 0)
            {
                name[i] = br.ReadString();
                scores[0, i] = br.ReadInt32();
                scores[1, i] = br.ReadInt32();
                i++;
            }

            br.Close();
            fs.Close();

            counter = i;
            ShowData();
        }

        private void button49_Click(object sender, EventArgs e)
        {
            string filename = "tmp_score_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".dat";

            FileStream fs = new FileStream(filename, FileMode.Create);
            BinaryWriter bw = new BinaryWriter(fs);

            for (int i = 0; i < counter; i++)
            {
                bw.Write(name[i]);
                bw.Write(scores[0, i]);
                bw.Write(scores[1, i]);
            }

            bw.Flush();
            bw.Close();
            fs.Close();

            richTextBox2.Text += "已存檔 : " + filename + "\n";
        }

        /*  清除資料
            for (int i = 0; i < counter; i++)
            {
                name[i] = "";
                scores[0, i] = 0;
                scores[1, i] = 0;
            }
            counter = 0;

            richTextBox1.Text += "共有" + counter + "人\n";
        */
    }
}


//6060
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個

//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個


/*  可搬出


*/



//string filename = Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".unicode.txt";


