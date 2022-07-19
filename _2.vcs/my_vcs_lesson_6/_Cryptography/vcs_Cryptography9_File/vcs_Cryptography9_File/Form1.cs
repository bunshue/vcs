using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Security.Cryptography;

//文件校驗工具的開發及問題，校驗工具開發

namespace vcs_Cryptography9_File
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\__RW\_txt\txt_clear.txt";          //明碼
        string filename2 = @"C:\______test_files\__RW\_txt\txt_encrypt.txt";        //密碼

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
            dx = 190;
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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";

            string result_MD5 = ValidHelper.GetFileMD5(filename);
            string result_SHA1 = ValidHelper.GetFileSHA1(filename);
            string result_SHA256 = ValidHelper.GetFileSHA256(filename);
            string result_SHA384 = ValidHelper.GetFileSHA384(filename);
            string result_SHA512 = ValidHelper.GetFileSHA512(filename);

            richTextBox1.Text += "MD5 : \t\t" + result_MD5 + "\n";
            richTextBox1.Text += "SHA1 : \t\t" + result_SHA1 + "\n";
            richTextBox1.Text += "SHA256 : \t" + result_SHA256 + "\n";
            richTextBox1.Text += "SHA384 : \t" + result_SHA384 + "\n";
            richTextBox1.Text += "SHA512 : \t" + result_SHA512 + "\n";
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
            SHA256 shaM = SHA256.Create();
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
            SHA384 shaM = SHA384.Create();
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

        private void button1_Click(object sender, EventArgs e)
        {
            //上面幾個函數

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲取文件MD5值
            //獲取文件MD5值
            string result = string.Empty;
            string filename = @"C:\______test_files\picture1.jpg";

            result = GetMD5HashFromFile(filename);
            richTextBox1.Text += "檔案 MD5加密的密碼：" + result + "\tMD5加密長度是：" + result.Length + "\n";
        }

        /// <summary>
        /// 獲取文件MD5值
        /// </summary>
        /// <param name="fileName">文件絕對路徑</param>
        /// <returns>MD5值</returns>
        public static string GetMD5HashFromFile(string fileName)
        {
            try
            {
                FileStream file = new FileStream(fileName, FileMode.Open);
                MD5 md5 = new MD5CryptoServiceProvider();
                byte[] retVal = md5.ComputeHash(file);
                file.Close();

                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < retVal.Length; i++)
                {
                    sb.Append(retVal[i].ToString("x2"));
                }
                return sb.ToString();
            }
            catch (Exception ex)
            {
                throw new Exception("GetMD5HashFromFile() fail,error:" + ex.Message);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //文件加密
            //文件加密
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

        private void button4_Click(object sender, EventArgs e)
        {
            //文件解密
            //文件解密

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

        private void button5_Click(object sender, EventArgs e)
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

        private void button6_Click(object sender, EventArgs e)
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

        private void button7_Click(object sender, EventArgs e)
        {
            //算一個檔案的MD5值
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                using (FileStream fs = File.OpenRead(openFileDialog1.FileName))
                {
                    MD5 m = MD5.Create();
                    richTextBox1.Text += "MD5 result : " + Convert.ToBase64String(m.ComputeHash(fs));
                }
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //用MD5比較兩個檔案

            //第一個檔案
            string FirstFilePath = "c://______test_files//zzz.html";
            //第一個檔案的MD5碼
            string FirstFileMD5 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第一個檔案MD5演算後的陣列
            byte[] FirstHash = algorithm.ComputeHash(File.ReadAllBytes(FirstFilePath));
            //建立第一個檔案的MD5碼
            foreach (byte b in FirstHash)
            {
                FirstFileMD5 += b.ToString("X2");
            }
            richTextBox1.Text += "檔案：" + FirstFilePath + ",\tMD5：" + FirstFileMD5 + "\n";

        }

        private void button9_Click(object sender, EventArgs e)
        {
            //計算文件的MD5值

            string filename = @"C:\______test_files\picture1.jpg";

            //01.計算文件的 MD5 值
            Console.WriteLine(string.Format("計算文件的 MD5 值：{0}", HashHelper.MD5File(filename)));
            richTextBox1.Text += "計算文件的 MD5 值：" + HashHelper.MD5File(filename) + "\n";

            //02.計算文件的 sha1 值
            Console.WriteLine(string.Format("計算文件的 sha1 值：{0}", HashHelper.SHA1File(filename)));
            richTextBox1.Text += "計算文件的 sha1 值：" + HashHelper.SHA1File(filename) + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //用MD5比對兩個檔案是否相同

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

        private void button11_Click(object sender, EventArgs e)
        {
            //用MD5比較兩個檔案

            //第一個檔案
            string FirstFilePath = @"c:/______test_files/picture1.jpg";
            //第二個檔案
            string SecondFilePath = @"c:/______test_files/picture2.jpg";
            //第一個檔案的MD5碼
            string FirstFileMD5 = string.Empty;
            //建立MD5的演算法
            HashAlgorithm algorithm = MD5.Create();
            //取得第一個檔案MD5演算後的陣列
            byte[] FirstHash = algorithm.ComputeHash(File.ReadAllBytes(FirstFilePath));
            //建立第一個檔案的MD5碼
            foreach (byte b in FirstHash)
            {
                FirstFileMD5 += b.ToString("X2");
            }
            //第二個檔案的MD5碼
            string SecondFileMD5 = string.Empty;
            //取得第二個檔案MD5演算後的陣列
            byte[] SecondHash = algorithm.ComputeHash(File.ReadAllBytes(SecondFilePath));
            ///建立第二個檔案的MD5碼
            foreach (byte b in SecondHash)
            {
                SecondFileMD5 += b.ToString("X2");
            }

            richTextBox1.Text += "檔案：" + FirstFilePath + ",\tMD5：" + FirstFileMD5 + "\n";
            richTextBox1.Text += "檔案：" + SecondFilePath + ",\tMD5：" + SecondFileMD5 + "\n";

            if (FirstFileMD5.Equals(SecondFileMD5))
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
            //算一個檔案的SHA1值

            string filename = @"C:\______test_files\picture1.jpg";

            using (FileStream fs = File.OpenRead(filename))
            {
                SHA256Managed sha = new SHA256Managed();
                richTextBox1.Text += "SHA1 result : " + Convert.ToBase64String(sha.ComputeHash(fs));
            }


        }

        private void button13_Click(object sender, EventArgs e)
        {
            //取得檔案的唯一檢查碼Checksum MD5 SHA

            string filename = @"C:\______test_files\picture1.jpg";


            using (FileStream fs = File.OpenRead(filename))
            {
                //SHA Code :
                SHA256Managed sha = new SHA256Managed();
                richTextBox1.Text += "SHA code:\n";
                richTextBox1.Text += Convert.ToBase64String(sha.ComputeHash(fs)) + "\n";

                //MD5 Code :
                MD5 m = MD5.Create();
                richTextBox1.Text += "MD5 code:\n";
                richTextBox1.Text += Convert.ToBase64String(m.ComputeHash(fs)) + "\n";
            }

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

    public static class ValidHelper
    {
        /* same
        //獲取文件的MD5值
        public static string GetFileMD5(string filePath)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] result = md5.ComputeHash(fs);
            md5.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < result.Length; i++)
            {
                sb.Append(result[i].ToString("X2"));
            }
            return sb.ToString();
        }

        //獲取文件的SHA1值
        public static string GetFileSHA1(string filePath)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            FileStream fs = new FileStream(filePath, FileMode.Open, FileAccess.Read, FileShare.Read);
            byte[] result = sha1.ComputeHash(fs);
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
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
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

    public class EncryptHelper
    {
        /// <summary>
        /// 获取某个哈希算法对应下的哈希值
        /// </summary>
        /// <param name="sourceString">源字符串</param>
        /// <param name="algorithm">哈希算法</param>
        /// <returns>经过计算的哈希值</returns>
        private static string GetHash(string sourceString, HashAlgorithm algorithm)
        {
            byte[] sourceBytes = Encoding.UTF8.GetBytes(sourceString);
            byte[] result = algorithm.ComputeHash(sourceBytes);
            algorithm.Clear();
            StringBuilder sb = new StringBuilder(32);
            for (int i = 0; i < result.Length; i++)
            {
                sb.Append(result[i].ToString("X2"));
            }
            return sb.ToString();
        }

        /* same
        /// <summary>
        /// MD5加密
        /// </summary>
        /// <param name="strPwd">原字符串</param>
        /// <returns>加密后字符串</returns>
        public static string GetMD5(string strPwd)
        {
            //MD5 对象创建的两种方式
            //MD5 md5 = MD5.Create();
            MD5 md5 = new MD5CryptoServiceProvider();
            //将输入的密码转换成字节数组
            byte[] bPwd = Encoding.UTF8.GetBytes(strPwd);
            //计算指定字节数组的哈希值
            byte[] bMD5 = md5.ComputeHash(bPwd);
            //释放加密服务提供类的所有资源
            md5.Clear();
            StringBuilder sbMD5Pwd = new StringBuilder();
            for (int i = 0; i < bMD5.Length; i++)
            {
                //将每个字节数据转换为2位的16进制的字符
                sbMD5Pwd.Append(bMD5[i].ToString("x2"));
            }
            return sbMD5Pwd.ToString();
        }
        */

        /// <summary>
        /// 获取MD5值
        /// </summary>
        /// <param name="sourceString">源字符串</param>
        /// <returns>MD5值</returns>
        public static string GetMD5(string sourceString)
        {
            MD5CryptoServiceProvider md5 = new MD5CryptoServiceProvider();
            return GetHash(sourceString, md5);
        }

        /// <summary>
        /// 获取SHA1值
        /// </summary>
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA1值</returns>
        public static string GetSHA1(string sourceString)
        {
            SHA1 sha1 = new SHA1CryptoServiceProvider();
            return GetHash(sourceString, sha1);
        }

        /// <summary>
        /// 获取SHA256值
        /// </summary>
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA256值</returns>
        public static string GetSHA256(string sourceString)
        {
            SHA256 sha256 = SHA256.Create();
            return GetHash(sourceString, sha256);
        }

        /// <summary>
        /// 获取SHA384值
        /// </summary>
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA384值</returns>
        public static string GetSHA384(string sourceString)
        {
            SHA384 sha384 = SHA384.Create();
            return GetHash(sourceString, sha384);
        }

        /// <summary>
        /// 获取SHA512值
        /// </summary>
        /// <param name="sourceString">源字符串</param>
        /// <returns>SHA512值</returns>
        public static string GetSHA512(string sourceString)
        {
            SHA512 sha512 = SHA512.Create();
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
            byte[] buffer = Encoding.UTF8.GetBytes(sourceString);
            return GetBase64String(buffer);
        }

        public static string GetBase64String(string sourceString, Encoding encoding)
        {
            byte[] buffer = encoding.GetBytes(sourceString);
            return GetBase64String(buffer);
        }

        public static string GetBase64String(byte[] sourceBytes)
        {
            string base64String = System.Convert.ToBase64String(sourceBytes);
            return base64String;
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
