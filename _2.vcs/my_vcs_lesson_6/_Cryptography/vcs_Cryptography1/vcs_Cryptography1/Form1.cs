using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography;  // for CryptoConfig, MD5, SHA

/*
雜湊值（Hash, Hash Value）
Hash Function（雜湊函式）

Hash Function/Hash Algorithm：

MD5      128位元，快速但不安全
SHA-1    160位元，已被破解
SHA-256  256位元，目前安全
SHA-512  512位元，高度安全
SHA3-256 新一代SHA算法
BLAKE2b  高效能現代算法

MD5（Message Digest Algorithm 5）  雜湊值（Hash Value）	128 位元（16 拜, 32字符）
SHA-256（Secure Hash Algorithm 256-bit）
*/

namespace vcs_Cryptography1
{
    public partial class Form1 : Form
    {
        //欲進行加密的字串資料
        string str_clear_text = "MD5 產生 128 位元摘要，以 32 個十六進位字元表示。";

        //加密後的結果
        string str_encrypted_text = string.Empty;

        //準備計算雜湊值的檔案
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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

            richTextBox1.Size = new Size(1140, 690);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 750);
            this.Text = "vcs_Cryptography1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        //拜列轉字串
        public static string BytesToString(byte[] bytes)
        {
            string result = "";
            foreach (byte b in bytes)
            {
                result += b.ToString("X2");  // 轉2位的16進制字串
            }
            return result;
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //MD5(用自建函數)
            //MD5 產生 128 位元摘要，以 32 個十六進位字元表示。

            str_encrypted_text = MD5_Ecnrypt03(str_clear_text);
            richTextBox1.Text += "03m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt15(str_clear_text);
            richTextBox1.Text += "15m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt22(str_clear_text);
            richTextBox1.Text += "22m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt20(str_clear_text);
            richTextBox1.Text += "20m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt04(str_clear_text);
            richTextBox1.Text += "04m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt08(str_clear_text);
            richTextBox1.Text += "08m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt25(str_clear_text);
            richTextBox1.Text += "25m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt14(str_clear_text);
            richTextBox1.Text += "14m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            str_encrypted_text = MD5_Ecnrypt28(str_clear_text);
            richTextBox1.Text += "28m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜\n";

            //64位的MD5加密
            str_encrypted_text = MD5_Ecnrypt30_Base64(str_clear_text);
            richTextBox1.Text += "30m明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\t長度 : " + str_encrypted_text.Length.ToString() + " 拜, Base64\n";
        }

        //64位的MD5加密
        public static string MD5_Ecnrypt30_Base64(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值

            string md5Result = Convert.ToBase64String(md5Hash);  // Hash轉字串, Base64
            return md5Result;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // 計算一個檔案的MD5值

            MD5 md5 = MD5.Create();  // 創建MD5對象

            //取得第一個檔案MD5演算後的陣列
            byte[] input1 = File.ReadAllBytes(filename);
            byte[] md5Hash1 = md5.ComputeHash(input1);  // 算拜列之Hash值

            //計算檔案的MD5碼
            string FileMD5_1 = BytesToString(md5Hash1);  // Hash轉字串
            richTextBox1.Text += "01mf檔案 : " + filename + "\tMD5 : " + FileMD5_1 + "\n";

            //------------------------------------------------------------  # 60個

            //未使用函數 MD5

            FileStream fs = new FileStream(filename, FileMode.Open);

            //byte[] md5Hash = md5.ComputeHash(fs);  // 算拜列之Hash值

            string ccc = MD5Encrypt(fs);
            richTextBox1.Text += "02mf檔案 : " + filename + "\tMD5 : " + ccc + "\n";

            fs.Close();

            //------------------------------------------------------------  # 60個

            //FileStream
            fs = new FileStream(filename, FileMode.Open);
            byte[] md5Hash = md5.ComputeHash(fs);  // 算拜列之Hash值
            fs.Close();

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
            }
            str_encrypted_text = sb.ToString();

            richTextBox1.Text += "03mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            str_encrypted_text = BytesToString(GetHashMD5(filename));
            richTextBox1.Text += "04mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            //取得第一個檔案MD5演算後的陣列
            byte[] input = File.ReadAllBytes(filename);
            //byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值
            md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值

            //建立第一個檔案的MD5碼
            str_encrypted_text = BytesToString(md5Hash);  // Hash轉字串

            richTextBox1.Text += "05mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            //FileStream
            fs = new FileStream(filename, FileMode.Open, FileAccess.Read, FileShare.Read);
            //byte[]
            md5Hash = md5.ComputeHash(fs);  // 算拜列之Hash值
            fs.Close();
            //StringBuilder
            sb = new StringBuilder(32);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
            }
            str_encrypted_text = sb.ToString();

            richTextBox1.Text += "06mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            //ValidHelper

            str_encrypted_text = ValidHelper.GetFileMD5(filename);
            richTextBox1.Text += "07mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            //測試 HashHelper

            str_encrypted_text = HashHelper.MD5File(filename);
            richTextBox1.Text += "08mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            //檔案轉拜列轉Hash值
            //byte[]
            md5Hash = GetHashMD5(filename);

            //Hash轉字串
            str_encrypted_text = Convert.ToBase64String(md5Hash);  // Hash轉字串, Base64
            richTextBox1.Text += "09mf檔案 : " + filename + "\tMD5 : " + str_encrypted_text + ", Base64\n";
        }

        // Compute the file's hash.
        private byte[] GetHashMD5(string filename)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            FileStream fs = File.OpenRead(filename);
            byte[] md5Hash = md5.ComputeHash(fs);  // 算拜列之Hash值
            fs.Close();

            return md5Hash;
        }

        // MD5對文件流加密
        public static string MD5Encrypt(Stream stream)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象
            byte[] md5Hash = md5.ComputeHash(stream);  // 算拜列之Hash值
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                sb.Append(b.ToString("X2"));  // 轉2位的16進制字串
            }
            return sb.ToString();
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button3_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button4_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //EncryptHelper
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            //各種SHA 1
            //SHA1，SHA256，SHA512

            //此類提供SHA1，SHA256，SHA512等3種算法，加密字串的長度依次增大。

            str_encrypted_text = SHA1Encrypt(str_clear_text);
            richTextBox1.Text += "01s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA1\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //各種加密算法
            byte[] tmpByte;
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            tmpByte = sha1.ComputeHash(GetKeyByteArray(str_clear_text));
            sha1.Clear();
            str_encrypted_text = GetStringValue(tmpByte);

            richTextBox1.Text += "02s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA1\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //------------------------------------------------------------  # 60個

            str_encrypted_text = SHA256Encrypt(str_clear_text);
            richTextBox1.Text += "03s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA256\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //byte[] tmpByte;
            SHA256 sha256 = new SHA256Managed();
            tmpByte = sha256.ComputeHash(GetKeyByteArray(str_clear_text));
            sha256.Clear();
            str_encrypted_text = GetStringValue(tmpByte);

            richTextBox1.Text += "04s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA256\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //------------------------------------------------------------  # 60個

            str_encrypted_text = SHA512Encrypt(str_clear_text);
            richTextBox1.Text += "05s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA512\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //byte[] tmpByte;
            SHA512 sha512 = new SHA512Managed();
            tmpByte = sha512.ComputeHash(GetKeyByteArray(str_clear_text));
            sha512.Clear();
            str_encrypted_text = GetStringValue(tmpByte);
            richTextBox1.Text += "06s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA512\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //------------------------------------------------------------  # 60個

            //SHA1
            str_encrypted_text = SHA1_Ecnrypt05(str_clear_text);
            richTextBox1.Text += "07s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA1\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            str_encrypted_text = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str_clear_text, "SHA1");
            richTextBox1.Text += "08s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA1\t長度 : " + str_encrypted_text.Length + "\n";

            //------------------------------------------------------------  # 60個

            string key = "abc";
            str_encrypted_text = DESEncrypt(str_clear_text, key);
            richTextBox1.Text += "DES Enc = " + str_encrypted_text + "\n";

            string str_encrypted_text_decrypted = DESDecrypt(str_encrypted_text, key, "0");
            richTextBox1.Text += "DES Dec = " + str_encrypted_text_decrypted + "\n";

            //------------------------------------------------------------  # 60個

            //算一個字串的SHA1值

            byte[] data = new byte[5];
            data[0] = (byte)'A';
            data[1] = (byte)'B';
            data[2] = (byte)'C';
            data[3] = (byte)'D';
            data[4] = (byte)'E';

            SHA1 sha = new SHA1CryptoServiceProvider();
            // This is one implementation of the abstract class SHA1.
            byte[] result = sha.ComputeHash(data);
            richTextBox1.Text += "SHA1 :\t";
            foreach (byte b in result)
            {
                richTextBox1.Text += b.ToString("X2");
            }
            richTextBox1.Text += "\n";
        }

        public string SHA1Encrypt(string strIN)
        {
            byte[] tmpByte;
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            tmpByte = sha1.ComputeHash(GetKeyByteArray(strIN));
            sha1.Clear();
            return GetStringValue(tmpByte);
        }

        public string SHA256Encrypt(string strIN)
        {
            byte[] tmpByte;
            SHA256 sha256 = new SHA256Managed();
            tmpByte = sha256.ComputeHash(GetKeyByteArray(strIN));
            sha256.Clear();
            return GetStringValue(tmpByte);
        }

        public string SHA512Encrypt(string strIN)
        {
            byte[] tmpByte;
            SHA512 sha512 = new SHA512Managed();
            tmpByte = sha512.ComputeHash(GetKeyByteArray(strIN));
            sha512.Clear();
            return GetStringValue(tmpByte);
        }

        /// <summary>
        /// 基于Sha1的自定义加密字符串方法 : 输入一个字符串，返回一个由40个字符组成的十六进制的哈希散列（字符串）。
        /// </summary>
        /// <param name="str">要加密的字符串</param>
        /// <returns>加密后的十六进制的哈希散列（字符串）</returns>
        public static string SHA1_Ecnrypt05(string str)
        {
            var buffer = Encoding.UTF8.GetBytes(str);
            var data = SHA1.Create().ComputeHash(buffer);  // 創建SHA1對象

            var sb = new StringBuilder();
            foreach (var t in data)
            {
                sb.Append(t.ToString("X2"));
            }
            return sb.ToString();
        }

        /// <summary>
        /// 使用DES加密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="originalValue">待加密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">初始化向量(最大長度8)</param>
        /// <returns>加密後的字符串</returns>
        public string DESEncrypt(string originalValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateEncryptor();
            byt = Encoding.UTF8.GetBytes(originalValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Convert.ToBase64String(ms.ToArray());  // Hash轉字串, Base64
        }

        public string DESEncrypt(string originalValue, string key)
        {
            return DESEncrypt(originalValue, key, key);
        }

        /// <summary>
        /// 使用DES解密（Added by niehl 2005-4-6）
        /// </summary>
        /// <param name="encryptedValue">待解密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">m初始化向量(最大長度8)</param>
        /// <returns>解密後的字符串</returns>
        public string DESDecrypt(string encryptedValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);
            sa.IV = Encoding.UTF8.GetBytes(IV);
            ct = sa.CreateDecryptor();
            byt = Convert.FromBase64String(encryptedValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Encoding.UTF8.GetString(ms.ToArray());
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            //各種SHA 2
            //各種加密算法
            byte[] input;
            byte[] output;

            SHA1 sha1 = new SHA1CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha1.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);  // Hash轉字串, Base64
            richTextBox1.Text += "09s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA1, Base64\n";


            SHA256 sha256 = new SHA256CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha256.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);  // Hash轉字串, Base64
            richTextBox1.Text += "10s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA256, Base64\n";


            SHA384 sha384 = new SHA384CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha384.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);  // Hash轉字串, Base64
            richTextBox1.Text += "11s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA384, Base64\n";


            SHA512 sha512 = new SHA512CryptoServiceProvider();
            input = Encoding.Default.GetBytes(str_clear_text);
            output = sha512.ComputeHash(input);
            str_encrypted_text = Convert.ToBase64String(output);  // Hash轉字串, Base64
            richTextBox1.Text += "12s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text + "\tSHA512, Base64\n";

            //------------------------------------------------------------  # 60個

            //各種加密算法

            //SHA1
            richTextBox1.Text += "SHA1\t";
            UnicodeEncoding oConvert = new UnicodeEncoding();
            Byte[] bytData = oConvert.GetBytes(str_clear_text);
            SHA1Managed oSha1 = new SHA1Managed();
            Byte[] bytResult = oSha1.ComputeHash(bytData);
            foreach (int oItem in bytResult)
            {
                richTextBox1.Text += oItem.ToString("X2");
            }
            richTextBox1.Text += "\n";


            //SHA512
            richTextBox1.Text += "SHA512\t";
            //SHA512程式碼只有三行就解決了
            SHA512 oSHA = new SHA512Managed();
            byte[] aryByte = oSHA.ComputeHash(Encoding.UTF8.GetBytes(str_clear_text));
            richTextBox1.Text += System.BitConverter.ToString(aryByte).Replace("-", "");
            richTextBox1.Text += "\n";

            //------------------------------------------------------------  # 60個

            //生成SHA1加密字符串，

            var strRes = Encoding.Default.GetBytes(str_clear_text);
            HashAlgorithm iSha = new SHA1CryptoServiceProvider();
            strRes = iSha.ComputeHash(strRes);
            var str_encrypted_text2 = new StringBuilder();
            foreach (byte iByte in strRes)
            {
                str_encrypted_text2.AppendFormat("{0:x2}", iByte);
            }
            richTextBox1.Text += "13s明碼 : " + str_clear_text + "\t密碼 : " + str_encrypted_text2 + "\tSHA1\t長度 : " + str_encrypted_text.Length + " 拜\n";

            //------------------------------------------------------------  # 60個

            //另一種SHA1加密

            string key = "123";
            HMACSHA1 hmacsha1 = new HMACSHA1(Encoding.UTF8.GetBytes(key));
            byte[] rstRes = hmacsha1.ComputeHash(Encoding.UTF8.GetBytes(str_clear_text));
            string strs = Convert.ToBase64String(rstRes);  // Hash轉字串, Base64
            richTextBox1.Text += "14s明碼 : " + str_clear_text + "\t密碼 : " + strs + "\tSHA1\t長度 : " + strs.Length + ", Base64\n";
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            //算一個檔案的 SHA1, SHA256值

            //SHA1
            var tragetFile = new FileStream(filename, FileMode.Open);

            var sha1 = new SHA1CryptoServiceProvider();
            byte[] hashbytes = sha1.ComputeHash(tragetFile);

            tragetFile.Close();

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < hashbytes.Length; i++)
            {
                sb.Append(hashbytes[i].ToString("X2"));
            }
            richTextBox1.Text += "SHA1\n";
            richTextBox1.Text += sb.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //SHA256
            tragetFile = new FileStream(filename, FileMode.Open);

            var sha256 = new SHA256CryptoServiceProvider();
            hashbytes = sha256.ComputeHash(tragetFile);

            tragetFile.Close();

            sb = new StringBuilder();
            for (int i = 0; i < hashbytes.Length; i++)
            {
                sb.Append(hashbytes[i].ToString("x2"));
            }
            richTextBox1.Text += "SHA256\n";
            richTextBox1.Text += sb.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "計算一個檔案的SHA值\n";
            //各種檔案加密1
            string result_SHA1 = ValidHelper.GetFileSHA1(filename);
            string result_SHA256 = ValidHelper.GetFileSHA256(filename);
            string result_SHA384 = ValidHelper.GetFileSHA384(filename);
            string result_SHA512 = ValidHelper.GetFileSHA512(filename);

            //SHA1 40 字符
            richTextBox1.Text += "SHA1 : \t\t" + result_SHA1 + "\n";

            //SHA256 64 字符
            richTextBox1.Text += "SHA256 : \t" + result_SHA256 + "\n";

            //SHA384
            richTextBox1.Text += "SHA384 : \t" + result_SHA384 + "\n";

            //SHA512 128 字符
            richTextBox1.Text += "SHA512 : \t" + result_SHA512 + "\n";

            /* 
            SHA1 40 字符
            b962fe33ed5288407d2e673403a7b68bdb160e5a
            SHA256 64 字符
            5d57e3deb441b789f6035d28dcbbaf6a436c54450972786fad4ce4527059d291
            SHA512 128 字符
            1b8eac217e4a1ce78585290c74456d1e7ed683ae12b91e1d67bd46452ea318d00523f74f7ebc7949aef45a410525b470541efca031e0ef23b8a82ef860874977
            SHA3-256 64 字符
            2a2ce75f2a2ce75f2a2ce75f2a2ce75f2a2ce75f2a2ce75f2a2ce75f2a2ce75f 
            */

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "計算一個檔案的SHA1值\n";
            str_encrypted_text = HashHelper.SHA1File(filename);
            richTextBox1.Text += "01ms檔案 : " + filename + "\tSHA1值 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "計算一個檔案的SHA256值\n";
            FileStream stream = File.OpenRead(filename);
            SHA256 Sha256 = SHA256.Create();  // 創建SHA256對象
            byte[] ccc = Sha256.ComputeHash(stream);

            str_encrypted_text = BytesToString(ccc);
            richTextBox1.Text += "02ms檔案 : " + filename + "\tSHA256值 : " + str_encrypted_text + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "計算一個檔案的SHA256值\n";
            FileStream fs = File.OpenRead(filename);

            SHA256Managed sha = new SHA256Managed();
            str_encrypted_text = Convert.ToBase64String(sha.ComputeHash(fs));  // Hash轉字串, Base64
            richTextBox1.Text += "03ms檔案 : " + filename + "\tSHA256值 : " + str_encrypted_text + ", Base64\n";
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
            //各種檔案加密

            //下面幾個函數

            //TBD

        }

        ///SHA1加密
        /// <summary>
        /// 使用 SHA1 加密算法来加密
        /// </summary>
        /// <param name="sourceString">原字符串</param>
        /// <returns>加密后字符串</returns>
        public static string SHA1_Encrypt(string sourceString)
        {
            byte[] StrRes = Encoding.UTF8.GetBytes(sourceString);
            HashAlgorithm iSHA = new SHA1CryptoServiceProvider();
            StrRes = iSHA.ComputeHash(StrRes);
            StringBuilder EnText = new StringBuilder();
            foreach (byte iByte in StrRes)
            {
                EnText.AppendFormat("{0:x2}", iByte);
            }
            return EnText.ToString();
        }

        ///SHA256加密

        /// <summary>
        /// SHA256 加密
        /// </summary>
        /// <param name="sourceString">原字符串</param>
        /// <returns>加密后字符串</returns>
        public static string SHA256_Encrypt(string sourceString)
        {
            byte[] data = Encoding.UTF8.GetBytes(sourceString);
            SHA256 shaM = SHA256.Create();  // 創建SHA256對象
            byte[] result = shaM.ComputeHash(data);
            StringBuilder EnText = new StringBuilder();
            foreach (byte iByte in result)
            {
                EnText.AppendFormat("{0:x2}", iByte);
            }
            return EnText.ToString();
        }

        ///SHA384加密
        /// <summary>
        /// SHA384 加密
        /// </summary>
        /// <param name="sourceString">原字符串</param>
        /// <returns>加密后字符串</returns>
        public static string SHA384_Encrypt(string sourceString)
        {
            byte[] data = Encoding.UTF8.GetBytes(sourceString);
            SHA384 shaM = SHA384.Create();  // 創建SHA384對象
            byte[] result = shaM.ComputeHash(data);
            StringBuilder EnText = new StringBuilder();
            foreach (byte iByte in result)
            {
                EnText.AppendFormat("{0:x2}", iByte);
            }
            return EnText.ToString();
        }

        ///SHA512加密

        /// <summary>
        /// SHA512_加密
        /// </summary>
        /// <param name="sourceString">原字符串</param>
        /// <returns>加密后字符串</returns>
        public static string SHA512_Encrypt(string sourceString)
        {
            byte[] data = Encoding.UTF8.GetBytes(sourceString);
            SHA512 shaM = new SHA512Managed();
            byte[] result = shaM.ComputeHash(data);
            StringBuilder EnText = new StringBuilder();
            foreach (byte iByte in result)
            {
                EnText.AppendFormat("{0:x2}", iByte);
            }
            return EnText.ToString();
        }

        //------------------------------------------------------------  # 60個
        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {


        }

        //------------------------------------------------------------  # 60個

        private void button19_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        //自建函數 ST

        string MD5_Ecnrypt04(string text)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = Encoding.UTF8.GetBytes(text);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                sb.Append(b.ToString("X2"));  // 轉2位的16進制字串
            }
            return sb.ToString();
        }

        //------------------------------------------------------------  # 60個

        //MD5加密, 以此為標準
        string MD5_Ecnrypt08(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象
            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值
            string md5Result = BytesToString(md5Hash);  // Hash轉字串
            return md5Result;
        }

        //------------------------------------------------------------  # 60個

        public static string MD5_Ecnrypt14(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值
            //string md5Result = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串  NG
            string md5Result = BytesToString(md5Hash);  // Hash轉字串
            return md5Result;
        }

        private string GetStringValue(byte[] Byte)
        {
            // 這一個應該是不太對  不應該是   tmpString = tmpString + Byte[i].ToString();

            string tmpString = "";
            /*
            ASCIIEncoding Asc = new ASCIIEncoding();
            tmpString = Asc.GetString(Byte);  // 拜列轉字串
            */

            for (int i = 0; i < Byte.Length; i++)
            {
                tmpString = tmpString + Byte[i].ToString();
            }
            return tmpString;
        }

        private byte[] GetKeyByteArray(string str)
        {
            /*
            int tmpStrLen = str.Length;
            byte[] input = new byte[tmpStrLen - 1];
            ASCIIEncoding Asc = new ASCIIEncoding();
            input = Asc.GetBytes(str);  // 字串轉拜列
            return input;
            */
            //改成用UTF8
            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            return input;
        }

        //------------------------------------------------------------  # 60個

        public static string MD5_Ecnrypt03(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                sb.Append(b.ToString("X2"));  // 轉2位的16進制字串
            }
            return sb.ToString();
        }

        public string MD5_Ecnrypt15(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值
            //string md5Result = GetStringValue(md5Hash);  // Hash轉字串, 這個應該是不對的
            //return md5Result;
            string md5Result = "";  //定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5Hash.Length; i++)//遍歷Byte數組
            {
                md5Result += md5Hash[i].ToString("X2");//對遍歷到的Byte進行加密  // 轉2位的16進制字串
            }
            return md5Result;
        }



        //------------------------------------------------------------  # 60個

        /*
        //c#實現md5加密
        1. 首先創建MD5的哈希算法。
        ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(UTF8.GetBytes(input))
        2.計算哈希值
        使用方法:ComputeHash(byte[] value);
        3.轉化成字符串.
        */
        string MD5_Ecnrypt20(string str)
        {
            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = ((HashAlgorithm)CryptoConfig.CreateFromName("MD5")).ComputeHash(input);  // 算拜列之Hash值
            string md5Result = BytesToString(md5Hash);  // Hash轉字串
            return md5Result;
        }

        //------------------------------------------------------------  # 60個

        /// 加密用戶密碼
        /// <param name="password">密碼</param>
        /// <param name="codeLength">加密位數</param>
        /// <returns>加密密碼</returns>
        public static string MD5_Ecnrypt22(string str)
        {
            string md5Result = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5").ToUpper();
            return md5Result;
        }

        public string MD5_Ecnrypt25(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = GetKeyByteArray(str); //字串轉拜列
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值
            //string md5Result = GetStringValue(md5Hash);  // Hash轉字串, 這個應該是不對的
            //return md5Result;
            string md5Result = "";  //定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5Hash.Length; i++)//遍歷Byte數組
            {
                md5Result += md5Hash[i].ToString("X2");//對遍歷到的Byte進行加密  // 轉2位的16進制字串
            }
            return md5Result;
        }

        public string MD5_Ecnrypt28(string str)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象

            byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            //string md5Result = ASCIIEncoding.ASCII.GetString(md5.ComputeHash(input));  // 拜列轉字串 NG
            byte[] md5Hash = md5.ComputeHash(input);  // 算拜列之Hash值
            //string md5Result = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串
            string md5Result = BytesToString(md5Hash);  // Hash轉字串
            return md5Result;
        }

        //自建函數 SP
    }

    //------------------------------------------------------------  # 60個

    public class EncryptHelper
    {
        /// 获取某个哈希算法对应下的哈希值
        /// <param name="sourceString">源字符串</param>
        /// <param name="algorithm">哈希算法</param>
        /// <returns>经过计算的哈希值</returns>
        private static string GetHash(string sourceString, HashAlgorithm algorithm)
        {
            byte[] sourceBytes = Encoding.UTF8.GetBytes(sourceString);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            byte[] md5Hash = algorithm.ComputeHash(sourceBytes);  // 算拜列之Hash值
            algorithm.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
            }
            return sb.ToString();
        }

        /// 获取MD5值
        /// <param name="sourceString">源字符串</param>
        /// <returns>MD5值</returns>
        public static string GetMD5(string sourceString)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            return GetHash(sourceString, md5);
        }

        /// 获取SHA1值
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA1值</returns>
        public static string GetSHA1(string sourceString)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            return GetHash(sourceString, sha1);
        }

        /// 获取SHA256值
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA256值</returns>
        public static string GetSHA256(string sourceString)
        {
            SHA256 sha256 = SHA256.Create();  // 創建SHA256對象
            return GetHash(sourceString, sha256);
        }

        /// 获取SHA384值
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA384值</returns>
        public static string GetSHA384(string sourceString)
        {
            SHA384 sha384 = SHA384.Create();  // 創建SHA384對象
            return GetHash(sourceString, sha384);
        }

        /// 获取SHA512值
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA512值</returns>
        public static string GetSHA512(string sourceString)
        {
            SHA512 sha512 = SHA512.Create();  // 創建SHA512對象
            return GetHash(sourceString, sha512);
        }

        public static string GetFileBase64String(string filePath)
        {
            using (FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read))
            {
                using (BinaryReader reader = new BinaryReader(fs))
                {
                    try
                    {
                        return GetBase64String(reader.ReadBytes((int)fs.Length));
                    }
                    catch (System.Exception ex)
                    {
                        throw ex;
                    }
                }
            }
        }

        public static string GetBase64String(string sourceString)
        {
            byte[] buffer = Encoding.UTF8.GetBytes(sourceString);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            return GetBase64String(buffer);
        }

        public static string GetBase64String(string sourceString, Encoding encoding)
        {
            byte[] buffer = encoding.GetBytes(sourceString);  // 字串轉拜列
            return GetBase64String(buffer);
        }

        public static string GetBase64String(byte[] sourceBytes)
        {
            string base64String = System.Convert.ToBase64String(sourceBytes);  // Hash轉字串, Base64
            return base64String;
        }
    }

    //------------------------------------------------------------  # 60個

    // Hash輔助類
    public class HashHelper
    {
        /// 計算文件的 MD5 值
        /// <param name="filename">要計算 MD5 值的文件名和路徑</param>
        /// <returns>MD5 值16進制字符串</returns>
        public static string MD5File(string filename)
        {
            return HashFile(filename, "md5");
        }

        /// 計算文件的 sha1 值
        /// <param name="filename">要計算 sha1 值的文件名和路徑</param>
        /// <returns>sha1 值16進制字符串</returns>
        public static string SHA1File(string filename)
        {
            return HashFile(filename, "sha1");
        }

        /// 計算文件的哈希值
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

        /// 計算哈希值
        /// <param name="stream">要計算哈希值的 Stream</param>
        /// <param name="algorithm">算法:SHA1 或 MD5</param>
        /// <returns>哈希值字節數組</returns>
        private static byte[] HashData(Stream stream, string algorithm)
        {
            //創建物件, 可能是 SHA1 或 MD5
            HashAlgorithm hashAlgorithm;

            if (algorithm == null)
            {
                throw new ArgumentNullException("algorithm 不能為 null");
            }

            if (string.Compare(algorithm, "sha1", true) == 0)
            {
                hashAlgorithm = SHA1.Create();  // 創建SHA1對象
            }
            else
            {
                if (string.Compare(algorithm, "md5", true) != 0)
                {
                    throw new Exception("algorithm 只能使用 sha1 或 md5");
                }
                hashAlgorithm = MD5.Create();  // 創建MD5對象
            }
            return hashAlgorithm.ComputeHash(stream);
        }

        // 字節數組轉換為16進制表示的字符串
        private static string ByteArrayToHexString(byte[] buf)
        {
            return BitConverter.ToString(buf).Replace("-", "");
        }
    }

    public static class ValidHelper
    {
        public static string GetFileHash(string filePath, HashAlgorithm algorithm)
        {
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] md5Hash = algorithm.ComputeHash(fs);
            fs.Close();
            algorithm.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
            }
            return sb.ToString();
        }

        public static string GetFileMD5(string filePath)
        {
            MD5 md5 = MD5.Create();  // 創建MD5對象
            return GetFileHash(filePath, md5);
        }

        public static string GetFileSHA1(string filePath)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            return GetFileHash(filePath, sha1);
        }

        public static string GetFileSHA256(string filePath)
        {
            SHA256 sha256 = SHA256.Create();  // 創建SHA256對象
            return GetFileHash(filePath, sha256);
        }

        public static string GetFileSHA384(string filePath)
        {
            SHA384 sha384 = SHA384.Create();  // 創建SHA384對象
            return GetFileHash(filePath, sha384);
        }

        public static string GetFileSHA512(string filePath)
        {
            SHA512 sha512 = SHA512.Create();  // 創建SHA512對象
            return GetFileHash(filePath, sha512);
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


/*  可搬出

*/


/*
//C#使用MD5對用戶密碼加密與驗證
//C#中常涉及到對用戶密碼的加密於解密的算法，其中使用MD5加密是最常見的的實現方式
      
5）通過DESCryptoServiceProvider對象對字符串進行加密解密

/// DES數據加密
/// <param name="targetValue">目標值</param>
/// <param name="key">密鑰</param>
/// <returns>加密值</returns>
public static string Encrypt(string targetValue, string key)
{
    StringBuilder sb = new StringBuilder();
    var des = new DESCryptoServiceProvider();
    byte[] input = Encoding.UTF8.GetBytes(targetValue);  // 字串轉拜列, 中文字要先用 UTF8轉碼
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
    cs.Write(input, 0, input.Length);
    cs.FlushFinalBlock();
    foreach (byte b in ms.ToArray())
    {
        sb.AppendFormat("{0:X2}", b);
    }
    return sb.ToString();
}

//此種算法可以通過加密密鑰進行解密，解密方法如下 :
/// DES數據解密
/// <param name="targetValue"></param>
/// <param name="key"></param>
/// <returns></returns>
public static string Decrypt(string targetValue, string key)
{
    // 定義DES加密對象
    var des = new DESCryptoServiceProvider();
    int len = targetValue.Length / 2;
    var input = new byte[len];
    int x, i;
    for (x = 0; x < len; x++)
    {
        i = Convert.ToInt32(targetValue.Substring(x * 2, 2), 16);
        input[x] = (byte)i;
    }
    // 通過兩次哈希密碼設置對稱算法的初始化向量   
    des.Key = Encoding.UTF8.GetBytes(FormsAuthentication.HashPasswordForStoringInConfigFile
                                            (FormsAuthentication.HashPasswordForStoringInConfigFile(key, "md5").
                                                Substring(0, 8), "sha1").Substring(0, 8));
    // 通過兩次哈希密碼設置算法的機密密鑰   
    des.IV = Encoding.UTF8.GetBytes(FormsAuthentication.HashPasswordForStoringInConfigFile
                                            (FormsAuthentication.HashPasswordForStoringInConfigFile(key, "md5")
                                                .Substring(0, 8), "md5").Substring(0, 8));
    // 定義內存流
    var ms = new MemoryStream();
    // 定義加密流
    var cs = new CryptoStream(ms, des.CreateDecryptor(), CryptoStreamMode.Write);
    cs.Write(input, 0, input.Length);
    cs.FlushFinalBlock();
    return Encoding.UTF8.GetString(ms.ToArray());  // 拜列轉字串
}

//------------------------------------------------------------  # 60個

         // MD5加密(返回16位加密串)
         public static string MD5Encrypt16b(string input, Encoding encode)
         {
             MD5 md5 = MD5.Create();  // 創建MD5對象
             string md5Hash = BitConverter.ToString(md5.ComputeHash(encode.GetBytes(input)), 4, 8);
             md5Hash = md5Hash.Replace("-", "");
             return md5Hash;
         }

            //將字串用MD5加密
            Console.Write("請輸入密碼 : ");
            string P_str_Code = Console.ReadLine();//记录要加密的密码
            Program program = new Program();//创建Program对象
            Console.WriteLine("結果:\n" + program.Encrypt2(P_str_Code));//输出加密后的字符串

 //獲取要加密的字段，並轉化為Byte[]數組
            byte[] input = Encoding.UTF8.GetBytes(str.ToCharArray());  // 字串轉拜列, 中文字要先用 UTF8轉碼
            //建立加密服務
            MD5 md5 = MD5.Create();  // 創建MD5對象

//------------------------------------------------------------  # 60個

MD5/SHA1說明大集合

異名同義字

MD5 md5 = new MD5CryptoServiceProvider();  // 創建MD5對象
等同於
MD5 md5 = MD5.Create();  // 創建MD5對象
使用後者


MD5 md5 = MD5CryptoServiceProvider.Create();  // 創建MD5對象
 * 
 * 
MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
HashAlgorithm md5 = new MD5CryptoServiceProvider(); // or SHA1CryptoServiceProvider();
HashAlgorithm md5 = MD5.Create();

MD5 md5 = MD5.Create();  // 創建MD5對象
//MD5 md5 = MD5CryptoServiceProvider.Create();  // 創建MD5對象
//MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
//HashAlgorithm md5 = new MD5CryptoServiceProvider(); // or SHA1CryptoServiceProvider();
//HashAlgorithm md5 = MD5.Create();

//------------------------------------------------------------  # 60個

string md5Result = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串

各種拜列轉字串

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
            }
            md5Result = sb.ToString();

            //Hash轉字串
            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result = md5Result + md5Hash[i].ToString("X2");  // 轉2位的16進制字串
            }

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
                //sb.AppendFormat("{0:X2}", md5Hash[i]);    //same
            }
            md5Result = sb.ToString();

            //Hash轉字串
            StringBuilder sb = new StringBuilder();
            foreach (byte b in md5Hash)
            {
                sb.Append(b.ToString("X2"));  // 轉2位的16進制字串
            }
            md5Result = sb.ToString();

            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result += md5Hash[i].ToString("X2");  // 轉2位的16進制字串
            }

            //Hash轉字串
            md5Result = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串

            //Hash轉字串
            md5Result = GetStringValue(md5Hash);  // 這個應該是不對的

            //Hash轉字串
            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result += md5Hash[i].ToString("X2");  // 轉2位的16進制字串
            }

            for (int i = 0; i < md5Hash.Length - 1; i++)//遍歷Byte數組
            {
                md5Result += md5Hash[i].ToString("X2");//對遍歷到的Byte進行加密  // 轉2位的16進制字串
            }

            for (int i = 0; i < md5Hash.Length; i++)
            {
                md5Result = md5Result + md5Hash[i].ToString("X2");  // 轉2位的16進制字串
            }

            //Hash轉字串
            StringBuilder sb = new StringBuilder(16);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append((md5Hash[i]).ToString("X2", System.Globalization.CultureInfo.InvariantCulture));  // 轉2位的16進制字串
            }
            md5Result = sb.ToString();

            //Hash轉字串
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < md5Hash.Length; i++)
            {
                sb.Append(md5Hash[i].ToString("X2"));  // 轉2位的16進制字串
            }
            md5Result = sb.ToString();

            //md5Result = BitConverter.ToString(md5Hash).Replace("-", "");
            //md5Result = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串

            //Hash轉字串
            //將加密後的數組轉化為字段(普通加密)  
            //string testResult = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串

            //作為密碼方式加密
            //需要改用.NetFramework4.0 且 參考/加入參考 .NET /System.Web
            //md5Result = System.Web.Security.FormsAuthentication.HashPasswordForStoringInConfigFile(str, "MD5");

//------------------------------------------------------------  # 60個

        //MD5，SHA1，SHA256，SHA512 ST

        // 使用DES加密（Added by niehl 2005-4-6）
        // <param name="originalValue">待加密的字符串</param>
        // <param name="key">密鑰(最大長度8)</param>
        // <param name="IV">初始化向量(最大長度8)</param>
        // <returns>加密後的字符串</returns>
        public string DESEncrypt(string originalValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            sa.IV  = Encoding.UTF8.GetBytes(IV);   // 字串轉拜列, 中文字要先用 UTF8轉碼
            ct = sa.CreateEncryptor();
            byt = Encoding.UTF8.GetBytes(originalValue);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Convert.ToBase64String(ms.ToArray());  // Hash轉字串, Base64
        }

        public string DESEncrypt(string originalValue, string key)
        {
            return DESEncrypt(originalValue, key, key);
        }

        // 使用DES解密（Added by niehl 2005-4-6）
        /// <param name="encryptedValue">待解密的字符串</param>
        /// <param name="key">密鑰(最大長度8)</param>
        /// <param name="IV">m初始化向量(最大長度8)</param>
        /// <returns>解密後的字符串</returns>
        public string DESDecrypt(string encryptedValue, string key, string IV)
        {
            //將key和IV處理成8個字符
            key += "12345678";
            IV += "12345678";
            key = key.Substring(0, 8);
            IV = IV.Substring(0, 8);
            SymmetricAlgorithm sa;
            ICryptoTransform ct;
            MemoryStream ms;
            CryptoStream cs;
            byte[] byt;
            sa = new DESCryptoServiceProvider();
            sa.Key = Encoding.UTF8.GetBytes(key);  // 字串轉拜列, 中文字要先用 UTF8轉碼
            sa.IV  = Encoding.UTF8.GetBytes(IV);   // 字串轉拜列, 中文字要先用 UTF8轉碼
            ct = sa.CreateDecryptor();
            byt = Convert.FromBase64String(encryptedValue);
            ms = new MemoryStream();
            cs = new CryptoStream(ms, ct, CryptoStreamMode.Write);
            cs.Write(byt, 0, byt.Length);
            cs.FlushFinalBlock();
            cs.Close();
            return Encoding.UTF8.GetString(ms.ToArray());  // 拜列轉字串
        }

        public string DESDecrypt(string encryptedValue, string key)
        {
            return DESDecrypt(encryptedValue, key, key);
        }

//------------------------------------------------------------  # 60個

            //Hash轉字串
            // 轉為32位字符串
            string hashString = "";
            for (int i = 0; i < md5Hash.Length; i++)
            {
                hashString += Convert.ToString(md5Hash[i], 16).PadLeft(2, '0');
            }
            md5Result = hashString.PadLeft(32, '0');
*/

/*
測試網站
https://tw.piliapp.com/hash/md5/

*/


/*
// 字串轉拜列

預設編碼 改 UTF8編碼

把所有的 
byte[] input = Encoding.Default.GetBytes(str);  // 字串轉拜列
改成
byte[] input = Encoding.UTF8.GetBytes(str);  // 字串轉拜列, 中文字要先用 UTF8轉碼

*/

// 拜列轉字串
// md5Result = Encoding.UTF8.GetString(md5Hash);  // 拜列轉字串

//byte[] input = Encoding.ASCII.GetBytes(str);
//byte[] input = Encoding.Unicode.GetBytes(str);
//byte[] input = ASCIIEncoding.ASCII.GetBytes(str);   //字串轉拜列

//Encoding encode = Encoding.Unicode;
//Encoding encode = new UTF8Encoding();
//byte[] input = encode.GetBytes(str); //字串轉拜列

//


