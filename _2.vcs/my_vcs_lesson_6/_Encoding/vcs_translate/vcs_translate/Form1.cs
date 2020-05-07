using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

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
            byteArray = System.Text.Encoding.GetEncoding("unicode").GetBytes(str);  //指名使用big5編碼, 把字串轉成拜列
            translate_code(byteArray);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "簡中轉出\n";
            string str = textBox2.Text;
            byte[] byteArray;
            //richTextBox7.Text += "簡中字串\t" + str1 + "\t轉成gb2312編碼 : " + "\t";
            byteArray = System.Text.Encoding.GetEncoding("gb2312").GetBytes(str);  //指名使用gb2312編碼, 把字串轉成拜列
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
            byteArray = System.Text.Encoding.GetEncoding("big5").GetBytes(str);  //指名使用big5編碼, 把字串轉成拜列
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
            //str = System.Text.Encoding.Default.GetString(byteArray);
            //richTextBox7.Text += "用預設編碼轉成字串\t" + str + "\n";

            str = System.Text.Encoding.GetEncoding("big5").GetString(byteArray);
            richTextBox7.Text += "用Big5編碼轉成字串\t" + str + "\n";
            richTextBox6.Text = str;

            str = System.Text.Encoding.GetEncoding("gb2312").GetString(byteArray);
            richTextBox7.Text += "用gb2312編碼轉成字串\t" + str + "\n";
            richTextBox5.Text = str;

            byteArray[0] = 0x9D;
            byteArray[1] = 0x32;
            str = System.Text.Encoding.GetEncoding("unicode").GetString(byteArray);
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
            string str;
            byte[] byteArray;
            //TC    您讓球網園謂鎮縣創景維斯提蘭想錫傳統厚載著歐斯與瓊駕駛船壹起務
            //SC    琵琶行间隔回答国家奈何古巴马公塔两年多么的历度界可渐变今将们城和唱暮美空ひばり恋酒
            //unicode

            richTextBox7.Text += "正中轉簡中\n";
            str = "您讓球網園謂鎮縣創景維斯提蘭想錫傳統厚載著歐斯與瓊駕駛船壹起務";
            byteArray = System.Text.Encoding.GetEncoding("Big5").GetBytes(str);
            richTextBox7.Text += str + "\n";
            richTextBox7.Text += System.Text.Encoding.GetEncoding("gb2312").GetString(byteArray) + "\n";


            richTextBox7.Text += "簡中轉正中\n";
            str = "琵琶行间隔回答国家奈何古巴马公塔两年多么的历度界可渐变今将们城和唱暮美空ひばり恋酒";
            byteArray = System.Text.Encoding.GetEncoding("gb2312").GetBytes(str);
            richTextBox7.Text += str + "\n";
            richTextBox7.Text += System.Text.Encoding.GetEncoding("big5").GetString(byteArray) + "\n";

            /*
            string str1 = "測試一下";
            byte[] byteArray1 = System.Text.UnicodeEncoding.Unicode.GetBytes(str1);
            richTextBox7.Text += System.Text.UnicodeEncoding.Unicode.GetString(byteArray1) + "\n";
            */

        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox7.Text += "日文轉出\n";
            //都はるみの三度笠
            byte[] data = { 0x93, 0x73, 0x82, 0xCD, 0x82, 0xE9, 0x82, 0xDD, 0x82, 0xCC, 0x8E, 0x4F, 0x93, 0x78, 0x8A, 0x7D };

            int i;

            //string str = System.Text.Encoding.ASCII.GetString(data);
            string str = System.Text.Encoding.GetEncoding("shift_jis").GetString(data);  //指名使用gb2312編碼, 把字串轉成拜列
            richTextBox7.Text += "str = " + str + "\n";


            /*
            string str = textBox2.Text;
            byte[] byteArray;
            //richTextBox7.Text += "簡中字串\t" + str1 + "\t轉成gb2312編碼 : " + "\t";
            byteArray = System.Text.Encoding.GetEncoding("gb2312").GetBytes(str);  //指名使用gb2312編碼, 把字串轉成拜列
            translate_code(byteArray);
             * 
             * */

        }



    }
}
