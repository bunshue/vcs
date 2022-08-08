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

        private void button0_Click(object sender, EventArgs e)
        {
            //MD5(用自建函數)

            //MD5
            str_encrypted_text = MD5_Ecnryp01(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //MD5   32位
            //MD5驗證 32 位元
            //使用Md5Sum算出32位的校驗碼字符串
            //MD5 校驗默認為32位的字符串， 而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，
            string key = "123";
            str_encrypted_text = MD5_Ecnryp02(str_clear_text + key);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t加key\n";

            str_encrypted_text = MD5_Ecnryp05_big(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t32位MD5\n";
            str_encrypted_text = MD5_Ecnryp05_small(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t16位MD5\n";

            str_encrypted_text = MD5_Ecnryp06_big(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t32位MD5\n";

            str_encrypted_text = MD5_Ecnryp06_small(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\t16位MD5\n";

            str_encrypted_text = MD5_Ecnryp07(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp08(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp09(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp10(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp11(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp12(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp13(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp14(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp15(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp16(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5_Ecnryp17(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            /*
            //將字串用MD5加密
            Console.Write("請輸入密碼 : ");
            string P_str_Code = Console.ReadLine();//记录要加密的密码
            Program program = new Program();//创建Program对象
            Console.WriteLine("結果:\n" + program.Encrypt2(P_str_Code));//输出加密后的字符串
            */
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
            //C# MD5驗證
            string key = "123";
            str_encrypted_text = Md5Sum(str_clear_text + key);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

        }

        public static string Md5Sum(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            System.Security.Cryptography.MD5 md5;
            md5 = System.Security.Cryptography.MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += System.Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }


        private void button3_Click(object sender, EventArgs e)
        {
            str_encrypted_text = MD5Encrypt(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = MD5Encrypt(str_clear_text, Encoding.Unicode);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="input">需要加密的字符串</param>
        /// <returns></returns>
        public static string MD5Encrypt(string input)
        {
            return MD5Encrypt(input, new UTF8Encoding());
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="input">需要加密的字符串</param>
        /// <param name="encode">字符的編碼</param>
        /// <returns></returns>
        public static string MD5Encrypt(string input, Encoding encode)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] t = md5.ComputeHash(encode.GetBytes(input));
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < t.Length; i++)
                sb.Append(t[i].ToString("x").PadLeft(2, '0'));
            return sb.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            str_encrypted_text = MD5encode(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        public static string MD5encode(string str)
        {
            string strResult = "";
            MD5 md5 = System.Security.Cryptography.MD5.Create();
            byte[] bData = md5.ComputeHash(Encoding.Unicode.GetBytes(str));
            for (int i = 0; i < bData.Length; i++)
            {
                strResult = strResult + bData[i].ToString("X");
            }
            return strResult;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string key = "123";
            str_encrypted_text = GetMD5(str_clear_text, key);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="value">需要加密的值</param>
        /// <param name="pwSalt">附加值</param>
        /// <returns></returns>
        public static string GetMD5(string value, string pwSalt)
        {
            HashAlgorithm hashAlgorithm = new MD5CryptoServiceProvider(); // or SHA1CryptoServiceProvider();
            byte[] result = hashAlgorithm.ComputeHash(Encoding.UTF8.GetBytes(pwSalt + value));

            StringBuilder sBuilder = new StringBuilder();
            for (int i = 0; i < result.Length; i++)
            {
                sBuilder.Append(result[i].ToString("x2"));
            }
            return sBuilder.ToString();
        }



        private void button6_Click(object sender, EventArgs e)
        {
            //使用Md5Sum算出32位的校驗碼字符串。
            string data = "hello world";
            string key = "123";
            Md5Sumaa(data + key);  // 返回
        }

        public static string Md5Sumaa(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            System.Security.Cryptography.MD5 md5;
            md5 = System.Security.Cryptography.MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += System.Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }


        private void button7_Click(object sender, EventArgs e)
        {
            str_encrypted_text = HashMD5(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

        }

        /*
        //c#實現md5加密

        1. 首先創建MD5的哈希算法。
        ((HashAlgorithm)System.Security.Cryptogrophy.CryptoConfig.CreateFromName("MD5")).ComputeHash(System.Text.UTF8.GetBytes(input))
        2.計算哈希值
        使用方法:ComputeHash(byte[] value);
        3.轉化成字符串.
        */

        protected virtual string HashMD5(string input)
        {
            byte[] result = ((HashAlgorithm)System.Security.Cryptography.CryptoConfig.CreateFromName("MD5")).ComputeHash(System.Text.Encoding.UTF8.GetBytes(input));
            StringBuilder output = new StringBuilder(16);
            for (int i = 0; i < result.Length; i++)
            {
                // convert from hexa-decimal to character
                output.Append((result[i]).ToString("x2", System.Globalization.CultureInfo.InvariantCulture));
            }
            return output.ToString();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            ///此種加密之後的字符串是三十二位的(字母加數據)字符串  
            /// Example: password是admin 加密變成後21232f297a57a5a743894a0e4a801fc3

            str_encrypted_text = MD5Encrypt2(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        public string MD5Encrypt2(string beforeStr)
        {
            string afterString = "";
            try
            {
                MD5 md5 = MD5.Create();
                byte[] hashs = md5.ComputeHash(Encoding.UTF8.GetBytes(beforeStr));

                foreach (byte by in hashs)
                {
                    //這裡是字母加上數據進行加密.//3y 可以,y3不可以或 x3j等應該是超過32位不可以
                    afterString += by.ToString("x2");
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.ToString() + "\n";
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            return afterString;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //16位的MD5加密
            str_encrypted_text = MD5Encrypt16(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //32位的MD5加密
            str_encrypted_text = MD5Encrypt32(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            //64位的MD5加密
            str_encrypted_text = MD5Encrypt64(str_clear_text);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            int code_length = 16;
            str_encrypted_text = md5(str_clear_text, code_length);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            code_length = 32;
            str_encrypted_text = md5(str_clear_text, code_length);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        //16位的MD5加密
        /// <summary>
        /// 16位MD5加密
        /// </summary>
        /// <param name="password"></param>
        /// <returns></returns>
        public static string MD5Encrypt16(string password)
        {
            var md5 = new MD5CryptoServiceProvider();
            string t2 = BitConverter.ToString(md5.ComputeHash(Encoding.Default.GetBytes(password)), 4, 8);
            t2 = t2.Replace("-", "");
            return t2;
        }

        //32位的MD5加密
        /// <summary>
        /// 32位MD5加密
        /// </summary>
        /// <param name="password"></param>
        /// <returns></returns>
        public static string MD5Encrypt32(string password)
        {
            string cl = password;
            string pwd = "";
            MD5 md5 = MD5.Create(); //實例化一個md5對像
            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));
            // 通過使用循環，將字節類型的數組轉換為字符串，此字符串是常規字符格式化所得
            for (int i = 0; i < s.Length; i++)
            {
                // 將得到的字符串使用十六進制類型格式。格式後的字符是小寫的字母，如果使用大寫（X）則格式後的字符是大寫字符 
                pwd = pwd + s[i].ToString("X");
            }
            return pwd;
        }

        //64位的MD5加密
        public static string MD5Encrypt64(string password)
        {
            string cl = password;
            //string pwd = "";
            MD5 md5 = MD5.Create(); //實例化一個md5對像
            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));
            return Convert.ToBase64String(s);
        }

        /// <summary>
        /// 加密用戶密碼
        /// </summary>
        /// <param name="password">密碼</param>
        /// <param name="codeLength">加密位數</param>
        /// <returns>加密密碼</returns>
        public static string md5(string str, int codeLength)
        {
            if (!string.IsNullOrEmpty(str))
            {
                // 16位MD5加密（取32位加密的9~25字符）  
                if (codeLength == 16)
                {
                    return System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5").ToLower().Substring(8, 16);
                }

                // 32位加密
                if (codeLength == 32)
                {
                    return System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5").ToLower();
                }
            }
            return string.Empty;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            MD5 md5 = MD5.Create();
            byte[] input = Encoding.Default.GetBytes(str_clear_text);
            byte[] output = md5.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] tmpByte = md5.ComputeHash(GetKeyByteArray(str_clear_text));
            md5.Clear();
            str_encrypted_text = GetStringValue(tmpByte);
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            /*
            //獲取要加密的字段，並轉化為Byte[]數組
            byte[] input = Encoding.Unicode.GetBytes(str.ToCharArray());
            //建立加密服務
            MD5 md5 = new MD5CryptoServiceProvider();
            //加密Byte[]數組
            byte[] output = md5.ComputeHash(input);
            */
        }

        private void button13_Click(object sender, EventArgs e)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] input = Encoding.Default.GetBytes(str_clear_text);
            byte[] output = md5.ComputeHash(input);

            str_encrypted_text = BitConverter.ToString(output).Replace("-", "");
            richTextBox1.Text += "明碼a：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";

            str_encrypted_text = Encoding.Default.GetString(output);
            richTextBox1.Text += "明碼b：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得MD5演算後的陣列
            byte[] hash = algorithm.ComputeHash(Encoding.UTF8.GetBytes(str_clear_text));

            str_encrypted_text = string.Empty;
            //依序轉存到str_encrypted_text
            foreach (byte b in hash)
            {
                str_encrypted_text += b.ToString("X2");
            }
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
            MD5CryptoServiceProvider M5 = new MD5CryptoServiceProvider();
            str_encrypted_text = ASCIIEncoding.ASCII.GetString(M5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(str_clear_text)));
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] input = Encoding.Default.GetBytes(str_clear_text);
            byte[] output = md5.ComputeHash(input);
            str_encrypted_text = BitConverter.ToString(output).Replace("-", "");
            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //獲取加密服務  
            MD5CryptoServiceProvider md5CSP = new MD5CryptoServiceProvider();

            //獲取要加密的字段，並轉化為Byte[]數組  
            byte[] testEncrypt = Encoding.Unicode.GetBytes(str_clear_text);

            //加密Byte[]數組  
            byte[] resultEncrypt = md5CSP.ComputeHash(testEncrypt);

            //將加密後的數組轉化為字段(普通加密)  
            string testResult = Encoding.Unicode.GetString(resultEncrypt);

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            str_encrypted_text = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str_clear_text, "MD5");

            richTextBox1.Text += "明碼：" + str_clear_text + "\t密碼：" + str_encrypted_text + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        //自建函數 ST

        public static string MD5_Ecnryp01(string password)
        {
            //這裡Hash算法用MD5算法為例，MD5加密是不可逆的，所以只有加密沒有解密。
            //明文密碼由字符串轉換為byte數組
            byte[] clearBytes = new UnicodeEncoding().GetBytes(password);
            //由明文的byte數組計算出MD5密文byte數組
            byte[] hashedBytes = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(clearBytes);

            //把byte數組轉換為字符串後返回，BitConverter用於將基礎數據類型與字節數組相互轉換
            return BitConverter.ToString(hashedBytes);
        }

        //C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串
        public static string MD5_Ecnryp02(string strToEncrypt)
        {
            MD5 md5 = MD5CryptoServiceProvider.Create();    //創建MD5對象

            // 將需要加密的字符串轉為byte數組
            byte[] input = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 生成16位的二進制校驗碼
            byte[] output = md5.ComputeHash(input);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < output.Length; i++)
            {
                hashString += Convert.ToString(output[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }

        /// <summary>
        /// 32位md5
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public static string MD5_Ecnryp05_big(string str)
        {
            string cl = str;
            string pwd = "";
            var md5 = MD5.Create();

            byte[] output = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));

            for (int i = 0; i < output.Length; i++)
            {
                pwd = pwd + output[i].ToString("X2");
            }

            return pwd;
        }

        /// <summary>
        /// 16位MD5
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public static string MD5_Ecnryp05_small(string str)
        {
            MD5 md5 = new MD5CryptoServiceProvider();

            string t2 = BitConverter.ToString(md5.ComputeHash(UTF8Encoding.Default.GetBytes(str)), 4, 8);
            t2 = t2.Replace("-", "");
            return t2;
        }

        /// <summary>
        /// MD5 32位加密
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        static string MD5_Ecnryp06_big(string str)
        {
            string cl = str;
            string pwd = "";
            MD5 md5 = MD5.Create();//實例化一個md5對像
            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] output = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));
            // 通過使用循環，將字節類型的數組轉換為字符串，此字符串是常規字符格式化所得
            for (int i = 0; i < output.Length; i++)
            {
                pwd = pwd + output[i].ToString("X2");
            }
            return pwd;
        }

        /// <summary>
        /// MD5 16位加密
        /// </summary>
        /// <param name="ConvertString"></param>
        /// <returns></returns>
        public static string MD5_Ecnryp06_small(string ConvertString)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            string t2 = BitConverter.ToString(md5.ComputeHash(UTF8Encoding.Default.GetBytes(ConvertString)), 4, 8);
            t2 = t2.Replace("-", "");
            //t2 = t2.ToLower();  //轉為小寫
            return t2;
        }

        public string MD5_Ecnryp07(string str)
        {
            MD5 md5 = MD5.Create();//MD5抽象類無法實例化 實例化該方法
            byte[] input = Encoding.Default.GetBytes(str); //將字符串轉換為字節數組
            byte[] output = md5.ComputeHash(input); //調用ComputeHash方法把數組傳進去
            //將字節數組中每個元素ToString();
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                result.Append(output[i].ToString("X2"));
            }
            return result.ToString();
        }

        public static string MD5_Ecnryp08(string str)
        {
            //建立MD5物件
            MD5 md5 = MD5.Create();
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
            string strNew = "";
            for (int i = 0; i < output.Length; i++)
            {
                strNew += output[i].ToString("X2");
            }
            return strNew;
        }

        public string MD5_Ecnryp09(string str)
        {
            MD5 md5 = MD5.Create();
            byte[] input = Encoding.UTF8.GetBytes(str);
            byte[] output = md5.ComputeHash(input);

            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                sb.Append(output[i].ToString("X2"));
            }
            return sb.ToString();
        }

        public string MD5_Ecnryp10(string str)
        {
            //MD5 Encode但不轉Base64 String
            //        MSSQL 使用
            //        select SUBSTRING(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','加密字串')),3,32)
            //        可得同樣結果

            // step 1, calculate MD5 hash from input
            MD5 md5 = MD5.Create();
            byte[] input = Encoding.ASCII.GetBytes(str);
            //byte[] input = Encoding.Unicode.GetBytes(str);
            byte[] output = md5.ComputeHash(input);

            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                sb.Append(output[i].ToString("X2"));
            }
            return sb.ToString();
        }

        public static string MD5_Ecnryp11(string str)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            byte[] output = md5.ComputeHash(Encoding.ASCII.GetBytes(str));
            //byte[] output = md5.ComputeHash(str);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < output.Length; i++)
            {
                sb.AppendFormat("{0:x2}", output[i]);
            }
            return sb.ToString();
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="text">原文</param>
        public static string MD5_Ecnryp12(string str)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();

            byte[] output = md5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(str));
            StringBuilder sb = new StringBuilder();
            foreach (byte b in output)
            {
                sb.Append(b.ToString("X2"));
            }
            return sb.ToString();
        }

        public static string MD5_Ecnryp13(string str)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] input = Encoding.Unicode.GetBytes(str);
            byte[] output = md5.ComputeHash(input);
            string byte2String = null;

            for (int i = 0; i < output.Length; i++)
            {
                byte2String += output[i].ToString("X");
            }

            return byte2String;
        }

        ///   <summary>
        ///   給一個字符串進行MD5加密
        ///   </summary>
        ///   <param   name="strText">待加密字符串</param>
        ///   <returns>加密後的字符串</returns>
        public static string MD5_Ecnryp14(string str)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] output = md5.ComputeHash(Encoding.Default.GetBytes(str));
            return Encoding.Default.GetString(output);
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
        public string MD5_Ecnryp15(string strText)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] result = md5.ComputeHash(GetKeyByteArray(getstrIN(strText)));
            //byte[] output = md5.ComputeHash(input);
            return GetStringValue(result);
            /* fail
            byte[] result = md5.ComputeHash(Encoding.Default.GetBytes(strText));
            return Encoding.Default.GetString(result);
            */
        }

        public string MD5_Ecnryp16(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //創建MD5對象
            byte[] data = Encoding.Default.GetBytes(strPwd);//將字串編碼為一個Byte序列
            byte[] md5data = md5.ComputeHash(data);//計算data Byte array的Hash值
            md5.Clear();    //清空MD5對象
            string str = "";//定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5data.Length - 1; i++)//遍歷Byte數組
            {
                str += md5data[i].ToString("X").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }
            return str;//返回得到的加密字串
        }

        static string MD5_Ecnryp17(string input)
        {
            MD5 md5Hash = MD5.Create();
            // Convert the input string to a byte array and compute the hash.
            byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));
            //byte[] output = md5.ComputeHash(input);

            // Create a new Stringbuilder to collect the bytes
            // and create a string.
            StringBuilder sBuilder = new StringBuilder();

            // Loop through each byte of the hashed data 
            // and format each one as a hexadecimal string.
            for (int i = 0; i < data.Length; i++)
            {
                sBuilder.Append(data[i].ToString("X2"));
            }

            // Return the hexadecimal string.
            return sBuilder.ToString();
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
            var sb = new StringBuilder();

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
            string strResult = "";
            MD5 md5 = System.Security.Cryptography.MD5.Create();    //此行不能簡略
            byte[] bData = md5.ComputeHash(Encoding.Unicode.GetBytes(str));
            //byte[] output = md5.ComputeHash(input);
            for (int i = 0; i < bData.Length; i++)
            {
                strResult = strResult + bData[i].ToString("X");
            }
            return strResult;
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
                sb.Append(b.ToString("x2"));
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
    if (string.IsNullOrEmpty(targetValue))
    {
        return string.Empty;
    }

    var returnValue = new StringBuilder();
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
        returnValue.AppendFormat("{0:X2}", b);
    }
    return returnValue.ToString();
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
    if (string.IsNullOrEmpty(targetValue))
    {
        return string.Empty;
    }
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
             MD5 md5serv = MD5CryptoServiceProvider.Create();
             byte[] buffer = md5serv.ComputeHash(stream);
             StringBuilder sb = new StringBuilder();
             foreach (byte var in buffer)
                 sb.Append(var.ToString("x2"));
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
             string result = BitConverter.ToString(md5.ComputeHash(encode.GetBytes(input)), 4, 8);
             result = result.Replace("-", "");
             return result;
         }
         #endregion
         
         

//--------------------------------------------------------------------------------------------------------------------------


//C#最簡單的文本加密，

private char[] TextEncrypt(string content, string secretKey)
{
    char[] data = content.ToCharArray();
    char[] key = secretKey.ToCharArray();

    for (int i = 0; i < data.Length; i++)
    {
        data[i] ^= key[i % key.Length];
    }

    return data;
}

private string TextDecrypt(char[] data, string secretKey)
{
    char[] key = secretKey.ToCharArray();

    for (int i = 0; i < data.Length; i++)
    {
        data[i] ^= key[i % key.Length];
    }

    return new string(data);
}

//上面是最簡單的加密和解密文本的函數，不需要任何庫文件支持，只是把原文和密鑰進行字節的異或，想要把密文翻譯回來，很簡單，拿著密文和密鑰重新異或一次就可以。
//如果密鑰正確的話，就會回來正確的原始文本，如果密鑰錯誤的話，翻譯回來的就會是一堆的亂碼。
//所以也起到了最簡單的加密功能。


*/