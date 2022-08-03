using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography;

namespace vcs_Cryptography2_SHA1
{
    public partial class Form1 : Form
    {
        //欲進行加密的字符串  
        string str_clear_text = "this is a lion-mouse";

        //加密後的結果
        string str_encrypted_text = string.Empty;

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
            x_st = 12;
            y_st = 12;
            dx = 200;
            dy = 65;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private string GetStringValue(byte[] Byte)
        {
            string tmpString = "";
            /*
            ASCIIEncoding Asc = new ASCIIEncoding();
            tmpString = Asc.GetString(Byte);
            */
            int iCounter;
            for (iCounter = 0; iCounter < Byte.Length; iCounter++)
            {
                tmpString = tmpString + Byte[iCounter].ToString();
            }
            return tmpString;
        }

        private byte[] GetKeyByteArray(string strKey)
        {
            ASCIIEncoding Asc = new ASCIIEncoding();
            int tmpStrLen = strKey.Length;
            byte[] tmpByte = new byte[tmpStrLen - 1];
            tmpByte = Asc.GetBytes(strKey);
            return tmpByte;
        }

        public string SHA1Encrypt(string strIN)
        {
            byte[] tmpByte;
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            tmpByte = sha1.ComputeHash(GetKeyByteArray(strIN));
            sha1.Clear();
            return GetStringValue(tmpByte);
        }

        public string SHA256Encrypt(string strIN)
        {
            byte[] tmpByte;
            SHA256 sha256 = new SHA256Managed();
            tmpByte = sha256.ComputeHash(GetKeyByteArray(strIN));
            sha256.Clear();
            return GetStringValue(tmpByte);
        }

        public string SHA512Encrypt(string strIN)
        {
            byte[] tmpByte;
            SHA512 sha512 = new SHA512Managed();
            tmpByte = sha512.ComputeHash(GetKeyByteArray(strIN));
            sha512.Clear();
            return GetStringValue(tmpByte);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //SHA1，SHA256，SHA512

            //此類提供SHA1，SHA256，SHA512等3種算法，加密字串的長度依次增大。

            str_encrypted_text = SHA1Encrypt(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA1\t長度：" + str_encrypted_text.Length + "\n";

            str_encrypted_text = SHA256Encrypt(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA256\t長度：" + str_encrypted_text.Length + "\n";

            str_encrypted_text = SHA512Encrypt(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA512\t長度：" + str_encrypted_text.Length + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //SHA1
            str_encrypted_text = str_clear_text.Sha1();
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA1\t長度：" + str_encrypted_text.Length + "\n";

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            str_encrypted_text = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str_clear_text, "SHA1");
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA1\tSHA1加密長度是：" + str_encrypted_text.Length + "\n";
        }

        /// <summary>
        /// 使用DES加密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="originalValue">待加密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">初始化向量(最大長度8)</param>
        /// <returns>加密後的字符串</returns>
        public string DESEncrypt(string originalValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateEncryptor();
            byt = Encoding.UTF8.GetBytes(originalValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Convert.ToBase64String(ms.ToArray());
        }

        public string DESEncrypt(string originalValue, string key)
        {
            return DESEncrypt(originalValue, key, key);
        }

        /// <summary>
        /// 使用DES解密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="encryptedValue">待解密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">m初始化向量(最大長度8)</param>
        /// <returns>解密後的字符串</returns>
        public string DESDecrypt(string encryptedValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateDecryptor();
            byt = Convert.FromBase64String(encryptedValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Encoding.UTF8.GetString(ms.ToArray());
        }


        private void button2_Click(object sender, EventArgs e)
        {
            //各種加密算法
            byte[] tmpByte;
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            tmpByte = sha1.ComputeHash(GetKeyByteArray(str_clear_text));
            sha1.Clear();
            str_encrypted_text = GetStringValue(tmpByte);

            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA1\t長度：" + str_encrypted_text.Length + "\n";

            //byte[] tmpByte;
            SHA256 sha256 = new SHA256Managed();
            tmpByte = sha256.ComputeHash(GetKeyByteArray(str_clear_text));
            sha256.Clear();
            str_encrypted_text = GetStringValue(tmpByte);

            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA256\t長度：" + str_encrypted_text.Length + "\n";

            //byte[] tmpByte;
            SHA512 sha512 = new SHA512Managed();
            tmpByte = sha512.ComputeHash(GetKeyByteArray(str_clear_text));
            sha512.Clear();
            str_encrypted_text = GetStringValue(tmpByte);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA512\t長度：" + str_encrypted_text.Length + "\n";

            string key = "abc";
            str_encrypted_text = DESEncrypt(str_clear_text, key);
            richTextBox1.Text += "DES Enc = " + str_encrypted_text + "\n";

            string str_encrypted_text_decrypted = DESDecrypt(str_encrypted_text, key, "0");
            richTextBox1.Text += "DES Dec = " + str_encrypted_text_decrypted + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //算一個字串的SHA1值

            byte[] data = new byte[5];
            byte[] result;

            data[0] = (byte)'A';
            data[1] = (byte)'B';
            data[2] = (byte)'C';
            data[3] = (byte)'D';
            data[4] = (byte)'E';

            SHA1 sha = new SHA1CryptoServiceProvider();
            // This is one implementation of the abstract class SHA1.
            result = sha.ComputeHash(data);
            richTextBox1.Text += "SHA1 : " + result.ToArray().ToString() + "\n";

            //TBD

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //各種加密算法
            byte[] input;
            byte[] output;

            SHA1 sha1 = new SHA1CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha1.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA1\n";


            SHA256 sha256 = new SHA256CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha256.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA256\n";


            SHA384 sha384 = new SHA384CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha384.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA384\n";


            SHA512 sha512 = new SHA512CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha512.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA512\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //各種加密算法

            //SHA1
            richTextBox1.Text += "SHA1\n";
            UnicodeEncoding oConvert = new UnicodeEncoding();
            Byte[] bytData = oConvert.GetBytes(str_clear_text);
            System.Security.Cryptography.SHA1Managed oSha1 = new System.Security.Cryptography.SHA1Managed();
            Byte[] bytResult = oSha1.ComputeHash(bytData);
            foreach (int oItem in bytResult)
            {
                richTextBox1.Text += oItem.ToString("X");
            }
            richTextBox1.Text += "\n\n";


            //SHA512
            richTextBox1.Text += "SHA512\n";
            //SHA512程式碼只有三行就解決了
            System.Security.Cryptography.SHA512 oSHA = new System.Security.Cryptography.SHA512Managed();
            byte[] aryByte = oSHA.ComputeHash(Encoding.UTF8.GetBytes(str_clear_text));
            richTextBox1.Text += System.BitConverter.ToString(aryByte).Replace("-", "");
            richTextBox1.Text += "\n\n";


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

        private void button10_Click(object sender, EventArgs e)
        {
            //c# 生成SHA1加密字符串，

            var strRes = Encoding.Default.GetBytes(str_clear_text);
            HashAlgorithm iSha = new SHA1CryptoServiceProvider();
            strRes = iSha.ComputeHash(strRes);
            var str_encrypted_text = new StringBuilder();
            foreach (byte iByte in strRes)
            {
                str_encrypted_text.AppendFormat("{0:x2}", iByte);
            }

            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\tSHA1\t長度：" + str_encrypted_text.Length + "\n";


            //另一種SHA1加密

            string key = "123";
            HMACSHA1 hmacsha1 = new HMACSHA1(Encoding.UTF8.GetBytes(key));
            byte[] rstRes = hmacsha1.ComputeHash(Encoding.UTF8.GetBytes(str_clear_text));
            string strs = Convert.ToBase64String(rstRes);


            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + strs + "\tSHA1\t長度：" + strs.Length + "\n";

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

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

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }

    public static class EncryptHelper
    {
        /// <summary>
        /// 基于Sha1的自定义加密字符串方法：输入一个字符串，返回一个由40个字符组成的十六进制的哈希散列（字符串）。
        /// </summary>
        /// <param name="str">要加密的字符串</param>
        /// <returns>加密后的十六进制的哈希散列（字符串）</returns>
        public static string Sha1(this string str)
        {
            var buffer = Encoding.UTF8.GetBytes(str);
            var data = SHA1.Create().ComputeHash(buffer);

            var sb = new StringBuilder();
            foreach (var t in data)
            {
                sb.Append(t.ToString("X2"));
            }
            return sb.ToString();
        }
    }


}
