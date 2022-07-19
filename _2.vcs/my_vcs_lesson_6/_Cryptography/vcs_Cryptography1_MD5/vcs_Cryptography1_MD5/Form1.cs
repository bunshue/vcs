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
        //欲進行md5加密的字符串  
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

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            /*
            MD5簡介： 
            MD5的全稱是Message-Digest Algorithm 5，在90年代初由MIT的計算機科學實驗室和RSA Data Security Inc發明，
            經MD2、MD3和MD4發展而來。MD5將任意長度的“字節串”變換成一個128bit的大整數，並且它是一個不可逆的字符串變換算法。
            換句話說就是，即使你看到源程序和算法描述，也無法將一個MD5的值變換回原始的字符串，
            從數學原理上說，是因為原始的字符串有無窮多個，這有點象不存在反函數的數學函數。
            */

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
            string str2 = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str_clear_text, "MD5");
            richTextBox1.Text += "MD5加密的密碼：" + str2 + "\tMD5加密長度是：" + str2.Length + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //MD5
            string result = EncryptCode(str_clear_text);
            richTextBox1.Text += "MD5加密的密碼：" + result + "\tMD5加密長度是：" + result.Length + "\n";
        }

        public static string EncryptCode(string password)
        {
            //這裡Hash算法用MD5算法為例，MD5加密是不可逆的，所以只有加密沒有解密。
            //明文密碼由字符串轉換為byte數組
            byte[] clearBytes = new UnicodeEncoding().GetBytes(password);
            //由明文的byte數組計算出MD5密文byte數組
            byte[] hashedBytes = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(clearBytes);

            //把byte數組轉換為字符串後返回，BitConverter用於將基礎數據類型與字節數組相互轉換
            return BitConverter.ToString(hashedBytes);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //使用Md5Sum算出32位的校驗碼字符串

            string key = "123";
            string result = Md5Sum(str_clear_text + key);  // 返回

            richTextBox1.Text += "MD5加密的密碼：" + result + "\tMD5加密長度是：" + result.Length + "\n";
        }

        //C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串
        public static string Md5Sum(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            MD5 md5 = MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //MD5驗證 32 位元

            string key = "123";
            string result = Md5Sum2(str_clear_text + key);  // 返回
            richTextBox1.Text += result + "\n";
            richTextBox1.Text += "MD5加密的密碼：" + result + "\tMD5加密長度是：" + result.Length + "\n";
        }

        public static string Md5Sum2(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            MD5 md5 = MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="text">原文</param>
        public static string Encrypt3(string text)
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

        private void button4_Click(object sender, EventArgs e)
        {
            //MD5加密

            string input = "lion";
            string output = Encrypt3(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = Encrypt3(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //MD5
            byte[] tmpByte;
            MD5 md5 = new MD5CryptoServiceProvider();
            tmpByte = md5.ComputeHash(GetKeyByteArray(str_clear_text));
            md5.Clear();
            string md5_result = GetStringValue(tmpByte);

            richTextBox1.Text += "MD5 = " + md5_result + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //MD5

            richTextBox1.Text += "明碼：" + str_clear_text + "\n";

            richTextBox1.Text += "Md5：" + str_clear_text.Md5() + "\n";
            richTextBox1.Text += "長度：" + str_clear_text.Md5().Length + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //MD5   32位
            //MD5 校驗默認為32位的字符串， 而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，

            string key = "123";
            string result = Md5Sum3(str_clear_text + key);  // 返回
            richTextBox1.Text += "MD5加密的密碼：" + result + "\tMD5加密長度是：" + result.Length + "\n";
        }

        public static string Md5Sum3(string strToEncrypt)
        {
            // 將需要加密的字符串轉為byte數組
            byte[] bs = UTF8Encoding.UTF8.GetBytes(strToEncrypt);

            // 創建md5 對象
            MD5 md5;
            md5 = MD5CryptoServiceProvider.Create();

            // 生成16位的二進制校驗碼
            byte[] hashBytes = md5.ComputeHash(bs);

            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < hashBytes.Length; i++)
            {
                hashString += Convert.ToString(hashBytes[i], 16).PadLeft(2, '0');
            }

            return hashString.PadLeft(32, '0');
        }

        public string getMd5(string str)
        {
            MD5 md5 = MD5.Create();//MD5抽象類無法實例化 實例化該方法
            byte[] buffer = Encoding.Default.GetBytes(str); //將字符串轉換為字節數組
            byte[] mdbuffer = md5.ComputeHash(buffer); //調用ComputeHash方法把數組傳進去
            //將字節數組中每個元素ToString();
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < mdbuffer.Length; i++)
            {
                result.Append(mdbuffer[i].ToString("x2")); //ToString得到十進制字符串 ToString("x")十六進制字符串 ToString("x2")對齊
            }
            return result.ToString();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //MD5加密

            string result = getMd5(str_clear_text);
            richTextBox1.Text += "MD5加密的密碼：" + result + "\tMD5加密長度是：" + result.Length + "\n";
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
        public string MD5Encrypt(string strText)
        {
            richTextBox1.Text += "1111111\n";
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] result = md5.ComputeHash(GetKeyByteArray(getstrIN(strText)));
            return GetStringValue(result);
            /* fail
            byte[] result = md5.ComputeHash(Encoding.Default.GetBytes(strText));
            return Encoding.Default.GetString(result);
            */
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //將字串用MD5加密
            string s1 = MD5Encrypt(str_clear_text);
            richTextBox1.Text += "s1 = " + s1 + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string str_md5_32 = GetBigMd5(str_clear_text);
            string str_md5_16 = GetSmallMd5(str_clear_text);

            richTextBox1.Text += "32位MD5 : " + str_md5_32 + "\n";
            richTextBox1.Text += "16位MD5 : " + str_md5_16 + "\n";
        }

        /// <summary>
        /// 32位md5
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public static string GetBigMd5(string str)
        {
            string cl = str;
            string pwd = "";
            var md5 = MD5.Create();

            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));

            for (int i = 0; i < s.Length; i++)
            {
                pwd = pwd + s[i].ToString("X2");
            }

            return pwd;
        }

        /// <summary>
        /// 16位MD5
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public static string GetSmallMd5(string str)
        {
            var md5 = new MD5CryptoServiceProvider();
            string t2 = BitConverter.ToString(md5.ComputeHash(UTF8Encoding.Default.GetBytes(str)), 4, 8);
            t2 = t2.Replace("-", "");
            return t2;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //MD5加密 a
            string result = getMd5a(str_clear_text);
            richTextBox1.Text += result + "\n";
        }

        public string getMd5a(string str)
        {
            MD5 md5 = MD5.Create();//MD5抽象类无法实例化 实例化该方法
            byte[] buffer = Encoding.Default.GetBytes(str); //将字符串转换为字节数组
            byte[] mdbuffer = md5.ComputeHash(buffer); //调用ComputeHash方法把数组传进去
            //将字节数组中每个元素ToString();
            StringBuilder result = new StringBuilder();
            for (int i = 0; i < mdbuffer.Length; i++)
            {
                result.Append(mdbuffer[i].ToString("x2")); //ToString得到十进制字符串 ToString("x")十六进制字符串 ToString("x2")对齐
            }
            return result.ToString();
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //MD5加密 b
            //MD5加密
            //MD5加密是不可以逆的，只能將字串轉為MD5值，不能將MD5值轉回字串。

            //202cb962ac59075b964b07152d234b70
            //202cb962ac5975b964b7152d234b70   ToString x引數
            //202cb962ac59075b964b07152d234b70  ToString x2引數

            // 3244185981728979115075721453575112   ToString  沒加引數
            //ToString引數需要到百度拿來用
            string s = GetMD5b("123");
            richTextBox1.Text += s + "\n";
        }

        public static string GetMD5b(string str)
        {
            //建立MD5物件
            MD5 md5 = MD5.Create();
            //開始加密
            //需要將字串轉為位元組陣列
            byte[] buffer = Encoding.Default.GetBytes(str);
            //返回一個加密好的位元組陣列
            byte[] MD5Buffer = md5.ComputeHash(buffer);

            //將位元組陣列轉換成字串
            //位元組陣列---字串
            //1.將位元組陣列中每個元素按照自定的編碼格式解析成字串
            //2.直接將陣列ToString();
            //3.將位元組陣列中的每個元素ToString()
            //  return Encoding.Default.GetString(MD5Buffer);
            string strNew = " ";
            for (int i = 0; i < MD5Buffer.Length; i++)
            {
                //ToString("x") 加x引數將十進位制轉為十六進位制，屬於ToString的方法
                strNew += MD5Buffer[i].ToString("x2");
            }
            return strNew;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //MD5加密 c
            //MD5加密
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] result1 = Encoding.Default.GetBytes(str_clear_text);
            byte[] result2 = md5.ComputeHash(result1);

            string result3 = BitConverter.ToString(result2).Replace("-", "");
            richTextBox1.Text += "MD5加密結果 : " + result3 + "\n";

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //MD5加密 d
            //MD5加密
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] result1 = Encoding.Default.GetBytes(str_clear_text);
            byte[] result2 = md5.ComputeHash(result1);

            string result3 = Encoding.Default.GetString(result2);
            richTextBox1.Text += "XXXX MD5加密結果 : " + result3 + "\n";

        }

        private void button15_Click(object sender, EventArgs e)
        {
            //MD5加密 e
            //MD5加密
            string result = My_MD5.EncryptCode(str_clear_text);
            richTextBox1.Text += result + "\n";

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //MD5加密 f
            //MD5加密
            string result = Safety.MD5(str_clear_text);
            richTextBox1.Text += result + "\n";

        }

        //C#實現MD5加密
        /*
        MD5的全稱是message-digest algorithm 5(信息-摘要算法，在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest開發出來， 經md2、md3和md4發展而來。
        MD5具有很好的安全性(因為它具有不可逆的特征,加過密的密文經過解密後和加密前的東東相同的可能性極小)
        */
        //MD5 g ST
        private void button17_Click(object sender, EventArgs e)
        {
            //MD5加密 g


            byte[] result = Encoding.Default.GetBytes(str_clear_text);
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] output = md5.ComputeHash(result);

            richTextBox1.Text += BitConverter.ToString(output).Replace("-", "") + "\n";

        }
        //MD5 g SP

        ////MD5 b ST
        public static string GetMD5(string myString)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] fromData = Encoding.Unicode.GetBytes(myString);
            byte[] targetData = md5.ComputeHash(fromData);
            string byte2String = null;

            for (int i = 0; i < targetData.Length; i++)
            {
                byte2String += targetData[i].ToString("x");
            }

            return byte2String;
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //MD5加密 h
            string result = GetMD5(str_clear_text);

            richTextBox1.Text += result + "\n";
        }
        //MD5 h SP

        //MD5 i ST
        ///   <summary>
        ///   給一個字符串進行MD5加密
        ///   </summary>
        ///   <param   name="strText">待加密字符串</param>
        ///   <returns>加密後的字符串</returns>
        public static string MD5Encrypt2(string strText)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] result = md5.ComputeHash(Encoding.Default.GetBytes(strText));
            return Encoding.Default.GetString(result);
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //MD5加密 i
            string result = MD5Encrypt2(str_clear_text);  //cf string result = MD5Encrypt(str_clear_text);

            richTextBox1.Text += result + "\n";

        }
        //MD5 i SP

        //MD5加密 j ST

        /// <summary>
        /// MD5 16位加密 加密後密碼為大寫
        /// </summary>
        /// <param name="ConvertString"></param>
        /// <returns></returns>
        public static string GetMd5StrA(string ConvertString)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            string t2 = BitConverter.ToString(md5.ComputeHash(UTF8Encoding.Default.GetBytes(ConvertString)), 4, 8);
            t2 = t2.Replace("-", "");
            return t2;
        }

        /// <summary>
        /// MD5 16位加密 加密後密碼為小寫
        /// </summary>
        /// <param name="ConvertString"></param>
        /// <returns></returns>
        public static string GetMd5StrB(string ConvertString)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            string t2 = BitConverter.ToString(md5.ComputeHash(UTF8Encoding.Default.GetBytes(ConvertString)), 4, 8);
            t2 = t2.Replace("-", "");

            t2 = t2.ToLower();

            return t2;
        }

        /// <summary>
        /// MD5 32位加密
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        static string UserMd5(string str)
        {
            string cl = str;
            string pwd = "";
            MD5 md5 = MD5.Create();//實例化一個md5對像
            // 加密後是一個字節類型的數組，這裡要注意編碼UTF8/Unicode等的選擇　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));
            // 通過使用循環，將字節類型的數組轉換為字符串，此字符串是常規字符格式化所得
            for (int i = 0; i < s.Length; i++)
            {
                // 將得到的字符串使用十六進制類型格式。格式後的字符是小寫的字母，如果使用大寫（X）則格式後的字符是大寫字符

                pwd = pwd + s[i].ToString("X2");
            }
            return pwd;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //MD5加密 j

            string result1 = GetMd5StrA(str_clear_text);
            richTextBox1.Text += "MD5 16位加密 加密後密碼為大寫 : \t" + result1 + "\n";

            string result2 = GetMd5StrB(str_clear_text);
            richTextBox1.Text += "MD5 16位加密 加密後密碼為小寫 : \t" + result2 + "\n";

            string result3 = UserMd5(str_clear_text);
            richTextBox1.Text += "MD5 32位加密 : \t" + result3 + "\n";

            string input = "lion";
            string output = UserMd5(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }
        //MD5加密 j SP

        //MD5加密 k ST
        public static string StringToMD5Hash(string inputString)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            byte[] encryptedBytes = md5.ComputeHash(Encoding.ASCII.GetBytes(inputString));
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < encryptedBytes.Length; i++)
            {
                sb.AppendFormat("{0:x2}", encryptedBytes[i]);
            }
            return sb.ToString();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //MD5加密 k

            string result = StringToMD5Hash(str_clear_text);
            richTextBox1.Text += result + "\n";

        }
        //MD5加密 k SP

        //MD5加密 l ST
        private void button22_Click(object sender, EventArgs e)
        {
            //MD5加密 l
            /*
            //獲取要加密的字段，並轉化為Byte[]數組
            byte[] data = Encoding.Unicode.GetBytes(str.ToCharArray());
            //建立加密服務
            MD5 md5 = new MD5CryptoServiceProvider();
            //加密Byte[]數組
            byte[] result = md5.ComputeHash(data);
            */
        }
        //MD5加密 l SP

        private void button23_Click(object sender, EventArgs e)
        {
            //MD5加密 m
            //string InputValue = "這是要轉MD5的文字";
            string InputValue = "Hello World!";
            string OutputValue = string.Empty;

            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得MD5演算後的陣列
            byte[] hash = algorithm.ComputeHash(Encoding.UTF8.GetBytes(InputValue));
            //依序轉存到OutputValue
            foreach (byte b in hash)
            {
                OutputValue += b.ToString("X2");
            }
            richTextBox1.Text += "字串：" + InputValue + ",\tMD5：" + OutputValue + "\n";

        }


        //結果：// The MD5 hash of Hello World! is: ed076287532e86365e841e92bfc50d8c.
        static string GetMd5Hash(MD5 md5Hash, string input)
        {

            // Convert the input string to a byte array and compute the hash.
            byte[] data = md5Hash.ComputeHash(Encoding.UTF8.GetBytes(input));

            // Create a new Stringbuilder to collect the bytes
            // and create a string.
            StringBuilder sBuilder = new StringBuilder();

            // Loop through each byte of the hashed data 
            // and format each one as a hexadecimal string.
            for (int i = 0; i < data.Length; i++)
            {
                sBuilder.Append(data[i].ToString("x2"));
            }

            // Return the hexadecimal string.
            return sBuilder.ToString();
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //MD5加密 n

            string source = "Hello World!"; //保留, 有答案
            using (MD5 md5Hash = MD5.Create())
            {
                string hash = GetMd5Hash(md5Hash, source);
                richTextBox1.Text += "The MD5 hash of " + source + " is: " + hash + ".\n";
            }
        }

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //創建MD5對象
            byte[] data = Encoding.Default.GetBytes(strPwd);//將字串編碼為一個Byte序列
            byte[] md5data = md5.ComputeHash(data);//計算dataByte的Hash值
            md5.Clear();    //清空MD5對象
            string str = "";//定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5data.Length - 1; i++)//遍歷byte數組
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }
            return str;//返回得到的加密字串
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //MD5加密 o

            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "使用MD5加密後的結果為：" + Encrypt(P_str_Code) + "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //MD5加密 p

            string old_string = "abcdefg";
            string new_string = string.Empty;

            MD5CryptoServiceProvider M5 = new MD5CryptoServiceProvider();
            new_string = ASCIIEncoding.ASCII.GetString(M5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(old_string)));

            richTextBox1.Text += "原字串:\t" + old_string + "\n";
            richTextBox1.Text += "MD5加密後的字串:\t" + new_string + "\n";
        }

        //MD5加密 q ST
        public string Encrypt2(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();//创建MD5对象
            byte[] data = Encoding.Default.GetBytes(strPwd);//将字符编码为一个字节序列
            byte[] md5data = md5.ComputeHash(data);//计算data字节数组的哈希值
            md5.Clear();//清空MD5对象
            string str = "";//定义一个变量，用来记录加密后的密码
            for (int i = 0; i < md5data.Length - 1; i++)//遍历字节数组
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//对遍历到的字节进行加密
            }
            return str;//返回得到的加密字符串
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //MD5加密 q
            /*
            //將字串用MD5加密
            Console.Write("請輸入密碼 : ");
            string P_str_Code = Console.ReadLine();//记录要加密的密码
            Program program = new Program();//创建Program对象
            Console.WriteLine("結果:\n" + program.Encrypt2(P_str_Code));//输出加密后的字符串
            */
            string input = "lion";
            string output = Encrypt2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = Encrypt2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }
        //MD5加密 q SP


        //MD5加密 r ST
        public string CalculateMD5Hash(string input)
        {
            //MD5 Encode但不轉Base64 String
            //        MSSQL 使用
            //        select SUBSTRING(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','加密字串')),3,32)
            //        可得同樣結果

            // step 1, calculate MD5 hash from input
            MD5 md5 = MD5.Create();
            byte[] inputBytes = Encoding.ASCII.GetBytes(input);
            //byte[] inputBytes = Encoding.Unicode.GetBytes(input);
            byte[] hash = md5.ComputeHash(inputBytes);

            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hash.Length; i++)
            {
                sb.Append(hash[i].ToString("X2"));
            }
            return sb.ToString();
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //MD5加密 r
            string input = "lion";
            string output = CalculateMD5Hash(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = CalculateMD5Hash(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }
        //MD5加密 r SP

        //MD5加密 s ST
        public string CalculateMD5Hash2(string input)
        {
            MD5 md5 = MD5.Create();
            byte[] inputBytes = Encoding.UTF8.GetBytes(input);
            byte[] hash = md5.ComputeHash(inputBytes);
            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hash.Length; i++)
            {
                sb.Append(hash[i].ToString("X2"));
            }
            return sb.ToString();
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //MD5加密 s
            string input = "lion";
            string output = CalculateMD5Hash2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = CalculateMD5Hash2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }
        //MD5加密 s SP

        private void button30_Click(object sender, EventArgs e)
        {

        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {

        }

        private void button34_Click(object sender, EventArgs e)
        {

        }

        private void button35_Click(object sender, EventArgs e)
        {

        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        private void button37_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
        {

        }
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
            for (int i = 0; i < bData.Length; i++)
            {
                strResult = strResult + bData[i].ToString("X");
            }
            return strResult;
        }
    }
}
