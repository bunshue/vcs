using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Cryptography;
using System.IO;

namespace vcs_Cryptography2
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\______test_files\__RW\_txt\txt_clear.txt";          //明碼
        string filename2 = @"C:\______test_files\__RW\_txt\txt_encrypt.txt";        //密碼

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
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

        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button3_Click(object sender, EventArgs e)
        {
            string old_string = "abcdefg";
            string new_string = string.Empty;


            MD5CryptoServiceProvider M5 = new MD5CryptoServiceProvider();
            new_string = ASCIIEncoding.ASCII.GetString(M5.ComputeHash(ASCIIEncoding.ASCII.GetBytes(old_string)));


            richTextBox1.Text += "原字串:\t" + old_string + "\n";
            richTextBox1.Text += "MD5加密後的字串:\t" + new_string + "\n";
        }
    }
}
