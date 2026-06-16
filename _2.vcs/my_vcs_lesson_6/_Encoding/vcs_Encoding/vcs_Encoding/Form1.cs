using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

            //------------------------------------------------------------  # 60個

            Get_Unicode();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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

            richTextBox1.Size = new Size(500, 690 - 70 * 4);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            tb_unicode.Size = new Size(500, 690 - 70 * 4);
            tb_unicode.Location = new Point(x_st + dx * 3 + 90, y_st + dy * 4);
            lb_unicode.Location = new Point(x_st + dx * 3 + 360, y_st + dy * 4 - 60);

            richTextBox_string1.Size = new Size(250, 270);
            richTextBox_string2.Size = new Size(250, 270);
            richTextBox_hex.Size = new Size(250, 270);
            richTextBox_string1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            richTextBox_hex.Location = new Point(x_st + dx * 2 + 50, y_st + dy * 0);
            richTextBox_string2.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 0);

            bt_string2hex.Location = new Point(x_st + dx * 1 + 250 - 35, y_st + dy * 0 + 270 - 80);
            bt_hex2string.Location = new Point(x_st + dx * 2 + 50 + 250 - 35, y_st + dy * 0 + 270 - 80);
            bt_string2hex.Text = "字串\n轉\n十六進位";
            bt_hex2string.Text = "十六進位\n轉\n字串";

            this.Size = new Size(1260, 750);
            this.Text = "vcs_Encoding";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

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
            由 Big 5 內碼表 得知，我們要的中文字自 A440 開始，換成 10 進位 = 42048，
            所以 for 迴圈起始值設為 42048，結束值為 63964。
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

            //byte[] bytes_big5;      //存放 big5 轉換出來的拜列
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

        private void bt_string2hex_Click(object sender, EventArgs e)
        {
            // 字串轉十六進位
            // Convert the string into bytes.
            UnicodeEncoding ascii_encoder = new UnicodeEncoding();
            byte[] bytes = ascii_encoder.GetBytes(richTextBox_string1.Text);

            // Display the result as a string of hexadecimal values.
            richTextBox_hex.Text = bytes.ToHex(' ');
        }

        private void bt_hex2string_Click(object sender, EventArgs e)
        {
            //十六進位轉字串

            // Convert the string of hexadecimal values into an array of bytes.
            byte[] bytes = richTextBox_hex.Text.ToBytes();

            // Convert the bytes into a string and display the result.
            UnicodeEncoding ascii_encoder = new UnicodeEncoding();
            richTextBox_string2.Text = ascii_encoder.GetString(bytes);
        }

        //------------------------------------------------------------  # 60個

        void Get_Unicode()
        {
            tb_unicode.Clear();

            Cursor = Cursors.WaitCursor;
            Refresh();

            // Set the font size.
            float font_size = 20.0f;
            Font font = new Font("Times New Roman", font_size);
            tb_unicode.Font = font;

            // Display the characters.
            int min = 10000;
            int max = 20000;
            richTextBox1.Text += "轉換範圍 : " + min.ToString() + " ~ " + max.ToString() + "\n";

            StringBuilder sb = new StringBuilder();
            for (int i = min; i <= max; i++)
            {
                sb.Append(((char)i).ToString());
            }
            tb_unicode.Text = sb.ToString();
            tb_unicode.Select(0, 0);

            Cursor = Cursors.Default;
        }

        private void tb_unicode_MouseMove(object sender, MouseEventArgs e)
        {
            char ch = tb_unicode.GetCharFromPosition(e.Location);

            lb_unicode.Text = ch.ToString() + "\t" + ((int)ch).ToString();
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/




/*


33. String 轉為 Byte 序列與 Byte 序列轉為 String。

使用 System.Text.Encoding 類別中的這兩個方法，須注意編碼方式 :

Encoding.GetBytes 方法 : 將字元集編碼成位元組序列。

Encoding.GetString 方法 : 將位元組序列解碼成字串。

程式碼

	String strOrg = "12345";
            // Encoding.GetBytes方法，將 String 轉為 Byte 序列
            byte[] stringConvByte = Encoding.Default.GetBytes(strOrg);
            // Encoding.GetString方法，將 Byte 序列 轉為 String
            string byteConvStrig = Encoding.Default.GetString(stringConvByte);
            

//------------------------------------------------------------  # 60個

字串 和 拜列 的轉換

string和byte[]的轉換 (C#)

string類型轉成byte[]：
byte[] byteArray = System.Text.Encoding.Default.GetBytes ( str );

反過來，byte[]轉成string：
string str = System.Text.Encoding.Default.GetString ( byteArray );

其它編碼方式的，如System.Text.UTF8Encoding，System.Text.UnicodeEncoding class等；例如：

string類型轉成ASCII byte[]：（"01" 轉成 byte[] = new byte[]{ 0x30, 0x31}）

byte[] byteArray = System.Text.Encoding.ASCII.GetBytes ( str );

ASCII byte[] 轉成string：（byte[] = new byte[]{ 0x30, 0x31} 轉成 "01"）

string str = System.Text.Encoding.ASCII.GetString(byteArray);

string text = "是不是漢字，ABC，keleyi.com";
for (int i = 0; i < text.Length; i++)
{
	if (Regex.IsMatch(text[i].ToString(), @"[\u4e00-\u9fbb]+{1}quot;))
	{
		Console.WriteLine("是漢字");
	}
	else
	{
		Console.WriteLine("不是漢字");
	}
}

3400～4DFFh：中日韓認同表意文字擴充A區，總計收容6,582個中日韓漢字。
	4E00～9FFFh：中日韓認同表意文字區，總計收容20,902個中日韓漢字。
A000～A4FFh：彝族文字區，收容中國南方彝族文字和字根。
AC00～D7FFh：韓文拼音組合字區，收容以韓文音符拼成的文字。
F900～FAFFh：中日韓兼容表意文字區，總計收容302個中日韓漢字。
FB00～FFFDh：文字表現形式區，收容組合拉丁文字、希伯來文、阿拉伯文、中日韓直式標點、小符號、半角符號、全角符號等。

Hexadecimal value of 基 is 57FA
Hexadecimal value of 本 is 672C
Hexadecimal value of 運 is 904B
Hexadecimal value of 算 is 7B97
Hexadecimal value of 制 is 5236
Hexadecimal value of 作 is 4F5C
Hexadecimal value of U is 0055
Hexadecimal value of S is 0053
Hexadecimal value of B is 0042
Hexadecimal value of ? is 542F
Hexadecimal value of ? is 52A8
Hexadecimal value of ? is 76D8
Hexadecimal value of ? is 30A6
Hexadecimal value of ? is 30A3
Hexadecimal value of ? is 30AD
Hexadecimal value of ? is 30DA
Hexadecimal value of ? is 30C7
Hexadecimal value of ? is 30A3
Hexadecimal value of ? is 30A2
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of 世 is 4E16
Hexadecimal value of ? is 003F
Hexadecimal value of 生 is 751F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of 概 is 6982
Hexadecimal value of ? is 003F
Hexadecimal value of 表 is 8868
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F
Hexadecimal value of ? is 003F

//------------------------------------------------------------  # 60個


byte[] input = Encoding.Default.GetBytes(str);	//字串轉拜列  111
byte[] input = Encoding.UTF8.GetBytes(key + str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列   222
byte[] input = Encoding.Unicode.GetBytes(str);  //字串轉拜列
byte[] input = Encoding.ASCII.GetBytes(str);
byte[] input = Encoding.Unicode.GetBytes(str);
byte[] input = Encoding.UTF8.GetBytes(key + str); //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str);  //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str);  //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str); //字串轉拜列

byte[] input = ASCIIEncoding.ASCII.GetBytes(str); //字串轉拜列
byte[] input = ASCIIEncoding.ASCII.GetBytes(str);
byte[] input = new UnicodeEncoding().GetBytes(str);   //字串轉拜列
byte[] input = Encoding.Unicode.GetBytes(str); //字串轉拜列
byte[] input = UTF8Encoding.UTF8.GetBytes(str); //字串轉拜列
byte[] input = UTF8Encoding.UTF8.GetBytes(str); //字串轉拜列


UTF8Encoding.Default.GetBytes(str)


        private byte[] GetKeyByteArray(string str)
        {
            int tmpStrLen = str.Length;
            byte[] input = input = new ASCIIEncoding().GetBytes(str);
            return input;
        }

        //byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列

//------------------------------------------------------------  # 60個



*/





