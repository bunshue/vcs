using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography;

//C# MD5摘要算法、哈希算法，
//MD5即Message-Digest Algorithm 5（信息-摘要算法5），用於確保信息傳輸完整一致。是計算機廣泛使用的雜湊算法之一（又譯摘要算法、哈希算法）

//C#計算文件的MD5值實例
//MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，廣泛用於加密、解密、數據簽名和數據完整性校驗等方面。

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

        private void button2_Click(object sender, EventArgs e)
        {
            string input = "lion";
            string output = CalculateMD5Hash(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = CalculateMD5Hash(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }

        public string CalculateMD5Hash(string input)
        {
            //MD5 Encode但不轉Base64 String
            //        MSSQL 使用
            //        select SUBSTRING(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','加密字串')),3,32)
            //        可得同樣結果

            // step 1, calculate MD5 hash from input
            MD5 md5 = System.Security.Cryptography.MD5.Create();
            byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);
            //byte[] inputBytes = System.Text.Encoding.Unicode.GetBytes(input);
            byte[] hash = md5.ComputeHash(inputBytes);

            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hash.Length; i++)
            {
                sb.Append(hash[i].ToString("X2"));
            }
            return sb.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string input = "lion";
            string output = CalculateMD5Hash2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = CalculateMD5Hash2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }

        public string CalculateMD5Hash2(string input)
        {
            MD5 md5 = System.Security.Cryptography.MD5.Create();
            byte[] inputBytes = System.Text.Encoding.UTF8.GetBytes(input);
            byte[] hash = md5.ComputeHash(inputBytes);
            // step 2, convert byte array to hex string
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hash.Length; i++)
            {
                sb.Append(hash[i].ToString("X2"));
            }
            return sb.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //C#計算文件的MD5值實例
            string filename = @"C:\______test_files\picture1.jpg";

            //01.計算文件的 MD5 值
            Console.WriteLine(string.Format("計算文件的 MD5 值：{0}", HashHelper.MD5File(filename)));
            richTextBox1.Text += "計算文件的 MD5 值：" + HashHelper.MD5File(filename) + "\n";

            //02.計算文件的 sha1 值
            Console.WriteLine(string.Format("計算文件的 sha1 值：{0}", HashHelper.SHA1File(filename)));
            richTextBox1.Text += "計算文件的 sha1 值：" + HashHelper.SHA1File(filename) + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string input = "lion";
            string output = Encrypt2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";

            input = "mouse";
            output = Encrypt2(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }

        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="text">原文</param>
        public static string Encrypt2(string text)
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

        private void button6_Click(object sender, EventArgs e)
        {
            string data = "hello world";
            string key = "123";
            string result = Md5Sum(data + key);
            richTextBox1.Text += result + "\n";
        }

        //C# MD5驗證
        //C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，代碼如下：
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

        private void button7_Click(object sender, EventArgs e)
        {
            string input = "lion";
            string output = UserMd5(input);
            richTextBox1.Text += "輸入:\n" + input + "\n";
            richTextBox1.Text += "輸出:\n" + output + "\n";
        }


        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="str"></param>
        /// <returns></returns>
        public string UserMd5(string str)
        {
            string cl = str;
            string pwd = "";
            MD5 md5 = MD5.Create();//实例化一个md5对像
            // 加密后是一个字节类型的数组，这里要注意编码UTF8/Unicode等的选择　
            byte[] s = md5.ComputeHash(Encoding.UTF8.GetBytes(cl));

            // 通过使用循环，将字节类型的数组转换为字符串，此字符串是常规字符格式化所得
            for (int i = 0; i < s.Length; i++)
            {
                // 将得到的字符串使用十六进制类型格式。格式后的字符是小写的字母，如果使用大写（X）则格式后的字符是大写字符

                pwd = pwd + s[i].ToString("x");
                pwd = pwd + s[i].ToString("x2");
            }
            return pwd;
        }
    }

    //C#計算文件的MD5值實例
    /*
在C#中，數據的Hash以MD5或SHA1的方式實現，MD5與SHA1都是Hash算法，MD5輸出是128位的，SHA1輸出是160位的，MD5比SHA1快，SHA1比MD5強度高。
1.1 SHA-1和MD5的比較

因為二者均由MD4導出，SHA-1和MD5彼此很相似。相應的，他們的強度和其他特性也是相似，但還有以下幾點不同：

    對強行攻擊的安全性：最顯著和最重要的區別是SHA-1摘要比MD5摘要長32 位。使用強行技術，產生任何一個報文使其摘要等於給定報摘要的難度對MD5是2128數量級的操作，而對SHA-1則是2160數量級的操作。這樣，SHA-1對強行攻擊有更大的強度。
    對密碼分析的安全性：由於MD5的設計，易受密碼分析的攻擊，SHA-1顯得不易受這樣的攻擊。
    速度：在相同的硬件上，SHA-1的運行速度比MD5慢。

1.2 SHA-1和MD5在C#中的實現
*/

    /*
    MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，廣泛用於加密、解密、數據簽名和數據完整性校驗等方面。任何一個文件，無論是可執行程序、圖像文件、臨時文件或者其他任何類型的文件，也不管它體積多大，都可以計算出一個MD5值，如果文件被修改過，就算只改動了一個字節，其 MD5 值也會變得完全不同。因此，我們可以通過對比同一文件的 MD5 值，來校驗這個文件是否被“篡改”過。C# 可以方便的計算出文件的 MD5 值：
    \\計算文件的MD5值
    */

    /// <summary>
    /// Hash輔助類
    /// </summary>
    public class HashHelper
    {
        /// <summary>
        /// 計算文件的 MD5 值
        /// </summary>
        /// <param name="fileName">要計算 MD5 值的文件名和路徑</param>
        /// <returns>MD5 值16進制字符串</returns>
        public static string MD5File(string fileName)
        {
            return HashFile(fileName, "md5");
        }

        /// <summary>
        /// 計算文件的 sha1 值
        /// </summary>
        /// <param name="fileName">要計算 sha1 值的文件名和路徑</param>
        /// <returns>sha1 值16進制字符串</returns>
        public static string SHA1File(string fileName)
        {
            return HashFile(fileName, "sha1");
        }

        /// <summary>
        /// 計算文件的哈希值
        /// </summary>
        /// <param name="fileName">要計算哈希值的文件名和路徑</param>
        /// <param name="algName">算法:sha1,md5</param>
        /// <returns>哈希值16進制字符串</returns>
        private static string HashFile(string fileName, string algName)
        {
            if (!System.IO.File.Exists(fileName))
            {
                return string.Empty;
            }

            System.IO.FileStream fs = new System.IO.FileStream(fileName, System.IO.FileMode.Open, System.IO.FileAccess.Read);
            byte[] hashBytes = HashData(fs, algName);
            fs.Close();
            return ByteArrayToHexString(hashBytes);
        }

        /// <summary>
        /// 計算哈希值
        /// </summary>
        /// <param name="stream">要計算哈希值的 Stream</param>
        /// <param name="algName">算法:sha1,md5</param>
        /// <returns>哈希值字節數組</returns>
        private static byte[] HashData(System.IO.Stream stream, string algName)
        {
            System.Security.Cryptography.HashAlgorithm algorithm;
            if (algName == null)
            {
                throw new ArgumentNullException("algName 不能為 null");
            }

            if (string.Compare(algName, "sha1", true) == 0)
            {
                algorithm = System.Security.Cryptography.SHA1.Create();
            }
            else
            {
                if (string.Compare(algName, "md5", true) != 0)
                {
                    throw new Exception("algName 只能使用 sha1 或 md5");
                }
                algorithm = System.Security.Cryptography.MD5.Create();
            }

            return algorithm.ComputeHash(stream);
        }

        /// <summary>
        /// 字節數組轉換為16進制表示的字符串
        /// </summary>
        private static string ByteArrayToHexString(byte[] buf)
        {
            return BitConverter.ToString(buf).Replace("-", "");
        }
    }



}

