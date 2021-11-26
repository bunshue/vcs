using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security;
using System.Security.Cryptography;


namespace vcs_Cryptography8
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
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //MD5，SHA1，SHA256，SHA512 ST
        private string getstrIN(string strIN)
        {
            if (strIN.Length == 0)
            {
                strIN = "~NULL~";
            }
            return strIN;
        }

        public string MD5Encrypt(string strIN)
        {
            byte[] tmpByte;
            MD5 md5 = new MD5CryptoServiceProvider();
            tmpByte = md5.ComputeHash(GetKeyByteArray(getstrIN(strIN)));
            md5.Clear();
            return GetStringValue(tmpByte);
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

        /**/
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

        /**/
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

        public string DESDecrypt(string encryptedValue, string key)
        {
            return DESDecrypt(encryptedValue, key, key);
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

        private void button0_Click(object sender, EventArgs e)
        {
            //MD5，SHA1，SHA256，SHA512
            //此類提供MD5，SHA1，SHA256，SHA512等四種算法，加密字串的長度依次增大。
            string str = "lion-mouse";

            string s1 = MD5Encrypt(str);
            string s2 = SHA1Encrypt(str);
            string s3 = SHA256Encrypt(str);
            string s4 = SHA512Encrypt(str);


            richTextBox1.Text += "s1 = " + s1 + "\n";
            richTextBox1.Text += "s2 = " + s2 + "\n";
            richTextBox1.Text += "s3 = " + s3 + "\n";
            richTextBox1.Text += "s4 = " + s4 + "\n";
        }
        //MD5，SHA1，SHA256，SHA512 SP

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

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

        private void button10_Click(object sender, EventArgs e)
        {

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
    }
}

