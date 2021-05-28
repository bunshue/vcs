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


namespace 提取并保存网页源码
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
        public string strS;//存取网页内容
        public void GetPageSource()
        {
            string strAddress = textBox1.Text.Trim();//输入网址
            if (ValidateDate1(strAddress))//检查输入网址是否合法
            {
                strAddress = strAddress.ToLower();
                strS = GetSource(strAddress);//调用方法提取网页内容
                if (strS.Length > 1)
                {
                    showSource();  //设置窗体样式
                }
            }
            else
            {
                MessageBox.Show("输入网址不正确请重新输入");
            }
        }
        //设置窗体样式
        private void showSource()
        {
            Form1.ActiveForm.Height = 608;
            textBox2.Text = strS;//显示网页内容
            textBox2.Visible = true;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            char chr = e.KeyChar;
            if (chr == 13)
            {
                GetPageSource();//获取网页编码
            }
        }
        //保存
        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";

            this.textBox2.Text = filename;
            if (this.textBox1.Text.Trim().ToString() != "")
            {
                saveInfo(this.textBox2.Text.Trim().ToString(), this.textBox1.Text.Trim().ToString());
                MessageBox.Show("保存成功");
            }
            else
            {
                MessageBox.Show("请写入目标页的URL");
                this.textBox2.Text = string.Empty;
            }
        }/// end block menthod showSource()
        //保存网页信息
        private void saveInfo(string strPath, string strDown)
        {
            WebClient wC = new WebClient();
            wC.DownloadFile(strDown, strPath);
        }
        //验证网址是否正确
        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }
        //提取网页内容。
        public string GetSource(string webAddress)
        {
            StringBuilder strSource = new StringBuilder("");
            try
            {

                WebRequest WReq = WebRequest.Create(webAddress);//对URl地址发出请求
                WebResponse WResp = WReq.GetResponse();//返回服务器的响应
                StreamReader sr = new StreamReader(WResp.GetResponseStream(), Encoding.ASCII);//从数据流中读取数据
                string strTemp = "";
                while ((strTemp = sr.ReadLine()) != null)//循环读出数据
                {
                    strSource.Append(strTemp + "\r\n");//把数据添加到字符串中
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