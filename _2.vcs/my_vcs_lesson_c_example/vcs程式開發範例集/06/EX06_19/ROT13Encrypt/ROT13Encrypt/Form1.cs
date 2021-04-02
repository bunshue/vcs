using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ROT13Encrypt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox2.Text= ROT13Encode(textBox1.Text);
        }

        public string ROT13Encode(string InputText)
        {
            char tem_Character;
            int UnicodeChar;
            string EncodedText = "";
            for (int i = 0; i < InputText.Length; i++)//搜尋字串中的所有字符
            {
                tem_Character = System.Convert.ToChar(InputText.Substring(i, 1));//取得字串中指定的字符
                UnicodeChar = (int)tem_Character;//取得目前字符的Unicode編碼
                if (UnicodeChar >= 97 && UnicodeChar <= 109)//對字符進行加密
                {
                    UnicodeChar = UnicodeChar + 13;
                }
                else if (UnicodeChar >= 110 && UnicodeChar <= 122)//對字符進行解密
                {
                    UnicodeChar = UnicodeChar - 13;
                }
                else if (UnicodeChar >= 65 && UnicodeChar <= 77)//對字符進行加密
                {
                    UnicodeChar = UnicodeChar + 13;
                }
                else if (UnicodeChar >= 78 && UnicodeChar <= 90)//對字符進行解密
                {
                    UnicodeChar = UnicodeChar - 13;
                }
                EncodedText = EncodedText + (char)UnicodeChar;//傳回設定後的字符
            }
            return EncodedText;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox2.Text = ROT13Encode(textBox2.Text);
        }  
    }
}
