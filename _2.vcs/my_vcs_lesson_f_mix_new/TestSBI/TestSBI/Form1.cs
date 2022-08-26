using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Windows.Forms;

using System.Text.RegularExpressions;

namespace TestSBI
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
            string keyword = GetKeyWordByImagePath(txtURL.Text);
            //MessageBox.Show(keyword);

            richTextBox1.Text += "---" + keyword + "---\n";
        }

        /// <summary>
        /// 傳入圖片網址
        /// </summary>
        /// <param name="imagePath"></param>
        /// <returns></returns>
        private string GetKeyWordByImagePath(string imagePath)
        {
            string url = String.Format("http://www.google.com/searchbyimage?hl=zh-TW&site=search&image_url=" + imagePath);

            richTextBox1.Text += "url = " + url + "\n";
            var webRequest = WebRequest.Create(url) as HttpWebRequest;

            webRequest.Method = "GET";
            webRequest.ProtocolVersion = HttpVersion.Version11;
            webRequest.UserAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1";

            var response = webRequest.GetResponse() as HttpWebResponse;
            var reader = new StreamReader(response.GetResponseStream());

            var str = reader.ReadToEnd();

            //richTextBox1.Text += "str = " + str + "\n";

            var regexId = new Regex(@"這個圖片最有可能的推測結果：(?<ID>.*?)搜尋結果", RegexOptions.IgnoreCase);

            //richTextBox1.Text += "str = " + str + "\n";

            MatchCollection mcId = regexId.Matches(str);

            richTextBox1.Text += "mcId = " + mcId + "\n";

            if (mcId.Count != 0)
            {
                return Regex.Replace(mcId[0].Groups["ID"].Value, @"<[^>]*>", String.Empty).Replace("&nbsp;", "");
            }
            else
            {
                richTextBox1.Text += "無資料\n";
                return "";
            }
        }
    }
}
