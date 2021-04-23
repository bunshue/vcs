using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.IO;
using System.Text.RegularExpressions;


namespace �����ëO�s�������X
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }///
        public string strS;//�s���������e
        public void GetPageSource()
        {
            string strAddress = textBox1.Text.Trim();//��J���}
            if (ValidateDate1(strAddress))//�ˬd��J���}�O�_�X�k
            {
                strAddress = strAddress.ToLower();
                strS = GetSource(strAddress);//�I�s��k�����������e
                if (strS.Length > 1)
                {
                    showSource();  //�]�w�����˦�
                }
            }
            else
            {
                MessageBox.Show("��J���}�����T�бq�s��J");
            }
        }
        //�]�w�����˦�
        private void showSource()
        {
            Form1.ActiveForm.Height = 608;
            textBox2.Text = strS;//��ܺ������e
            textBox2.Visible = true;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            char chr = e.KeyChar;
            if (chr == 13)
            {
                GetPageSource();//���o�����s�X
            }
        }
        //�O�s
        private void button1_Click(object sender, EventArgs e)
        {
            GetPageSource();//���o�����s�X

            string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";

            saveInfo(filename, this.textBox1.Text.Trim().ToString());
            MessageBox.Show("�O�s���\");

        }/// end block menthod showSource()

        //�O�s�����T��
        private void saveInfo(string strPath, string strDown)
        {
            WebClient wc = new WebClient();
            wc.DownloadFile(strDown, strPath);
        }

        //���Һ��}�O�_���T
        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }
        //�����������e�C
        public string GetSource(string webAddress)
        {
            StringBuilder strSource = new StringBuilder("");
            try
            {

                WebRequest WReq = WebRequest.Create(webAddress);//��URl�a�}�o�X�ШD
                WebResponse WResp = WReq.GetResponse();//�Ǧ^�A�Ⱦ����T��
                StreamReader sr = new StreamReader(WResp.GetResponseStream(), Encoding.ASCII);//�q�ƾڬy��Ū���ƾ�
                string strTemp = "";
                while ((strTemp = sr.ReadLine()) != null)//�`��Ū�X�ƾ�
                {
                    strSource.Append(strTemp + "\r\n");//��ƾڷs�W��r�ꤤ
                }
                sr.Close();
            }
            catch (WebException WebExcp)
            {
                MessageBox.Show(WebExcp.Message, "error", MessageBoxButtons.OK);
            }
            return strSource.ToString();
        }
    }
}

