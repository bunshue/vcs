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
namespace 文字文件加密與解密
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

        //選擇加密解密文件路徑
        private void button3_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "文字文件|*.txt|*.*|*.*";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }  
        }
        ///*************************/

        //解密
        private void button4_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            {
                MessageBox.Show("請選擇要解密的文件路徑");
            }
            else
            {
                string strPath = textBox1.Text;//加密文件的路徑
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
                string strInName = strPath.Substring(0, strPath.LastIndexOf("\\") + 1) + strName + ".txt";
                byte[] key = { 24, 55, 102, 24, 98, 26, 67, 29, 84, 19, 37, 118, 104, 85, 121, 27, 93, 86, 24, 55, 102, 24, 98, 26, 67, 29, 9, 2, 49, 69, 73, 92 };
                byte[] IV ={ 22, 56, 82, 77, 84, 31, 74, 24, 55, 102, 24, 98, 26, 67, 29, 99 };
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
                if (MessageBox.Show(strInName, "提示:解密成功!解密後的文件名及路徑為:" + "是否冊除源文件", MessageBoxButtons.YesNo) == DialogResult.Yes)
                {
                    File.Delete(strPath);
                    textBox1.Text = "";
                }
                else
                {
                    textBox1.Text = "";
                }

            }
        }
        //加密
        private void button5_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            { MessageBox.Show("請選擇要加密的文件"); }
            else
            {
               try{
                string strPath = textBox1.Text;//加密文件的路徑
                int intLent=strPath.LastIndexOf("\\")+1;
                int intLong = strPath.Length;
                string strName = strPath.Substring(intLent,intLong-intLent);//要加密的文件名稱
                int intTxt = strName.LastIndexOf(".");
                int intTextLeng = strName.Length;
                string strTxt = strName.Substring(intTxt,intTextLeng-intTxt);//取出文件的擴充名
                strName = strName.Substring(0,intTxt);
                //加密後的文件名及路徑
                string strOutName = strPath.Substring(0, strPath.LastIndexOf("\\") + 1) + strName + "Out" + strTxt;
                byte[] key = { 24, 55, 102, 24, 98, 26, 67, 29, 84, 19, 37, 118, 104, 85, 121, 27, 93, 86, 24, 55, 102, 24, 98, 26, 67, 29, 9, 2, 49, 69, 73, 92 };
                byte[] IV ={ 22, 56, 82, 77, 84, 31, 74, 24, 55, 102, 24, 98, 26, 67, 29, 99 };
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
                if (MessageBox.Show(strOutName, "提示:加密成功!加密後的文件名及路徑為:\n"+"是否冊除源文件", MessageBoxButtons.YesNo) == DialogResult.Yes)
                {
                    File.Delete(strPath);
                    textBox1.Text = "";
                }else
                { textBox1.Text = ""; }
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
            }
        }

      /***************************/
    }
}