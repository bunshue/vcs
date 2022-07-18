using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography; //for MD5

namespace vcs_Cryptography4_MD5_SHA1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //取得檔案的唯一檢查碼Checksum MD5 SHA
        private void button1_Click(object sender, EventArgs e)
        {
            //這個有問題～～～～～～
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "open file ok, filename: " + openFileDialog1.FileName + "\n";

                using (FileStream fs = File.OpenRead(openFileDialog1.FileName))
                {
                    //SHA Code :
                    SHA256Managed sha = new SHA256Managed();
                    richTextBox1.Text += "SHA code:\n";
                    richTextBox1.Text += Convert.ToBase64String(sha.ComputeHash(fs)) + "\n";

                    //MD5 Code :
                    MD5 m = MD5.Create();
                    richTextBox1.Text += "MD5 code:\n";
                    richTextBox1.Text += Convert.ToBase64String(m.ComputeHash(fs)) + "\n";
                }
            }
            else
                richTextBox1.Text += "open file fails\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //用MD5比較兩個檔案

            //第一個檔案
            string FirstFilePath = "c://______test_files//bear.jpg";
            //第二個檔案
            string SecondFilePath = "c://______test_files//lion.jpg";
            //第一個檔案的MD5碼
            string FirstFileMD5 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第一個檔案MD5演算後的陣列
            byte[] FirstHash = algorithm.ComputeHash(File.ReadAllBytes(FirstFilePath));
            //建立第一個檔案的MD5碼
            foreach (byte b in FirstHash)
            {
                FirstFileMD5 += b.ToString("X2");
            }
            //第二個檔案的MD5碼
            string SecondFileMD5 = string.Empty;
            //取得第二個檔案MD5演算後的陣列
            byte[] SecondHash = algorithm.ComputeHash(File.ReadAllBytes(SecondFilePath));
            ///建立第二個檔案的MD5碼
            foreach (byte b in SecondHash)
            {
                SecondFileMD5 += b.ToString("X2");
            }

            richTextBox1.Text += "檔案：" + FirstFilePath + ",\tMD5：" + FirstFileMD5 + "\n";
            richTextBox1.Text += "檔案：" + SecondFilePath + ",\tMD5：" + SecondFileMD5 + "\n";

            if (FirstFileMD5.Equals(SecondFileMD5))
                richTextBox1.Text += "兩個檔案\t完全相同\n";
            else
                richTextBox1.Text += "兩個檔案\t不相同\n";
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
            richTextBox1.Text += "SHA1 : " + result.ToString() + "\n";

        }

        private void button8_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                using (FileStream fs = File.OpenRead(openFileDialog1.FileName))
                {
                    SHA256Managed sha = new SHA256Managed();
                    richTextBox1.Text += "SHA1 result : " + Convert.ToBase64String(sha.ComputeHash(fs));
                }
            }

        }


        private void button9_Click(object sender, EventArgs e)
        {
        }
    }
}
