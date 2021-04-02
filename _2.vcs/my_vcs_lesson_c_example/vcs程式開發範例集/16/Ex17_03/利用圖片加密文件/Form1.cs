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
namespace �Q�ιϤ��[�K���
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //���}�Ϥ�
        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "jpg,bmp,gif|*.jpg|*.gif|*.bmp";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.ImageLocation = openFileDialog1.FileName;
            }
        }
        //���}�[�K���
        private void button2_Click(object sender, EventArgs e)
        {
            openFileDialog1.Filter = "��r���|*.txt";
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }
        // �[�K
        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
                if (pictureBox1.ImageLocation==null)
                { MessageBox.Show("�п�ܤ@�T�Ϥ��Ω�[�K"); return; }
                if (textBox1.Text == "")
                { MessageBox.Show("�п�ܥ[�K�����|"); return; }
                //�Ϥ��y
                FileStream fsPic = new FileStream(pictureBox1.ImageLocation, FileMode.Open, FileAccess.Read);
                //�[�K���y
                FileStream fsText = new FileStream(textBox1.Text, FileMode.Open, FileAccess.Read);
                //��l��Key IV
                byte[] bykey = new byte[16];
                byte[] byIv = new byte[8];
                fsPic.Read(bykey, 0, 16);
                fsPic.Read(byIv, 0, 8);
                //�{�ɥ[�K���
                string strPath = textBox1.Text;//�[�K��󪺸��|
                int intLent = strPath.LastIndexOf("\\") + 1;
                int intLong = strPath.Length;
                string strName = strPath.Substring(intLent, intLong - intLent);//�n�[�K�����W��
                string strLinPath = "C:\\" + strName;//�{�ɥ[�K�����|
                FileStream fsOut = File.Open(strLinPath, FileMode.Create, FileAccess.Write);
                //�}�l�[�K
                RC2CryptoServiceProvider desc = new RC2CryptoServiceProvider();//des�i��[
                BinaryReader br = new BinaryReader(fsText);//�q�n�[�K�����Ū�X��󤺮e
                CryptoStream cs = new CryptoStream(fsOut, desc.CreateEncryptor(bykey, byIv), CryptoStreamMode.Write);//�g�J�{�ɥ[�K���
                cs.Write(br.ReadBytes((int)fsText.Length), 0, (int)fsText.Length);//�g�J�[�K�y
                cs.FlushFinalBlock();
                cs.Flush();
                cs.Close();
                fsPic.Close();
                fsText.Close();
                fsOut.Close();
                File.Delete(textBox1.Text.TrimEnd());//�U������
                File.Copy(strLinPath, textBox1.Text);//�ƻs�[�K���
                File.Delete(strLinPath);//�U���{�ɤ��
                MessageBox.Show("�[�K���\");
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
        //�ѱK
        private void button4_Click(object sender, EventArgs e)
        {
            try
            {
                //�Ϥ��y
                FileStream fsPic = new FileStream(pictureBox1.ImageLocation, FileMode.Open, FileAccess.Read);
                //�ѱK���y
                FileStream fsOut = File.Open(textBox1.Text, FileMode.Open, FileAccess.Read);
                //��l��Key IV
                byte[] bykey = new byte[16];
                byte[] byIv = new byte[8];
                fsPic.Read(bykey, 0, 16);
                fsPic.Read(byIv, 0, 8);
                //�{�ɸѱK���
                string strPath = textBox1.Text;//�[�K��󪺸��|
                int intLent = strPath.LastIndexOf("\\") + 1;
                int intLong = strPath.Length;
                string strName = strPath.Substring(intLent, intLong - intLent);//�n�[�K�����W��
                string strLinPath = "C:\\" + strName;//�{�ɸѱK�����|
                FileStream fs = new FileStream(strLinPath, FileMode.Create, FileAccess.Write);
                //�}�l�ѱK
                RC2CryptoServiceProvider desc = new RC2CryptoServiceProvider();//des�i���
                CryptoStream csDecrypt = new CryptoStream(fsOut, desc.CreateDecryptor(bykey, byIv), CryptoStreamMode.Read);//Ū�X�[�K���
                BinaryReader sr = new BinaryReader(csDecrypt);//�q�n�[�K�y��Ū�X��󤺮e
                BinaryWriter sw = new BinaryWriter(fs);//�g�J�ѱK�y
                sw.Write(sr.ReadBytes(Convert.ToInt32(fsOut.Length)));//
                sw.Flush();
                sw.Close();
                sr.Close();
                fs.Close();
                fsOut.Close();
                fsPic.Close();
                csDecrypt.Flush();

                File.Delete(textBox1.Text.TrimEnd());//�U������
                File.Copy(strLinPath, textBox1.Text);//�ƻs�[�K���
                File.Delete(strLinPath);//�U���{�ɤ��
                MessageBox.Show("�ѱK���\");
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