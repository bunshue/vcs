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

//統一資源識別碼(Uniform Resource Identifier, URI)

namespace vcs_WebRequest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "當前下載進度 " + 0.ToString("00.00") + " %";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            richTextBox1.Text += "判斷網頁是否存在......\n";

            Uri uri = new Uri("http://tw.yahoo.com");
            //Uri uri = new Uri("https://apod.nasa.gov/apod/image/2102/SwissAlpsMartianSky.jpg");   //fail

            WebRequest request = WebRequest.Create(uri);

            try
            {
                WebResponse response = request.GetResponse();
                richTextBox1.Text += "網頁存在\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
                richTextBox1.Text += "網頁不存在\n";
            }
            this.Cursor = Cursors.Default;
        }

        //GET型別
        public string GetContent(string uri, Encoding coding)
        {

            WebRequest request = WebRequest.Create(uri);	//Get請求中請求引數等直接拼接在url中

            string result = "";
            try
            {
                WebResponse response = request.GetResponse();		//返回對Internet請求的響應

                Stream stream = response.GetResponseStream();		//從網路資源中返回資料流

                StreamReader sr = new StreamReader(stream, coding);

                result = sr.ReadToEnd();		//將資料流轉換文字串

                stream.Close();		//關閉流資料
                sr.Close();			//關閉流資料
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
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

            string result = "";
            try
            {
                WebResponse response = request.GetResponse();

                //從網路資源中返回資料流
                stream = response.GetResponseStream();

                StreamReader sr = new StreamReader(stream, coding);

                //將資料流轉換文字串
                result = sr.ReadToEnd();

                //關閉流資料
                stream.Close();
                sr.Close();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            return result;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;

            string str = GetContent("https://www.baidu.com/", Encoding.UTF8);

            richTextBox1.Text += "aaaaa = " + str + "\n";

            /*
            string str2 = GetContentPost("https://www.baidu.com/", "aaaaaaa", Encoding.UTF8);

            richTextBox1.Text += "bbbbb = " + str2 + "\n";
            */

            this.Cursor = Cursors.Default;
        }

        string pic1 = "http://www.myson.com.tw/images/index/ad01.jpg";
        string pic2 = "http://www.myson.com.tw/images/index/ad02.jpg";
        string pic3 = "http://www.myson.com.tw/images/index/ad03.jpg";
        string pic4 = "http://www.myson.com.tw/images/index/ad04.jpg";
        string pic5 = "https://apod.nasa.gov/apod/image/2102/SwissAlpsMartianSky.jpg";  //fail
        private void button3_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            //取得網路上的圖片並顯示
            pictureBox1.Image = ReadImageFromUrl(pic2);
            this.Cursor = Cursors.Default;
        }

        private Image ReadImageFromUrl(string url)
        {
            Uri uri = new Uri(url);
            WebRequest request = WebRequest.Create(uri);
            Image res = null;

            try
            {
                WebResponse response = request.GetResponse();
                Stream stream = response.GetResponseStream();
                res = Image.FromStream(stream);
            }
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            return res;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            //C# 文字版瀏覽器

            HttpWebRequest httpRequest = null;
            HttpWebResponse httpResponse;

            string result = "";
            String url = "https://www.google.com.tw/";
            char[] cbuffer = new char[256];
            int byteRead = 0;
            try
            {
                Uri uri = new Uri(url);
                httpRequest = (HttpWebRequest)WebRequest.Create(uri);
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
            catch (Exception ex)
            {
                richTextBox1.Text += ex.Message + "\n";
            }
            this.Cursor = Cursors.Default;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;
            string result = null;
            string Url = "http://easun.org/perl/perl-toc/ch04.html";
            HttpWebRequest request = HttpWebRequest.Create(Url) as HttpWebRequest;
            request.Method = "GET";

            using (WebResponse response = request.GetResponse())
            {
                StreamReader sr = new StreamReader(response.GetResponseStream());
                result = sr.ReadToEnd();        //讀取所有文字內容
                sr.Close();
            }
            richTextBox1.Text += result + "\n";
            this.Cursor = Cursors.Default;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            this.Cursor = Cursors.WaitCursor;

            //要取得的網址
            Uri uri = new Uri("http://easun.org/perl/perl-toc/ch04.html");

            //建立request
            HttpWebRequest request = (HttpWebRequest)HttpWebRequest.Create(uri);

            //在request Header加入認證字串
            request.Headers.Add("Authorization", "Basic " + Convert.ToBase64String(new ASCIIEncoding().GetBytes("admin:admin")));

            //實際發送請求，並取回回應資訊
            HttpWebResponse response = (HttpWebResponse)request.GetResponse();

            //建立讀取串流
            StreamReader reader = new StreamReader(response.GetResponseStream());

            //將串流轉字串
            string tmp = reader.ReadToEnd();	//讀取所有文字內容

            //關閉連線
            response.Close();

            //顯示回應資訊
            richTextBox1.Text += tmp + "\n";

            this.Cursor = Cursors.Default;
        }


        //下載http文件 並顯示進度條 ST
        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "下載http文件 並顯示進度條\n";
            Application.DoEvents();

            string url = "http://weisico.com/program/2015/0630/237.html";
            //string filename = @"D:\_git\vcs\_1.data\______test_files1\aaaaaaaa.html";
            string filename = Application.StartupPath + "\\" + "aaaaaaaa.html";

            DownloadFile_percentage(url, filename);

            richTextBox1.Text += "下載完畢, 檔案 : " + filename + "\n";
        }

        /// <summary>
        /// c#,.net 下载文件
        /// </summary>
        /// <param name="URL">下载文件地址</param>
        ///
        /// <param name="Filename">下载后的存放地址</param>
        /// <param name="Prog">用于显示的进度条</param>
        ///
        public void DownloadFile_percentage(string URL, string filename)
        {
            if (URL == "")
            {
                MessageBox.Show("URL为空", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return;
            }
            float percent = 0;
            label1.Text = "當前下載進度 " + percent.ToString("00.00") + " %";
            Application.DoEvents();

            try
            {
                HttpWebRequest Myrq = (HttpWebRequest)HttpWebRequest.Create(URL);
                HttpWebResponse myrp = (HttpWebResponse)Myrq.GetResponse();
                long totalBytes = myrp.ContentLength;
                if (progressBar1 != null)
                {
                    progressBar1.Maximum = (int)totalBytes;
                }
                Stream st = myrp.GetResponseStream();
                Stream so = new FileStream(filename, FileMode.Create);
                long totalDownloadedByte = 0;
                byte[] by = new byte[1024];
                int osize = st.Read(by, 0, (int)by.Length);
                while (osize > 0)
                {
                    totalDownloadedByte = osize + totalDownloadedByte;
                    Application.DoEvents();
                    so.Write(by, 0, osize);
                    if (progressBar1 != null)
                    {
                        progressBar1.Value = (int)totalDownloadedByte;
                    }
                    osize = st.Read(by, 0, (int)by.Length);

                    percent = (float)totalDownloadedByte / (float)totalBytes * 100;
                    label1.Text = "當前下載進度 " + percent.ToString("00.00") + " %";
                    Application.DoEvents(); //必须加注这句代码，否则label1将因为循环执行太快而来不及显示信息
                    if (percent == 100)
                    {
                        MessageBox.Show("下载完成", "消息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                so.Close();
                st.Close();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "Error\t" + ex.Message + "\n";
            }
        }
        //下載http文件 並顯示進度條 SP




    }
}
