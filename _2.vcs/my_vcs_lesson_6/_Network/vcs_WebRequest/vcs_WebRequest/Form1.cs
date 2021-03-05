using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;       //for WebRequest
using System.IO;    //for Stream

namespace vcs_WebRequest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //統一資源識別碼(Uniform Resource Identifier, URI)

            //Uri uri = new Uri("http://tw.yahoo.com");
            Uri uri = new Uri("https://apod.nasa.gov/apod/image/2102/SwissAlpsMartianSky.jpg");


            /*
            WebRequest request = WebRequest.Create(uri);
            WebResponse response;
            try
            {
                response = request.GetResponse();
                richTextBox1.Text += "網頁存在\n";

                Stream stream = request.GetResponse().GetResponseStream();

                richTextBox1.Text += "len = " + stream.Length.ToString() + "\n";


            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
                richTextBox1.Text += "網頁不存在\n";
            }
            */

            string str = GetContent("https://www.baidu.com/", Encoding.UTF8);

            richTextBox1.Text += "aaaaa = " + str + "\n";

            /*
            string str2 = GetContentPost("https://www.baidu.com/", "aaaaaaa", Encoding.UTF8);

            richTextBox1.Text += "bbbbb = " + str2 + "\n";
            */

        }

        //GET型別
        public string GetContent(string uri, Encoding coding)
        {

            WebRequest request = WebRequest.Create(uri);	//Get請求中請求引數等直接拼接在url中
            WebResponse resp = request.GetResponse();		//返回對Internet請求的響應

            Stream stream = resp.GetResponseStream();		//從網路資源中返回資料流

            StreamReader sr = new StreamReader(stream, coding);

            string result = sr.ReadToEnd();		//將資料流轉換文字串

            stream.Close();		//關閉流資料
            sr.Close();			//關閉流資料


            return result;

        }

        //POST型別
        public string GetContentPost(string uri, string data, Encoding coding)
        {
            WebRequest request = WebRequest.Create(uri);
            request.ContentType = "application/x-www-form-urlencoded";
            request.Method = "POST";

            //將字串資料轉化為位元組串,這也是POST請求與GET請求區別的地方
            byte[] buffer = coding.GetBytes(data);

            //用於將資料寫入Internet資源
            Stream stream = request.GetRequestStream();
            stream.Write(buffer, 0, buffer.Length);
            request.ContentLength = buffer.Length;

            WebResponse response = request.GetResponse();

            //從網路資源中返回資料流
            stream = response.GetResponseStream();

            StreamReader sr = new StreamReader(stream, coding);

            //將資料流轉換文字串
            string result = sr.ReadToEnd();

            //關閉流資料
            stream.Close();
            sr.Close();

            return result;
        }





    }
}
