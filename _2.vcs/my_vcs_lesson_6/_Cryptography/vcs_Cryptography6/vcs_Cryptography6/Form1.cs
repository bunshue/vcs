using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using CryptoStuffNamespace;

/*
    明碼 clear code
    密碼 password
    明碼經使用密碼編碼後 Ciphertext
    編碼經使用密碼解密後 Deciphered
*/

namespace vcs_Cryptography6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Encrypt the text.
        private void btnEncrypt_Click(object sender, EventArgs e)
        {
            byte[] bytes = tb_clear_code.Text.Encrypt(tb_password.Text);
            tb_encrypted.Text = bytes.ToHex();
        }

        // Decrypt the text.
        private void btnDecrypt_Click(object sender, EventArgs e)
        {
            byte[] ciphertext = tb_encrypted.Text.ToBytes();
            tb_decrypted.Text = ciphertext.Decrypt(tb_password.Text);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string clear_code = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; //明碼
            string password = "SecretPassword";         //密碼
            string encrypted = "0D BC 23 DF 7B 43 58 28 1C BC 83 B8 97 45 DB 7A 9D A4 A7 E5 4C 68 C3 09 65 83 29 08 EA 32 A3 69";         //明碼經使用密碼編碼後的編碼
            byte[] bytes;
            byte[] ciphertext;
            string result1;
            string result2;

            richTextBox1.Text += "明碼 : \t" + clear_code + "\n";
            richTextBox1.Text += "密碼 : \t" + password + "\n";
            richTextBox1.Text += "編碼 : \t" + encrypted + "\n";

            // Encrypt the text. 加密
            bytes = clear_code.Encrypt(password);
            result1 = bytes.ToHex();
            richTextBox1.Text += "明碼經使用密碼加密後 : \t" + result1 + "\n";

            // Decrypt the text. 解密
            ciphertext = encrypted.ToBytes();
            result2 = ciphertext.Decrypt(password);
            richTextBox1.Text += "編碼經使用密碼解密後 : \t" + result2 + "\n";


            clear_code = tb_clear_code.Text;
            password = tb_password.Text;
            richTextBox1.Text += "明碼 : \t" + clear_code + "\n";
            richTextBox1.Text += "密碼 : \t" + password + "\n";
            // Encrypt the text. 加密
            bytes = clear_code.Encrypt(password);
            result1 = bytes.ToHex();
            richTextBox1.Text += "明碼經使用密碼加密後 : \t" + result1 + "\n";
            tb_encrypted.Text = result1;
            encrypted = result1;

            richTextBox1.Text += "編碼 : \t" + encrypted + "\n";
            // Decrypt the text. 解密
            ciphertext = encrypted.ToBytes();
            result2 = ciphertext.Decrypt(password);
            richTextBox1.Text += "編碼經使用密碼解密後 : \t" + result2 + "\n";
            tb_decrypted.Text = result2;
        }
    }
}
