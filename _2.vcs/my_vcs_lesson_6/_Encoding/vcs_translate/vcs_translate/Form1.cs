using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport
using System.IO;                        //for FileAccess, File

namespace vcs_translate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string Big5toGB2312(string strBig5)
        {
            StringBuilder sb = new StringBuilder();
            byte[] tmp = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
            return Encoding.GetEncoding("gb2312").GetString(tmp); // 簡體中文 (GB2312) 
        }

        //使用系統 kernel32.dll LCMapString進行轉換
        internal const int LOCALE_SYSTEM_DEFAULT = 0x0800;
        internal const int LCMAP_SIMPLIFIED_CHINESE = 0x02000000;
        internal const int LCMAP_TRADITIONAL_CHINESE = 0x04000000;
        [DllImport("kernel32", CharSet = CharSet.Auto, SetLastError = true)]
        internal static extern int LCMapString(int Locale, int dwMapFlags, string lpSrcStr, int cchSrc, [Out] string lpDestStr, int cchDest);

        /// <summary>
        /// 將簡體中文字元轉換成繁體中文
        /// </summary>
        /// <param name="strGB2312"></param>
        /// <returns></returns>
        private string GB2312translateBig5(string strGB2312)
        {
            String tTarget = new String(' ', strGB2312.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_TRADITIONAL_CHINESE, strGB2312, strGB2312.Length, tTarget, strGB2312.Length);
            return tTarget;
        }

        /// <summary>
        /// 將繁體中文字元轉換成簡體中文
        /// </summary>
        /// <param name="strBig5"></param>
        /// <returns></returns>
        private string Big5translateGB2312(string strBig5)
        {
            String tTarget = new String(' ', strBig5.Length);
            int tReturn = LCMapString(LOCALE_SYSTEM_DEFAULT, LCMAP_SIMPLIFIED_CHINESE, strBig5, strBig5.Length, tTarget, strBig5.Length);
            return tTarget;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox5.Text = Big5toGB2312(this.richTextBox1.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox6.Text = GB2312translateBig5(this.richTextBox2.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox4.Clear();
            richTextBox5.Clear();
            richTextBox6.Clear();
            richTextBox7.Clear();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox5.Text = Big5translateGB2312(this.richTextBox3.Text);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "統一轉出\n";
            //string和byte[]的轉換
            //string類型轉成byte[]：
            string str = textBox3.Text;
            byte[] byteArray;
            //richTextBox7.Text += "統一字串\t" + str1 + "\t轉成unicode編碼 : " + "\t";
            byteArray = Encoding.GetEncoding("unicode").GetBytes(str);  //指名使用big5編碼, 把字串轉成拜列
            translate_code(byteArray);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "簡中轉出\n";
            string str = textBox2.Text;
            byte[] byteArray;
            //richTextBox7.Text += "簡中字串\t" + str1 + "\t轉成gb2312編碼 : " + "\t";
            byteArray = Encoding.GetEncoding("gb2312").GetBytes(str);  //指名使用gb2312編碼, 把字串轉成拜列
            translate_code(byteArray);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "正中轉出\n";
            //string和byte[]的轉換
            //string類型轉成byte[]：
            string str = textBox1.Text;
            byte[] byteArray;
            //richTextBox7.Text += "正中字串\t" + str1 + "\t轉成Big5編碼 : " + "\t";
            byteArray = Encoding.GetEncoding("big5").GetBytes(str);  //指名使用big5編碼, 把字串轉成拜列
            translate_code(byteArray);
        }

        void translate_code(byte[] byteArray)
        {
            int i;
            int len;
            string str;

            len = byteArray.Length;
            for (i = 0; i < len; i++)
            {
                //richTextBox7.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox7.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox7.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox7.Text += "\n";


            richTextBox7.Text += "byteArray 資料\t";
            for (i = 0; i < len; i++)
            {
                //richTextBox7.Text += "i = " + i.ToString() + "\t" + (char)byteArray[i] + "\t" + byteArray[i].ToString("X2") + "\t" + byteArray[i].ToString() + "\n";
                //richTextBox7.Text += "i = " + i.ToString() + "\t" + byteArray[i].ToString("X2") + "\n";
                richTextBox7.Text += byteArray[i].ToString("X2") + " ";
            }
            richTextBox7.Text += "\n";

            //byte[]轉成string：
            //str = Encoding.Default.GetString(byteArray);
            //richTextBox7.Text += "用預設編碼轉成字串\t" + str + "\n";

            str = Encoding.GetEncoding("big5").GetString(byteArray);
            richTextBox7.Text += "用Big5編碼轉成字串\t" + str + "\n";
            richTextBox6.Text = str;

            str = Encoding.GetEncoding("gb2312").GetString(byteArray);
            richTextBox7.Text += "用gb2312編碼轉成字串\t" + str + "\n";
            richTextBox5.Text = str;

            byteArray[0] = 0x9D;
            byteArray[1] = 0x32;
            str = Encoding.GetEncoding("unicode").GetString(byteArray);
            richTextBox7.Text += "用unicode編碼轉成字串\t" + str + "\n";
            richTextBox4.Text = str;




        }

        /// <summary>
        /// 判斷是否為GB2312編碼
        /// </summary>
        /// <param name="word"></param>
        /// <returns></returns>
        public bool IsGBCode(string word)
        {
            byte[] bytes = Encoding.GetEncoding("GB2312").GetBytes(word);
            // if there is only one byte, it is ASCII code or other code
            if (bytes.Length <= 1)
            {
                return false;
            }
            else
            {
                byte byte1 = bytes[0];
                byte byte2 = bytes[1];
                //判斷是否是GB2312
                if (byte1 >= 176 && byte1 <= 247 && byte2 >= 160 && byte2 <= 254)
                {
                    return true;
                }
                else
                {
                    return false;
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (IsGBCode(richTextBox1.Text) == true)
                richTextBox7.Text += "richTextBox1   是GB2312碼\n";
            else
                richTextBox7.Text += "richTextBox1 不是GB2312碼\n";

            if (IsGBCode(richTextBox2.Text) == true)
                richTextBox7.Text += "richTextBox2   是GB2312碼\n";
            else
                richTextBox7.Text += "richTextBox2 不是GB2312碼\n";

            if (IsGBCode(richTextBox3.Text) == true)
                richTextBox7.Text += "richTextBox3   是GB2312碼\n";
            else
                richTextBox7.Text += "richTextBox3 不是GB2312碼\n";

            if (IsGBCode(textBox1.Text) == true)
                richTextBox7.Text += "字串: " + textBox1.Text + "    是GB2312碼\n";
            else
                richTextBox7.Text += "字串: " + textBox1.Text + "  不是GB2312碼\n";

            if (IsGBCode(textBox2.Text) == true)
                richTextBox7.Text += "字串: " + textBox2.Text + "    是GB2312碼\n";
            else
                richTextBox7.Text += "字串: " + textBox2.Text + "  不是GB2312碼\n";

            if (IsGBCode(textBox3.Text) == true)
                richTextBox7.Text += "字串: " + textBox3.Text + "    是GB2312碼\n";
            else
                richTextBox7.Text += "字串: " + textBox3.Text + "  不是GB2312碼\n";

        }

        private void button9_Click(object sender, EventArgs e)
        {
            string str = "都はるみ全曲集２ Disc 2";
            int i;
            richTextBox7.Text += "len = " + str.Length.ToString() + "\n";
            for (i = 0; i < str.Length; i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\t" + str[i] + "\tvalue\t" + ((int)str[i]).ToString("X4") + "\n";
            }
            richTextBox1.Text += "\n文字編碼都是Unicode編碼 Unicode (Big-Endian) 	1201 	utf-16BE\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            int i;
            for (i = 0x64C2; i < 0x64C2 + 10; i++)
            {
                richTextBox7.Text += "unicode value = 0x" + i.ToString("X4") + ", code = " + ((char)i).ToString() + "\n";
            }

            //用unicode打印出特殊符號
            //特殊字元 平方、立方、micrometer 之顯示
            /*
            其實就是印出unicode碼：                                 
            178=0xB2='²'
            178=0xB3='³'
            178=0xB5='µ'
            */

            richTextBox7.Text += "s" + ((char)178).ToString() + "   s" + ((char)179).ToString() + "  " + ((char)181).ToString() + "m";



            //去 https://unicode-table.com/en/#2327 找出需要的unicode
            //int i;
            for (i = 0x23E9; i < (0x23E9 + 18); i++)
            {
                richTextBox7.Text += "i = 0x" + i.ToString("X4") + "\t" + ((char)i).ToString() + "\n";


            }



        }

        private void button11_Click(object sender, EventArgs e)
        {
            string str_old;
            string str_new;
            byte[] byteArray;
            //TC    您讓球網園謂鎮縣創景維斯提蘭想錫傳統厚載著歐斯與瓊駕駛船壹起務
            //SC    琵琶行间隔回答国家奈何古巴马公塔两年多么的历度界可渐变今将们城和唱暮美空ひばり恋酒
            //unicode

            richTextBox7.Text += "正中轉簡中\n";
            str_old = "您讓球網園謂鎮縣創景維斯提蘭想錫傳統厚載著歐斯與瓊駕駛船壹起務";
            byteArray = Encoding.GetEncoding("big5").GetBytes(str_old);
            str_new = Encoding.GetEncoding("gb2312").GetString(byteArray);
            richTextBox7.Text += "原字串\t" + str_old + "\n";
            richTextBox7.Text += "新字串\t" + str_new + "\n";


            richTextBox7.Text += "簡中轉正中\n";
            str_old = "琵琶行间隔回答国家奈何古巴马公塔两年多么的历度界可渐变今将们城和唱暮美空ひばり恋酒";
            byteArray = Encoding.GetEncoding("gb2312").GetBytes(str_old);
            str_new = Encoding.GetEncoding("big5").GetString(byteArray);
            richTextBox7.Text += "原字串\t" + str_old + "\n";
            richTextBox7.Text += "新字串\t" + str_new + "\n";

            /*
            string str1 = "測試一下";
            byte[] byteArray1 = UnicodeEncoding.Unicode.GetBytes(str1);
            richTextBox7.Text += UnicodeEncoding.Unicode.GetString(byteArray1) + "\n";
            */

        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "日文轉出\n";
            //都はるみの三度笠
            byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x82, 0xCC, 0x8E, 0x4F, 0x93, 0x78, 0x8A, 0x7D };

            //string str = Encoding.ASCII.GetString(data);
            string str = Encoding.GetEncoding("shift_jis").GetString(data);  //指名使用gb2312編碼, 把字串轉成拜列
            richTextBox7.Text += "str = " + str + "\n";


            /*
            string str = textBox2.Text;
            byte[] byteArray;
            //richTextBox7.Text += "簡中字串\t" + str1 + "\t轉成gb2312編碼 : " + "\t";
            byteArray = Encoding.GetEncoding("gb2312").GetBytes(str);  //指名使用gb2312編碼, 把字串轉成拜列
            translate_code(byteArray);
             * 
             * */

        }

        private void button13_Click(object sender, EventArgs e)
        {
            // Print the header.
            //richTextBox1.Text += 
            richTextBox7.Text += "Info.CodePage      ";
            richTextBox7.Text += "Info.Name                    ";
            richTextBox7.Text += "Info.DisplayName";
            richTextBox7.Text += "\n";

            // Display the EncodingInfo names for every encoding, and compare with the equivalent Encoding names.
            foreach (EncodingInfo ei in Encoding.GetEncodings())
            {
                Encoding enc = ei.GetEncoding();

                richTextBox7.Text += ei.CodePage;
                if (ei.CodePage == enc.CodePage)
                    richTextBox7.Text += "    ";
                else
                    richTextBox7.Text += "*** ";

                richTextBox7.Text += ei.Name;
                if (ei.CodePage == enc.CodePage)
                    richTextBox7.Text += "    ";
                else
                    richTextBox7.Text += "*** ";

                richTextBox7.Text += ei.DisplayName;
                if (ei.CodePage == enc.CodePage)
                    richTextBox7.Text += "    ";
                else
                    richTextBox7.Text += "*** ";

                richTextBox7.Text += "\n";
            }

        }

        string transform_encoding(string string_old, string enc_old, string enc_new)
        {
            int i;

            //richTextBox1.Text += "len = " + string_old.Length.ToString() + "\n";
            for (i = 0; i < string_old.Length; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + string_old[i] + "\tvalue\t" + ((int)string_old[i]).ToString("X4") + "\n";
            }
            //richTextBox1.Text += "\n文字編碼都是Unicode編碼 Unicode (Big-Endian) 	1201 	utf-16BE\n";

            // Create two different encodings.
            Encoding encoding_old = Encoding.Unicode;
            //Encoding ascii = Encoding.ASCII;
            Encoding encoding_new = Encoding.GetEncoding(enc_new);

            // Convert the string into a byte array.
            byte[] bytes_old = encoding_old.GetBytes(string_old);

            // Perform the conversion from one encoding to the other.
            byte[] bytes_new = Encoding.Convert(encoding_old, encoding_new, bytes_old); //將old轉成new

            // Convert the new byte[] into a char[] and then into a string.
            char[] chars_new = new char[encoding_new.GetCharCount(bytes_new, 0, bytes_new.Length)];
            encoding_new.GetChars(bytes_new, 0, bytes_new.Length, chars_new, 0);
            string string_new = new string(chars_new);

            //richTextBox1.Text += "len = " + string_new.Length.ToString() + "\n";
            for (i = 0; i < string_new.Length; i++)
            {
                //richTextBox1.Text += "i = " + i.ToString() + "\t" + string_new[i] + "\tvalue\t" + ((int)string_new[i]).ToString("X4") + "\n";
            }

            return string_new;
        }


        private void button14_Click(object sender, EventArgs e)
        {
            //string string_old = "unicode Pi (\u03a0) pi (\u03c0)";
            //string string_old = "16 ????三度笠(1969.04.01-春美?";
            string string_old = "都はるみ全曲集２ Disc 2";
            string encoding_old = "unicode";
            string encoding_new = "big5";
            string string_new = transform_encoding(string_old, encoding_old, encoding_new);
            // Display the strings created before and after the conversion.
            richTextBox7.Text += "old string: " + string_old + "\n";
            richTextBox7.Text += "new string: " + string_new + "\n";

        }

        private void button15_Click(object sender, EventArgs e)
        {
            string string_old = "都はるみ全曲集２ Disc 2";
            string encoding_old = "unicode";
            string encoding_new = "gb2312";
            string string_new = transform_encoding(string_old, encoding_old, encoding_new);
            // Display the strings created before and after the conversion.
            richTextBox7.Text += "old string: " + string_old + "\n";
            richTextBox7.Text += "new string: " + string_new + "\n";

        }

        private void button16_Click(object sender, EventArgs e)
        {
            int i;
            string string_old = "都はるみ全曲集２";
            string string_new;
            string encoding_old = "unicode";
            string encoding_new;

            richTextBox7.Text += "\nvcs之RichTextBox只能顯示Unicode編碼, 原Unicode編碼字串:\t" + string_old + "\n";

            for (i = 0; i < string_old.Length; i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\t" + string_old[i] + "\tvalue\t" + ((int)string_old[i]).ToString("X4") + "\n";
            }

            richTextBox7.Text += "轉成big5\n";
            encoding_new = "big5";
            string_new = transform_encoding(string_old, encoding_old, encoding_new);
            for (i = 0; i < string_new.Length; i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\t" + string_new[i] + "\tvalue\t" + ((int)string_new[i]).ToString("X4") + "\n";
            }

            richTextBox7.Text += "轉成gb2312\n";
            encoding_new = "gb2312";
            string_new = transform_encoding(string_old, encoding_old, encoding_new);
            for (i = 0; i < string_new.Length; i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\t" + string_new[i] + "\tvalue\t" + ((int)string_new[i]).ToString("X4") + "\n";
            }

        }

        void print_data(byte[] data)
        {
            int i;
            int len;
            len = data.Length;
            for (i = 0; i < len; i++)
            {
                richTextBox7.Text += data[i].ToString("X2");
                if (i != (len - 1))
                    richTextBox7.Text += " ";
            }
            richTextBox7.Text += "\n";

        }

        private void button17_Click(object sender, EventArgs e)
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
            richTextBox7.Text += "str = " + str + "\n";

            data = data_1;
            print_data(data);
            str = Encoding.GetEncoding("big5").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += "str = " + str + "\n";

            data = data_2;
            print_data(data);
            str = Encoding.GetEncoding("gb2312").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += "str = " + str + "\n";

            data = data_3;
            print_data(data);
            str = Encoding.GetEncoding("shift_jis").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += "str = " + str + "\n";

            data = data_4;
            print_data(data);
            str = Encoding.GetEncoding("unicode").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += "str = " + str + "\n";

        }

        void translate_encoding0(byte[] data)
        {
            string str;

            richTextBox7.Text += "\t轉成預設編碼 :\t";
            str = Encoding.Default.GetString(data);
            richTextBox7.Text += str + "\n";

            richTextBox7.Text += "\t轉成正中編碼 :\t";
            str = Encoding.GetEncoding("big5").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += str + "\n";

            richTextBox7.Text += "\t轉成簡中編碼 :\t";
            str = Encoding.GetEncoding("gb2312").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += str + "\n";

            richTextBox7.Text += "\t轉成日文編碼 :\t";
            str = Encoding.GetEncoding("shift_jis").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += str + "\n";

            richTextBox7.Text += "\t轉成統一編碼 :\t";
            str = Encoding.GetEncoding("unicode").GetString(data); // 簡體中文 (GB2312) 
            richTextBox7.Text += str + "\n";
        }

        void translate_encoding(string str)
        {
            byte[] data;
            richTextBox7.Text += "原字串 :\t" + str + "\n";

            richTextBox7.Text += "預設編碼 :\t";
            data = Encoding.Default.GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox7.Text += "正中編碼 :\t";
            data = Encoding.GetEncoding("big5").GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox7.Text += "簡中編碼 :\t";
            data = Encoding.GetEncoding("gb2312").GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox7.Text += "日文編碼 :\t";
            data = Encoding.GetEncoding("shift_jis").GetBytes(str);
            print_data(data);
            translate_encoding0(data);

            richTextBox7.Text += "統一編碼 :\t";
            data = Encoding.GetEncoding("unicode").GetBytes(str);
            print_data(data);
            translate_encoding0(data);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            string str_old;

            str_old = "ABCDEFG";
            translate_encoding(str_old);
            richTextBox7.Text += "\n";

            str_old = "都はるみ全曲集２";
            translate_encoding(str_old);
            richTextBox7.Text += "\n";

            str_old = "琵琶行";
            translate_encoding(str_old);
            richTextBox7.Text += "\n";

        }

        private void button19_Click(object sender, EventArgs e)
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
                    richTextBox7.Text += "get UniCode File\n";
                    // UniCode File
                    reader.Position = 2;
                    encoder = Encoding.Unicode;
                }
                else if (header[0] == 0xEF && header[1] == 0xBB && header[2] == 0xBF)
                {
                    richTextBox7.Text += "get UTF-8 File\n";
                    // UTF-8 File
                    reader.Position = 3;
                    encoder = Encoding.UTF8;
                }
                else
                {
                    richTextBox7.Text += "get Default Encoding File\n";
                    // Default Encoding File
                    reader.Position = 0;
                    encoder = Encoding.Default;
                }
                byte[] buffer = new byte[32];
                int source = reader.Read(buffer, 0, 32);
                richTextBox7.Text += "source = " + source.ToString() + "\n";
                string sSource = string.Empty;
                int i;

                if (source > 0)
                {
                    if (encoder != Encoding.Default)
                    {
                        sSource += encoder.GetString(buffer, 0, source);
                        //reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox7.Text += "文件內容: " + sSource + "\n";
                    }
                    else
                    {
                        richTextBox7.Text += "\ntry default\n";
                        encoder = Encoding.Default;
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox7.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox7.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox7.Text += "\n";

                        richTextBox7.Text += "\ntry big5\n";
                        encoder = Encoding.GetEncoding("big5");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox7.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox7.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox7.Text += "\n";

                        richTextBox7.Text += "\ntry gb2312\n";
                        encoder = Encoding.GetEncoding("gb2312");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox7.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox7.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox7.Text += "\n";

                        richTextBox7.Text += "\ntry shift_JIS\n";
                        encoder = Encoding.GetEncoding("shift_jis");
                        sSource = encoder.GetString(buffer, 0, source);
                        reader.Position = 0;
                        source = reader.Read(buffer, 0, 32);
                        richTextBox7.Text += "文件內容: " + sSource + "\n";
                        for (i = 0; i < sSource.Length; i++)
                        {
                            richTextBox7.Text += ((int)sSource[i]).ToString("X2") + " ";
                        }
                        richTextBox7.Text += "\n";



                    }
                }
                reader.Close();

                //richTextBox1.Text += "文件內容: " + sSource + "\n";


            }
            else
            {
                richTextBox7.Text += "未選取檔案\n";

            }
            richTextBox7.Text += "\n文字編碼都是Unicode編碼 Unicode (Big-Endian) 	1201 	utf-16BE\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            char c = 'A';
            richTextBox7.Text += "ccc = " + c + "\n";

            c = '\u0045';

            //c = 0x46;

            richTextBox7.Text += "ccc = " + c + "\n";
            richTextBox7.Text += "ccc = " + c.ToString() + "\n";

            string nnn = "清太祖";
            int len = nnn.Length;
            richTextBox7.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\tdata = " + nnn[i] + "\n";
                richTextBox7.Text += "i = " + i.ToString() + "\tdata = " + ((int)nnn[i]).ToString("X4") + "\n";


            }

            for (i = 0x6E05; i < (0x6E05 + 10); i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\tdata = " + i + "\n";


            }

        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "把系統暫存區的資料印出來\n";


            //C# – 貼上剪貼簿
            //richTextBox1.Text += Clipboard.GetData(DataFormats.Text);
            //richTextBox1.Text += Clipboard.GetText();   //建議用此



            string data = Clipboard.GetText();

            int len = data.Length;
            richTextBox7.Text += "len = " + len.ToString() + "\n";

            richTextBox7.Text += "內容:\n";
            richTextBox7.Text += data;
            richTextBox7.Text += "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox7.Text += "i = " + i.ToString() + "\tdata = " + data[i] + "\n";
                richTextBox7.Text += "i = " + i.ToString() + "\tdata = " + ((int)data[i]).ToString("X4") + "\n";


            }

        }



    }
}
