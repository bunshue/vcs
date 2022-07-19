using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography;

namespace vcs_Cryptography2_SHA1
{
    public partial class Form1 : Form
    {
        //欲進行SHA1加密的字符串  
        string str_clear_text = "this is a lion-mouse";

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

            string s2 = SHA1Encrypt(str_clear_text);
            string s3 = SHA256Encrypt(str_clear_text);
            string s4 = SHA512Encrypt(str_clear_text);


            richTextBox1.Text += "s2 = " + s2 + "\n";
            richTextBox1.Text += "s3 = " + s3 + "\n";
            richTextBox1.Text += "s4 = " + s4 + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //SHA1

            richTextBox1.Text += "明碼：" + str_clear_text + "\n";

            richTextBox1.Text += "Sha1：" + str_clear_text.Sha1() + "\n";
            richTextBox1.Text += "長度：" + str_clear_text.Sha1().Length + "\n";

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            string str1 = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str_clear_text, "SHA1");
            richTextBox1.Text += "SHA1加密的密碼:" + str1 + "\tSHA1加密長度是：" + str1.Length + "\n";
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
