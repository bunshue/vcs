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
            richTextBox1.Text += "判斷網頁是否存在\n";

            //統一資源識別碼(Uniform Resource Identifier, URI)

            Uri uri = new Uri("http://tw.yahoo.com");
            //Uri uri = new Uri("https://apod.nasa.gov/apod/image/2102/SwissAlpsMartianSky.jpg");   //fail

            WebRequest request = WebRequest.Create(uri);
            WebResponse response;
            try
            {
                response = request.GetResponse();
                richTextBox1.Text += "網頁存在\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
                richTextBox1.Text += "網頁不存在\n";
            }
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

        private void button2_Click(object sender, EventArgs e)
        {


            string str = GetContent("https://www.baidu.com/", Encoding.UTF8);

            richTextBox1.Text += "aaaaa = " + str + "\n";

            /*
            string str2 = GetContentPost("https://www.baidu.com/", "aaaaaaa", Encoding.UTF8);

            richTextBox1.Text += "bbbbb = " + str2 + "\n";
            */


        }

        string pic1 = "http://www.myson.com.tw/images/index/ad01.jpg";
        string pic2 = "http://www.myson.com.tw/images/index/ad02.jpg";
        string pic3 = "http://www.myson.com.tw/images/index/ad03.jpg";
        string pic4 = "http://www.myson.com.tw/images/index/ad04.jpg";
        string pic5 = "https://apod.nasa.gov/apod/image/2102/SwissAlpsMartianSky.jpg";  //fail
        private void button3_Click(object sender, EventArgs e)
        {
            //取得網路上的圖片並顯示

            pictureBox1.Image = ReadImageFromUrl(pic2);







        }

        private Image ReadImageFromUrl(string urlImagePath)
        {
            Uri uri = new Uri(urlImagePath);
            WebRequest request = WebRequest.Create(uri);
            Stream stream = request.GetResponse().GetResponseStream();
            Image res = Image.FromStream(stream);
            return res;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //C# 文字版瀏覽器

            HttpWebRequest httpRequest = null;
            HttpWebResponse httpResponse;

            string result = "";
            String txtURL = "https://www.google.com.tw/";
            char[] cbuffer = new char[256];
            int byteRead = 0;
            try
            {
                Uri httpURL = new Uri(txtURL);
                httpRequest = (HttpWebRequest)WebRequest.Create(httpURL);
                httpResponse = (HttpWebResponse)httpRequest.GetResponse();
                System.IO.Stream respStream = httpResponse.GetResponseStream();
                System.IO.StreamReader respStreamReader = new StreamReader(respStream);
                byteRead = respStreamReader.Read(cbuffer, 0, 256);
                while (byteRead != 0)
                {
                    string response = new string(cbuffer, 0, byteRead);
                    result = result + response;
                    byteRead = respStreamReader.Read(cbuffer, 0, 256);
                    richTextBox1.Text += response + "\n";
                }
            }
            catch (Exception)
            {

            }

        }



    }
}
