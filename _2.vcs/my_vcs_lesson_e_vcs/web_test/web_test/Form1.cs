using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;

namespace web_test
{
    public partial class Form1 : Form
    {
        DataTable dt = new DataTable();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //要抓取的URL地址
            string Url = "http://list.mp3.baidu.com/topso/mp3topsong.html?id=1#top2";
            //得到指定Url的源码
            string strWebContent = GetWebContent(Url);
            richTextBox1.Text = strWebContent;
            //取出和数据有关的那段源码
            int iBodyStart = strWebContent.IndexOf("<body", 0);
            int iStart = strWebContent.IndexOf("歌曲TOP500", iBodyStart);
            int iTableStart = strWebContent.IndexOf("<table", iStart);
            int iTableEnd = strWebContent.IndexOf("</table>", iTableStart);
            string strWeb = strWebContent.Substring(iTableStart, iTableEnd - iTableStart + 8);
            //生成HtmlDocument
            WebBrowser webb = new WebBrowser();
            webb.Navigate("about:blank");
            HtmlDocument htmldoc = webb.Document.OpenNew(true);
            htmldoc.Write(strWeb);
            HtmlElementCollection htmlTR = htmldoc.GetElementsByTagName("TR");
            foreach (HtmlElement tr in htmlTR)
            {
                string strID = tr.GetElementsByTagName("TD")[0].InnerText;
                //string strName = SplitName(tr.GetElementsByTagName("TD")[1].InnerText, "MusicName");
                //string strSinger = SplitName(tr.GetElementsByTagName("TD")[1].InnerText, "Singer");
                strID = strID.Replace(".", "");
                //插入DataTable
                //AddLine(strID, strName, strSinger, "0");

                string strID1 = tr.GetElementsByTagName("TD")[2].InnerText;
                //string strName1 = SplitName(tr.GetElementsByTagName("TD")[3].InnerText, "MusicName");
                //string strSinger1 = SplitName(tr.GetElementsByTagName("TD")[3].InnerText, "Singer");
                //插入DataTable
                strID1 = strID1.Replace(".", "");
                //AddLine(strID1, strName1, strSinger1, "0");
                string strID2 = tr.GetElementsByTagName("TD")[4].InnerText;
                //string strName2 = SplitName(tr.GetElementsByTagName("TD")[5].InnerText, "MusicName");
                //string strSinger2 = SplitName(tr.GetElementsByTagName("TD")[5].InnerText, "Singer");
                //插入DataTable
                strID2 = strID2.Replace(".", "");
                //AddLine(strID2, strName2, strSinger2, "0");
            }
            //插入数据库
            //InsertData(dt);

            dataGridView1.DataSource = dt.DefaultView;

        }

        //根据Url地址得到网页的html源码
        private string GetWebContent(string Url)
        {
            string strResult = "";
            try
            {
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(Url);
                //声明一个HttpWebRequest请求
                request.Timeout = 30000;
                //设置连接超时时间
                request.Headers.Set("Pragma", "no-cache");
                HttpWebResponse response = (HttpWebResponse)request.GetResponse();
                Stream streamReceive = response.GetResponseStream();
                Encoding encoding = Encoding.GetEncoding("GB2312");
                StreamReader streamReader = new StreamReader(streamReceive, encoding);
                strResult = streamReader.ReadToEnd();
            }
            catch
            {
                MessageBox.Show("出错");
            }
            return strResult;
        }

    }

    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

}
