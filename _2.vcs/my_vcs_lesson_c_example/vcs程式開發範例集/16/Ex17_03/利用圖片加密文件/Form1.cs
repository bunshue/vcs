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
namespace 利用圖片加密文件
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //打開圖片
        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "jpg,bmp,gif|*.jpg|*.gif|*.bmp";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.ImageLocation = openFileDialog1.FileName;
            }
        }
        //打開加密文件
        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "文字文件|*.txt";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }
        // 加密
        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                if (pictureBox1.ImageLocation==null)
                { MessageBox.Show("請選擇一幅圖片用於加密"); return; }
                if (textBox1.Text == "")
                { MessageBox.Show("請選擇加密文件路徑"); return; }
                //圖片流
                FileStream fsPic = new FileStream(pictureBox1.ImageLocation, FileMode.Open, FileAccess.Read);
                //加密文件流
                FileStream fsText = new FileStream(textBox1.Text, FileMode.Open, FileAccess.Read);
                //初始化Key IV
                byte[] bykey = new byte[16];
                byte[] byIv = new byte[8];
                fsPic.Read(bykey, 0, 16);
                fsPic.Read(byIv, 0, 8);
                //臨時加密文件
                string strPath = textBox1.Text;//加密文件的路徑
                int intLent = strPath.LastIndexOf("\\") + 1;
                int intLong = strPath.Length;
                string strName = strPath.Substring(intLent, intLong - intLent);//要加密的文件名稱
                string strLinPath = "C:\\" + strName;//臨時加密文件路徑
                FileStream fsOut = File.Open(strLinPath, FileMode.Create, FileAccess.Write);
                //開始加密
                RC2CryptoServiceProvider desc = new RC2CryptoServiceProvider();//des進行加
                BinaryReader br = new BinaryReader(fsText);//從要加密的文件中讀出文件內容
                CryptoStream cs = new CryptoStream(fsOut, desc.CreateEncryptor(bykey, byIv), CryptoStreamMode.Write);//寫入臨時加密文件
                cs.Write(br.ReadBytes((int)fsText.Length), 0, (int)fsText.Length);//寫入加密流
                cs.FlushFinalBlock();
                cs.Flush();
                cs.Close();
                fsPic.Close();
                fsText.Close();
                fsOut.Close();
                File.Delete(textBox1.Text.TrimEnd());//冊除原文件
                File.Copy(strLinPath, textBox1.Text);//複製加密文件
                File.Delete(strLinPath);//冊除臨時文件
                MessageBox.Show("加密成功");
                pictureBox1.ImageLocation = null;
                textBox1.Text = "";
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }

        }

        private void Form2_Load(object sender, EventArgs e)
        {

        }
        //解密
        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                //圖片流
                FileStream fsPic = new FileStream(pictureBox1.ImageLocation, FileMode.Open, FileAccess.Read);
                //解密文件流
                FileStream fsOut = File.Open(textBox1.Text, FileMode.Open, FileAccess.Read);
                //初始化Key IV
                byte[] bykey = new byte[16];
                byte[] byIv = new byte[8];
                fsPic.Read(bykey, 0, 16);
                fsPic.Read(byIv, 0, 8);
                //臨時解密文件
                string strPath = textBox1.Text;//加密文件的路徑
                int intLent = strPath.LastIndexOf("\\") + 1;
                int intLong = strPath.Length;
                string strName = strPath.Substring(intLent, intLong - intLent);//要加密的文件名稱
                string strLinPath = "C:\\" + strName;//臨時解密文件路徑
                FileStream fs = new FileStream(strLinPath, FileMode.Create, FileAccess.Write);
                //開始解密
                RC2CryptoServiceProvider desc = new RC2CryptoServiceProvider();//des進行解
                CryptoStream csDecrypt = new CryptoStream(fsOut, desc.CreateDecryptor(bykey, byIv), CryptoStreamMode.Read);//讀出加密文件
                BinaryReader sr = new BinaryReader(csDecrypt);//從要加密流中讀出文件內容
                BinaryWriter sw = new BinaryWriter(fs);//寫入解密流
                sw.Write(sr.ReadBytes(Convert.ToInt32(fsOut.Length)));//
                sw.Flush();
                sw.Close();
                sr.Close();
                fs.Close();
                fsOut.Close();
                fsPic.Close();
                csDecrypt.Flush();

                File.Delete(textBox1.Text.TrimEnd());//冊除原文件
                File.Copy(strLinPath, textBox1.Text);//複製加密文件
                File.Delete(strLinPath);//冊除臨時文件
                MessageBox.Show("解密成功");
                pictureBox1.ImageLocation = null;
                textBox1.Text = "";
            }
            catch (Exception ee)
            {
                MessageBox.Show(ee.Message);
            }
        }
    }
}