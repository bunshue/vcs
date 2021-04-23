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


namespace 提取並保存網頁源碼
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
        public string strS;//存取網頁內容
        public void GetPageSource()
        {
            string strAddress = textBox1.Text.Trim();//輸入網址
            if (ValidateDate1(strAddress))//檢查輸入網址是否合法
            {
                strAddress = strAddress.ToLower();
                strS = GetSource(strAddress);//呼叫方法提取網頁內容
                if (strS.Length > 1)
                {
                    showSource();  //設定視窗樣式
                }
            }
            else
            {
                MessageBox.Show("輸入網址不正確請從新輸入");
            }
        }
        //設定視窗樣式
        private void showSource()
        {
            Form1.ActiveForm.Height = 608;
            textBox2.Text = strS;//顯示網頁內容
            textBox2.Visible = true;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            char chr = e.KeyChar;
            if (chr == 13)
            {
                GetPageSource();//取得網頁編碼
            }
        }
        //保存
        private void button1_Click(object sender, EventArgs e)
        {
            GetPageSource();//取得網頁編碼

            string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";

            saveInfo(filename, this.textBox1.Text.Trim().ToString());
            MessageBox.Show("保存成功");

        }/// end block menthod showSource()

        //保存網頁訊息
        private void saveInfo(string strPath, string strDown)
        {
            WebClient wc = new WebClient();
            wc.DownloadFile(strDown, strPath);
        }

        //驗證網址是否正確
        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }
        //提取網頁內容。
        public string GetSource(string webAddress)
        {
            StringBuilder strSource = new StringBuilder("");
            try
            {

                WebRequest WReq = WebRequest.Create(webAddress);//對URl地址發出請求
                WebResponse WResp = WReq.GetResponse();//傳回服務器的響應
                StreamReader sr = new StreamReader(WResp.GetResponseStream(), Encoding.ASCII);//從數據流中讀取數據
                string strTemp = "";
                while ((strTemp = sr.ReadLine()) != null)//循環讀出數據
                {
                    strSource.Append(strTemp + "\r\n");//把數據新增到字串中
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

