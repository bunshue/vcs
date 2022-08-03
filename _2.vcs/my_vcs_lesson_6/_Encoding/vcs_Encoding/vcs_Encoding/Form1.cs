using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web

namespace vcs_Encoding
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
            dx = 180;
            dy = 80;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            int i;
            int len;

            string initial_string = "ABC密碼錯誤";
            richTextBox1.Text += "原資料 : " + initial_string + "\t";

            len = initial_string.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += initial_string[i].ToString() + "\n";
            }

            byte[] charData;

            richTextBox1.Text += "ASCII編碼 :\t";
            charData = Encoding.ASCII.GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "Default 編碼 = Big5編碼\t";
            charData = Encoding.Default.GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "Big5編碼 :\t";
            charData = Encoding.GetEncoding("big5").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "gb2312編碼 :\t";
            charData = Encoding.GetEncoding("gb2312").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "Unicode編碼 = utf-16 編碼\t";
            charData = Encoding.GetEncoding("unicode").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "utf-16 編碼 :\t";
            charData = Encoding.GetEncoding("utf-16").GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

            richTextBox1.Text += "UTF8 編碼 :\t";
            charData = Encoding.UTF8.GetBytes(initial_string);
            len = charData.Length;
            richTextBox1.Text += "長度 : " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += charData[i].ToString() + "\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //編碼轉換
            string str1 = "https://ja.wikipedia.org/wiki/和 製 英 語";

            richTextBox1.Text += "原字串(a)\t\t" + str1 + "\n";
            richTextBox1.Text += "原字串空白轉nbsp(b)\t" + str1.SpaceToNbsp() + "\n";

            string str2 = str1.UrlEncode();

            richTextBox1.Text += "原字串特殊符號編碼(c)\t" + str2 + "\n";

            richTextBox1.Text += "(c)再解碼\t\t" + str2.UrlDecode() + "\n";

            richTextBox1.Text += "(b)目前無法解碼\n";
            richTextBox1.Text += "\n";


        }

        private void button2_Click(object sender, EventArgs e)
        {
            //列出 中文字 與 BIG5 內碼 的對應表

            /*
            以程式列出 中文字 與 BIG5 內碼 的對應表

            由 Big 5 內碼表 得知，我們要的中文字自 A440 開始，換成 10 進位 = 42048，所以 for 迴圈起始值設為 42048，結束值為 63964。
            */

            richTextBox1.Clear();   // 用來顯示 10 進位 ←→ 16 進位 對應
            richTextBox1.Clear();   // 列出 csv 格式的 BIG5 內碼 ←→ 實際對應的中文字

            for (int x = 42048; x < 63965; x++)
            {
                // 得出 x 的 16 進位內碼
                var sHex = x.ToString("X4");
                // sHex = "A7DA";  // 測試範例文字: 我

                // 再由內碼轉成中文字
                byte[] codeBytes = new byte[2];
                // 由於中文字是由 2 個 byte 組成 , 將 sHex 切成兩組
                // 再由 16 進位轉換成 10 進位
                codeBytes[0] = (byte)Convert.ToInt32(sHex.Substring(0, 2), 16);
                codeBytes[1] = (byte)Convert.ToInt32(sHex.Substring(2, 2), 16);
                var sBig5 = System.Text.Encoding.GetEncoding("BIG5").GetString(codeBytes);
                if ((sBig5.Trim() != "?") && (sBig5.Trim() != "") && (sBig5.Trim() != ""))
                {   // 還是會有一些不要的字，再濾掉 
                    richTextBox1.AppendText(x.ToString() + " = " + sHex + ", " + sBig5 + "\n");
                    richTextBox1.AppendText("\"" + sHex + "\", \"" + sBig5 + "\"\n");
                }
                Application.DoEvents();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //字串編碼處理
            /*
            GB2312是簡體中文系統的標准編碼 用“區” 跟“位”的概念表示 稱之為區位碼
            區指代大的范圍 位相當於偏移量。
            每個漢字占兩個字節
            高位字節”的范圍是0xB0-0xF7，“低位字節”的范圍是0xA1-0xFE。
            它的規律好像是按拼音a到z的順序排列的
            “啊”字是GB2312之中的第一個漢字，它的區位碼就是1601
            為此我們現在用代碼的方式輸出一個漢字

            c#下是little字節序 b0跑後面去了。
            */

            ushort u = 0xa1b0;

            int i;
            for (i = 0; i < 30; i++)
            {
                byte[] chs = BitConverter.GetBytes(u + i);
                Console.Write(Encoding.GetEncoding("GB2312").GetString(chs));
                richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(chs);
            }
            richTextBox1.Text += "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //輸出所有的漢字
            /*
            GB2312是簡體中文系統的標准編碼 用“區” 跟“位”的概念表示 稱之為區位碼
            區指代大的范圍 位相當於偏移量。
            每個漢字占兩個字節
            高位字節”的范圍是0xB0-0xF7，“低位字節”的范圍是0xA1-0xFE。
            它的規律好像是按拼音a到z的順序排列的
            “啊”字是GB2312之中的第一個漢字，它的區位碼就是1601
            為此我們現在用代碼的方式輸出一個漢字

            c#下是little字節序 b0跑後面去了。
            */

            richTextBox1.Text += "輸出所有的漢字\n";
            //gb2312
            //B0-F7，低字節從A1-FE
            //byte hi = 0xB0;
            //byte lo = 0xA1;
            for (byte i = 0xB0; i <= 0xF7; i++)
            {
                for (byte j = 0xA1; j <= 0xFE; j++)
                {
                    //byte t = (byte)(j | (byte)0x01);
                    Console.Write(Encoding.GetEncoding("GB2312").GetString(new byte[] { i, j }));
                    richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(new byte[] { i, j });
                }
            }
            richTextBox1.Text += "\n\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //編碼轉換範例
            string string_old = "方法";   //原字串
            string string_by_big5 = "群曜";   //使用 big5 的字串
            string string_by_gb2312 = "醫電"; //使用 gb2312 的字串
            string string_by_utf8 = "股份"; //使用 UTF8 的字串
            string string_by_ascii = "有限"; //使用 ASCII 的字串
            string string_by_default = "公司"; //使用 預設編碼 的字串

            byte[] bytes_big5;      //存放 big5 轉換出來的拜列
            byte[] bytes_gb2312;    //存放 gb2312 轉換出來的拜列
            byte[] bytes_utf8;      //存放 UTF8 轉換出來的拜列
            byte[] bytes_ascii;     //存放 ASCII 轉換出來的拜列
            byte[] bytes_default;   //存放 預設編碼 轉換出來的拜列
            int len = 0;

            richTextBox1.Text += "用gb2312寫\"方法\"二字, 就是寫B7BD B7A8\n";
            //使用gb2312將字串轉成拜列
            bytes_gb2312 = Encoding.GetEncoding("gb2312").GetBytes(string_old);
            len = bytes_gb2312.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\tdata : \t";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += bytes_gb2312[i].ToString("X2");

            }
            richTextBox1.Text += "\n";

            //B7BD B7A8用big5解開, 得到"源楊"二字.
            //用gb2312將拜列解開成字串
            string_by_gb2312 = Encoding.GetEncoding("gb2312").GetString(bytes_gb2312);
            //用big5將拜列解開成字串
            string_by_big5 = Encoding.GetEncoding("big5").GetString(bytes_gb2312);

            richTextBox1.Text += "拜列用gb2312解開 : \t" + string_by_gb2312 + "\t正確\n";
            //B7BD B7A8用big5解開, 得到"源楊"二字.
            richTextBox1.Text += "拜列用big解開 : \t" + string_by_big5 + "\t錯誤\n";

            //以下就不展開了

            //使用UTF8將字串轉成拜列
            bytes_utf8 = Encoding.UTF8.GetBytes(string_by_utf8);
            //用UTF8將拜列解開成字串
            string string_by_utf8_new = Encoding.UTF8.GetString(bytes_utf8);

            //使用ASCII將字串轉成拜列
            bytes_ascii = Encoding.ASCII.GetBytes(string_by_ascii);
            //用ASCII將拜列解開成字串
            string string_by_ascii_new = Encoding.ASCII.GetString(bytes_ascii);

            //使用預設編碼將字串轉成拜列
            bytes_default = Encoding.Default.GetBytes(string_by_default);
            //用預設編碼將拜列解開成字串
            string string_by_default_new = Encoding.Default.GetString(bytes_default);

            //在 C# 中使用 BitConverter.ToString() 方法將字串轉換為十六進位制
            string decString = "0123456789";
            byte[] bytes = Encoding.Default.GetBytes(decString);
            string hexString = BitConverter.ToString(bytes);
            hexString = hexString.Replace("-", "");
            Console.WriteLine(hexString);
            richTextBox1.Text += hexString + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //特殊的字串解碼

            //特殊的字串解碼

            /*三組字串
            =?big5?B?W01WUF0gp96zTrjqt70gZnJvbSBNVlAgcHJpdmF0ZSBuZXdzZ3JvdXA=?=
            =?gb2312?B?S0BNUyDpX7Bs7ZjQ8g==?=
            =?utf-8?b?N+aciOS7veaVsOaNruW6k+W6lOeUqOeoi+W6j+W8gOWPkeS6uuWRmOaWsOmXu+W/q+iurw==?=
            */
            string str1 = "W01WUF0gp96zTrjqt70gZnJvbSBNVlAgcHJpdmF0ZSBuZXdzZ3JvdXA=";
            string str2 = "S0BNUyDpX7Bs7ZjQ8g==";
            string str3 = "N+aciOS7veaVsOaNruW6k+W6lOeUqOeoi+W6j+W8gOWPkeS6uuWRmOaWsOmXu+W/q+iurw==";

            string strParser1 = Encoding.GetEncoding("big5").GetString(Convert.FromBase64String(str1));
            string strParser2 = Encoding.GetEncoding("gb2312").GetString(Convert.FromBase64String(str2));
            string strParser3 = Encoding.GetEncoding("utf-8").GetString(Convert.FromBase64String(str3));

            richTextBox1.Text += "strParser1 = " + strParser1 + "\n";
            richTextBox1.Text += "strParser2 = " + strParser2 + "\n";
            richTextBox1.Text += "strParser3 = " + strParser3 + "\n";

        }

        //C#兩種方法判斷字符是否為漢字
        //一、用漢字的 UNICODE 編碼范圍判斷
        //漢字的 UNICODE 編碼范圍是4e00-9fbb，
        private void button7_Click(object sender, EventArgs e)
        {
            //判斷是不是漢字
            string text = "判斷是不是漢字，ABC,keleyi.com";
            char[] c = text.ToCharArray();

            for (int i = 0; i < c.Length; i++)
            {
                richTextBox1.Text += c[i] + "\t";
                if (c[i] >= 0x4e00 && c[i] <= 0x9fbb)
                {
                    richTextBox1.Text += "是漢字\n";
                }
                else
                {
                    richTextBox1.Text += "不是漢字\n";
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

    }

    static class StringExtensions
    {
        // Extension to replace spaces with &nbsp;
        public static string SpaceToNbsp(this string s)
        {
            return s.Replace(" ", "&nbsp;");
        }

        // Url encode an ASCII string.
        public static string UrlEncode(this string s)
        {
            return HttpUtility.UrlEncode(s);
        }

        // Url decode an ASCII string.
        public static string UrlDecode(this string s)
        {
            return HttpUtility.UrlDecode(s);
        }
    }

}
