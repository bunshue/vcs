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

        }

        private void button4_Click(object sender, EventArgs e)
        {

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
