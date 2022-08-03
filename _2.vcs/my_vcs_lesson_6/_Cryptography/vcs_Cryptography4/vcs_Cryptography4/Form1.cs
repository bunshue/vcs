using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Cryptography4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

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

        private void button1_Click(object sender, EventArgs e)
        {
            //ROT13編碼
            richTextBox_rot13b.Text = ROT13Encode(richTextBox_rot13a.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //ROT13解碼, 其實就是再編碼一次
            richTextBox_rot13c.Text = ROT13Encode(richTextBox_rot13b.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //加密
            textBox2.Text = Encrypt(textBox1.Text);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //解密
            textBox2.Text = Decryptor(textBox2.Text);
        }

        private string Encrypt(string s)
        {
            Encoding ascii = Encoding.ASCII;
            string EncryptString;
            EncryptString = "";
            for (int i = 0; i < s.Length; i++)
            {
                int j;
                byte[] b = new byte[1];
                j = Convert.ToInt32(ascii.GetBytes(s[i].ToString())[0]);
                j = j + 5;
                b[0] = Convert.ToByte(j);
                EncryptString = EncryptString + ascii.GetString(b);
            }
            return EncryptString;
        }

        private string Decryptor(string s)
        {
            Encoding ascii = Encoding.ASCII;
            string DecryptorString;
            DecryptorString = "";
            for (int i = 0; i < s.Length; i++)
            {
                int j;
                byte[] b = new byte[1];
                j = Convert.ToInt32(ascii.GetBytes(s[i].ToString())[0]);
                j = j - 5;
                b[0] = Convert.ToByte(j);
                DecryptorString = DecryptorString + ascii.GetString(b);
            }
            return DecryptorString;
        }
    }
}
