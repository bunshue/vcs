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

