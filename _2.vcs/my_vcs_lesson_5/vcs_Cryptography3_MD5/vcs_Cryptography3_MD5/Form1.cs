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
        public Form1()
        {
            InitializeComponent();
        }

        //第一個檔案的MD5碼
        string FirstFileMD5 = string.Empty;
        //第二個檔案的MD5碼
        string SecondFileMD5 = string.Empty;

        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
                string FirstFilePath = openFileDialog1.FileName;
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
                label1.Text = "File 1 MD5 :   " + FirstFileMD5;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox2.Text = openFileDialog1.FileName;
                string SecondFilePath = openFileDialog1.FileName;
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
                label2.Text = "File 2 MD5 :   " + SecondFileMD5;
            }
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

        private void Form1_Load(object sender, EventArgs e)
        {
            label_compare.Text = "";
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

        private void button5_Click(object sender, EventArgs e)
        {
            //利用檔案的MD5碼比對兩個檔案是否相同
            //第一個檔案
            string filename1 = "C:\\______test_files\\compare\\aaaa.txt";
            //第二個檔案
            string filename2 = "C:\\______test_files\\compare\\bbbb.txt";
            //第三個檔案
            string filename3 = "C:\\______test_files\\compare\\ssss.txt";

            //第一個檔案的MD5碼
            string FileMD5_1 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第一個檔案MD5演算後的陣列
            byte[] Hash1 = algorithm.ComputeHash(File.ReadAllBytes(filename1));
            //建立第一個檔案的MD5碼
            foreach (byte b in Hash1)
            {
                FileMD5_1 += b.ToString("X2");
            }

            //第二個檔案的MD5碼
            string FileMD5_2 = string.Empty;
            //取得第二個檔案MD5演算後的陣列
            byte[] Hash2 = algorithm.ComputeHash(File.ReadAllBytes(filename2));
            ///建立第二個檔案的MD5碼
            foreach (byte b in Hash2)
            {
                FileMD5_2 += b.ToString("X2");
            }

            //第三個檔案的MD5碼
            string FileMD5_3 = string.Empty;
            //取得第三個檔案MD5演算後的陣列
            byte[] Hash3 = algorithm.ComputeHash(File.ReadAllBytes(filename3));
            ///建立第三個檔案的MD5碼
            foreach (byte b in Hash3)
            {
                FileMD5_3 += b.ToString("X2");
            }

            if (FileMD5_1.Equals(FileMD5_2))
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename2 + " 不相同\n";

            if (FileMD5_1.Equals(FileMD5_3))
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename1 + "和檔案" + filename3 + " 不相同\n";

            if (FileMD5_2.Equals(FileMD5_3))
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 完全相同\n";
            else
                richTextBox1.Text += "檔案" + filename2 + "和檔案" + filename3 + " 不相同\n";

        }

        //對字串加MD5 ST
        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();//创建MD5对象
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//将字符编码为一个字节序列
            byte[] md5data = md5.ComputeHash(data);//计算data字节数组的哈希值
            md5.Clear();//清空MD5对象
            string str = "";//定义一个变量，用来记录加密后的密码
            for (int i = 0; i < md5data.Length - 1; i++)//遍历字节数组
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//对遍历到的字节进行加密
            }
            return str;//返回得到的加密字符串
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string str = textBox4.Text;
            string md5_result = Encrypt(str);
            richTextBox1.Text += "使用MD5加密後的結果為 : " + md5_result + "\n";
        }

        //對字串加MD5 SP


    }
}
