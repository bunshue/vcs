using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography; //for CryptoConfig

namespace vcs_Cryptography1_MD5
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

            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //MD5(用自建函數)

            str_encrypted_text = MD5_Ecnrypt01(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            string key = "123";
            str_encrypted_text = MD5_Ecnrypt02(str_clear_text + key);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t加key\n";

            str_encrypted_text = MD5_Ecnrypt03(str_clear_text + key);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt04(str_clear_text, key);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt05_big(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t32位MD5\n";

            str_encrypted_text = MD5_Ecnrypt06_big(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t32位MD5\n";

            str_encrypted_text = MD5_Ecnrypt06_small(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t16位MD5\n";

            str_encrypted_text = MD5_Ecnrypt07(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt08(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt10(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt11(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt12(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt13(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt14(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt15(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt16(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt17(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt18(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //19
            ///此種加密之後的字符串是三十二位的(字母加數據)字符串  
            /// Example: password是admin 加密變成後21232f297a57a5a743894a0e4a801fc3
            str_encrypted_text = MD5_Ecnrypt19(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt20(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //16位的MD5加密
            str_encrypted_text = MD5_Ecnrypt21_16(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //32位的MD5加密
            str_encrypted_text = MD5_Ecnrypt21_32(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //64位的MD5加密
            str_encrypted_text = MD5_Ecnrypt21_64(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            int code_length = 16;
            str_encrypted_text = MD5_Ecnrypt22(str_clear_text, code_length);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            code_length = 32;
            str_encrypted_text = MD5_Ecnrypt22(str_clear_text, code_length);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt23(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt23(str_clear_text, Encoding.Unicode);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt24(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt25(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt26(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt28(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt29(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnrypt30(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
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

        //自建函數 ST

        public static string MD5_Ecnrypt01(string str)
        {
            string md5Result = "";

            //這裡Hash算法用MD5算法為例，MD5加密是不可逆的，所以只有加密沒有解密。
            //明文密碼由字符串轉換為byte數組
            byte[] clearBytes = new UnicodeEncoding().GetBytes(str);
            //由明文的byte數組計算出MD5密文byte數組
            byte[] hashedBytes = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(clearBytes);

            //把byte數組轉換為字符串後返回，BitConverter用於將基礎數據類型與字節數組相互轉換
            md5Result = BitConverter.ToString(hashedBytes);

            return md5Result;
        }

        //C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串
        public static string MD5_Ecnrypt02(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象

            // 將需要加密的字符串轉為byte數組
            byte[] input = UTF8Encoding.UTF8.GetBytes(str);

            // 生成16位的二進制校驗碼
            byte[] output = md5.ComputeHash(input);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < output.Length; i++)
            {
                hashString += Convert.ToString(output[i], 16).PadLeft(2, '0');
            }

            md5Result = hashString.PadLeft(32, '0');
            return md5Result;
        }

        public static string MD5_Ecnrypt03(string str)
        {
            string md5Result = "";

            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(str);

            MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += System.Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            md5Result = hashString.PadLeft(32, '0');
            return md5Result;
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="value">需要加密的值</param>
        /// <param name="pwSalt">附加值</param>
        /// <returns></returns>
        public static string MD5_Ecnrypt04(string str, string key)
        {
            string md5Result = "";

            HashAlgorithm hashAlgorithm = new MD5CryptoServiceProvider(); // or SHA1CryptoServiceProvider();

            byte[] result = hashAlgorithm.ComputeHash(Encoding.UTF8.GetBytes(key + str));

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.Length; i++)
            {
                sb.Append(result[i].ToString("X2"));
            }
            md5Result = sb.ToString();

            return md5Result;
        }

        /// <summary>
        /// 32位md5
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public static string MD5_Ecnrypt05_big(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象
            //MD5 md5 = MD5.Create();    //創建MD5對象, same

            byte[] output = md5.ComputeHash(Encoding.UTF8.GetBytes(str));

            for (int i = 0; i < output.Length; i++)
            {
                md5Result = md5Result + output[i].ToString("X2");
            }

            return md5Result;
        }

        /// <summary>
        /// MD5 32位加密
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public static string MD5_Ecnrypt06_big(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] output = md5.ComputeHash(Encoding.UTF8.GetBytes(str));
            // 通過使用循環，將字節類型的數組轉換為字符串，此字符串是常規字符格式化所得
            for (int i = 0; i < output.Length; i++)
            {
                md5Result = md5Result + output[i].ToString("X2");
            }
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

            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            md5Result = BitConverter.ToString(md5.ComputeHash(UTF8Encoding.Default.GetBytes(str)), 4, 8);
            md5Result = md5Result.Replace("-", "");
            //md5Result = md5Result.ToLower();  //轉為小寫

            return md5Result;
        }

        public static string MD5_Ecnrypt07(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.Default.GetBytes(str); //將字符串轉換為字節數組
            byte[] output = md5.ComputeHash(input); //調用ComputeHash方法把數組傳進去
            //將字節數組中每個元素ToString();
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                sb.Append(output[i].ToString("X2"));
            }
            md5Result = sb.ToString();

            return md5Result;
        }

        public static string MD5_Ecnrypt08(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            //開始加密
            //需要將字串轉為位元組陣列
            byte[] input = Encoding.Default.GetBytes(str);
            //返回一個加密好的位元組陣列
            byte[] output = md5.ComputeHash(input);

            //將位元組陣列轉換成字串
            //位元組陣列---字串
            //1.將位元組陣列中每個元素按照自定的編碼格式解析成字串
            //2.直接將陣列ToString();
            //3.將位元組陣列中的每個元素ToString()
            //  return Encoding.Default.GetString(output);

            for (int i = 0; i < output.Length; i++)
            {
                md5Result += output[i].ToString("X2");
            }
            return md5Result;
        }

        public static string MD5_Ecnrypt10(string str)
        {
            string md5Result = "";

            //MD5 Encode但不轉Base64 String
            //        MSSQL 使用
            //        select SUBSTRING(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','加密字串')),3,32)
            //        可得同樣結果

            // step 1, calculate MD5 hash from input

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] input = Encoding.ASCII.GetBytes(str);
            //byte[] input = Encoding.Unicode.GetBytes(str);
            //byte[] input = Encoding.UTF8.GetBytes(str);
            byte[] output = md5.ComputeHash(input);

            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                sb.Append(output[i].ToString("X2"));
            }
            md5Result = sb.ToString();

            return md5Result;
        }

        public static string MD5_Ecnrypt11(string str)
        {
            string md5Result = "";

            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            byte[] output = md5.ComputeHash(Encoding.ASCII.GetBytes(str));
            //byte[] output = md5.ComputeHash(str);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                sb.AppendFormat("{0:X2}", output[i]);
            }
            md5Result = sb.ToString();

            return md5Result;
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="text">原文</param>
        public static string MD5_Ecnrypt12(string str)
        {
            string md5Result = "";

            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            byte[] output = md5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(str));
            StringBuilder sb = new StringBuilder();
            foreach (byte b in output)
            {
                sb.Append(b.ToString("X2"));
            }
            md5Result = sb.ToString();

            return md5Result;
        }

        public static string MD5_Ecnrypt13(string str)
        {
            string md5Result = "";

            MD5 md5 = new MD5CryptoServiceProvider();

            byte[] input = Encoding.Unicode.GetBytes(str);
            byte[] output = md5.ComputeHash(input);

            for (int i = 0; i < output.Length; i++)
            {
                md5Result += output[i].ToString("X2");
            }

            return md5Result;
        }

        ///   <summary>
        ///   給一個字符串進行MD5加密
        ///   </summary>
        ///   <param   name="strText">待加密字符串</param>
        ///   <returns>加密後的字符串</returns>
        public static string MD5_Ecnrypt14(string str)
        {
            string md5Result = "";

            MD5 md5 = new MD5CryptoServiceProvider();

            byte[] output = md5.ComputeHash(Encoding.Default.GetBytes(str));
            md5Result = Encoding.Default.GetString(output);

            return md5Result;
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

            MD5 md5 = new MD5CryptoServiceProvider();

            byte[] result = md5.ComputeHash(GetKeyByteArray(getstrIN(str)));
            //byte[] output = md5.ComputeHash(input);
            md5Result = GetStringValue(result);

            return md5Result;

            /* fail
            byte[] result = md5.ComputeHash(Encoding.Default.GetBytes(strText));
            md5Result= Encoding.Default.GetString(result);
            return md5Result;
            */
        }

        public static string MD5_Ecnrypt16(string str)
        {
            string md5Result = "";  //定義一個變量，用來記錄加密後的密碼

            MD5 md5 = new MD5CryptoServiceProvider();   //創建MD5對象

            byte[] data = Encoding.Default.GetBytes(str);//將字串編碼為一個Byte序列
            byte[] md5data = md5.ComputeHash(data);//計算data Byte array的Hash值
            md5.Clear();    //清空MD5對象
            for (int i = 0; i < md5data.Length - 1; i++)//遍歷Byte數組
            {
                md5Result += md5data[i].ToString("X2").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }

            return md5Result;//返回得到的加密字串
        }

        public static string MD5_Ecnrypt17(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            // Convert the input string to a byte array and compute the hash.
            byte[] data = md5.ComputeHash(Encoding.UTF8.GetBytes(str));
            //byte[] output = md5.ComputeHash(input);

            // Create a new Stringbuilder to collect the bytes
            // and create a string.
            StringBuilder sb = new StringBuilder();

            // Loop through each byte of the hashed data 
            // and format each one as a hexadecimal string.
            for (int i = 0; i < data.Length; i++)
            {
                sb.Append(data[i].ToString("X2"));
            }

            // Return the hexadecimal string.
            md5Result = sb.ToString();

            return md5Result;
        }

        public static string MD5_Ecnrypt18(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            byte[] bData = md5.ComputeHash(Encoding.Unicode.GetBytes(str));
            for (int i = 0; i < bData.Length; i++)
            {
                md5Result = md5Result + bData[i].ToString("X2");
            }
            return md5Result;
        }

        public string MD5_Ecnrypt19(string str)
        {
            string md5Result = "";

            ///此種加密之後的字符串是三十二位的(字母加數據)字符串  
            /// Example: password是admin 加密變成後21232f297a57a5a743894a0e4a801fc3

            try
            {
                MD5 md5 = MD5.Create();    //創建MD5對象

                byte[] hashs = md5.ComputeHash(Encoding.UTF8.GetBytes(str));

                foreach (byte by in hashs)
                {
                    //這裡是字母加上數據進行加密.//3y 可以,y3不可以或 x3j等應該是超過32位不可以
                    md5Result += by.ToString("X2");
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.ToString() + "\n";
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            return md5Result;
        }

        /*
        //c#實現md5加密
        1. 首先創建MD5的哈希算法。
        ((HashAlgorithm)System.Security.Cryptogrophy.CryptoConfig.CreateFromName("MD5")).ComputeHash(System.Text.UTF8.GetBytes(input))
        2.計算哈希值
        使用方法:ComputeHash(byte[] value);
        3.轉化成字符串.
        */
        public static string MD5_Ecnrypt20(string str)
        {
            string md5Result = "";

            byte[] result = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(System.Text.Encoding.UTF8.GetBytes(str));
            StringBuilder sb = new StringBuilder(16);
            for (int i = 0; i < result.Length; i++)
            {
                // convert from hexa-decimal to character
                sb.Append((result[i]).ToString("X2", System.Globalization.CultureInfo.InvariantCulture));
            }
            md5Result = sb.ToString();

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

            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            md5Result = BitConverter.ToString(md5.ComputeHash(Encoding.Default.GetBytes(str)), 4, 8);
            md5Result = md5Result.Replace("-", "");

            return md5Result;
        }

        //32位的MD5加密
        /// <summary>
        /// 32位MD5加密
        /// </summary>
        /// <param name="password"></param>
        /// <returns></returns>
        public static string MD5_Ecnrypt21_32(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(str));
            // 通過使用循環，將字節類型的數組轉換為字符串，此字符串是常規字符格式化所得
            for (int i = 0; i < s.Length; i++)
            {
                // 將得到的字符串使用十六進制類型格式。格式後的字符是小寫的字母，如果使用大寫（X）則格式後的字符是大寫字符 
                md5Result = md5Result + s[i].ToString("X2");
            }
            return md5Result;
        }

        //64位的MD5加密
        public static string MD5_Ecnrypt21_64(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象

            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(str));
            md5Result = Convert.ToBase64String(s);

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
        /// <returns></returns>
        public static string MD5_Ecnrypt23(string str)
        {
            string md5Result = "";

            md5Result = MD5_Ecnrypt23(str, new UTF8Encoding());

            return md5Result;
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="input">需要加密的字符串</param>
        /// <param name="encode">字符的編碼</param>
        /// <returns></returns>
        public static string MD5_Ecnrypt23(string str, Encoding encode)
        {
            string md5Result = "";

            MD5 md5 = new MD5CryptoServiceProvider();

            byte[] t = md5.ComputeHash(encode.GetBytes(str));
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < t.Length; i++)
            {
                sb.Append(t[i].ToString("X2").PadLeft(2, '0'));
            }
            md5Result = sb.ToString();

            return md5Result;
        }

        public static string MD5_Ecnrypt24(string str)
        {
            string md5Result = "";

            MD5 md5 = MD5.Create();    //創建MD5對象
            byte[] input = Encoding.Default.GetBytes(str);
            byte[] output = md5.ComputeHash(input);
            md5Result = Convert.ToBase64String(output);

            return md5Result;
        }

        public string MD5_Ecnrypt25(string str)
        {
            string md5Result = "";

            MD5 md5 = new MD5CryptoServiceProvider();

            byte[] tmpByte = md5.ComputeHash(GetKeyByteArray(str));
            md5.Clear();
            md5Result = GetStringValue(tmpByte);

            return md5Result;
        }

        public static string MD5_Ecnrypt26(string str)
        {
            string md5Result = "";

            MD5 md5 = new MD5CryptoServiceProvider();

            byte[] input = Encoding.Default.GetBytes(str);
            byte[] output = md5.ComputeHash(input);

            md5Result = BitConverter.ToString(output).Replace("-", "");
            //md5Result = Encoding.Default.GetString(output);

            return md5Result;
        }

        public static string MD5_Ecnrypt28(string str)
        {
            string md5Result = "";

            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            md5Result = ASCIIEncoding.ASCII.GetString(md5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(str)));

            return md5Result;
        }

        public static string MD5_Ecnrypt29(string str)
        {
            string md5Result = "";

            //獲取加密服務  
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            //獲取要加密的字段，並轉化為Byte[]數組  
            byte[] testEncrypt = Encoding.Unicode.GetBytes(str);

            //加密Byte[]數組  
            byte[] resultEncrypt = md5.ComputeHash(testEncrypt);

            //將加密後的數組轉化為字段(普通加密)  
            string testResult = Encoding.Unicode.GetString(resultEncrypt);

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            md5Result = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5");

            return md5Result;
        }

        public static string MD5_Ecnrypt30(string str)
        {
            string md5Result = "";

            //建立MD5的演算法
            HashAlgorithm hashAlgorithm = MD5.Create();
            //取得MD5演算後的陣列
            byte[] hash = hashAlgorithm.ComputeHash(Encoding.UTF8.GetBytes(str));

            //依序轉存到md5Result
            foreach (byte b in hash)
            {
                md5Result += b.ToString("X2");
            }
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
            //将输入字符串转换成字节数组
            var buffer = Encoding.Default.GetBytes(str);
            //接着，创建Md5对象进行散列计算
            var data = MD5.Create().ComputeHash(buffer);
            //byte[] output = md5.ComputeHash(input);

            //创建一个新的Stringbuilder收集字节
            StringBuilder sb = new StringBuilder();

            //遍历每个字节的散列数据
            foreach (var t in data)
            {
                //格式每一个十六进制字符串
                sb.Append(t.ToString("X2"));
            }

            //返回十六进制字符串
            return sb.ToString();
        }
    }

    public class My_MD5
    {
        public static string EncryptCode(string password)
        {
            //明文密碼由字符串轉換為byte數組
            byte[] clearBytes = new UnicodeEncoding().GetBytes(password);
            //由明文的byte數組計算出MD5密文byte數組
            byte[] hashedBytes = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(clearBytes);

            //把byte數組轉換為字符串後返回，BitConverter用於將基礎數據類型與字節數組相互轉換
            return BitConverter.ToString(hashedBytes);
        }
    }

    public class Safety
    {
        public static string MD5(string str)
        {
            string md5Result = "";

            MD5 md5 = System.Security.Cryptography.MD5.Create();    //此行不能簡略
            byte[] bData = md5.ComputeHash(Encoding.Unicode.GetBytes(str));
            //byte[] output = md5.ComputeHash(input);
            for (int i = 0; i < bData.Length; i++)
            {
                md5Result = md5Result + bData[i].ToString("X2");
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
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            byte[] bArr = md5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(text));
            StringBuilder sb = new StringBuilder();
            foreach (byte b in bArr)
            {
                sb.Append(b.ToString("X2"));
            }
            return sb.ToString();
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
    byte[] inputByteArray = Encoding.Default.GetBytes(targetValue);
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
             MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象 1111
             byte[] buffer = md5.ComputeHash(stream);
             StringBuilder sb = new StringBuilder();
             foreach (byte var in buffer)
                 sb.Append(var.ToString("X2"));
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
             MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
 * 
             string result = BitConverter.ToString(md5.ComputeHash(encode.GetBytes(input)), 4, 8);
             result = result.Replace("-", "");
             return result;
         }
         #endregion




            //將字串用MD5加密
            Console.Write("請輸入密碼 : ");
            string P_str_Code = Console.ReadLine();//记录要加密的密码
            Program program = new Program();//创建Program对象
            Console.WriteLine("結果:\n" + program.Encrypt2(P_str_Code));//输出加密后的字符串


 //獲取要加密的字段，並轉化為Byte[]數組
            byte[] input = Encoding.Unicode.GetBytes(str.ToCharArray());
            //建立加密服務
            MD5 md5 = new MD5CryptoServiceProvider();
 
            //加密Byte[]數組
            byte[] output = md5.ComputeHash(input);






異名同義字
            MD5 md5 = new MD5CryptoServiceProvider();
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();




*/



