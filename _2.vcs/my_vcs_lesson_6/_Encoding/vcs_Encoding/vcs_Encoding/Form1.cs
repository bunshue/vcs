using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
Big 5 內碼表
https://web.tnu.edu.tw/me/study/moodle/tutor/vb6/tutor/r05/index.htm
*/

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

            richTextBox1.Size = new Size(500 + 210, 690);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            tb_unicode.Size = new Size(500, 690 - 70 * 1);
            tb_unicode.Location = new Point(x_st + dx * 5 + 90, y_st + dy * 1);
            lb_unicode.Location = new Point(x_st + dx * 5 + 260, y_st + dy * 1 - 60);

            this.Size = new Size(1470 + 210, 750);
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

        void Get_Unicode()
        {
            tb_unicode.Clear();

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
        }

        private void tb_unicode_MouseMove(object sender, MouseEventArgs e)
        {
            char ch = tb_unicode.GetCharFromPosition(e.Location);

            lb_unicode.Text = ch.ToString() + "\t" + ((int)ch).ToString();
        }

        //------------------------------------------------------------  # 60個

        byte ascii2int(char c)
        {
            byte value = 0;
            if ((c >= (Char)48 && c <= (Char)57))
                value = (byte)(c - 48);
            else if ((c >= 'A') && (c <= 'F'))
            {
                value = (byte)(c - 'A' + 10);
            }
            else if ((c >= 'a') && (c <= 'f'))
            {
                value = (byte)(c - 'a' + 10);
            }
            return value;
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

        public void PrintHexBytes(byte[] byteArray)
        {
            if ((byteArray == null) || (byteArray.Length == 0))
            {
                richTextBox1.Text += "空拜列\n";
            }
            else
            {
                richTextBox1.Text += "拜列 : ";
                for (int i = 0; i < byteArray.Length; i++)
                {
                    richTextBox1.Text += byteArray[i].ToString("X2");
                }
                richTextBox1.Text += "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //字串轉拜列 / 拜列轉字串


            //拜列轉字串 ASCII
            /*
            ASCII  半形A~Z 0x41~0x41+25
            BIG5   全形大小寫A-Za-Z (A2CF-A343) 中間有空
            GB2312 全形英數A-Z (A3C1-A3xx)
            */

            richTextBox1.Text += "ASCII 半形 A~Z\n";
            byte[] byteArray = new byte[26];
            for (byte i = 0; i < 26; i++)
            {
                byteArray[i] = (byte)(0x41 + i);
            }
            PrintHexBytes(byteArray);

            string text = Encoding.ASCII.GetString(byteArray);  // 拜列轉字串
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "BIG5 全形 A~Z\n";
            for (byte i = 0; i < 26; i++)
            {
                byte[] byteArray2a = new byte[2];
                byteArray2a[0] = 0xA2;
                byteArray2a[1] = (byte)(0xCF + i);

                // 使用big5將拜列轉字串
                richTextBox1.Text += Encoding.GetEncoding("BIG5").GetString(byteArray2a);  // 使用big5將拜列轉字串
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "GB2312 全形 A~Z\n";
            for (byte i = 0; i < 26; i++)
            {
                byte[] byteArray2b = new byte[2];
                byteArray2b[0] = 0xA3;
                byteArray2b[1] = (byte)(128 + 0x41 + i);

                // 使用gb2312將拜列轉字串
                richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(byteArray2b);  // 使用gb2312將拜列轉字串
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "BIG5中文\n";
            byteArray = new byte[2];
            byteArray[0] = 0xA5;
            byteArray[1] = 0xD5;
            richTextBox1.Text += Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
            byteArray[0] = 0xA4;
            byteArray[1] = 0xE9;
            richTextBox1.Text += Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
            byteArray[0] = 0xA8;
            byteArray[1] = 0xCC;
            richTextBox1.Text += Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
            byteArray[0] = 0xA4;
            byteArray[1] = 0x73;
            richTextBox1.Text += Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
            byteArray[0] = 0xBA;
            byteArray[1] = 0xC9;
            richTextBox1.Text += Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
            richTextBox1.Text += "\n";

            richTextBox1.Text += "gb2312中文\n";
            byteArray = new byte[2];
            byteArray[0] = 0xB0;
            byteArray[1] = 0xD7;
            richTextBox1.Text += Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            byteArray[0] = 0xC8;
            byteArray[1] = 0xD5;
            richTextBox1.Text += Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            byteArray[0] = 0xD2;
            byteArray[1] = 0xC0;
            richTextBox1.Text += Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            byteArray[0] = 0xC9;
            byteArray[1] = 0xBD;
            richTextBox1.Text += Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            byteArray[0] = 0xBE;
            byteArray[1] = 0xA1;
            richTextBox1.Text += Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            richTextBox1.Text += "\n";

            byteArray = new byte[10];
            byteArray[0] = 0xA5;
            byteArray[1] = 0xD5;
            byteArray[2] = 0xA4;
            byteArray[3] = 0xE9;
            byteArray[4] = 0xA8;
            byteArray[5] = 0xCC;
            byteArray[6] = 0xA4;
            byteArray[7] = 0x73;
            byteArray[8] = 0xBA;
            byteArray[9] = 0xC9;
            PrintHexBytes(byteArray);
            text = Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
            richTextBox1.Text += "result : " + text + "\n";

            byteArray = new byte[10];
            byteArray[0] = 0xB0;
            byteArray[1] = 0xD7;
            byteArray[2] = 0xC8;
            byteArray[3] = 0xD5;
            byteArray[4] = 0xD2;
            byteArray[5] = 0xC0;
            byteArray[6] = 0xC9;
            byteArray[7] = 0xBD;
            byteArray[8] = 0xBE;
            byteArray[9] = 0xA1;
            PrintHexBytes(byteArray);
            text = Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            richTextBox1.Text += "result : " + text + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //編碼/解碼

            // 待編碼的字串
            string text = "黃河遠上白雲間，一片孤城萬仞山。";  // 待編碼的字串

            byte[] byteArray;

            richTextBox1.Text += "指名使用日語(Shift-JIS)編碼, 把字串轉成拜列\n";
            byteArray = Encoding.GetEncoding("shift_jis").GetBytes(text);  //指名使用日語(Shift-JIS)編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "指名使用Unicode編碼, 把字串轉成拜列\n";
            byteArray = Encoding.GetEncoding("utf-16").GetBytes(text);  //指名使用Unicode編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "指名使用Unicode(Big-Endian)編碼, 把字串轉成拜列\n";
            byteArray = Encoding.GetEncoding("utf-16BE").GetBytes(text);  //指名使用Unicode(Big-Endian)編碼, 把字串轉成拜列
            print_data(byteArray);

            richTextBox1.Text += "指名使用Unicode (UTF-8)編碼, 把字串轉成拜列\n";
            byteArray = Encoding.GetEncoding("utf-8").GetBytes(text);  //指名使用Unicode (UTF-8)編碼, 把字串轉成拜列
            print_data(byteArray);

            //------------------------------------------------------------  # 60個

            // 待解碼的數列

            int i;
            int len;
            text = "C7BCB5D1BACEED9AD4B997EEC1F8A3ACB4BAEF4CB2BBB6C8D3F1E954EA50A1A3";  // 待解碼的數列
            richTextBox1.Text += "text is " + text + "\n";
            len = text.Length;
            richTextBox1.Text += "len is " + len.ToString() + "\n";
            text = text.Replace(" ", "");
            len = text.Length;
            richTextBox1.Text += "text is " + text + "\n";
            richTextBox1.Text += "len is " + len.ToString() + "\n";

            byteArray = new byte[len / 2];
            for (i = 0; i < (len / 2); i++)
            {
                byteArray[i] = (byte)(ascii2int(text[2 * i]) * 16 + ascii2int(text[2 * i + 1]));
            }

            print_data(byteArray);

            //byte[]轉成string：
            text = Encoding.Default.GetString(byteArray);
            richTextBox1.Text += "用預設編碼轉成字串\t\t\t" + text + "\n";

            richTextBox1.Text += "日語(Shift-JIS)解碼\t\t\t";
            text = Encoding.GetEncoding("shift_jis").GetString(byteArray);	//指名使用日語(Shift-JIS)解碼, 把拜列轉成字串
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "簡體中文(GB2312)解碼\t\t\t";
            text = Encoding.GetEncoding("gb2312").GetString(byteArray);	//指名使用簡體中文(GB2312)解碼, 把拜列轉成字串
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "正體中文(Big5)解碼\t\t\t";
            text = Encoding.GetEncoding("big5").GetString(byteArray);	//指名使用正體中文(Big5)解碼, 把拜列轉成字串
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "Unicode解碼\t\t\t\t";
            text = Encoding.GetEncoding("utf-16").GetString(byteArray);	//指名使用Unicode解碼解碼, 把拜列轉成字串
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "Unicode (Big-Endian)解碼\t\t\t";
            text = Encoding.GetEncoding("utf-16BE").GetString(byteArray);	//指名使用Unicode (Big-Endian)解碼, 把拜列轉成字串
            richTextBox1.Text += text + "\n";

            richTextBox1.Text += "Unicode (UTF-8)解碼\t\t\t";
            text = Encoding.GetEncoding("utf-8").GetString(byteArray);	//指名使用Unicode (UTF-8)解碼, 把拜列轉成字串
            richTextBox1.Text += text + "\n";
        }

        //------------------------------------------------------------  # 60個

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
                byte[] byteArray = new byte[2];
                // 由於中文字是由 2 個 byte 組成 , 將 sHex 切成兩組
                // 再由 16 進位轉換成 10 進位
                byteArray[0] = (byte)Convert.ToInt32(sHex.Substring(0, 2), 16);
                byteArray[1] = (byte)Convert.ToInt32(sHex.Substring(2, 2), 16);

                string text = Encoding.GetEncoding("BIG5").GetString(byteArray);  // 使用big5將拜列轉字串
                if ((text.Trim() != "?") && (text.Trim() != "") && (text.Trim() != ""))
                {
                    // 還是會有一些不要的字，再濾掉
                    richTextBox1.AppendText(x.ToString() + " = " + sHex + ", " + text + "\n");
                    richTextBox1.AppendText("\"" + sHex + "\", \"" + text + "\"\n");
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
            richTextBox1.Text += "從GB2312編碼 0x" + u.ToString("X4") + " 開始的30字 :\n";

            for (int i = 0; i < 30; i++)
            {
                byte[] byteArray = BitConverter.GetBytes(u + i);  // 字串轉拜列
                // 使用gb2312將拜列轉字串
                richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
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
                    Console.Write(Encoding.GetEncoding("GB2312").GetString(new byte[] { i, j }));  // 使用gb2312將拜列轉字串
                    richTextBox1.Text += Encoding.GetEncoding("GB2312").GetString(new byte[] { i, j });  // 使用gb2312將拜列轉字串
                }
            }
            richTextBox1.Text += "\n\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //編碼轉換範例
            string text1 = "春城美酒斜柳明月寒食山花";   //原字串, 正簡相同字串
            string text2 = string.Empty;  //轉換回來的字串
            byte[] byteArray;    //存放拜列

            richTextBox1.Text += "正簡相同字串 : " + text1 + "\n";

            richTextBox1.Text += "使用gb2312將字串轉拜列\n";
            byteArray = Encoding.GetEncoding("gb2312").GetBytes(text1);  // 使用gb2312將字串轉拜列
            PrintHexBytes(byteArray);

            richTextBox1.Text += "使用gb2312將拜列轉字串\n";
            text2 = Encoding.GetEncoding("gb2312").GetString(byteArray);  // 使用gb2312將拜列轉字串
            richTextBox1.Text += "結果 : \t" + text2 + "\t正確\n";

            richTextBox1.Text += "使用big5將拜列轉字串\n";
            text2 = Encoding.GetEncoding("big5").GetString(byteArray);  // 使用big5將拜列轉字串
            richTextBox1.Text += "結果 : \t" + text2 + "\t錯誤\n";

            //------------------------------------------------------------  # 60個

        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //特殊的字串解碼

            string str1 = "W01WUF0gp96zTrjqt70gZnJvbSBNVlAgcHJpdmF0ZSBuZXdzZ3JvdXA=";
            string str2 = "S0BNUyDpX7Bs7ZjQ8g==";
            string str3 = "N+aciOS7veaVsOaNruW6k+W6lOeUqOeoi+W6j+W8gOWPkeS6uuWRmOaWsOmXu+W/q+iurw==";
            string text1 = Encoding.GetEncoding("big5").GetString(Convert.FromBase64String(str1));  // 使用big5將拜列轉字串
            string text2 = Encoding.GetEncoding("gb2312").GetString(Convert.FromBase64String(str2));  // 使用gb2312將拜列轉字串
            string text3 = Encoding.GetEncoding("utf-8").GetString(Convert.FromBase64String(str3));  // 拜列轉字串
            richTextBox1.Text += "text1 : " + text1 + "\n";
            richTextBox1.Text += "text2 : " + text2 + "\n";
            richTextBox1.Text += "text3 : " + text3 + "\n";
        }

        //------------------------------------------------------------  # 60個

        //C#兩種方法判斷字符是否為漢字
        //一、用漢字的 UNICODE 編碼范圍判斷
        //漢字的 UNICODE 編碼范圍是4e00-9fbb，
        private void button7_Click(object sender, EventArgs e)
        {
            string text = "判斷是不是漢字";
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

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            //兩種, 一樣

            //列印出所有的編碼方式
            StringBuilder sb = new StringBuilder();
            foreach (EncodingInfo ei in Encoding.GetEncodings())
            {
                sb.Append(ei.CodePage).Append("\t").Append(ei.Name).Append("\t").Append(ei.DisplayName).Append("\r\n");
            }

            richTextBox1.Text += sb.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //顯示Windows內所有編碼
            richTextBox1.Text += "Info.CodePage      ";
            richTextBox1.Text += "Info.Name                    ";
            richTextBox1.Text += "Info.DisplayName\n";

            //列印出所有的編碼方式
            foreach (EncodingInfo ei in Encoding.GetEncodings())
            {
                Encoding enc = ei.GetEncoding();

                richTextBox1.Text += ei.CodePage;

                if (ei.CodePage == enc.CodePage)
                    richTextBox1.Text += "    ";
                else
                    richTextBox1.Text += "*** ";

                richTextBox1.Text += ei.Name;

                if (ei.CodePage == enc.CodePage)
                    richTextBox1.Text += "    ";
                else
                    richTextBox1.Text += "*** ";

                richTextBox1.Text += ei.DisplayName;

                if (ei.CodePage == enc.CodePage)
                    richTextBox1.Text += "    ";
                else
                    richTextBox1.Text += "*** ";

                richTextBox1.Text += "\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //new

            int number = 75;
            string result = ((char)number).ToString();//将ASCII码转换为字符
            richTextBox1.Text += "轉換結果 : " + result + "\n";

            //------------------------------------------------------------  # 60個

            // 拜列轉字串

            int i;
            byte[] byteArray = new byte[30];
            for (i = 0; i < 26; i++)
            {
                byteArray[i] = (byte)(65 + i);
            }
            PrintHexBytes(byteArray);
            richTextBox1.Text += "len = " + byteArray.Length.ToString() + "\n";

            string text1 = UTF8Encoding.Default.GetString(byteArray);  // 拜列轉字串
            richTextBox1.Text += text1 + "\n";
            richTextBox1.Text += "len = " + text1.Length.ToString() + "\n";

            int length = 16;
            richTextBox1.Text += "拜列轉字串, 只轉某段, 從10開始長度16\n";
            string text2 = UTF8Encoding.Default.GetString(byteArray, 10, length);  // 拜列轉字串, 只轉某段
            richTextBox1.Text += text2 + "\n";
            richTextBox1.Text += "len = " + text2.Length.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            byteArray = new byte[5] { 0x41, 0x42, 0x43, 0x44, 0x45 };
            string text = Encoding.Default.GetString(byteArray);  // 使用預設編碼將拜列轉字串
            richTextBox1.Text += "使用預設編碼將拜列轉字串 : " + text + "\n";

            text = "this is a lion-mouse";
            richTextBox1.Text += "\n原字串:\t" + text + "\n";

            byteArray = Encoding.Default.GetBytes(text);  // 使用預設編碼將字串轉拜列
            richTextBox1.Text += "使用GetBytes將字串轉成拜列\t內容:\t";
            for (i = 0; i < byteArray.Length; i++)
            {
                richTextBox1.Text += (char)byteArray[i];  //多了(char)變成%c
            }
            richTextBox1.Text += "\n";

            //------------------------------------------------------------  # 60個

            //Byte型態的陣列轉換為字串
            Byte[] byteArray2 = new Byte[256];
            byteArray2[0] = (byte)'A';
            byteArray2[1] = (byte)'B';
            byteArray2[2] = (byte)'C';

            length = 3;
            text = Encoding.ASCII.GetString(byteArray2, 0, length);  // 拜列轉字串, 只轉某段
            richTextBox1.Text += "使用GetString將拜列轉成字串\t" + text + "\n";

            //------------------------------------------------------------  # 60個

            //字串轉換為Byte型態的陣列
            text = "this is a lion-mouse";
            byteArray = Encoding.ASCII.GetBytes(text);  // 使用ASCII編碼將字串轉拜列
            richTextBox1.Text += "使用GetBytes將字串轉成拜列\t內容:\t";
            foreach (char c in byteArray)
            {
                richTextBox1.Text += c.ToString() + " ";
            }
            richTextBox1.Text += "\n";

            //------------------------------------------------------------  # 60個

            text = "ABCDE\n";
            richTextBox1.Text += "原字串 : " + text + "\n";

            byteArray = Encoding.Default.GetBytes(text);  // 使用預設編碼將字串轉拜列
            PrintHexBytes(byteArray);

            byteArray[1] += 5;
            byteArray[3] += 7;

            text = Encoding.Default.GetString(byteArray);  // 使用預設編碼將拜列轉字串
            richTextBox1.Text += "轉回來字串 : " + text + "\n";

            //char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };

            /*
            richTextBox1.Text += "byte[] 轉 char[]\n";

            byte[] byteArray = new byte[5] { 0x01, 0x02, 0x03, 0x04, 0x05 };
            char[] cChar = Encoding.ASCII.GetChars(byteArray);

            richTextBox1.Text += "char[] 轉 二進位碼的文字型態\n";
            char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            byte[] byteArray = Encoding.Default.GetBytes(cChar);  // 使用預設編碼將字串轉拜列
            */

            //------------------------------------------------------------  # 60個

            //獲取區位碼

            text = "汉字区位码";

            try
            {
                //得到汉字区位码信息
                string result3 = getCode(text);
                richTextBox1.Text += "獲取區位碼 : " + result3 + "\n";
            }
            catch (IndexOutOfRangeException ex)
            {
                //使用消息对话框提示异常信息
                MessageBox.Show(ex.Message + "请输入正确的汉字", "出错！");
            }
        }

        /// <summary>
        /// 得到汉字区位码方法
        /// </summary>
        /// <param name="strChinese">汉字字符</param>
        /// <returns>返回汉字区位码</returns>
        public string getCode(string text)
        {
            byte[] byteArray = Encoding.Default.GetBytes(text);  // 使用預設編碼將字串轉拜列
            int front = (short)(byteArray[0] - '\0');//将字节数组的第一位转换成short类型
            int back = (short)(byteArray[1] - '\0');//将字节数组的第二位转换成short类型
            return (front - 160).ToString() + (back - 160).ToString();//计算并返回区位码
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            //絞怀隙陬奀ㄛ壽敕耀宒勤趕敦极

            string old_text = "絞怀隙陬奀ㄛ壽敕耀宒勤趕敦极";

            richTextBox1.Text += "測試編碼轉換\n";

            richTextBox1.Text += "看到一個亂碼字串 : " + old_text + "\n";

            //原本是 簡中編碼 => 正中解碼 導致的錯誤 故需要反向操作

            richTextBox1.Text += "1. 亂碼字串先用BIG5編碼取得正確編碼\n";
            byte[] byteArray = Encoding.GetEncoding("BIG5").GetBytes(old_text);  //指名使用簡體中文(GB2312)編碼, 把字串轉成拜列  // 使用gb2312將字串轉拜列
            richTextBox1.Text += "2. 正確編碼再用正確編碼(GB2312)解碼\n";
            string new_text = Encoding.GetEncoding("GB2312").GetString(byteArray);  // 使用gb2312將拜列轉字串

            richTextBox1.Text += "得到一個正確字串 : " + new_text + "\n";

            richTextBox1.Text += new_text + "\n";

            //------------------------------  # 30個

            richTextBox1.Text += "驗算\n";

            old_text = new_text;

            richTextBox1.Text += "原本正確的字串 : " + old_text + "\tGB2312編碼";

            richTextBox1.Text += "使用正確的編碼編碼\n";
            byteArray = Encoding.GetEncoding("GB2312").GetBytes(old_text);  //指名使用簡體中文(GB2312)編碼, 把字串轉成拜列  // 使用gb2312將字串轉拜列

            // 正確的編碼資料，經過傳輸後，卻使用錯誤的編碼來解碼
            new_text = Encoding.Default.GetString(byteArray);  // 使用gb2312將拜列轉字串

            richTextBox1.Text += "使用錯誤的編碼解碼 : " + new_text + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {

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

/*
字串 和 拜列 的轉換

其它編碼方式的，如UTF8Encoding，UnicodeEncoding class等；例如：

string類型轉成ASCII byte[]：（"01" 轉成 byte[] = new byte[]{ 0x30, 0x31}）

byte[] byteArray = Encoding.ASCII.GetBytes(text);  // 使用ASCII編碼將字串轉拜列

ASCII byte[] 轉成string：（byte[] = new byte[]{ 0x30, 0x31} 轉成 "01"）

string text = "是不是漢字";
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

char c = 'A';
int i = 'A';

richTextBox1.Text += "字元變數c是" + c + "\n";
richTextBox1.Text += "字元A的內碼是" + i + "\n";

i = 'B';
richTextBox1.Text += "字元B的內碼是" + i + "\n";

c = '\u0041'; //16進位,2個Bytes
richTextBox1.Text += "UniCode 0041的字元是" + c + "\n";

//------------------------------------------------------------  # 60個

Encoding.GetEncoding big5 gb2312 shift_jis UTF-8 unicode
大小寫不分

//設定檔案的編碼
Encoding enc = Encoding.GetEncoding("BIG5");
Encoding enc = Encoding.GetEncoding("GB2312");

使用 Encoding 類別中的這兩個方法，須注意編碼方式 :
字串轉拜列 與 拜列轉字串

Encoding.GetBytes方法 : 將字元集編碼成位元組序列。  // 字串轉拜列
Encoding.GetBytes方法 : 將 String 轉為 Byte 序列  // 字串轉拜列
Encoding.GetString方法 : 將位元組序列解碼成字串。
Encoding.GetString方法 : 將 Byte 序列 轉為 String, 拜列轉字串

// 字串轉拜列
string text = "中秋佳節";
byte[] byteArray = Encoding.Default.GetBytes(text);  // 使用預設編碼將字串轉拜列
byte[] byteArray = Encoding.ASCII.GetBytes(text);  // 使用ASCII編碼將字串轉拜列
byte[] byteArray = Encoding.UTF8.GetBytes(text);  // 使用UTF8將字串轉拜列
byte[] byteArray = Encoding.Unicode.GetBytes(text);
byte[] byteArray = Encoding.GetEncoding("Big5").GetBytes(text);  //指名使用正體中文(Big5)編碼, 把字串轉成拜列  // 使用big5將字串轉拜列
byte[] byteArray = Encoding.GetEncoding("GB2312").GetBytes(text);  //指名使用簡體中文(GB2312)編碼, 把字串轉成拜列  // 使用gb2312將字串轉拜列
byte[] byteArray = Encoding.GetEncoding("unicode").GetBytes(text);  // Unicode編碼 = utf-16 編碼 字串轉拜列
byte[] byteArray = Encoding.GetEncoding("utf-16").GetBytes(text);  // utf-16 編碼 字串轉拜列
byte[] byteArray = Encoding.GetEncoding(1252).GetBytes(text);
byte[] byteArray = ASCIIEncoding.ASCII.GetBytes(text);
byte[] byteArray = UTF8Encoding.UTF8.GetBytes(text);  // 使用UTF8將字串轉拜列
byte[] byteArray = new UnicodeEncoding().GetBytes(text);
byte[] byteArray = new ASCIIEncoding().GetBytes(text);

// 拜列轉字串
text = Encoding.Default.GetString(byteArray);  // 使用預設編碼將拜列轉字串
text = Encoding.ASCII.GetString(byteArray);  // 拜列轉字串
text = Encoding.UTF8.GetString(byteArray);  // 使用UTF8將拜列轉字串
text = Encoding.Unicode.GetString(byteArray);  // 使用Unicode編碼 將拜列轉字串

//------------------------------------------------------------  # 60個

        private string[] DirName()
        {
            int j = 0;
            string[] str = new string[26];
            for (int i = 65; i <91;i++ )
            {
                str [j]= Convert.ToChar(i).ToString()+":";
                j++;
            }
            return str;
        }

//------------------------------------------------------------  # 60個

//字串轉拜列
string mystring = "this is a string"
char[] mychars  = mystring.ToCharArray();

//foreach循環處理char數組
foreach(char mychar in mystring)
{
    Console.WriteLine(mychar);
}
mystring.Length //獲取元素的個數 

//------------------------------------------------------------  # 60個

//使用 GetBytes() 將字串轉換為位元組陣列
//使用 GetBytes() 方法將字串轉換為位元組陣列

string myString = "This is a string.";
byte[] byteArray = Encoding.ASCII.GetBytes(myString);
richTextBox1.Text += "The Byte Array is:\n";
foreach (byte bytes in byteArray)
{
    richTextBox1.Text += bytes.ToString() + "\n";
}

*/

//絞怀隙陬奀ㄛ壽敕耀宒勤趕敦极
//当输入回车时，关闭模式对话窗体

