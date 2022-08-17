using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography; //for RijndaelManaged

//文件校驗工具的開發及問題，校驗工具開發

namespace vcs_Cryptography4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        public string ROT13Encode(string InputText)
        {
            char tem_Character;
            int UnicodeChar;
            string EncodedText = "";
            for (int i = 0; i < InputText.Length; i++)//搜尋字串中的所有字符
            {
                tem_Character = System.Convert.ToChar(InputText.Substring(i, 1));//取得字串中指定的字符
                UnicodeChar = (int)tem_Character;//取得目前字符的Unicode編碼
                if (UnicodeChar >= 97 && UnicodeChar <= 109)//對字符進行加密
                {
                    UnicodeChar = UnicodeChar + 13;
                }
                else if (UnicodeChar >= 110 && UnicodeChar <= 122)//對字符進行解密
                {
                    UnicodeChar = UnicodeChar - 13;
                }
                else if (UnicodeChar >= 65 && UnicodeChar <= 77)//對字符進行加密
                {
                    UnicodeChar = UnicodeChar + 13;
                }
                else if (UnicodeChar >= 78 && UnicodeChar <= 90)//對字符進行解密
                {
                    UnicodeChar = UnicodeChar - 13;
                }
                EncodedText = EncodedText + (char)UnicodeChar;//傳回設定後的字符
            }
            return EncodedText;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //ROT13編碼
            richTextBox_rot13b.Text = ROT13Encode(richTextBox_rot13a.Text);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //ROT13解碼, 其實就是再編碼一次
            richTextBox_rot13c.Text = ROT13Encode(richTextBox_rot13b.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //加密
            textBox2.Text = Encrypt(textBox1.Text);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //解密
            textBox2.Text = Decryptor(textBox2.Text);
        }

        private string Encrypt(string s)
        {
            Encoding ascii = Encoding.ASCII;
            string EncryptString;
            EncryptString = "";
            for (int i = 0; i < s.Length; i++)
            {
                int j;
                byte[] b = new byte[1];
                j = Convert.ToInt32(ascii.GetBytes(s[i].ToString())[0]);
                j = j + 5;
                b[0] = Convert.ToByte(j);
                EncryptString = EncryptString + ascii.GetString(b);
            }
            return EncryptString;
        }

        private string Decryptor(string s)
        {
            Encoding ascii = Encoding.ASCII;
            string DecryptorString;
            DecryptorString = "";
            for (int i = 0; i < s.Length; i++)
            {
                int j;
                byte[] b = new byte[1];
                j = Convert.ToInt32(ascii.GetBytes(s[i].ToString())[0]);
                j = j - 5;
                b[0] = Convert.ToByte(j);
                DecryptorString = DecryptorString + ascii.GetString(b);
            }
            return DecryptorString;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //加密

            //TextEncrypt
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //解密

            //TextDecrypt

        }

        //C#最簡單的文本加密 與 解密
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

        string str_encrypted_text = string.Empty;   //加密後的結果
        string filename1 = @"C:\______test_files\__RW\_txt\txt_clear.txt";          //明碼
        string filename2 = @"C:\______test_files\__RW\_txt\txt_encrypt.txt";        //密碼

        private void button7_Click(object sender, EventArgs e)
        {
            //檔案加密1
            try
            {
                string strPath = filename1;//加密文件的路徑
                int intLent = strPath.LastIndexOf("\\") + 1;
                int intLong = strPath.Length;
                string strName = strPath.Substring(intLent, intLong - intLent);//要加密的文件名稱
                int intTxt = strName.LastIndexOf(".");
                int intTextLeng = strName.Length;
                string strTxt = strName.Substring(intTxt, intTextLeng - intTxt);//取出文件的擴充名
                strName = strName.Substring(0, intTxt);
                //加密後的文件名及路徑

                string strOutName = Application.StartupPath + "\\txt_encode_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
                //string strOutName = strPath.Substring(0, strPath.LastIndexOf("\\") + 1) + strName + "Out" + strTxt;

                byte[] key = { 24, 55, 102, 24, 98, 26, 67, 29, 84, 19, 37, 118, 104, 85, 121, 27, 93, 86, 24, 55, 102, 24, 98, 26, 67, 29, 9, 2, 49, 69, 73, 92 };
                byte[] IV = { 22, 56, 82, 77, 84, 31, 74, 24, 55, 102, 24, 98, 26, 67, 29, 99 };
                RijndaelManaged myRijndael = new RijndaelManaged();
                FileStream fsOut = File.Open(strOutName, FileMode.Create, FileAccess.Write);
                FileStream fsIn = File.Open(strPath, FileMode.Open, FileAccess.Read);
                //寫入加密文字文件
                CryptoStream csDecrypt = new CryptoStream(fsOut, myRijndael.CreateEncryptor(key, IV), CryptoStreamMode.Write);
                //讀加密文字
                BinaryReader br = new BinaryReader(fsIn);
                csDecrypt.Write(br.ReadBytes((int)fsIn.Length), 0, (int)fsIn.Length);
                csDecrypt.FlushFinalBlock();
                csDecrypt.Close();
                fsIn.Close();
                fsOut.Close();

                richTextBox1.Text += "加密完成\n";

            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //檔案解密1

            string strPath = filename2; //加密文件的路徑
            int intLent = strPath.LastIndexOf("\\") + 1;
            int intLong = strPath.Length;
            string strName = strPath.Substring(intLent, intLong - intLent);//要加密的文件名稱
            int intTxt = strName.LastIndexOf(".");
            int intTextLeng = strName.Length;
            strName = strName.Substring(0, intTxt);

            if (strName.LastIndexOf("Out") != -1)
            {
                strName = strName.Substring(0, strName.LastIndexOf("Out"));
            }
            else
            {
                strName = strName + "In";
            }
            //加密後的文件名及路徑
            string strInName = Application.StartupPath + "\\txt_decode_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt";
            //string strInName = strPath.Substring(0, strPath.LastIndexOf("\\") + 1) + strName + ".txt";
            byte[] key = { 24, 55, 102, 24, 98, 26, 67, 29, 84, 19, 37, 118, 104, 85, 121, 27, 93, 86, 24, 55, 102, 24, 98, 26, 67, 29, 9, 2, 49, 69, 73, 92 };
            byte[] IV = { 22, 56, 82, 77, 84, 31, 74, 24, 55, 102, 24, 98, 26, 67, 29, 99 };
            RijndaelManaged myRijndael = new RijndaelManaged();
            FileStream fsOut = File.Open(strPath, FileMode.Open, FileAccess.Read);
            CryptoStream csDecrypt = new CryptoStream(fsOut, myRijndael.CreateDecryptor(key, IV), CryptoStreamMode.Read);
            StreamReader sr = new StreamReader(csDecrypt);//把文件讀出來
            StreamWriter sw = new StreamWriter(strInName);//解密後文件寫入一個新的文件
            sw.Write(sr.ReadToEnd());
            sw.Flush();
            sw.Close();
            sr.Close();
            fsOut.Close();

            richTextBox1.Text += "解密完成\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //檔案加密2
            string inFile = @"C:\______test_files\picture1.jpg";
            string outFile = inFile + ".dat";
            string password = "lion-mouse";
            DESFile.DESFileClass.EncryptFile(inFile, outFile, password);//加密文件
            //刪除加密前的文件
            //File.Delete(inFile);
            richTextBox1.Text += "加密成功\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //檔案解密2
            string inFile = @"C:\______test_files\picture1.jpg.dat";
            if (File.Exists(inFile) == false)
            {
                richTextBox1.Text += "檔案 : " + inFile + ", 不存在, 離開\n";
                return;
            }
            string outFile = inFile.Substring(0, inFile.Length - 4);
            string password = "lion-mouse";
            DESFile.DESFileClass.DecryptFile(inFile, outFile, password);//解密文件
            //刪除解密前的文件
            //File.Delete(inFile);
            richTextBox1.Text += "解密成功, 檔名 : " + outFile + "\n";
        }
    }
}


namespace DESFile
{
    /// <summary>
    /// 異常處理類
    /// </summary>
    public class CryptoHelpException : ApplicationException
    {
        public CryptoHelpException(string msg) : base(msg) { }
    }

    /// <summary>
    /// CryptHelp
    /// </summary>
    public class DESFileClass
    {
        private const ulong FC_TAG = 0xFC010203040506CF;

        private const int BUFFER_SIZE = 128 * 1024;

        /// <summary>
        /// 檢驗兩個Byte數組是否相同
        /// </summary>
        /// <param name="b1">Byte數組</param>
        /// <param name="b2">Byte數組</param>
        /// <returns>true－相等</returns>
        private static bool CheckByteArrays(byte[] b1, byte[] b2)
        {
            if (b1.Length == b2.Length)
            {
                for (int i = 0; i < b1.Length; ++i)
                {
                    if (b1[i] != b2[i])
                        return false;
                }
                return true;
            }
            return false;
        }

        /// <summary>
        /// 創建DebugLZQ ,http://www.cnblogs.com/DebugLZQ
        /// </summary>
        /// <param name="password">密碼</param>
        /// <param name="salt"></param>
        /// <returns>加密對象</returns>
        private static SymmetricAlgorithm CreateRijndael(string password, byte[] salt)
        {
            PasswordDeriveBytes pdb = new PasswordDeriveBytes(password, salt, "SHA256", 1000);
            SymmetricAlgorithm sma = Rijndael.Create();
            sma.KeySize = 256;
            sma.Key = pdb.GetBytes(32);
            sma.Padding = PaddingMode.PKCS7;
            return sma;
        }

        /// <summary>
        /// 加密文件隨機數生成
        /// </summary>
        private static RandomNumberGenerator rand = new RNGCryptoServiceProvider();

        /// <summary>
        /// 生成指定長度的隨機Byte數組
        /// </summary>
        /// <param name="count">Byte數組長度</param>
        /// <returns>隨機Byte數組</returns>
        private static byte[] GenerateRandomBytes(int count)
        {
            byte[] bytes = new byte[count];
            rand.GetBytes(bytes);
            return bytes;
        }

        /// <summary>
        /// 加密文件
        /// </summary>
        /// <param name="inFile">待加密文件</param>
        /// <param name="outFile">加密後輸入文件</param>
        /// <param name="password">加密密碼</param>
        public static void EncryptFile(string inFile, string outFile, string password)
        {
            using (FileStream fin = File.OpenRead(inFile),
            fout = File.OpenWrite(outFile))
            {
                long lSize = fin.Length; // 輸入文件長度
                int size = (int)lSize;
                byte[] bytes = new byte[BUFFER_SIZE]; // 緩存
                int read = -1; // 輸入文件讀取數量
                int value = 0;
                // 獲取IV和salt
                byte[] IV = GenerateRandomBytes(16);
                byte[] salt = GenerateRandomBytes(16);
                // 創建加密對象
                SymmetricAlgorithm sma = DESFileClass.CreateRijndael(password, salt);
                sma.IV = IV;
                // 在輸出文件開始部分寫入IV和salt
                fout.Write(IV, 0, IV.Length);
                fout.Write(salt, 0, salt.Length);
                // 創建散列加密
                HashAlgorithm hasher = SHA256.Create();
                using (CryptoStream cout = new CryptoStream(fout, sma.CreateEncryptor(), CryptoStreamMode.Write),
                chash = new CryptoStream(Stream.Null, hasher, CryptoStreamMode.Write))
                {
                    BinaryWriter bw = new BinaryWriter(cout);
                    bw.Write(lSize);
                    bw.Write(FC_TAG);
                    // 讀寫字節塊到加密流緩沖區
                    while ((read = fin.Read(bytes, 0, bytes.Length)) != 0)
                    {
                        cout.Write(bytes, 0, read);
                        chash.Write(bytes, 0, read);
                        value += read;
                    }
                    // 關閉加密流
                    chash.Flush();
                    chash.Close();
                    // 讀取散列
                    byte[] hash = hasher.Hash;
                    // 輸入文件寫入散列
                    cout.Write(hash, 0, hash.Length);
                    // 關閉文件流
                    cout.Flush();
                    cout.Close();
                }
            }
        }

        /// <summary>
        /// 解密文件
        /// </summary>
        /// <param name="inFile">待解密文件</param>
        /// <param name="outFile">解密後輸出文件</param>
        /// <param name="password">解密密碼</param>
        public static void DecryptFile(string inFile, string outFile, string password)
        {
            // 創建打開文件流
            using (FileStream fin = File.OpenRead(inFile),
            fout = File.OpenWrite(outFile))
            {
                int size = (int)fin.Length;
                byte[] bytes = new byte[BUFFER_SIZE];
                int read = -1;
                int value = 0;
                int outValue = 0;
                byte[] IV = new byte[16];
                fin.Read(IV, 0, 16);
                byte[] salt = new byte[16];
                fin.Read(salt, 0, 16);
                SymmetricAlgorithm sma = DESFileClass.CreateRijndael(password, salt);
                sma.IV = IV;
                value = 32;
                long lSize = -1;
                // 創建散列對象, 校驗文件
                HashAlgorithm hasher = SHA256.Create();
                using (CryptoStream cin = new CryptoStream(fin, sma.CreateDecryptor(), CryptoStreamMode.Read),
                chash = new CryptoStream(Stream.Null, hasher, CryptoStreamMode.Write))
                {
                    // 讀取文件長度
                    BinaryReader br = new BinaryReader(cin);
                    lSize = br.ReadInt64();
                    ulong tag = br.ReadUInt64();
                    if (FC_TAG != tag)
                        throw new CryptoHelpException("文件被破壞");
                    long numReads = lSize / BUFFER_SIZE;
                    long slack = (long)lSize % BUFFER_SIZE;
                    for (int i = 0; i < numReads; ++i)
                    {
                        read = cin.Read(bytes, 0, bytes.Length);
                        fout.Write(bytes, 0, read);
                        chash.Write(bytes, 0, read);
                        value += read;
                        outValue += read;
                    }
                    if (slack > 0)
                    {
                        read = cin.Read(bytes, 0, (int)slack);
                        fout.Write(bytes, 0, read);
                        chash.Write(bytes, 0, read);
                        value += read;
                        outValue += read;
                    }
                    chash.Flush();
                    chash.Close();
                    fout.Flush();
                    fout.Close();
                    byte[] curHash = hasher.Hash;
                    // 獲取比較和舊的散列對象
                    byte[] oldHash = new byte[hasher.HashSize / 8];
                    read = cin.Read(oldHash, 0, oldHash.Length);
                    if ((oldHash.Length != read) || (!CheckByteArrays(oldHash, curHash)))
                    {
                        throw new CryptoHelpException("文件被破壞");
                    }
                }
                if (outValue != lSize)
                {
                    throw new CryptoHelpException("文件大小不匹配");
                }
            }
        }
    }
}

