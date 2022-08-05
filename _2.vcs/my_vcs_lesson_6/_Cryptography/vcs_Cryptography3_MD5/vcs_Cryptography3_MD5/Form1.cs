using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;                    //for file
using System.Security.Cryptography; //for MD5

namespace vcs_Cryptography3_MD5
{
    public partial class Form1 : Form
    {
        //第一個檔案的MD5碼
        string FirstFileMD5 = string.Empty;
        //第二個檔案的MD5碼
        string SecondFileMD5 = string.Empty;

        string filename1 = @"C:\______test_files\picture1.jpg";
        string filename2 = @"C:\______test_files\elephant.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label_compare.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string FirstFilePath = filename1;
            FirstFileMD5 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第一個檔案MD5演算後的陣列
            byte[] FirstHash = algorithm.ComputeHash(File.ReadAllBytes(FirstFilePath));
            //建立第一個檔案的MD5碼
            foreach (byte b in FirstHash)
            {
                FirstFileMD5 += b.ToString("X2");
            }
            richTextBox1.Text += "File 1 MD5 :   " + FirstFileMD5 + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string SecondFilePath = filename2;
            SecondFileMD5 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第二個檔案MD5演算後的陣列
            byte[] SecondHash = algorithm.ComputeHash(File.ReadAllBytes(SecondFilePath));
            //建立第一個檔案的MD5碼
            foreach (byte b in SecondHash)
            {
                SecondFileMD5 += b.ToString("X2");
            }
            richTextBox1.Text += "File 2 MD5 :   " + SecondFileMD5 + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (FirstFileMD5 == string.Empty)
            {
                label_compare.Text = "未選擇第一個檔案";
                return;
            }
            if (SecondFileMD5 == string.Empty)
            {
                label_compare.Text = "未選擇第二個檔案";
                return;
            }
            if (FirstFileMD5.ToLower() == SecondFileMD5.ToLower())
            {
                label_compare.Text = "兩個檔案相等";
            }
            else
            {
                label_compare.Text = "兩個檔案不同";
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            {
                label4.Text = "未選取檔案";
                return;
            }
            if (textBox3.Text == "")
            {
                label4.Text = "未填入MD5值";
                return;
            }
            if (FirstFileMD5.Trim().ToLower() == textBox3.Text.Trim().ToLower())
                label4.Text = "檔案驗證正確";
            else
                label4.Text = "檔案驗證錯誤";
        }
    }
}
