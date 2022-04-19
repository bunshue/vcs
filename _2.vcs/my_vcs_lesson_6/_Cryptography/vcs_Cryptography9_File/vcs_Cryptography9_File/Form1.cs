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

//文件校驗工具的開發及問題，校驗工具開發

namespace vcs_Cryptography9_File
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

        private void button1_Click(object sender, EventArgs e)
        {

            string filename = @"C:\______test_files\picture1.jpg";

            string result_MD5 = ValidHelper.GetFileMD5(filename);
            string result_SHA1 = ValidHelper.GetFileSHA1(filename);
            string result_SHA256 = ValidHelper.GetFileSHA256(filename);
            string result_SHA384 = ValidHelper.GetFileSHA384(filename);
            string result_SHA512 = ValidHelper.GetFileSHA512(filename);

            richTextBox1.Text += "MD5 : \t\t" + result_MD5 + "\n";
            richTextBox1.Text += "SHA1 : \t\t" + result_SHA1 + "\n";
            richTextBox1.Text += "SHA256 : \t" + result_SHA256 + "\n";
            richTextBox1.Text += "SHA384 : \t" + result_SHA384 + "\n";
            richTextBox1.Text += "SHA512 : \t" + result_SHA512 + "\n";

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
    }
    public static class ValidHelper
    {
        /* same
        //獲取文件的MD5值
        public static string GetFileMD5(string filePath)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] result = md5.ComputeHash(fs);
            md5.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < result.Length; i++)
            {
                sb.Append(result[i].ToString("X2"));
            }
            return sb.ToString();
        }

        //獲取文件的SHA1值
        public static string GetFileSHA1(string filePath)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] result = sha1.ComputeHash(fs);
            sha1.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < result.Length; i++)
            {
                sb.Append(result[i].ToString("X2"));
            }
            return sb.ToString();
        }
        */

        public static string GetFileHash(string filePath, HashAlgorithm algorithm)
        {
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] result = algorithm.ComputeHash(fs);
            algorithm.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < result.Length; i++)
            {
                sb.Append(result[i].ToString("X2"));
            }
            return sb.ToString();
        }

        public static string GetFileMD5(string filePath)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            return GetFileHash(filePath, md5);
        }

        public static string GetFileSHA1(string filePath)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            return GetFileHash(filePath, sha1);
        }

        public static string GetFileSHA256(string filePath)
        {
            SHA256 sha256 = SHA256.Create();
            return GetFileHash(filePath, sha256);
        }

        public static string GetFileSHA384(string filePath)
        {
            SHA384 sha384 = SHA384.Create();
            return GetFileHash(filePath, sha384);
        }

        public static string GetFileSHA512(string filePath)
        {
            SHA512 sha512 = SHA512.Create();
            return GetFileHash(filePath, sha512);
        }
    }
}
