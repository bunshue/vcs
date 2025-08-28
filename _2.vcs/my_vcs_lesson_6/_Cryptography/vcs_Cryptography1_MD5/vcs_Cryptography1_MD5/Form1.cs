using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography; //for CryptoConfig

namespace vcs_Cryptography1_MD5
{
    public partial class Form1 : Form
    {
        //欲進行加密的字符串  
        string str_clear_text = "this is a lion-mouse";

        //加密後的結果
        string str_encrypted_text = string.Empty;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";                      //準備算MD5的檔案

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

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //拜列轉字串
        public static string BytesToString(byte[] bytes)
        {
            string result = "";
            foreach (byte b in bytes)
            {
                result += b.ToString("X2");
            }
            return result;
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //MD5(用自建函數)

            string key = "123";

            str_encrypted_text = MD5_Ecnrypt01(str_clear_text, key);
            richTextBox1.Text += "01明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt02(str_clear_text + key);
            richTextBox1.Text += "02明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t加key\n";

            str_encrypted_text = MD5_Ecnrypt06_small(str_clear_text);
            richTextBox1.Text += "06明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t\t16位MD5\n";

            str_encrypted_text = MD5_Ecnrypt07(str_clear_text);
            richTextBox1.Text += "07明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt14(str_clear_text);
            richTextBox1.Text += "14明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt15(str_clear_text);
            richTextBox1.Text += "15明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt16(str_clear_text);
            richTextBox1.Text += "16明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt18(str_clear_text);
            richTextBox1.Text += "18明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt20(str_clear_text);
            richTextBox1.Text += "20明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //16位的MD5加密
            str_encrypted_text = MD5_Ecnrypt21_16(str_clear_text);
            richTextBox1.Text += "21明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //64位的MD5加密
            str_encrypted_text = MD5_Ecnrypt21_64(str_clear_text);
            richTextBox1.Text += "21明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            int code_length = 16;
            str_encrypted_text = MD5_Ecnrypt22(str_clear_text, code_length);
            richTextBox1.Text += "22明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            code_length = 32;
            str_encrypted_text = MD5_Ecnrypt22(str_clear_text, code_length);
            richTextBox1.Text += "22明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt23(str_clear_text, new UTF8Encoding());
            richTextBox1.Text += "23明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt23(str_clear_text, Encoding.Unicode);
            richTextBox1.Text += "23明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt25(str_clear_text);
            richTextBox1.Text += "25明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt28(str_clear_text);
            richTextBox1.Text += "28明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //MD5(用類別)
            str_encrypted_text = str_clear_text.Md5();
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = My_MD5.EncryptCode(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = Safety.MD5(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5Helper.Encrypt(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
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
            //用MD5比較兩個檔案

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\compare\aaaa.txt";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\compare\bbbb.txt";
            string FileMD5_1 = string.Empty;    //第1個檔案的MD5碼
            string FileMD5_2 = string.Empty;    //第2個檔案的MD5碼

            MD5 md5 = MD5.Create();    //創建MD5對象
            //取得第一個檔案MD5演算後的陣列
            byte[] input1 = File.ReadAllBytes(filename1);
            byte[] md5Hash1 = md5.ComputeHash(input1);  //算拜列之Hash值

            //建立第一個檔案的MD5碼
            FileMD5_1 = BytesToString(md5Hash1);    //Hash轉字串
            
            //取得第二個檔案MD5演算後的陣列
            byte[] input2 = File.ReadAllBytes(filename2);
            byte[] md5Hash2 = md5.ComputeHash(input2);  //算拜列之Hash值

            //建立第二個檔案的MD5碼
            FileMD5_2 = BytesToString(md5Hash2);    //Hash轉字串

            richTextBox1.Text += "檔案：" + filename1 + ",\tMD5：" + FileMD5_1 + "\n";
            richTextBox1.Text += "檔案：" + filename2 + ",\tMD5：" + FileMD5_2 + "\n";

            if (FileMD5_1.ToLower() == FileMD5_2.ToLower())
            {
                richTextBox1.Text += "兩個檔案\t完全相同\n";
            }
            else
            {
                richTextBox1.Text += "兩個檔案\t不相同\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //算一個檔案的MD5值
            str_encrypted_text = GetMD5HashFromFile(filename);
            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";

            //算一個檔案的MD5值
            str_encrypted_text = BytesToString(GetHashMD5(filename));
            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";

            //算一個檔案的MD5值
            str_encrypted_text = HashHelper.MD5File(filename);
            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";

            //算一個檔案的MD5值
            str_encrypted_text = ValidHelper.GetFileMD5(filename);
            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";

            //算一個檔案的MD5值
            //檔案轉拜列轉Hash值
            byte[] md5Hash = GetHashMD5(filename);

            //Hash轉字串
            str_encrypted_text = Convert.ToBase64String(md5Hash);
            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";
        }

        // Compute the file's hash.
        private byte[] GetHashMD5(string filename)
        {
            MD5 md5 = MD5.Create();

            FileStream fs = File.OpenRead(filename);
            byte[] md5Hash = md5.ComputeHash(fs);   //算拜列之Hash值
            fs.Close();

            return md5Hash;
        }

        /// <summary>
        /// 獲取文件MD5值
        /// </summary>
        /// <param name="fileName">文件絕對路徑</param>
        /// <returns>MD5值</returns>
        public static string GetMD5HashFromFile(string filename)
        {
            try
            {
                MD5 md5 = MD5.Create();    //創建MD5對象

                FileStream fs = new FileStream(filename, FileMode.Open);
                byte[] md5Hash = md5.ComputeHash(fs);   //算拜列之Hash值
                fs.Close();

                //Hash轉字串
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < md5Hash.Length; i++)
                {
                    sb.Append(md5Hash[i].ToString("x2"));
                }
                return sb.ToString();
            }
            catch (Exception ex)
            {
                throw new Exception("GetMD5HashFromFile() fail,error:" + ex.Message);
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //算一個檔案的MD5值
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";                      //準備算MD5的檔案

            //加密後的結果
            string str_encrypted_text = string.Empty;

            //建立MD5的演算法
            MD5 md5 = MD5.Create();    //創建MD5對象

            //取得第一個檔案MD5演算後的陣列
            byte[] input = File.ReadAllBytes(filename);
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //建立第一個檔案的MD5碼
            str_encrypted_text = BytesToString(md5Hash);    //Hash轉字串

            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //算一個檔案的MD5值

            MD5 md5 = MD5.Create();    //創建MD5對象

            FileStream fs = new FileStream(filename, FileMode.Open);
            byte[] md5Hash = md5.ComputeHash(fs);   //算拜列之Hash值
            fs.Close();

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("x2"));
            }

            str_encrypted_text = sb.ToString();
            richTextBox1.Text += "檔案：" + filename + "\tMD5密碼：" + str_encrypted_text + "\n";
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

        //自建函數 ST

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="value">需要加密的值</param>
        /// <param name="pwSalt">附加值</param>
        /// <returns></returns>
        public static string MD5_Ecnrypt01(string str, string key)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str + key);    //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            string md5Result = BytesToString(md5Hash);  //Hash轉字串

            return md5Result;
        }

        //C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串
        public static string MD5_Ecnrypt02(string str)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            string md5Result = BytesToString(md5Hash);  //Hash轉字串

            /*
            //Hash轉字串
            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < md5Hash.Length; i++)
            {
                hashString += Convert.ToString(md5Hash[i], 16).PadLeft(2, '0');
            }

            md5Result = hashString.PadLeft(32, '0');
            */
            return md5Result;
        }

        /// <summary>
        /// MD5 16位加密
        /// </summary>
        /// <param name="ConvertString"></param>
        /// <returns></returns>
        public static string MD5_Ecnrypt06_small(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            md5Result = BitConverter.ToString(md5.ComputeHash(input), 4, 8);
            md5Result = md5Result.Replace("-", "");
            //md5Result = md5Result.ToLower();  //轉為小寫

            return md5Result;
        }

        public static string MD5_Ecnrypt07(string str)
        {
            //以此為標準
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列  111
            //byte[] input = Encoding.UTF8.GetBytes(str); //字串轉拜列   222
            //byte[] input = Encoding.ASCII.GetBytes(str);
            //byte[] input = Encoding.Unicode.GetBytes(str);
            //byte[] input = ASCIIEncoding.ASCII.GetBytes(str);   //字串轉拜列

            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值
            string md5Result = BytesToString(md5Hash);  //Hash轉字串

            return md5Result;
        }

        ///   <summary>
        ///   給一個字符串進行MD5加密
        ///   </summary>
        ///   <param   name="strText">待加密字符串</param>
        ///   <returns>加密後的字符串</returns>
        public static string MD5_Ecnrypt14(string str)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            string md5Result = Encoding.Default.GetString(md5Hash); //Hash轉字串

            return md5Result;
        }

        private string GetStringValue(byte[] Byte)
        {
            string tmpString = "";
            /*
            ASCIIEncoding Asc = new ASCIIEncoding();
            tmpString = Asc.GetString(Byte);
            */

            for (int i = 0; i < Byte.Length; i++)
            {
                tmpString = tmpString + Byte[i].ToString();
            }
            return tmpString;
        }

        private byte[] GetKeyByteArray(string str)
        {
            int tmpStrLen = str.Length;
            byte[] input = new byte[tmpStrLen - 1];
            input = new ASCIIEncoding().GetBytes(str);
            return input;
        }

        //byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列

        private string getstrIN(string strIN)
        {
            if (strIN.Length == 0)
            {
                strIN = "~NULL~";
            }
            return strIN;
        }

        ///   <summary>
        ///   給一個字符串進行MD5加密
        ///   </summary>
        ///   <param   name="strText">待加密字符串</param>
        ///   <returns>加密後的字符串</returns>
        public string MD5_Ecnrypt15(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列

            //byte[] input = GetKeyByteArray(getstrIN(str));  //字串轉拜列

            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            md5Result = GetStringValue(md5Hash);

            return md5Result;

            /* fail
            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);
            md5Result= Encoding.Default.GetString(md5Hash);
            return md5Result;
            */
        }

        public static string MD5_Ecnrypt16(string str)
        {
            string md5Result = "";  //定義一個變量，用來記錄加密後的密碼

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            for (int i = 0; i < md5Hash.Length - 1; i++)//遍歷Byte數組
            {
                md5Result += md5Hash[i].ToString("X2").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }

            return md5Result;//返回得到的加密字串
        }

        public static string MD5_Ecnrypt18(string str)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            string md5Result = BytesToString(md5Hash);  //Hash轉字串

            return md5Result;
        }

        /*
        //c#實現md5加密
        1. 首先創建MD5的哈希算法。
        ((HashAlgorithm)System.Security.Cryptogrophy.CryptoConfig.CreateFromName("MD5")).ComputeHash(UTF8.GetBytes(input))
        2.計算哈希值
        使用方法:ComputeHash(byte[] value);
        3.轉化成字符串.
        */
        public static string MD5_Ecnrypt20(string str)
        {
            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(input);

            string md5Result = BytesToString(md5Hash);  //Hash轉字串

            return md5Result;
        }

        //16位的MD5加密
        /// <summary>
        /// 16位MD5加密
        /// </summary>
        /// <param name="password"></param>
        /// <returns></returns>
        public static string MD5_Ecnrypt21_16(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            md5Result = BitConverter.ToString(md5.ComputeHash(input), 4, 8);
            md5Result = md5Result.Replace("-", "");

            return md5Result;
        }

        //64位的MD5加密
        public static string MD5_Ecnrypt21_64(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            md5Result = Convert.ToBase64String(md5Hash);

            return md5Result;
        }

        /// <summary>
        /// 加密用戶密碼
        /// </summary>
        /// <param name="password">密碼</param>
        /// <param name="codeLength">加密位數</param>
        /// <returns>加密密碼</returns>
        public static string MD5_Ecnrypt22(string str, int codeLength)
        {
            string md5Result = "";

            if (codeLength == 16)   // 16位MD5加密（取32位加密的9~25字符）  
            {
                md5Result = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5").ToUpper().Substring(8, 16);
                return md5Result;
            }
            else if (codeLength == 32)   // 32位加密
            {
                md5Result = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5").ToUpper();
                return md5Result;
            }
            else
            {
                return string.Empty;
            }
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="input">需要加密的字符串</param>
        /// <param name="encode">字符的編碼</param>
        /// <returns></returns>
        public static string MD5_Ecnrypt23(string str, Encoding encode)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = encode.GetBytes(str); //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            string md5Result = BytesToString(md5Hash);  //Hash轉字串

            return md5Result;
        }

        public string MD5_Ecnrypt25(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = GetKeyByteArray(str); //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            md5Result = GetStringValue(md5Hash);

            return md5Result;
        }

        public static string MD5_Ecnrypt28(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            md5Result = ASCIIEncoding.ASCII.GetString(md5.ComputeHash(input));

            return md5Result;
        }

        //自建函數 SP
    }

    public static class EncryptHelper
    {
        /// <summary>
        /// 基于Md5的自定义加密字符串方法：输入一个字符串，返回一个由32个字符组成的十六进制的哈希散列（字符串）。
        /// </summary>
        /// <param name="str">要加密的字符串</param>
        /// <returns>加密后的十六进制的哈希散列（字符串）</returns>
        public static string Md5(this string str)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                //格式每一个十六进制字符串
                sb.Append(b.ToString("X2"));
            }

            //返回十六进制字符串
            return sb.ToString();
        }
    }

    public class My_MD5
    {
        public static string EncryptCode(string str)
        {
            string md5Result = "";

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            //BitConverter用於將基礎數據類型與字節數組相互轉換
            md5Result = BitConverter.ToString(md5Hash);
            return md5Result;
        }
    }

    public class Safety
    {
        public static string MD5(string str)
        {
            string md5Result = "";

            MD5 md5 = System.Security.Cryptography.MD5.Create();    //此行不能簡略

            byte[] input = Encoding.Default.GetBytes(str);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result = md5Result + md5Hash[i].ToString("X2");
            }

            return md5Result;
        }
    }

    /// <summary>
    /// MD5加密
    /// </summary>
    public class MD5Helper
    {
        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="text">原文</param>
        public static string Encrypt(string text)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(text);  //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                sb.Append(b.ToString("X2"));
            }
            return sb.ToString();
        }
    }

    /// <summary>
    /// Hash輔助類
    /// </summary>
    public class HashHelper
    {
        /// <summary>
        /// 計算文件的 MD5 值
        /// </summary>
        /// <param name="filename">要計算 MD5 值的文件名和路徑</param>
        /// <returns>MD5 值16進制字符串</returns>
        public static string MD5File(string filename)
        {
            return HashFile(filename, "md5");
        }

        /// <summary>
        /// 計算文件的 sha1 值
        /// </summary>
        /// <param name="filename">要計算 sha1 值的文件名和路徑</param>
        /// <returns>sha1 值16進制字符串</returns>
        public static string SHA1File(string filename)
        {
            return HashFile(filename, "sha1");
        }

        /// <summary>
        /// 計算文件的哈希值
        /// </summary>
        /// <param name="filename">要計算哈希值的文件名和路徑</param>
        /// <param name="algorithm">算法:SHA1 或 MD5</param>
        /// <returns>哈希值16進制字符串</returns>
        private static string HashFile(string filename, string algorithm)
        {
            if (!File.Exists(filename))
            {
                return string.Empty;
            }

            FileStream fs = new FileStream(filename, FileMode.Open, FileAccess.Read);
            byte[] hashBytes = HashData(fs, algorithm);
            fs.Close();

            return ByteArrayToHexString(hashBytes);
        }

        /// <summary>
        /// 計算哈希值
        /// </summary>
        /// <param name="stream">要計算哈希值的 Stream</param>
        /// <param name="algorithm">算法:SHA1 或 MD5</param>
        /// <returns>哈希值字節數組</returns>
        private static byte[] HashData(Stream stream, string algorithm)
        {
            HashAlgorithm hashAlgorithm;
            if (algorithm == null)
            {
                throw new ArgumentNullException("algName 不能為 null");
            }

            if (string.Compare(algorithm, "sha1", true) == 0)
            {
                hashAlgorithm = SHA1.Create();  //創建MD5對象
            }
            else
            {
                if (string.Compare(algorithm, "md5", true) != 0)
                {
                    throw new Exception("algorithm 只能使用 sha1 或 md5");
                }
                hashAlgorithm = MD5.Create();   //創建MD5對象
            }

            return hashAlgorithm.ComputeHash(stream);
        }

        /// <summary>
        /// 字節數組轉換為16進制表示的字符串
        /// </summary>
        private static string ByteArrayToHexString(byte[] buf)
        {
            return BitConverter.ToString(buf).Replace("-", "");
        }
    }

    public static class ValidHelper
    {
        /* same
        //獲取文件的MD5值
        public static string GetFileMD5(string filePath)
        {
            MD5 md5 = MD5.Create();    //創建MD5對象
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] md5Hash = md5.ComputeHash(fs);
            fs.Close();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));
            }
            return sb.ToString();
        }

        //獲取文件的SHA1值
        public static string GetFileSHA1(string filePath)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] result = sha1.ComputeHash(fs);
            fs.Close();
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
            fs.Close();
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
            MD5 md5 = MD5.Create();    //創建MD5對象
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



/*

//C#使用MD5對用戶密碼加密與驗證
//C#中常涉及到對用戶密碼的加密於解密的算法，其中使用MD5加密是最常見的的實現方式

      
5）通過DESCryptoServiceProvider對象對字符串進行加密解密

/// <summary>
/// DES數據加密
/// </summary>
/// <param name="targetValue">目標值</param>
/// <param name="key">密鑰</param>
/// <returns>加密值</returns>
public static string Encrypt(string targetValue, string key)
{
    StringBuilder sb = new StringBuilder();
    var des = new DESCryptoServiceProvider();
    byte[] inputByteArray = Encoding.Default.GetBytes(targetValue); //字串轉拜列
    // 通過兩次哈希密碼設置對稱算法的初始化向量   
    des.Key = Encoding.ASCII.GetBytes(FormsAuthentication.HashPasswordForStoringInConfigFile
                                            (FormsAuthentication.HashPasswordForStoringInConfigFile(key, "md5").
                                                Substring(0, 8), "sha1").Substring(0, 8));
    // 通過兩次哈希密碼設置算法的機密密鑰   
    des.IV = Encoding.ASCII.GetBytes(FormsAuthentication.HashPasswordForStoringInConfigFile
                                            (FormsAuthentication.HashPasswordForStoringInConfigFile(key, "md5")
                                                .Substring(0, 8), "md5").Substring(0, 8));
    var ms = new MemoryStream();
    var cs = new CryptoStream(ms, des.CreateEncryptor(), CryptoStreamMode.Write);
    cs.Write(inputByteArray, 0, inputByteArray.Length);
    cs.FlushFinalBlock();
    foreach (byte b in ms.ToArray())
    {
        sb.AppendFormat("{0:X2}", b);
    }
    return sb.ToString();
}

此種算法可以通過加密密鑰進行解密，解密方法如下：

/// <summary>
/// DES數據解密
/// </summary>
/// <param name="targetValue"></param>
/// <param name="key"></param>
/// <returns></returns>
public static string Decrypt(string targetValue, string key)
{
    // 定義DES加密對象
    var des = new DESCryptoServiceProvider();
    int len = targetValue.Length / 2;
    var inputByteArray = new byte[len];
    int x, i;
    for (x = 0; x < len; x++)
    {
        i = Convert.ToInt32(targetValue.Substring(x * 2, 2), 16);
        inputByteArray[x] = (byte)i;
    }
    // 通過兩次哈希密碼設置對稱算法的初始化向量   
    des.Key = Encoding.ASCII.GetBytes(FormsAuthentication.HashPasswordForStoringInConfigFile
                                            (FormsAuthentication.HashPasswordForStoringInConfigFile(key, "md5").
                                                Substring(0, 8), "sha1").Substring(0, 8));
    // 通過兩次哈希密碼設置算法的機密密鑰   
    des.IV = Encoding.ASCII.GetBytes(FormsAuthentication.HashPasswordForStoringInConfigFile
                                            (FormsAuthentication.HashPasswordForStoringInConfigFile(key, "md5")
                                                .Substring(0, 8), "md5").Substring(0, 8));
    // 定義內存流
    var ms = new MemoryStream();
    // 定義加密流
    var cs = new CryptoStream(ms, des.CreateDecryptor(), CryptoStreamMode.Write);
    cs.Write(inputByteArray, 0, inputByteArray.Length);
    cs.FlushFinalBlock();
    return Encoding.Default.GetString(ms.ToArray());
}




//--------------------------------------------------------------------------------------------------------------------------




         #region MD5加密
 
         /// <summary>
         /// MD5對文件流加密
         /// </summary>
         /// <param name="sr"></param>
         /// <returns></returns>
         public static string MD5Encrypt(Stream stream)
         {
             MD5 md5 = MD5.Create();    //創建MD5對象
             byte[] md5Hash = md5.ComputeHash(stream);
             StringBuilder sb = new StringBuilder();
             foreach (byte b in md5Hash)
                 sb.Append(b.ToString("X2"));
             return sb.ToString();
         }
 
         /// <summary>
         /// MD5加密(返回16位加密串)
         /// </summary>
         /// <param name="input"></param>
         /// <param name="encode"></param>
         /// <returns></returns>
         public static string MD5Encrypt16b(string input, Encoding encode)
         {
             MD5 md5 = MD5.Create();    //創建MD5對象
 * 
             string result = BitConverter.ToString(md5.ComputeHash(encode.GetBytes(input)), 4, 8);
             result = result.Replace("-", "");
             return result;
         }
         #endregion




            //將字串用MD5加密
            Console.Write("請輸入密碼：");
            string P_str_Code = Console.ReadLine();//记录要加密的密码
            Program program = new Program();//创建Program对象
            Console.WriteLine("結果:\n" + program.Encrypt2(P_str_Code));//输出加密后的字符串


 //獲取要加密的字段，並轉化為Byte[]數組
            byte[] input = Encoding.Unicode.GetBytes(str.ToCharArray());    //字串轉拜列
            //建立加密服務
            MD5 md5 = MD5.Create();    //創建MD5對象
 
            //加密Byte[]數組
            byte[] md5Hash = md5.ComputeHash(input);    //算拜列之Hash值


*/



