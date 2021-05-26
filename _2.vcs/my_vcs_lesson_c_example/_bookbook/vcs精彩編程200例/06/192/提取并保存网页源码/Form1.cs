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


namespace ��ȡ��������ҳԴ��
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
        public string strS;//��ȡ��ҳ����
        public void GetPageSource()
        {
            string strAddress = textBox1.Text.Trim();//������ַ
            if (ValidateDate1(strAddress))//���������ַ�Ƿ�Ϸ�
            {
                strAddress = strAddress.ToLower();
                strS = GetSource(strAddress);//���÷�����ȡ��ҳ����
                if (strS.Length > 1)
                {
                    showSource();  //���ô�����ʽ
                }
            }
            else
            {
                MessageBox.Show("������ַ����ȷ����������");
            }
        }
        //���ô�����ʽ
        private void showSource()
        {
            Form1.ActiveForm.Height = 608;
            textBox2.Text = strS;//��ʾ��ҳ����
            textBox2.Visible = true;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            char chr = e.KeyChar;
            if (chr == 13)
            {
                GetPageSource();//��ȡ��ҳ����
            }
        }
        //����
        private void button1_Click(object sender, EventArgs e)
        {
            saveFileDialog1.Filter = "�ı��ļ�|*.txt";
            if (this.saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox2.Text = this.saveFileDialog1.FileName;//
                if (this.textBox1.Text.Trim().ToString() != "")
                {
                    saveInfo(this.textBox2.Text.Trim().ToString(), this.textBox1.Text.Trim().ToString());
                    MessageBox.Show("����ɹ�");
                }
                else
                {
                    MessageBox.Show("��д��Ŀ��ҳ��URL");
                    this.textBox2.Text = string.Empty;
                }
            }
        }/// end block menthod showSource()
         //������ҳ��Ϣ
        private void saveInfo(string strPath, string strDown)
        {
            WebClient wC = new WebClient();
            wC.DownloadFile(strDown, strPath);
        }
        //��֤��ַ�Ƿ���ȷ
        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }
        //��ȡ��ҳ���ݡ�
        public string GetSource(string webAddress)
        {
            StringBuilder strSource = new StringBuilder("");
            try
            {

                WebRequest WReq = WebRequest.Create(webAddress);//��URl��ַ��������
                WebResponse WResp = WReq.GetResponse();//���ط���������Ӧ
                StreamReader sr = new StreamReader(WResp.GetResponseStream(), Encoding.ASCII);//���������ж�ȡ����
                string strTemp = "";
                while ((strTemp = sr.ReadLine()) != null)//ѭ����������
                {
                    strSource.Append(strTemp + "\r\n");//��������ӵ��ַ�����
                }
                sr.Close();
            }
            catch (WebException WebExcp)
            {
                MessageBox.Show(WebExcp.Message, "error", MessageBoxButtons.OK);
            }
            return strSource.ToString();
        }

      
    }///
}