using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security;
using System.Security.Cryptography;


//C# MD5加密

//C#開發筆記   一、C# MD5-16位加密實例,32位加密實例(兩種方法)
//1.MD5　16位加密實例


namespace vcs_Cryptography8
{
    public partial class Form1 : Form
    {
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
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //MD5，SHA1，SHA256，SHA512 ST
        private string getstrIN(string strIN)
        {
            if (strIN.Length == 0)
            {
                strIN = "~NULL~";
            }
            return strIN;
        }

        public string MD5Encrypt(string strIN)
        {
            byte[] tmpByte;
            MD5 md5 = new MD5CryptoServiceProvider();
            tmpByte = md5.ComputeHash(GetKeyByteArray(getstrIN(strIN)));
            md5.Clear();
            return GetStringValue(tmpByte);
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

        /**/
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
            return Convert.ToBase64String(ms.ToArray());
        }

        public string DESEncrypt(string originalValue, string key)
        {
            return DESEncrypt(originalValue, key, key);
        }

        /**/
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

        public string DESDecrypt(string encryptedValue, string key)
        {
            return DESDecrypt(encryptedValue, key, key);
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

        private void button0_Click(object sender, EventArgs e)
        {
            //MD5，SHA1，SHA256，SHA512
            //此類提供MD5，SHA1，SHA256，SHA512等四種算法，加密字串的長度依次增大。
            string str = "lion-mouse";

            string s1 = MD5Encrypt(str);
            string s2 = SHA1Encrypt(str);
            string s3 = SHA256Encrypt(str);
            string s4 = SHA512Encrypt(str);


            richTextBox1.Text += "s1 = " + s1 + "\n";
            richTextBox1.Text += "s2 = " + s2 + "\n";
            richTextBox1.Text += "s3 = " + s3 + "\n";
            richTextBox1.Text += "s4 = " + s4 + "\n";
        }
        //MD5，SHA1，SHA256，SHA512 SP

        private void button1_Click(object sender, EventArgs e)
        {
            //MD5加密
            string text = "lion-mouse";
            string result = getMd5a(text);
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

        private void button2_Click(object sender, EventArgs e)
        {
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


        //C#實現MD5加密
        /*
        MD5的全稱是message-digest algorithm 5(信息-摘要算法，在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest開發出來， 經md2、md3和md4發展而來。
        MD5具有很好的安全性(因為它具有不可逆的特征,加過密的密文經過解密後和加密前的東東相同的可能性極小)
        */
        //MD5 a ST
        private void button8_Click(object sender, EventArgs e)
        {
            string cccc = "lion-mouse";

            byte[] result = Encoding.Default.GetBytes(cccc);
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] output = md5.ComputeHash(result);

            richTextBox1.Text += BitConverter.ToString(output).Replace("-", "") + "\n";
        }
        //MD5 a SP

        ////MD5 b ST
        public static string GetMD5(string myString)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] fromData = System.Text.Encoding.Unicode.GetBytes(myString);
            byte[] targetData = md5.ComputeHash(fromData);
            string byte2String = null;

            for (int i = 0; i < targetData.Length; i++)
            {
                byte2String += targetData[i].ToString("x");
            }

            return byte2String;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string cccc = "lion-mouse";

            string result = GetMD5(cccc);

            richTextBox1.Text += result + "\n";
        }
        //MD5 b SP

        //MD5 c ST


        ///   <summary>
        ///   給一個字符串進行MD5加密
        ///   </summary>
        ///   <param   name="strText">待加密字符串</param>
        ///   <returns>加密後的字符串</returns>
        public static string MD5Encrypt2(string strText)
        {
            MD5 md5 = new MD5CryptoServiceProvider();
            byte[] result = md5.ComputeHash(System.Text.Encoding.Default.GetBytes(strText));
            return System.Text.Encoding.Default.GetString(result);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            string cccc = "lion-mouse";

            string result = MD5Encrypt2(cccc);  //cf string result = MD5Encrypt(cccc);

            richTextBox1.Text += result + "\n";
        }
        //MD5 c SP


        //MD5 d ST

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
        /// MD5　32位加密
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

        private void button11_Click(object sender, EventArgs e)
        {
            string cccc = "lion-mouse";

            string result = GetMd5StrA(cccc);
            richTextBox1.Text += result + "\n";

            result = GetMd5StrB(cccc);
            richTextBox1.Text += result + "\n";

            result = UserMd5(cccc);
            richTextBox1.Text += result + "\n";
        }
        //MD5 d SP

        //MD5 e ST

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

        private void button12_Click(object sender, EventArgs e)
        {
            string cccc = "lion-mouse";
            string result = StringToMD5Hash(cccc);
            richTextBox1.Text += result + "\n";
        }
        //MD5 e SP

        //MD5 f ST
        private void button13_Click(object sender, EventArgs e)
        {
            /*
            //獲取要加密的字段，並轉化為Byte[]數組
            byte[] data = System.Text.Encoding.Unicode.GetBytes(str.ToCharArray());
            //建立加密服務
            System.Security.Cryptography.MD5 md5 = new System.Security.Cryptography.MD5CryptoServiceProvider();
            //加密Byte[]數組
            byte[] result = md5.ComputeHash(data);
            */
        }
        //MD5 f SP

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

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

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //加密檔案
            string inFile = @"C:\______test_files\picture1.jpg";
            string outFile = inFile + ".dat";
            string password = "lion-mouse";
            DESFile.DESFileClass.EncryptFile(inFile, outFile, password);//加密文件
            //刪除加密前的文件
            //File.Delete(inFile);
            richTextBox1.Text += "加密成功\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //解密檔案
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
                        throw new CryptoHelpException("文件被破壞");
                }
                if (outValue != lSize)
                    throw new CryptoHelpException("文件大小不匹配");
            }
        }

    }

}






