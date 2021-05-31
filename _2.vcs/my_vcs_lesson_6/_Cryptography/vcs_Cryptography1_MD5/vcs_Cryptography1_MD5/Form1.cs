using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography;

namespace vcs_Cryptography1_MD5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

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

        private void button1_Click(object sender, EventArgs e)
        {
            /*
            //將字串用MD5加密
            Console.Write("請輸入密碼 : ");
            string P_str_Code = Console.ReadLine();//记录要加密的密码
            Program program = new Program();//创建Program对象
            Console.WriteLine("結果:\n" + program.Encrypt(P_str_Code));//输出加密后的字符串
            */
            string input = "lion";
            string output = Encrypt(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = Encrypt(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

        }
    }
}
