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

namespace 提取網頁標題
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

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            { MessageBox.Show("請輸入網址"); return; }
            else{
                if (ValidateDate1(textBox1.Text.TrimEnd()))
                {
                    string strl;//儲存編碼
                    WebRequest wb = WebRequest.Create(textBox1.Text.Trim());//請求資源
                    WebResponse webRed = wb.GetResponse();//響應請求
                    Stream redweb = webRed.GetResponseStream();//傳回數據存入流中
                    StreamReader sr = new StreamReader(redweb, Encoding.Default);//從流中讀出數據
                    StringBuilder sb = new StringBuilder();//可變字符
                    while ((strl = sr.ReadLine()) != null)
                    {
                        sb.Append(strl);//讀出數據存入可變字符中
                    }
                    getstr(sb.ToString());//呼叫正則表達式方法讀出標題
                }
                else { MessageBox.Show("請輸入正確的網址"); return; };
            }
        }

        public void getstr(string strUrl)
        {
            string d = @"<title>(?<title>[^<]*)</title>"; 
            textBox2.Text = Regex.Match(strUrl,d).ToString();
          
        }
        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }



     


        
        
        
   
    }
}